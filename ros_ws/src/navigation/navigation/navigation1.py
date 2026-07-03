import heapq
import math

from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
import rclpy
from rclpy.node import Node


class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.has_pose = False

        self.env_map = []
        self.map_width = 0
        self.map_height = 0
        self.map_resolution = 0.0
        self.map_origin_x = 0.0
        self.map_origin_y = 0.0
        self.has_map = False

        self.goal_x = 0.0
        self.goal_y = 0.0
        self.has_goal = False

        self.path = []
        self.path_grid = []
        self.last_planned_start = None
        self.last_planned_goal = None

        self.OCCUPIED_THRESHOLD = 50
        self.GOAL_TOLERANCE = 0.12
        self.WAYPOINT_TOLERANCE = 0.10
        self.WAYPOINT_LOOKAHEAD = 4
        self.LINEAR_SPEED = 0.12
        self.ANGULAR_GAIN = 1.6
        self.MAX_ANGULAR_SPEED = 0.7

        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            1
        )

        self.pos_subscription = self.create_subscription(
            PoseStamped,
            '/pos',
            self.pos_callback,
            1
        )

        self.goal_pose_subscription = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_pose_callback,
            1
        )

        self.publisher = self.create_publisher(TargetVector, '/target_vector', 1)
        self.timer = self.create_timer(0.2, self.timer_callback)

    def map_callback(self, msg):
        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_resolution = msg.info.resolution
        self.map_origin_x = msg.info.origin.position.x
        self.map_origin_y = msg.info.origin.position.y
        self.env_map = list(msg.data)
        self.has_map = True
        self.path = []
        self.path_grid = []
        self.last_planned_start = None
        self.last_planned_goal = None

    def pos_callback(self, msg):
        self.update_pose(msg.pose)

    def update_pose(self, pose):
        self.x = pose.position.x
        self.y = pose.position.y
        self.yaw = self.yaw_from_quaternion(pose.orientation)
        self.has_pose = True

    def goal_pose_callback(self, msg):
        self.goal_x = msg.pose.position.x
        self.goal_y = msg.pose.position.y
        self.has_goal = True
        self.path = []
        self.path_grid = []
        self.last_planned_goal = None

    def timer_callback(self):
        msg = TargetVector()

        if not self.ready_to_plan():
            self.publisher.publish(msg)
            return

        if self.distance(self.x, self.y, self.goal_x, self.goal_y) <= self.GOAL_TOLERANCE:
            self.path = []
            self.path_grid = []
            self.publisher.publish(msg)
            return

        start = self.world_to_grid(self.x, self.y)
        goal = self.world_to_grid(self.goal_x, self.goal_y)

        if start is None or goal is None:
            self.publisher.publish(msg)
            self.get_logger().warn('Robot or goal is outside the map')
            return

        should_replan = (
            not self.path
            or start != self.last_planned_start
            or goal != self.last_planned_goal
        )

        if should_replan:
            self.path_grid = self.a_star(start, goal)
            self.path = [self.grid_to_world(cell) for cell in self.path_grid]
            self.last_planned_start = start
            self.last_planned_goal = goal

        if not self.path:
            self.publisher.publish(msg)
            self.get_logger().warn('No path to goal found')
            return

        waypoint = self.next_waypoint()
        linear, angular = self.target_vector_to_waypoint(waypoint)
        msg.linear = linear
        msg.angular = angular
        self.publisher.publish(msg)

    def ready_to_plan(self):
        return self.has_map and self.has_pose and self.has_goal

    def a_star(self, start, goal):
        if not self.is_free(start) or not self.is_free(goal):
            return []

        open_set = []
        heapq.heappush(open_set, (0.0, start))
        came_from = {}
        g_score = {start: 0.0}
        closed = set()

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            if current in closed:
                continue
            closed.add(current)

            for neighbor, step_cost in self.neighbors(current):
                if neighbor in closed:
                    continue

                new_score = g_score[current] + step_cost
                if new_score >= g_score.get(neighbor, math.inf):
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = new_score
                f_score = new_score + self.heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

        return []

    def neighbors(self, cell):
        x, y = cell
        directions = [
            (-1, 0, 1.0),
            (1, 0, 1.0),
            (0, -1, 1.0),
            (0, 1, 1.0),
            (-1, -1, math.sqrt(2.0)),
            (-1, 1, math.sqrt(2.0)),
            (1, -1, math.sqrt(2.0)),
            (1, 1, math.sqrt(2.0)),
        ]

        for dx, dy, cost in directions:
            neighbor = (x + dx, y + dy)
            if dx != 0 and dy != 0:
                adjacent_x = (x + dx, y)
                adjacent_y = (x, y + dy)
                if not self.is_free(adjacent_x) or not self.is_free(adjacent_y):
                    continue

            if self.is_free(neighbor):
                yield neighbor, cost

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def next_waypoint(self):
        while len(self.path) > 1:
            waypoint_x, waypoint_y = self.path[0]
            if self.distance(self.x, self.y, waypoint_x, waypoint_y) > self.WAYPOINT_TOLERANCE:
                break
            self.path.pop(0)
            self.path_grid.pop(0)

        index = min(self.WAYPOINT_LOOKAHEAD, len(self.path) - 1)
        return self.path[index]

    def target_vector_to_waypoint(self, waypoint):
        waypoint_x, waypoint_y = waypoint
        dx = waypoint_x - self.x
        dy = waypoint_y - self.y
        distance_to_waypoint = math.hypot(dx, dy)

        desired_yaw = math.atan2(dy, dx)
        yaw_error = self.normalize_angle(desired_yaw - self.yaw)

        angular = self.clamp(
            yaw_error * self.ANGULAR_GAIN,
            -self.MAX_ANGULAR_SPEED,
            self.MAX_ANGULAR_SPEED
        )

        turn_scale = max(0.0, 1.0 - abs(yaw_error) / (math.pi / 2.0))
        linear = min(self.LINEAR_SPEED, distance_to_waypoint) * turn_scale

        return linear, angular

    def world_to_grid(self, x, y):
        if self.map_resolution <= 0.0:
            return None

        grid_x = math.floor((x - self.map_origin_x) / self.map_resolution)
        grid_y = math.floor((y - self.map_origin_y) / self.map_resolution)
        cell = (grid_x, grid_y)

        if not self.in_bounds(cell):
            return None
        return cell

    def grid_to_world(self, cell):
        x, y = cell
        return (
            self.map_origin_x + (x + 0.5) * self.map_resolution,
            self.map_origin_y + (y + 0.5) * self.map_resolution,
        )

    def is_free(self, cell):
        if not self.in_bounds(cell):
            return False

        value = self.env_map[self.map_index(cell)]
        return value >= 0 and value < self.OCCUPIED_THRESHOLD

    def in_bounds(self, cell):
        x, y = cell
        return 0 <= x < self.map_width and 0 <= y < self.map_height

    def map_index(self, cell):
        x, y = cell
        return y * self.map_width + x

    def heuristic(self, cell, goal):
        return math.hypot(goal[0] - cell[0], goal[1] - cell[1])

    def yaw_from_quaternion(self, q):
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        return math.atan2(siny_cosp, cosy_cosp)

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def clamp(self, value, minimum, maximum):
        return max(minimum, min(value, maximum))


def main():
    rclpy.init()
    navigation = Navigation()
    try:
        rclpy.spin(navigation)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = TargetVector()
        navigation.publisher.publish(stop_msg)
        navigation.destroy_node()
        rclpy.shutdown()
