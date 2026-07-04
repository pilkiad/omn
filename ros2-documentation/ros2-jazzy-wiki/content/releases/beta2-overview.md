---
title: "Beta 2 ( r2b2 )"
docname: "Releases/Beta2-Overview"
source: "Releases/Beta2-Overview.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md) | [Bouncy Bolson ( bouncy )](release-bouncy-bolson.md)

<a id="beta-2-r2b2"></a>

# Beta 2 (`r2b2`)

Table of Contents

- [Supported Platforms](#supported-platforms)
- [Features](#features)

  - [Improvements since Beta 1 release](#improvements-since-beta-1-release)
  - [New demo application](#new-demo-application)
  - [Selected features from previous Alpha/Beta releases](#selected-features-from-previous-alpha-beta-releases)
  - [Known issues](#known-issues)

<a id="supported-platforms"></a>

## Supported Platforms

We support ROS 2 Beta 2 on three platforms: Ubuntu 16.04 (Xenial), macOS 10.12 (Sierra), and Windows 10.
We provide both binary packages and instructions for how to compile from source for all 3 platforms (see [install instructions](../installation/overview.md) as well as [documentation](https://docs.ros2.org/beta2/)).

<a id="features"></a>

## Features

<a id="improvements-since-beta-1-release"></a>

### Improvements since Beta 1 release

- DDS\_Security support (aka SROS2, see [sros2](https://github.com/ros2/sros2))
- Debian packages for Ubuntu Xenial
- Typesupport has been redesigned so that you only build a single executable and can choose one of the available RMW implementations by setting an environment variable (see [documentation](../how-to/working-with-multiple-rmw-implementations.md)).
- Namespace support for nodes and topics (see [design article](https://design.ros2.org/articles/topic_and_service_names.html), see known issues below).
- A set of command-line tools using the extensible `ros2` command (see [conceptual article](../concepts/basic/about-command-line-tools.md)).
- A set of macros for logging messages in C / C++ (see API docs of [rcutils](https://docs.ros2.org/beta2/api/rcutils/index.html)).

<a id="new-demo-application"></a>

### New demo application

- [Turtlebot 2 demos](https://github.com/ros2/turtlebot2_demo) using the following repositories that have been (partially) converted to ROS 2 (Linux only):

  - [ros\_astra\_camera](https://github.com/ros2/ros_astra_camera.git)
  - [depthimage\_to\_laserscan](https://github.com/ros2/depthimage_to_laserscan.git)
  - [pcl\_conversions](https://github.com/ros2/pcl_conversions.git)
  - [cartographer](https://github.com/ros2/cartographer.git)
  - [cartographer\_ros](https://github.com/ros2/cartographer_ros.git)
  - [ceres-solver](https://github.com/ros2/ceres-solver.git)
  - [navigation](https://github.com/ros2/navigation.git)
  - [teleop\_twist\_keyboard](https://github.com/ros2/teleop_twist_keyboard.git)
  - [joystick\_drivers](https://github.com/ros2/joystick_drivers.git)
  - [teleop\_twist\_joy](https://github.com/ros2/teleop_twist_joy.git)
- [Dummy\_robot demo](../tutorials/demos/dummy-robot-demo.md):

  - [robot\_model](https://github.com/ros2/robot_model)
  - [robot\_state\_publisher](https://github.com/ros2/robot_state_publisher)

<a id="selected-features-from-previous-alpha-beta-releases"></a>

### Selected features from previous Alpha/Beta releases

For the complete list, see [earlier release notes](../getting-started/ros-2-documentation.md).

- C++ and Python implementations of ROS 2 client libraries including APIs for:

  - Publishing and subscribing to ROS topics
  - Requesting and replying ROS services (synchronous (C++ only) and asynchronous)
  - Getting and setting ROS parameters (C++ only, synchronous and asynchronous)
  - Timer callbacks
- Support for interoperability between multiple DDS/RTPS implementations

  - eProsima Fast RTPS is our default implementation, and is included in the binary packages
  - RTI Connext is supported: build from source to try it out
  - We initially supported PrismTech OpenSplice but support for it is currently on hold
- A graph API for network events
- Distributed discovery
- Realtime safe code paths for publish and subscribe with compatible DDS implementation (only Connext at the moment)

  - Support for custom allocators
- ROS 1 <-> ROS 2 dynamic bridge node
- Executor threading model (C++ only)
- Component model to compose nodes at compile / link / runtime
- Managed component using a standard lifecycle
- Extended `.msg` format with new features:

  - Bounded arrays
  - Default values

<a id="known-issues"></a>

### Known issues

- We’re tracking issues in various repositories, but the main entry point is the [ros2/ros2 issue tracker](https://github.com/ros2/ros2/issues)
- We’d like to highlight a [known issue](https://github.com/ros2/rmw_connext/issues/234) that we are looking into which doesn’t allow two topics with the same base name but different namespaces to have a different type when using `rmw_connext_cpp`.
- Services with long responses are not working with Fast-RTPS. The fix, while not being part of beta2, is available upstream so you can work around this issue by building from source using Fast-RTPS master branch.
