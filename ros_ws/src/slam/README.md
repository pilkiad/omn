# SLAM Package

A ROS 2 package for SLAM (Simultaneous Localization and Mapping) using SLAM Toolbox with integrated convergence analysis and automatic stopping criteria.

## Overview

This package provides SLAM mapping capabilities with:

- **SLAM Toolbox Integration**: Uses the official `slam_toolbox` for online asynchronous SLAM mapping
- **SLAM Analyzer Node**: Monitors map convergence and publishes confidence scores
- **Automatic Stop Condition**: Can detect when mapping has converged (>= 97% confidence)

## Nodes

### slam_analyzer_node

Analyzes the map quality during SLAM and publishes confidence metrics.

**Subscribed Topics:**
- `/map` (`nav_msgs/msg/OccupancyGrid`): Current map from SLAM Toolbox
- `/mapping_finished` (`std_msgs/msg/Bool`): Signal to stop mapping

**Published Topics:**
- `/slam_confidence` (`std_msgs/msg/String`): JSON-encoded confidence metrics including:
  - `confidence`: Overall SLAM confidence score (0.0-1.0)
  - `frontier_ratio`: Ratio of frontier cells to total cells
  - `unknown_ratio`: Ratio of unknown cells to total cells
  - `growth_ratio`: Rate of known cell growth

**Confidence Calculation:**
The confidence score is computed based on four factors:
- Frontier density (40% weight)
- Known cells growth rate (30% weight)
- Unknown area ratio (20% weight)
- Motion stability (10% weight)

## Launch Files

### slam_mapping.launch.py

Launches the complete SLAM mapping setup:
- Static TF publisher for laser frame
- SLAM Toolbox (online_async mode)
- SLAM Analyzer node

```bash
ros2 launch slam slam_mapping.launch.py
```

## Configuration

Configuration file: `config/slam_config.yaml`

Key parameters:
- `use_sim_time`: Set to `true` for simulation, `false` for real hardware
- `odom_frame`, `map_frame`, `base_frame`: Frame configuration
- `scan_topic`: LiDAR scan topic (`/scan`)
- `resolution`: Map resolution (0.05 m/cell)
- `max_laser_range`: Maximum laser range (20.0 m)
- `map_update_interval`: Time between map updates (5.0 s)
- `do_loop_closing`: Enable loop closure (true)

## Installation

```bash
cd /home/om/ros2_ws/omn/ros_ws
colcon build --packages-select slam
source install/setup.bash
```

## Dependencies

- `rclpy`
- `nav_msgs`
- `slam_toolbox`
- `tf2_ros`
- `opencv-python` (cv2)
- `numpy`

## Usage

1. Start the SLAM mapping:
   ```bash
   ros2 launch slam slam_mapping.launch.py
   ```

2. Drive the robot through the environment

3. Monitor confidence:
   ```bash
   ros2 topic echo /slam_confidence
   ```

4. When confidence reaches 97%+, the analyzer will log convergence

## License

Apache License 2.0