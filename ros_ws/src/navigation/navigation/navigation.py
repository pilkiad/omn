import math
import heapq
import numpy as np

import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import (
    PoseStamped,
    PoseWithCovarianceStamped,
    Twist
)
from tf_transformations import euler_from_quaternion


class Navigation(Node):
    def _init_(self):
        super()._init_("navigation")

        self.map = None
        self.width = 0
        self.height = 0
        self.resolution = 0.0
        self.origin = None

        self.robot_x = 0.0
        self.robot_y = 0.0

        self.goal_x = None
        self.goal_y = None

        self.path = []
        self.current_waypoint = 0

        self.inflation_radius = 0.25
        self.inflated_map = None

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            "/map",
            self.map_callback,
            1
        )

        self.pose_sub = self.create_subscription(
            PoseWithCovarianceStamped,
            "/pose",
            self.pose_callback,
            1
        )

        self.goal_sub = self.create_subscription(
            PoseStamped,
            "/goal_pose",
            self.goal_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            TargetVector,
            "/target_vector",
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.navigation_loop
        )

    def map_callback(self, msg):

        self.width = msg.info.width
        self.height = msg.info.height
        self.resolution = msg.info.resolution
        self.origin = msg.info.origin.position

        self.map = np.array(msg.data).reshape(
            (self.height, self.width)
        )

        self.inflate_map()

    def pose_callback(self, msg):

        p = msg.pose.pose.position

        self.robot_x = p.x
        self.robot_y = p.y

        q = msg.pose.pose.orientation

        _, _, self.robot_yaw = euler_from_quaternion([
            q.x,
            q.y,
            q.z,
            q.w
        ])

    def goal_callback(self, msg):

        self.goal_x = msg.pose.position.x
        self.goal_y = msg.pose.position.y

        self.plan_path()

    def world_to_grid(self, x, y):

        gx = int((x - self.origin.x) / self.resolution)
        gy = int((y - self.origin.y) / self.resolution)

        return gx, gy

    def grid_to_world(self, gx, gy):

        x = gx * self.resolution + self.origin.x
        y = gy * self.resolution + self.origin.y

        return x, y

    def heuristic(self, a, b):

        return math.hypot(a[0]-b[0], a[1]-b[1])

    def neighbors(self, node):

        x, y = node

        directions = [
            (-1, 0, 1.0),
            ( 1, 0, 1.0),
            ( 0,-1, 1.0),
            ( 0, 1, 1.0),

            (-1,-1, math.sqrt(2)),
            (-1, 1, math.sqrt(2)),
            ( 1,-1, math.sqrt(2)),
            ( 1, 1, math.sqrt(2)),
        ]

        result = []

        for dx, dy, cost in directions:

            nx = x + dx
            ny = y + dy

            if not (0 <= nx < self.width and
                    0 <= ny < self.height):
                continue

            if self.inflated_map[ny][nx] == -1 or self.inflated_map[ny][nx] > 50:
                continue

            #
            # Prevent corner cutting
            #
            if abs(dx) == 1 and abs(dy) == 1:

                if self.inflated_map[y][nx] > 50:
                    continue

                if self.inflated_map[ny][x] > 50:
                    continue

            result.append(((nx, ny), cost))

        return result

    def astar(self, start, goal):

        frontier = []

        heapq.heappush(frontier, (0, start))

        came_from = {}
        cost = {}

        came_from[start] = None
        cost[start] = 0

        while frontier:

            _, current = heapq.heappop(frontier)

            if current == goal:
                break

            for nxt, move_cost in self.neighbors(current):

                new_cost = cost[current] + move_cost

                if nxt not in cost or new_cost < cost[nxt]:

                    cost[nxt] = new_cost

                    priority = new_cost + self.heuristic(
                        goal,
                        nxt
                    )

                    heapq.heappush(
                        frontier,
                        (priority, nxt)
                    )

                    came_from[nxt] = current

        if goal not in came_from:
            return []

        path = []

        node = goal

        while node is not None:

            path.append(node)
            node = came_from[node]

        path.reverse()

        return path

    def plan_path(self):

        if self.map is None:
            return

        start = self.world_to_grid(
            self.robot_x,
            self.robot_y
        )

        goal = self.world_to_grid(
            self.goal_x,
            self.goal_y
        )

        self.path = self.astar(start, goal)

        self.current_waypoint = 0

        self.get_logger().info(
            f"Planned path with {len(self.path)} cells"
        )

    def navigation_loop(self):

        if len(self.path) == 0:
            return

        if self.current_waypoint >= len(self.path):

            self.cmd_pub.publish(Twist())

            self.get_logger().info("Goal reached")

            self.path = []

            return

        gx, gy = self.path[self.current_waypoint]

        wx, wy = self.grid_to_world(gx, gy)

        dx = wx - self.robot_x
        dy = wy - self.robot_y

        distance = math.hypot(dx, dy)

        if distance < 0.10:

            self.current_waypoint += 1
            return

        desired_heading = math.atan2(dy, dx)

        #
        # This assumes robot heading = 0.
        #
        # Replace with actual yaw from odometry/TF.
        #

        heading_error = desired_heading - self.robot_yaw

        while heading_error > math.pi:
            heading_error -= 2 * math.pi

        while heading_error < -math.pi:
            heading_error += 2 * math.pi

        cmd = TargetVector()

        distance = math.hypot(dx, dy)

        heading_error = desired_heading - self.robot_yaw

        heading_error = math.atan2(
            math.sin(heading_error),
            math.cos(heading_error)
        )

        cmd.angular = 2.0 * heading_error

        if abs(heading_error) < 0.5:
            cmd.linear = min(0.35, 0.8 * distance)
        else:
            cmd.linear = 0.0

        self.cmd_pub.publish(cmd)

    def inflate_map(self):

        if self.map is None:
            return

        # Start with a copy of the original map
        self.inflated_map = self.map.copy()

        # Convert inflation radius from meters to cells
        radius_cells = math.ceil(
            self.inflation_radius / self.resolution
        )

        occupied = np.argwhere(self.map > 50)

        for y, x in occupied:

            for dy in range(-radius_cells, radius_cells + 1):
                for dx in range(-radius_cells, radius_cells + 1):

                    # Circular inflation
                    if dx*dx + dy*dy > radius_cells*radius_cells:
                        continue

                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:

                        self.inflated_map[ny][nx] = 100


def main():
    rclpy.init()
    navigation= Navigation()
    try:
        rclpy.spin(navigation)
    except KeyboardInterrupt:
        pass
    finally:
        navigation.destroy_node()
        rclpy.shutdown()


if _name_ == "_main_":
    main()