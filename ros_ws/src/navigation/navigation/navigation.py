import heapq
import math

from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Path
import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import ReliabilityPolicy


class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.has_pose = False

        self.env_map = []
        self.obstacle_distance_map = []
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
        self.ROBOT_RADIUS = 0.33
        self.ROBOT_SAFETY_MARGIN = 0.10
        # Clearance is measured from the robot center on the planning grid.
        # self.ROBOT_CLEARANCE_RADIUS = self.ROBOT_RADIUS * (1.0 + self.ROBOT_SAFETY_MARGIN)
        self.ROBOT_CLEARANCE_RADIUS = 0.7
        self.MAX_INFLATION_COST = 4.0
        self.GOAL_TOLERANCE = 0.10
        self.WAYPOINT_TOLERANCE = 0.10
        self.WAYPOINT_LOOKAHEAD = 2
        self.OFF_PATH_REPLAN_DISTANCE_CELLS = 2
        self.LINEAR_SPEED = 0.18
        self.ANGULAR_GAIN = 1.6
        self.MAX_ANGULAR_SPEED = 0.9

        planned_path_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
        )
        self.path_publisher = self.create_publisher(
            Path,
            '/planned_path',
            planned_path_qos,
        )

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
        env_map = list(msg.data)
        map_changed = (
            not self.has_map
            or self.map_width != msg.info.width
            or self.map_height != msg.info.height
            or self.map_resolution != msg.info.resolution
            or self.map_origin_x != msg.info.origin.position.x
            or self.map_origin_y != msg.info.origin.position.y
            or self.env_map != env_map
        )

        if not map_changed:
            return

        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_resolution = msg.info.resolution
        self.map_origin_x = msg.info.origin.position.x
        self.map_origin_y = msg.info.origin.position.y
        self.env_map = env_map
        self.obstacle_distance_map = self.build_obstacle_distance_map()
        self.has_map = True
        self.clear_planned_path()

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
        self.get_logger().info(
            f'Received goal pose x={self.goal_x:.3f}, y={self.goal_y:.3f}'
        )
        self.clear_planned_path()

    def publish_planned_path(self):
        msg = Path()
        msg.header.frame_id = 'map'
        msg.header.stamp = self.get_clock().now().to_msg()

        for x, y in self.path:
            pose = PoseStamped()
            pose.header.frame_id = msg.header.frame_id
            pose.header.stamp = msg.header.stamp
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation.w = 1.0
            msg.poses.append(pose)

        self.path_publisher.publish(msg)

    def clear_planned_path(self):
        self.path = []
        self.path_grid = []
        self.last_planned_start = None
        self.last_planned_goal = None
        self.publish_planned_path()

    def timer_callback(self):
        msg = TargetVector()

        if not self.ready_to_plan():
            self.publisher.publish(msg)
            return

        if self.distance(self.x, self.y, self.goal_x, self.goal_y) <= self.GOAL_TOLERANCE:
            self.clear_planned_path()
            self.has_goal = False
            self.publisher.publish(msg)
            self.get_logger().info('Goal succeeded')
            return

        start = self.world_to_grid(self.x, self.y)
        goal = self.world_to_grid(self.goal_x, self.goal_y)

        if start is None or goal is None:
            self.clear_planned_path()
            self.publisher.publish(msg)
            self.get_logger().warn('Robot or goal is outside the map')
            return

        replan_reason = self.replan_reason(start, goal)

        if replan_reason is not None:
            planned_path_grid = self.a_star(start, goal)
            self.get_logger().info(
                f'Planned path with {len(planned_path_grid)} cells; '
                f'reason={replan_reason}'
            )

            if not planned_path_grid:
                self.clear_planned_path()
                self.publisher.publish(msg)
                self.get_logger().warn(
                    'No path to goal found; '
                    f'reason={replan_reason} '
                    f'start={start} raw_free={self.is_raw_free(start)} '
                    f'traversable={self.is_traversable(start)} '
                    f'goal={goal} raw_free={self.is_raw_free(goal)} '
                    f'traversable={self.is_traversable(goal)}'
                )
                return

            self.path_grid = planned_path_grid
            self.path = [self.grid_to_world(cell) for cell in self.path_grid]
            self.last_planned_start = start
            self.last_planned_goal = goal
            self.publish_planned_path()

        if not self.path:
            self.publisher.publish(msg)
            self.get_logger().warn(
                'No path to goal found; '
                f'start={start} raw_free={self.is_raw_free(start)} '
                f'traversable={self.is_traversable(start)} '
                f'goal={goal} raw_free={self.is_raw_free(goal)} '
                f'traversable={self.is_traversable(goal)}'
            )
            return

        waypoint = self.next_waypoint()
        linear, angular = self.target_vector_to_waypoint(waypoint)
        msg.linear = linear
        msg.angular = angular
        self.publisher.publish(msg)

    def ready_to_plan(self):
        return self.has_map and self.has_pose and self.has_goal

    def replan_reason(self, start, goal):
        if not self.path or not self.path_grid:
            return 'no current path'

        if goal != self.last_planned_goal:
            return 'goal changed'

        if self.path_is_blocked(start, goal):
            return 'path blocked'

        if self.distance_to_path_grid(start) > self.OFF_PATH_REPLAN_DISTANCE_CELLS:
            return 'robot off path'

        return None

    def path_is_blocked(self, start, goal):
        for cell in self.path_grid:
            if cell == start or cell == goal:
                if not self.is_raw_free(cell):
                    return True
                continue

            if not self.is_traversable(cell):
                return True

        return False

    def distance_to_path_grid(self, cell):
        if not self.path_grid:
            return math.inf

        return min(
            math.hypot(cell[0] - path_cell[0], cell[1] - path_cell[1])
            for path_cell in self.path_grid
        )

    def a_star(self, start, goal):
        if not self.is_raw_free(start) or not self.is_raw_free(goal):
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

            for neighbor, step_cost in self.neighbors(current, goal):
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

    def neighbors(self, cell, goal):
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
                if not self.is_traversable(adjacent_x) or not self.is_traversable(adjacent_y):
                    continue

            if self.is_traversable(neighbor) or (neighbor == goal and self.is_raw_free(neighbor)):
                yield neighbor, cost + self.inflation_penalty(neighbor)

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
        return self.is_traversable(cell) and not self.is_inflated(cell)

    def is_traversable(self, cell):
        return self.is_raw_free(cell) and self.has_map_edge_clearance(cell)

    def inflation_penalty(self, cell):
        if self.ROBOT_CLEARANCE_RADIUS <= 0.0:
            return 0.0

        obstacle_distance = self.obstacle_distance(cell)
        if obstacle_distance >= self.ROBOT_CLEARANCE_RADIUS:
            return 0.0

        closeness = (
            self.ROBOT_CLEARANCE_RADIUS - obstacle_distance
        ) / self.ROBOT_CLEARANCE_RADIUS
        return self.MAX_INFLATION_COST * closeness * closeness

    def is_inflated(self, cell):
        return self.obstacle_distance(cell) < self.ROBOT_CLEARANCE_RADIUS

    def obstacle_distance(self, cell):
        if len(self.obstacle_distance_map) != len(self.env_map):
            return math.inf

        if not self.in_bounds(cell):
            return math.inf

        index = self.map_index(cell)
        if index >= len(self.obstacle_distance_map):
            return math.inf

        return self.obstacle_distance_map[index]

    def is_raw_free(self, cell):
        if not self.in_bounds(cell):
            return False

        index = self.map_index(cell)
        if index >= len(self.env_map):
            return False

        return not self.raw_value_blocked(self.env_map[index])

    def build_obstacle_distance_map(self):
        obstacle_distance_map = [math.inf] * len(self.env_map)
        if not self.env_map or self.map_width <= 0 or self.map_height <= 0:
            return obstacle_distance_map

        offsets = self.inflation_offsets()
        for index, value in enumerate(self.env_map):
            if not self.raw_value_blocked(value):
                continue

            obstacle_x = index % self.map_width
            obstacle_y = index // self.map_width
            for dx, dy, distance in offsets:
                nearby_cell = (obstacle_x + dx, obstacle_y + dy)
                if not self.in_bounds(nearby_cell):
                    continue

                nearby_index = self.map_index(nearby_cell)
                obstacle_distance_map[nearby_index] = min(
                    obstacle_distance_map[nearby_index],
                    distance,
                )

        return obstacle_distance_map

    def inflation_offsets(self):
        if self.map_resolution <= 0.0:
            return [(0, 0, 0.0)]

        clearance_cells = self.clearance_cells()
        offsets = []
        for dy in range(-clearance_cells, clearance_cells + 1):
            for dx in range(-clearance_cells, clearance_cells + 1):
                cell_distance = math.hypot(dx, dy)
                if cell_distance <= clearance_cells:
                    offsets.append((dx, dy, cell_distance * self.map_resolution))

        return offsets

    def has_map_edge_clearance(self, cell):
        if self.map_resolution <= 0.0:
            return False

        x, y = cell
        clearance_cells = self.clearance_cells()
        return (
            x >= clearance_cells
            and y >= clearance_cells
            and x < self.map_width - clearance_cells
            and y < self.map_height - clearance_cells
        )

    def clearance_cells(self):
        if self.map_resolution <= 0.0:
            return 0

        return math.ceil(self.ROBOT_CLEARANCE_RADIUS / self.map_resolution)

    def raw_value_blocked(self, value):
        return value < 0 or value >= self.OCCUPIED_THRESHOLD

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
        try:
            if rclpy.ok():
                navigation.publisher.publish(TargetVector())
        except Exception:
            pass
        try:
            navigation.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()
