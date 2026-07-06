---
title: "Composing multiple nodes in a single process"
docname: "Tutorials/Intermediate/Composition"
source: "Tutorials/Intermediate/Composition.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Configure service introspection](../demos/service-introspection.md) | [Configuring environment](../beginner-cli-tools/configuring-ros2-environment.md)

<a id="composing-multiple-nodes-in-a-single-process"></a>

# Composing multiple nodes in a single process

Table of Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Run the demos](#run-the-demos)

  - [Discover available components](#discover-available-components)
  - [Run-time composition using ROS services with a publisher and subscriber](#run-time-composition-using-ros-services-with-a-publisher-and-subscriber)
  - [Run-time composition using ROS services with a server and client](#run-time-composition-using-ros-services-with-a-server-and-client)
  - [Compile-time composition with hardcoded nodes](#compile-time-composition-with-hardcoded-nodes)
  - [Run-time composition using dlopen](#run-time-composition-using-dlopen)
  - [Composition using launch actions](#composition-using-launch-actions)
- [Advanced Topics](#advanced-topics)

  - [Component container types](#component-container-types)
  - [Unloading components](#unloading-components)
  - [Remapping container name and namespace](#remapping-container-name-and-namespace)
  - [Remap component names and namespaces](#remap-component-names-and-namespaces)
  - [Passing parameter values into components](#passing-parameter-values-into-components)
  - [Passing additional arguments into components](#passing-additional-arguments-into-components)
- [Composable nodes as shared libraries](#composable-nodes-as-shared-libraries)
- [Composing Non-Node Derived Components](#composing-non-node-derived-components)

**Goal:** Compose multiple nodes into a single process.

**Tutorial level:** Intermediate

**Time:** 20 minutes

<a id="background"></a>

## Background

See the [conceptual article](../../concepts/intermediate/about-composition.md).

For information on how to write a composable node, [check out this tutorial](writing-a-composable-node.md).

<a id="prerequisites"></a>

## Prerequisites

This tutorial uses executables from the [rclcpp\_components](https://github.com/ros2/rclcpp/tree/jazzy/rclcpp_components), [ros2component](https://github.com/ros2/ros2cli/tree/jazzy/ros2component), [composition](https://github.com/ros2/demos/tree/jazzy/composition), and [image\_tools](https://github.com/ros2/demos/tree/jazzy/image_tools) packages.
If you’ve followed the [installation instructions](../../installation/overview.md) for your platform, these should already be installed.

<a id="run-the-demos"></a>

## Run the demos

<a id="discover-available-components"></a>

### Discover available components

To see what components are registered and available in the workspace, execute the following in a shell:

```
$ ros2 component types
(... components of other packages here)
composition
  composition::Talker
  composition::Listener
  composition::NodeLikeListener
  composition::Server
  composition::Client
(... components of other packages here)
```

<a id="run-time-composition-using-ros-services-with-a-publisher-and-subscriber"></a>

### Run-time composition using ROS services with a publisher and subscriber

In the first shell, start the component container:

```
$ ros2 run rclcpp_components component_container
```

Open the second shell and verify that the container is running via `ros2` command line tools.
You should see a name of the component:

```
$ ros2 component list
/ComponentManager
```

In the second shell load the talker component (see [talker](https://github.com/ros2/demos/blob/jazzy/composition/src/talker_component.cpp) source code).
The command will return the unique ID of the loaded component as well as the node name:

```
$ ros2 component load /ComponentManager composition composition::Talker
Loaded component 1 into '/ComponentManager' container node as '/talker'
```

Now the first shell should show a message that the component was loaded as well as repeated message for publishing a message.

Run another command in the second shell to load the listener component (see [listener](https://github.com/ros2/demos/blob/jazzy/composition/src/listener_component.cpp) source code):

```
$ ros2 component load /ComponentManager composition composition::Listener
Loaded component 2 into '/ComponentManager' container node as '/listener'
```

The `ros2` command line utility can now be used to inspect the state of the container:

```
$ ros2 component list
/ComponentManager
   1  /talker
   2  /listener
```

Now the first shell should show repeated output for each received message.

<a id="run-time-composition-using-ros-services-with-a-server-and-client"></a>

### Run-time composition using ROS services with a server and client

The example with a server and a client is very similar.

In the first shell:

```
$ ros2 run rclcpp_components component_container
```

In the second shell (see [server](https://github.com/ros2/demos/blob/jazzy/composition/src/server_component.cpp) and [client](https://github.com/ros2/demos/blob/jazzy/composition/src/client_component.cpp) source code):

```
$ ros2 component load /ComponentManager composition composition::Server
$ ros2 component load /ComponentManager composition composition::Client
```

In this case the client sends a request to the server, the server processes the request and replies with a response, and the client prints the received response.

<a id="compile-time-composition-with-hardcoded-nodes"></a>

### Compile-time composition with hardcoded nodes

This demo shows that the same shared libraries can be reused to compile a single executable running multiple components without using ROS interfaces.
The executable contains all four components from above: talker and listener as well as server and client, which is hardcoded in the main function.

In the shell call (see [source code](https://github.com/ros2/demos/blob/jazzy/composition/src/manual_composition.cpp)):

```
$ ros2 run composition manual_composition
```

This should show repeated messages from both pairs, the talker and the listener as well as the server and the client.

> [!NOTE]
>
> Manually-composed components will not be reflected in the `ros2 component list` command line tool output.

<a id="run-time-composition-using-dlopen"></a>

### Run-time composition using dlopen

This demo presents an alternative to run-time composition by creating a generic container process and explicitly passing the libraries to load without using ROS interfaces.
The process will open each library and create one instance of each “rclcpp::Node” class in the library ([source code](https://github.com/ros2/demos/blob/jazzy/composition/src/dlopen_composition.cpp)).

Linux

```
$ ros2 run composition dlopen_composition `ros2 pkg prefix composition`/lib/libtalker_component.so `ros2 pkg prefix composition`/lib/liblistener_component.so
```

macOS

```
$ ros2 run composition dlopen_composition `ros2 pkg prefix composition`/lib/libtalker_component.dylib `ros2 pkg prefix composition`/lib/liblistener_component.dylib
```

Windows

```
$ ros2 pkg prefix composition
```

to get the path to where composition is installed.
Then call

```
$ ros2 run composition dlopen_composition <path_to_composition_install>\bin\talker_component.dll <path_to_composition_install>\bin\listener_component.dll
```

Now the shell should show repeated output for each sent and received message.

> [!NOTE]
>
> dlopen-composed components will not be reflected in the `ros2 component list` command line tool output.

<a id="composition-using-launch-actions"></a>

### Composition using launch actions

While the command line tools are useful for debugging and diagnosing component configurations, it is frequently more convenient to start a set of components at the same time.
To automate this action, we can use a [launch file](https://github.com/ros2/demos/blob/jazzy/composition/launch/composition_demo_launch.py):

```
$ ros2 launch composition composition_demo_launch.py
```

<a id="advanced-topics"></a>

## Advanced Topics

Now that we have seen the basic operation of components, we can discuss a few more advanced topics.

<a id="component-container-types"></a>
<a id="componentcontainertypes"></a>

### Component container types

As introduced in [Component Container](../../concepts/intermediate/about-composition.md#componentcontainer), there are a few component container types with different options.
You can choose the most appropriate component container type for your requirement.

- `component_container` (No options / parameters available)

  > ```
  > $ ros2 run rclcpp_components component_container
  > ```
- `component_container_mt` with `MultiThreadedExecutor` composed of 4 threads.
  :   - `thread_num` parameter option is available to specify the number of threads in `MultiThreadedExecutor`.

      ```
      $ ros2 run rclcpp_components component_container_mt --ros-args -p thread_num:=4
      ```
- `component_container_isolated` with `MultiThreadedExecutor` for each component.
  :   - `--use_multi_threaded_executor` argument specifies executor type used for each component to `MultiThreadedExecutor`.

      ```
      $ ros2 run rclcpp_components component_container_isolated --use_multi_threaded_executor
      ```

<a id="unloading-components"></a>

### Unloading components

In the first shell, start the component container:

```
$ ros2 run rclcpp_components component_container
```

Verify that the container is running via `ros2` command line tools:

```
$ ros2 component list
/ComponentManager
```

In the second shell load both the talker and listener as we have before:

```
$ ros2 component load /ComponentManager composition composition::Talker
Loaded component 1 into '/ComponentManager' container node as '/talker'
$ ros2 component load /ComponentManager composition composition::Listener
Loaded component 2 into '/ComponentManager' container node as '/listener'
```

The unique ID of a component is printed when it gets loaded.
You can also get the unique IDs of all components by just listing them now that they are loaded:

```
$ ros2 component list
/ComponentManager
  1  /talker
  2  /listener
```

Use the unique ID to unload the component from the component container.

```
$ ros2 component unload /ComponentManager 1 2
Unloaded component 1 from '/ComponentManager' container
Unloaded component 2 from '/ComponentManager' container
```

In the first shell, verify that the repeated messages from talker and listener have stopped.

<a id="remapping-container-name-and-namespace"></a>

### Remapping container name and namespace

The component manager name and namespace can be remapped via standard command line arguments:

```
$ ros2 run rclcpp_components component_container --ros-args -r __node:=MyContainer -r __ns:=/ns
```

In a second shell, components can be loaded by using the updated container name:

```
$ ros2 component load /ns/MyContainer composition composition::Listener
```

> [!NOTE]
>
> Namespace remappings of the container do not affect loaded components.

<a id="remap-component-names-and-namespaces"></a>

### Remap component names and namespaces

Component names and namespaces may be adjusted via arguments to the load command.

In the first shell, start the component container:

```
$ ros2 run rclcpp_components component_container
```

Some examples of how to remap names and namespaces.

Remap node name:

```
$ ros2 component load /ComponentManager composition composition::Talker --node-name talker2
```

Remap namespace:

```
$ ros2 component load /ComponentManager composition composition::Talker --node-namespace /ns
```

Remap both:

```
$ ros2 component load /ComponentManager composition composition::Talker --node-name talker3 --node-namespace /ns2
```

Now use `ros2` command line utility:

```
$ ros2 component list
/ComponentManager
   1  /talker2
   2  /ns/talker
   3  /ns2/talker3
```

> [!NOTE]
>
> Namespace remappings of the container do not affect loaded components.

<a id="passing-parameter-values-into-components"></a>

### Passing parameter values into components

The `ros2 component load` command-line supports passing arbitrary parameters to the node as it is constructed.
This functionality can be used as follows:

```
$ ros2 component load /ComponentManager image_tools image_tools::Cam2Image -p burger_mode:=true
$ ros2 run rqt_image_view rqt_image_view  # Shows burgers bouncing, instead of image from camera
```

<a id="passing-additional-arguments-into-components"></a>

### Passing additional arguments into components

The `ros2 component load` command-line supports passing particular options to the component manager for use when constructing the node.

The following example shows the use of the extra arguments `use_intra_process_comms` and `forward_global_arguments`:

```
$ ros2 component load /ComponentManager composition composition::Talker -e use_intra_process_comms:=true -e forward_global_arguments:=false
```

The following extra arguments are supported.

Extra Arguments for Component Manager

| Argument | Type | Default | Description |
| --- | --- | --- | --- |
| `forward_global_arguments` | Boolean | True | Apply global arguments to the component node when loading. |
| `use_intra_process_comms` | Boolean | False | Enable intra-process communication in the component node. |

<a id="composable-nodes-as-shared-libraries"></a>

## Composable nodes as shared libraries

If you want to export a composable node as a shared library from a package and use that node in another package that does link-time composition, add code to the CMake file which imports the actual targets in downstream packages.

Then install the generated file and export the generated file.

A practical example can be seen here: [ROS Discourse - Ament best practice for sharing libraries](https://discourse.openrobotics.org/t/ament-best-practice-for-sharing-libraries/3602)

<a id="composing-non-node-derived-components"></a>

## Composing Non-Node Derived Components

In ROS 2, components allow for more efficient use of system resources and provide a powerful feature that enables you to create reusable functionality that is not tied to a specific node.

One advantage of using components is that they allow you to create non-node derived functionality as standalone executables or shared libraries that can be loaded into the ROS system as needed.

To create a component that is not derived from a node, follow these guidelines:

1. Implement a constructor that takes `const rclcpp::NodeOptions&` as its argument.
2. Implement the `get_node_base_interface()` method, which should return a `NodeBaseInterface::SharedPtr`.
   You can use the `get_node_base_interface()` method of a node that you create in your constructor to provide this interface.

Here’s an example of a component that is not derived from a node, which listens to a ROS topic: [node\_like\_listener\_component](https://github.com/ros2/demos/blob/jazzy/composition/src/node_like_listener_component.cpp).

For more information on this topic, you can refer to this [discussion](https://github.com/ros2/rclcpp/issues/2110#issuecomment-1454228192).
