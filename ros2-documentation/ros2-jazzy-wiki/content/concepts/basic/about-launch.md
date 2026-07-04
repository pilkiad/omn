---
title: "Launch"
docname: "Concepts/Basic/About-Launch"
source: "Concepts/Basic/About-Launch.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](about-actions.md) | [Client libraries](about-client-libraries.md) | [Composition](../intermediate/about-composition.md) | [Cross-compilation](../intermediate/about-cross-compilation.md) | [Different ROS 2 middleware vendors](../intermediate/about-different-middleware-vendors.md)

<a id="launch"></a>

# Launch

A ROS 2 system typically consists of many nodes running across many different processes (and even different machines).
While it is possible to manually start each of these nodes, it gets cumbersome quite quickly.

The launch system in ROS 2 is meant to automate the running of many nodes with a single command.
It helps the user describe the configuration of their system and then executes it as described.
The configuration of the system includes what programs to run, where to run them, what arguments to pass them, and ROS-specific conventions which make it easy to reuse components throughout the system by giving them each a different configuration.
It is also responsible for monitoring the state of the processes launched, and reporting and/or reacting to changes in the state of those processes.

All of the above is specified in a “launch file”, which can be written in XML, YAML, or Python.
This launch file can then be run using the `ros2 launch` command, and all of the nodes specified will be run.

To get started writing and using launch files, see [the launch tutorials](../../tutorials/intermediate/launch/launch-main.md).

For more detailed information, see [the launch documentation](https://docs.ros.org/en/jazzy/p/launch).
