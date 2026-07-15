# robot_manager

Supervisory robot manager for the OMN Tortugabot stack, with a built-in web
dashboard. It owns the **complete mission lifecycle** and provides:

- **Live localization** — robot position `(x, y, θ)` on the occupancy grid,
  with trail, planned path and goal overlay
- **Health monitor** — per-component message rate / age / status
  (LiDAR, localization, SLAM, planner, motors) with critical-fault handling
- **Point-to-point navigation** — click the map to publish `/goal_pose`;
  progress and completion tracked as a task
- **Task status** — which task the robot is performing, progress, and a
  history of completed/failed/cancelled tasks
- **SLAM performance** — live confidence / unknown / frontier / growth
  metrics from the `slam_analyzer`, with the debounced convergence logic
  that triggers automatic map saving
- **E-stop** — one click stops the robot from any state

See [`ROBOT_MANAGER_WORKFLOW.md`](../../../ROBOT_MANAGER_WORKFLOW.md) at the
repo root for the full lifecycle and architecture diagrams.

## Quick start — no ROS required (simulator)

The dashboard ships with a full robot simulator (loads the recorded
`my_map_1` map) so it runs on any machine with Python 3.8+, zero
dependencies:

```bash
cd ros_ws/src/robot_manager
python -m robot_manager.dashboard_server --sim
# open http://localhost:8765
```

The sim walks the real lifecycle: initialize → SLAM mapping (watch the
confidence climb) → save map → ready. Then click the map to navigate.
`--premapped` skips the mapping phase. The **Drop LiDAR (sim)** button
injects a sensor fault to demonstrate FAULT → recovery.

## On the robot (ROS 2)

```bash
cd ros_ws
colcon build --packages-select robot_manager
source install/setup.bash
ros2 launch robot_manager robot_manager.launch.py
# dashboard: http://<robot-ip>:8765
```

Launch the rest of the stack as usual (drivers, `slam_toolbox`,
`slam_analyzer`, `navigation2`, `collision_avoidance`, `odom_to_pos`).
The manager only observes and commands existing topics — **no teammate node
needs modification**.

Parameters:

| Parameter | Default | Meaning |
|---|---|---|
| `dashboard_port` | `8765` | HTTP port of the dashboard |
| `assume_map_available` | `false` | skip the mapping phase (map already saved) |
| `map_save_name` | `auto_map` | prefix for maps saved via slam_toolbox |

## Interfaces

Subscribes: `/pose`, `/map`, `/scan`, `/slam_confidence`, `/planned_path`,
`/base/cmd_vel` (heartbeat).
Publishes: `/goal_pose`, `/mapping_finished`, `/robot_manager/state` (JSON),
and zero `Twist` on `/base/cmd_vel` while e-stopped/faulted.
Service client: `/slam_toolbox/save_map`.

## Module layout

| File | Responsibility |
|---|---|
| `lifecycle.py` | mission FSM (pure Python, unit-testable) |
| `health_monitor.py` | component rate/age tracking + fault classification |
| `task_manager.py` | active task + bounded history |
| `slam_metrics.py` | SLAM metric time series + debounced convergence |
| `robot_manager_node.py` | ROS 2 node wiring the core to real topics |
| `sim_backend.py` | full robot simulator (same core, no ROS) |
| `dashboard_server.py` | stdlib HTTP + SSE server and API |
| `web/` | single-page dashboard (vanilla JS, no dependencies) |
