# Testing walkthrough

Run everything below from a sourced terminal (`source install/setup.bash`
after building). Use separate terminals where noted.

## 1. Bring the whole thing up

**Terminal A:**
```bash
ros2 launch mock_lifecycle_nodes mock_nodes.launch.py
```

You should see, in order: 6 mock nodes logging `on_configure` then
`on_activate`, then the System Manager logging
`Robot state: BOOTING -> READY`.

## 2. Confirm the lifecycle interface is really there

**Terminal B:**
```bash
ros2 lifecycle list localization
ros2 lifecycle get localization
```

You should see the standard transition list and `active [3]`. This
confirms the `/change_state` and `/get_state` services exist and work
exactly the way they will for a teammate's real node.

## 3. Watch your dashboard topics

```bash
ros2 topic echo /system_manager/node_states
ros2 topic echo /system_manager/health
```

## 4. Test the Task Scheduler (queue / reject / interrupt)

```bash
ros2 topic pub --once /system_manager/task_request std_msgs/msg/String "data: 'mapping'"
ros2 topic pub --once /system_manager/task_request std_msgs/msg/String "data: 'mapping'"
ros2 topic pub --once /system_manager/task_request std_msgs/msg/String "data: 'navigation'"
```

Watch `/system_manager/task_status`: the first `mapping` task should
run, the second `mapping` should be REJECTED (same priority as
current), and `navigation` should INTERRUPT the running `mapping` task
since 50 > 20.

## 5. Test failure detection + recovery

```bash
ros2 topic pub --once /localization/simulate_crash std_msgs/msg/String "data: 'x'"
```

Expected sequence in Terminal A's logs:
1. `HEALTH: localization expected active, saw inactive`
2. `Robot state: READY -> ERROR`
3. `Robot state: ERROR -> RECOVERY`
4. `navigation: deactivate OK`, `motion_controller: deactivate OK`
5. `Recovering localization...` → `localization: cleanup/configure/activate OK`
6. `motion_controller: activate OK`, `navigation: activate OK`
7. `Robot state: RECOVERY -> READY`

This is the exact failure policy from your project spec, executing for
real through the ROS2 lifecycle services.

## 6. Test emergency stop

```bash
ros2 topic pub --once /motion_controller/simulate_crash std_msgs/msg/String "data: 'x'"
```

Expected: `motion_controller failed -- EMERGENCY STOP`, followed by
`EMERGENCY STOP triggered by motion_controller` and
`Robot state: ... -> ERROR` (no recovery attempted, matching the spec's
"Controller fails -> Emergency Stop").

## 7. Swap a mock for a real teammate node

Once a teammate's real node exists and builds:
1. Stop `mock_nodes.launch.py`.
2. Write your own combined launch file (or ask a teammate to) that
   starts their real node(s) plus
   `ros2 launch system_manager system_manager.launch.py`.
3. Everything above should behave identically, because your code never
   changes based on whether the node behind the name is a mock or real.

## Unit-testing the modules without ROS2 at all

`robot_state_machine.py` and `task_scheduler.py` have zero ROS2
dependencies — you can `import` and test them directly with plain
`pytest`, no `colcon` or `rclpy` needed:

```python
from system_manager.robot_state_machine import RobotStateMachine, RobotState

def test_boot_to_ready():
    sm = RobotStateMachine()
    assert sm.transition(RobotState.READY) is True
    assert sm.state == RobotState.READY

def test_illegal_transition_rejected():
    sm = RobotStateMachine()
    assert sm.transition(RobotState.NAVIGATING) is False  # can't skip READY
```
