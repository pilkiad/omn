from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import Twist
import rclpy
from rclpy.duration import Duration
from rclpy.node import Node


class TargetVectorToCmdVel(Node):
    def __init__(self):
        super().__init__('target_vector_to_cmd_vel')

        self.declare_parameter('input_topic', '/target_vector')
        self.declare_parameter('output_topic', '/cmd_vel')
        self.declare_parameter('linear_scale', 1.0)
        self.declare_parameter('angular_scale', 1.0)
        self.declare_parameter('stale_timeout', 0.75)

        input_topic = self.string_parameter('input_topic')
        output_topic = self.string_parameter('output_topic')
        self.linear_scale = self.double_parameter('linear_scale')
        self.angular_scale = self.double_parameter('angular_scale')
        self.stale_timeout = self.double_parameter('stale_timeout')

        self.last_command_time = None
        self.zero_sent_after_stale = True

        self.subscription = self.create_subscription(
            TargetVector,
            input_topic,
            self.target_vector_callback,
            10,
        )
        self.publisher = self.create_publisher(Twist, output_topic, 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def string_parameter(self, name):
        return self.get_parameter(name).get_parameter_value().string_value

    def double_parameter(self, name):
        return self.get_parameter(name).get_parameter_value().double_value

    def target_vector_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.linear * self.linear_scale
        twist.angular.z = msg.angular * self.angular_scale

        self.last_command_time = self.get_clock().now()
        self.zero_sent_after_stale = self.is_zero(twist)
        self.publisher.publish(twist)

    def timer_callback(self):
        if self.last_command_time is None:
            return
        if self.stale_timeout <= 0.0 or self.zero_sent_after_stale:
            return

        elapsed = self.get_clock().now() - self.last_command_time
        if elapsed > Duration(seconds=self.stale_timeout):
            self.publisher.publish(Twist())
            self.zero_sent_after_stale = True

    def is_zero(self, twist):
        return twist.linear.x == 0.0 and twist.angular.z == 0.0


def main():
    rclpy.init()
    node = TargetVectorToCmdVel()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            if rclpy.ok():
                node.publisher.publish(Twist())
        except Exception:
            pass
        try:
            node.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()
