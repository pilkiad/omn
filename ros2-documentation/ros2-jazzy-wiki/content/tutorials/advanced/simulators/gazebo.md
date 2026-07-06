---
title: "Setting up a robot simulation (Gazebo)"
docname: "Tutorials/Advanced/Simulators/Gazebo/Gazebo"
source: "Tutorials/Advanced/Simulators/Gazebo/Gazebo.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Building a Custom RViz Display](../../intermediate/rviz/rviz-custom-display.md) | [Building a Custom RViz Panel](../../intermediate/rviz/rviz-custom-panel.md) | [Defining worlds, robots, and sensors](mvsim/defining-worlds-mvsim.md) | [Gazebo](gazebo/simulation-gazebo.md) | [Getting started with MVSim](mvsim/getting-started-mvsim.md)

<a id="setting-up-a-robot-simulation-gazebo"></a>

# Setting up a robot simulation (Gazebo)

**Goal:** Launch a Simulation with Gazebo and ROS 2

**Tutorial level:** Advanced

**Time:** 5 minutes

Contents

- [Prerequisites](#prerequisites)

  - [ROS 2](#ros-2)
  - [Gazebo](#gazebo)
- [Quick Check](#quick-check)
- [Further Resources](#further-resources)
- [Summary](#summary)
> [!NOTE]
>
> These instructions are about the current [Gazebo](https://gazebosim.org/) (previously known as Ignition), not [Gazebo Classic](https://classic.gazebosim.org/).

<a id="prerequisites"></a>

## Prerequisites

You’ll need to install both ROS 2 and Gazebo.

<a id="ros-2"></a>

### ROS 2

For ROS 2 you should follow the [ROS 2 install instructions](../../../installation/overview.md).

<a id="gazebo"></a>

### Gazebo

Gazebo and ROS support different combinations of versions.

All supported combinations can be seen [here](https://gazebosim.org/docs/harmonic/ros_installation#summary-of-compatible-ros-and-gazebo-combinations).

[ROS REP-2000](https://reps.openrobotics.org/rep-2000/) standardizes what the default version of Gazebo is for each ROS distribution.

If you haven’t installed a version of Gazebo on your system yet, you can install Gazebo by following the [installation instructions](https://gazebosim.org/docs/harmonic/ros_installation).

<a id="quick-check"></a>

## Quick Check

To verify your Gazebo installation is correct, check you can run it:

```
$ gz sim
```

<a id="further-resources"></a>

## Further Resources

Once Gazebo is installed and is all clear on the last quick test, you can move to the [Gazebo tutorials](https://gazebosim.org/docs/harmonic/tutorials) to try out building your own robot!

If you use a different version of Gazebo than the recommended version, make sure to use the dropdown to select the correct version of documentation.

<a id="summary"></a>

## Summary

In this tutorial, you have installed Gazebo and set-up your workspace to start with the [Gazebo tutorials](https://gazebosim.org/docs/harmonic/tutorials).
