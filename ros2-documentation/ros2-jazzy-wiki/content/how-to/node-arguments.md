---
title: "Passing ROS arguments to nodes via the command-line"
docname: "How-To-Guides/Node-arguments"
source: "How-To-Guides/Node-arguments.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="passing-ros-arguments-to-nodes-via-the-command-line"></a>

# Passing ROS arguments to nodes via the command-line

Table of Contents

- [Name remapping](#name-remapping)

  - [Example](#example)
- [Logger configuration](#logger-configuration)
- [Parameters](#parameters)

  - [Setting parameters directly from the command line](#setting-parameters-directly-from-the-command-line)
  - [Setting parameters from YAML files](#setting-parameters-from-yaml-files)

All ROS nodes take a set of arguments that allow various properties to be reconfigured.
Examples include configuring the name/namespace of the node, topic/service names used, and parameters on the node.
All ROS-specific arguments have to be specified after a `--ros-args` flag:

```
$ ros2 run my_package node_executable --ros-args ...
```

For more details, see [this design doc](https://design.ros2.org/articles/ros_command_line_arguments.html).

<a id="name-remapping"></a>

## Name remapping

Names within a node (e.g. topics/services) can be remapped using the syntax `-r <old name>:=<new name>`.
The name/namespace of the node itself can be remapped using `-r __node:=<new node name>` and `-r __ns:=<new node namespace>`.

Note that these remappings are “static” remappings, in that they apply for the lifetime of the node.
“Dynamic” remapping of names after nodes have been started is not yet supported.

See [this design doc](https://design.ros2.org/articles/static_remapping.html) for more details on remapping arguments (not all functionality is available yet).

<a id="example"></a>

### Example

The following invocation will cause the `talker` node to be started under the node name `my_talker`, publishing on the topic named `my_topic` instead of the default of `chatter`.
The namespace, which must start with a forward slash, is set to `/demo`, which means that topics are created in that namespace (`/demo/my_topic`), as opposed to globally (`/my_topic`).

```
$ ros2 run demo_nodes_cpp talker --ros-args -r __ns:=/demo -r __node:=my_talker -r chatter:=my_topic
```

<a id="passing-remapping-arguments-to-specific-nodes"></a>

#### Passing remapping arguments to specific nodes

If multiple nodes are being run within a single process (e.g. using [Composition](../concepts/intermediate/about-composition.md)), remapping arguments can be passed to a specific node using its name as a prefix.
For example, the following will pass the remapping arguments to the specified nodes:

```
$ ros2 run composition manual_composition --ros-args -r talker:__node:=my_talker -r listener:__node:=my_listener
```

The following example will both change the node name and remap a topic (node and namespace changes are always applied *before* topic remapping):

```
$ ros2 run composition manual_composition --ros-args -r talker:__node:=my_talker -r my_talker:chatter:=my_topic -r listener:__node:=my_listener -r my_listener:chatter:=my_topic
```

<a id="logger-configuration"></a>

## Logger configuration

The per-node logging level can be specified using the `--log-level` command line argument.
The executable log file name prefix, which includes all nodes in the executable, can be specified using `--log-file-name` command line argument.
For more information please see [the logging page](../tutorials/demos/logging-and-logger-configuration.md).

<a id="parameters"></a>

## Parameters

<a id="setting-parameters-directly-from-the-command-line"></a>
<a id="nodeargsparameters"></a>

### Setting parameters directly from the command line

You can set parameters directly from the command line using the following syntax:

```
$ ros2 run package_name executable_name --ros-args -p param_name:=param_value
```

As an example, you can run:

```
$ ros2 run demo_nodes_cpp parameter_blackboard --ros-args -p some_int:=42 -p "a_string:=Hello world" -p "some_lists.some_integers:=[1, 2, 3, 4]" -p "some_lists.some_doubles:=[3.14, 2.718]"
```

Other nodes will be able to retrieve the parameter values, e.g.:

```
$ ros2 param list parameter_blackboard
a_string
qos_overrides./parameter_events.publisher.depth
qos_overrides./parameter_events.publisher.durability
qos_overrides./parameter_events.publisher.history
qos_overrides./parameter_events.publisher.reliability
some_int
some_lists.some_doubles
some_lists.some_integers
use_sim_time
```

<a id="setting-parameters-from-yaml-files"></a>

### Setting parameters from YAML files

Parameters can be set from the command-line in the form of yaml files.

[See here](https://github.com/ros2/rcl/tree/jazzy/rcl_yaml_param_parser) for examples of the yaml file syntax.

As an example, save the following as `demo_params.yaml`:

```
parameter_blackboard:
    ros__parameters:
        some_int: 42
        a_string: "Hello world"
        some_lists:
            some_integers: [1, 2, 3, 4]
            some_doubles : [3.14, 2.718]

/**:
  ros__parameters:
    wildcard_full: "Full wildcard for any namespaces and any node names"

/**/parameter_blackboard:
  ros__parameters:
    wildcard_namespace: "Wildcard for a specific node name under any namespace"

/*:
  ros__parameters:
    wildcard_nodename_root_namespace: "Wildcard for any node names, but only in root namespace"
```

> [!NOTE]
>
> Wildcards can be used for node names and namespaces.
> `*` matches a single token delimited by slashes (`/`).
> `**` matches zero or more tokens delimited by slashes.
> Partial matches are not allowed (e.g. `foo*`).

Then either declare the parameters within your node with [declare\_parameter](http://docs.ros.org/en/jazzy/p/rclcpp/generated/classrclcpp_1_1Node.html#_CPPv4N6rclcpp4Node17declare_parameterERKNSt6stringERKN6rclcpp14ParameterValueERKN14rcl_interfaces3msg19ParameterDescriptorEb) or [declare\_parameters](http://docs.ros.org/en/jazzy/p/rclcpp/generated/classrclcpp_1_1Node.html#_CPPv4I0EN6rclcpp4Node18declare_parametersENSt6vectorI10ParameterTEERKNSt6stringERKNSt3mapINSt6stringENSt4pairI10ParameterTN14rcl_interfaces3msg19ParameterDescriptorEEEEEb), or [set the node to automatically declare parameters](http://docs.ros.org/en/jazzy/p/rclcpp/generated/classrclcpp_1_1NodeOptions.html#_CPPv4NK6rclcpp11NodeOptions47automatically_declare_parameters_from_overridesEv) if they were passed in via a command line override.

Then run the following:

```
$ ros2 run demo_nodes_cpp parameter_blackboard --ros-args --params-file demo_params.yaml
```

Other nodes will be able to retrieve the parameter values, e.g.:

```
$ ros2 param list parameter_blackboard
a_string
qos_overrides./parameter_events.publisher.depth
qos_overrides./parameter_events.publisher.durability
qos_overrides./parameter_events.publisher.history
qos_overrides./parameter_events.publisher.reliability
some_int
some_lists.some_doubles
some_lists.some_integers
use_sim_time
wildcard_full
wildcard_namespace
wildcard_nodename_root_namespace
```
