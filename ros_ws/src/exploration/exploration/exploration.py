import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from collision_interfaces.msg import TargetVector
from nav_msgs.msg import OccupancyGrid

import math
import random
import time

class Exploration(Node):
    def __init__(self):
        super().__init__("exploration")

        self.MIN_DISTANCE_BETWEEN = 1.0 # Minimum distance a desirable position has to have to all previously explored positions

        self.target_vector = [ 0.0, 0.0 ]
        self.our_position = [ 0.0, 0.0 ]

        self.env_map = None
        self.map_width = 0.0
        self.map_height = 0.0
        self.map_origin = [ 0.0, 0.0 ]
        self.map_resolution = 0.0

        self.already_visited = []

        self.publisher = self.create_publisher(PoseStamped, "/goal_pose", 1)
        self.map_subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 1)
        self.pose_subscription = self.create_subscription(PoseStamped, '/pose', self.pose_callback, 1)
        self.exploration_time = self.create_timer(30, self.exploration_callback)

    def get_cell_at(self, x, y):
        return self.env_map[(y * self.map_width) + x]

    def distance(self, from_pos, to_pos):
        return math.sqrt((to_pos[0]-from_pos[0])**2+(to_pos[1]-from_pos[1])**2)

    def exploration_callback(self):
        # Ensure some map has been received in the last n seconds to we have some current data to work with
        if self.env_map is None:
            self.get_logger().info("Cannot explore: no current map")
            return
        if self.our_position is None:
            self.get_logger().info("Cannot explore: no current position")
            return

        target_positions = []

        # Go through all cells of map
        for y in range(1, self.map_height - 1):
            for x in range(1, self.map_width - 1):

                # Take a look at each cell and their neighbors
                cell_value = self.get_cell_at(x, y)
                neighbors = [
                    self.get_cell_at(x+1, y),
                    self.get_cell_at(x-1, y),
                    self.get_cell_at(x, y+1),
                    self.get_cell_at(x, y-1)
                ]

                # Only look at non-visited cells
                if cell_value != -1:
                    continue

                # Atleast one neighbor needs to be marked as "free" to consider the position reachable
                reachable = False
                for neighbor in neighbors:
                    if neighbor == 0:
                        reachable = True

                if not reachable:
                    continue

                # Note the position as desireable
                position = [
                    self.map_origin[0] + (x + 0.5) * self.map_resolution,
                    self.map_origin[1] + (y + 0.5) * self.map_resolution
                ]
                target_positions.append(position)

        # Get closest non-visited position
        closest_distance = None
        closest_position = None
        for target_position in target_positions:
            # Check if we have been close to this position already in the past
            skip = False
            for already_visited_position in self.already_visited:
                if self.distance(target_position, already_visited_position) < self.MIN_DISTANCE_BETWEEN:
                    skip = True
            if skip:
                continue

            # Check if this position is the closest out of all possible positions
            distance = self.distance(target_position, self.our_position)
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_position = target_position

        if closest_position is None:
            self.get_logger().info("Cannot explore: no suitable position")
            return

        # Send the desired position over to navigation
        self.send_position(closest_position)

        # Wipe stored data so we don't work with stale data
        self.env_map = None
        self.our_position = None

    def send_position(self, position):
        self.already_visited.append(position)
        msg = PoseStamped()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.position.x = position[0]
        msg.pose.position.y = position[1]
        self.get_logger().info(f"Exploring at: {position}")
        self.publisher.publish(msg)

    def pose_callback(self, msg):
        self.our_position = [ msg.pose.position.x, msg.pose.position.y ]

    def map_callback(self, msg):
        self.env_map = list(msg.data)
        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_origin = [ msg.info.origin.positon.x, msg.info.origin.positon.y ]
        self.map_resolution = msg.info.resolution

        self.get_logger().info("Updated map")

def main():
    rclpy.init()
    exploration = Exploration()
    try:
        rclpy.spin(exploration)
    except KeyboardInterrupt:
        pass
    finally:
        exploration.destroy_node()
        rclpy.shutdown()