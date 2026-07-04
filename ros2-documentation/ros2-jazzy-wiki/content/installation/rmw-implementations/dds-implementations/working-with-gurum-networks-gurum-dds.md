---
title: "GurumNetworks GurumDDS"
docname: "Installation/RMW-Implementations/DDS-Implementations/Working-with-GurumNetworks-GurumDDS"
source: "Installation/RMW-Implementations/DDS-Implementations/Working-with-GurumNetworks-GurumDDS.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Installation hub](../../../../wiki/task-map.md)
> Related: [Eclipse Cyclone DDS](working-with-eclipse-cyclone-dds.md) | [eProsima Fast DDS](working-with-e-prosima-fast-dds.md) | [RTI Connext DDS](working-with-rti-connext-dds.md) | [Zenoh](../non-dds-implementations/working-with-zenoh.md)

<a id="gurumnetworks-gurumdds"></a>

# GurumNetworks GurumDDS

`rmw_gurumdds` is an implementation of the ROS middleware interface using GurumNetworks GurumDDS.
For more information about GurumDDS, visit the [GurumNetworks website](https://gurum.cc/index_eng).

<a id="prerequisites"></a>

## Prerequisites

This guide assumes you have completed the ROS 2 environment setup process, either by [Installing ROS 2 via Deb Packages](../../ubuntu-install-debs.md) or [Building ROS 2 from source on Ubuntu](../../alternatives/ubuntu-development-setup.md).

Version Requirements ([see the README for details](https://github.com/ros2/rmw_gurumdds)):

| ROS 2 Distro | GurumDDS Version |
| --- | --- |
| rolling | `>= 3.2.0` |
| lyrical | `>= 3.2.0` |
| kilted | `>= 3.2.0` |
| jazzy | `>= 3.2.0` |
| humble | `3.1.x` |

Deb packages of GurumDDS are provided in the ROS 2 apt repositories on Ubuntu.
Windows binary installer of GurumDDS will be available soon.

You can obtain a free trial license from the [GurumDDS Free Trial page](https://gurum.cc/free_trial_eng.html).

After acquiring a license, place it in the following location: `/etc/gurumnet`

<a id="installation"></a>

## Installation

<a id="option-1-install-from-the-ros-2-apt-repository-recommended"></a>

### Option 1: Install from the ROS 2 apt repository (Recommended)

```
$ sudo apt install ros-jazzy-rmw-gurumdds-cpp
```

This installs both `rmw_gurumdds_cpp` and `gurumdds`.

<a id="option-2-build-from-source-code"></a>

### Option 2: Build from source code

1. Clone the repository

```
$ cd ros2_ws/src
$ git clone https://github.com/ros2/rmw_gurumdds -b jazzy ros2/rmw_gurumdds
```

2. Install dependencies:

```
$ cd ..
$ rosdep install --from src -i --rosdistro jazzy
```

3. Build the workspace using Colcon:

```
$ colcon build --symlink-install
```

<a id="switch-to-rmw-gurumdds"></a>

## Switch to rmw\_gurumdds

Switch from other RMW implementations to rmw\_gurumdds by setting the environment variable:

```
$ export RMW_IMPLEMENTATION=rmw_gurumdds_cpp
```

For more information on working with multiple RMW implementations, see [Working with multiple RMW implementations](../../../how-to/working-with-multiple-rmw-implementations.md).

<a id="testing-the-installation"></a>

## Testing the installation

Run the `talker` and `listener` nodes to verify your installation:

```
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp talker
```

```
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp listener
```

If the nodes communicate successfully, your installation is working correctly.

> [!NOTE]
>
> Remember to source your ROS 2 setup script before running these commands.
