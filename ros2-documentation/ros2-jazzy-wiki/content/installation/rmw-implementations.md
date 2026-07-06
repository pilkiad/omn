---
title: "RMW implementations"
docname: "Installation/RMW-Implementations"
source: "Installation/RMW-Implementations.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Installation hub](../../wiki/task-map.md)
> Related: [Alternatives](alternatives.md) | [Maintain source checkout](maintaining-a-source-checkout.md) | [Mirrors](ros-2-mirrors.md) | [RHEL (RPM packages)](rhel-install-rpms.md) | [Testing with pre-release binaries](testing.md)

<a id="rmw-implementations"></a>

# RMW implementations

By default, ROS 2 uses DDS as its [middleware](https://design.ros2.org/articles/ros_on_dds.html).
It is compatible with multiple DDS or RTPS (the DDS wire protocol) vendors.
There is currently support for eProsima’s Fast DDS, RTI’s Connext DDS, Eclipse Cyclone DDS, and GurumNetworks GurumDDS.

It also supports non DDS RMW implementations such as Zenoh.

See [REP-2000](https://reps.openrobotics.org/rep-2000/) for supported RMW vendors by distribution.

The default RMW vendor is eProsima’s Fast DDS.

Review all the possible options:

- [DDS implementations](rmw-implementations/dds-implementations.md) explains how to use DDS.
- [Non DDS implementations](rmw-implementations/non-dds-implementations.md) explains how to use non DDS implementations.
