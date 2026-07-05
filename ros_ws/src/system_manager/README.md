# System Manager Package

A ROS 2 package that manages the SLAM mapping workflow with automatic map saving and state transitions.

## Overview

The System Manager orchestrates the SLAM mapping process by monitoring confidence scores from the SLAM Analyzer and automatically saving the map when convergence is detected. It uses a finite state machine (FSM) to manage transitions between states.

## Nodes

### system_manager

Main controller node for SLAM workflow management.

**Subscribed Topics:**
- `/slam_confidence` (`std_msgs/msg/String`): Confidence metrics from SLAM Analyzer in JSON format

**Services Called:**
- `/slam_toolbox/save_map` (`slam_toolbox/srv/SaveMap`): Saves the current map

## Internal State Machine

The node transitions through the following states:

| State | Description |
|-------|-------------|
| `UNCONFIGURED` | Initial state after node creation |
| `CONFIGURED` | Resources allocated, subscriptions created |
| `WAIT_FOR_COMPLETION` | Monitoring confidence stream |
| `SAVE_MAP` | Saving the converged map |
| `STOP_MAPPING` | Stopping the mapping process |
| `FINISHED` | Mapping complete, ready for navigation |

## Confidence Threshold Logic

The node uses a debouncing mechanism to ensure stable convergence:

- **Threshold Values**: 
  - If confidence > 1.0: threshold is 50.0 (normalized 0-100 scale)
  - Otherwise: threshold is 0.5 (standard scale)
- **Stability Check**: Confidence must remain above threshold for 5 seconds before triggering map save
- **Reset**: If confidence drops below threshold during the timer, the countdown resets

## Usage

```bash
# Launch the system manager
ros2 run system_manager system_manager
# to set it in configure state 
ros2 lifecycle set /system_manager configure
# to set it in active state
ros2 lifecycle set /system_manager activate


```

The system manager should be started after the SLAM mapping process begins. It will automatically:
1. Monitor `/slam_confidence` topic
2. Wait for stable confidence above threshold
3. Call `/slam_toolbox/save_map` service
4. Log when mapping is complete

## Dependencies

- `rclpy`
- `std_msgs`
- `slam_toolbox` (for SaveMap service)

## Installation

```bash
cd /home/om/ros2_ws/omn/ros_ws
colcon build --packages-select system_manager
source install/setup.bash
```

## License

Apache License 2.0