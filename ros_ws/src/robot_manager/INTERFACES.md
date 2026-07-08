# Interface contract between System Manager and teammate nodes

Share this file with your team. It's the entire agreement needed for
your code and theirs to work together without touching each other's
packages.

## 1. Every teammate node MUST be a LifecycleNode

Not `rclpy.node.Node` — it has to inherit from the lifecycle base class:

```python
# Python (rclpy)
from rclpy.lifecycle import Node as LifecycleNode

class MappingNode(LifecycleNode):
    def __init__(self):
        super().__init__('mapping')   # <- the NAME is the contract

    def on_configure(self, state): ...
    def on_activate(self, state): ...
    def on_deactivate(self, state): ...
    def on_cleanup(self, state): ...
    def on_shutdown(self, state): ...
```

```cpp
// C++ (rclcpp_lifecycle), if any teammate uses C++
class MappingNode : public rclcpp_lifecycle::LifecycleNode {
public:
  MappingNode() : LifecycleNode("mapping") {}
  // on_configure, on_activate, on_deactivate, on_cleanup, on_shutdown overrides
};
```

## 2. Agreed node names (edit this table with your team)

| Module | ROS2 node name | Owner |
|---|---|---|
| Camera Processor | `camera_processor` | teammate |
| LiDAR Processor | `lidar_processor` | teammate |
| Mapping | `mapping` | teammate |
| Localization | `localization` | teammate |
| Navigation | `navigation` | teammate |
| Motion Controller | `motion_controller` | teammate |

These exact strings are what `system_manager/config/managed_nodes.yaml`
and your recovery policy table key off. If a teammate's node name
doesn't match, your System Manager simply won't find it — that's the
single most likely integration bug, so agree on names in writing.

## 3. What this contract gives you for free

The moment a node inherits `LifecycleNode` with the name above, these
exist automatically — no code required from either side:

- `/<name>/change_state` — service, `lifecycle_msgs/srv/ChangeState`
  (your Lifecycle Manager calls this to configure/activate/deactivate/
  cleanup/shutdown their node)
- `/<name>/get_state` — service, `lifecycle_msgs/srv/GetState`
  (your Health Monitor polls this)
- `/<name>/transition_event` — topic, `lifecycle_msgs/msg/TransitionEvent`
  (optional: subscribe here instead of polling, for push-based health)

## 4. What teammates should NOT do

- Don't call `configure()`/`activate()` on themselves at startup — the
  System Manager drives lifecycle transitions. If their launch file
  activates the node immediately, your Lifecycle Manager's own
  `configure()` call will be rejected (already active).
- Don't rename their node after agreeing on it here without telling you.
- Don't publish emergency-stop or crash behavior by killing the process
  — instead, return `TransitionCallbackReturn.FAILURE` from an `on_*`
  callback, or call `self.trigger_deactivate()`, so it shows up as a
  normal lifecycle transition your Health Monitor can see.

## 5. What YOU (System Manager) publish for the dashboard / teammates

| Topic | Type | Published by |
|---|---|---|
| `system_manager/node_states` | `system_manager_msgs/NodeStateArray` | Health Monitor |
| `system_manager/health` | `system_manager_msgs/SystemHealth` | Dashboard Backend |
| `system_manager/task_status` | `system_manager_msgs/TaskStatus` | Dashboard Backend |

| Topic | Type | Subscribed by |
|---|---|---|
| `system_manager/task_request` | `std_msgs/String` (task name, e.g. "navigation") | Task Scheduler |

This is intentionally a plain `String` topic for now — swap it for a
proper action server later if the dashboard needs live feedback
("navigation 40% to goal") or the ability to cancel a task mid-flight.

## 6. For the RViz dashboard: map, live position, and click-to-navigate

Your RViz dashboard (`system_manager/config/dashboard.rviz`) is already
wired up for this. It needs three things from teammates, none of which
involve writing any RViz code — RViz's map view, robot-position display,
and "2D Goal Pose" click button are all built in:

| Needed for | Who provides it | What exactly |
|---|---|---|
| Live map view | Mapping | Publish `nav_msgs/OccupancyGrid` on topic `/map`, with `frame_id: map` |
| Live robot position | Localization | Broadcast the TF transform `map -> odom` (and `odom -> base_link` typically comes from whoever does wheel odometry / the motion controller) |
| Click-to-navigate | Navigation | Subscribe to topic `/goal_pose` (`geometry_msgs/PoseStamped`) |

That `/goal_pose` topic is exactly what RViz's built-in **"2D Goal Pose"**
toolbar button publishes when someone clicks a spot on the map. Nobody
needs to build a "send goal" button — it already exists in RViz. Your
teammate on Navigation just needs to receive that click as a normal ROS2
topic subscription and act on it.

The moment those three things exist, opening
`ros2 launch mock_lifecycle_nodes mock_nodes_with_rviz.launch.py` (swap
in a launch file with real nodes later) will show the live map, the
robot moving on it, and clicking will send it somewhere — with zero
changes needed to the dashboard config.

## 7. If a teammate uses a DIFFERENT lifecycle framework version

Some ROS2 distros vary slightly in `rclpy.lifecycle` API surface (e.g.
`TransitionCallbackReturn` import path). If a teammate's node builds and
its `ros2 lifecycle list <node>` and `ros2 lifecycle get <node>` commands
work from the terminal, your System Manager will work with it — the
compatibility check is a CLI check, not a code review.
