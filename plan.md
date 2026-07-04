# Finish A* Navigation Planner

  ## Summary

  Complete ros_ws/src/navigation/navigation/navigation.py as a ROS 2 navigation node that plans
  from the robot’s current SLAM pose to an RViz goal using A*, then publishes
  collision_interfaces/TargetVector to /target_vector for collision_avoidance to convert into /
  base/cmd_vel.

  ## Interfaces

  - Subscribe to /map as nav_msgs/OccupancyGrid.
  - Subscribe to /pos as geometry_msgs/PoseStamped for the SLAM robot pose.
  - Keep /pose as an optional geometry_msgs/PoseWithCovarianceStamped compatibility fallback if
    already present.

  - Subscribe to /goal_pose as geometry_msgs/PoseStamped from RViz2.
  - Publish /target_vector as collision_interfaces/TargetVector.
  - Do not change TargetVector.msg; use linear and angular as desired motion commands.

  ## Implementation Changes

  - Store map metadata, occupancy data, robot pose, goal pose, and planner state in Navigation.
  - Convert world coordinates to grid cells using map origin and resolution; convert planned grid
    cells back to world waypoint centers.

  - Implement A* over an 8-connected grid with cardinal cost 1.0, diagonal cost sqrt(2), and
    Euclidean or octile heuristic.

  - Treat occupied cells >= 50 and unknown cells -1 as blocked.
  - Prevent diagonal corner cutting by requiring both adjacent cardinal cells to be free before
    allowing a diagonal step.

  - Add obstacle padding by rejecting cells within one inflated obstacle radius of occupied/
    unknown cells, using OBSTACLE_INFLATION_RADIUS_M = 0.18.

  - Replan when the map changes, the goal changes, no path exists, the current path becomes
    blocked, or the robot drifts off the current path.

  - Stop and publish a zero TargetVector when map/pose/goal is missing, the goal is reached,
    start/goal is outside the map, start/goal is blocked, or no path exists.

  - Follow the path using a short lookahead waypoint and convert heading error into
    TargetVector.linear/angular, keeping the existing conservative defaults: LINEAR_SPEED = 0.12,
    ANGULAR_GAIN = 1.6, MAX_ANGULAR_SPEED = 0.7, GOAL_TOLERANCE = 0.12.

  - Leave manager/exploration/collision avoidance behavior out of scope; navigation should only
    fit into the existing /target_vector -> collision_avoidance -> /base/cmd_vel chain.

  ## Test Plan

  - Add focused pytest coverage for A*: straight path, obstacle wall with gap, no path, unknown
    cells blocked, and diagonal corner-cut prevention.

  - Test world/grid coordinate conversion with non-zero origin and map resolution.
  - Test target-vector generation for forward, left-turn, right-turn, and goal-reached cases.
  - Run syntax check for navigation.py.
  - Run colcon test --packages-select navigation collision_interfaces after implementation.

  ## Assumptions

  - /pos from SLAM is geometry_msgs/PoseStamped.
  - Unknown occupancy grid cells must be treated as blocked for safe navigation.
  - RViz2 goals arrive on /goal_pose.
  - Only one high-level behavior node should publish /target_vector at runtime unless a manager
    later arbitrates control.




# Gazebo Smoke Test For Your Navigation Node

  ## Summary

  - Target navigation1.py as the implementation to test

  - Build a deterministic Gazebo Sim test harness for ROS 2 Jazzy + Gazebo Sim
    8, using ros_gz_sim and ros_gz_bridge, which are installed locally.

  - Use a static nav2_map_server map instead of SLAM for the first test, so
    failures isolate navigation/control logic.

  - Approach follows Gazebo’s ROS 2 launch, bridge, and project-template
    guidance, plus the Gazebo DiffDrive and Sensors systems docs: launch
    Gazebo (https://gazebosim.org/docs/latest/ros2_launch_gazebo/), ROS-Gazebo
    bridge (https://gazebosim.org/docs/latest/ros2_integration/), project
    template
    (https://gazebosim.org/docs/latest/ros_gz_project_template_guide/),
    DiffDrive
    (https://gazebosim.org/api/sim/8/classgz_1_1sim_1_1systems_1_1DiffDrive.html
),
    Sensors
    (https://gazebosim.org/api/sim/8/classgz_1_1sim_1_1systems_1_1Sensors.html).

  ## Key Changes

  
  - Add a new ament_python package named navigation_gazebo containing:
      - A simple Gazebo world with one diff-drive robot, lidar, boundary
        walls, and one obstacle.

      - A matching static map YAML/PGM served by nav2_map_server.
      - A bridge YAML for /clock, /scan, /odom, /tf, and /base/cmd_vel.
      - An odom_to_pos adapter node that subscribes to /odom and publishes /
        pos as geometry_msgs/PoseStamped, matching navigation.py.

      - A launch file nav_smoke_gazebo.launch.py that starts Gazebo, the
        bridge, map server, lifecycle manager, static map -> odom transform,
        odom_to_pos, navigation, and collision_avoidance.

  ## Test Flow

  - Build:

    cd /home/nasimpcm/Desktop/omn/ros_ws
    colcon build --packages-select collision_interfaces navigation
    collision_avoidance navigation_gazebo
    source install/setup.bash

  - Launch:

    ros2 launch navigation_gazebo nav_smoke_gazebo.launch.py gui:=true

  - Send a goal:

    ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "{header:
    {frame_id: map}, pose: {position: {x: 2.5, y: 1.0, z: 0.0}, orientation: {w:
    1.0}}}"

  - Verify:
      - /map, /scan, /odom, /pos, /goal_pose, /target_vector, and /base/
        cmd_vel exist.

      - navigation logs a planned path.
      - /target_vector publishes nonzero commands.
      - collision_avoidance publishes /base/cmd_vel.
      - The robot moves toward the goal in Gazebo and stops within roughly
        0.25 m.

  ## Assumptions

  - Use Gazebo Sim, not Gazebo Classic, because this machine has gz sim
    8.11.0, ros_gz_sim, and ros_gz_bridge, but not gazebo_ros.

  - Use the deterministic static-map test first; add a later SLAM Toolbox
    launch only after this basic closed loop works.

  - In the simulator you need to publish directly to /cmd_vel as the collision avoidance node will not work correctly in the simulator. For the real world application (after you have tested) you may switch to publishing your desired movement to /target_vector using from collision_interfaces.msg import TargetVector which takes two values: linear and angular velocity (you can see this also in the target_vector.msg file)
  - 
