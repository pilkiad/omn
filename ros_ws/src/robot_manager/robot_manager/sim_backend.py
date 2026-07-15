"""Simulated robot backend for the dashboard.

Runs the exact same lifecycle / health / task / SLAM-metric core as the real
ROS 2 node, but against a simulated Tortugabot, so the whole dashboard can be
demonstrated and tested on any machine without ROS installed.

The simulator loads the recorded map (``my_map_1.pgm``/``.yaml``) if it can
find one, drives a simulated robot through the full mission lifecycle
(initialize -> map with SLAM "reveal" -> save map -> ready -> navigate), and
feeds the health monitor with realistic message beats. Faults can be injected
from the dashboard to demonstrate the FAULT / recovery path.

No third-party dependencies (stdlib only, no numpy) so it runs everywhere.
"""

import base64
import heapq
import math
import os
import random
import threading
import time

from .health_monitor import HealthMonitor
from .lifecycle import RobotEvent, RobotLifecycle, RobotState
from .slam_metrics import SlamMetrics
from .task_manager import (
    TASK_EXPLORE, TASK_FOLLOW_RED, TASK_MAP, TASK_NAVIGATE, TaskManager,
)

FREE = 0
OCCUPIED = 100
UNKNOWN = -1

# Byte encoding used for the dashboard map payload.
_CELL_BYTE = {FREE: 0, OCCUPIED: 100, UNKNOWN: 255}


# ---------------------------------------------------------------------------
# Map loading
# ---------------------------------------------------------------------------

def _parse_pgm(path):
    """Minimal P5 PGM parser. Returns (width, height, bytearray)."""
    with open(path, 'rb') as handle:
        data = handle.read()

    # Tokenize the header (magic, width, height, maxval), skipping comments.
    tokens = []
    index = 0
    while len(tokens) < 4:
        while index < len(data) and data[index:index + 1].isspace():
            index += 1
        if data[index:index + 1] == b'#':
            while index < len(data) and data[index] != 0x0A:
                index += 1
            continue
        start = index
        while index < len(data) and not data[index:index + 1].isspace():
            index += 1
        tokens.append(data[start:index])
    index += 1  # single whitespace after maxval

    if tokens[0] != b'P5':
        raise ValueError('not a binary PGM (P5) file: %s' % path)
    width, height = int(tokens[1]), int(tokens[2])
    return width, height, bytearray(data[index:index + width * height])


def _parse_map_yaml(path):
    """Tiny parser for the standard map_server YAML (no yaml dependency)."""
    values = {'resolution': 0.05, 'origin': [0.0, 0.0, 0.0],
              'occupied_thresh': 0.65, 'free_thresh': 0.196, 'negate': 0}
    with open(path, 'r', encoding='utf-8') as handle:
        for line in handle:
            line = line.strip()
            if ':' not in line or line.startswith('#'):
                continue
            key, _, raw = line.partition(':')
            key = key.strip()
            raw = raw.strip()
            if key == 'origin':
                raw = raw.strip('[]')
                values['origin'] = [float(part) for part in raw.split(',')]
            elif key in ('resolution', 'occupied_thresh', 'free_thresh'):
                values[key] = float(raw)
            elif key == 'negate':
                values[key] = int(raw)
    return values


class GridMap:
    """ROS-style occupancy grid: row-major, cell (0,0) at origin corner."""

    def __init__(self, width, height, resolution, origin_x, origin_y, cells):
        self.width = width
        self.height = height
        self.resolution = resolution
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.cells = cells  # list of FREE / OCCUPIED / UNKNOWN

    def index(self, gx, gy):
        return gy * self.width + gx

    def in_bounds(self, gx, gy):
        return 0 <= gx < self.width and 0 <= gy < self.height

    def cell(self, gx, gy):
        return self.cells[self.index(gx, gy)]

    def world_to_grid(self, x, y):
        gx = int(math.floor((x - self.origin_x) / self.resolution))
        gy = int(math.floor((y - self.origin_y) / self.resolution))
        if not self.in_bounds(gx, gy):
            return None
        return gx, gy

    def grid_to_world(self, gx, gy):
        return (
            self.origin_x + (gx + 0.5) * self.resolution,
            self.origin_y + (gy + 0.5) * self.resolution,
        )

    @classmethod
    def load(cls, pgm_path, yaml_path, max_dimension=340):
        width, height, pixels = _parse_pgm(pgm_path)
        meta = _parse_map_yaml(yaml_path)
        occupied_thresh = meta['occupied_thresh']
        free_thresh = meta['free_thresh']
        negate = meta['negate']

        factor = 1
        while max(width, height) // factor > max_dimension:
            factor += 1

        new_width = width // factor
        new_height = height // factor
        cells = [UNKNOWN] * (new_width * new_height)

        for ny in range(new_height):
            for nx in range(new_width):
                # Sample the block; occupied wins, then free, else unknown.
                block_occupied = False
                block_free = False
                for dy in range(factor):
                    row = (ny * factor + dy) * width
                    for dx in range(factor):
                        value = pixels[row + nx * factor + dx]
                        shade = value if negate else 255 - value
                        occupancy = shade / 255.0
                        if occupancy > occupied_thresh:
                            block_occupied = True
                        elif occupancy < free_thresh:
                            block_free = True
                # PGM row 0 is the TOP of the map; grid row 0 is the BOTTOM.
                gy = new_height - 1 - ny
                if block_occupied:
                    cells[gy * new_width + nx] = OCCUPIED
                elif block_free:
                    cells[gy * new_width + nx] = FREE

        return cls(new_width, new_height, meta['resolution'] * factor,
                   meta['origin'][0], meta['origin'][1], cells)

    @classmethod
    def synthetic(cls, width=160, height=120, resolution=0.1):
        """Fallback map (walled arena with a few rooms) if no PGM is found."""
        cells = [FREE] * (width * height)

        def set_wall(gx, gy):
            if 0 <= gx < width and 0 <= gy < height:
                cells[gy * width + gx] = OCCUPIED

        for gx in range(width):
            set_wall(gx, 0), set_wall(gx, height - 1)
        for gy in range(height):
            set_wall(0, gy), set_wall(width - 1, gy)
        # Interior walls with door gaps.
        for gy in range(0, int(height * 0.6)):
            set_wall(int(width * 0.4), gy)
        for gy in range(int(height * 0.75), height):
            set_wall(int(width * 0.4), gy)
        for gx in range(int(width * 0.55), width):
            set_wall(gx, int(height * 0.5))
        for gx in range(int(width * 0.4), int(width * 0.62)):
            set_wall(gx, int(height * 0.25))
        return cls(width, height, resolution, -width * resolution / 2.0,
                   -height * resolution / 2.0, cells)


# ---------------------------------------------------------------------------
# Planning helpers (mirror of the navigation2 A* behaviour, simplified)
# ---------------------------------------------------------------------------

def inflate_obstacles(grid, clearance_m):
    """Multi-source BFS distance from obstacles; returns set of blocked idx."""
    clearance_cells = max(1, int(math.ceil(clearance_m / grid.resolution)))
    blocked = [False] * len(grid.cells)
    frontier = []
    for idx, value in enumerate(grid.cells):
        if value == OCCUPIED:
            blocked[idx] = True
            frontier.append((idx, 0))
    head = 0
    while head < len(frontier):
        idx, depth = frontier[head]
        head += 1
        if depth >= clearance_cells:
            continue
        gx, gy = idx % grid.width, idx // grid.width
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = gx + dx, gy + dy
            if grid.in_bounds(nx, ny):
                nidx = ny * grid.width + nx
                if not blocked[nidx]:
                    blocked[nidx] = True
                    frontier.append((nidx, depth + 1))
    return blocked


def a_star(grid, blocked, start, goal):
    """8-connected A* from start to goal (grid cells). Returns cell list."""
    def free(cell):
        gx, gy = cell
        if not grid.in_bounds(gx, gy):
            return False
        idx = grid.index(gx, gy)
        return grid.cells[idx] == FREE and not blocked[idx]

    if not free(start) or not free(goal):
        return []

    def heuristic(cell):
        return math.hypot(goal[0] - cell[0], goal[1] - cell[1])

    open_set = [(heuristic(start), start)]
    came_from = {}
    g_score = {start: 0.0}
    closed = set()
    diagonal = math.sqrt(2.0)

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        if current in closed:
            continue
        closed.add(current)
        cx, cy = current
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                neighbor = (cx + dx, cy + dy)
                if neighbor in closed or not free(neighbor):
                    continue
                if dx != 0 and dy != 0:
                    if not free((cx + dx, cy)) or not free((cx, cy + dy)):
                        continue
                cost = diagonal if dx != 0 and dy != 0 else 1.0
                tentative = g_score[current] + cost
                if tentative < g_score.get(neighbor, math.inf):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    heapq.heappush(open_set,
                                   (tentative + heuristic(neighbor), neighbor))
    return []


# ---------------------------------------------------------------------------
# The simulator
# ---------------------------------------------------------------------------

class SimBackend:
    TICK_HZ = 10.0
    LINEAR_SPEED = 0.45          # m/s (faster than the real turtle, for demos)
    ANGULAR_SPEED = 2.4          # rad/s
    GOAL_TOLERANCE = 0.15        # m (navigation2 uses 0.10)
    CLEARANCE = 0.20             # m inflation radius for planning
    REVEAL_RADIUS = 4.0          # m SLAM "sensor range" while mapping
    NAV_TIMEOUT = 180.0          # s before a navigation task fails
    CUBE_SPEED = 0.30            # m/s walking pace of the simulated cube
    FOLLOW_DISTANCE = 0.60       # m the robot keeps behind the cube
    FOLLOW_REPLAN_S = 0.7        # s between path re-plans to the cube

    def __init__(self, map_search_paths=(), premapped=False):
        self.mode = 'sim'
        self.map_name = None
        self.grid = self._load_map(map_search_paths)
        self.blocked = inflate_obstacles(self.grid, self.CLEARANCE)

        self.lifecycle = RobotLifecycle()
        self.health = HealthMonitor()
        self.tasks = TaskManager()
        self.slam = SlamMetrics(convergence_threshold=0.97, hold_seconds=5.0)

        self.health.add_component('scan', 'LiDAR /scan', 10.0, 1.0, 3.0, critical=True)
        self.health.add_component('pose', 'Localization /pose', 10.0, 1.0, 3.0, critical=True)
        self.health.add_component('map', 'SLAM map /map', 0.5, 6.0, 15.0)
        self.health.add_component('slam_confidence', 'SLAM analyzer', 0.5, 6.0, 15.0)
        # planner and motors are event-driven: they only publish while a task
        # runs, so silence is not a failure (they never WARN/DOWN on age).
        self.health.add_component('planner', 'Planner /planned_path', 0.0, 1e9, 2e9)
        self.health.add_component('motors', 'Motor cmd /base/cmd_vel', 0.0, 1e9, 2e9)
        self.health.set_battery(100.0)

        # Robot state
        start = self._find_free_start()
        self.x, self.y = self.grid.grid_to_world(*start)
        self.yaw = 0.0
        self.speed = 0.0

        # Navigation state
        self.goal = None
        self.path = []          # list of world (x, y)
        self.nav_state = 'idle'
        self._nav_started = None
        self._nav_initial_distance = None

        # Simulated red cube (follow_red task): a person carrying the cube
        # wanders through the map and the robot follows at a short distance.
        self.cube = None            # world (x, y) or None
        self._cube_path = []        # waypoints the cube wanders along
        self._cube_replan = 0.0     # last time the robot re-planned to the cube

        # SLAM reveal state
        self.premapped = premapped
        self.revealed = [premapped] * len(self.grid.cells)
        # Coverage is measured against the *navigable* region (flood fill from
        # the start): free space sealed off by walls/inflation can never be
        # mapped, exactly like a real SLAM run.
        self._navigable = self._flood_fill(start)
        self._total_free = sum(1 for reachable in self._navigable if reachable)
        self._confidence_ema = 1.0 if premapped else 0.0
        self._wander_goal = None
        self._boot_time = time.time()
        self.map_saved = premapped
        self._save_started = None

        # Fault injection (set of component names whose beats are suppressed)
        self.injected_faults = set()
        self.estopped = False

        self.map_version = 1
        self._map_dirty = True
        self._last_map_beat = 0.0
        self._last_slam_beat = 0.0

        self._lock = threading.RLock()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    # ------------------------------------------------------------------
    # Setup helpers
    # ------------------------------------------------------------------
    def _load_map(self, search_paths):
        for pgm, yml in search_paths:
            if os.path.exists(pgm) and os.path.exists(yml):
                try:
                    grid = GridMap.load(pgm, yml)
                    self.map_name = os.path.basename(pgm)
                    return grid
                except Exception:
                    continue
        self.map_name = 'synthetic_arena'
        return GridMap.synthetic()

    def _flood_fill(self, start):
        """Reachable FREE & unblocked cells from start (4-connected BFS)."""
        navigable = [False] * len(self.grid.cells)
        start_idx = self.grid.index(*start)
        navigable[start_idx] = True
        queue = [start_idx]
        head = 0
        while head < len(queue):
            idx = queue[head]
            head += 1
            gx, gy = idx % self.grid.width, idx // self.grid.width
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = gx + dx, gy + dy
                if not self.grid.in_bounds(nx, ny):
                    continue
                nidx = ny * self.grid.width + nx
                if (not navigable[nidx] and not self.blocked[nidx]
                        and self.grid.cells[nidx] == FREE):
                    navigable[nidx] = True
                    queue.append(nidx)
        return navigable

    def _find_free_start(self):
        center = (self.grid.width // 2, self.grid.height // 2)
        best = None
        best_distance = math.inf
        for gy in range(self.grid.height):
            for gx in range(self.grid.width):
                idx = self.grid.index(gx, gy)
                if self.grid.cells[idx] == FREE and not self.blocked[idx]:
                    distance = math.hypot(gx - center[0], gy - center[1])
                    if distance < best_distance:
                        best_distance = distance
                        best = (gx, gy)
        return best or center

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------
    def _run(self):
        period = 1.0 / self.TICK_HZ
        while True:
            started = time.time()
            with self._lock:
                self._tick(started)
            time.sleep(max(0.0, period - (time.time() - started)))

    def _beat(self, name, now):
        if name not in self.injected_faults:
            self.health.beat(name, now)

    def _tick(self, now):
        state = self.lifecycle.state

        # --- sensor heartbeats (10 Hz components) --------------------------
        self._beat('scan', now)
        self._beat('pose', now)
        if now - self._last_map_beat >= 2.0:
            self._beat('map', now)
            self._last_map_beat = now

        # battery drains slowly, recharges never (demo telemetry)
        self.health.set_battery(
            max(5.0, 100.0 - (now - self._boot_time) / 60.0))

        # --- lifecycle progression -----------------------------------------
        if state == RobotState.BOOT:
            self.lifecycle.handle(RobotEvent.START)
            return

        # Critical health failures pre-empt everything.
        failure = self.health.critical_failure(now)
        if failure and state not in (RobotState.FAULT, RobotState.ESTOPPED):
            self.lifecycle.handle(RobotEvent.CRITICAL_FAULT, note=failure)
            if self.tasks.busy:
                self.tasks.fail('critical fault: {} lost'.format(failure))
            self._stop_motion()
            return

        if state == RobotState.FAULT:
            self._stop_motion()
            if self.health.all_critical_ok(now):
                self.lifecycle.handle(RobotEvent.FAULT_CLEARED)
            return

        if state == RobotState.ESTOPPED:
            self._stop_motion()
            return

        if state == RobotState.INITIALIZING:
            # Wait until critical sensors report a healthy rate.
            if self.health.all_critical_ok(now) and now - self._boot_time > 1.5:
                if self.map_saved:
                    self.lifecycle.handle(RobotEvent.SENSORS_READY_MAP_AVAILABLE)
                else:
                    self.lifecycle.handle(RobotEvent.SENSORS_READY_MAP_MISSING)
                    self.tasks.start(TASK_MAP)
            return

        if state == RobotState.MAPPING:
            self._tick_mapping(now)
            return

        if state == RobotState.SAVING_MAP:
            if self._save_started is None:
                self._save_started = now
            elif now - self._save_started >= 1.5:
                self.map_saved = True
                self._save_started = None
                self.lifecycle.handle(RobotEvent.MAP_SAVED)
                self.tasks.succeed('map saved as my_map_1')
            return

        if state in (RobotState.READY, RobotState.EXECUTING):
            self._tick_navigation(now)

    # ------------------------------------------------------------------
    # Mapping simulation (drives the SLAM performance panel)
    # ------------------------------------------------------------------
    def _tick_mapping(self, now):
        # Wander toward unexplored space.
        if not self.path:
            self._pick_wander_goal()
        self._follow_path(now)
        self._reveal(now)

        # Publish SLAM metrics at ~0.5 Hz like the real analyzer.
        if now - self._last_slam_beat >= 2.0:
            self._last_slam_beat = now
            revealed_free = sum(
                1 for idx, reachable in enumerate(self._navigable)
                if reachable and self.revealed[idx])
            ratio = revealed_free / max(1, self._total_free)
            target = min(1.0, 0.05 + 0.95 * ratio ** 0.8)
            self._confidence_ema += 0.35 * (target - self._confidence_ema)
            unknown_ratio = 1.0 - ratio
            growth = abs(target - self._confidence_ema)
            converged = self.slam.update(
                confidence=self._confidence_ema + random.uniform(-0.004, 0.004),
                frontier_ratio=round(unknown_ratio * 0.02, 4),
                unknown_ratio=round(unknown_ratio, 4),
                growth_ratio=round(growth, 4),
                stamp=now,
            )
            self._beat('slam_confidence', now)
            self.tasks.update_progress(
                self._confidence_ema,
                'confidence {:.1%}'.format(self._confidence_ema))
            self._map_dirty = True
            self.map_version += 1
            if converged:
                self._clear_navigation()
                self.lifecycle.handle(RobotEvent.SLAM_CONVERGED)

    def _pick_wander_goal(self):
        # Prefer frontier cells: revealed FREE cells adjacent to unrevealed.
        frontier = []
        for gy in range(1, self.grid.height - 1, 3):
            for gx in range(1, self.grid.width - 1, 3):
                idx = self.grid.index(gx, gy)
                if self._navigable[idx] and not self.revealed[idx]:
                    frontier.append((gx, gy))
        if not frontier:
            return
        start = self.grid.world_to_grid(self.x, self.y)
        if start is None:
            return
        target = random.choice(frontier)
        cells = a_star(self.grid, self.blocked, start, target)
        if cells:
            self.path = [self.grid.grid_to_world(gx, gy) for gx, gy in cells]
            self.nav_state = 'exploring'
            self._beat('planner', time.time())
        else:
            # Unreachable pocket (e.g. free space outside the building):
            # mark it revealed so the coverage ratio can still converge.
            tx, ty = target
            radius = max(2, int(1.0 / self.grid.resolution))
            for dy in range(-radius, radius + 1):
                gy = ty + dy
                if 0 <= gy < self.grid.height:
                    for dx in range(-radius, radius + 1):
                        gx = tx + dx
                        if 0 <= gx < self.grid.width:
                            self.revealed[gy * self.grid.width + gx] = True

    def _reveal(self, now):
        cell = self.grid.world_to_grid(self.x, self.y)
        if cell is None:
            return
        radius = int(self.REVEAL_RADIUS / self.grid.resolution)
        cx, cy = cell
        for dy in range(-radius, radius + 1):
            gy = cy + dy
            if gy < 0 or gy >= self.grid.height:
                continue
            span = int(math.sqrt(max(0, radius * radius - dy * dy)))
            for gx in range(max(0, cx - span),
                            min(self.grid.width, cx + span + 1)):
                self.revealed[gy * self.grid.width + gx] = True

    # ------------------------------------------------------------------
    # Navigation simulation (point-to-point)
    # ------------------------------------------------------------------
    def _tick_navigation(self, now):
        if not self.tasks.busy or self.tasks.active.type not in (
                TASK_NAVIGATE, TASK_EXPLORE, TASK_FOLLOW_RED):
            return

        task = self.tasks.active
        if task.type == TASK_FOLLOW_RED:
            self._tick_follow_red(now)
            self._follow_path(now)
            return

        if task.type == TASK_EXPLORE and not self.path:
            self._pick_wander_goal()
            if not self.path:
                self._finish_task_ok('exploration area covered')
            return

        if self.goal is None and task.type == TASK_NAVIGATE:
            self._finish_task_fail('goal lost')
            return

        if task.type == TASK_NAVIGATE:
            if now - (self._nav_started or now) > self.NAV_TIMEOUT:
                self._finish_task_fail('navigation timed out')
                return
            remaining = math.hypot(self.goal[0] - self.x, self.goal[1] - self.y)
            if remaining <= self.GOAL_TOLERANCE:
                self._finish_task_ok('goal reached')
                return
            if not self.path:
                self._finish_task_fail('no path to goal')
                return
            if self._nav_initial_distance:
                progress = 1.0 - remaining / self._nav_initial_distance
                self.tasks.update_progress(
                    progress, '{:.2f} m to goal'.format(remaining))

        self._follow_path(now)

    # ------------------------------------------------------------------
    # Follow-red-cube simulation
    # ------------------------------------------------------------------
    def _tick_follow_red(self, now):
        """Move the simulated cube and keep the robot chasing it."""
        if self.cube is None:
            self._spawn_cube()
            if self.cube is None:
                self._finish_task_fail('no free space to place the red cube')
                return

        self._move_cube(now)

        distance = math.hypot(self.cube[0] - self.x, self.cube[1] - self.y)
        self.tasks.update_progress(
            0.0, 'following red cube · {:.2f} m away'.format(distance))

        # Re-plan a path toward the cube at a low rate (like the tracker
        # updating /target_vector). Stop short so we do not run it over.
        if now - self._cube_replan < self.FOLLOW_REPLAN_S:
            return
        self._cube_replan = now
        if distance <= self.FOLLOW_DISTANCE:
            self.path = []
            self.speed = 0.0
            return
        start = self.grid.world_to_grid(self.x, self.y)
        target = self.grid.world_to_grid(*self.cube)
        if start is None or target is None:
            return
        cells = a_star(self.grid, self.blocked, start, target)
        if cells:
            waypoints = [self.grid.grid_to_world(gx, gy) for gx, gy in cells]
            # Trim the tail so the robot keeps FOLLOW_DISTANCE to the cube.
            trim = int(self.FOLLOW_DISTANCE / self.grid.resolution)
            self.path = waypoints[:-trim] if trim < len(waypoints) else []
            self.nav_state = 'following'
            self._beat('planner', now)

    def _spawn_cube(self):
        """Place the cube on a free cell a couple of metres from the robot."""
        start = self.grid.world_to_grid(self.x, self.y)
        if start is None:
            return
        candidates = []
        for gy in range(1, self.grid.height - 1, 2):
            for gx in range(1, self.grid.width - 1, 2):
                idx = self.grid.index(gx, gy)
                if not self._navigable[idx]:
                    continue
                wx, wy = self.grid.grid_to_world(gx, gy)
                distance = math.hypot(wx - self.x, wy - self.y)
                if 1.5 <= distance <= 4.0:
                    candidates.append((gx, gy))
        if not candidates:
            return
        gx, gy = random.choice(candidates)
        if not a_star(self.grid, self.blocked, start, (gx, gy)):
            return
        self.cube = list(self.grid.grid_to_world(gx, gy))
        self._cube_path = []

    def _move_cube(self, now):
        """The person carrying the cube wanders at walking pace."""
        if not self._cube_path:
            self._pick_cube_goal()
        if not self._cube_path:
            return
        step = self.CUBE_SPEED / self.TICK_HZ
        tx, ty = self._cube_path[0]
        dx, dy = tx - self.cube[0], ty - self.cube[1]
        distance = math.hypot(dx, dy)
        if distance <= step:
            self.cube[0], self.cube[1] = tx, ty
            self._cube_path.pop(0)
        else:
            self.cube[0] += dx / distance * step
            self.cube[1] += dy / distance * step

    def _pick_cube_goal(self):
        """Pick a random reachable spot for the cube to wander toward."""
        start = self.grid.world_to_grid(*self.cube)
        if start is None:
            return
        for _ in range(12):
            gx = random.randint(1, self.grid.width - 2)
            gy = random.randint(1, self.grid.height - 2)
            if not self._navigable[self.grid.index(gx, gy)]:
                continue
            cells = a_star(self.grid, self.blocked, start, (gx, gy))
            if cells:
                self._cube_path = [
                    self.grid.grid_to_world(cx, cy) for cx, cy in cells]
                return

    def _follow_path(self, now):
        if not self.path or self.estopped:
            self.speed = 0.0
            return
        dt = 1.0 / self.TICK_HZ
        # Waypoint chasing with a lookahead, like the navigation2 node.
        while self.path and math.hypot(self.path[0][0] - self.x,
                                       self.path[0][1] - self.y) < 0.12:
            self.path.pop(0)
        if not self.path:
            self.speed = 0.0
            return
        target = self.path[min(2, len(self.path) - 1)]
        desired_yaw = math.atan2(target[1] - self.y, target[0] - self.x)
        yaw_error = math.atan2(math.sin(desired_yaw - self.yaw),
                               math.cos(desired_yaw - self.yaw))
        max_turn = self.ANGULAR_SPEED * dt
        self.yaw += max(-max_turn, min(max_turn, yaw_error))
        self.yaw = math.atan2(math.sin(self.yaw), math.cos(self.yaw))
        turn_scale = max(0.0, 1.0 - abs(yaw_error) / (math.pi / 2.0))
        self.speed = self.LINEAR_SPEED * turn_scale
        self.x += math.cos(self.yaw) * self.speed * dt
        self.y += math.sin(self.yaw) * self.speed * dt
        if self.speed > 0.01:
            self._beat('motors', now)

    def _stop_motion(self):
        self.speed = 0.0

    def _clear_navigation(self):
        self.goal = None
        self.path = []
        self.speed = 0.0
        self.nav_state = 'idle'
        self._nav_started = None
        self._nav_initial_distance = None
        self.cube = None
        self._cube_path = []

    def _finish_task_ok(self, detail):
        self.tasks.succeed(detail)
        self._clear_navigation()
        self.lifecycle.handle(RobotEvent.TASK_FINISHED)

    def _finish_task_fail(self, detail):
        self.tasks.fail(detail)
        self._clear_navigation()
        self.lifecycle.handle(RobotEvent.TASK_FINISHED)

    # ------------------------------------------------------------------
    # Dashboard API (same contract as the ROS backend)
    # ------------------------------------------------------------------
    def command(self, payload):
        with self._lock:
            return self._command(payload)

    def _command(self, payload):
        action = payload.get('action')

        if action == 'navigate':
            x, y = float(payload['x']), float(payload['y'])
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False,
                        'error': 'robot not READY (state: {})'.format(
                            self.lifecycle.state.value)}
            start = self.grid.world_to_grid(self.x, self.y)
            goal = self.grid.world_to_grid(x, y)
            if goal is None:
                return {'ok': False, 'error': 'goal outside the map'}
            cells = a_star(self.grid, self.blocked, start, goal)
            if not cells:
                return {'ok': False, 'error': 'no collision-free path found'}
            task = self.tasks.start(TASK_NAVIGATE, {'x': x, 'y': y})
            if task is None:
                return {'ok': False, 'error': 'another task is active'}
            self.goal = (x, y)
            self.path = [self.grid.grid_to_world(gx, gy) for gx, gy in cells]
            self.nav_state = 'tracking'
            self._nav_started = time.time()
            self._nav_initial_distance = max(
                0.001, math.hypot(x - self.x, y - self.y))
            self._beat('planner', time.time())
            self.lifecycle.handle(RobotEvent.TASK_STARTED)
            return {'ok': True, 'task_id': task.id}

        if action == 'explore':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False, 'error': 'robot not READY'}
            # Exploring re-visits unrevealed space; reset a bit of the mask.
            task = self.tasks.start(TASK_EXPLORE)
            if task is None:
                return {'ok': False, 'error': 'another task is active'}
            self.lifecycle.handle(RobotEvent.TASK_STARTED)
            return {'ok': True, 'task_id': task.id}

        if action == 'follow_red':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False, 'error': 'robot not READY'}
            task = self.tasks.start(TASK_FOLLOW_RED)
            if task is None:
                return {'ok': False, 'error': 'another task is active'}
            self._cube_replan = 0.0
            self.lifecycle.handle(RobotEvent.TASK_STARTED)
            return {'ok': True, 'task_id': task.id}

        if action == 'remap':
            if self.lifecycle.state != RobotState.READY:
                return {'ok': False, 'error': 'robot not READY'}
            self.map_saved = False
            self.revealed = [False] * len(self.grid.cells)
            self._confidence_ema = 0.0
            self.slam.reset_convergence()
            self.tasks.start(TASK_MAP)
            self.lifecycle.handle(RobotEvent.REMAP_REQUESTED)
            self._map_dirty = True
            self.map_version += 1
            return {'ok': True}

        if action == 'cancel':
            if not self.tasks.busy:
                return {'ok': False, 'error': 'no active task'}
            self.tasks.cancel()
            self._clear_navigation()
            if self.lifecycle.state == RobotState.EXECUTING:
                self.lifecycle.handle(RobotEvent.TASK_FINISHED)
            elif self.lifecycle.state in (RobotState.MAPPING,
                                          RobotState.SAVING_MAP):
                # Cancelled mapping: treat current map as good enough.
                self.map_saved = True
                self.lifecycle.handle(RobotEvent.MAPPING_CANCELLED)
            return {'ok': True}

        if action == 'estop':
            engage = bool(payload.get('engage', True))
            if engage and not self.estopped:
                self.estopped = True
                if self.tasks.busy:
                    self.tasks.fail('emergency stop')
                self._clear_navigation()
                self.lifecycle.handle(RobotEvent.ESTOP_PRESSED)
            elif not engage and self.estopped:
                self.estopped = False
                self.lifecycle.handle(RobotEvent.ESTOP_RELEASED)
            return {'ok': True, 'estopped': self.estopped}

        if action == 'inject_fault':
            component = payload.get('component', 'scan')
            enable = bool(payload.get('enable', True))
            if enable:
                self.injected_faults.add(component)
            else:
                self.injected_faults.discard(component)
            return {'ok': True, 'faults': sorted(self.injected_faults)}

        return {'ok': False, 'error': 'unknown action: {}'.format(action)}

    def state(self):
        with self._lock:
            now = time.time()
            return {
                'time': now,
                'mode': self.mode,
                'map_name': self.map_name,
                'robot': {
                    'x': round(self.x, 3),
                    'y': round(self.y, 3),
                    'yaw': round(self.yaw, 3),
                    'speed': round(self.speed, 3),
                    'frame': 'map',
                    'has_pose': True,
                },
                'lifecycle': self.lifecycle.snapshot(),
                'health': self.health.snapshot(now),
                'task': self.tasks.snapshot(),
                'slam': self.slam.snapshot(),
                'nav': {
                    'state': self.nav_state,
                    'goal': ({'x': self.goal[0], 'y': self.goal[1]}
                             if self.goal else None),
                    'cube': ({'x': round(self.cube[0], 3),
                              'y': round(self.cube[1], 3)}
                             if self.cube else None),
                    'path': [[round(px, 3), round(py, 3)]
                             for px, py in self.path[::2][:400]],
                },
                'estopped': self.estopped,
                'injected_faults': sorted(self.injected_faults),
                'map_version': self.map_version,
            }

    def map_payload(self):
        with self._lock:
            raw = bytearray(len(self.grid.cells))
            mapping_phase = not self.map_saved
            for idx, value in enumerate(self.grid.cells):
                if mapping_phase and not self.revealed[idx]:
                    raw[idx] = _CELL_BYTE[UNKNOWN]
                else:
                    raw[idx] = _CELL_BYTE[value]
            return {
                'version': self.map_version,
                'width': self.grid.width,
                'height': self.grid.height,
                'resolution': self.grid.resolution,
                'origin_x': self.grid.origin_x,
                'origin_y': self.grid.origin_y,
                'data_b64': base64.b64encode(bytes(raw)).decode('ascii'),
            }
