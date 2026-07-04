---
title: "Migrating Packages"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-Packages"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-Packages.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating C++ Packages Reference](migrating-cpp-packages.md)

<a id="migrating-packages"></a>

# Migrating Packages

Table of Contents

- [Prerequisites](#prerequisites)
- [Package.xml format version](#package-xml-format-version)
- [Dependency names](#dependency-names)
- [Metapackages](#metapackages)
- [Licensing](#licensing)

  - [Changing the License](#changing-the-license)

There are two different kinds of package migrations:

- Migrating the source code of an existing package from ROS 1 to ROS 2 with the intent that a significant part of the source code will stay the same or at least similar.
  An example for this is [pluginlib](https://github.com/ros/pluginlib) where the source code is maintained in different branches within the same repository and common patches can be ported between those branches when necessary.
- Implementing the same or similar functionality of a ROS 1 package for ROS 2 but with the assumption that the source code will be significantly different.
  An example for this is [roscpp](https://github.com/ros/ros_comm/tree/melodic-devel/clients/roscpp) in ROS 1 and [rclcpp](https://github.com/ros2/rclcpp/tree/rolling/rclcpp) in ROS 2 which are separate repositories and don’t share any code.

<a id="prerequisites"></a>

## Prerequisites

Before being able to migrate a ROS 1 package to ROS 2 all of its dependencies must be available in ROS 2.

<a id="package-xml-format-version"></a>

## Package.xml format version

ROS 2 only supports `package.xml` format versions 2 and higher.
If your package’s `package.xml` uses format 1, then update it using the [Package.xml format 1 to 2 migration guide](migrating-package-xml.md).

<a id="dependency-names"></a>

## Dependency names

Dependency names that come from [rosdep](../../tutorials/intermediate/rosdep.md) should not need to change, as those are shared across ROS 1 and ROS 2.

Some packages released into ROS might have different names in ROS 2 so the dependencies might need to be updated accordingly.

<a id="metapackages"></a>

## Metapackages

ROS 2 doesn’t have a special package type for metapackages.
Metapackages can still exist as regular packages that only contain runtime dependencies.
When migrating metapackages from ROS 1, simply remove the `<metapackage />` tag in your package manifest.
See [Using variants](../using-variants.md) for more information on metapackages/variants.

<a id="licensing"></a>

## Licensing

In ROS 1 our recommended license was the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).
In ROS 2 our recommended license is the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

For any new project we recommend using the Apache 2.0 License, whether ROS 1 or ROS 2.

However, when migrating code from ROS 1 to ROS 2 we cannot simply change the license.
The existing license must be preserved for any preexisting contributions.

To that end if a package is being migrated we recommend keeping the existing license and continuing to contribute to that package under the existing OSI license, which we expect to be the BSD license for core elements.

This will keep things clear and easy to understand.

<a id="changing-the-license"></a>

### Changing the License

It is possible to change the license, however you will need to contact all the contributors and get permission.
For most packages this is likely to be a significant effort and not worth considering.
If the package has a small set of contributors then this may be feasible.
