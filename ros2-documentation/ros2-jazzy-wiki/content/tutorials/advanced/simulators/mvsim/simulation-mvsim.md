---
title: "MVSim"
docname: "Tutorials/Advanced/Simulators/MVSim/Simulation-MVSim"
source: "Tutorials/Advanced/Simulators/MVSim/Simulation-MVSim.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../../index.md) | [Summary](../../../../../SUMMARY.md) | [Tutorials hub](../../../../../wiki/tutorial-paths.md)
> Related: [Building a Custom RViz Display](../../../intermediate/rviz/rviz-custom-display.md) | [Building a Custom RViz Panel](../../../intermediate/rviz/rviz-custom-panel.md) | [Defining worlds, robots, and sensors](defining-worlds-mvsim.md) | [Gazebo](../gazebo/simulation-gazebo.md) | [Getting started with MVSim](getting-started-mvsim.md)

<a id="mvsim"></a>

# MVSim

This set of tutorials will teach you how to configure the [MVSim](https://mvsimulator.readthedocs.io/) simulator with ROS 2.

MVSim is a lightweight, open-source, multi-vehicle simulator focused on 2D+3D visualization of mobile robots.
It uses Box2D for 2D rigid body physics and provides realistic vehicle dynamics models (differential drive, Ackermann steering),
sensor simulation (2D/3D LiDARs, cameras, IMUs, GPS), and native ROS 2 integration.
MVSim is particularly well-suited for testing navigation, SLAM, and multi-robot coordination scenarios
with low computational overhead and fast iteration times.

- [Installation (Ubuntu)](installation-ubuntu.md)
- [Getting started with MVSim](getting-started-mvsim.md)
- [Defining worlds, robots, and sensors](defining-worlds-mvsim.md)
