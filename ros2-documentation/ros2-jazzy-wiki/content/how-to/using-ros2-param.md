---
title: "Using the ros2 param command-line tool"
docname: "How-To-Guides/Using-ros2-param"
source: "How-To-Guides/Using-ros2-param.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="using-the-ros2-param-command-line-tool"></a>

# Using the `ros2 param` command-line tool

Table of Contents

- [`ros2 param list`](#ros2-param-list)
- [`ros2 param get`](#ros2-param-get)
- [`ros2 param set`](#ros2-param-set)
- [`ros2 param delete`](#ros2-param-delete)
- [`ros2 param describe`](#ros2-param-describe)
- [`ros2 param dump`](#ros2-param-dump)
- [`ros2 param load`](#ros2-param-load)

Parameters in ROS 2 can be get, set, listed, and described through a set of services as described in [the concept document](../concepts/basic/about-parameters.md).
The `ros2 param` command-line tool is a wrapper around these service calls that makes it easy to manipulate parameters from the command-line.

<a id="ros2-param-list"></a>

## `ros2 param list`

This command will list all of the available parameters on a given node, or on all discoverable nodes if no node is given.

To get all of the parameters on a given node:

```
$ ros2 param list /my_node
```

To get all of the parameters on all nodes in the system (this can take a long time on a complicated network):

```
$ ros2 param list
```

<a id="ros2-param-get"></a>

## `ros2 param get`

This command will get the value of a particular parameter on a particular node.

To get the value of a parameter on a node:

```
$ ros2 param get /my_node use_sim_time
```

<a id="ros2-param-set"></a>

## `ros2 param set`

This command will set the value of a particular parameter on a particular node.
For most parameters, the type of the new value must be the same as the existing type.

To set the value of a parameter on a node:

```
$ ros2 param set /my_node use_sim_time false
```

The value that is passed on the command-line is in YAML, which allows arbitrary YAML expressions to be used.
However, it also means that certain expressions will be interpreted differently than might be expected.
For instance, if the parameter `my_string` on node `my_node` is of type string, the following will not work:

```
$ ros2 param set /my_node my_string off
```

That’s because YAML is interpreting “off” as a boolean, and `my_string` is a string type.
This can be worked around by using the YAML syntax for explicitly setting strings, e.g.:

```
$ ros param set /my_node my_string '!!str off'
```

Additionally, YAML supports heterogeneous lists, containing (say) a string, a boolean, and an integer.
However, ROS 2 parameters do not support heterogeneous lists, so any YAML list that has multiple types will be interpreted as a string.
Assuming that the parameter `my_int_array` on node `my_node` is of type integer array, the following will not work:

```
$ ros param set /my_node my_int_array '[foo,off,1]'
```

The following string typed parameter would work:

```
$ ros param set /my_node my_string '[foo,off,1]'
```

<a id="ros2-param-delete"></a>

## `ros2 param delete`

This command will remove a parameter from a particular node.
However, note that this can only remove dynamic parameters (not declared parameters).
See [the concept document](../concepts/basic/about-parameters.md) for more information.

```
$ ros2 param delete /my_node my_string
```

<a id="ros2-param-describe"></a>

## `ros2 param describe`

This command will provide a textual description of a particular parameter on a particular node:

```
$ ros2 param describe /my_node use_sim_time
```

<a id="ros2-param-dump"></a>

## `ros2 param dump`

This command will print out all of the parameters on a particular node in a YAML file format.
The output of this command can then be used to re-run the node with the same parameters later:

```
$ ros2 param dump /my_node
```

<a id="ros2-param-load"></a>

## `ros2 param load`

This command will load the values of the parameters from a YAML file into a particular node.
That is, this command can reload values at runtime that were dumped out by `ros2 param dump`:

```
$ ros2 param load /my_node my_node.yaml
```
