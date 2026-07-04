---
title: "RTI Connext DDS"
docname: "Installation/RMW-Implementations/DDS-Implementations/Working-with-RTI-Connext-DDS"
source: "Installation/RMW-Implementations/DDS-Implementations/Working-with-RTI-Connext-DDS.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Installation hub](../../../../wiki/task-map.md)
> Related: [Eclipse Cyclone DDS](working-with-eclipse-cyclone-dds.md) | [eProsima Fast DDS](working-with-e-prosima-fast-dds.md) | [GurumNetworks GurumDDS](working-with-gurum-networks-gurum-dds.md) | [Zenoh](../non-dds-implementations/working-with-zenoh.md)

<a id="rti-connext-dds"></a>

# RTI Connext DDS

RTI Connext DDS is trusted in over 2000 of the world’s most demanding system designs, distributing critical real-time data with the highest levels of performance, reliability, and security.
It is free-of-charge for prototyping, research, non-commercial and academic use.
Visit the [RTI website](https://www.rti.com/ros) for more information and to learn about options for support and commercial licenses.

<a id="prerequisites"></a>

## Prerequisites

<a id="install-rti-connext-dds"></a>

### Install RTI Connext DDS

> To build and use `rmw_connextdds` requires a version of Connext DDS compatible with the distribution of ROS 2 in use.
> Connext DDS is included when installing `rmw_connextdds` using apt, or can be installed manually for building from source.
> The following table details which Connext DDS versions are installed using `apt`, and which versions are required for building from source:
>
> | ROS 2 Distribution | Installed using apt | To Build from Source |
> | --- | --- | --- |
> | rolling | n/a | `7.7.0` |
> | lyrical | `7.7.0` | `7.7.0` |
> | kilted | `7.3.0` | `7.3.0` |
> | jazzy | `6.0.1` | `6.0.1` |
> | humble | `6.0.1` | `6.0.1` |

RTI Connext Pro is available through a variety of channels:

**ROS 2 apt repositories**
:   ROS 2 users can install a non-commercial-use version of the RTI Connext DDS libraries for x86\_64 Linux from the ROS apt repository using the following command:

    v7.3.0

    ```
    $ sudo apt update && sudo apt install -q -y rti-connext-dds-7.3.0-ros
    ```

    v6.0.1

    ```
    $ sudo apt update && sudo apt install -q -y rti-connext-dds-6.0.1
    ```

    This package includes the RTI Connext core DDS libraries only; it does not include the full Connext Professional suite of tools and run-time services.
    Note that these Connext libraries are automatically installed when installing `rmw_connextdds` using apt.

**Other Installation Options**
<<<<<<< HEAD
RTI Connext DDS is a proprietary DDS implementation with a number of advanced features and commercial support options.
RTI provides both a [non-commercial / research license](https://www.rti.com/free-trial/university-program) for students and researchers and a [time-limited free trial license](https://www.rti.com/free-trial) for commercial users.
Detailed instructions for building and tuning the RMW and ROS 2 applications for a variety of platforms, and enabling DDS Security and safety-cert options are available on the [RTI ROS Community](https://community.rti.com/ros) pages.
=======
The [Connext Robotics Toolkit](https://www.rti.com/developers/connext-robotics-toolkit) includes the full suite of Connext tools and infrastructure services.
It provides a single step installation of ROS and Connext using apt.
It is free for prototype development, research, non-commercial and academic use.

Detailed instructions for building and tuning the RMW and ROS 2 applications for a variety of platforms, and enabling DDS Security are available on the [RTI ROS Community](https://community.rti.com/ros) pages.
>>>>>>> e3eca81 (Update Connext RMW documentation (#6441))

<a id="install-rmw-connextdds-binary-packages"></a>

## Install rmw\_connextdds binary packages

To install the binary packages for `rmw_connextdds` and the Connext libraries from the ROS 2 apt repositories, use the following command:

```
$ sudo apt update && sudo apt install -q -y ros-jazzy-rmw-connextdds
```

<a id="building-rmw-connextdds-from-source-code"></a>

## Building rmw\_connextdds from source code

Building from source code can ensure the RMW is matched to your system and installed correctly.
The following instructions assume a Linux x86\_64 build host and target; the [RTI ROS Community](https://community.rti.com/ros)
pages have instructions for building for other platforms and targets, including Arm, Windows, and macOS.

Clone the repository for `rmw_connextdds` into your ROS 2 workspace and select the branch that matches the ROS 2 distribution in use:

```
$ mkdir -p ros2_ws/src
$ cd ros2_ws
$ git clone -b jazzy https://github.com/ros2/rmw_connextdds src/rmw_connextdds
```

Set up the environment to help colcon discover where RTI Connext is installed.
This can be done by manually setting the environment variable `NDDSHOME` to the location of the RTI Connext installation, or by using a script that comes with the RTI Connext installation:

```
$ source ${RTI_CONNEXT_INSTALL_LOCATION}/resource/scripts/rtisetenv_x64Linux4gcc7.3.0.bash
```

Make sure you have the ROS 2 environment set up:

```
$ source /opt/ros/jazzy/setup.bash
```

Build the RMW using colcon:

```
$ colcon build --symlink-install
```

After the build completes successfully, be sure to source the setup file for the workspace:

```
$ source install/setup.bash
```

<a id="use-the-resulting-rmw-connextdds"></a>

## Use the resulting rmw\_connextdds

Set the environment variable `RMW_IMPLEMENTATION` to tell ROS 2 which RMW to use:

```
$ export RMW_IMPLEMENTATION=rmw_connextdds
```

See also: [Working with multiple RMW implementations](../../../how-to/working-with-multiple-rmw-implementations.md)

<a id="run-the-talker-and-listener"></a>

## Run the talker and listener

Now run `talker` and `listener` to test RTI Connext DDS

```
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp talker
```

```
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp listener
```
