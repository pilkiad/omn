"""A generic, well-behaved LifecycleNode used to stand in for whichever
teammate node hasn't been written yet. Launch six of these under
different names (see launch/mock_nodes.launch.py) and your System
Manager cannot tell the difference from the real thing, because it only
ever talks to the standard lifecycle interface.

Also exposes a "simulate_crash" topic per node so you can exercise your
Health Monitor and Recovery Manager on demand, e.g.:

    ros2 topic pub --once /localization/simulate_crash std_msgs/msg/String "data: 'crash'"
"""

import rclpy
from rclpy.lifecycle import Node as LifecycleNode
from rclpy.lifecycle import State, TransitionCallbackReturn
from std_msgs.msg import String


class MockLifecycleNode(LifecycleNode):

    def __init__(self):
        super().__init__('mock_lifecycle_node')
        self.declare_parameter('fail_on_configure', False)
        self.create_subscription(
            String, f'{self.get_name()}/simulate_crash', self._on_simulate_crash, 10)

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(f'{self.get_name()}: on_configure')
        if self.get_parameter('fail_on_configure').value:
            return TransitionCallbackReturn.FAILURE
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(f'{self.get_name()}: on_activate')
        return TransitionCallbackReturn.SUCCESS

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(f'{self.get_name()}: on_deactivate')
        return TransitionCallbackReturn.SUCCESS

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(f'{self.get_name()}: on_cleanup')
        return TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(f'{self.get_name()}: on_shutdown')
        return TransitionCallbackReturn.SUCCESS

    def _on_simulate_crash(self, msg: String):
        # Forces an unrequested deactivate, so it looks like the node
        # crashed out of ACTIVE -- exactly what your Health Monitor
        # should notice on its next poll.
        self.get_logger().warn(f'{self.get_name()}: simulating a crash now')
        self.trigger_deactivate()


def main(args=None):
    rclpy.init(args=args)
    node = MockLifecycleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
