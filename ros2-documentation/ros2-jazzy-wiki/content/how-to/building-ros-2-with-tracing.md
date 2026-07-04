---
title: "Building ROS 2 with tracing"
docname: "How-To-Guides/Building-ROS-2-with-Tracing"
source: "How-To-Guides/Building-ROS-2-with-Tracing.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md) | [Cross-compilation](cross-compilation.md)

<a id="building-ros-2-with-tracing"></a>

# Building ROS 2 with tracing

Table of Contents

- [Prerequisites](#prerequisites)
- [Build configurations](#build-configurations)

  - [Building without tracepoints](#building-without-tracepoints)
  - [Building without instrumentation](#building-without-instrumentation)
- [Validating](#validating)

Tracing instrumentation is included in the ROS 2 source code, and Linux installations of ROS 2 include the LTTng tracer as a dependency.
Therefore, ROS 2 can be traced out-of-the-box on Linux.

However, ROS 2 can be built from source to remove the tracepoints or completely remove the instrumentation.
This guide shows how to do that.
For more information, see [the repository](https://github.com/ros2/ros2_tracing).

> [!NOTE]
>
> This guide only applies to Linux systems.

<a id="prerequisites"></a>

## Prerequisites

Set up your system to build ROS 2 from source.
See [the source installation page](../installation/alternatives/ubuntu-development-setup.md) for more information.

<a id="build-configurations"></a>

## Build configurations

The ROS 2 tracing instrumentation is split into two components: function instrumentation and tracepoints.
First, a ROS 2 core package (e.g., `rclcpp`) calls a function provided by the `tracetools` package.
Then, that function triggers a tracepoint, which records data if the tracepoint is enabled at runtime.

By default, if the tracer is not [configured to trace or if the tracepoints are not enabled](https://github.com/ros2/ros2_tracing#tracing), they will have virtually no impact on the execution.
However, the tracepoints can still be removed through a CMake option.
Furthermore, the functions can be completely removed through a CMake option, which implies that tracepoints are also removed.

<a id="building-without-tracepoints"></a>

### Building without tracepoints

This step depends on whether you are [building ROS 2 from source](../installation/alternatives/ubuntu-development-setup.md) or using ROS 2 binaries ([deb packages](../installation/ubuntu-install-debs.md) or [binary archive](../installation/alternatives/ubuntu-install-binary.md)).
To remove the tracepoints, (re)build `tracetools` and set the `TRACETOOLS_TRACEPOINTS_EXCLUDED` CMake option to `ON`:

Source installation

```
$ cd ~/ros2_jazzy
$ colcon build --packages-select tracetools --cmake-clean-cache --cmake-args -DTRACETOOLS_TRACEPOINTS_EXCLUDED=ON
```

Binary installation

Clone the `ros2_tracing` repository into your workspace and build:

```
$ cd ~/ws
$ git clone https://github.com/ros2/ros2_tracing.git -b jazzy src/ros2_tracing
$ colcon build --packages-select tracetools --cmake-args -DTRACETOOLS_TRACEPOINTS_EXCLUDED=ON
```

<a id="building-without-instrumentation"></a>

### Building without instrumentation

To completely remove both tracepoints and function calls, [build ROS 2 from source](../installation/alternatives/ubuntu-development-setup.md) and set the `TRACETOOLS_DISABLED` CMake option to `ON`:

```
$ cd ~/ros2_jazzy
$ colcon build --cmake-args -DTRACETOOLS_DISABLED=ON --no-warn-unused-cli
```

<a id="validating"></a>

## Validating

Validate that tracing is disabled:

```
$ cd ~/ws
$ source install/setup.bash
$ ros2 run tracetools status
```

It should print out:

Without tracepoints

```
Tracing disabled
```

Without instrumentation

```
Tracing disabled through configuration
```

If something else is printed, then something went wrong.
