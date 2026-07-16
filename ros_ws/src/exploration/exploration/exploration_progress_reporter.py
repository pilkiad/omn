import rclpy
from rclpy.node import LifecycleNode, State, TransitionCallbackReturn

from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from collision_interfaces.msg import TargetVector
from nav_msgs.msg import OccupancyGrid

import math
import random
import time

class ExplorationProgressReporter(LifecycleNode):
    def __init__(self):
        super().__init__("exploration_progress_reporter")

        self.our_position = [ 0.0, 0.0 ]

        self.env_map = None
        self.map_width = 0.0
        self.map_height = 0.0
        self.map_origin = [ 0.0, 0.0 ]
        self.map_resolution = 0.0

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("configuring exploration progress report")
        self.map_subscription = self.create_lifecycle_subscription(OccupancyGrid, '/map', self.map_callback, 1)
        self.pose_subscription = self.create_subscription(PoseStamped, '/pose', self.pose_callback, 1)
        self.ratio_publisher = self.create_lifecycle_publisher(Float64, '/exploration_ratio', 10)
        self.exploration_time = self.create_timer(10, self.exploration_callback)

        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State):
        self.get_logger().info("Activating exploration progress report")
        return super().on_activate(state)

    def on_deactivate(self, state: State):
        self.get_logger().info("Deactivating exploration progress report")
        return super().on_deactivate(state)

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Cleaning up exploration progress reporter")

        self.destroy_lifecycle_publisher(self.ratio_publisher)
        self.destroy_subscription(self.map_subscription)
        self.destroy_subscription(self.pose_subscription)
        self.destroy_timer(self.exploration_time)

        return TransitionCallbackReturn.SUCCESS

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
        if not self.ratio_publisher.is_activated:
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

        msg = Float64()
        msg.data = ratio
        self.ratio_publisher.publish(msg)

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
    exploration_progress_reporter = ExplorationProgressReporter()

    exploration_progress_reporter.trigger_configure()
    exploration_progress_reporter.trigger_activate()

    try:
        rclpy.spin(exploration_progress_reporter)
    except KeyboardInterrupt:
        pass
    finally:
        exploration_progress_reporter.trigger_deactivate()
        exploration_progress_reporter.trigger_cleanup()
        exploration_progress_reporter.destroy_node()
        rclpy.shutdown()