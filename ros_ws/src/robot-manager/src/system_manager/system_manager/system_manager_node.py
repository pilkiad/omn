import rclpy
from rclpy.node import Node

from .system_manager import SystemManager


class SystemManagerNode(Node):

    def __init__(self):
        super().__init__("system_manager")

        self.manager = SystemManager()

        self.get_logger().info("System Manager started")

        self.manager.initialize_robot()

        self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(
            f"State: {self.manager.get_robot_state().name}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = SystemManagerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
