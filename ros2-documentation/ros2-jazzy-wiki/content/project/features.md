---
title: "Features Status"
docname: "The-ROS2-Project/Features"
source: "The-ROS2-Project/Features.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "project"
tags: ["ros2", "jazzy", "project"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Project hub](../../wiki/tooling-map.md)
> Related: [Contributing](contributing.md) | [Feature Ideas](feature-ideas.md) | [Marketing](marketing.md) | [Metrics](metrics.md) | [Platform EOL Policy](platform-eol-policy.md)

<a id="features-status"></a>
<a id="features"></a>

# Features Status

The features listed below are available in the current ROS 2 release.
Unless otherwise specified, the features are available for all supported platforms (Ubuntu 24.04 (Noble), Windows 10), DDS implementations (eProsima Fast DDS, RTI Connext DDS, and Eclipse Cyclone DDS) and programming language client libraries (C++ and Python).
For planned future development, see the [Roadmap](roadmap.md).

| Functionality | Link | Fine print |
| --- | --- | --- |
| Discovery, transport and serialization over DDS | [Article](https://design.ros2.org/articles/ros_on_dds.html) |  |
| Support for [multiple DDS implementations](../concepts/intermediate/about-different-middleware-vendors.md), chosen at runtime | [Concept](../concepts/intermediate/about-different-middleware-vendors.md), [How-to Guide](../how-to/working-with-multiple-rmw-implementations.md) | Currently Eclipse Cyclone DDS, eProsima Fast DDS, and RTI Connext DDS are fully supported. |
| Common core client library that is wrapped by language-specific libraries | [Details](../concepts/basic/about-client-libraries.md) |  |
| Publish/subscribe over topics | [Sample code](https://github.com/ros2/examples), [Article](https://design.ros2.org/articles/topic_and_service_names.html) |  |
| Clients and services | [Sample code](https://github.com/ros2/examples) |  |
| Set/retrieve parameters | [Sample code](https://github.com/ros2/demos/tree/0.5.1/demo_nodes_cpp/src/parameters) |  |
| ROS 1 - ROS 2 communication bridge | [Tutorial](https://github.com/ros2/ros1_bridge/blob/master/README.md) | Available for topics and services, not yet available for actions. |
| Quality of service settings for handling non-ideal networks | [Demo](../tutorials/demos/quality-of-service.md) |  |
| Inter- and intra-process communication using the same API | [Demo](../tutorials/demos/intra-process-communication.md) | Currently only in C++. |
| Composition of node components at compile, link, load, or run time | [Demo](../tutorials/intermediate/composition.md) | Currently only in C++. |
| Multiple executors (at level of callback groups) in same node | [Demo](https://github.com/ros2/examples/tree/jazzy/rclcpp/executors/cbg_executor) | Only in C++. |
| Support for nodes with managed lifecycles | [Demo](../tutorials/demos/managed-nodes.md) | Currently only in C++. |
| DDS-Security support | [Demo](https://github.com/ros2/sros2) |  |
| Command-line introspection tools using an extensible framework | [Concept](../concepts/basic/about-command-line-tools.md) |  |
| Launch system for coordinating multiple nodes | [Tutorial](../tutorials/intermediate/launch/launch-system.md) |  |
| Namespace support for nodes and topics | [Article](https://design.ros2.org/articles/topic_and_service_names.html) |  |
| Static remapping of ROS names | [How-to Guide](../how-to/node-arguments.md) |  |
| Demos of an all-ROS 2 mobile robot | [Demo](https://github.com/ros2/turtlebot2_demo) |  |
| Preliminary support for real-time code | [Demo](../tutorials/demos/real-time-programming.md), [demo](../tutorials/advanced/allocator-template-tutorial.md) | Linux only. Not available for Fast RTPS. |
| Preliminary support for “bare-metal” microcontrollers | [Wiki](https://github.com/ros2/freertps/wiki) |  |
| Content filtering subscription | [Demo](../tutorials/demos/content-filtering-subscription.md) | Currently only in C++. |
| Service Introspection | [Demo](../tutorials/demos/service-introspection.md) |  |

Besides core features of the platform, the biggest impact of ROS comes from its available packages.
The following are a few high-profile packages which are available in the latest release:

- [gazebo\_ros\_pkgs](https://index.ros.org/r/gazebo_ros_pkgs/)
- [image\_transport](https://index.ros.org/r/image_common)
- [navigation2](https://index.ros.org/r/navigation2/)
- [rosbag2](https://index.ros.org/r/rosbag2/)
- [RQt](https://index.ros.org/r/rqt/)
- [RViz2](https://index.ros.org/r/rviz/)
