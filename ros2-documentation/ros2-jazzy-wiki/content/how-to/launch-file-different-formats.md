---
title: "Using XML, YAML, and Python for ROS 2 Launch Files"
docname: "How-To-Guides/Launch-file-different-formats"
source: "How-To-Guides/Launch-file-different-formats.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="using-xml-yaml-and-python-for-ros-2-launch-files"></a>

# Using XML, YAML, and Python for ROS 2 Launch Files

Table of Contents

- [Launch file examples](#launch-file-examples)
- [Using the Launch files from the command line](#using-the-launch-files-from-the-command-line)

  - [Launching](#launching)
  - [Setting arguments](#setting-arguments)
  - [Controlling the turtles](#controlling-the-turtles)
- [XML, YAML, or Python: Which should I use?](#xml-yaml-or-python-which-should-i-use)

ROS 2 launch files can be written in XML, YAML, and Python.
This guide shows how to use these different formats to accomplish the same task, as well as has some discussion on when to use each format.

<a id="launch-file-examples"></a>

## Launch file examples

Below is a launch file implemented in XML, YAML, and Python.
Each launch file performs the following actions:

- Setup command line arguments with defaults
- Include another launch file
- Include another launch file in another namespace
- Start a node and setting its namespace
- Start a node, setting its namespace, and setting parameters in that node (using the args)
- Create a node to remap messages from one topic to another

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <!-- args that can be set from the command line or a default will be used -->
  <arg name="background_r" default="0" />
  <arg name="background_g" default="255" />
  <arg name="background_b" default="0" />
  <arg name="chatter_py_ns" default="chatter/py/ns" />
  <arg name="chatter_xml_ns" default="chatter/xml/ns" />
  <arg name="chatter_yaml_ns" default="chatter/yaml/ns" />

  <!-- include another launch file -->
  <include file="$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.py" />

  <!-- include a Python launch file in the chatter_py_ns namespace-->
  <group>
    <!-- push_ros_namespace to set namespace of included nodes -->
    <push_ros_namespace namespace="$(var chatter_py_ns)" />
    <include file="$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.py" />
  </group>

  <!-- include a xml launch file in the chatter_xml_ns namespace-->
  <group>
    <!-- push_ros_namespace to set namespace of included nodes -->
    <push_ros_namespace namespace="$(var chatter_xml_ns)" />
    <include file="$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.xml" />
  </group>

  <!-- include a yaml launch file in the chatter_yaml_ns namespace-->
  <group>
    <!-- push_ros_namespace to set namespace of included nodes -->
    <push_ros_namespace namespace="$(var chatter_yaml_ns)" />
    <include file="$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.yaml" />
  </group>

  <!-- start a turtlesim_node in the turtlesim1 namespace and use args to set the log level -->
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" namespace="turtlesim1" args="--ros-args --log-level info" />

  <!-- start another turtlesim_node in the turtlesim2 namespace, use ros_args to set the log level, and child elements to set the parameters -->
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" namespace="turtlesim2" ros_args="--log-level warn">
    <param name="background_r" value="$(var background_r)" />
    <param name="background_g" value="$(var background_g)" />
    <param name="background_b" value="$(var background_b)" />
  </node>

  <!-- perform remap so both turtles listen to the same command topic -->
  <node pkg="turtlesim" exec="mimic" name="mimic">
    <remap from="/input/pose" to="/turtlesim1/turtle1/pose" />
    <remap from="/output/cmd_vel" to="/turtlesim2/turtle1/cmd_vel" />
  </node>
</launch>
```

YAML

```
%YAML 1.2
---
launch:
# args that can be set from the command line or a default will be used
- arg:
    name: "background_r"
    default: "0"
- arg:
    name: "background_g"
    default: "255"
- arg:
    name: "background_b"
    default: "0"
- arg:
    name: "chatter_py_ns"
    default: "chatter/py/ns"
- arg:
    name: "chatter_xml_ns"
    default: "chatter/xml/ns"
- arg:
    name: "chatter_yaml_ns"
    default: "chatter/yaml/ns"

# include another launch file
- include:
    file: "$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.py"

# include a Python launch file in the chatter_py_ns namespace
- group:
    - push_ros_namespace:
        namespace: "$(var chatter_py_ns)"
    - include:
        file: "$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.py"

# include a xml launch file in the chatter_xml_ns namespace
- group:
    - push_ros_namespace:
        namespace: "$(var chatter_xml_ns)"
    - include:
        file: "$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.xml"

# include a yaml launch file in the chatter_yaml_ns namespace
- group:
    - push_ros_namespace:
        namespace: "$(var chatter_yaml_ns)"
    - include:
        file: "$(find-pkg-share demo_nodes_cpp)/launch/topics/talker_listener_launch.yaml"

# start a turtlesim_node in the turtlesim1 namespace and use args to set the log level
- node:
    pkg: "turtlesim"
    exec: "turtlesim_node"
    name: "sim"
    namespace: "turtlesim1"
    args: "--ros-args --log-level info"

# start another turtlesim_node in the turtlesim2 namespace, use ros_args to set the log level, and param to set the parameters
- node:
    pkg: "turtlesim"
    exec: "turtlesim_node"
    name: "sim"
    namespace: "turtlesim2"
    ros_args: "--log-level warn"
    param:
    - name: "background_r"
      value: "$(var background_r)"
    - name: "background_g"
      value: "$(var background_g)"
    - name: "background_b"
      value: "$(var background_b)"

# perform remap so both turtles listen to the same command topic
- node:
    pkg: "turtlesim"
    exec: "mimic"
    name: "mimic"
    remap:
    - from: "/input/pose"
      to: "/turtlesim1/turtle1/pose"
    - from: "/output/cmd_vel"
      to: "/turtlesim2/turtle1/cmd_vel"
```

Python

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node, PushROSNamespace
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    launch_dir = PathJoinSubstitution([FindPackageShare('demo_nodes_cpp'), 'launch', 'topics'])
    return LaunchDescription([
        # args that can be set from the command line or a default will be used
        DeclareLaunchArgument('background_r', default_value='0'),
        DeclareLaunchArgument('background_g', default_value='255'),
        DeclareLaunchArgument('background_b', default_value='0'),
        DeclareLaunchArgument('chatter_py_ns', default_value='chatter/py/ns'),
        DeclareLaunchArgument('chatter_xml_ns', default_value='chatter/xml/ns'),
        DeclareLaunchArgument('chatter_yaml_ns', default_value='chatter/yaml/ns'),

        # include another launch file
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'talker_listener_launch.py'])
        ),

        # include a Python launch file in the chatter_py_ns namespace
        GroupAction(
            actions=[
                # push_ros_namespace first to set namespace of included nodes for following actions
                PushROSNamespace('chatter_py_ns'),
                IncludeLaunchDescription(
                    PathJoinSubstitution([launch_dir, 'talker_listener_launch.py'])),
            ]
        ),

        # include a xml launch file in the chatter_xml_ns namespace
        GroupAction(
            actions=[
                # push_ros_namespace first to set namespace of included nodes for following actions
                PushROSNamespace('chatter_xml_ns'),
                IncludeLaunchDescription(
                    PathJoinSubstitution([launch_dir, 'talker_listener_launch.xml'])),
            ]
        ),

        # include a yaml launch file in the chatter_yaml_ns namespace
        GroupAction(
            actions=[
                # push_ros_namespace first to set namespace of included nodes for following actions
                PushROSNamespace('chatter_yaml_ns'),
                IncludeLaunchDescription(
                    PathJoinSubstitution([launch_dir, 'talker_listener_launch.yaml'])),
            ]
        ),

        # start a turtlesim_node in the turtlesim1 namespace and use arguments to set the log level
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim',
            arguments=['--ros-args', '--log-level', 'info']
        ),

        # start another turtlesim_node in the turtlesim2 namespace,
        # use ros_arguments to set the log level, and parameters to set the parameters
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim',
            ros_arguments=['--log-level', 'warn'],
            parameters=[{
                'background_r': LaunchConfiguration('background_r'),
                'background_g': LaunchConfiguration('background_g'),
                'background_b': LaunchConfiguration('background_b'),
            }]
        ),

        # perform remap so both turtles listen to the same command topic
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        ),
    ])
```

<a id="using-the-launch-files-from-the-command-line"></a>

## Using the Launch files from the command line

<a id="launching"></a>

### Launching

Any of the launch files above can be run with `ros2 launch`.
To try them locally, you can either create a new package and use

```
$ ros2 launch <package_name> <launch_file_name>
```

or run the file directly by specifying the path to the launch file

```
$ ros2 launch <path_to_launch_file>
```

<a id="setting-arguments"></a>

### Setting arguments

To set the arguments that are passed to the launch file, you should use `key:=value` syntax.
For example, you can set the value of `background_r` in the following way:

```
$ ros2 launch <package_name> <launch_file_name> background_r:=255
```

or

```
$ ros2 launch <path_to_launch_file> background_r:=255
```

<a id="controlling-the-turtles"></a>

### Controlling the turtles

To test that the remapping is working, you can control the turtles by running the following command in another terminal:

```
$ ros2 run turtlesim turtle_teleop_key --ros-args --remap __ns:=/turtlesim1
```

<a id="xml-yaml-or-python-which-should-i-use"></a>
<a id="launch-file-different-formats-which"></a>

## XML, YAML, or Python: Which should I use?

> [!NOTE]
>
> Launch files in ROS 1 were written in XML, so XML may be the most familiar to people coming from ROS 1.
> To see what’s changed, you can visit [Migrating Launch Files](migrating-from-ros1/migrating-launch-files.md).

For most applications the choice of which ROS 2 launch format comes down to developer preference.
However, if your launch file requires flexibility that you cannot achieve with XML or YAML, you can use Python to write your launch file.
Using Python for ROS 2 launch is more flexible because of following two reasons:

- Python is a scripting language, and thus you can leverage the language and its libraries in your launch files.
- [ros2/launch](https://github.com/ros2/launch) (general launch features) and [ros2/launch\_ros](https://github.com/ros2/launch_ros) (ROS 2 specific launch features) are written in Python and thus you have lower level access to launch features that may not be exposed by XML and YAML.

That being said, a launch file written in Python may be more complex and verbose than one in XML or YAML.
