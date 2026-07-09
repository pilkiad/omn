"""Orchestrator Node.

The single ROS2 node that owns all five System Manager modules and
wires them together with callbacks. Every other file in this package is
a plain Python class with no ROS2 dependency -- easy to unit test
without rclpy running. This file is the only place that touches rclpy
directly for the modules' wiring.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from system_manager.robot_state_machine import RobotStateMachine, RobotState
from system_manager.lifecycle_manager import LifecycleManager
from system_manager.health_monitor import HealthMonitor
from system_manager.recovery_manager import RecoveryManager
from system_manager.task_scheduler import TaskScheduler
from system_manager.dashboard_backend import DashboardBackend


# Startup dependency order from the project spec: camera -> lidar ->
# mapping -> localization -> navigation -> motion_controller.
DEFAULT_STARTUP_ORDER = [
    'camera_processor',
    'lidar_processor',
    'mapping',
    'localization',
    'navigation',
    'motion_controller',
]


class OrchestratorNode(Node):

    def __init__(self):
        super().__init__('system_manager')

        self.declare_parameter('managed_node_names', DEFAULT_STARTUP_ORDER)
        self.managed_names = list(self.get_parameter('managed_node_names').value)

        # Cache of the latest known values, used only to redraw the RViz
        # dashboard as a full snapshot whenever any one piece changes.
        self._last_node_states = {name: 'unknown' for name in self.managed_names}
        self._last_task_name = ''
        self._last_task_state = ''

        self.state_machine = RobotStateMachine(on_change=self._on_robot_state_change)
        self.lifecycle_manager = LifecycleManager(self, self.managed_names)
        self.dashboard = DashboardBackend(self)

        self.health_monitor = HealthMonitor(
            self, self.lifecycle_manager, self.managed_names,
            on_failure=self._on_node_failure,
            on_states=self._on_node_states_update)

        self.recovery_manager = RecoveryManager(
            self, self.lifecycle_manager, self.health_monitor,
            on_recovery_start=self._on_recovery_start,
            on_recovery_done=self._on_recovery_done,
            on_emergency_stop=self._on_emergency_stop)

        self.task_scheduler = TaskScheduler(on_state_change=self._on_task_state_change)

        # Simple string topic for task requests for now. Swap for a
        # proper action server later once you need feedback/cancel from
        # the dashboard (e.g. "navigation 40% complete").
        self.create_subscription(String, 'system_manager/task_request', self._on_task_request, 10)

        self.get_logger().info(f'System manager starting, will bring up: {self.managed_names}')
        self._startup_timer = self.create_timer(2.0, self._startup_once)
        self._refresh_markers()

    def _startup_once(self):
        self._startup_timer.cancel()
        if self.lifecycle_manager.bring_up_in_order(self.managed_names):
            for name in self.managed_names:
                self.health_monitor.expect_active(name)
            self.state_machine.transition(RobotState.READY)
        else:
            self.state_machine.transition(RobotState.ERROR)

    def _refresh_markers(self):
        self.dashboard.publish_markers(
            self.state_machine.state.value, self._last_node_states,
            self._last_task_name, self._last_task_state)

    def _on_robot_state_change(self, previous, new):
        self.get_logger().info(f'Robot state: {previous.value} -> {new.value}')
        self.dashboard.publish_health(
            robot_state=new.value, healthy=(new != RobotState.ERROR),
            failed_nodes=[], last_event=f'{previous.value}->{new.value}')
        self._refresh_markers()

    def _on_node_states_update(self, states: dict):
        self._last_node_states = states
        self._refresh_markers()

    def _on_node_failure(self, node_name: str):
        self.state_machine.transition(RobotState.ERROR)
        self.state_machine.transition(RobotState.RECOVERY)
        self.recovery_manager.handle_failure(node_name)

    def _on_recovery_start(self, node_name: str):
        self.dashboard.publish_health(self.state_machine.state.value, False, [node_name], 'recovery_start')
        self._refresh_markers()

    def _on_recovery_done(self, node_name: str):
        self.state_machine.transition(RobotState.READY)

    def _on_emergency_stop(self, node_name: str):
        self.get_logger().error(f'EMERGENCY STOP triggered by {node_name}')
        if 'motion_controller' in self.managed_names:
            self.lifecycle_manager.deactivate('motion_controller')
        self.state_machine.transition(RobotState.ERROR)

    def _on_task_request(self, msg: String):
        task_name = msg.data
        task_id = f'{task_name}-{self.get_clock().now().nanoseconds}'
        self.task_scheduler.submit(task_id, task_name)

    def _on_task_state_change(self, task_id, task_name, state, priority, reason):
        state_str = state.value if hasattr(state, 'value') else str(state)
        self.dashboard.publish_task(task_id, task_name, state, priority, reason)
        self._last_task_name = task_name
        self._last_task_state = state_str
        self._refresh_markers()


def main(args=None):
    rclpy.init(args=args)
    node = OrchestratorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.lifecycle_manager.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
