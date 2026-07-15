#!/usr/bin/env python3
"""Robot manager ROS 2 node.

The single supervisory node for the Tortugabot stack. It owns the full
mission lifecycle (see ``lifecycle.py``) and exposes the web dashboard.

It deliberately talks only to interfaces that already exist in this
workspace, so no teammate node needs to change:

Subscribes
    /pose             geometry_msgs/PoseStamped  robot localization
    /map              nav_msgs/OccupancyGrid     SLAM map (slam_toolbox)
    /scan             sensor_msgs/LaserScan      LiDAR heartbeat
    /slam_confidence  std_msgs/String (JSON)     SLAM analyzer metrics
    /planned_path     nav_msgs/Path              planner output (navigation2)
    /base/cmd_vel     geometry_msgs/Twist        motor command heartbeat

Publishes
    /goal_pose            geometry_msgs/PoseStamped  navigation goal
    /mapping_finished     std_msgs/Bool              signals SLAM analyzer
    /robot_manager/state  std_msgs/String (JSON)     full manager state

Service clients
    /slam_toolbox/save_map  slam_toolbox/srv/SaveMap

While ESTOPPED or FAULTed the node streams zero velocities on
/base/cmd_vel to override any stale motion commands.
"""

import base64
import json
import math
import subprocess
import time

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    DurabilityPolicy, QoSProfile, ReliabilityPolicy,
)

from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import OccupancyGrid, Path
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool, String

from .dashboard_server import DashboardServer
from .health_monitor import HealthMonitor
from .lifecycle import RobotEvent, RobotLifecycle, RobotState
from .slam_metrics import SlamMetrics
from .task_manager import TASK_FOLLOW_RED, TASK_NAVIGATE, TaskManager

try:
    from slam_toolbox.srv import SaveMap
    HAVE_SLAM_TOOLBOX = True
except ImportError:
    HAVE_SLAM_TOOLBOX = False


class RobotManagerNode(Node):
    GOAL_TOLERANCE = 0.15      # m; slightly looser than navigation2's 0.10
    NAV_TIMEOUT = 300.0        # s
    DASHBOARD_PORT = 8765

    def __init__(self):
        super().__init__('robot_manager')

        self.declare_parameter('dashboard_port', self.DASHBOARD_PORT)
        self.declare_parameter('assume_map_available', False)
        self.declare_parameter('map_save_name', 'auto_map')

        self.lifecycle = RobotLifecycle()
        self.health = HealthMonitor()
        self.tasks = TaskManager()
        self.slam = SlamMetrics(convergence_threshold=0.97, hold_seconds=5.0)

        self.health.add_component('scan', 'LiDAR /scan', 10.0, 1.5, 4.0, critical=True)
        self.health.add_component('pose', 'Localization /pose', 10.0, 1.5, 4.0, critical=True)
        self.health.add_component('map', 'SLAM map /map', 0.5, 8.0, 20.0)
        self.health.add_component('slam_confidence', 'SLAM analyzer', 0.5, 8.0, 20.0)
        # planner and motors are event-driven: they only publish while a task
        # runs, so silence is not a failure (they never WARN/DOWN on age).
        self.health.add_component('planner', 'Planner /planned_path', 0.0, 1e9, 2e9)
        self.health.add_component('motors', 'Motor cmd /base/cmd_vel', 0.0, 1e9, 2e9)

        # Robot / navigation state
        self.x = self.y = self.yaw = 0.0
        self.has_pose = False
        self.goal = None
        self.nav_started = None
        self.nav_initial_distance = None
        self.planned_path = []
        self.estopped = False
        self.map_saved = bool(self.get_parameter('assume_map_available').value)
        self._boot_time = time.time()
        self._save_in_flight = False
        self._follow_red_proc = None   # subprocess running the follow_red pipeline

        # Latest map payload for the dashboard
        self.map_version = 0
        self._map_msg = None

        # --- subscriptions -------------------------------------------------
        transient = QoSProfile(depth=1,
                               reliability=ReliabilityPolicy.RELIABLE,
                               durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.create_subscription(PoseStamped, '/pose', self._on_pose, 10)
        self.create_subscription(OccupancyGrid, '/map', self._on_map, transient)
        self.create_subscription(LaserScan, '/scan', self._on_scan, 10)
        self.create_subscription(String, '/slam_confidence', self._on_confidence, 10)
        self.create_subscription(Path, '/planned_path', self._on_path, transient)
        self.create_subscription(Twist, '/base/cmd_vel', self._on_cmd_vel, 10)

        # --- publishers ------------------------------------------------------
        self.goal_pub = self.create_publisher(PoseStamped, '/goal_pose', 1)
        self.mapping_finished_pub = self.create_publisher(Bool, '/mapping_finished', 1)
        self.state_pub = self.create_publisher(String, '/robot_manager/state', 1)
        self.cmd_pub = self.create_publisher(Twist, '/base/cmd_vel', 1)

        if HAVE_SLAM_TOOLBOX:
            self.save_map_client = self.create_client(SaveMap, '/slam_toolbox/save_map')
        else:
            self.save_map_client = None
            self.get_logger().warning(
                'slam_toolbox not available - map saving will be skipped')

        self.create_timer(0.2, self._tick)
        self.create_timer(1.0, self._publish_state)

        port = int(self.get_parameter('dashboard_port').value)
        self.dashboard = DashboardServer(self, port=port)
        self.dashboard.start_background()
        self.get_logger().info(
            'Robot manager started; dashboard on http://0.0.0.0:%d' % port)

    # ------------------------------------------------------------------
    # Subscriptions
    # ------------------------------------------------------------------
    def _on_pose(self, msg):
        self.x = msg.pose.position.x
        self.y = msg.pose.position.y
        q = msg.pose.orientation
        self.yaw = math.atan2(2.0 * (q.w * q.z + q.x * q.y),
                              1.0 - 2.0 * (q.y * q.y + q.z * q.z))
        self.has_pose = True
        self.health.beat('pose')

    def _on_map(self, msg):
        self._map_msg = msg
        self.map_version += 1
        self.health.beat('map')

    def _on_scan(self, _msg):
        self.health.beat('scan')

    def _on_confidence(self, msg):
        try:
            data = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().warning('bad JSON on /slam_confidence')
            return
        self.health.beat('slam_confidence')
        converged = self.slam.update(
            confidence=float(data.get('confidence', 0.0)),
            frontier_ratio=data.get('frontier_ratio'),
            unknown_ratio=data.get('unknown_ratio'),
            growth_ratio=data.get('growth_ratio'),
        )
        if self.lifecycle.state == RobotState.MAPPING:
            self.tasks.update_progress(
                self.slam.latest['confidence'],
                'confidence {:.1%}'.format(self.slam.latest['confidence']))
            if converged:
                self.lifecycle.handle(RobotEvent.SLAM_CONVERGED)
                self._request_map_save()

    def _on_path(self, msg):
        self.planned_path = [
            [pose.pose.position.x, pose.pose.position.y] for pose in msg.poses]
        if msg.poses:
            self.health.beat('planner')

    def _on_cmd_vel(self, _msg):
        self.health.beat('motors')

    # ------------------------------------------------------------------
    # Lifecycle tick
    # ------------------------------------------------------------------
    def _tick(self):
        now = time.time()
        state = self.lifecycle.state

        if state == RobotState.BOOT:
            self.lifecycle.handle(RobotEvent.START)
            return

        if self.estopped or state in (RobotState.ESTOPPED, RobotState.FAULT):
            # Actively command zero velocity to stop the base.
            self.cmd_pub.publish(Twist())

        failure = self.health.critical_failure(now)
        if failure and state not in (RobotState.FAULT, RobotState.ESTOPPED):
            self.get_logger().error('critical fault: %s is down' % failure)
            self.lifecycle.handle(RobotEvent.CRITICAL_FAULT, note=failure)
            if self.tasks.busy:
                self.tasks.fail('critical fault: {} lost'.format(failure))
            self._stop_follow_red()
            self._clear_navigation()
            return

        if state == RobotState.FAULT:
            if self.health.all_critical_ok(now):
                self.get_logger().info('critical sensors recovered')
                self.lifecycle.handle(RobotEvent.FAULT_CLEARED)
            return

        if state == RobotState.ESTOPPED:
            return

        if state == RobotState.INITIALIZING:
            if self.health.all_critical_ok(now) and now - self._boot_time > 2.0:
                if self.map_saved:
                    self.lifecycle.handle(RobotEvent.SENSORS_READY_MAP_AVAILABLE)
                else:
                    self.lifecycle.handle(RobotEvent.SENSORS_READY_MAP_MISSING)
                    from .task_manager import TASK_MAP
                    self.tasks.start(TASK_MAP)
            return

        if state == RobotState.EXECUTING:
            self._tick_navigation(now)
            self._tick_follow_red(now)

    def _tick_follow_red(self, now):
        if not self.tasks.busy or self.tasks.active.type != TASK_FOLLOW_RED:
            return
        proc = self._follow_red_proc
        if proc is None or proc.poll() is not None:
            # Pipeline is gone (crashed or was never started properly).
            self._follow_red_proc = None
            self.tasks.fail('follow_red pipeline stopped unexpectedly')
            self.lifecycle.handle(RobotEvent.TASK_FINISHED)
            return
        elapsed = now - (self.tasks.active.started or now)
        self.tasks.update_progress(
            0.0, 'following the red cube · {:.0f}s'.format(elapsed))

    def _stop_follow_red(self):
        proc = self._follow_red_proc
        self._follow_red_proc = None
        if proc is None or proc.poll() is not None:
            return
        try:
            proc.terminate()
            try:
                proc.wait(timeout=3.0)
            except subprocess.TimeoutExpired:
                proc.kill()
        except Exception as error:
            self.get_logger().warning(
                'failed to stop follow_red pipeline: %s' % error)

    def _tick_navigation(self, now):
        if not self.tasks.busy or self.tasks.active.type != TASK_NAVIGATE:
            return
        if self.goal is None:
            self._finish_task(False, 'goal lost')
            return
        if self.nav_started and now - self.nav_started > self.NAV_TIMEOUT:
            self._finish_task(False, 'navigation timed out')
            return
        if not self.has_pose:
            return
        remaining = math.hypot(self.goal[0] - self.x, self.goal[1] - self.y)
        if remaining <= self.GOAL_TOLERANCE:
            self._finish_task(True, 'goal reached')
            return
        if self.nav_initial_distance:
            self.tasks.update_progress(
                1.0 - remaining / self.nav_initial_distance,
                '{:.2f} m to goal'.format(remaining))

    def _finish_task(self, success, detail):
        if success:
            self.tasks.succeed(detail)
        else:
            self.tasks.fail(detail)
        self._clear_navigation()
        self.lifecycle.handle(RobotEvent.TASK_FINISHED)

    def _clear_navigation(self):
        self.goal = None
        self.nav_started = None
        self.nav_initial_distance = None

    # ------------------------------------------------------------------
    # Map saving
    # ------------------------------------------------------------------
    def _request_map_save(self):
        if self.save_map_client is None:
            # No slam_toolbox: consider the in-memory map good enough.
            self._on_map_saved(True, 'slam_toolbox unavailable, map kept in memory')
            return
        if self._save_in_flight:
            return
        if not self.save_map_client.wait_for_service(timeout_sec=2.0):
            self._on_map_saved(False, '/slam_toolbox/save_map unavailable')
            return
        self._save_in_flight = True
        request = SaveMap.Request()
        request.name = String()
        request.name.data = '{}_{}'.format(
            self.get_parameter('map_save_name').value, int(time.time()))
        future = self.save_map_client.call_async(request)
        future.add_done_callback(self._on_save_response)

    def _on_save_response(self, future):
        self._save_in_flight = False
        try:
            response = future.result()
            success = response.result == SaveMap.Response.RESULT_SUCCESS
            self._on_map_saved(success, 'save_map result: {}'.format(response.result))
        except Exception as error:
            self._on_map_saved(False, 'save_map call failed: {}'.format(error))

    def _on_map_saved(self, success, detail):
        if success:
            self.map_saved = True
            self.mapping_finished_pub.publish(Bool(data=True))
            self.lifecycle.handle(RobotEvent.MAP_SAVED, note=detail)
            self.tasks.succeed(detail)
            self.get_logger().info('map saved: %s' % detail)
        else:
            self.lifecycle.handle(RobotEvent.MAP_SAVE_FAILED, note=detail)
            self.slam.reset_convergence()
            self.get_logger().error('map save failed: %s' % detail)

    # ------------------------------------------------------------------
    # State publication
    # ------------------------------------------------------------------
    def _publish_state(self):
        self.state_pub.publish(String(data=json.dumps(self.state())))

    # ------------------------------------------------------------------
    # Dashboard backend contract
    # ------------------------------------------------------------------
    def state(self):
        now = time.time()
        return {
            'time': now,
            'mode': 'ros',
            'map_name': 'live /map',
            'robot': {
                'x': round(self.x, 3),
                'y': round(self.y, 3),
                'yaw': round(self.yaw, 3),
                'speed': None,
                'frame': 'map',
                'has_pose': self.has_pose,
            },
            'lifecycle': self.lifecycle.snapshot(),
            'health': self.health.snapshot(now),
            'task': self.tasks.snapshot(),
            'slam': self.slam.snapshot(),
            'nav': {
                'state': 'tracking' if self.goal else 'idle',
                'goal': ({'x': self.goal[0], 'y': self.goal[1]}
                         if self.goal else None),
                'cube': None,  # cube pose is camera-relative on the robot
                'path': [[round(px, 3), round(py, 3)]
                         for px, py in self.planned_path[:400]],
            },
            'estopped': self.estopped,
            'injected_faults': [],
            'map_version': self.map_version,
        }

    def map_payload(self):
        msg = self._map_msg
        if msg is None:
            return {'version': 0, 'width': 0, 'height': 0, 'resolution': 0.05,
                    'origin_x': 0.0, 'origin_y': 0.0, 'data_b64': ''}
        raw = bytearray(len(msg.data))
        for idx, value in enumerate(msg.data):
            if value < 0:
                raw[idx] = 255
            elif value >= 50:
                raw[idx] = 100
            else:
                raw[idx] = 0
        return {
            'version': self.map_version,
            'width': msg.info.width,
            'height': msg.info.height,
            'resolution': msg.info.resolution,
            'origin_x': msg.info.origin.position.x,
            'origin_y': msg.info.origin.position.y,
            'data_b64': base64.b64encode(bytes(raw)).decode('ascii'),
        }

    def command(self, payload):
        action = payload.get('action')

        if action == 'navigate':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False,
                        'error': 'robot not READY (state: {})'.format(
                            self.lifecycle.state.value)}
            x, y = float(payload['x']), float(payload['y'])
            task = self.tasks.start(TASK_NAVIGATE, {'x': x, 'y': y})
            if task is None:
                return {'ok': False, 'error': 'another task is active'}
            goal = PoseStamped()
            goal.header.frame_id = 'map'
            goal.header.stamp = self.get_clock().now().to_msg()
            goal.pose.position.x = x
            goal.pose.position.y = y
            goal.pose.orientation.w = 1.0
            self.goal_pub.publish(goal)
            self.goal = (x, y)
            self.nav_started = time.time()
            self.nav_initial_distance = max(
                0.001, math.hypot(x - self.x, y - self.y))
            self.lifecycle.handle(RobotEvent.TASK_STARTED)
            return {'ok': True, 'task_id': task.id}

        if action == 'follow_red':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False,
                        'error': 'robot not READY (state: {})'.format(
                            self.lifecycle.state.value)}
            task = self.tasks.start(TASK_FOLLOW_RED)
            if task is None:
                return {'ok': False, 'error': 'another task is active'}
            # Start the existing follow_red pipeline (camera tracker +
            # collision avoidance). It publishes /target_vector and drives
            # the base until it is cancelled.
            try:
                self._follow_red_proc = subprocess.Popen(
                    ['ros2', 'launch', 'follow_red',
                     'follow_red_with_avoidance.launch.py'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except OSError as error:
                self.tasks.fail('could not start follow_red: {}'.format(error))
                return {'ok': False,
                        'error': 'could not start follow_red: {}'.format(error)}
            self.tasks.update_progress(0.0, 'starting red cube tracking…')
            self.lifecycle.handle(RobotEvent.TASK_STARTED)
            self.get_logger().info('follow_red pipeline started (pid %d)'
                                   % self._follow_red_proc.pid)
            return {'ok': True, 'task_id': task.id}

        if action == 'cancel':
            if not self.tasks.busy:
                return {'ok': False, 'error': 'no active task'}
            was_follow_red = self.tasks.active.type == TASK_FOLLOW_RED
            self.tasks.cancel()
            if was_follow_red:
                self._stop_follow_red()
                # Command zero velocity so the base stops immediately.
                self.cmd_pub.publish(Twist())
            if self.goal is not None and self.has_pose:
                # navigation2 has no cancel interface: retarget the goal to
                # the robot's current position so it stops immediately.
                stop = PoseStamped()
                stop.header.frame_id = 'map'
                stop.header.stamp = self.get_clock().now().to_msg()
                stop.pose.position.x = self.x
                stop.pose.position.y = self.y
                stop.pose.orientation.w = 1.0
                self.goal_pub.publish(stop)
            self._clear_navigation()
            if self.lifecycle.state == RobotState.EXECUTING:
                self.lifecycle.handle(RobotEvent.TASK_FINISHED)
            elif self.lifecycle.state in (RobotState.MAPPING,
                                          RobotState.SAVING_MAP):
                # Operator accepts the current map instead of converging.
                self.map_saved = True
                self.mapping_finished_pub.publish(Bool(data=True))
                self.lifecycle.handle(RobotEvent.MAPPING_CANCELLED)
            return {'ok': True}

        if action == 'estop':
            engage = bool(payload.get('engage', True))
            if engage and not self.estopped:
                self.estopped = True
                if self.tasks.busy:
                    self.tasks.fail('emergency stop')
                self._stop_follow_red()
                self._clear_navigation()
                self.lifecycle.handle(RobotEvent.ESTOP_PRESSED)
                self.cmd_pub.publish(Twist())
            elif not engage and self.estopped:
                self.estopped = False
                self.lifecycle.handle(RobotEvent.ESTOP_RELEASED)
            return {'ok': True, 'estopped': self.estopped}

        if action == 'remap':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False, 'error': 'robot not READY'}
            from .task_manager import TASK_MAP
            self.map_saved = False
            self.slam.reset_convergence()
            self.tasks.start(TASK_MAP)
            self.lifecycle.handle(RobotEvent.REMAP_REQUESTED)
            return {'ok': True}

        if action in ('explore', 'inject_fault'):
            return {'ok': False,
                    'error': '{} is only available in sim mode'.format(action)}

        return {'ok': False, 'error': 'unknown action: {}'.format(action)}


def main(args=None):
    rclpy.init(args=args)
    node = RobotManagerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node._stop_follow_red()
            node.dashboard.shutdown()
            node.destroy_node()
        except Exception:
            pass
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
