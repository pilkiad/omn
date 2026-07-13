# navigation_gazebo

Gazebo Sim smoke-test harness for the `navigation` ROS 2 package.

This package launches a simulated world, bridges the required Gazebo topics into
ROS 2, starts a Nav2 map server, republishes the static map, converts Gazebo
odometry into the `/pose` pose input expected by `navigation`, and converts
`/target_vector` commands into `/cmd_vel` for the simulated robot.

## Package Contents

- `launch/nav_smoke_gazebo.launch.py` - main launch file for Gazebo, ROS/Gazebo
  bridges, map server, navigation, and optional RViz/collision avoidance.
- `worlds/` - Gazebo SDF worlds. The launch file currently uses
  `worlds/my_map_1.sdf` by default.
- `maps/` - occupancy maps used by `nav2_map_server`. The launch file currently
  uses `maps/my_map_1.yaml` by default.
- `config/nav_smoke_bridge.yaml` - `ros_gz_bridge` topic bridge configuration.
- `rviz/planned_path.rviz` - RViz view for inspecting the map, pose, and path.
- `navigation_gazebo/` - helper ROS 2 nodes used by the simulation harness.

## Dependencies

This is an `ament_python` ROS 2 package. Runtime dependencies are declared in
`package.xml` and include:

- `ros_gz_sim` and `ros_gz_bridge`
- `nav2_map_server` and `nav2_lifecycle_manager`
- `navigation`
- `collision_avoidance` and `collision_interfaces`
- `geometry_msgs`, `nav_msgs`, `sensor_msgs`, `tf2_msgs`, `tf2_ros`
- `rviz2`

From the workspace root, install missing ROS dependencies with:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

## Build

From the ROS workspace root:

```bash
colcon build --packages-select navigation_gazebo
source install/setup.bash
```

If dependent local packages such as `navigation`, `collision_avoidance`, or
`collision_interfaces` changed, build the workspace or include those packages in
the build command.

## Run

Default headless simulation:

```bash
ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py
```

Start Gazebo with the GUI:

```bash
ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py gui:=true
```

Start RViz with the bundled config:

```bash
ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py rviz:=true
```

Start the optional collision avoidance node:

```bash
ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py use_collision_avoidance:=true
```

Arguments can be combined:

```bash
ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py gui:=true rviz:=true use_collision_avoidance:=true
```

## Launch Arguments

| Argument | Default | Description |
| --- | --- | --- |
| `gui` | `false` | Start Gazebo with the GUI instead of server-only mode. |
| `use_sim_time` | `true` | Use Gazebo simulation time for launched ROS nodes. |
| `use_collision_avoidance` | `false` | Launch `collision_avoidance` for `/base/cmd_vel` comparison. |
| `rviz` | `false` | Start RViz. |
| `rviz_config` | `rviz/planned_path.rviz` | RViz config file used when `rviz:=true`. |

## Data Flow

The default launch sets up this ROS/Gazebo flow:

1. Gazebo Sim loads `worlds/my_map_1.sdf`.
2. `ros_gz_bridge` bridges simulation topics listed in
   `config/nav_smoke_bridge.yaml`.
3. `nav2_map_server` loads `maps/my_map_1.yaml`.
4. `map_service_to_topic` calls `/map_server/map` and republishes the returned
   occupancy grid on `/map`.
5. `odom_to_pos` subscribes to `/odom`, applies the configured initial map
   offset, and publishes `geometry_msgs/PoseStamped` on `/pose`.
6. `navigation` consumes the map, scan, and pose inputs and publishes
   `collision_interfaces/TargetVector` on `/target_vector`.
7. `target_vector_to_cmd_vel` converts `/target_vector` into
   `geometry_msgs/Twist` on `/cmd_vel`, which is bridged back to Gazebo.

## Bridged Topics

| ROS topic | Gazebo topic | Type | Direction |
| --- | --- | --- | --- |
| `/clock` | `/clock` | `rosgraph_msgs/msg/Clock` | Gazebo to ROS |
| `/scan` | `/scan` | `sensor_msgs/msg/LaserScan` | Gazebo to ROS |
| `/odom` | `/odom` | `nav_msgs/msg/Odometry` | Gazebo to ROS |
| `/tf` | `/tf` | `tf2_msgs/msg/TFMessage` | Gazebo to ROS |
| `/cmd_vel` | `/cmd_vel` | `geometry_msgs/msg/Twist` | ROS to Gazebo |
| `/base/cmd_vel` | `/base/cmd_vel` | `geometry_msgs/msg/Twist` | ROS to Gazebo |

## Helper Nodes

### `map_service_to_topic`

Requests an occupancy grid from a `nav_msgs/srv/GetMap` service and republishes
it periodically as `nav_msgs/msg/OccupancyGrid`.

Parameters:

- `service_name` - map service to call, default `/map_server/map`
- `topic_name` - output map topic, default `/map`
- `publish_period` - republish period in seconds, default `1.0`

### `odom_to_pos`

Converts `nav_msgs/msg/Odometry` from `/odom` into `geometry_msgs/msg/PoseStamped`
on `/pose`, applying an initial pose offset into the map frame.

Parameters:

- `output_topic` - pose output topic, default `/pose`
- `output_frame_id` - output frame, default `map`
- `initial_x` - initial x offset in meters, default `0.0`
- `initial_y` - initial y offset in meters, default `0.0`
- `initial_yaw` - initial yaw offset in radians, default `0.0`

### `target_vector_to_cmd_vel`

Converts `collision_interfaces/msg/TargetVector` commands into
`geometry_msgs/msg/Twist`. If no non-zero command is received before the stale
timeout, it publishes a zero twist.

Parameters:

- `input_topic` - target vector input, default `/target_vector`
- `output_topic` - twist output, default `/cmd_vel`
- `linear_scale` - linear velocity multiplier, default `1.0`
- `angular_scale` - angular velocity multiplier, default `1.0`
- `stale_timeout` - seconds before sending zero velocity, default `0.75`

## Useful Commands

Inspect active topics:

```bash
ros2 topic list
```

Watch the generated velocity command:

```bash
ros2 topic echo /cmd_vel
```

Watch the navigation pose input:

```bash
ros2 topic echo /pose
```

Check the map server lifecycle state:

```bash
ros2 lifecycle get /map_server
```

## Notes

- The launch file publishes a static `map -> odom` transform and configures
  `odom_to_pos` with the same initial map offset.
- The package still includes `nav_smoke` map/world assets, but the current launch
  defaults point at `my_map_1`.
- After editing maps, worlds, launch files, or config files, rebuild and source
  the workspace so the installed package share directory is updated.
