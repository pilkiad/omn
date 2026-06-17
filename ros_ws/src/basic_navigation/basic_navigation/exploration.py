import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

import math

class Exploration(Node):
    def __init__(self):
        super().__init__("basic_navigation")

        self.angle_range = 30
        self.left_detection_angle = -90
        self.right_detection_angle = 90
        self.distance = 1.0

        self.danger = [False, False, False]

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
        self.danger = [False,False,False]
        for i, r in enumerate(msg.ranges):
            angle = round(math.degrees(msg.angle_min + (i* msg.angle_increment)))
            if angle >= -self.angle_range and angle <= self.angle_range and r < self.distance:
                self.danger[1] = True
            if angle >= self.left_detection_angle - self.angle_range and angle <= self.left_detection_angle + self.angle_range and r < self.distance:
                self.danger[2] = True
            if angle >= self.right_detection_angle - self.angle_range and angle <= self.right_detection_angle + self.angle_range and r < self.distance:
                self.danger[0] = True

    def timer_callback(self):
        msg = Twist()

        #print(self.danger)

        if not self.danger[1]:
            msg.linear.x = 0.1
        else:
            msg.linear.x = 0.0

        if self.danger[0]:
            msg.angular.z = 0.2
        elif self.danger[2]:
            msg.angular.z = -0.2
        else:
            msg.angular.z = -0.2

        self.get_logger().info(f"danger={self.danger}, angular={msg.angular.z}, linear={msg.linear.x}")

        self.publisher.publish(msg)

        """
        if not self.danger:
            print("forward")
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        else:
            print("stop")
            msg.linear.x = 0.0
            msg.angular.z = 0.2

        self.publisher.publish(msg)
        """

def main():
    rclpy.init()
    forwardScan = Exploration()
    try:
        rclpy.spin(forwardScan)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = Twist()
        forwardScan.publisher.publish(stop_msg)
        forwardScan.destroy_node()
        rclpy.shutdown()