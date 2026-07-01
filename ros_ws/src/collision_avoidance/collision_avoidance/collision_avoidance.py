"""
Exploration Node

Will explore the environment by
1. Driving forward continuously
2. Adaptively avoiding obstacle
3. Hugging obstacles if detected
4. Applying slight random variations to the movement pattern
"""

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from collision_interfaces.msg import TargetVector

import math
import random

class CollisionAvoidance(Node):
    def __init__(self):
        super().__init__("collision_avoidance")

        self.target_vector = [ 0.0, 0.0 ]

        # NOTE: Block all driving until we have received sensor data, so we know potential collisions may be avoided
        self.lidar_received = False
        self.target_vector_received = False

        # Behavioural constants
        self.MAX_SENSOR_RANGE = 0.55                # Maximum obstacle distance that robot will alter curse
        self.DAMPING_MULTIPLIER = [ 0.02, 0.02 ]    # How much obstacle detection should change the target direction (linear, angular)

        # Prepare some default values
        self.stuck_counter = 0
        self.unstuck_counter = 0
        self.unstuck_spin_direction = 0.5

        # Handle topics
        self.scan_subscription = self.create_subscription(LaserScan, "/scan", self.scan_callback, 1)
        self.scan_subscription = self.create_subscription(TargetVector, "/target_vector", self.target_vector, 1)
        self.publisher = self.create_publisher(Twist, "/base/cmd_vel", 1)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def get_point(self, origin: list[int], a: float, d: float) -> list[int]:
        """
        Helper function to calculate a point that is a degrees and d distance from origin
        """

        a_rad = math.radians(a)
        dx = d * math.cos(a_rad)
        dy = d * math.sin(a_rad)
        return [origin[0]+dx, origin[1]+dy]

    def target_vector_callback(self, msg):
        self.target_vector_received = True
        self.target_vector = [ msg.linear, msg.angular ]

    def scan_callback(self, msg):
        self.lidar_received = True

        # Define movement vector with a bias for going forward
        self.adjusted_vector = self.target_vector.copy()
        # For simplicity consider the robot to be at coordinate center
        center_point = [0.0, 0.0]

        # Define range of angles we are interested in
        # (left is -90, forward is 0, right is 90)
        interesting_angles = []
        for a in range(-70, 70, 2):
            interesting_angles.append(a)

        for i, r in enumerate(msg.ranges):
            # Convert index to degrees
            a = round(math.degrees(msg.angle_min + (i * msg.angle_increment)))

            # Ignore every angle outside forward vision cone
            angle_found = False
            for interesting_angle in interesting_angles:
                if a < (interesting_angle + 1) and a > (interesting_angle - 1):
                    angle_found = True

            # If there is an obstacle at the angle
            if r < self.MAX_SENSOR_RANGE and angle_found:
                # Get vector pointing away from obstacle a inverse distance (gets further away the close the obstacle is)
                correction_point = self.get_point(center_point, a-180, self.MAX_SENSOR_RANGE - r)
                # Move our target movement vector by the offset we just calculated, apply damping per axis
                self.adjusted_vector[0] += correction_point[0] * self.DAMPING_MULTIPLIER[0]
                self.adjusted_vector[1] += correction_point[1] * self.DAMPING_MULTIPLIER[1]

        # If movement has been non-existent for too long, call for unstuck
        if (abs(self.adjusted_vector[0]) + abs(self.adjusted_vector[1])) < 0.01:
            self.stuck_counter = self.stuck_counter + 1
        else:
            self.stuck_counter = 0
        # Unstuck self by rotating ~180 degrees
        if self.stuck_counter > 100:
            self.unstuck_counter = 150
        if self.unstuck_counter > 0:
            self.unstuck_counter = self.unstuck_counter - 1
            self.adjusted_vector[1] = self.unstuck_spin_direction
            self.adjusted_vector[0] = 0.0
        else:
            self.unstuck_spin_direction = random.choice([-0.5, 0.5])

    def timer_callback(self):
        msg = Twist()

        # Check if we are able to move
        if not self.lidar_received:
            self.get_logger().info(f"Can't drive, no sensor info received")
        if not self.adjusted_vector_received:
            self.get_logger().info(f"Can't drive, no target vector received")

        # Move according to target vector
        msg.linear.x = self.adjusted_vector[0]
        msg.angular.z = self.adjusted_vector[1]

        # Publish
        self.publisher.publish(msg)
        self.get_logger().info(f"adjusted_vector={self.adjusted_vector}, target_vector={self.target_vector} s={self.stuck_counter}")

def main():
    rclpy.init()
    colliosion_avoidance = CollisionAvoidance()
    try:
        rclpy.spin(colliosion_avoidance)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = Twist()
        colliosion_avoidance.publisher.publish(stop_msg)
        colliosion_avoidance.destroy_node()
        rclpy.shutdown()