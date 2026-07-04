---
title: "Migrating Launch Files"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-Launch-Files"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-Launch-Files.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating C++ Packages Reference](migrating-cpp-packages.md)

<a id="migrating-launch-files"></a>
<a id="migratinglaunch"></a>

# Migrating Launch Files

Table of Contents

- [Background](#background)
- [Migrating tags](#migrating-tags)

  - [launch](#launch)
  - [node](#node)
  - [param](#param)
  - [rosparam](#rosparam)
  - [remap](#remap)
  - [include](#include)
  - [arg](#arg)
  - [env](#env)
  - [group](#group)
  - [machine](#machine)
  - [test](#test)
- [New tags in ROS 2](#new-tags-in-ros-2)

  - [set\_env and unset\_env](#set-env-and-unset-env)
  - [push\_ros\_namespace](#push-ros-namespace)
  - [let](#let)
  - [executable](#executable)
- [Replacing an include tag](#replacing-an-include-tag)
- [Substitutions](#substitutions)
- [Type inference rules](#id8)

While launch files in ROS 1 are always specified using [XML](https://wiki.ros.org/roslaunch/XML) files, ROS 2 supports both XML and YAML files.
ROS 2 also supports Python launch scripts to enable more flexibility (see [launch package](https://github.com/ros2/launch/tree/jazzy/launch)).
However, for typical use cases, XML and YAML should be preferred over Python.

This guide describes how to write ROS 2 XML launch files for an easy migration from ROS 1.

<a id="background"></a>

## Background

A description of the ROS 2 launch system can be found in [Launch System tutorial](../../tutorials/intermediate/launch/launch-system.md).

<a id="migrating-tags"></a>

## Migrating tags

<a id="launch"></a>

### launch

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/launch).
- `launch` is the root element of any ROS 2 launch XML file.

<a id="node"></a>

### node

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/node).
- Launches a new node.
- Differences from ROS 1:

  > - `type` attribute is now `exec`.
  > - `ns` attribute is now `namespace`.
  > - `required="true"` is now `on_exit="shutdown"`.
  > - The following attributes aren’t available: `machine`, `respawn_delay`, `clear_params`.

<a id="example"></a>

#### Example

```
<launch>
   <node pkg="demo_nodes_cpp" exec="talker"/>
   <node pkg="demo_nodes_cpp" exec="listener"/>
</launch>
```

<a id="param"></a>

### param

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/param).
- Used for passing a parameter to a node.
- There’s no global parameter concept in ROS 2.
  For that reason, it can only be used nested in a `node` tag.
  Some attributes aren’t supported in ROS 2: `type`, `textfile`, `binfile`, `executable`.
- The `command` attribute is now `value="$(command '...' )"`.

<a id="id1"></a>

#### Example

```
<launch>
   <node pkg="demo_nodes_cpp" exec="parameter_event">
      <param name="foo" value="5"/>
   </node>
</launch>
```

<a id="type-inference-rules"></a>

#### Type inference rules

Here are some examples of how to write parameters:

```
<node pkg="my_package" exec="my_executable" name="my_node">
   <!--A string parameter with value "1"-->
   <param name="a_string" value="'1'"/>
   <!--A integer parameter with value 1-->
   <param name="an_int" value="1"/>
   <!--A float parameter with value 1.0-->
   <param name="a_float" value="1.0"/>
   <!--A string parameter with value "asd"-->
   <param name="another_string" value="asd"/>
   <!--Another string parameter, with value "asd"-->
   <param name="string_with_same_value_as_above" value="'asd'"/>
   <!--Another string parameter, with value "'asd'"-->
   <param name="quoted_string" value="\'asd\'"/>
   <!--A list of strings, with value ["asd", "bsd", "csd"]-->
   <param name="list_of_strings" value="asd, bsd, csd" value-sep=", "/>
   <!--A list of ints, with value [1, 2, 3]-->
   <param name="list_of_ints" value="1,2,3" value-sep=","/>
   <!--Another list of strings, with value ["1", "2", "3"]-->
   <param name="another_list_of_strings" value="'1';'2';'3'" value-sep=";"/>
   <!--A list of strings using an strange separator, with value ["1", "2", "3"]-->
   <param name="strange_separator" value="'1'//'2'//'3'" value-sep="//"/>
</node>
```

<a id="parameter-grouping"></a>

#### Parameter grouping

In ROS 2, `param` tags are allowed to be nested.
For example:

```
<node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
   <param name="group1">
      <param name="group2">
         <param name="my_param" value="1"/>
      </param>
      <param name="another_param" value="2"/>
   </param>
</node>
```

That will create two parameters:

- A `group1.group2.my_param` of value `1`, hosted by node `/an_absolute_ns/my_node`.
- A `group1.another_param` of value `2` hosted by node `/an_absolute_ns/my_node`.

It’s also possible to use full parameter names:

```
<node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
   <param name="group1.group2.my_param" value="1"/>
   <param name="group1.another_param" value="2"/>
</node>
```

<a id="rosparam"></a>

### rosparam

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/rosparam).
- Loads parameters from a yaml file.
- It has been replaced with a `from` attribute in `param` tags.

<a id="id2"></a>

#### Example

```
<node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
   <param from="/path/to/file"/>
</node>
```

<a id="remap"></a>

### remap

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/remap).
- Used to pass remapping rules to a node.
- It can only be used within `node` tags.

<a id="id3"></a>

#### Example

```
<launch>
   <node pkg="demo_nodes_cpp" exec="talker">
      <remap from="chatter" to="my_topic"/>
   </node>
   <node pkg="demo_nodes_cpp" exec="listener">
      <remap from="chatter" to="my_topic"/>
   </node>
</launch>
```

<a id="include"></a>

### include

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/include).
- Allows including another launch file.
- Differences from ROS 1:

  > - Available in ROS 1, included content was scoped.
  >   In ROS 2, it’s not.
  >   This means the values of `arg` tags are propagated into included launch files as if `pass_all_args="true"` were used in ROS 1.
  >   However, this propagation only works for args that have a default value (in the inner/included launch file).
  >   Required args have to be passed explicitly.
  >   Nest includes in `group` tags to scope them (see also `group` attributes `scoped` and `forwarding` ).
  > - `ns` attribute is not supported.
  >   See example of `push_ros_namespace` tag for a workaround.
  > - `arg` tag nested in an `include` tag is now `let`.
  >   However, `arg` is still supported for now.
  > - `let` tags nested in an `include` tag don’t support conditionals (`if`, `unless`) or the `description` attribute.
  > - There is no support for nested `env` tags.
  >   `set_env` and `unset_env` can be used instead.
  > - Both `clear_params` and `pass_all_args` attributes aren’t supported.
  >   ROS 2 launch behaves as if `pass_all_args` were set to true (see above).

<a id="examples"></a>

#### Examples

See [Replacing an include tag](#replacing-an-include-tag).

<a id="arg"></a>

### arg

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/arg).
- `arg` is used for declaring a launch argument, or to pass an argument when using `include` tags.
- Differences from ROS 1:

  > - `value` attribute is not allowed.
  >   Use `let` tag for this.
  > - `doc` is now `description`.
  > - When nested within an `include` tag:
  >
  >   > - Use `let` instead of `arg`.
  >   > - `if`, `unless`, and `description` attributes aren’t allowed.

<a id="id4"></a>

#### Example

```
<launch>
   <arg name="topic_name" default="chatter"/>
   <node pkg="demo_nodes_cpp" exec="talker">
      <remap from="chatter" to="$(var topic_name)"/>
   </node>
   <node pkg="demo_nodes_cpp" exec="listener">
      <remap from="chatter" to="$(var topic_name)"/>
   </node>
</launch>
```

<a id="passing-an-argument-to-the-launch-file"></a>

#### Passing an argument to the launch file

In the XML launch file above, the `topic_name` defaults to the name `chatter`, but can be configured on the command-line.
Assuming the above launch configuration is in a file named `mylaunch.xml`, a different topic name can be used by launching it with the following:

```
$ ros2 launch mylaunch.xml topic_name:=custom_topic_name
```

There is some additional information about passing command-line arguments in [Using Substitutions](../../tutorials/intermediate/launch/using-substitutions.md).

<a id="env"></a>

### env

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/env).
- Sets an environment variable.
- It has been replaced with `env`, `set_env` and `unset_env`:

  > - `env` can only be used nested in a `node` or `executable` tag.
  >   `if` and `unless` tags aren’t supported.
  > - `set_env` can be nested within the root tag `launch` or in `group` tags.
  >   It accepts the same attributes as `env`, and also `if` and `unless` tags.
  > - `unset_env` unsets an environment variable.
  >   It accepts a `name` attribute and conditionals.

<a id="id5"></a>

#### Example

```
<launch>
   <set_env name="MY_ENV_VAR" value="MY_VALUE" if="CONDITION_A"/>
   <set_env name="ANOTHER_ENV_VAR" value="ANOTHER_VALUE" unless="CONDITION_B"/>
   <set_env name="SOME_ENV_VAR" value="SOME_VALUE"/>
   <node pkg="MY_PACKAGE" exec="MY_EXECUTABLE" name="MY_NODE">
      <env name="NODE_ENV_VAR" value="SOME_VALUE"/>
   </node>
   <unset_env name="MY_ENV_VAR" if="CONDITION_A"/>
   <node pkg="ANOTHER_PACKAGE" exec="ANOTHER_EXECUTABLE" name="ANOTHER_NODE"/>
   <unset_env name="ANOTHER_ENV_VAR" unless="CONDITION_B"/>
   <unset_env name="SOME_ENV_VAR"/>
</launch>
```

<a id="group"></a>

### group

- [Available in ROS 1](https://wiki.ros.org/roslaunch/XML/group).
- Allows limiting the scope of launch configurations.
  Usually used together with `let`, `include` and `push_ros_namespace` tags.
- Differences from ROS 1:

  > - There is no `ns` attribute.
  >   See the new `push_ros_namespace` tag as a workaround.
  > - `clear_params` attribute isn’t available.
  > - It doesn’t accept `remap` nor `param` tags as children.
  > - It has two new attributes: `scoped` and `forwarding` (both are true by default).
  >   If `scoped` is false, the group does not introduce a new variable scope, so actions done to variables inside the group also affect the outside variables.
  >   If `forwarding` is false, no outside launch configurations ( `arg` ) are available inside the group.
  >   This can be useful to isolate an included launch file and thus prevent collisions in argument names.

<a id="launch-prefix-example"></a>
<a id="id6"></a>

#### Example

`launch-prefix` configuration affects both `executable` and `node` tags’ actions.
This example will use `time` as a prefix if `use_time_prefix_in_talker` argument is `1`, only for the talker.

```
<launch>
   <arg name="use_time_prefix_in_talker" default="0"/>
   <group>
      <let name="launch-prefix" value="time" if="$(var use_time_prefix_in_talker)"/>
      <node pkg="demo_nodes_cpp" exec="talker"/>
   </group>
   <node pkg="demo_nodes_cpp" exec="listener"/>
</launch>
```

<a id="machine"></a>

### machine

It is not supported at the moment.

<a id="test"></a>

### test

It is not supported at the moment.

<a id="new-tags-in-ros-2"></a>

## New tags in ROS 2

<a id="set-env-and-unset-env"></a>

### set\_env and unset\_env

See [env](#env) tag description.

<a id="push-ros-namespace"></a>

### push\_ros\_namespace

`include` and `group` tags don’t accept an `ns` attribute.
This action can be used as a workaround:

```
<!-Other tags-->
<group>
   <push_ros_namespace namespace="my_ns"/>
   <!--Nodes here are namespaced with "my_ns".-->
   <!--If there is an include action here, its nodes will also be namespaced.-->
   <push_ros_namespace namespace="another_ns"/>
   <!--Nodes here are namespaced with "another_ns/my_ns".-->
   <push_ros_namespace namespace="/absolute_ns"/>
   <!--Nodes here are namespaced with "/absolute_ns".-->
   <!--The following node receives an absolute namespace, so it will ignore the others previously pushed.-->
   <!--The full path of the node will be /asd/my_node.-->
   <node pkg="my_pkg" exec="my_executable" name="my_node" namespace="/asd"/>
</group>
<!--Nodes outside the group action won't be namespaced.-->
<!-Other tags-->
```

<a id="let"></a>

### let

It’s a replacement of `arg` tag with a value attribute.

```
<let name="foo" value="asd"/>
```

`let` and `arg` serve two different purposes in ROS 2:

- `let` sets a launch configuration value.
- `arg` declares a launch argument/configuration and optionally provides a default value.
  The value can separately be set from the CLI or when including the given launch file.
  If no value is set, the default value is used if one was provided, otherwise an error is reported.

<a id="executable"></a>

### executable

It allows running any executable.

<a id="id7"></a>

#### Example

```
<executable cmd="ls -las" cwd="/var/log" name="my_exec" launch-prefix="something" output="screen" shell="true">
   <env name="LD_LIBRARY" value="/lib/some.so"/>
</executable>
```

<a id="replacing-an-include-tag"></a>

## Replacing an include tag

In order to include a launch file under a **namespace** as in ROS 1 then the `include` tags must be nested in a `group` tag.

```
<group>
   <include file="another_launch_file"/>
</group>
```

Then, instead of using the `ns` attribute, add the `push_ros_namespace` action tag to specify the namespace:

```
<group>
   <push_ros_namespace namespace="my_ns"/>
   <include file="another_launch_file"/>
</group>
```

Nesting `include` tags under a `group` tag is only required when specifying a namespace

<a id="substitutions"></a>

## Substitutions

Documentation about ROS 1’s substitutions can be found in [roslaunch XML wiki](https://wiki.ros.org/roslaunch/XML).
Substitutions syntax hasn’t changed, i.e. it still follows the `$(substitution-name arg1 arg2 ...)` pattern.
There are, however, some changes w.r.t. ROS 1:

- `env` and `optenv` tags have been replaced by the `env` tag.
  `$(env <NAME>)` will fail if the environment variable doesn’t exist.
  `$(env <NAME> '')` does the same as ROS 1’s `$(optenv <NAME>)`.
  `$(env <NAME> <DEFAULT>)` does the same as ROS 1’s `$(env <NAME> <DEFAULT>)` or `$(optenv <NAME> <DEFAULT>)`.
- `find` has been replaced with `find-pkg-share` (substituting the share directory of an installed package).
  Alternatively `find-pkg-prefix` will return the root of an installed package.
- There is a new `exec-in-pkg` substitution.
  e.g.: `$(exec-in-pkg <exec_name> <package_name>)`.
- There is a new `find-exec` substitution.
- `arg` has been replaced with `var`.
  It looks at configurations defined either with `arg` or `let` tag.
- `eval` and `dirname` substitutions require escape characters for string values, e.g. `if="$(eval '\'$(var variable)\' == \'val1\'')"`.
  You can also use HTML escapes like `&quot;` .
- Boolean predicates can also be expressed directly with the `equals`, `not-equals`, `and`, `or`, `any`, and `all` substitutions.
  For example, `if="$(equals $(var variable) val1)"` is equivalent to `if="$(eval '\'$(var variable)\' == \'val1\'')"`.
  See [Boolean substitutions](../../tutorials/intermediate/launch/using-substitutions.md#booleansubstitutions) for details.
- `eval` does not pass configurations ( `arg` ) as local Python variables.
  They have to be accessed via `$(var name)`.
- The argument of `eval` has to be a quoted string in ROS 2.
  That is also the reason why quotes inside the expression have to be escaped.

<a id="id8"></a>

## Type inference rules

The rules that were shown in `Type inference rules` subsection of `param` tag applies to any attribute.
For example:

```
<!--Setting a string value to an attribute expecting an int will raise an error.-->
<tag1 attr-expecting-an-int="'1'"/>
<!--Correct version.-->
<tag1 attr-expecting-an-int="1"/>
<!--Setting an integer in an attribute expecting a string will raise an error.-->
<tag2 attr-expecting-a-str="1"/>
<!--Correct version.-->
<tag2 attr-expecting-a-str="'1'"/>
<!--Setting a list of strings in an attribute expecting a string will raise an error.-->
<tag3 attr-expecting-a-str="asd, bsd" str-attr-sep=", "/>
<!--Correct version.-->
<tag3 attr-expecting-a-str="don't use a separator"/>
```

Some attributes accept more than a single type, for example `value` attribute of `param` tag.
It’s usual that parameters that are of type `int` (or `float`) also accept an `str`, that will be later substituted and tried to convert to an `int` (or `float`) by the action.
