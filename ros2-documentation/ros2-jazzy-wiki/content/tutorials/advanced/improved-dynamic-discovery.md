---
title: "Improved Dynamic Discovery"
docname: "Tutorials/Advanced/Improved-Dynamic-Discovery"
source: "Tutorials/Advanced/Improved-Dynamic-Discovery.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="improved-dynamic-discovery"></a>
<a id="improveddynamicdiscovery"></a>

# Improved Dynamic Discovery

**Goal:** This tutorial will show how to use the improved dynamic discovery configuration.

**Tutorial level:** Advanced

**Time:** 15 minutes

Table of Contents

- [Overview](#overview)
- [Configuration Parameters](#configuration-parameters)
- [Examples](#examples)

<a id="overview"></a>

## Overview

By default, ROS 2 will attempt to find all nodes on all hosts on the same subnet automatically.
However, the following options are available to control the ROS 2 discovery range.

> [!WARNING]
>
> These environment variables (`ROS_AUTOMATIC_DISCOVERY_RANGE` and `ROS_STATIC_PEERS`) are **not supported** by `rmw_zenoh`.
> If you are using `rmw_zenoh` as your RMW implementation, please refer to the [rmw\_zenoh configuration documentation](https://github.com/ros2/rmw_zenoh?tab=readme-ov-file#configuration) for instructions on how to configure discovery and communication behavior.

<a id="configuration-parameters"></a>

## Configuration Parameters

- `ROS_AUTOMATIC_DISCOVERY_RANGE`: controls how far ROS nodes will try to discover each other.

  > Valid options are:
  >
  > - `SUBNET` is the default, and for DDS based middleware it means it will discover any node reachable via multicast.
  > - `LOCALHOST` means a node will only try to discover other nodes on the same machine.
  > - `OFF` means the node won’t discover any other nodes, even on the same machine.
  > - `SYSTEM_DEFAULT` means “don’t change any discovery settings”.
- `ROS_STATIC_PEERS`: is a semicolon (`;`) separated list of addresses that ROS should try to discover nodes on.
  This allows connecting to nodes on specific machines (as long as their discovery range is not set to `OFF`).

The combination of these two environment variables for local and remote nodes will enable and control the ROS 2 communication discovery range.
The following tables highlight the discovery range behavior for possible combination.

A `X` indicates that nodes A and B will not discover each other and communicate.
A `O` indicates that nodes A and B will discover each other and communicate.

Node A and B running in the same host

| Same host |  |  | Node B setting |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | No static peer |  |  | With static peer |  |  |
|  |  |  | Off | Localhost | Subnet | Off | Localhost | Subnet |
| Node A setting | No static peer | Off | `X` | `X` | `X` | `X` | `X` | `X` |
|  |  | Localhost | `X` | `O` | `O` | `X` | `O` | `O` |
|  |  | Subnet | `X` | `O` | `O` | `X` | `O` | `O` |
|  | With static peer | Off | `X` | `X` | `X` | `X` | `X` | `X` |
|  |  | Localhost | `X` | `O` | `O` | `X` | `O` | `O` |
|  |  | Subnet | `X` | `O` | `O` | `X` | `O` | `O` |

Node A and B running in the different hosts

| Different hosts |  |  | Node B setting |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | No static peer |  |  | With static peer |  |  |
|  |  |  | Off | Localhost | Subnet | Off | Localhost | Subnet |
| Node A setting | No static peer | Off | `X` | `X` | `X` | `X` | `X` | `X` |
|  |  | Localhost | `X` | `X` | `X` | `X` | `O` | `O` |
|  |  | Subnet | `X` | `X` | `O` | `X` | `O` | `O` |
|  | With static peer | Off | `X` | `X` | `X` | `X` | `X` | `X` |
|  |  | Localhost | `X` | `O` | `O` | `X` | `O` | `O` |
|  |  | Subnet | `X` | `O` | `O` | `X` | `O` | `O` |

<a id="examples"></a>

## Examples

For example, the following commands will limit the ROS 2 communication only with localhost and specific peers:

Linux

```
$ export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
$ export ROS_STATIC_PEERS='192.168.0.1;remote.com'
```

To maintain this setting between shell sessions, you can add the command to your shell startup script:

```
$ echo "export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST" >> ~/.bashrc
$ echo "export ROS_STATIC_PEERS='192.168.0.1;remote.com'" >> ~/.bashrc
```

macOS

```
$ export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
$ export ROS_STATIC_PEERS='192.168.0.1;remote.com'
```

To maintain this setting between shell sessions, you can add the command to your shell startup script:

```
$ echo "export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST" >> ~/.bash_profile
$ echo "export ROS_STATIC_PEERS='192.168.0.1;remote.com'" >> ~/.bash_profile
```

Windows

```
$ set ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
$ set ROS_STATIC_PEERS=192.168.0.1;remote.com
```

If you want to make this permanent between shell sessions, also run:

```
$ setx ROS_AUTOMATIC_DISCOVERY_RANGE LOCALHOST
$ setx ROS_STATIC_PEERS 192.168.0.1;remote.com
```
