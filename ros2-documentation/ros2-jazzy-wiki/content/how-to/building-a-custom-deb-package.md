---
title: "Building a custom deb package"
docname: "How-To-Guides/Building-a-Custom-Deb-Package"
source: "How-To-Guides/Building-a-Custom-Deb-Package.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md) | [Cross-compilation](cross-compilation.md)

<a id="building-a-custom-deb-package"></a>

# Building a custom deb package

Many Ubuntu users install ROS 2 on their system by installing [deb packages](../installation/ubuntu-install-debs.md).
This guide gives a short set of instructions to build local, custom deb packages.

Table of Contents

- [Prerequisites](#prerequisites)
- [Install dependencies](#install-dependencies)
- [Initialize rosdep](#initialize-rosdep)
- [Build the deb from the package](#build-the-deb-from-the-package)

<a id="prerequisites"></a>

## Prerequisites

To successfully build a custom package, all of the dependencies of the package to be built must be available locally or in rosdep.
Additionally, all of the dependencies of the package should be properly declared in the `package.xml` file of the package.

<a id="install-dependencies"></a>

## Install dependencies

Run the following command to install utilities needed for the build:

```
$ sudo apt install python3-bloom python3-rosdep fakeroot debhelper dh-python
```

<a id="initialize-rosdep"></a>

## Initialize rosdep

Initialize the rosdep database by calling:

```
$ sudo rosdep init
$ rosdep update
```

Note that the `rosdep init` command may fail if it has already been initialized in the past; this can safely be ignored.

<a id="build-the-deb-from-the-package"></a>

## Build the deb from the package

Run the following commands to build the deb:

```
$ cd /path/to/pkg_source  # this should be the directory that contains the package.xml
$ bloom-generate rosdebian
$ fakeroot debian/rules binary
```

Assuming that all required dependencies are available and that compilation succeeds, the new package will be available in the parent directory of this directory.
