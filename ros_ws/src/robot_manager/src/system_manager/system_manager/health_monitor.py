"""Health Monitor.

Polls every managed node's lifecycle state through the LifecycleManager
(which is how it stays decoupled from teammates' code), publishes the
result as a NodeStateArray for the dashboard, and fires on_failure(name)
the moment a node stops reporting 'active' while we expect it to be.
"""

from rclpy.node import Node
from system_manager_msgs.msg import NodeStateArray


class HealthMonitor:

    def __init__(self, node: Node, lifecycle_manager, managed_node_names,
                 on_failure=None, on_states=None, poll_period_sec: float = 1.0):
        self._node = node
        self._lm = lifecycle_manager
        self._nodes = list(managed_node_names)
        self._on_failure = on_failure
        self._on_states = on_states
        self._expected_active = set()
        self._known_bad = set()

        self._pub = node.create_publisher(NodeStateArray, 'system_manager/node_states', 10)
        self._timer = node.create_timer(poll_period_sec, self._poll)

    def expect_active(self, name: str):
        self._expected_active.add(name)
        self._known_bad.discard(name)

    def stop_expecting(self, name: str):
        self._expected_active.discard(name)

    def _poll(self):
        msg = NodeStateArray()
        for name in self._nodes:
            state = self._lm.get_state(name)
            msg.node_names.append(name)
            msg.states.append(state or 'unknown')

            if name in self._expected_active and state != 'active':
                if name not in self._known_bad:
                    self._known_bad.add(name)
                    self._node.get_logger().error(f'HEALTH: {name} expected active, saw {state}')
                    if self._on_failure:
                        self._on_failure(name)
            elif state == 'active':
                self._known_bad.discard(name)

        msg.stamp = self._node.get_clock().now().to_msg()
        self._pub.publish(msg)

        if self._on_states:
            self._on_states(dict(zip(msg.node_names, msg.states)))
