import math

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import rclpy
from rclpy.node import Node


class OdomToPos(Node):
    def __init__(self):
        super().__init__('odom_to_pos')
        self.declare_parameter('output_frame_id', 'map')
        self.declare_parameter('initial_x', 0.0)
        self.declare_parameter('initial_y', 0.0)
        self.declare_parameter('initial_yaw', 0.0)

        self.output_frame_id = (
            self.get_parameter('output_frame_id')
            .get_parameter_value()
            .string_value
        )
        self.initial_x = (
            self.get_parameter('initial_x')
            .get_parameter_value()
            .double_value
        )
        self.initial_y = (
            self.get_parameter('initial_y')
            .get_parameter_value()
            .double_value
        )
        self.initial_yaw = (
            self.get_parameter('initial_yaw')
            .get_parameter_value()
            .double_value
        )
        self.cos_initial_yaw = math.cos(self.initial_yaw)
        self.sin_initial_yaw = math.sin(self.initial_yaw)

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10,
        )
        self.publisher = self.create_publisher(PoseStamped, '/pos', 10)

    def odom_callback(self, msg):
        odom_pose = msg.pose.pose

        pos = PoseStamped()
        pos.header.stamp = msg.header.stamp
        pos.header.frame_id = self.output_frame_id or msg.header.frame_id
        pos.pose.position.x = (
            self.initial_x
            + self.cos_initial_yaw * odom_pose.position.x
            - self.sin_initial_yaw * odom_pose.position.y
        )
        pos.pose.position.y = (
            self.initial_y
            + self.sin_initial_yaw * odom_pose.position.x
            + self.cos_initial_yaw * odom_pose.position.y
        )
        pos.pose.position.z = odom_pose.position.z
        yaw = self.initial_yaw + self.yaw_from_quaternion(odom_pose.orientation)
        pos.pose.orientation.x = 0.0
        pos.pose.orientation.y = 0.0
        pos.pose.orientation.z = math.sin(yaw / 2.0)
        pos.pose.orientation.w = math.cos(yaw / 2.0)
        self.publisher.publish(pos)

    @staticmethod
    def yaw_from_quaternion(quaternion):
        siny_cosp = 2.0 * (
            quaternion.w * quaternion.z + quaternion.x * quaternion.y
        )
        cosy_cosp = 1.0 - 2.0 * (
            quaternion.y * quaternion.y + quaternion.z * quaternion.z
        )
        return math.atan2(siny_cosp, cosy_cosp)


def main():
    rclpy.init()
    node = OdomToPos()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()
