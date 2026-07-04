---
title: "Intel ROS 2 Projects"
docname: "Related-Projects/Intel-ROS2-Projects"
source: "Related-Projects/Intel-ROS2-Projects.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "related-projects"
tags: ["ros2", "jazzy", "related-projects"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Related Projects hub](../../wiki/tooling-map.md)
> Related: [NVIDIA ROS 2 Projects](nvidia-ros2-projects.md) | [Visualizing Data and Teleoperating with Phantom Bridge](visualizing-data-and-teleoperating-with-phantom-bridge.md)

<a id="intel-ros-2-projects"></a>

# Intel ROS 2 Projects

Intel® Robotics Open Source Project (Intel® ROS Project) to enable object detection/location/tracking, people detection, vehicle detection, industry robot arm grasp point analysis with kinds of Intel technologies and platforms, including CPU, GPU, [Intel® Movidius™ NCS](https://www.intel.com/content/www/us/en/developer/tools/neural-compute-stick/overview.html) optimized deep learning backend, FPGA, [Intel® RealSense™](https://www.intel.com/content/www/us/en/architecture-and-technology/realsense-overview.html) camera, etc.

<a id="key-projects"></a>

## Key Projects

We are working on below ROS 2 projects and publish source code through <https://github.com/intel/> or ROS 2 GitHub repo gradually.

- [ROS2 OpenVINO](https://github.com/intel/ros2_openvino_toolkit): ROS 2 package for Intel® Visual Inference and Neural Network Optimization Toolkit to develop multiplatform computer vision solutions.
- [ROS2 RealSense Camera](https://github.com/IntelRealSense/realsense-ros): ROS 2 package for Intel® RealSense™ D400 serial cameras
- [ROS2 Movidius NCS](https://github.com/intel/ros2_intel_movidius_ncs): ROS 2 package for object detection with Intel® Movidius™ Neural Computing Stick (NCS).
- [ROS2 Object Messages](https://github.com/intel/ros2_object_msgs): ROS 2 messages for object.
- [ROS2 Object Analytics](https://github.com/intel/ros2_object_analytics): ROS 2 package for object detection, tracking and 2D/3D localization.
- [ROS2 Message Filters](https://github.com/ros2/message_filters): ROS 2 package for message synchronization with time stamp.
- [ROS2 CV Bridge](https://github.com/ros-perception/vision_opencv/tree/ros2/cv_bridge): ROS 2 package to bridge with openCV.
- [ROS2 Object Map](https://github.com/intel/ros2_object_map): ROS 2 package to mark tag of objects on map when SLAM based on information provided by ROS 2 object analytics.
- [ROS2 Moving Object](https://github.com/intel/ros2_moving_object): ROS 2 package to provide object motion information (like object velocity on x, y, z axis) based on information provided by ROS 2 object analytics.
- [ROS2 Grasp Library](https://github.com/intel/ros2_grasp_library): ROS 2 package for grasp position analysis, and compatible with [MoveIt](https://github.com/ros-planning/moveit2.git) grasp interfaces.
- [ROS2 Navigation](https://github.com/ros-planning/navigation2): ROS 2 package for robot navigation, it’s already integrated to ROS 2 Crystal release.
- [Intel Robot DevKit (SDK)](https://github.com/intel/robot_devkit): An open source project which enables developers to easily and efficiently create, customize, optimize, and deploy a robot software stack to an Autonomous Mobile Robot (AMR) platform based on the Robot Operating System 2 (ROS 2) framework.

<a id="reference"></a>

## Reference

ROS components at: <https://wiki.ros.org/IntelROSProject> shows the relationship among those packages, which also applies to ROS 2.
