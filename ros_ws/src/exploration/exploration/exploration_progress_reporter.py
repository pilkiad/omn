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
        super().__init__("exploration_progress_reporter")

        self.env_map = None
        self.map_width = 0.0
        self.map_height = 0.0
        self.map_origin = [ 0.0, 0.0 ]
        self.map_resolution = 0.0

        self.map_subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 1)
        self.pose_subscription = self.create_subscription(PoseStamped, '/pose', self.pose_callback, 1)
        self.exploration_time = self.create_timer(10, self.exploration_callback)

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

        frontier_count = 0
        ground_count = 0

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

                # Only look at free cells
                if cell_value != 0:
                    continue

                # Atleast one neighbor needs to be marked as "free" to consider the position reachable
                has_empty_neighbor = False
                has_full_neighbor = False
                has_wall_neighbor = False
                for neighbor in neighbors:
                    if neighbor == -1:
                        has_empty_neighbor = True
                    elif neighbor == 0:
                        has_full_neighbor = True
                    else:
                        has_wall_neighbor = True

                # A cell if considered when it has an empty neighbor, also has a full neighbor (not floating), and DOESNT have a wall neighbor
                if (has_empty_neighbor and has_full_neighbor and not has_wall_neighbor):
                    frontier_count += 1
                elif (not has_empty_neighbor and has_full_neighbor):
                    ground_count += 1

        ratio = frontier_count / ground_count
        self.get_logger().info(f"Exploration: {ratio*100}%")

    def pose_callback(self, msg):
        self.our_position = [ msg.pose.position.x, msg.pose.position.y ]

    def map_callback(self, msg):
        self.env_map = list(msg.data)
        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_origin = [ msg.info.origin.position.x, msg.info.origin.position.y ]
        self.map_resolution = msg.info.resolution
        self.already_visited = []

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