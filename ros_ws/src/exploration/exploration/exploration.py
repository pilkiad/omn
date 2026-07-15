import rclpy
from rclpy.lifecycle import LifecycleNode, State, TransitionCallbackReturn

from geometry_msgs.msg import PoseStamped
from collision_interfaces.msg import TargetVector
from nav_msgs.msg import OccupancyGrid
from visualization_msgs.msg import Marker, MarkerArray
from tf2_ros import TransformListener, Buffer

import math
import random
import time
from collections import deque

class Exploration(LifecycleNode):
    def __init__(self):
        super().__init__("exploration")

        self.MIN_DISTANCE_BETWEEN = 1.0 # Minimum distance a desirable position has to have to all previously explored positions
        self.MIN_DISTANCE_BETWEEN_SQ = self.MIN_DISTANCE_BETWEEN ** 2
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

    # ---------------------------
    # LIFECYCLE
    # ---------------------------
    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Configuring exploration node")

        self.publisher = self.create_lifecycle_publisher(PoseStamped, "/goal_pose", 1)
        self.map_subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 1)
        self.target_vector_subscription = self.create_subscription(TargetVector, '/target_vector', self.target_vector_callback, 1)
        self.exploration_time = self.create_timer(10, self.exploration_callback)
        self.marker_pub = self.create_lifecycle_publisher(MarkerArray, '/exploration_markers', 1)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.tf_timer = self.create_timer(0.1, self.get_tf)

        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State):
        self.get_logger().info("Activating exploration node")
        return super().on_activate(state)

    def on_deactivate(self, state: State):
        self.get_logger().info("Deactivating exploration node")
        return super().on_deactivate(state)

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Cleaning up exploration node")

        self.destroy_lifecycle_publisher(self.publisher)
        self.destroy_subscription(self.map_subscription)
        self.destroy_subscription(self.target_vector_subscription)
        self.destroy_timer(self.exploration_time)
        self.destroy_lifecycle_publisher(self.marker_pub)
        self.destroy_timer(self.tf_timer)

        return TransitionCallbackReturn.SUCCESS

    def target_vector_callback(self, msg):
        self.target_vector = [ msg.linear, msg.angular ]

    def get_cell_at(self, x, y):
        index = (y * self.map_width) + x
        if index < 0 or index > len(self.env_map):
            return -1
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
        neighbors = deque([start_pos])
        visited_neighbors = set()
        reachable_map = set()

        while len(neighbors) > 0:
            neighbor = neighbors.popleft()
            cell = self.get_cell_at(neighbor[0], neighbor[1])

            if neighbor in visited_neighbors:
                continue

            visited_neighbors.add(neighbor)

            if cell != 0:
                continue

            reachable_map.add(neighbor)

            neighbors.append((neighbor[0]+1,neighbor[1]))
            neighbors.append((neighbor[0]-1,neighbor[1]))
            neighbors.append((neighbor[0],neighbor[1]+1))
            neighbors.append((neighbor[0],neighbor[1]-1))

        self.flood_fill_map = reachable_map
        self.get_logger().info("Completed flood fill")

    def is_reachable(self, position):
        return (position[0], position[1]) in self.flood_fill_map

    def exploration_callback(self):
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

        self.flood_fill()
        self.get_logger().info("Searching for best exploration spot...")

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
                    dx = position[0] - already_visited_position[0]
                    dy = position[1] - already_visited_position[1]
                    if dx*dx + dy*dy < self.MIN_DISTANCE_BETWEEN_SQ:
                        skip = True
                        break
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

                empty_count = 0
                wall_count = 0
                for oy in range(-5, 5):
                    for ox in range(-5, 5):
                        other_cell = self.get_cell_at(x+ox,y+oy)
                        if other_cell == -1:
                            empty_count += 1
                        elif other_cell > 0:
                            wall_count += 1

                # Only look at free cells
                if cell_value != 0 or empty_count < 10 or wall_count > 3 or not self.is_reachable([x,y]):
                    continue

                # Note the position as desireable
                target_positions.append(position)

        # Get closest non-visited position
        closest_distance_sq = None
        closest_position = None
        for target_position in target_positions:
            dx = target_position[0] - self.our_position[0]
            dy = target_position[1] - self.our_position[1]
            distance_sq = dx*dx + dy*dy
            if closest_distance_sq is None or distance_sq > closest_distance_sq:
                closest_distance_sq = distance_sq
                closest_position = target_position

        if closest_position is None:
            self.get_logger().info("Cannot explore: no suitable position")
            return

        # Send the desired position over to navigation
        self.marker_positions = target_positions
        self.send_position(closest_position)
        self.publish_markers()

    def publish_markers(self):
        if not self.publisher.is_activated:
            return

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

        if marker_array.markers:
            self.marker_pub.publish(marker_array)

    def send_position(self, position):
        if not self.publisher.is_activated:
            return

        self.already_visited.append(position)
        msg = PoseStamped()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.position.x = position[0]
        msg.pose.position.y = position[1]
        self.get_logger().info(f"Exploring at: {position}")
        self.publisher.publish(msg)

    def get_tf(self):
        try:
            t = self.tf_buffer.lookup_transform("map", "base_footprint", rclpy.time.Time())
            self.our_position = [ t.transform.translation.x, t.transform.translation.y ]
        except Exception as e:
            pass

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

    exploration.trigger_configure()
    exploration.trigger_activate()

    try:
        rclpy.spin(exploration)
    except KeyboardInterrupt:
        pass
    finally:
        exploration.trigger_deactivate()
        exploration.trigger_cleanup()
        exploration.destroy_node()
        rclpy.shutdown()