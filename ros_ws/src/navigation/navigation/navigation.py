from collections import deque
import heapq
import json
import math

from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Path
from std_msgs.msg import String
import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import ReliabilityPolicy
from tf2_ros import Buffer, TransformListener


class Navigation(Node):
    STATUS_HEARTBEAT_SEC = 2.0
    TF_MAP_FRAME = 'map'
    TF_ROBOT_FRAME = 'base_footprint'
    TURN_IN_PLACE_THRESHOLD = math.pi / 3.0

    def __init__(self):
        super().__init__('navigation')

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.has_pose = False
        self.last_pose_time = None

        self.env_map = []
        self.obstacle_distance_map = []
        self.map_width = 0
        self.map_height = 0
        self.map_resolution = 0.0
        self.map_origin_x = 0.0
        self.map_origin_y = 0.0
        self.has_map = False

        self.goal_x = 0.0
        self.goal_y = 0.0
        self.has_goal = False
        self.last_goal_time = None

        # FIFO queue for tracking waypoints.
        self.goal_queue = deque()
        self.last_received_goal = None
        self.MIN_GOAL_SPACING = 0.25
        self.MAX_GOAL_QUEUE_SIZE = 100

        self.path = []
        self.path_grid = []
        self.path_progress = 0.0
        self.last_planned_start = None
        self.last_planned_goal = None

        self.state = 'idle'
        self.blocking_reason = 'none'
        self.tf_ok = False
        self.tf_map_frame = self.TF_MAP_FRAME
        self.tf_robot_frame = self.TF_ROBOT_FRAME
        self.tf_error = 'not_checked'
        self._last_status_signature = None
        self._last_status_log_time = None
        self._last_planning_context = None

        self.OCCUPIED_THRESHOLD = 50
        # Clearance is measured from the robot center on the planning grid.
        self.ROBOT_CLEARANCE_RADIUS = 0.40
        self.GOAL_TOLERANCE = 0.10
        self.LOOKAHEAD_DISTANCE = 0.40
        self.OFF_PATH_REPLAN_DISTANCE_CELLS = 2
        self.LINEAR_SPEED = 0.11
        self.MAX_ANGULAR_SPEED = 0.45

        planned_path_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
        )
        self.path_publisher = self.create_publisher(
            Path,
            '/planned_path',
            planned_path_qos,
        )

        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            1
        )

        self.pos_subscription = self.create_subscription(
            PoseStamped,
            '/pose',
            self.pos_callback,
            1
        )

        self.goal_pose_subscription = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_pose_callback,
            1
        )

        self.publisher = self.create_publisher(TargetVector, '/target_vector', 1)

        status_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
        )
        self.status_publisher = self.create_publisher(
            String,
            '/navigation_status',
            status_qos,
        )

        self.timer = self.create_timer(0.2, self.timer_callback)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.tf_timer = self.create_timer(0.1, self.get_tf)
        self.log_status(force=True)

    def get_tf(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                self.tf_map_frame,
                self.tf_robot_frame,
                rclpy.time.Time(),
            )
            self.tf_ok = True
            self.tf_error = 'none'
            self.x = transform.transform.translation.x
            self.y = transform.transform.translation.y
            self.yaw = self.yaw_from_quaternion(
                transform.transform.rotation
            )
            self.has_pose = True
            self.last_pose_time = self.now_seconds()
        except Exception as error:
            new_failure = self.tf_ok or self.tf_error == 'not_checked'
            self.tf_ok = False
            self.tf_error = self.sanitize_error(error)
            if new_failure:
                self.log_status(force=True, warning=True)

    def sanitize_error(self, error):
        return ' '.join(str(error).split()) or error.__class__.__name__

    def now_seconds(self):
        return self.get_clock().now().nanoseconds / 1_000_000_000.0

    def age_seconds(self, timestamp, now):
        if timestamp is None:
            return None
        return max(0.0, now - timestamp)

    def status_snapshot(self, now):
        start_cell = None
        goal_cell = None

        if self.has_map and self.has_pose:
            start_cell = self.world_to_grid(self.x, self.y)
        if self.has_map and self.has_goal:
            goal_cell = self.world_to_grid(self.goal_x, self.goal_y)

        return {
            'state': self.state,
            'blocking_reason': self.blocking_reason,
            'has_map': self.has_map,
            'has_pose': self.has_pose,
            'has_goal': self.has_goal,
            'queued_goals': len(self.goal_queue),
            'ready_to_plan': self.ready_to_plan(),
            'start_cell': start_cell,
            'pose_age_sec': self.age_seconds(self.last_pose_time, now),
            'goal_cell': goal_cell,
            'goal_age_sec': self.age_seconds(self.last_goal_time, now),
            'tf_ok': self.tf_ok,
            'tf_map_frame': self.tf_map_frame,
            'tf_robot_frame': self.tf_robot_frame,
            'tf_error': self.tf_error,
        }

    def status_signature(self, status):
        return tuple(
            status[key]
            for key in (
                'state',
                'blocking_reason',
                'has_map',
                'has_pose',
                'has_goal',
                'queued_goals',
                'ready_to_plan',
                'start_cell',
                'goal_cell',
                'tf_ok',
                'tf_map_frame',
                'tf_robot_frame',
            )
        )

    def format_status_value(self, value):
        if value is None:
            return 'n/a'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, tuple):
            return f'({value[0]},{value[1]})'
        if isinstance(value, float):
            return f'{value:.2f}'

        text = str(value)
        if any(character.isspace() for character in text):
            escaped = text.replace('\\', '\\\\').replace('"', '\\"')
            return f'"{escaped}"'
        return text

    def format_status(self, status):
        fields = (
            'state',
            'blocking_reason',
            'has_map',
            'has_pose',
            'has_goal',
            'queued_goals',
            'ready_to_plan',
            'start_cell',
            'pose_age_sec',
            'goal_cell',
            'goal_age_sec',
            'tf_ok',
            'tf_map_frame',
            'tf_robot_frame',
            'tf_error',
        )
        return ' '.join(
            f'{field}={self.format_status_value(status[field])}'
            for field in fields
        )

    def log_status(self, force=False, warning=False):
        now = self.now_seconds()
        status = self.status_snapshot(now)
        signature = self.status_signature(status)
        heartbeat_due = (
            self._last_status_log_time is None
            or now - self._last_status_log_time >= self.STATUS_HEARTBEAT_SEC
        )

        if not force and signature == self._last_status_signature:
            if not heartbeat_due:
                return

        message = self.format_status(status)
        if warning or self.state in ('no_path', 'outside_map'):
            self.get_logger().warning(message)
        else:
            self.get_logger().info(message)

        self._last_status_signature = signature
        self._last_status_log_time = now

    def set_status(self, state, blocking_reason='none'):
        self.state = state
        self.blocking_reason = blocking_reason
        if state != 'no_path':
            self._last_planning_context = None
        self.log_status()
        self.publish_navigation_status(state, blocking_reason)

    def set_planning_status(self, replan_reason, start, goal):
        self.state = 'planning'
        self.blocking_reason = 'none'
        context = (replan_reason, start, goal)
        if context == self._last_planning_context:
            return

        self._last_planning_context = context
        self.log_status(force=True)
        self.publish_navigation_status('planning', replan_reason)

    def readiness_status(self):
        if not self.has_map:
            return 'waiting_for_map', 'map_missing'
        if not self.has_pose:
            return 'waiting_for_pose', 'pose_missing'
        if not self.has_goal:
            return 'waiting_for_goal', 'goal_missing'
        return None

    def outside_map_reason(self, start, goal):
        if start is None and goal is None:
            return 'both_outside'
        if start is None:
            return 'start_outside'
        return 'goal_outside'

    def no_path_reason(self, start, goal):
        if not self.is_raw_free(start):
            return 'start_blocked'
        if not self.is_raw_free(goal):
            return 'goal_blocked'
        return 'astar_exhausted'

    def map_callback(self, msg):
        env_map = list(msg.data)
        map_changed = (
            not self.has_map
            or self.map_width != msg.info.width
            or self.map_height != msg.info.height
            or self.map_resolution != msg.info.resolution
            or self.map_origin_x != msg.info.origin.position.x
            or self.map_origin_y != msg.info.origin.position.y
            or self.env_map != env_map
        )

        if not map_changed:
            return

        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_resolution = msg.info.resolution
        self.map_origin_x = msg.info.origin.position.x
        self.map_origin_y = msg.info.origin.position.y
        self.env_map = env_map
        self.obstacle_distance_map = self.build_obstacle_distance_map()
        self.has_map = True
        self.clear_planned_path(reset_planning_context=True)

    def pos_callback(self, msg):
        self.update_pose(msg.pose)

    def update_pose(self, pose):
        self.x = pose.position.x
        self.y = pose.position.y
        self.yaw = self.yaw_from_quaternion(pose.orientation)
        self.has_pose = True
        self.last_pose_time = self.now_seconds()

    def goal_pose_callback(self, msg):
        goal_x = msg.pose.position.x
        goal_y = msg.pose.position.y

        source_frame = msg.header.frame_id
        if source_frame and source_frame != self.tf_map_frame:
            try:
                transform = self.tf_buffer.lookup_transform(
                    self.tf_map_frame,
                    source_frame,
                    rclpy.time.Time(),
                )
                t = transform.transform.translation
                q = transform.transform.rotation
                cos_a = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
                sin_a = 2.0 * (q.w * q.z + q.x * q.y)
                new_x = cos_a * goal_x - sin_a * goal_y + t.x
                new_y = sin_a * goal_x + cos_a * goal_y + t.y
                goal_x = new_x
                goal_y = new_y
            except Exception as error:
                self.get_logger().warning(
                    f'Failed to transform goal from {source_frame} '
                    f'to {self.tf_map_frame}: {error}'
                )
                return

        new_goal = (goal_x, goal_y)

        if self.last_received_goal is not None:
            spacing = self.distance(
                new_goal[0],
                new_goal[1],
                self.last_received_goal[0],
                self.last_received_goal[1],
            )
            if spacing < self.MIN_GOAL_SPACING:
                return

        if len(self.goal_queue) >= self.MAX_GOAL_QUEUE_SIZE:
            self.get_logger().warning(
                'Goal queue is full. New waypoint rejected.'
            )
            self.publish_navigation_status(
                'queue_full',
                'new_waypoint_rejected',
            )
            return

        self.last_received_goal = new_goal

        if not self.has_goal:
            self.activate_goal(new_goal)
            return

        self.goal_queue.append(new_goal)
        self.get_logger().info(
            f'Queued goal x={new_goal[0]:.3f}, '
            f'y={new_goal[1]:.3f}; '
            f'queue size={len(self.goal_queue)}'
        )
        self.publish_navigation_status(
            'waypoint_queued',
            'waiting_for_current_waypoint',
        )

    def activate_goal(self, goal):
        self.goal_x = goal[0]
        self.goal_y = goal[1]
        self.has_goal = True
        self.last_goal_time = self.now_seconds()
        self.clear_planned_path(reset_planning_context=True)
        self.set_status('planning')

    def activate_next_goal(self):
        if self.goal_queue:
            self.activate_goal(self.goal_queue.popleft())
            return True

        self.has_goal = False
        self.last_goal_time = None
        self.last_received_goal = None
        self.clear_planned_path(reset_planning_context=True)
        return False

    def publish_navigation_status(self, state, description='none'):
        previous_state = getattr(
            self,
            '_last_published_navigation_state',
            None
    )
        status = String()
        status.data = json.dumps({
            'state': state,
            'description': description,
            'blocking_reason': self.blocking_reason,
            'has_map': self.has_map,
            'has_pose': self.has_pose,
            'has_active_goal': self.has_goal,
            'active_goal': {
                'x': round(self.goal_x, 3),
                'y': round(self.goal_y, 3),
            } if self.has_goal else None,
            'queued_goals': len(self.goal_queue),
            'robot_pose': {
                'x': round(self.x, 3),
                'y': round(self.y, 3),
                'yaw': round(self.yaw, 3),
            } if self.has_pose else None,
            'tf_ok': self.tf_ok,
        })
        self.status_publisher.publish(status)
        
        if state != previous_state:
            active_goal_text = (
                f'({self.goal_x:.2f}, {self.goal_y:.2f})'
                if self.has_goal
                else 'none'
        )

            message = (
                f'NAVIGATION STATUS | '
                f'state={state} | '
                f'goal={active_goal_text} | '
                f'queued={len(self.goal_queue)} | '
                f'{description}'
        )

            if state in ('no_path', 'outside_map', 'queue_full'):
                self.get_logger().warning(message)
            else:
                self.get_logger().info(message)

        self._last_published_navigation_state = state

    def publish_planned_path(self):
        msg = Path()
        msg.header.frame_id = 'map'
        msg.header.stamp = self.get_clock().now().to_msg()

        for x, y in self.path:
            pose = PoseStamped()
            pose.header.frame_id = msg.header.frame_id
            pose.header.stamp = msg.header.stamp
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation.w = 1.0
            msg.poses.append(pose)

        self.path_publisher.publish(msg)

    def clear_planned_path(self, reset_planning_context=False):
        self.path = []
        self.path_grid = []
        self.last_planned_start = None
        self.last_planned_goal = None
        if reset_planning_context:
            self._last_planning_context = None
        self.publish_planned_path()

    def timer_callback(self):
        msg = TargetVector()

        readiness_status = self.readiness_status()
        if readiness_status is not None:
            self.set_status(*readiness_status)
            return

        if self.distance(self.x, self.y, self.goal_x, self.goal_y) <= self.GOAL_TOLERANCE:
            reached_goal = (self.goal_x, self.goal_y)
            self.publisher.publish(msg)
            self.clear_planned_path(reset_planning_context=True)

            self.get_logger().info(
                f'Waypoint reached x={reached_goal[0]:.3f}, '
                f'y={reached_goal[1]:.3f}'
            )
            self.publish_navigation_status(
                'waypoint_reached',
                'activating_next_waypoint',
            )

            if not self.activate_next_goal():
                self.set_status('goal_succeeded')
            return

        start = self.world_to_grid(self.x, self.y)
        goal = self.world_to_grid(self.goal_x, self.goal_y)

        if start is None or goal is None:
            self.clear_planned_path()
            self.publisher.publish(msg)
            self.set_status(
                'outside_map',
                self.outside_map_reason(start, goal),
            )
            return

        replan_reason = self.replan_reason(start, goal)

        if replan_reason is not None:
            self.set_planning_status(replan_reason, start, goal)
            planned_path_grid = self.a_star(start, goal)

            if not planned_path_grid:
                self.clear_planned_path()
                self.publisher.publish(msg)
                self.set_status(
                    'no_path',
                    self.no_path_reason(start, goal),
                )
                return

            self.path_grid = planned_path_grid
            self.path = [self.grid_to_world(cell) for cell in self.path_grid]
            self.path_progress = 0.0
            self.last_planned_start = start
            self.last_planned_goal = goal
            self.publish_planned_path()

        if not self.path:
            self.publisher.publish(msg)
            self.set_status(
                'no_path',
                self.no_path_reason(start, goal),
            )
            return

        waypoint = self.next_waypoint()
        linear, angular = self.target_vector_to_waypoint(waypoint)
        msg.linear = linear
        msg.angular = angular
        self.publisher.publish(msg)
        self.set_status('tracking')

    def ready_to_plan(self):
        return self.has_map and self.has_pose and self.has_goal

    def replan_reason(self, start, goal):
        if not self.path or not self.path_grid:
            return 'no current path'

        if goal != self.last_planned_goal:
            return 'goal changed'

        if self.path_is_blocked(start, goal):
            return 'path blocked'

        if self.distance_to_path_grid(start) > self.OFF_PATH_REPLAN_DISTANCE_CELLS:
            return 'robot off path'

        return None

    def path_is_blocked(self, start, goal):
        for cell in self.path_grid:
            if cell == start or cell == goal:
                if not self.is_raw_free(cell):
                    return True
                continue

            if not self.is_traversable(cell):
                return True

        return False

    def distance_to_path_grid(self, cell):
        if not self.path_grid:
            return math.inf

        return min(
            math.hypot(cell[0] - path_cell[0], cell[1] - path_cell[1])
            for path_cell in self.path_grid
        )

    def a_star(self, start, goal):
        if not self.is_raw_free(start) or not self.is_raw_free(goal):
            return []

        open_set = []
        heapq.heappush(open_set, (0.0, start))
        came_from = {}
        g_score = {start: 0.0}
        closed = set()

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            if current in closed:
                continue
            closed.add(current)

            for neighbor, step_cost in self.neighbors(current, goal):
                if neighbor in closed:
                    continue

                new_score = g_score[current] + step_cost
                if new_score >= g_score.get(neighbor, math.inf):
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = new_score
                f_score = new_score + self.heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

        return []

    def neighbors(self, cell, goal):
        x, y = cell
        directions = [
            (-1, 0, 1.0),
            (1, 0, 1.0),
            (0, -1, 1.0),
            (0, 1, 1.0),
            (-1, -1, math.sqrt(2.0)),
            (-1, 1, math.sqrt(2.0)),
            (1, -1, math.sqrt(2.0)),
            (1, 1, math.sqrt(2.0)),
        ]

        for dx, dy, cost in directions:
            neighbor = (x + dx, y + dy)
            if dx != 0 and dy != 0:
                adjacent_x = (x + dx, y)
                adjacent_y = (x, y + dy)
                if not self.is_traversable(adjacent_x) or not self.is_traversable(adjacent_y):
                    continue

            if self.is_traversable(neighbor) or (neighbor == goal and self.is_raw_free(neighbor)):
                yield neighbor, cost + (2.0 if self.is_inflated(neighbor) else 0.0)

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def next_waypoint(self):
        path_distance = 0.0
        projected_progress = self.path_progress
        projection_distance_squared = math.inf

        for segment_start, segment_end in zip(self.path, self.path[1:]):
            start_x, start_y = segment_start
            end_x, end_y = segment_end
            segment_x = end_x - start_x
            segment_y = end_y - start_y
            segment_length_squared = (
                segment_x * segment_x + segment_y * segment_y
            )
            if segment_length_squared == 0.0:
                continue

            segment_length = math.sqrt(segment_length_squared)
            segment_end_progress = path_distance + segment_length
            if segment_end_progress < self.path_progress:
                path_distance = segment_end_progress
                continue

            minimum_t = self.clamp(
                (self.path_progress - path_distance) / segment_length,
                0.0,
                1.0,
            )
            projection_t = self.clamp(
                (
                    (self.x - start_x) * segment_x
                    + (self.y - start_y) * segment_y
                ) / segment_length_squared,
                minimum_t,
                1.0,
            )
            projection_x = start_x + projection_t * segment_x
            projection_y = start_y + projection_t * segment_y
            distance_squared = (
                (self.x - projection_x) * (self.x - projection_x)
                + (self.y - projection_y) * (self.y - projection_y)
            )
            if distance_squared < projection_distance_squared:
                projection_distance_squared = distance_squared
                projected_progress = (
                    path_distance + projection_t * segment_length
                )

            path_distance = segment_end_progress

        self.path_progress = projected_progress
        lookahead_progress = min(
            self.path_progress + self.LOOKAHEAD_DISTANCE,
            path_distance,
        )

        path_distance = 0.0
        for segment_start, segment_end in zip(self.path, self.path[1:]):
            start_x, start_y = segment_start
            end_x, end_y = segment_end
            segment_x = end_x - start_x
            segment_y = end_y - start_y
            segment_length = math.hypot(segment_x, segment_y)
            if segment_length == 0.0:
                continue

            segment_end_progress = path_distance + segment_length
            if lookahead_progress <= segment_end_progress:
                target_t = (
                    lookahead_progress - path_distance
                ) / segment_length
                return (
                    start_x + target_t * segment_x,
                    start_y + target_t * segment_y,
                )
            path_distance = segment_end_progress

        return self.path[-1]

    def target_vector_to_waypoint(self, waypoint):
        waypoint_x, waypoint_y = waypoint
        dx = waypoint_x - self.x
        dy = waypoint_y - self.y
        cos_yaw = math.cos(self.yaw)
        sin_yaw = math.sin(self.yaw)
        robot_x = cos_yaw * dx + sin_yaw * dy
        robot_y = -sin_yaw * dx + cos_yaw * dy
        distance_squared = robot_x * robot_x + robot_y * robot_y
        distance_to_waypoint = math.sqrt(distance_squared)
        heading_error = math.atan2(robot_y, robot_x)

        if abs(heading_error) >= self.TURN_IN_PLACE_THRESHOLD:
            angular = self.clamp(
                heading_error,
                -self.MAX_ANGULAR_SPEED,
                self.MAX_ANGULAR_SPEED,
            )
            return 0.0, angular

        turn_scale = max(0.0, 1.0 - abs(heading_error) / (math.pi / 2.0))
        linear = min(self.LINEAR_SPEED, distance_to_waypoint) * turn_scale

        curvature = 0.0
        if distance_squared > 0.0:
            curvature = 2.0 * robot_y / distance_squared
        angular = self.clamp(
            linear * curvature,
            -self.MAX_ANGULAR_SPEED,
            self.MAX_ANGULAR_SPEED,
        )

        return linear, angular

    def world_to_grid(self, x, y):
        if self.map_resolution <= 0.0:
            return None

        grid_x = math.floor((x - self.map_origin_x) / self.map_resolution)
        grid_y = math.floor((y - self.map_origin_y) / self.map_resolution)
        cell = (grid_x, grid_y)

        if not self.in_bounds(cell):
            return None
        return cell

    def grid_to_world(self, cell):
        x, y = cell
        return (
            self.map_origin_x + (x + 0.5) * self.map_resolution,
            self.map_origin_y + (y + 0.5) * self.map_resolution,
        )

    def is_free(self, cell):
        return self.is_traversable(cell) and not self.is_inflated(cell)

    def is_traversable(self, cell):
        return self.is_raw_free(cell) and self.has_map_edge_clearance(cell)

    def is_inflated(self, cell):
        return self.obstacle_distance(cell) < self.ROBOT_CLEARANCE_RADIUS

    def obstacle_distance(self, cell):
        if len(self.obstacle_distance_map) != len(self.env_map):
            return math.inf

        if not self.in_bounds(cell):
            return math.inf

        index = self.map_index(cell)
        if index >= len(self.obstacle_distance_map):
            return math.inf

        return self.obstacle_distance_map[index]

    def is_raw_free(self, cell):
        if not self.in_bounds(cell):
            return False

        index = self.map_index(cell)
        if index >= len(self.env_map):
            return False

        return not self.raw_value_blocked(self.env_map[index])

    def build_obstacle_distance_map(self):
        obstacle_distance_map = [math.inf] * len(self.env_map)
        if not self.env_map or self.map_width <= 0 or self.map_height <= 0:
            return obstacle_distance_map

        offsets = self.inflation_offsets()
        for index, value in enumerate(self.env_map):
            if not self.raw_value_blocked(value):
                continue

            obstacle_x = index % self.map_width
            obstacle_y = index // self.map_width
            for dx, dy, distance in offsets:
                nearby_cell = (obstacle_x + dx, obstacle_y + dy)
                if not self.in_bounds(nearby_cell):
                    continue

                nearby_index = self.map_index(nearby_cell)
                obstacle_distance_map[nearby_index] = min(
                    obstacle_distance_map[nearby_index],
                    distance,
                )

        return obstacle_distance_map

    def inflation_offsets(self):
        if self.map_resolution <= 0.0:
            return [(0, 0, 0.0)]

        clearance_cells = self.clearance_cells()
        offsets = []
        for dy in range(-clearance_cells, clearance_cells + 1):
            for dx in range(-clearance_cells, clearance_cells + 1):
                cell_distance = math.hypot(dx, dy)
                if cell_distance <= clearance_cells:
                    offsets.append((dx, dy, cell_distance * self.map_resolution))

        return offsets

    def has_map_edge_clearance(self, cell):
        if self.map_resolution <= 0.0:
            return False

        x, y = cell
        clearance_cells = self.clearance_cells()
        return (
            x >= clearance_cells
            and y >= clearance_cells
            and x < self.map_width - clearance_cells
            and y < self.map_height - clearance_cells
        )

    def clearance_cells(self):
        if self.map_resolution <= 0.0:
            return 0

        return math.ceil(self.ROBOT_CLEARANCE_RADIUS / self.map_resolution)

    def raw_value_blocked(self, value):
        return value < 0 or value >= self.OCCUPIED_THRESHOLD

    def in_bounds(self, cell):
        x, y = cell
        return 0 <= x < self.map_width and 0 <= y < self.map_height

    def map_index(self, cell):
        x, y = cell
        return y * self.map_width + x

    def heuristic(self, cell, goal):
        return math.hypot(goal[0] - cell[0], goal[1] - cell[1])

    def yaw_from_quaternion(self, q):
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        return math.atan2(siny_cosp, cosy_cosp)

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def clamp(self, value, minimum, maximum):
        return max(minimum, min(value, maximum))


def main():
    rclpy.init()
    navigation = Navigation()
    try:
        rclpy.spin(navigation)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            if rclpy.ok():
                navigation.publisher.publish(TargetVector())
        except Exception:
            pass
        try:
            navigation.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()
