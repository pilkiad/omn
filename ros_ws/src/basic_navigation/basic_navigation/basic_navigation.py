import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

import math

class BasicNavigation(Node):
    def __init__(self):
        super().__init__("basic_navigation")

        self.angle = 30
        self.distance = 1.0

        self.danger = False

        self.scan_subscription = self.create_subscription(
                LaserScan,
                "/scan",
                self.scan_callback,
                1
        )
        self.publisher = self.create_publisher(
                Twist,
                "/base/cmd_vel",
                1
        )
        self.timer = self.create_timer(0.5, self.timer_callback)

    def scan_callback(self, msg):
        self.danger = False
        for i, r in enumerate(msg.ranges):
            angle = round(math.degrees(msg.angle_min + (i* msg.angle_increment)))
            if angle >= -self.angle and angle <= self.angle and r < self.distance:
                self.danger = True

    def timer_callback(self):
        msg = Twist()

        if not self.danger:
            print("forward")
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        else:
            print("stop")
            msg.linear.x = 0.0
            msg.angular.z = 0.2

        self.publisher.publish(msg)

def main():
    rclpy.init()
    forwardScan = BasicNavigation()
    try:
        rclpy.spin(forwardScan)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = Twist()
        forwardScan.publisher.publish(stop_msg)
        forwardScan.destroy_node()
        rclpy.shutdown()