---
title: "Non-DDS-Implementations"
docname: "Installation/RMW-Implementations/Non-DDS-Implementations"
source: "Installation/RMW-Implementations/Non-DDS-Implementations.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Installation hub](../../../wiki/task-map.md)
> Related: [DDS implementations](dds-implementations.md) | [Latest development (source)](../alternatives/latest-development-setup.md) | [macOS (source)](../alternatives/mac-os-development-setup.md) | [RHEL (binary)](../alternatives/rhel-install-binary.md) | [RHEL (source)](../alternatives/rhel-development-setup.md)

<a id="non-dds-implementations"></a>

# Non-DDS-Implementations

- [Working with Zenoh](non-dds-implementations/working-with-zenoh.md) explains how to utilize Zenoh.

If you would like to use one of the other vendors you will need to install their software separately before building.
The ROS 2 build will automatically build support for vendors that have been installed and sourced correctly.

Once you’ve installed a new RMW vendor, you can change the vendor used at runtime: [Working with Multiple RMW Implementations](../../how-to/working-with-multiple-rmw-implementations.md).
