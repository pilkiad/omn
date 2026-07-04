---
title: "Zenoh"
docname: "Installation/RMW-Implementations/Non-DDS-Implementations/Working-with-Zenoh"
source: "Installation/RMW-Implementations/Non-DDS-Implementations/Working-with-Zenoh.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Installation hub](../../../../wiki/task-map.md)
> Related: [Eclipse Cyclone DDS](../dds-implementations/working-with-eclipse-cyclone-dds.md) | [eProsima Fast DDS](../dds-implementations/working-with-e-prosima-fast-dds.md) | [GurumNetworks GurumDDS](../dds-implementations/working-with-gurum-networks-gurum-dds.md) | [RTI Connext DDS](../dds-implementations/working-with-rti-connext-dds.md)

<a id="zenoh"></a>

# Zenoh

Zenoh is an open source communication protocol and middleware designed to facilitate efficient data distribution across heterogeneous systems.
It provides location-transparent abstractions for high performance pub/sub and distributed queries.
See also: <https://zenoh.io/docs/getting-started/first-app/>

<a id="prerequisites"></a>

## Prerequisites

Have [rosdep installed](../../../tutorials/intermediate/rosdep.md).

<a id="installation-packages"></a>

## Installation packages

The rmw implementation Zenoh can be installed via binaries, recommended for stable development.

Binary packages for supported ROS 2 distributions (see distro branches) are available on respective Tier-1 platforms for the distributions.
First ensure that your system is set up to install ROS 2 binaries by following the instructions here.

Then install rmw\_zenoh binaries using the command

```
sudo apt install ros-jazzy-rmw-zenoh-cpp
```

<a id="build-from-source-code"></a>

## Build from source code

Building from source is only recommended if latest features are needed.

By default, we vendor and compile `zenoh-cpp` with a subset of zenoh features.
The `ZENOHC_CARGO_FLAGS` CMake argument may be overwritten with other features included if required.
See [zenoh\_cpp\_vendor/CMakeLists.txt](https://github.com/ros2/rmw_zenoh/blob/jazzy/zenoh_cpp_vendor/CMakeLists.txt) for more details.

1. Clone the repository

```
mkdir ~/ws_rmw_zenoh/src -p && cd ~/ws_rmw_zenoh/src
git clone https://github.com/ros2/rmw_zenoh.git -b jazzy
```

1. Install dependencies:

```
cd ~/ws_rmw_zenoh
rosdep install --from-paths src --ignore-src --rosdistro jazzy -y
```

3. Build the workspace using Colcon:

```
source /opt/ros/jazzy/setup.bash
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
```

<a id="switch-to-rmw-zenoh-cpp"></a>

## Switch to rmw\_zenoh\_cpp

Switch from other rmw to rmw\_zenoh\_cpp by specifying the environment variable.

```
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
```

<a id="run-the-talker-and-listener"></a>

## Run the talker and listener

Now run `talker` and `listener` to test Zenoh.

Start the Zenoh router

```
# terminal 1
source /opt/ros/jazzy/setup.bash
ros2 run rmw_zenoh_cpp rmw_zenohd
```

> [!NOTE]
>
> Without the Zenoh router, nodes will not be able to discover each other since multicast discovery is disabled by default in the node’s session config.
> Instead, nodes will receive discovery information about other peers via the Zenoh router’s gossip functionality.

```
# terminal 2
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```

```
# terminal 3
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp listener
```

> [!NOTE]
>
> Remember to source your ROS 2 setup script before running these commands.
