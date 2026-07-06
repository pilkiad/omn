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

class BlindExploration(Node):
    def __init__(self):
        super().__init__("blind_exploration")

        # Behavioural constants
        self.MAX_SENSOR_RANGE = 0.55                # Maximum obstacle distance that robot will alter curse
        self.WALL_HUG_RANGE = [                     # Range at which obstacle is considered ideally position and should be "hugged"
            self.MAX_SENSOR_RANGE * 0.75,           # ... min
            self.MAX_SENSOR_RANGE * 1.1             # ... max
        ]
        self.WALL_HUG_STRENGTH = 0.1                # Angular strength used for turning
        self.WALL_HUG_MIN_LINEAR_SPEED = 0.03       # How fast the robot needs to be in order to wall hug
        self.DAMPING_MULTIPLIER = [ 0.02, 0.02 ]    # How much obstacle detection should change the target direction (linear, angular)
        self.DEFAULT_TARGET_VECTOR = [ 0.1, 0.0 ]   # Default desired movement direction (linear, angular) -> forward
        self.DRIFT_MAX = [ 0.05, 0.1 ]              # Maximum random drift (offset from default target vector)
        self.DRIFT_SHUFFLE_MAX_TIME = 15            # Num. movement commands before recalculating random drift

        # Prepare some default values
        self.target_vector = self.DEFAULT_TARGET_VECTOR
        self.drift = [0.0,0.0]
        self.drift_shuffle_c = 0
        self.no_drift_counter = 0

        # Handle topics
        self.scan_subscription = self.create_subscription(LaserScan, "/scan", self.scan_callback, 1)
        self.publisher = self.create_publisher(TargetVector, "/target_vector", 1)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def scan_callback(self, msg):
        # Define movement vector with a bias for going forward
        self.target_vector = self.DEFAULT_TARGET_VECTOR.copy()
        # For simplicity consider the robot to be at coordinate center
        center_point = [0.0, 0.0]

        # Indicate whether left or right wall was detected
        right_wall = False
        left_wall = False

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

            # Check if a wall is close enough left/right to start hugging it
            if (a >= 70 and a <= 110) and (r > self.WALL_HUG_RANGE[0] and r < self.WALL_HUG_RANGE[1]):
                right_wall = True
            if (a >= -110 and a <= 70) and (r > self.WALL_HUG_RANGE[0] and r < self.WALL_HUG_RANGE[1]):
                left_wall = True

        # Initiate wall hug if sufficient speed is present
        # (do it outside the loop since linear velocity needs to be completely calculated to know how fast we are going)
        if left_wall and self.target_vector[0] > self.WALL_HUG_MIN_LINEAR_SPEED and not right_wall:
            self.target_vector[1] -= self.WALL_HUG_STRENGTH
            #self.no_drift_counter = 50
        if right_wall and self.target_vector[0] > self.WALL_HUG_MIN_LINEAR_SPEED and not left_wall:
            self.target_vector[1] += self.WALL_HUG_STRENGTH
            #self.no_drift_counter = 50
        if self.no_drift_counter > 0:
            self.no_drift_counter = self.no_drift_counter - 1

        # Apply random drift to target vector
        if not left_wall and not right_wall and self.no_drift_counter <= 0:
            self.target_vector = [self.target_vector[0] + self.drift[0], self.target_vector[1] + self.drift[1]]

    def timer_callback(self):
        msg = TargetVector()

        # Shuffle the drift every now and then
        self.drift_shuffle_c += 1
        if self.drift_shuffle_c > self.DRIFT_SHUFFLE_MAX_TIME:
            self.drift_shuffle_c = 0
            self.drift = [random.random()*(self.DRIFT_MAX[0]*2)-self.DRIFT_MAX[0], random.random()*(self.DRIFT_MAX[1]*2)-self.DRIFT_MAX[1]]
            self.get_logger().info(f"recalc drift")

        # Move according to target vector
        msg.linear = self.target_vector[0]
        msg.angular = self.target_vector[1]

        # Publish
        self.publisher.publish(msg)
        self.get_logger().info(f"target_vector={self.target_vector}, drift={self.drift}, c={self.drift_shuffle_c}")

def main():
    rclpy.init()
    blindExploration = BlindExploration()
    try:
        rclpy.spin(blindExploration)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = TargetVector()
        stop_msg.linear = 0.0
        stop_msg.angular = 0.0
        blindExploration.publisher.publish(stop_msg)
        blindExploration.destroy_node()
        rclpy.shutdown()