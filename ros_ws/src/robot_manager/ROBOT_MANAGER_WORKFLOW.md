# Robot Manager — Workflow Diagram & Architecture

> Reference document for the `robot_manager` package (`ros_ws/src/robot_manager`).
> The diagrams are Mermaid — GitHub / VS Code render them natively.

---

## 1. The mission lifecycle (the "whole lifecycle")

The robot manager owns one supervisory state machine. Unlike the earlier
notes/nodes, this is the **complete** lifecycle from power-on to task
execution, including the failure paths:

```mermaid
stateDiagram-v2
    [*] --> BOOT
    BOOT --> INITIALIZING : start
    INITIALIZING --> MAPPING : sensors OK, no saved map
    INITIALIZING --> READY : sensors OK, map available
    MAPPING --> SAVING_MAP : SLAM confidence ≥ 97%\nheld for 5 s (debounced)
    SAVING_MAP --> READY : /slam_toolbox/save_map succeeded
    SAVING_MAP --> MAPPING : save failed (retry)
    READY --> EXECUTING : task started\n(e.g. navigate to goal)
    EXECUTING --> READY : task finished\n(succeeded / failed / cancelled)

    state "ESTOPPED" as E
    state "FAULT" as F
    BOOT --> E : e-stop (any state)
    MAPPING --> F : critical sensor DOWN\n(/scan or /pose lost)
    EXECUTING --> F : critical sensor DOWN
    E --> INITIALIZING : e-stop released
    F --> INITIALIZING : sensors recovered
```

State meanings:

| State | Meaning | Motion allowed |
|---|---|---|
| `BOOT` | process started, nothing verified | no |
| `INITIALIZING` | waiting for critical inputs (`/scan`, `/pose`) at healthy rates | no |
| `MAPPING` | SLAM active; convergence monitored via `/slam_confidence` | yes |
| `SAVING_MAP` | confidence converged; saving via slam_toolbox | no |
| `READY` | healthy, map available, waiting for a task | yes (idle) |
| `EXECUTING` | a task is active (navigation / exploration) | yes |
| `ESTOPPED` | operator emergency stop — zero velocity streamed | no |
| `FAULT` | critical component lost — task aborted, robot stopped | no |

Key rules:

- **E-stop and critical faults pre-empt every state.** Both abort the active
  task and stream zero `Twist` on `/base/cmd_vel` to override stale commands.
- **Recovery always re-enters `INITIALIZING`** so sensor health is re-verified
  before the robot is allowed to move again — never straight back to `READY`.
- **SLAM convergence is debounced**: confidence must stay above the threshold
  for a continuous hold period (5 s); a dip resets the timer.

## 2. How the manager plugs into the existing stack

The manager **only uses interfaces the team's nodes already provide** — no
teammate code changes:

```mermaid
graph TD
    subgraph Hardware
        LIDAR["Hokuyo LiDAR<br/>(urg_node2)"]
        BASE["Roboclaw base<br/>(roboclaw_node)"]
    end

    subgraph Teammate nodes
        SLAM["slam_toolbox"]
        ANALYZER["slam_analyzer<br/>(SLAM confidence)"]
        NAV["navigation2<br/>(A* planner + tracker)"]
        CA["collision_avoidance"]
        ODOM["odom_to_pos / TF"]
    end

    subgraph "robot_manager (this package)"
        RM["robot_manager node<br/>lifecycle + health + tasks"]
        DASH["dashboard server<br/>HTTP + SSE :8765"]
        WEB["web dashboard<br/>(browser)"]
    end

    LIDAR -->|/scan| SLAM
    LIDAR -->|/scan| CA
    LIDAR -->|/scan heartbeat| RM
    SLAM -->|/map| NAV
    SLAM -->|/map| ANALYZER
    SLAM -->|/map| RM
    ANALYZER -->|"/slam_confidence (JSON)"| RM
    ODOM -->|/pose| NAV
    ODOM -->|/pose| RM
    RM -->|"/goal_pose (task goal)"| NAV
    NAV -->|/planned_path| RM
    NAV -->|/target_vector| CA
    CA -->|/base/cmd_vel| BASE
    RM -->|"/base/cmd_vel = 0<br/>(e-stop / fault)"| BASE
    RM -->|/mapping_finished| ANALYZER
    RM -->|"save_map service"| SLAM
    RM <--> DASH
    DASH <-->|"SSE state stream +<br/>command POSTs"| WEB
```

## 3. Point-to-point navigation flow

```mermaid
sequenceDiagram
    participant User as Operator (dashboard)
    participant D as dashboard server
    participant RM as robot_manager
    participant NAV as navigation2 (A*)
    participant CA as collision_avoidance

    User->>D: click map → POST /api/command {navigate, x, y}
    D->>RM: command()
    RM->>RM: state must be READY,<br/>start Task #N (active)
    RM->>NAV: publish /goal_pose
    NAV->>NAV: A* plan on /map (+ inflation)
    NAV-->>RM: /planned_path
    loop 5 Hz until goal
        NAV->>CA: /target_vector
        CA->>CA: reactive obstacle avoidance
        CA->>NAV: /base/cmd_vel → base moves
        RM->>RM: progress = 1 − remaining/initial
        RM-->>User: SSE state (pose, path, progress)
    end
    RM->>RM: distance ≤ 0.15 m → task SUCCEEDED
    RM-->>User: task history updated, state → READY
```

## 4. Health monitoring model

Every monitored component is fed one "beat" per received message; the monitor
derives **rate** and **age** and classifies:

| Component | Topic | Expected | WARN if silent | DOWN if silent | Critical |
|---|---|---|---|---|---|
| LiDAR | `/scan` | 10 Hz | 1.5 s | 4 s | ★ yes |
| Localization | `/pose` | 10 Hz | 1.5 s | 4 s | ★ yes |
| SLAM map | `/map` | 0.5 Hz | 8 s | 20 s | no |
| SLAM analyzer | `/slam_confidence` | 0.5 Hz | 8 s | 20 s | no |
| Planner | `/planned_path` | event | never | never | no |
| Motors | `/base/cmd_vel` | event | never | never | no |

`★ critical` DOWN ⇒ lifecycle event `CRITICAL_FAULT` ⇒ task aborted, robot
stopped, dashboard banner raised. Recovery of all critical components ⇒
`FAULT_CLEARED` ⇒ back through `INITIALIZING`.

## 5. Dashboard data flow

```mermaid
graph LR
    B["backend<br/>(RobotManagerNode or SimBackend)"]
    S["dashboard_server.py<br/>stdlib HTTP + SSE"]
    UI["web/ single page app"]

    B -- "state() 5 Hz" --> S
    B -- "map_payload() on change" --> S
    S -- "SSE /events (state, map)" --> UI
    UI -- "POST /api/command<br/>navigate · cancel · estop ·<br/>explore · remap · inject_fault" --> S
    S -- "command()" --> B
```

Both backends implement the same three-method contract (`state()`,
`map_payload()`, `command()`), so the dashboard is byte-identical in
simulation and on the robot.

## 6. Running it

```bash
# On any machine, no ROS needed (simulator):
cd ros_ws/src/robot_manager
python -m robot_manager.dashboard_server --sim
# → http://localhost:8765   (add --premapped to skip the mapping phase)

# On the robot / dev container with ROS 2:
cd ros_ws && colcon build --packages-select robot_manager
source install/setup.bash
ros2 launch robot_manager robot_manager.launch.py
# (drivers, slam_toolbox, slam_analyzer, navigation2, collision_avoidance
#  are launched separately, exactly as before)
```
