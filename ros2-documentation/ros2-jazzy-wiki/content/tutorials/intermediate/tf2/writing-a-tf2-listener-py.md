---
title: "Writing a listener (Python)"
docname: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Py"
source: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Py.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](adding-a-frame-cpp.md) | [Adding a frame (Python)](adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-a-listener-python"></a>

# Writing a listener (Python)

**Goal:** Learn how to use tf2 to get access to frame transformations.

**Tutorial level:** Intermediate

**Time:** 10 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Write the listener node](#write-the-listener-node)
  - [2 Update the launch file](#update-the-launch-file)
  - [3 Build](#build)
  - [4 Run](#run)
- [Summary](#summary)

<a id="background"></a>

## Background

In previous tutorials we created a tf2 broadcaster to publish the pose of a turtle to tf2.

In this tutorial we’ll create a tf2 listener to start using tf2.

<a id="prerequisites"></a>

## Prerequisites

This tutorial assumes you have completed the [tf2 static broadcaster tutorial (Python)](writing-a-tf2-static-broadcaster-py.md) and [tf2 broadcaster tutorial (Python)](writing-a-tf2-broadcaster-py.md).
In the previous tutorial, we created a `learning_tf2_py` package, which is where we will continue working from.

<a id="tasks"></a>

## Tasks

<a id="write-the-listener-node"></a>

### 1 Write the listener node

Let’s first create the source files.
Go to the `learning_tf2_py` package we created in the previous tutorial.
Inside the `src/learning_tf2_py/learning_tf2_py` directory download the example listener code by entering the following command:

Linux

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py
```

macOS

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py
```

Windows

In a Windows command line prompt:

```
$ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py -o turtle_tf2_listener.py
```

Or in powershell:

```
$ curl https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py -o turtle_tf2_listener.py
```

Now open the file called `turtle_tf2_listener.py` using your preferred text editor.

```
import math

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from turtlesim.srv import Spawn

class FrameListener(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

        # Declare and acquire `target_frame` parameter
        self.target_frame = self.declare_parameter(
          'target_frame', 'turtle1').get_parameter_value().string_value

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Create a client to spawn a turtle
        self.spawner = self.create_client(Spawn, 'spawn')
        # Boolean values to store the information
        # if the service for spawning turtle is available
        self.turtle_spawning_service_ready = False
        # if the turtle was successfully spawned
        self.turtle_spawned = False

        # Create turtle2 velocity publisher
        self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 1)

        # Call on_timer function every second
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        # Store frame names in variables that will be used to
        # compute transformations
        from_frame_rel = self.target_frame
        to_frame_rel = 'turtle2'

        if self.turtle_spawning_service_ready:
            if self.turtle_spawned:
                # Look up for the transformation between target_frame and turtle2 frames
                # and send velocity commands for turtle2 to reach target_frame
                try:
                    t = self.tf_buffer.lookup_transform(
                        to_frame_rel,
                        from_frame_rel,
                        rclpy.time.Time())
                except TransformException as ex:
                    self.get_logger().info(
                        f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
                    return

                msg = Twist()
                scale_rotation_rate = 1.0
                msg.angular.z = scale_rotation_rate * math.atan2(
                    t.transform.translation.y,
                    t.transform.translation.x)

                scale_forward_speed = 0.5
                msg.linear.x = scale_forward_speed * math.sqrt(
                    t.transform.translation.x ** 2 +
                    t.transform.translation.y ** 2)

                self.publisher.publish(msg)
            else:
                if self.result.done():
                    self.get_logger().info(
                        f'Successfully spawned {self.result.result().name}')
                    self.turtle_spawned = True
                else:
                    self.get_logger().info('Spawn is not finished')
        else:
            if self.spawner.service_is_ready():
                # Initialize request with turtle name and coordinates
                # Note that x, y and theta are defined as floats in turtlesim/srv/Spawn
                request = Spawn.Request()
                request.name = 'turtle2'
                request.x = float(4)
                request.y = float(2)
                request.theta = float(0)
                # Call request
                self.result = self.spawner.call_async(request)
                self.turtle_spawning_service_ready = True
            else:
                # Check if the service is ready
                self.get_logger().info('Service is not ready')

def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
```

<a id="examine-the-code"></a>

#### 1.1 Examine the code

To understand how the service behind spawning turtle works, please refer to [writing a simple service and client (Python)](../../beginner-client-libraries/writing-a-simple-py-service-and-client.md) tutorial.

Now, let’s take a look at the code that is relevant to get access to frame transformations.
The `tf2_ros` package provides an implementation of a `TransformListener` to help make the task of receiving transforms easier.

```
from tf2_ros.transform_listener import TransformListener
```

Here, we create a `TransformListener` object.
Once the listener is created, it starts receiving tf2 transformations over the wire, and buffers them for up to 10 seconds.

```
self.tf_listener = TransformListener(self.tf_buffer, self)
```

Finally, we query the listener for a specific transformation.
We call `lookup_transform` method with following arguments:

1. Target frame
2. Source frame
3. The time at which we want to transform

Providing `rclpy.time.Time()` will just get us the latest available transform.
All this is wrapped in a try-except block to handle possible exceptions.

```
t = self.tf_buffer.lookup_transform(
    to_frame_rel,
    from_frame_rel,
    rclpy.time.Time())
```

<a id="add-an-entry-point"></a>

#### 1.2 Add an entry point

To allow the `ros2 run` command to run your node, you must add the entry point to `setup.py` (located in the `src/learning_tf2_py` directory).

Add the following line between the `'console_scripts':` brackets:

```
'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
```

<a id="update-the-launch-file"></a>

### 2 Update the launch file

Open the launch file called `turtle_tf2_demo_launch` with extension `.py`, `.xml`, or `.yaml` in the `src/learning_tf2_py/launch` directory with your text editor, add two new nodes to the launch description, add a launch argument, and add the imports.
The resulting file should look like:

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" />
  <node pkg="learning_tf2_py" exec="turtle_tf2_broadcaster" name="broadcaster1">
    <param name="turtlename" value="turtle1" />
  </node>
  <arg name="target_frame" default="turtle1" description="Target frame name." />
  <node pkg="learning_tf2_py" exec="turtle_tf2_broadcaster" name="broadcaster2">
    <param name="turtlename" value="turtle2" />
  </node>
  <node pkg="learning_tf2_py" exec="turtle_tf2_listener" name="listener">
    <param name="target_frame" value="$(var target_frame)" />
  </node>
</launch>
```

YAML

```
%YAML 1.2
---
launch:
  - node:
      pkg: "turtlesim"
      exec: "turtlesim_node"
      name: "sim"
  - node:
      pkg: "learning_tf2_py"
      exec: "turtle_tf2_broadcaster"
      name: "broadcaster1"
      param:
      - name: "turtlename"
        value: "turtle1"
  - arg:
      name: "target_frame"
      default: "turtle1"
      description: "Target frame name."
  - node:
      pkg: "learning_tf2_py"
      exec: "turtle_tf2_broadcaster"
      name: "broadcaster2"
      param:
      - name: "turtlename"
        value: "turtle2"
  - node:
      pkg: "learning_tf2_py"
      exec: "turtle_tf2_listener"
      name: "listener"
      param:
      - name: "target_frame"
        value: "$(var target_frame)"
```

Python

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])
```

This will declare a `target_frame` launch argument, start a broadcaster for second turtle that we will spawn and listener that will subscribe to those transformations.

<a id="build"></a>

### 3 Build

Run `rosdep` in the root of your workspace to check for missing dependencies.

Linux

```
$ rosdep install -i --from-path src --rosdistro jazzy -y
```

macOS

rosdep only runs on Linux, so you will need to install `geometry_msgs` and `turtlesim` dependencies yourself

Windows

rosdep only runs on Linux, so you will need to install `geometry_msgs` and `turtlesim` dependencies yourself

Still in the root of your workspace, build your package:

Linux

```
$ colcon build --packages-select learning_tf2_py
```

macOS

```
$ colcon build --packages-select learning_tf2_py
```

Windows

```
$ colcon build --merge-install --packages-select learning_tf2_py
```

Open a new terminal, navigate to the root of your workspace, and source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

In a Windows command line prompt:

```
$ call install\setup.bat
```

Or in powershell:

```
$ .\install\setup.ps1
```

<a id="run"></a>

### 4 Run

Now you’re ready to start your full turtle demo:

XML

```
$ ros2 launch learning_tf2_py turtle_tf2_demo_launch.xml
```

YAML

```
$ ros2 launch learning_tf2_py turtle_tf2_demo_launch.yaml
```

Python

```
$ ros2 launch learning_tf2_py turtle_tf2_demo_launch.py
```

You should see the turtle sim with two turtles.
In the second terminal window type the following command:

```
$ ros2 run turtlesim turtle_teleop_key
```

To see if things work, simply drive around the first turtle using the arrow keys (make sure your terminal window is active, not your simulator window), and you’ll see the second turtle following the first one!

<a id="summary"></a>

## Summary

In this tutorial you learned how to use tf2 to get access to frame transformations.
You also have finished writing your own turtlesim demo that you first tried in [Introduction to tf2](introduction-to-tf2.md) tutorial.
