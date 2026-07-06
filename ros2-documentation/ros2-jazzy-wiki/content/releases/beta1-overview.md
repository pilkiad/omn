---
title: "Beta 1 ( Asphalt )"
docname: "Releases/Beta1-Overview"
source: "Releases/Beta1-Overview.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md) | [Bouncy Bolson ( bouncy )](release-bouncy-bolson.md)

<a id="beta-1-asphalt"></a>

# Beta 1 (`Asphalt`)

Table of Contents

- [Supported Platforms](#supported-platforms)
- [Features](#features)

  - [Improvements since Alpha 8 release](#improvements-since-alpha-8-release)
  - [Selected features from previous Alpha releases](#selected-features-from-previous-alpha-releases)
  - [Known issues](#known-issues)

<a id="supported-platforms"></a>

## Supported Platforms

We support ROS 2 Beta 1 on three platforms: Ubuntu 16.04 (Xenial), Mac OS X 10.11 (El Capitan), and Windows 8.1 and 10. We provide both binary packages and instructions for how to compile from source for all 3 platforms.

<a id="features"></a>

## Features

<a id="improvements-since-alpha-8-release"></a>

### Improvements since Alpha 8 release

- Support for node composition at compile, link, or runtime.
- A standard lifecycle for managed nodes.
- Improved support for Quality of Service tuning and tests.
- [New and updated design documents](https://design.ros2.org/)
- More [tutorials](../tutorials/overview.md) and [examples](https://github.com/ros2/examples)
- Bridging services to / from ROS 1 (in addition to topics)

<a id="selected-features-from-previous-alpha-releases"></a>

### Selected features from previous Alpha releases

For the complete list, see [earlier release notes](../getting-started/ros-2-documentation.md).

- C++ and Python implementations of ROS 2 client libraries including APIs for:

  - Publishing and subscribing to ROS topics
  - Requesting and replying ROS services (synchronous (C++ only) and asynchronous)
  - Getting and setting ROS parameters (C++ only, synchronous and asynchronous)
  - Timer callbacks
  - Support for interoperability between multiple DDS/RTPS implementations
  - eProsima Fast RTPS is our default implementation, and is included in the binary packages
  - RTI Connext is supported: build from source to try it out
  - We initially supported PrismTech OpenSplice but eventually decided to drop it
- A graph API for network events
- Distributed discovery
- Realtime safe code paths for publish and subscribe with compatible DDS implementation (only Connext at the moment)

  - Support for custom allocators
- ROS 1 <-> ROS 2 dynamic bridge node
- Executor threading model in C++
- Extended `.msg` format with new features:

  - Bounded arrays
  - Default values

<a id="known-issues"></a>

### Known issues

- We’re tracking issues in various repositories, but the main entry point is the [ros2/ros2 issue tracker](https://github.com/ros2/ros2/issues)
- We’d like to highlight a [known issue](https://github.com/ros2/rmw_fastrtps/issues/81) that we are working with eProsima to fix that results in significantly degrated performance for large messages under FastRTPS.
  This will be observed when running some of the demos with larger image resolutions.
