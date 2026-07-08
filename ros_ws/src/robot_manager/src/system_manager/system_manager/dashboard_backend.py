"""Dashboard Backend.

Publishes everything a dashboard needs. Two kinds of output:
1. Plain topics (system_manager/health, system_manager/task_status,
   and system_manager/node_states from the Health Monitor) -- for any
   future custom dashboard frontend.
2. A visualization_msgs/MarkerArray on system_manager/dashboard_markers
   -- this is what makes the RViz dashboard work. Add RViz's built-in
   "MarkerArray" display, point it at that topic, set Fixed Frame to
   "dashboard", and everything below renders live: no custom RViz
   plugin needed.
"""

from rclpy.node import Node
from std_msgs.msg import ColorRGBA
from visualization_msgs.msg import Marker, MarkerArray

from system_manager_msgs.msg import SystemHealth, TaskStatus


DASHBOARD_FRAME = 'map'  # same frame teammates' mapping/localization/navigation
                          # will use, so the status HUD appears in the same
                          # 3D view as the live map and robot position

ROBOT_STATE_COLOR = {
    'BOOTING': (0.6, 0.6, 0.6),
    'READY': (0.2, 0.8, 0.2),
    'MAPPING': (0.2, 0.5, 0.9),
    'NAVIGATING': (0.2, 0.5, 0.9),
    'BUSY': (0.9, 0.6, 0.1),
    'ERROR': (0.9, 0.15, 0.15),
    'RECOVERY': (0.9, 0.6, 0.1),
    'SHUTDOWN': (0.3, 0.3, 0.3),
}

NODE_STATE_COLOR = {
    'active': (0.2, 0.8, 0.2),
    'inactive': (0.9, 0.8, 0.1),
    'unconfigured': (0.6, 0.6, 0.6),
    'finalized': (0.3, 0.3, 0.3),
    'unknown': (0.9, 0.15, 0.15),
}


class DashboardBackend:

    def __init__(self, node: Node):
        self._node = node
        self._health_pub = node.create_publisher(SystemHealth, 'system_manager/health', 10)
        self._task_pub = node.create_publisher(TaskStatus, 'system_manager/task_status', 10)
        self._marker_pub = node.create_publisher(MarkerArray, 'system_manager/dashboard_markers', 10)

    def publish_health(self, robot_state: str, healthy: bool, failed_nodes, last_event: str = ''):
        msg = SystemHealth()
        msg.robot_state = robot_state
        msg.healthy = healthy
        msg.failed_nodes = list(failed_nodes)
        msg.last_event = last_event
        msg.stamp = self._node.get_clock().now().to_msg()
        self._health_pub.publish(msg)

    def publish_task(self, task_id: str, task_name: str, state, priority: int = 0, reason: str = ''):
        msg = TaskStatus()
        msg.task_id = task_id
        msg.task_name = task_name
        msg.state = state.value if hasattr(state, 'value') else str(state)
        msg.priority = priority
        msg.reason = reason
        msg.stamp = self._node.get_clock().now().to_msg()
        self._task_pub.publish(msg)

    def _text_marker(self, marker_id, ns, x, y, z, text, color, scale=0.3):
        m = Marker()
        m.header.frame_id = DASHBOARD_FRAME
        m.header.stamp = self._node.get_clock().now().to_msg()
        m.ns = ns
        m.id = marker_id
        m.type = Marker.TEXT_VIEW_FACING
        m.action = Marker.ADD
        m.pose.position.x = x
        m.pose.position.y = y
        m.pose.position.z = z
        m.pose.orientation.w = 1.0
        m.scale.z = scale
        m.color = ColorRGBA(r=color[0], g=color[1], b=color[2], a=1.0)
        m.text = text
        return m

    def _cube_marker(self, marker_id, ns, x, y, z, color, size=0.4):
        m = Marker()
        m.header.frame_id = DASHBOARD_FRAME
        m.header.stamp = self._node.get_clock().now().to_msg()
        m.ns = ns
        m.id = marker_id
        m.type = Marker.CUBE
        m.action = Marker.ADD
        m.pose.position.x = x
        m.pose.position.y = y
        m.pose.position.z = z
        m.pose.orientation.w = 1.0
        m.scale.x = m.scale.y = m.scale.z = size
        m.color = ColorRGBA(r=color[0], g=color[1], b=color[2], a=0.9)
        return m

    def publish_markers(self, robot_state: str, node_states: dict, task_name: str = '', task_state: str = ''):
        """Draws the whole dashboard as RViz markers:
        - a big header line with the global robot state, color-coded
        - a line showing the current task
        - one colored cube + text label per managed node, laid out in a row
        Call this any time robot state, task state, or node states change.
        """
        array = MarkerArray()

        rc = ROBOT_STATE_COLOR.get(robot_state, (0.6, 0.6, 0.6))
        array.markers.append(self._text_marker(
            0, 'header', 0.0, 0.0, 2.2, f'ROBOT STATE: {robot_state}', rc, scale=0.5))

        task_text = f'TASK: {task_name} [{task_state}]' if task_name else 'TASK: (none)'
        array.markers.append(self._text_marker(
            1, 'header', 0.0, 0.0, 1.6, task_text, (0.9, 0.9, 0.9), scale=0.3))

        names = list(node_states.keys())
        n = len(names)
        for i, name in enumerate(names):
            state = node_states[name]
            color = NODE_STATE_COLOR.get(state, (0.9, 0.15, 0.15))
            x = (i - (n - 1) / 2.0) * 1.6
            array.markers.append(self._cube_marker(10 + i, 'nodes', x, 0.0, 0.4, color))
            array.markers.append(self._text_marker(
                30 + i, 'nodes', x, 0.0, 0.95, f'{name}\n{state}', color, scale=0.22))

        self._marker_pub.publish(array)
