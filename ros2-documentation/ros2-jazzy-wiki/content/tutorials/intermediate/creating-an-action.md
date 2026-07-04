---
title: "Creating an action"
docname: "Tutorials/Intermediate/Creating-an-Action"
source: "Tutorials/Intermediate/Creating-an-Action.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="creating-an-action"></a>
<a id="actioncreate"></a>

# Creating an action

**Goal:** Define an action in a ROS 2 package.

**Tutorial level:** Intermediate

**Time:** 5 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Creating an interface package](#creating-an-interface-package)
  - [2 Defining an action](#defining-an-action)
  - [3 Building an action](#building-an-action)
- [Summary](#summary)
- [Next steps](#next-steps)
- [Related content](#related-content)

<a id="background"></a>

## Background

You learned about actions previously in the [Understanding actions](../beginner-cli-tools/understanding-ros2-actions.md) tutorial.
Like the other communication types and their respective interfaces (topics/msg and services/srv),
you can also custom-define actions in your packages.
This tutorial shows you how to define and build an action that you can use
with the action server and action client you will write in the next tutorial.

<a id="prerequisites"></a>

## Prerequisites

You should have [ROS 2](../../installation/overview.md) and [colcon](https://colcon.readthedocs.org) installed.

You should know how to set up a [workspace](../beginner-client-libraries/creating-a-workspace.md) and create packages.

Remember to [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md) first.

<a id="tasks"></a>

## Tasks

<a id="creating-an-interface-package"></a>

### 1 Creating an interface package

Linux

```
$ mkdir -p ~/ros2_ws/src # you can reuse an existing workspace with this naming convention
$ cd ~/ros2_ws/src
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 custom_action_interfaces
```

macOS

```
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws/src
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 custom_action_interfaces
```

Windows

```
$ md \ros2_ws\src
$ cd \ros2_ws\src
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 custom_action_interfaces
```

`custom_action_interfaces` is the name of the new package.
Note that it is, and can only be, a CMake package, but this doesn’t restrict in which type of packages you can use your actions.
The `--build-type ament_cmake` flag is largely optional when creating a new ROS 2 package but we are including it here for completeness.
You can create your own custom interfaces in a CMake package, and then use it in a C++ or Python node.

> [!NOTE]
>
> It is good practice to keep `.msg`, `.srv`, and `.action` files in separate packages from the nodes that use them.
> This makes it easier to reuse the interface definitions across different packages.

<a id="defining-an-action"></a>

### 2 Defining an action

Actions are defined in `.action` files of the form:

```
# Request
---
# Result
---
# Feedback
```

An action definition is made up of three message definitions separated by `---`.

- A *request* message is sent from an action client to an action server initiating a new goal.
- A *result* message is sent from an action server to an action client when a goal is done.
- *Feedback* messages are periodically sent from an action server to an action client with updates about a goal.

An instance of an action is typically referred to as a *goal*.

Say we want to define a new action “Fibonacci” for computing the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number).

Create an `action` directory in our ROS 2 package `custom_action_interfaces`:

Linux

```
$ cd custom_action_interfaces
$ mkdir action
```

macOS

```
$ cd custom_action_interfaces
$ mkdir action
```

Windows

```
$ cd custom_action_interfaces
$ md action
```

Within the `action` directory, create a file called `Fibonacci.action` with the following contents:

```
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

The goal request is the `order` of the Fibonacci sequence we want to compute, the result is the final `sequence`, and the feedback is the `partial_sequence` computed so far.

<a id="building-an-action"></a>

### 3 Building an action

Before we can use the new Fibonacci action type in our code, we must pass the definition to the rosidl code generation pipeline.

This is accomplished by adding the following lines to our `CMakeLists.txt` before the `ament_package()` line:

```
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Fibonacci.action"
)
```

We should also add the required dependencies to our `package.xml`:

```
<buildtool_depend>rosidl_default_generators</buildtool_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

We should now be able to build the package containing the `Fibonacci` action definition:

```
$ cd ~/ros2_ws # Change to the root of the workspace
$ colcon build # Build
```

We’re done!

By convention, action types will be prefixed by their package name and the word `action`.
So when we want to refer to our new action, it will have the full name `custom_action_interfaces/action/Fibonacci`.

We can check that our action built successfully with the command line tool.
First source our workspace:

Linux

```
$ source install/local_setup.bash
```

macOS

```
$ source install/local_setup.console
```

Windows

```
$ call install\local_setup.bat
```

Now check that our action definition exists:

```
$ ros2 interface show custom_action_interfaces/action/Fibonacci
```

You should see the Fibonacci action definition printed to the screen.

<a id="summary"></a>

## Summary

In this tutorial, you learned the structure of an action definition.
You also learned how to correctly build a new action interface using `CMakeLists.txt` and `package.xml`,
and how to verify a successful build.

<a id="next-steps"></a>

## Next steps

Next, let’s utilize your newly defined action interface by creating an action service and client (in [Python](writing-an-action-server-client/py.md) or [C++](writing-an-action-server-client/cpp.md)).

<a id="related-content"></a>

## Related content

For more detailed information about ROS actions, please refer to the [design article](http://design.ros2.org/articles/actions.html).
