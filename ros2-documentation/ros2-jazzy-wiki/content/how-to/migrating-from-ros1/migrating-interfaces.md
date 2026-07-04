---
title: "Migrating Interfaces"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-Interfaces"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-Interfaces.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating C++ Packages Reference](migrating-cpp-packages.md)

<a id="migrating-interfaces"></a>

# Migrating Interfaces

Table of Contents

- [Interface definitions](#interface-definitions)
- [Building interfaces](#building-interfaces)

  - [Migrating interface package to ROS 2](#migrating-interface-package-to-ros-2)

Messages, services, and actions are collectively called `interfaces` in ROS 2.

<a id="interface-definitions"></a>

## Interface definitions

Message files must end in `.msg` and must be located in the subfolder `msg`.
Service files must end in `.srv` and must be located in the subfolder `srv`.
Actions files must end in `.action` and must be located in the subfolder `action`.

These files might need to be updated to comply with the [ROS Interface definition](http://design.ros2.org/articles/legacy_interface_definition.html).
Some primitive types have been removed and the types `duration` and `time` which were builtin types in ROS 1 have been replaced with normal message definitions and must be used from the [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/jazzy/builtin_interfaces) package.
Also some naming conventions are stricter than in ROS 1.
There is additional information in the [conceptual article](../../concepts/basic/about-interfaces.md).

<a id="building-interfaces"></a>

## Building interfaces

The way in which interfaces are built in ROS 2 differs substantially from ROS 1.
Interfaces can only be built from packages containing a `CMakeLists.txt`.
If you are developing a pure Python package, then the interfaces should be placed in a different package containing only the interfaces (which is best practice anyway).
See the [custom interfaces tutorial](../../tutorials/beginner-client-libraries/custom-ros2-interfaces.md) for more information.

<a id="migrating-interface-package-to-ros-2"></a>

### Migrating interface package to ROS 2

In your `package.xml`:

- Add `<buildtool_depend>rosidl_default_generators</buildtool_depend>`.
- Add `<exec_depend>rosidl_default_runtime</exec_depend>`.
- Add `<member_of_group>rosidl_interface_packages</member_of_group>`
- For each dependent message package, add `<depend>message_package</depend>`.

In your `CMakeLists.txt`:

- Enable C++17

```
set(CMAKE_CXX_STANDARD 17)
```

- Add `find_package(rosidl_default_generators REQUIRED)`
- For each dependent message package, add `find_package(message_package REQUIRED)` and replace the CMake function call to `generate_messages` with `rosidl_generate_interfaces`.

This will replace `add_message_files` and `add_service_files` listing of all the message and service files, which can be removed.
