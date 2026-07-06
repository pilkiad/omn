---
title: "Managing node lifecycles - example"
docname: "Tutorials/Demos/Managed-Nodes"
source: "Tutorials/Demos/Managed-Nodes.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](service-introspection.md)

<a id="managing-node-lifecycles-example"></a>

# Managing node lifecycles - example

Managed lifecycles for nodes allow greater control over the state of the ROS system.
This example uses a simple talker/listener pair of managed nodes to show how a managed lifecycle can be implemented and used.
You can use the example to understand and experiment with managing nodes in this way.

**Area: ROS-framework | Content-type: example | Experience: expert**

Contents

- [Summary](#summary)
- [Prerequisites](#prerequisites)
- [Example](#example)

  - [Access the example](#access-the-example)
  - [Commentary](#commentary)
- [Related content](#related-content)

<a id="summary"></a>

## Summary

ROS 2 introduces the concept of managed nodes, also called lifecycle nodes.
These nodes can be used to ensure that resources are correctly initialised, activated, deactivated, and cleaned up as the node moves between lifecycle states.
A common use case is nodes that control hardware, where devices such as cameras, lidars, motor drivers, and other sensors and actuators must be started, configured, and shut down in a controlled order.

Using lifecycle nodes helps ensure hardware is only initialised when it is ready, and is safely released during shutdown or error recovery.
The following packages enable you to implement these managed nodes: [rclcpp\_lifecycle](https://index.ros.org/p/rclcpp_lifecycle/) (implementation library) and [lifecycle\_msgs](https://index.ros.org/p/lifecycle_msgs/) (interface definitions).

<a id="prerequisites"></a>

## Prerequisites

See the [installation instructions](../../installation/overview.md) for details on installing ROS 2.

<a id="example"></a>

## Example

<a id="access-the-example"></a>

### Access the example

Information on how to run the example is here: [lifecycle\_demo\_launch.py](https://github.com/ros2/demos/blob/jazzy/lifecycle_py/launch/lifecycle_demo_launch.py)

<a id="commentary"></a>

### Commentary

For more information about how to run it and what’s happening, see: [lifecycle README](https://github.com/ros2/demos/blob/jazzy/lifecycle/README.rst)

<a id="related-content"></a>

## Related content

Packages/reference:

- [rclcpp\_lifecycle](https://index.ros.org/p/rclcpp_lifecycle/) (implementation library): Package containing a prototype for lifecycle implementation.
- [lifecycle\_msgs](https://index.ros.org/p/lifecycle_msgs/) (interface definitions): Package containing some lifecycle related message and service definitions.
- [lifecycle](https://docs.ros.org/en/jazzy/p/lifecycle/): Package containing demos for lifecycle implementation.
