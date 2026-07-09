import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from collision_interfaces.msg import TargetVector
from nav_msgs.msg import OccupancyGrid
from visualization_msgs.msg import Marker, MarkerArray

import math
import random
import time

class Exploration(Node):
    def __init__(self):
        super().__init__("exploration")

        self.MIN_DISTANCE_BETWEEN = 1.0 # Minimum distance a desirable position has to have to all previously explored positions
        self.MARGIN = 10

        self.target_vector = [ 0.0, 0.0 ]
        self.our_position = [ 0.0, 0.0 ]

        self.map = None
        self.env_map = None
        self.map_width = 0.0
        self.map_height = 0.0
        self.map_origin = [ 0.0, 0.0 ]
        self.map_resolution = 0.0

        self.already_visited = []

        self.publisher = self.create_publisher(PoseStamped, "/goal_pose", 1)
        self.map_subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 1)
        self.target_vector_subscription = self.create_subscription(TargetVector, '/target_vector', self.target_vector_callback, 1)
        self.pose_subscription = self.create_subscription(PoseStamped, '/pos', self.pose_callback, 1)
        self.exploration_time = self.create_timer(5, self.exploration_callback)
        self.marker_pub = self.create_publisher(MarkerArray, '/exploration_markers', 1)

    def target_vector_callback(self, msg):
        self.target_vector = [ msg.linear, msg.angular ]

    def get_cell_at(self, x, y):
        return self.env_map[(y * self.map_width) + x]

    def distance(self, from_pos, to_pos):
        return math.sqrt((to_pos[0]-from_pos[0])**2+(to_pos[1]-from_pos[1])**2)

    def flood_fill(self):
        self.get_logger().info("Starting flood fill...")

        if self.env_map is None:
            self.get_logger().warn("Cannot flood fill: no map")
            return

        start_pos = (
            int((self.our_position[0] - self.map_origin[0]) / self.map_resolution),
            int((self.our_position[1] - self.map_origin[1]) / self.map_resolution)
        )
        neighbors = [start_pos]
        visited_neighbors = []
        reachable_map = []

        while len(neighbors) > 0 and len(visited_neighbors) < 25000:
            neighbor = neighbors[0]
            cell = self.get_cell_at(neighbor[0], neighbor[1])

            if cell != 0:
                visited_neighbors.append(neighbor)
                neighbors.remove(neighbor)
                continue
            if neighbor in visited_neighbors:
                neighbors.remove(neighbor)
                continue

            neighbors.remove(neighbor)
            visited_neighbors.append(neighbor)
            reachable_map.append(neighbor)

            neighbors.append([neighbor[0]+1,neighbor[1]])
            neighbors.append([neighbor[0]-1,neighbor[1]])
            neighbors.append([neighbor[0],neighbor[1]+1])
            neighbors.append([neighbor[0],neighbor[1]-1])

            #print("Size:", self.map_width * self.map_height, "Visited:", len(visited_neighbors), "Reachable:", len(reachable_map), "Ratio:", len(reachable_map)/len(visited_neighbors))

        self.flood_fill_map = reachable_map
        self.get_logger().info("Completed flood fill")

    def is_reachable(self, position):
        for reachable_pos in self.flood_fill_map:
            if reachable_pos[0] == position[0] and reachable_pos[1] == position[1]:
                return True
        return False

    def exploration_callback(self):
        self.flood_fill()
        self.get_logger().info("Searching for best exploration spot...")

        # Ensure some map has been received in the last n seconds to we have some current data to work with
        if self.env_map is None:
            self.get_logger().warn("Cannot explore: no current map")
            return
        if self.our_position is None:
            self.get_logger().warn("Cannot explore: no current position")
            return
        if self.target_vector != [ 0.0, 0.0 ]:
            self.get_logger().info("Waiting for standstill...")
            return

        marker_array = MarkerArray()
        target_positions = []

        # Go through all cells of map
        for y in range(self.MARGIN, self.map_height - self.MARGIN):
            for x in range(self.MARGIN, self.map_width - self.MARGIN):
                position = [
                    self.map_origin[0] + (x + 0.5) * self.map_resolution,
                    self.map_origin[1] + (y + 0.5) * self.map_resolution
                ]

                # Check if we have been close to this position already in the past
                skip = False
                for already_visited_position in self.already_visited:
                    if self.distance(position, already_visited_position) < self.MIN_DISTANCE_BETWEEN:
                        skip = True
                if skip:
                    continue

                # Take a look at each cell and their neighbors
                cell_value = self.get_cell_at(x, y)
                neighbors = [
                    self.get_cell_at(x+1, y),
                    self.get_cell_at(x-1, y),
                    self.get_cell_at(x, y+1),
                    self.get_cell_at(x, y-1)
                ]

                empty_count = 0
                wall_count = 0
                for oy in range(-5, 5):
                    for ox in range(-5, 5):
                        other_cell = self.get_cell_at(x+ox,y+oy)
                        if other_cell == -1:
                            empty_count += 1
                        elif self.get_cell_at(x+ox,y+oy) > 0:
                            wall_count += 1

                # Only look at free cells
                if cell_value != 0 or empty_count < 10 or wall_count > 3 or not self.is_reachable([x,y]):
                    continue

                # Atleast one neighbor needs to be marked as "free" to consider the position reachable
                has_empty = False
                has_full = False
                has_wall = False
                for neighbor in neighbors:
                    if neighbor == -1:
                        has_empty = True
                    elif neighbor == 0:
                        has_full = True
                    else:
                        has_wall = True

                if not (has_empty and has_full and not has_wall):
                    continue

                # Note the position as desireable
                target_positions.append(position)

        # Get closest non-visited position
        closest_distance = None
        closest_position = None
        for target_position in target_positions:
            # Check if this position is the closest out of all possible positions
            distance = self.distance(target_position, self.our_position)
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_position = target_position

        if closest_position is None:
            self.get_logger().info("Cannot explore: no suitable position")
            return

        # Send the desired position over to navigation
        self.marker_positions = target_positions
        self.send_position(closest_position)
        self.publish_markers()

    def publish_markers(self):
        print("lol")
        marker_array = MarkerArray()

        for idx, pos in enumerate(self.marker_positions):
            marker = Marker()
            marker.header.frame_id = self.map.header.frame_id
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = "frontiers"
            marker.id = idx
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            marker.pose.position.x = float(pos[0])
            marker.pose.position.y = float(pos[1])
            marker.pose.position.z = 0.0
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 1.0
            marker.color.a = 0.8
            marker_array.markers.append(marker)

        # Marker publizieren
        if marker_array.markers:
            self.marker_pub.publish(marker_array)

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
        self.map = msg
        self.env_map = list(msg.data)
        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_origin = [ msg.info.origin.position.x, msg.info.origin.position.y ]
        self.map_resolution = msg.info.resolution
        #self.already_visited = []

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