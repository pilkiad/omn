"""Tests for navigation path replanning decisions."""

import importlib
import sys
import types


class _Header:
    def __init__(self):
        self.frame_id = ''
        self.stamp = None


class _Position:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0


class _Orientation:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 1.0


class _Pose:
    def __init__(self):
        self.position = _Position()
        self.orientation = _Orientation()


class _PoseStamped:
    def __init__(self):
        self.header = _Header()
        self.pose = _Pose()


class _Path:
    def __init__(self):
        self.header = _Header()
        self.poses = []


class _OccupancyGrid:
    pass


class _TargetVector:
    def __init__(self):
        self.linear = 0.0
        self.angular = 0.0


class _Node:
    def __init__(self, *args, **kwargs):
        pass


class _QoSProfile:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class _Publisher:
    def __init__(self):
        self.messages = []

    def publish(self, msg):
        self.messages.append(msg)


class _Logger:
    def __init__(self):
        self.infos = []
        self.warnings = []

    def info(self, msg):
        self.infos.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


class _Clock:
    def now(self):
        return self

    def to_msg(self):
        return object()


def _install_ros_stubs():
    collision_interfaces = types.ModuleType('collision_interfaces')
    collision_msg = types.ModuleType('collision_interfaces.msg')
    collision_msg.TargetVector = _TargetVector
    collision_interfaces.msg = collision_msg
    sys.modules['collision_interfaces'] = collision_interfaces
    sys.modules['collision_interfaces.msg'] = collision_msg

    geometry_msgs = types.ModuleType('geometry_msgs')
    geometry_msg = types.ModuleType('geometry_msgs.msg')
    geometry_msg.PoseStamped = _PoseStamped
    geometry_msgs.msg = geometry_msg
    sys.modules['geometry_msgs'] = geometry_msgs
    sys.modules['geometry_msgs.msg'] = geometry_msg

    nav_msgs = types.ModuleType('nav_msgs')
    nav_msg = types.ModuleType('nav_msgs.msg')
    nav_msg.OccupancyGrid = _OccupancyGrid
    nav_msg.Path = _Path
    nav_msgs.msg = nav_msg
    sys.modules['nav_msgs'] = nav_msgs
    sys.modules['nav_msgs.msg'] = nav_msg

    rclpy = types.ModuleType('rclpy')
    rclpy.init = lambda: None
    rclpy.spin = lambda node: None
    rclpy.ok = lambda: False
    rclpy.shutdown = lambda: None
    rclpy_time = types.ModuleType('rclpy.time')
    rclpy_time.Time = lambda: object()
    rclpy.time = rclpy_time
    rclpy_node = types.ModuleType('rclpy.node')
    rclpy_node.Node = _Node
    rclpy.node = rclpy_node
    sys.modules['rclpy'] = rclpy
    sys.modules['rclpy.node'] = rclpy_node
    sys.modules['rclpy.time'] = rclpy_time

    rclpy_qos = types.ModuleType('rclpy.qos')
    rclpy_qos.DurabilityPolicy = types.SimpleNamespace(
        TRANSIENT_LOCAL=object(),
    )
    rclpy_qos.QoSProfile = _QoSProfile
    rclpy_qos.ReliabilityPolicy = types.SimpleNamespace(RELIABLE=object())
    sys.modules['rclpy.qos'] = rclpy_qos

    tf2_ros = types.ModuleType('tf2_ros')
    tf2_ros.Buffer = lambda *args, **kwargs: object()
    tf2_ros.TransformListener = lambda *args, **kwargs: object()
    sys.modules['tf2_ros'] = tf2_ros


_install_ros_stubs()
Navigation = importlib.import_module('navigation.navigation').Navigation


def _make_navigation(path_grid, goal=None):
    if goal is None:
        goal = path_grid[-1] if path_grid else (0, 0)

    nav = Navigation.__new__(Navigation)
    nav.x = 0.5
    nav.y = 0.5
    nav.yaw = 0.0
    nav.has_pose = True
    nav.has_map = True
    nav.has_goal = True

    nav.map_width = 20
    nav.map_height = 20
    nav.map_resolution = 1.0
    nav.map_origin_x = 0.0
    nav.map_origin_y = 0.0
    nav.env_map = [0] * (nav.map_width * nav.map_height)
    nav.obstacle_distance_map = []

    nav.GOAL_TOLERANCE = 0.01
    nav.WAYPOINT_TOLERANCE = 0.2
    nav.WAYPOINT_LOOKAHEAD = 1
    nav.OFF_PATH_REPLAN_DISTANCE_CELLS = 2
    nav.LINEAR_SPEED = 0.18
    nav.ANGULAR_GAIN = 1.6
    nav.MAX_ANGULAR_SPEED = 0.9

    nav.goal_x, nav.goal_y = nav.grid_to_world(goal)
    nav.path_grid = list(path_grid)
    nav.path = [nav.grid_to_world(cell) for cell in nav.path_grid]
    nav.last_planned_start = path_grid[0] if path_grid else None
    nav.last_planned_goal = goal

    nav.publisher = _Publisher()
    nav.path_publisher = _Publisher()
    nav.logger = _Logger()
    nav.get_logger = lambda: nav.logger
    nav.get_clock = lambda: _Clock()
    nav.is_raw_free = lambda cell: True
    nav.is_traversable = lambda cell: True

    return nav


def _set_robot_cell(nav, cell):
    nav.x, nav.y = nav.grid_to_world(cell)


def test_moving_to_next_grid_cell_on_path_does_not_replan():
    nav = _make_navigation([(0, 0), (1, 0), (2, 0)])

    assert nav.replan_reason((1, 0), (2, 0)) is None


def test_empty_path_triggers_replan():
    nav = _make_navigation([], goal=(4, 0))

    assert nav.replan_reason((0, 0), (4, 0)) == 'no current path'


def test_changed_goal_triggers_replan():
    nav = _make_navigation([(0, 0), (1, 0), (2, 0)])

    assert nav.replan_reason((0, 0), (3, 0)) == 'goal changed'


def test_blocked_remaining_path_triggers_replan():
    nav = _make_navigation([(0, 0), (1, 0), (2, 0)])
    nav.is_traversable = lambda cell: cell != (1, 0)

    assert nav.replan_reason((0, 0), (2, 0)) == 'path blocked'


def test_robot_far_from_remaining_path_triggers_replan():
    nav = _make_navigation([(0, 0), (1, 0)])

    assert nav.replan_reason((4, 0), (1, 0)) == 'robot off path'


def test_robot_within_two_cells_of_remaining_path_does_not_replan():
    nav = _make_navigation([(0, 0), (5, 0)])

    assert nav.replan_reason((2, 0), (5, 0)) is None


def test_timer_does_not_replan_while_advancing_along_valid_path():
    nav = _make_navigation([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    calls = []

    def a_star(start, goal):
        calls.append((start, goal))
        return []

    nav.a_star = a_star

    for cell in [(0, 0), (1, 0), (2, 0)]:
        _set_robot_cell(nav, cell)
        nav.timer_callback()

    assert calls == []
    assert len(nav.publisher.messages) == 3


def test_failed_replan_stops_and_clears_invalid_path():
    nav = _make_navigation([(0, 0), (1, 0), (2, 0)])
    nav.goal_x, nav.goal_y = nav.grid_to_world((3, 0))
    calls = []

    def a_star(start, goal):
        calls.append((start, goal))
        return []

    nav.a_star = a_star
    _set_robot_cell(nav, (0, 0))
    nav.timer_callback()

    assert calls == [((0, 0), (3, 0))]
    assert nav.path == []
    assert nav.path_grid == []
    assert nav.publisher.messages[-1].linear == 0.0
    assert nav.publisher.messages[-1].angular == 0.0
