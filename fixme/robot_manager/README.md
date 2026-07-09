# robot_ws — System Manager workspace

This is a standard ROS2 workspace. It contains **your** three packages.
Your teammates' packages (camera_processor, lidar_processor, mapping,
localization, navigation, motion_controller) will sit next to these
under `src/` as separate folders in the same shared git repo — nobody's
package folder gets edited by anyone else.

```
robot_ws/
  src/
    system_manager_msgs/     # custom .msg definitions (TaskStatus, NodeStateArray, SystemHealth)
    system_manager/          # YOUR real code: 5 modules + orchestrator node
    mock_lifecycle_nodes/    # FAKE stand-ins for teammates' nodes, for testing only
    camera_processor/        # <- teammate adds this later
    lidar_processor/         # <- teammate adds this later
    mapping/                 # <- teammate adds this later
    localization/            # <- teammate adds this later
    navigation/               # <- teammate adds this later
    motion_controller/       # <- teammate adds this later
```

## Why 3 packages instead of 1

- `system_manager_msgs` exists only because **custom `.msg` files require
  an `ament_cmake` package** with `rosidl_generate_interfaces` — you
  cannot generate messages from a pure-Python (`ament_python`) package.
  This is a ROS2 restriction, not a stylistic choice.
- `system_manager` is your actual code: 5 modules + 1 orchestrator node,
  `ament_python`, depends on `system_manager_msgs`.
- `mock_lifecycle_nodes` is scaffolding, not part of the final robot.
  Delete this package (or just stop launching it) the moment real
  teammate nodes exist. It costs you nothing to keep around either way.

## Build

On your Ubuntu machine, with ROS2 (Humble/Iron/Jazzy) sourced:

```bash
cd robot_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

`--symlink-install` means edits to your `.py` files take effect without
rebuilding — only new files or changed `setup.py`/`package.xml` need a
rebuild.

## Run the full test rig (no teammate code needed)

```bash
ros2 launch mock_lifecycle_nodes mock_nodes.launch.py
```

This brings up 6 fake lifecycle nodes named exactly like your real
teammates' nodes will be, then starts your System Manager, which will:
1. wait for each mock node's `change_state` service to appear
2. configure + activate them in the startup order (camera → lidar →
   mapping → localization → navigation → motion_controller)
3. transition the global robot state to READY
4. start polling health every second and publishing dashboard topics

See `TESTING.md` for a full walkthrough of exercising every module
(task scheduling, failure injection, recovery, emergency stop).

## Run against real teammate nodes later

```bash
ros2 launch system_manager system_manager.launch.py
```

Your teammates should bring their nodes up **unconfigured** (don't call
`configure()`/`activate()` themselves in their own launch files) —
the System Manager is what drives their lifecycle. See `INTERFACES.md`
for the exact contract you and your teammates need to agree on.
