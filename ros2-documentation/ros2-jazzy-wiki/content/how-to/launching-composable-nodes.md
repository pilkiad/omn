---
title: "Using ROS 2 launch to launch composable nodes"
docname: "How-To-Guides/Launching-composable-nodes"
source: "How-To-Guides/Launching-composable-nodes.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="using-ros-2-launch-to-launch-composable-nodes"></a>

# Using ROS 2 launch to launch composable nodes

Table of Contents

- [Setup](#setup)
- [Launch file examples](#launch-file-examples)
- [Loading composable nodes into an existing container](#loading-composable-nodes-into-an-existing-container)
- [Using the Launch files from the command-line](#using-the-launch-files-from-the-command-line)
- [Intra-process communications](#intra-process-communications)
- [XML, YAML, or Python: Which should I use?](#xml-yaml-or-python-which-should-i-use)

In the [Composition tutorial](../tutorials/intermediate/composition.md), you learned about composable nodes and how to use them from the command-line.
In the [Launch tutorials](../tutorials/intermediate/launch/launch-main.md), you learned about launch files and how to use them to manage multiple nodes.

This guide will combine the above two topics and teach you how to write launch files for composable nodes.

<a id="setup"></a>

## Setup

See the [installation instructions](../installation/overview.md) for details on installing ROS 2.

If you’ve installed ROS 2 from packages, ensure that you have `ros-jazzy-image-tools` installed.
If you downloaded the archive or built ROS 2 from source, it will already be part of the installation.

<a id="launch-file-examples"></a>

## Launch file examples

Below is a launch file that launches composable nodes in XML, YAML, and Python.
The launch files all do the following:

- Instantiate a cam2image composable node with remappings, custom parameters, and extra arguments
- Instantiate a showimage composable node with remappings, custom parameters, and extra arguments

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node_container pkg="rclcpp_components" exec="component_container" name="image_container" namespace="">
    <composable_node pkg="image_tools" plugin="image_tools::Cam2Image" name="cam2image">
      <remap from="/image" to="/burgerimage" />
      <param name="width" value="320" />
      <param name="height" value="240" />
      <param name="burger_mode" value="true" />
      <param name="history" value="keep_last" />
      <extra_arg name="use_intra_process_comms" value="true" />
    </composable_node>
    <composable_node pkg="image_tools" plugin="image_tools::ShowImage" name="showimage">
      <remap from="/image" to="/burgerimage" />
      <param name="history" value="keep_last" />
      <extra_arg name="use_intra_process_comms" value="true" />
    </composable_node>
  </node_container>
</launch>
```

YAML

```
%YAML 1.2
---
launch:
  - node_container:
      pkg: rclcpp_components
      exec: component_container
      name: image_container
      composable_node:
        - pkg: image_tools
          plugin: image_tools::Cam2Image
          name: cam2image
          remap:
            - from: /image
              to: /burgerimage
          param:
            - name: width
              value: 320
            - name: height
              value: 240
            - name: burger_mode
              value: true
            - name: history
              value: keep_last
          extra_arg:
            - name: use_intra_process_comms
              value: true

        - pkg: image_tools
          plugin: image_tools::ShowImage
          name: showimage
          remap:
            - from: /image
              to: /burgerimage
          param:
            - name: history
              value: keep_last
          extra_arg:
            - name: use_intra_process_comms
              value: true
```

Python

```
import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    """Generate launch description with multiple components."""
    return launch.LaunchDescription([
        ComposableNodeContainer(
            name='image_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='image_tools',
                    plugin='image_tools::Cam2Image',
                    name='cam2image',
                    remappings=[('/image', '/burgerimage')],
                    parameters=[{
                        'width': 320,
                        'height': 240,
                        'burger_mode': True,
                        'history': 'keep_last'}],
                    extra_arguments=[{'use_intra_process_comms': True}]),
                ComposableNode(
                    package='image_tools',
                    plugin='image_tools::ShowImage',
                    name='showimage',
                    remappings=[('/image', '/burgerimage')],
                    parameters=[{'history': 'keep_last'}],
                    extra_arguments=[{'use_intra_process_comms': True}])
            ],
            output='both',
        ),
    ])
```

<a id="loading-composable-nodes-into-an-existing-container"></a>

## Loading composable nodes into an existing container

Containers can sometimes be launched by other launch files or from a commandline.
In that case, you need to add your components to an existing container.
For this, you may use `LoadComposableNodes` to load components into a given container.
The below example launches the same nodes as above.

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="rclcpp_components" exec="component_container" name="image_container" />
  <load_composable_node target="image_container">
    <composable_node pkg="image_tools" plugin="image_tools::Cam2Image" name="cam2image">
      <remap from="/image" to="/burgerimage" />
      <param name="width" value="320" />
      <param name="height" value="240" />
      <param name="burger_mode" value="true" />
      <param name="history" value="keep_last" />
      <extra_arg name="use_intra_process_comms" value="true" />
    </composable_node>
    <composable_node pkg="image_tools" plugin="image_tools::ShowImage" name="showimage" namespace="">
      <remap from="/image" to="/burgerimage" />
      <param name="history" value="keep_last" />
      <extra_arg name="use_intra_process_comms" value="true" />
    </composable_node>
  </load_composable_node>
</launch>
```

YAML

```
%YAML 1.2
---
launch:
  - node_container:
      pkg: rclcpp_components
      exec: component_container
      name: image_container
  - load_composable_node:
      target: "image_container"
      composable_node:
        - pkg: image_tools
          plugin: image_tools::Cam2Image
          name: cam2image
          remap:
            - from: /image
              to: /burgerimage
          param:
            - name: width
              value: 320
            - name: height
              value: 240
            - name: burger_mode
              value: true
            - name: history
              value: keep_last
          extra_arg:
            - name: use_intra_process_comms
              value: true

        - pkg: image_tools
          plugin: image_tools::ShowImage
          name: showimage
          remap:
            - from: /image
              to: /burgerimage
          param:
            - name: history
              value: keep_last
          extra_arg:
            - name: use_intra_process_comms
              value: true
```

Python

```
from launch import LaunchDescription
from launch_ros.actions import LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    return LaunchDescription([
        Node(
            name='image_container',
            package='rclcpp_components',
            executable='component_container',
            output='both',
        ),
        LoadComposableNodes(
            target_container='image_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='image_tools',
                    plugin='image_tools::Cam2Image',
                    name='cam2image',
                    remappings=[('/image', '/burgerimage')],
                    parameters=[
                        {'width': 320, 'height': 240, 'burger_mode': True, 'history': 'keep_last'}
                    ],
                    extra_arguments=[{'use_intra_process_comms': True}],
                ),
                ComposableNode(
                    package='image_tools',
                    plugin='image_tools::ShowImage',
                    name='showimage',
                    remappings=[('/image', '/burgerimage')],
                    parameters=[{'history': 'keep_last'}],
                    extra_arguments=[{'use_intra_process_comms': True}]
                ),
            ],
        )
    ])
```

<a id="using-the-launch-files-from-the-command-line"></a>

## Using the Launch files from the command-line

Any of the launch files above can be run with `ros2 launch`.
Copy the data into a local file, and then run:

```
$ ros2 launch <path_to_launch_file>
```

<a id="intra-process-communications"></a>

## Intra-process communications

All of the above examples use an extra argument to setup intra-process communication between the nodes.
For more information on what intra-process communications are, see the [intra-process comms tutorial](../tutorials/demos/intra-process-communication.md).

<a id="xml-yaml-or-python-which-should-i-use"></a>

## XML, YAML, or Python: Which should I use?

See the [discussion](launch-file-different-formats.md#launch-file-different-formats-which) in [Using XML, YAML, and Python for ROS 2 Launch Files](launch-file-different-formats.md) for more information.
