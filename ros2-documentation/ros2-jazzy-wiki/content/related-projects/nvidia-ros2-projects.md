---
title: "NVIDIA ROS 2 Projects"
docname: "Related-Projects/Nvidia-ROS2-Projects"
source: "Related-Projects/Nvidia-ROS2-Projects.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "related-projects"
tags: ["ros2", "jazzy", "related-projects"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Related Projects hub](../../wiki/tooling-map.md)
> Related: [Intel ROS 2 Projects](intel-ros2-projects.md) | [Visualizing Data and Teleoperating with Phantom Bridge](visualizing-data-and-teleoperating-with-phantom-bridge.md)

<a id="nvidia-ros-2-projects"></a>

# NVIDIA ROS 2 Projects

NVIDIA Jetson is working towards developing ROS 2 packages to ease the development of AI applications for robotics.

<a id="ros-projects"></a>

## ROS Projects

- [Isaac ROS Nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox) : Hardware-accelerated 3D scene reconstruction and Nav2 local costmap provider using nvblox.
- [Isaac ROS Object Detection](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection) : Deep learning model support for object detection including DetectNet.
- [Isaac ROS DNN Inference](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference) : This repository provides two NVIDIA GPU-accelerated ROS 2 nodes that perform deep learning inference using custom models.
  One node uses the TensorRT SDK, while the other uses the Triton SDK.
- [Isaac ROS Visual SLAM](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam) : This repository provides a ROS 2 package that estimates stereo visual inertial odometry using the Isaac Elbrus GPU-accelerated library.
- [Isaac ROS Argus Camera](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_argus_camera) : This repository provides monocular and stereo nodes that enable ROS developers to use cameras connected to Jetson platforms over a CSI interface.
- [Isaac ROS image\_pipeline](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline) : This metapackage offers similar functionality as the standard, CPU-based image\_pipeline metapackage, but does so by leveraging the Jetson platform’s specialized computer vision hardware.
- [Isaac ROS Common](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common) : Isaac ROS common utilities for use in conjunction with the Isaac ROS suite of packages.
- [Isaac ROS AprilTags](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag) : ROS 2 node uses the NVIDIA GPU-accelerated AprilTags library to detect AprilTags in images and publish their poses, ids, and additional metadata.
- [ROS and ROS 2 Docker Images](https://github.com/NVIDIA-AI-IOT/ros2_jetson/tree/main/docker) : Docker images for easy deployment on the NVIDIA Jetson platform, consisting of ROS 2, PyTorch, and other important machine learning libraries.
- [ROS and ROS 2 DockerFiles](https://github.com/dusty-nv/jetson-containers): Dockerfiles for ROS 2 based on l4t which all you to build your own Docker image.
- [ROS 2 Packages for PyTorch and TensorRT](https://github.com/NVIDIA-AI-IOT/ros2_torch_trt): ROS 2 packageis for classification and object detection tasks using PyTorch and NVIDIA TensorRT.
  This tutorial is a good starting point AI integration with ROS 2 on NVIDIA Jetson.
- [ROS / ROS 2 Packages for Accelerated Deep Learning Nodes](https://github.com/dusty-nv/ros_deep_learning): Deep learning image recognition, object detection, and semantic segmentation inference nodes and camera/video streaming nodes for ROS/ROS 2 using the [jetson-inference](https://github.com/dusty-nv/jetson-inference) library and [NVIDIA Hello AI World tutorial](https://developer.nvidia.com/embedded/twodaystoademo).
- [ROS 2 Package for Human Pose Estimation](https://github.com/NVIDIA-AI-IOT/ros2_trt_pose): A ROS 2 package for human pose estimation.
- [ROS 2 Package for Hand Pose Estimation and Gesture Classification](https://github.com/NVIDIA-AI-IOT/ros2_trt_pose_hand): A ROS 2 package for real-time hand pose estimation and gesture classification using TensorRT.
- [GPU accelerated ROS 2 Packages for Monocular Depth Estimation](https://github.com/NVIDIA-AI-IOT/ros2_torch2trt_examples): ROS 2 package for NVIDIA GPU-accelerated torch2trtxb examples such as monocular depth estimation and text detection.
- [ROS 2 Package for Jetson stats](https://github.com/NVIDIA-AI-IOT/ros2_jetson_stats): ROS 2 package for monitoring and controlling your NVIDIA Jetson [Xavier NX, Nano, AGX Xavier, TX1, TX2].
- [ROS 2 Packages for DeepStream SDK](https://github.com/NVIDIA-AI-IOT/ros2_deepstream): ROS 2 package for NVIDIA DeepStream SDK.

<a id="simulation-projects"></a>

## Simulation Projects

- [Isaac Sim Nav2](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_ros2_navigation.html) : In this ROS 2 sample, we are demonstrating Omniverse Isaac Sim integrated with the ROS 2 Nav2 project.
- [Isaac Sim Multiple Robot ROS 2 Navigation](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_ros2_multi_navigation.html) : In this ROS 2 sample, we are demonstrating Omniverse Isaac Sim integrated with the ROS 2 Nav2 stack to perform simultaneous multiple robot navigation.

<a id="references"></a>

## References

More updates on NVIDIA Jetson ROS 2 can be found [here](https://nvidia-ai-iot.github.io/ros2_jetson/).
