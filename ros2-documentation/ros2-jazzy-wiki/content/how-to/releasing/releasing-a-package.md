---
title: "Releasing a Package"
docname: "How-To-Guides/Releasing/Releasing-a-Package"
source: "How-To-Guides/Releasing/Releasing-a-Package.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](first-time-release.md) | [Index Your Packages](index-your-packages.md) | [Migrating a C++ Package Example](../migrating-from-ros1/migrating-cpp-package-example.md) | [Migrating a Python Package Example](../migrating-from-ros1/migrating-python-package-example.md) | [Migrating C++ Packages Reference](../migrating-from-ros1/migrating-cpp-packages.md)

<a id="releasing-a-package"></a>

# Releasing a Package

**Releasing a package makes your package available on the public ROS 2 buildfarm.**
This will:

- Make your package available to be installed via package managers (e.g. `apt` on Ubuntu) for all supported Linux platforms in a ROS distribution as described in [REP 2000](https://reps.openrobotics.org/rep-2000/).
- Allow your package to have API documentation automatically generated.
- Make your package part of the [ROS Index](https://index.ros.org).
- (Optionally) Allow you to have automatic CI run for pull requests in your repository.

**Follow one of the guides below to get your package released:**

- [Index Your Packages](index-your-packages.md) - if this is the first release for the package
- [First Time Release](first-time-release.md) - if this is the first release for the package, but it is already indexed
- [Subsequent Releases](subsequent-releases.md) - if you are releasing a new version of a package that has already been released

After successfully following the instructions, your package will be released into the ROS ecosystem on the next distro synchronization!
