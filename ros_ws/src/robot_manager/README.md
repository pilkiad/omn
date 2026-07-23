# Robot Manager — Operating Guide

This is the complete, current guide to running the robot with `robot_manager`.
It covers what to launch, what each dashboard button does, why certain
things can't run at the same time, and how to recover when something goes
wrong.

---

## 1. Starting up

Only one terminal command is needed:

```bash
cd ~/      # your workspace root
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 launch robot_manager robot_manager.launch.py
```

Open the dashboard: **http://localhost:8765**

This single launch starts two things:
- `robot_manager` — the supervisor + web dashboard
- `pose_publisher` — bridges `roboclaw`'s `/odom` into `/pose`, which the
  dashboard and `navigation` both require

Everything else (LiDAR, motors, SLAM, navigation) is started **from the
dashboard**, not from extra terminals. See the Stack panel below.

---

## 2. The Stack panel — one-click hardware/software startup

| Button | Launches | Command |
|---|---|---|
| LiDAR driver (urg_node2) | LiDAR | `ros2 launch urg_node2 urg_node2.launch.py` |
| Motors (roboclaw) | Motor controller | `ros2 launch roboclaw_node roboclaw_launch.py` |
| SLAM (slam_toolbox) | Mapping | `ros2 launch slam slam_mapping.launch.py` |
| Navigation + collision avoidance | Path planning + safety layer | `ros2 launch navigation navigation.launch.py` |

**Startup order:** LiDAR → Motors → SLAM → Navigation. Each button shows
`running`/`stopped` live, so you always know what's actually up.

Stopping `robot_manager` (Ctrl+C) automatically stops everything it
launched — no orphaned processes left behind.

---

## 3. The Task panel — two ways to make the robot move

You are always in exactly one of two modes, and switching between them is
enforced by the system — but **not the same way in both directions**:

- **Going Mode A → B** (clicking Explore/Follow Red while Stack Navigation
  is running): **fully automatic.** The old pipeline is stopped for you,
  the new one starts. No action needed from you.
- **Going Mode B → A** (clicking Stack's Navigation button while a task is
  active): **blocked, not auto-switched.** You'll get an error telling you
  to cancel the task first. Click **Cancel** on the Task panel, then Stack
  Navigation will start normally.

### Mode A — Manual driving
1. Start Stack → **Navigation + collision avoidance**.
2. Click a point on the **Live Localization** map to send it there.

`/planned_path` in the Health Monitor only turns green once `navigation`
has actually received a goal — it stays gray if navigation isn't running,
or is running but has never been given a destination. That's expected,
not a fault.

### Mode B — Autonomous task
Click **Explore** or **Follow red cube**. Each button starts its own
complete pipeline (see table below) — you do **not** need Stack's
Navigation button running at the same time; if it was already running,
the dashboard stops it for you automatically the instant you click
Explore or Follow Red Cube.

| Button | What it runs | Notes |
|---|---|---|
| **Explore** | `blind_exploration.launch.py` (no map yet) **or** `exploration.launch.py` (once a map exists) | Picked automatically — see below |
| **Follow red cube** | `follow_red_with_navigation.launch.py` (`follow_red` + `navigation` + `collision_avoidance`) | Only enabled once robot is `ready` |
| **Re-map** | resets SLAM confidence tracking | `slam` keeps running the whole time, this doesn't relaunch it |
| **Cancel** | stops whatever pipeline is active | Always safe to press |

**Explore's automatic choice:**
- **No map yet** → runs `blind_exploration`: purely reactive, drives
  forward, avoids/hugs obstacles using only live LiDAR data. No map or
  planner needed — this is what bootstraps the very first map.
- **A map already exists** → runs `exploration`: reads the existing
  `/map` to find unexplored "frontier" areas and drives to them via
  `navigation`'s planner. Needs a map to work at all, so it's only used
  once one exists.

You don't choose which one runs — the same **Explore** button picks the
right pipeline for you based on whether a map has been saved yet.

---

## 4. Why some buttons block each other (and why that's correct)

Several launch files bundle the *same node names* together:

- Stack **Navigation**: `navigation` + `collision_avoidance`
- **Explore** (map mode): `exploration` + `navigation` + `collision_avoidance`
- **Explore** (blind mode): `blind_exploration` + `collision_avoidance`
- **Follow red cube**: `follow_red` + `navigation` + `collision_avoidance`

If two of these ran at once, you'd get two nodes named `navigation` (or
`collision_avoidance`) fighting over the same topics — commands published
twice, unpredictable behavior, exactly the kind of "nothing works
normally" symptom that's hard to diagnose from the outside.

The dashboard now enforces this for you:
- Starting **Explore** or **Follow red cube** automatically stops Stack's
  Navigation if it was running.
- Trying to start Stack's Navigation while a task pipeline already owns
  it is rejected with a clear error instead of silently conflicting.

---

## 5. Health Monitor — what each row means

| Row | Comes from | Critical? |
|---|---|---|
| LiDAR /scan | `urg_node2` | Yes — robot force-stops if this goes down |
| Localization /pose | `pose_publisher` (bridges `roboclaw`'s `/odom`) | Yes — robot force-stops if this goes down |
| SLAM map /map | `slam` (`slam_toolbox`) | No |
| SLAM analyzer | `slam`'s confidence tracker | No |
| Planner /planned_path | `navigation` (only after it gets a goal) | No |
| Motor cmd /base/cmd_vel | `collision_avoidance` | No |

`/pose` timing is tuned for the real ~1 Hz update rate from `roboclaw`
(warns after 3s silence, faults after 8s) — loose enough to tolerate
normal USB/serial jitter without falsely E-stopping the robot.

---

## 6. Recovering from a fault

If you see **CRITICAL FAULT** (red banner):
1. Check which component is down in the Health Monitor.
2. If it's `/scan` or `/pose`, check the matching Stack button — is
   the driver still marked `running`? If it crashed, click Start again.
3. Once the component recovers and stays healthy, the robot automatically
   returns to `ready` — no button needed.
4. **E-Stop** (top right, red) always immediately zeros `/base/cmd_vel`
   and cancels the active task. Use it any time something looks wrong.

---

## 7. Quick reference — full session from scratch

```
1. ros2 launch robot_manager robot_manager.launch.py   (one terminal)
2. Open http://localhost:8765
3. Stack: LiDAR → Motors → SLAM → Navigation            (click, in order)
4. Either:
     a) click the map to navigate manually, or
     b) click Explore / Follow red cube for autonomous tasks
5. Watch Health Monitor — everything should read "ok"
6. E-Stop any time something looks wrong
```