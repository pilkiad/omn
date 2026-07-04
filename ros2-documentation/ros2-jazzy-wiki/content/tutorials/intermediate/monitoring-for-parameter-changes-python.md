---
title: "Monitoring for parameter changes (Python)"
docname: "Tutorials/Intermediate/Monitoring-For-Parameter-Changes-Python"
source: "Tutorials/Intermediate/Monitoring-For-Parameter-Changes-Python.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="monitoring-for-parameter-changes-python"></a>

# Monitoring for parameter changes (Python)

**Goal:** Learn to use the ParameterEventHandler class to monitor and respond to parameter changes.

**Tutorial level:** Intermediate

**Time:** 20 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a package](#create-a-package)
  - [2 Write the Python node](#write-the-python-node)
  - [3 Build and run](#build-and-run)
- [Extensions](#extensions)

  - [Monitor changes to another node’s parameters](#monitor-changes-to-another-node-s-parameters)
  - [Monitor all node parameters simultaneously](#monitor-all-node-parameters-simultaneously)
- [Summary](#summary)
- [Related content](#related-content)

<a id="background"></a>

## Background

Often a node needs to respond to changes to its own parameters or another node’s parameters.
The ParameterEventHandler class makes it easy to listen for parameter changes so that your code can respond to them.
This tutorial will show you how to use the Python version of the ParameterEventHandler class to monitor for changes to a node’s own parameters as well as changes to another node’s parameters.

<a id="prerequisites"></a>

## Prerequisites

Before starting this tutorial, you should first complete the following tutorials:

- [Understanding parameters](../beginner-cli-tools/understanding-ros2-parameters.md)
- [Using parameters in a class (Python)](../beginner-client-libraries/using-parameters-in-a-class-python.md)

<a id="tasks"></a>

## Tasks

In this tutorial, you will create a new package to contain some sample code, write some Python code to use the ParameterEventHandler class, and test the resulting code.

<a id="create-a-package"></a>

### 1 Create a package

First, open a new terminal and [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md) so that `ros2` commands will work.

Follow [these instructions](../beginner-client-libraries/creating-a-workspace.md#new-directory) to create a new workspace named `ros2_ws`.

Recall that packages should be created in the `src` directory, not the root of the workspace.
So, navigate into `ros2_ws/src` and then create a new package there:

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 python_parameter_event_handler --dependencies rclpy
```

Your terminal will return a message verifying the creation of your package `python_parameter_event_handler` and all its necessary files and folders.

The `--dependencies` argument will automatically add the necessary dependency lines to `package.xml` and `CMakeLists.txt`.

<a id="update-package-xml"></a>

#### 1.1 Update `package.xml`

Because you used the `--dependencies` option during package creation, you don’t have to manually add dependencies to `package.xml`.
As always, though, make sure to add the description, maintainer email and name, and license information to `package.xml`.

```
<description>Python parameter events client tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

<a id="write-the-python-node"></a>

### 2 Write the Python node

Inside the `ros2_ws/src/python_parameter_event_handler/python_parameter_event_handler` directory, create a new file called `parameter_event_handler.py` and paste the following code within:

```
import rclpy
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler

class SampleNodeWithParameters(Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        self.declare_parameter('an_int_param', 0)

        self.handler = ParameterEventHandler(self)

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name="node_with_parameters",
            callback=self.callback,
        )

    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")

def main():
    rclpy.init()
    node = SampleNodeWithParameters()
    rclpy.spin(node)
    rclpy.shutdown()
```

<a id="examine-the-code"></a>

#### 2.1 Examine the code

The `import` statements at the top are used to import the package dependencies.

```
import rclpy
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler
```

The next piece of code creates the class `SampleNodeWithParameters` and the constructor.
The constructor for the class declares an integer parameter `an_int_param`, with a default value of 0.
Next, the code creates a `ParameterEventHandler` that will be used to monitor changes to parameters.

```
class SampleNodeWithParameters(Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        self.declare_parameter('an_int_param', 0)

        self.handler = ParameterEventHandler(self)
```

Finally, we add a parameter callback and get a callback handler for the new callback.

> [!NOTE]
>
> It is very important to save the handle that is returned by `add_parameter_callback`; otherwise, the callback will not be properly registered.

```
self.callback_handle = self.handler.add_parameter_callback(
    parameter_name="an_int_param",
    node_name="node_with_parameters",
    callback=self.callback,
)
```

For the callback function, we use the `callback` method of the `SampleNodeWithParameters` class.

```
def callback(self, p: rclpy.parameter.Parameter) -> None:
    self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")
```

Following the `SampleNodeWithParameters` is a typical `main` function which initializes ROS, spins the sample node so that it can send and receive messages, and then shuts down after the user enters ^C at the console.

```
def main():
    rclpy.init()
    node = SampleNodeWithParameters()
    rclpy.spin(node)
    rclpy.shutdown()
```

<a id="add-an-entry-point"></a>

#### 2.2 Add an entry point

Open the `setup.py` file.
Again, match the `maintainer`, `maintainer_email`, `description` and `license` fields to your `package.xml`:

```
maintainer='YourName',
maintainer_email='you@email.com',
description='Python parameter tutorial',
license='Apache-2.0',
```

Add the following line within the `console_scripts` brackets of the `entry_points` field:

```
entry_points={
    'console_scripts': [
        'node_with_parameters = python_parameter_event_handler.parameter_event_handler:main',
    ],
},
```

<a id="build-and-run"></a>

### 3 Build and run

It’s good practice to run `rosdep` in the root of your workspace (`ros2_ws`) to check for missing dependencies before building:

Linux

```
$ rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
```

macOS

rosdep only runs on Linux, so you can skip ahead to next step.

Windows

rosdep only runs on Linux, so you can skip ahead to next step.

Navigate back to the root of your workspace, `ros2_ws`, and build your new package:

```
$ colcon build --packages-select python_parameter_event_handler
```

Open a new terminal, navigate to `ros2_ws`, and source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install\setup.bat
```

Now run the node:

```
$ ros2 run python_parameter_event_handler node_with_parameters
```

The node is now active and has a single parameter and will print a message whenever this parameter is updated.
To test this, open up another terminal and source the ROS setup file as before and execute the following command:

```
$ ros2 param set node_with_parameters an_int_param 43
```

The terminal running the node will display a message similar to the following:

```
[INFO] [1698483083.315084660] [node_with_parameters]: Received an update to parameter: an_int_param: 43
```

The callback we set previously in the node has been invoked and has displayed the new updated value.
You can now terminate the running parameter\_event\_handler sample using ^C in the terminal.

<a id="extensions"></a>

## Extensions

So far, we built and tested a small node that monitors a single parameter owned by the node itself.
Using this node as a base, two other usecases where the ParameterEventHandler can be useful are presented below.

<a id="monitor-changes-to-another-node-s-parameters"></a>

### Monitor changes to another node’s parameters

You can also use the ParameterEventHandler to monitor parameter changes to another node’s parameters.
Let’s update the SampleNodeWithParameters class to monitor for changes to a parameter in another node.
We will use the parameter\_blackboard demo application to host a double parameter that we will monitor for updates.

First update the constructor to add the following code after the existing code:

```
def __init__(...):
    ...
    self.callback_handle2 = self.handler.add_parameter_callback(
        parameter_name="a_double_param",
        node_name="parameter_blackboard",
        callback=self.callback,
    )
```

In a terminal, navigate back to the root of your workspace, `ros2_ws`, and build your updated package as before:

```
$ colcon build --packages-select python_parameter_event_handler
```

Then source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install\setup.bat
```

Now, to test monitoring of remote parameters, first run the newly-built parameter\_event\_handler code:

```
$ ros2 run python_parameter_event_handler node_with_parameters
```

Next, from another terminal (with ROS initialized), run the parameter\_blackboard demo application, as follows:

```
$ ros2 run demo_nodes_cpp parameter_blackboard
```

Finally, from a third terminal (with ROS initialized), let’s set a parameter on the parameter\_blackboard node:

```
$ ros2 param set parameter_blackboard a_double_param 3.45
```

Upon executing this command, you should see output in the parameter\_event\_handler window, indicating that the callback function was invoked upon the parameter update:

```
[INFO] [1699821958.757770223] [node_with_parameters]: Received an update to parameter: a_double_param: 3.45
```

<a id="monitor-all-node-parameters-simultaneously"></a>

### Monitor all node parameters simultaneously

If you need to monitor multiple nodes or parameters at the same time, it would be cumbersome to have to call `add_parameter_callback` once for each of them.
In this case, you can use `add_parameter_event_callback` to register a single callback that fires when *any* parameters of *any* nodes change.

To do this, first update the SampleNodeWithParameters constructor to add the following code:

```
def __init__(...):
    self.declare_parameter("another_double_param", 0.0)
    ...
    self.event_calback_handle = self.handler.add_parameter_event_callback(
        callback=self.event_callback,
    )
```

This declares a new double parameter `another_double_param` and adds an event callback that will monitor both parameters.
The event callback signature is different from that of regular single-parameter callbacks, so we need to define a suitable callback as well:

```
def event_callback(self, parameter_event):
    self.get_logger().info(f"Received parameter event from node {parameter_event.node}")

    for p in parameter_event.changed_parameters:
        self.get_logger().info(
            f"Inside event: {p.name} changed to: {rclpy.parameter.parameter_value_to_python(p.value)}"
        )
```

Note that the `parameter_event` is of type [rcl\_interfaces/msg/ParameterEvent](https://docs.ros.org/en/jazzy/p/rcl_interfaces/msg/ParameterEvent.html).
Although it’s not shown in this tutorial, event callbacks can also be used to monitor when parameters are added or deleted.

Navigate back to the root of your workspace, `ros2_ws`, and rebuild your updated package as before:

```
$ colcon build --packages-select python_parameter_event_handler
```

Then source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install\setup.bat
```

To test the new event callback, first run the parameter\_event\_handler node:

```
$ ros2 run python_parameter_event_handler node_with_parameters
```

Then, from a second terminal (with ROS sourced), let’s set the original int parameter:

```
$ ros2 param set node_with_parameters an_int_param 44
```

Upon executing this command, you should see both the single-parameter callback, as well as the event callback being fired:

```
[INFO] [1746414766.240101027] [node_with_parameters]: Received an update to parameter: an_int_param: 44
[INFO] [1746414766.243499816] [node_with_parameters]: Received parameter event from node /node_with_parameters
[INFO] [1746414766.244271445] [node_with_parameters]: Inside event: an_int_param changed to: 4
```

Now set the new double parameter:

```
$ ros2 param set node_with_parameters another_double_param 4.4
```

Since no single-parameter callback was added (via `add_parameter_callback`) for the double parameter, we should see only the event callback fire:

```
[INFO] [1746414962.604832196] [node_with_parameters]: Received parameter event from node /node_with_parameters
[INFO] [1746414962.607429035] [node_with_parameters]: Inside event: another_double_param changed to: 4.4
```

> [!NOTE]
>
> When setting multiple parameters at once, it’s best to use `set_parameters_atomically`, explained in [Parameters](../../concepts/basic/about-parameters.md).
> This way, the event callback is only fired once.

<a id="summary"></a>

## Summary

You created a node with a parameter and used the ParameterEventHandler class to set a callback to monitor changes to that parameter.
You also used the same class to monitor changes to a remote node, and to monitor all parameters in a single event callback.
The ParameterEventHandler is a convenient way to monitor for parameter changes so that you can then respond to the updated values.

<a id="related-content"></a>

## Related content

To learn how to adapt ROS 1 parameter files for ROS 2, see the [Migrating YAML parameter files from ROS 1 to ROS2](../../how-to/migrating-from-ros1/migrating-parameters.md) tutorial.
