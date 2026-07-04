from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import rclpy
from rclpy.node import Node


class OdomToPos(Node):
    def __init__(self):
        super().__init__('odom_to_pos')
        self.declare_parameter('output_frame_id', 'map')

        self.output_frame_id = (
            self.get_parameter('output_frame_id')
            .get_parameter_value()
            .string_value
        )

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10,
        )
        self.publisher = self.create_publisher(PoseStamped, '/pos', 10)

    def odom_callback(self, msg):
        pos = PoseStamped()
        pos.header.stamp = msg.header.stamp
        pos.header.frame_id = self.output_frame_id or msg.header.frame_id
        pos.pose = msg.pose.pose
        self.publisher.publish(pos)


def main():
    rclpy.init()
    node = OdomToPos()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()
