---
title: "Installation (Ubuntu)"
docname: "Tutorials/Advanced/Simulators/MVSim/Installation-Ubuntu"
source: "Tutorials/Advanced/Simulators/MVSim/Installation-Ubuntu.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../../index.md) | [Summary](../../../../../SUMMARY.md) | [Tutorials hub](../../../../../wiki/tutorial-paths.md)
> Related: [Building a Custom RViz Display](../../../intermediate/rviz/rviz-custom-display.md) | [Building a Custom RViz Panel](../../../intermediate/rviz/rviz-custom-panel.md) | [Defining worlds, robots, and sensors](defining-worlds-mvsim.md) | [Gazebo](../gazebo/simulation-gazebo.md) | [Getting started with MVSim](getting-started-mvsim.md)

<a id="installation-ubuntu"></a>

# Installation (Ubuntu)

**Goal:** Install the `mvsim` package on Ubuntu and verify it works.

**Tutorial level:** Advanced

**Time:** 10 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Install `mvsim`](#install-mvsim)
  - [2 Verify the installation](#verify-the-installation)
  - [3 Launch a demo](#launch-a-demo)
- [Summary](#summary)

<a id="background"></a>

## Background

[MVSim](https://mvsimulator.readthedocs.io/) (MultiVehicle Simulator) is a lightweight, open-source simulator for mobile robots.
It provides 2D physics-based simulation with 3D visualization, supporting differential drive and Ackermann vehicles,
multiple sensor types (LiDAR, cameras, IMU, GPS), and native ROS 2 integration via standard message types.

MVSim is licensed under the BSD 3-clause license.

<a id="prerequisites"></a>

## Prerequisites

It is recommended to understand basic ROS principles covered in the beginner [Tutorials](../../../overview.md).
In particular, [Creating a workspace](../../../beginner-client-libraries/creating-a-workspace.md) is a useful prerequisite.

You should have a working ROS 2 installation.
Follow the [ROS 2 install instructions](../../../../installation/overview.md) if needed.

<a id="tasks"></a>

## Tasks

<a id="install-mvsim"></a>

### 1 Install `mvsim`

You can either install the released binary package or build from sources.

Install from ROS binary packages

Run the following command in a terminal:

```
$ sudo apt install ros-jazzy-mvsim
```

Build from sources

Create a ROS 2 workspace if you don’t already have one:

```
$ mkdir -p ~/ros2_ws/src
```

Source the ROS 2 environment:

```
$ source /opt/ros/jazzy/setup.bash
```

Clone the MVSim repository:

```
$ cd ~/ros2_ws/src
$ git clone https://github.com/MRPT/mvsim.git --recursive
```

Install dependencies using `rosdep`:

```
$ cd ~/ros2_ws
$ rosdep install --from-paths src --ignore-src -r -y
```

Build the package:

```
$ colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
```

Source the workspace:

```
$ source install/setup.bash
```

<a id="verify-the-installation"></a>

### 2 Verify the installation

Check that the `mvsim` CLI is available:

```
$ mvsim --version
```

You should see the installed version number printed to the terminal.

> [!WARNING]
>
> The `mvsim` package provides two executables:
>
> - `mvsim`: the main CLI tool for running the simulator standalone
> - `mvsim_node`: a ROS 2 node wrapper for running the simulator and connect it to other ROS 2 nodes

<a id="launch-a-demo"></a>

### 3 Launch a demo

To quickly verify everything is working, launch the warehouse demo with ROS 2:

```
$ ros2 launch mvsim demo_warehouse.launch.py
```

You should see the MVSim GUI window open with a Jackal robot in a warehouse environment.
Use the keyboard (W/A/S/D keys) to drive the robot.

<a id="summary"></a>

## Summary

You have installed MVSim and verified it works by launching a demo world.
In the next tutorial, you will learn how to launch different demo scenarios and interact with them through ROS 2 topics.
