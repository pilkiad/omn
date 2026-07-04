import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class OdomDownsampler(Node):

    def __init__(self):
        super().__init__('odom_downsampler')

        # Ziel-Frequenz
        self.target_hz = 20.0
        self.period = 1.0 / self.target_hz

        self.last_time = self.get_clock().now()

        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.pub = self.create_publisher(
            Odometry,
            '/odom_20hz',
            10
        )

        self.get_logger().info('Odom Downsampler gestartet (20 Hz)')

    def odom_callback(self, msg):
        now = self.get_clock().now()

        # Zeitdifferenz prüfen
        if (now - self.last_time).nanoseconds * 1e-9 < self.period:
            return

        self.last_time = now

        # Nachricht weiterleiten
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = OdomDownsampler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()