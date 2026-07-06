---
title: "Launch"
docname: "Tutorials/Intermediate/Launch/Launch-Main"
source: "Tutorials/Intermediate/Launch/Launch-Main.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="launch"></a>
<a id="launchfilesmain"></a>

# Launch

ROS 2 Launch files allow you to start up and configure a number of executables containing ROS 2 nodes simultaneously.

1. [Creating a launch file](creating-launch-files.md).

   Learn how to create a launch file that will start up nodes and their configurations all at once.
2. [Launching and monitoring multiple nodes](launch-system.md).

   Get a more advanced overview of how launch files work.
3. [Using substitutions](using-substitutions.md).

   Use substitutions to provide more flexibility when describing reusable launch files.
4. [Using event handlers](using-event-handlers.md).

   Use event handlers to monitor the state of processes or to define a complex set of rules that can be used to dynamically modify the launch file.
5. [Managing large projects](using-ros2-launch-for-large-projects.md).

   Structure launch files for large projects so they may be reused as much as possible in different situations.
   See usage examples of different launch tools like parameters, YAML files, remappings, namespaces, default arguments, and RViz configs.

> [!NOTE]
>
> If you are coming from ROS 1, you can use the [ROS Launch Migration guide](../../../how-to/migrating-from-ros1/migrating-launch-files.md) to help you migrate your launch files to ROS 2.
