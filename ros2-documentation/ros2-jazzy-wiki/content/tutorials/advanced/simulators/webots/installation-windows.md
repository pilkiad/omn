---
title: "Installation (Windows)"
docname: "Tutorials/Advanced/Simulators/Webots/Installation-Windows"
source: "Tutorials/Advanced/Simulators/Webots/Installation-Windows.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../../index.md) | [Summary](../../../../../SUMMARY.md) | [Tutorials hub](../../../../../wiki/tutorial-paths.md)
> Related: [Building a Custom RViz Display](../../../intermediate/rviz/rviz-custom-display.md) | [Building a Custom RViz Panel](../../../intermediate/rviz/rviz-custom-panel.md) | [Defining worlds, robots, and sensors](../mvsim/defining-worlds-mvsim.md) | [Gazebo](../gazebo/simulation-gazebo.md) | [Getting started with MVSim](../mvsim/getting-started-mvsim.md)

<a id="installation-windows"></a>

# Installation (Windows)

**Goal:** Install the `webots_ros2` package and run simulation examples on Windows.

**Tutorial level:** Advanced

**Time:** 10 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)

  - [Multiple Installations of Webots](#multiple-installations-of-webots)
- [Tasks](#tasks)

  - [1 Install WSL2](#install-wsl2)
  - [2 Install ROS 2 in WSL](#install-ros-2-in-wsl)
  - [3 Install `webots_ros2`](#install-webots-ros2)
  - [4 Launch the `webots_ros2_universal_robot` example](#launch-the-webots-ros2-universal-robot-example)
  - [5 RViz troubleshooting](#rviz-troubleshooting)

<a id="background"></a>

## Background

The `webots_ros2` package provides an interface between ROS 2 and Webots.
It includes several sub-packages, including `webots_ros2_driver`, which allows ROS nodes to communicate with Webots.
Other sub-packages are mainly examples that show multiple possible implementations using the interface.
In this tutorial, you are going to install the package and learn how to run one of these examples.

<a id="prerequisites"></a>

## Prerequisites

It is recommended to understand basic ROS principles covered in the beginner [Tutorials](../../../overview.md).
In particular, [Creating a workspace](../../../beginner-client-libraries/creating-a-workspace.md) and [Creating a package](../../../beginner-client-libraries/creating-your-first-ros2-package.md) are useful prerequisites.

Webots is a prerequisite to use the `webots_ros2` package.
You can follow the [installation procedure](https://cyberbotics.com/doc/guide/installation-procedure) or [build it from sources](https://github.com/cyberbotics/webots/wiki/Windows-installation/).

Alternatively, you can also let `webots_ros2` download Webots automatically.
This option appears when you launch an example of the package and no Webots installation is found.

<a id="multiple-installations-of-webots"></a>

### Multiple Installations of Webots

If you have more than one installation of Webots, ROS 2 will look for Webots at the following locations (in this order):

1. If the `ROS2_WEBOTS_HOME` environment variable is set, ROS 2 will use the Webots in this folder, regardless of its version.
2. If the `WEBOTS_HOME` environment variable is set, ROS 2 will use the Webots in this folder, regardless of its version.
3. If none of the previous points is set/installed ROS 2 will look for Webots in the default installation paths for a compatible version: `C:\Program Files\Webots`.
4. If Webots couldn’t be found, `webots_ros2` will show a window and offer automatic Webots installation of the last compatible version.

<a id="tasks"></a>

## Tasks

<a id="install-wsl2"></a>

### 1 Install WSL2

On Windows, WSL (Windows Subsystem for Linux) improves the user experience with ROS 2 compared to native Windows installation, as it runs on a Linux platform.
Install WSL with an Ubuntu version which is compatible with your ROS distribution and upgrade to WSL2 following the [official Microsoft tutorial](https://learn.microsoft.com/en-us/windows/wsl/install).

<a id="install-ros-2-in-wsl"></a>

### 2 Install ROS 2 in WSL

Install ROS 2 inside Ubuntu WSL, following [Ubuntu (deb packages)](../../../../installation/ubuntu-install-debs.md).

<a id="install-webots-ros2"></a>

### 3 Install `webots_ros2`

You can then either install `webots_ros2` from the official released package, or install it from the latest up-to-date sources from [Github](https://github.com/cyberbotics/webots_ros2).

The following commands must be run inside the WSL environment.

Install `webots_ros2` distributed package

Run the following command in a terminal.

```
$ sudo apt-get install ros-jazzy-webots-ros2
```

Install `webots_ros2` from sources

Create a ROS 2 workspace with its `src` directory.

```
$ mkdir -p ~/ros2_ws/src
```

Source the ROS 2 environment.

```
$ source /opt/ros/jazzy/setup.bash
```

Retrieve the sources from Github.

```
$ cd ~/ros2_ws
$ git clone --recurse-submodules https://github.com/cyberbotics/webots_ros2.git src/webots_ros2
```

Install the package dependencies.

```
$ sudo apt install python3-pip python3-rosdep python3-colcon-common-extensions
$ sudo rosdep init && rosdep update
$ rosdep install --from-paths src --ignore-src --rosdistro jazzy
```

Build the package using `colcon`.

```
$ colcon build
```

Source this workspace.

```
$ source install/local_setup.bash
```

<a id="launch-the-webots-ros2-universal-robot-example"></a>

### 4 Launch the `webots_ros2_universal_robot` example

WSL doesn’t support hardware acceleration (yet).
Therefore, Webots should be started on Windows, while the ROS part is running inside WSL.
To do so, the following commands must be run inside the WSL environment.

First source the ROS 2 environment, if not done already.

```
$ source /opt/ros/jazzy/setup.bash
```

Setting the `WEBOTS_HOME` environment variable allows you to start a specific Webots installation (e.g. `C:\Program Files\Webots`).
Use the mount point “/mnt” to refer to a path on native Windows.

```
$ export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
```

If installed from sources, source your ROS 2 workspace, if not done already.

```
$ cd ~/ros2_ws
$ source install/local_setup.bash
```

Use the ROS 2 launch command to start demo packages (e.g. `webots_ros2_universal_robot`).

```
$ ros2 launch webots_ros2_universal_robot multirobot_launch.py
```

<a id="rviz-troubleshooting"></a>

### 5 RViz troubleshooting

With recent versions of WSL2, RViz should work out of the box.

You can check if it works correctly by running any example that uses RViz, for example:

```
$ sudo apt install ros-jazzy-slam-toolbox
$ ros2 launch webots_ros2_tiago robot_launch.py rviz:=true slam:=true
```

The Tiago robot can be controlled using:

```
$ ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

With older WSL versions, RViz2 may not work directly, as no display is available.
To use RViz, you can either upgrade WSL or enable X11 forwarding.

Upgrade WSL

In a Windows shell:

```
$ wsl --update
```

Enable X11 forwarding

For older versions of WSL, the following steps can be followed:

1. Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/).
2. Launch VcXsrv.
   You can leave most of the parameters default, except the `Extra settings` page, where you must set `Clipboard`, `Primary Selection` and `Disable access control` and unset `Native opengl`.
3. You can save the configuration for future launches.
4. Click on `Finish`, you will see that the X11 server is running in the icon tray.
5. In your WSL environment, export the `DISPLAY` variable.

   > ```
   > $ export DISPLAY=$(ip route list default | awk '{print }'):0
   > ```
   >
   > You can add this to your `.bashrc`, so that it is set for every future WSL environment.
   >
   > ```
   > $ echo "export DISPLAY=$(ip route list default | awk '{print }'):0" >> ~/.bashrc
   > ```
