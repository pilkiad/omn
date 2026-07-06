---
title: "Cross-compilation"
docname: "How-To-Guides/Cross-compilation"
source: "How-To-Guides/Cross-compilation.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="cross-compilation"></a>

# Cross-compilation

The [cross\_compile](https://github.com/ros-tooling/cross_compile) tool is not supported anymore.

An alternative to cross-compilation is to [build multi-platform Docker images](https://github.com/docker/buildx#building-multi-platform-images) using `docker buildx`.
