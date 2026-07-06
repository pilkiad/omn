---
title: "Beta 3 ( r2b3 )"
docname: "Releases/Beta3-Overview"
source: "Releases/Beta3-Overview.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Bouncy Bolson ( bouncy )](release-bouncy-bolson.md)

<a id="beta-3-r2b3"></a>

# Beta 3 (`r2b3`)

Table of Contents

- [Supported Platforms](#supported-platforms)
- [Features](#features)

  - [Improvements since Beta 2 release](#improvements-since-beta-2-release)
  - [New demo application](#new-demo-application)
  - [Selected features from previous Alpha/Beta releases](#selected-features-from-previous-alpha-beta-releases)
- [Known issues](#known-issues)

<a id="supported-platforms"></a>

## Supported Platforms

We support ROS 2 Beta 3 on three platforms: Ubuntu 16.04 (Xenial), macOS 10.12 (Sierra), and Windows 10.
We provide both binary packages and instructions for how to compile from source for all 3 platforms (see [install instructions](../installation/overview.md) as well as [documentation](https://docs.ros2.org/beta3/)).

<a id="features"></a>

## Features

<a id="improvements-since-beta-2-release"></a>

### Improvements since Beta 2 release

- Execution model in Python, many fixes to memory management in Python C extension
- Experimental rewrite of [ros\_control](https://github.com/ros2/ros2_control)
- Exposure of DDS implementation-specific symbols to users (for Fast RTPS and Connext) (see [example](https://github.com/ros2/demos/blob/6363be2efe2fea799d92bc22a66e776b2ca9c5d0/demo_nodes_cpp_native/src/talker.cpp))
- Logging [API](https://github.com/ros2/rclpy/blob/1ef2924ef8e154c0553edf0fdba4840b08b728f8/rclpy/rclpy/logging.py) in Python
- Fixed several memory leaks and race conditions in various packages
- Readded support for OpenSplice (on Linux and Windows atm) provided by PrismTech
- Use bloom (without patches) to make ROS 2 releases

<a id="new-demo-application"></a>

### New demo application

- [HSR demo](https://github.com/ruffsl/hsr_demo)

  - Remote control a HSR robot using a ROS 2 joystick controller
  - Running the `ros1_bridge` in a Docker container on the HSR (since the robot is running ROS 1 on Ubuntu Trusty)
  - Run a ROS 2 development version of [rviz](https://github.com/ros2/rviz) to visualize sensor data from the robot etc. (see [video](https://vimeo.com/237016358))

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
  - PrismTech OpenSplice: see limitations below
- A graph API for network events
- Distributed discovery
- Realtime safe code paths for publish and subscribe with compatible DDS implementation (only Connext at the moment)

  - Support for custom allocators
- ROS 1 <-> ROS 2 dynamic bridge node
- Executor threading model (C++ and Python)
- Component model to compose nodes at compile / link / runtime
- Managed component using a standard lifecycle
- Extended `.msg` format with new features:

  - Bounded arrays
  - Default values

<a id="known-issues"></a>

## Known issues

- On Windows Python launch files might hang when trying to abort using `Ctrl-C` (see [issue](https://github.com/ros2/launch/issues/64)). In order to continue using the shell which is blocked by the hanging command you might want to end the hanging Python process using the process monitor.
- OpenSplice support is currently not available for MacOS. Also [access to native handles](https://github.com/ros2/rmw_opensplice/issues/182) is not yet implemented.
- Using Connext it is currently not allowed for two topics with the same base name but different namespaces to have a different type (see [issue](https://github.com/ros2/rmw_connext/issues/234)).
