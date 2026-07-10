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

    def warning(self, msg):
        self.warnings.append(msg)


class _Clock:
    def __init__(self, seconds=0.0):
        self.seconds = seconds

    def now(self):
        return self

    @property
    def nanoseconds(self):
        return int(self.seconds * 1_000_000_000)

    def to_msg(self):
        return object()

    def advance(self, seconds):
        self.seconds += seconds


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
    nav.last_pose_time = 0.0
    nav.last_goal_time = 0.0

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

    nav.STATUS_HEARTBEAT_SEC = 2.0
    nav.state = 'idle'
    nav.blocking_reason = 'none'
    nav.tf_ok = False
    nav.tf_map_frame = 'map'
    nav.tf_robot_frame = 'base_footprint'
    nav.tf_error = 'not_checked'
    nav._last_status_signature = None
    nav._last_status_log_time = None
    nav._last_planning_context = None

    nav.publisher = _Publisher()
    nav.path_publisher = _Publisher()
    nav.logger = _Logger()
    nav.clock = _Clock()
    nav.get_logger = lambda: nav.logger
    nav.get_clock = lambda: nav.clock
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


def test_readiness_status_prioritizes_map_pose_and_goal():
    nav = _make_navigation([(0, 0), (1, 0)])
    nav.has_map = False
    nav.has_pose = False
    nav.has_goal = False

    assert nav.readiness_status() == ('waiting_for_map', 'map_missing')

    nav.has_map = True
    assert nav.readiness_status() == ('waiting_for_pose', 'pose_missing')

    nav.has_pose = True
    assert nav.readiness_status() == ('waiting_for_goal', 'goal_missing')

    nav.has_goal = True
    assert nav.readiness_status() is None


def test_status_log_is_compact_and_uses_two_second_heartbeat():
    nav = _make_navigation([(0, 0), (1, 0)])
    nav.clock.seconds = 10.0
    nav.last_pose_time = 9.25
    nav.last_goal_time = 8.0
    nav.tf_ok = True
    nav.tf_error = 'none'

    nav.set_status('tracking')

    assert len(nav.logger.infos) == 1
    message = nav.logger.infos[-1]
    assert 'state=tracking' in message
    assert 'blocking_reason=none' in message
    assert 'has_map=true' in message
    assert 'has_pose=true' in message
    assert 'has_goal=true' in message
    assert 'ready_to_plan=true' in message
    assert 'start_cell=(0,0)' in message
    assert 'pose_age_sec=0.75' in message
    assert 'goal_cell=(1,0)' in message
    assert 'goal_age_sec=2.00' in message
    assert 'tf_ok=true' in message
    assert 'tf_map_frame=map' in message
    assert 'tf_robot_frame=base_footprint' in message
    assert 'tf_error=none' in message

    nav.clock.advance(1.0)
    nav.set_status('tracking')
    assert len(nav.logger.infos) == 1

    nav.clock.advance(1.1)
    nav.set_status('tracking')
    assert len(nav.logger.infos) == 2


def test_repeated_failed_replan_does_not_spam_planning_or_no_path():
    nav = _make_navigation([], goal=(4, 0))
    nav.a_star = lambda start, goal: []

    nav.timer_callback()

    assert len(nav.logger.infos) == 1
    assert 'state=planning' in nav.logger.infos[-1]
    assert len(nav.logger.warnings) == 1
    assert 'state=no_path' in nav.logger.warnings[-1]
    assert 'blocking_reason=astar_exhausted' in nav.logger.warnings[-1]

    nav.timer_callback()
    assert len(nav.logger.infos) == 1
    assert len(nav.logger.warnings) == 1

    nav.clock.advance(2.1)
    nav.timer_callback()
    assert len(nav.logger.infos) == 1
    assert len(nav.logger.warnings) == 2


def test_timer_reports_outside_map_and_goal_succeeded():
    nav = _make_navigation([(0, 0), (1, 0)])
    nav.x = -1.0
    nav.timer_callback()

    assert nav.state == 'outside_map'
    assert nav.blocking_reason == 'start_outside'
    assert 'state=outside_map' in nav.logger.warnings[-1]

    nav = _make_navigation([(0, 0)], goal=(0, 0))
    nav.timer_callback()

    assert nav.state == 'goal_succeeded'
    assert nav.has_goal is False
    assert 'state=goal_succeeded' in nav.logger.infos[-1]


def test_pose_and_goal_callbacks_record_receive_time():
    nav = _make_navigation([(0, 0), (1, 0)])
    pose = _Pose()
    nav.clock.seconds = 4.0

    nav.update_pose(pose)
    assert nav.last_pose_time == 4.0

    nav.clock.advance(3.0)
    goal = _PoseStamped()
    nav.goal_pose_callback(goal)
    assert nav.last_goal_time == 7.0


def test_tf_failure_logs_once_and_sanitizes_error():
    nav = _make_navigation([(0, 0), (1, 0)])
    nav.state = 'tracking'
    nav.tf_ok = True
    nav.tf_error = 'none'

    class FailingBuffer:
        def __init__(self):
            self.message = 'missing\ntransform'

        def lookup_transform(self, *args):
            raise RuntimeError(self.message)

    nav.tf_buffer = FailingBuffer()
    nav.get_tf()

    assert len(nav.logger.warnings) == 1
    assert 'tf_ok=false' in nav.logger.warnings[-1]
    assert 'tf_error="missing transform"' in nav.logger.warnings[-1]

    nav.tf_buffer.message = 'still missing'
    nav.get_tf()
    assert len(nav.logger.warnings) == 1

    transform = types.SimpleNamespace(
        transform=types.SimpleNamespace(
            translation=types.SimpleNamespace(x=0.5, y=0.5),
            rotation=_Orientation(),
        ),
    )
    nav.clock.advance(1.0)
    nav.tf_buffer = types.SimpleNamespace(
        lookup_transform=lambda *args: transform,
    )
    nav.get_tf()
    nav.timer_callback()

    assert nav.tf_ok is True
    assert nav.tf_error == 'none'
    assert nav.last_pose_time == 1.0
    assert 'tf_ok=true' in nav.logger.infos[-1]
