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
from geometry_msgs.msg import TwistStamped
from irobot_create_msgs.msg import DockStatus, HazardDetectionVector

from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

import math
import random

class Exploration(Node):
    def __init__(self):
        super().__init__("exploration")

        # Behavioural constants
        self.MAX_SENSOR_RANGE = 1.0                 # Maximum obstacle distance that robot will alter curse
        self.WALL_HUG_RANGE = [                     # Range at which obstacle is considered ideally position and should be "hugged"
            self.MAX_SENSOR_RANGE * 0.25,           # ... min
            self.MAX_SENSOR_RANGE * 2.0             # ... max
        ]
        self.WALL_HUG_STRENGTH = 0.3                # Angular strength used for turning
        self.WALL_HUG_MIN_LINEAR_SPEED = 0.1        # How fast the robot needs to be in order to wall hug
        self.DAMPING_MULTIPLIER = [ 0.2, 0.5 ]      # How much obstacle detection should change the target direction (linear, angular)
        self.DEFAULT_TARGET_VECTOR = [ 0.2, 0.0 ]   # Default desired movement direction (linear, angular) -> forward
        self.DRIFT_MAX = 0.05                       # Maximum random drift (offset from default target vector)
        self.DRIFT_SHUFFLE_MAX_TIME = 30            # Num. movement commands before recalculating random drift

        # Prepare some default values
        self.target_vector = self.DEFAULT_TARGET_VECTOR
        self.drift = [0.0,0.0]
        self.drift_shuffle_c = 0

        # Handle topics
        self.scan_subscription = self.create_subscription(LaserScan, "/scan", self.scan_callback, 1)
        self.publisher = self.create_publisher(TwistStamped, "/cmd_vel", 1)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def get_point(self, origin: list[int], a: float, d: float) -> list[int]:
        """
        Helper function to calculate a point that is a degrees and d distance from origin
        """

        a_rad = math.radians(a)
        dx = d * math.cos(a_rad)
        dy = d * math.sin(a_rad)
        return [origin[0]+dx, origin[1]+dy]

    def scan_callback(self, msg):
        # Define movement vector with a bias for going forward
        self.target_vector = self.DEFAULT_TARGET_VECTOR
        # For simplicity consider the robot to be at coordinate center
        center_point = [0.0, 0.0]

        # Indicate whether left or right wall was detected
        right_wall = False
        left_wall = False

        # Define range of angles we are interested in
        # (left is -90, forward is 0, right is 90)
        interesting_angles = []
        for a in range(-90, 90, 10):
            interesting_angles.append(a)

        for i, r in enumerate(msg.ranges):
            # Convert index to degrees
            a = round(math.degrees(msg.angle_min + (i * msg.angle_increment)))

            # Ignore every angle outside forward vision cone
            if a not in interesting_angles:
                continue

            # If there is an obstacle at the angle
            if r < self.MAX_SENSOR_RANGE:
                # Get vector pointing away from obstacle a inverse distance (gets further away the close the obstacle is)
                correction_point = self.get_point(center_point, a-180, self.MAX_SENSOR_RANGE - r)
                # Move our target movement vector by the offset we just calculated, apply damping per axis
                self.target_vector[0] -= correction_point[0] * self.DAMPING_MULTIPLIER[0]
                self.target_vector[1] -= correction_point[1] * self.DAMPING_MULTIPLIER[1]

            # Check if a wall is close enough left/right to start hugging it
            if a == 80 and (r > self.WALL_HUG_RANGE[0] and r < self.WALL_HUG_RANGE[1]):
                right_wall = True
            if a == 10 and (r > self.WALL_HUG_RANGE[0] and r < self.WALL_HUG_RANGE[1]):
                left_wall = True

        # Initiate wall hug if sufficient speed is present
        # (do it outside the loop since linear velocity needs to be completely calculated to know how fast we are going)
        if left_wall and self.target_vector[0] > self.WALL_HUG_MIN_LINEAR_SPEED:
            self.target_vector[1] -= self.WALL_HUG_STRENGTH
        if right_wall and self.target_vector[0] > self.WALL_HUG_MIN_LINEAR_SPEED:
            self.target_vector[1] += self.WALL_HUG_STRENGTH

        # Apply random drift to target vector
        self.target_vector = [self.target_vector[0] + self.drift[0], self.target_vector[1] + self.drift[1]]

    def timer_callback(self):
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = ""

        # Shuffle the drift every now and then
        self.drift_shuffle_c += 1
        if self.drift_shuffle_c > self.DRIFT_SHUFFLE_MAX_TIME:
            self.drift_shuffle_c = 0
            self.drift = [random.random()*(self.DRIFT_MAX*2)-self.DRIFT_MAX, random.random()*(self.DRIFT_MAX*2)-self.DRIFT_MAX]
            self.get_logger().info(f"recalc drift")

        # Move according to target vector
        msg.twist.linear.x = self.target_vector[0]
        msg.twist.angular.z = -self.target_vector[1]

        # Publish
        self.publisher.publish(msg)
        self.get_logger().info(f"target_vector={self.target_vector}, drift={self.drift}, c={self.drift_shuffle_c}")

def main():
    rclpy.init()
    forwardScan = Exploration()
    try:
        rclpy.spin(forwardScan)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = TwistStamped()
        forwardScan.publisher.publish(stop_msg)
        forwardScan.destroy_node()
        rclpy.shutdown()