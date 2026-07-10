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
from std_msgs.msg import Bool

import math
import random

class CollisionAvoidance(Node):
    def __init__(self):
        super().__init__("collision_avoidance")

        self.target_vector = [ 0.0, 0.0 ]
        self.adjusted_vector = [ 0.0, 0.0 ]

        # NOTE: Block all driving until we have received sensor data, so we know potential collisions may be avoided
        self.lidar_received = False
        self.target_vector_received = False
        self.unstuck_enabled = False

        # Behavioural constants
        self.MAX_SENSOR_RANGE = 0.6                 # Maximum obstacle distance that robot will alter curse
        self.DAMPING_MULTIPLIER = [ 0.015, 0.015 ]  # How much obstacle detection should change the target direction (linear, angular)
        self.MAX_LINEAR_VELOCITY = 0.125

        # Prepare some default values
        self.stuck_counter = 0
        self.unstuck_counter = 0
        self.unstuck_spin_direction = 0.5
        self.target_vector_age = 0

        # Handle topics
        self.scan_subscription = self.create_subscription(LaserScan, "/scan", self.scan_callback, 1)
        self.target_vector_subscription = self.create_subscription(TargetVector, "/target_vector", self.target_vector_callback, 1)
        self.toggle_unstuck_subscription = self.create_subscription(Bool, "/toggle_unstuck", self.toggle_unstuck_callback, 1)
        self.publisher = self.create_publisher(Twist, "/base/cmd_vel", 1)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def toggle_unstuck_callback(self, msg):
        self.unstuck_enabled = msg.data
        #self.get_logger().warn(f"Unstuck was set to {self.unstuck_enabled}")

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
        self.target_vector_age = 0
        self.target_vector = [ msg.linear, msg.angular ]
        #self.get_logger().info(f"Received new target vector")

    def scan_callback(self, msg):
        self.lidar_received = True

        # Define movement vector with a bias for going forward
        self.adjusted_vector = self.target_vector.copy()
        # For simplicity consider the robot to be at coordinate center
        center_point = [0.0, 0.0]

        # Clamp movement vector
        # We do this once after receiving the vector to ensure we start working with safe values
        # and once after collision avoidance was calculate to ensure we _produce_ safe values
        if self.adjusted_vector[0] > self.MAX_LINEAR_VELOCITY:
            self.adjusted_vector[0] = self.MAX_LINEAR_VELOCITY
            self.get_logger().warn(f"Clamped linear velocity to {self.MAX_LINEAR_VELOCITY} (incoming)")
        if self.adjusted_vector[0] < -self.MAX_LINEAR_VELOCITY:
            self.adjusted_vector[0] = -self.MAX_LINEAR_VELOCITY
            self.get_logger().warn(f"Clamped linear velocity to -{self.MAX_LINEAR_VELOCITY} (incoming)")
        #if self.adjusted_vector[1] > 0.1:
        #    self.adjusted_vector[1] = 0.1
        #    self.get_logger().info(f"Clamped angular velocity to 0.1 (incoming)")
        #if self.adjusted_vector[1] < -0.1:
        #    self.adjusted_vector[1] = -0.1
        #    self.get_logger().info(f"Clamped angular velocity to -0.1 (incoming)")

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
        if not self.unstuck_enabled:
            return

        if (abs(self.adjusted_vector[0]) + abs(self.adjusted_vector[1])) < 0.01:
            self.stuck_counter = self.stuck_counter + 1
        else:
            self.stuck_counter = 0
        # Unstuck self by rotating ~180 degrees
        if self.stuck_counter > 100:
            self.unstuck_counter = random.choice([50, 100, 150, 200])
        if self.unstuck_counter > 0:
            self.unstuck_counter = self.unstuck_counter - 1
            self.adjusted_vector[1] = self.unstuck_spin_direction
            self.adjusted_vector[0] = 0.0
        else:
            self.unstuck_spin_direction = random.choice([-0.5, -0.25, -0.1, 0.1, 0.25, 0.5])

    def timer_callback(self):
        msg = Twist()

        # Check if we are able to move
        if not self.lidar_received:
            self.get_logger().warn(f"Can't drive, no sensor info received")
            return
        if not self.target_vector_received:
            self.get_logger().warn(f"Can't drive, no target vector received")
            return

        # Clamp movement vector
        # We do this once after receiving the vector to ensure we start working with safe values
        # and once after collision avoidance was calculate to ensure we _produce_ safe values
        if self.adjusted_vector[0] > self.MAX_LINEAR_VELOCITY:
            self.adjusted_vector[0] = self.MAX_LINEAR_VELOCITY
            self.get_logger().warn(f"Clamped linear velocity to {self.MAX_LINEAR_VELOCITY} (outgoing)")
        if self.adjusted_vector[0] < -self.MAX_LINEAR_VELOCITY:
            self.adjusted_vector[0] = -self.MAX_LINEAR_VELOCITY
            self.get_logger().warn(f"Clamped linear velocity to -{self.MAX_LINEAR_VELOCITY} (outgoing)")

        # Move according to target vector
        msg.linear.x = self.adjusted_vector[0]
        msg.angular.z = self.adjusted_vector[1]

        # Publish
        self.publisher.publish(msg)
        self.get_logger().info(f"adjusted_vector={self.adjusted_vector}, target_vector={self.target_vector} s={self.stuck_counter} age={self.target_vector_age}")

        self.target_vector_age += 1
        if self.target_vector_age > 10:
            self.target_vector_received = False
            self.target_vector_age = 0
            self.get_logger().warn("Target vector died of old age")

def main():
    rclpy.init()
    colliosion_avoidance = CollisionAvoidance()
    try:
        rclpy.spin(colliosion_avoidance)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            colliosion_avoidance.publisher.publish(Twist())
            colliosion_avoidance.destroy_node()
            rclpy.shutdown()