---
title: "Using substitutions"
docname: "Tutorials/Intermediate/Launch/Using-Substitutions"
source: "Tutorials/Intermediate/Launch/Using-Substitutions.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="using-substitutions"></a>

# Using substitutions

**Goal:** Learn about substitutions in ROS 2 launch files.

**Tutorial level:** Intermediate

**Time:** 15 minutes

Table of Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Using substitutions](#id1)

  - [1 Create and setup the package](#create-and-setup-the-package)
  - [2 Parent launch file](#parent-launch-file)
  - [3 Substitutions example launch file](#substitutions-example-launch-file)
  - [4 Build the package](#build-the-package)
- [Launching example](#launching-example)
- [Modifying launch arguments](#modifying-launch-arguments)
- [Boolean substitutions](#boolean-substitutions)
- [Documentation](#documentation)
- [Summary](#summary)

<a id="background"></a>

## Background

Launch files are used to start nodes, services and execute processes.
This set of actions may have arguments, which affect their behavior.
Substitutions can be used in arguments to provide more flexibility when describing reusable launch files.
Substitutions are variables that are only evaluated during execution of the launch description and can be used to acquire specific information like a launch configuration, an environment variable, or to evaluate an arbitrary Python expression.

This tutorial shows usage examples of substitutions in ROS 2 launch files.

<a id="prerequisites"></a>

## Prerequisites

This tutorial uses the [turtlesim](../../beginner-cli-tools/introducing-turtlesim.md) package.
This tutorial also assumes you are familiar with [creating packages](../../beginner-client-libraries/creating-your-first-ros2-package.md).

As always, don’t forget to source ROS 2 in [every new terminal you open](../../beginner-cli-tools/configuring-ros2-environment.md).

<a id="id1"></a>

## Using substitutions

<a id="create-and-setup-the-package"></a>

### 1 Create and setup the package

First, create a new package with the name `launch_tutorial`:

Python package

Create a new package of build\_type `ament_python`:

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 launch_tutorial
```

C++ package

Create a new package of build\_type `ament_cmake`:

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 launch_tutorial
```

Inside of that package, create a directory called `launch`:

Linux

```
$ mkdir launch_tutorial/launch
```

macOS

```
$ mkdir launch_tutorial/launch
```

Windows

```
$ md launch_tutorial/launch
```

Finally, make sure to install the launch files:

Python package

Add in following changes to the `setup.py` of the package:

```
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'launch_tutorial'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ]
)
```

C++ package

Append following code to the `CMakeLists.txt` just before `ament_package()`:

```
install(DIRECTORY
        launch
        DESTINATION share/${PROJECT_NAME}/
)
```

<a id="parent-launch-file"></a>

### 2 Parent launch file

Let’s create a launch file that will call and pass arguments to another launch file.
This launch file can either be in YAML, XML, or in Python.

To do this, create following file in the `launch` folder of the `launch_tutorial` package.

XML

Copy and paste the complete code into the `launch/example_main_launch.xml` file:

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <let name="background_r" value="200" />
  <include file="$(find-pkg-share launch_tutorial)/launch/example_substitutions_launch.xml">
    <let name="turtlesim_ns" value="turtlesim2" />
    <let name="use_provided_red" value="True" />
    <let name="new_background_r" value="$(var background_r)" />
  </include>
</launch>
```

The `$(find-pkg-share launch_tutorial)` substitution is used to find the path to the `launch_tutorial` package.
The path substitution is then joined with the `example_substitutions_launch.xml` file name.

```
  <include file="$(find-pkg-share launch_tutorial)/launch/example_substitutions_launch.xml">
```

The `background_r` variable with `turtlesim_ns` and `use_provided_red` arguments is passed to the `include` action.
The `$(var background_r)` substitution is used to define the `new_background_r` argument with the value of the `background_r` variable.

```
    <let name="turtlesim_ns" value="turtlesim2" />
    <let name="use_provided_red" value="True" />
    <let name="new_background_r" value="$(var background_r)" />
```

YAML

Copy and paste the complete code into the `launch/example_main_launch.yaml` file:

```
%YAML 1.2
---
launch:
  - let:
      name: "background_r"
      value: "200"
  - include:
      file: "$(find-pkg-share launch_tutorial)/launch/example_substitutions_launch.yaml"
      let:
        - name: "turtlesim_ns"
          value: "turtlesim2"
        - name: "use_provided_red"
          value: "True"
        - name: "new_background_r"
          value: "$(var background_r)"
```

The `$(find-pkg-share launch_tutorial)` substitution is used to find the path to the `launch_tutorial` package.
The path substitution is then joined with the `example_substitutions_launch.yaml` file name.

```
      file: "$(find-pkg-share launch_tutorial)/launch/example_substitutions_launch.yaml"
```

The `background_r` variable with `turtlesim_ns` and `use_provided_red` arguments is passed to the `include` action.
The `$(var background_r)` substitution is used to define the `new_background_r` argument with the value of the `background_r` variable.

```
      let:
        - name: "turtlesim_ns"
          value: "turtlesim2"
        - name: "use_provided_red"
          value: "True"
        - name: "new_background_r"
          value: "$(var background_r)"
```

Python

Copy and paste the complete code into the `launch/example_main_launch.py` file:

```
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('launch_tutorial'),
                'launch',
                'example_substitutions_launch.py'
            ]),
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': colors['background_r'],
            }.items()
        )
    ])
```

The `FindPackageShare` substitution is used to find the path to the `launch_tutorial` package.
The `PathJoinSubstitution` substitution is then used to join the path to that package path with the `example_substitutions_launch.py` file name.

```
            PathJoinSubstitution([
                FindPackageShare('launch_tutorial'),
                'launch',
                'example_substitutions_launch.py'
            ]),
```

The `launch_arguments` dictionary with `turtlesim_ns` and `use_provided_red` arguments is passed to the `IncludeLaunchDescription` action.

```
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': colors['background_r'],
            }.items()
```

<a id="substitutions-example-launch-file"></a>

### 3 Substitutions example launch file

Now create the substitution launch file in the same folder:

XML

Create the file `launch/example_substitutions_launch.xml` and insert the following code:

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <arg name="turtlesim_ns" default="turtlesim1" />
  <arg name="use_provided_red" default="False" />
  <arg name="new_background_r" default="200" />

  <node pkg="turtlesim" namespace="$(var turtlesim_ns)" exec="turtlesim_node" name="sim" />
  <executable cmd="ros2 service call $(var turtlesim_ns)/spawn turtlesim/srv/Spawn '{x: 5, y: 2, theta: 0.2}'" />
  <executable cmd="ros2 param set $(var turtlesim_ns)/sim background_r 120" />
  <timer period="2.0">
    <executable cmd="ros2 param set $(var turtlesim_ns)/sim background_r $(var new_background_r)"
      if="$(eval '$(var new_background_r) == 200 and $(var use_provided_red)')" />
  </timer>
</launch>
```

The `turtlesim_ns`, `use_provided_red`, and `new_background_r` launch configurations are defined.
They are used to store values of launch arguments in the above variables and to pass them to required actions.
The launch configuration arguments can later be used with the `$(var <name>)` substitution to acquire the value of the launch argument in any part of the launch description.

The `arg` tag is used to define the launch argument that can be passed from the above launch file or from the console.

```
  <arg name="turtlesim_ns" default="turtlesim1" />
  <arg name="use_provided_red" default="False" />
  <arg name="new_background_r" default="200" />
```

The `turtlesim_node` node with the `namespace` set to the `turtlesim_ns` launch configuration value using the `$(var <name>)` substitution is defined.

```
  <node pkg="turtlesim" namespace="$(var turtlesim_ns)" exec="turtlesim_node" name="sim" />
```

Afterwards, an `executable` action is defined with the corresponding `cmd` tag.
This command makes a call to the spawn service of the turtlesim node.

Additionally, the `$(var <name>)` substitution is used to get the value of the `turtlesim_ns` launch argument to construct a command string.

```
  <executable cmd="ros2 service call $(var turtlesim_ns)/spawn turtlesim/srv/Spawn '{x: 5, y: 2, theta: 0.2}'" />
```

The same approach is used for the `ros2 param` `executable` actions that change the turtlesim background’s red color parameter.
The difference is that the second action inside of the timer is only executed if the provided `new_background_r` argument equals `200` and the `use_provided_red` launch argument is set to `True`.
The evaluation of the `if` predicate is done using the `$(eval <python-expression>)` substitution.

```
  <executable cmd="ros2 param set $(var turtlesim_ns)/sim background_r 120" />
  <timer period="2.0">
    <executable cmd="ros2 param set $(var turtlesim_ns)/sim background_r $(var new_background_r)"
      if="$(eval '$(var new_background_r) == 200 and $(var use_provided_red)')" />
  </timer>
```

YAML

Create the file `launch/example_substitutions_launch.yaml` and insert the following code:

```
%YAML 1.2
---
launch:
  - arg:
      name: "turtlesim_ns"
      default: "turtlesim1"
  - arg:
      name: "use_provided_red"
      default: "False"
  - arg:
      name: "new_background_r"
      default: "200"

  - node:
      pkg: "turtlesim"
      namespace: "$(var turtlesim_ns)"
      exec: "turtlesim_node"
      name: "sim"
  - executable:
      cmd: 'ros2 service call $(var turtlesim_ns)/spawn turtlesim/srv/Spawn "{x: 5, y: 2, theta: 0.2}"'
  - executable:
      cmd: "ros2 param set $(var turtlesim_ns)/sim background_r 120"
  - timer:
      period: 2.0
      children:
        - executable:
            cmd: "ros2 param set $(var turtlesim_ns)/sim background_r $(var new_background_r)"
            if: '$(eval "$(var new_background_r) == 200 and $(var use_provided_red)")'
```

The `turtlesim_ns`, `use_provided_red`, and `new_background_r` launch configurations are defined.
They are used to store values of launch arguments in the above variables and to pass them to required actions.
The launch configuration arguments can later be used with the `$(var <name>)` substitution to acquire the value of the launch argument in any part of the launch description.

The `arg` tag is used to define the launch argument that can be passed from the above launch file or from the console.

```
  - arg:
      name: "turtlesim_ns"
      default: "turtlesim1"
  - arg:
      name: "use_provided_red"
      default: "False"
  - arg:
      name: "new_background_r"
      default: "200"
```

The `turtlesim_node` node with the `namespace` set to the `turtlesim_ns` launch configuration value using the `$(var <name>)` substitution is defined.

```
  - node:
      pkg: "turtlesim"
      namespace: "$(var turtlesim_ns)"
      exec: "turtlesim_node"
      name: "sim"
```

Afterwards, an `executable` action is defined with the corresponding `cmd` tag.
This command makes a call to the spawn service of the turtlesim node.

Additionally, the `$(var <name>)` substitution is used to get the value of the `turtlesim_ns` launch argument to construct a command string.

```
  - executable:
      cmd: 'ros2 service call $(var turtlesim_ns)/spawn turtlesim/srv/Spawn "{x: 5, y: 2, theta: 0.2}"'
```

The same approach is used for the `ros2 param` `executable` actions that change the turtlesim background’s red color parameter.
The difference is that the second action inside of the timer is only executed if the provided `new_background_r` argument equals `200` and the `use_provided_red` launch argument is set to `True`.
The evaluation of the `if` predicate is done using the `$(eval <python-expression>)` substitution.

```
  - executable:
      cmd: "ros2 param set $(var turtlesim_ns)/sim background_r 120"
  - timer:
      period: 2.0
      children:
        - executable:
            cmd: "ros2 param set $(var turtlesim_ns)/sim background_r $(var new_background_r)"
            if: '$(eval "$(var new_background_r) == 200 and $(var use_provided_red)")'
```

Python

Create the file `launch/example_substitutions_launch.py` and insert the following code:

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    return LaunchDescription([
        DeclareLaunchArgument(
            'turtlesim_ns',
            default_value='turtlesim1'
        ),
        DeclareLaunchArgument(
            'use_provided_red',
            default_value='False'
        ),
        DeclareLaunchArgument(
            'new_background_r',
            default_value='200'
        ),
        Node(
            package='turtlesim',
            namespace=turtlesim_ns,
            executable='turtlesim_node',
            name='sim'
        ),
        ExecuteProcess(
            cmd=[[
                'ros2 service call ',
                turtlesim_ns,
                '/spawn ',
                'turtlesim/srv/Spawn ',
                '"{x: 2, y: 2, theta: 0.2}"'
            ]],
            shell=True
        ),
        ExecuteProcess(
            cmd=[[
                'ros2 param set ',
                turtlesim_ns,
                '/sim background_r ',
                '120'
            ]],
            shell=True
        ),
        TimerAction(
            period=2.0,
            actions=[
                ExecuteProcess(
                    condition=IfCondition(
                        PythonExpression([
                            new_background_r,
                            ' == 200',
                            ' and ',
                            use_provided_red
                        ])
                    ),
                    cmd=[[
                        'ros2 param set ',
                        turtlesim_ns,
                        '/sim background_r ',
                        new_background_r
                    ]],
                    shell=True
                ),
            ],
        )
    ])
```

The `turtlesim_ns`, `use_provided_red`, and `new_background_r` launch configurations are defined.
They are used to represent values of launch arguments in the above variables and to pass them to required actions.
These `LaunchConfiguration` substitutions allow us to acquire the value of the launch argument in any part of the launch description.

`DeclareLaunchArgument` is used to define the launch argument that can be passed from the above launch file or from the console.

```
        DeclareLaunchArgument(
            'turtlesim_ns',
            default_value='turtlesim1'
        ),
        DeclareLaunchArgument(
            'use_provided_red',
            default_value='False'
        ),
        DeclareLaunchArgument(
            'new_background_r',
            default_value='200'
        ),
```

The `turtlesim_node` node with the `namespace` set to `turtlesim_ns` `LaunchConfiguration` substitution is defined.

```
        Node(
            package='turtlesim',
            namespace=turtlesim_ns,
            executable='turtlesim_node',
            name='sim'
        ),
```

The next action, `ExecuteProcess`, is defined with the corresponding `cmd` argument to call the spawn service of the turtlesim node.

Additionally, the `LaunchConfiguration` substitution is used to provide the value of the `turtlesim_ns` launch argument in the command string.

```
        ExecuteProcess(
            cmd=[[
                'ros2 service call ',
                turtlesim_ns,
                '/spawn ',
                'turtlesim/srv/Spawn ',
                '"{x: 2, y: 2, theta: 0.2}"'
            ]],
            shell=True
        ),
```

The same approach is used for the `change_background_r` and `change_background_r_conditioned` actions that change the turtlesim background’s red color parameter.
The difference is that the next action is only executed if the provided `new_background_r` argument equals `200` and the `use_provided_red` launch argument is set to `True`.
The evaluation inside the `IfCondition` is done using the `PythonExpression` substitution.

```
        TimerAction(
            period=2.0,
            actions=[
                ExecuteProcess(
                    condition=IfCondition(
                        PythonExpression([
                            new_background_r,
                            ' == 200',
                            ' and ',
                            use_provided_red
                        ])
                    ),
                    cmd=[[
                        'ros2 param set ',
                        turtlesim_ns,
                        '/sim background_r ',
                        new_background_r
                    ]],
                    shell=True
                ),
            ],
        )
```

<a id="build-the-package"></a>

### 4 Build the package

Go to the root of the workspace, and build the package:

```
$ colcon build
```

Also remember to source the workspace after building.

<a id="launching-example"></a>

## Launching example

Now you can launch using the `ros2 launch` command.

YAML

```
$ ros2 launch launch_tutorial example_main_launch.yaml
```

XML

```
$ ros2 launch launch_tutorial example_main_launch.xml
```

Python

```
$ ros2 launch launch_tutorial example_main_launch.py
```

This will do the following:

1. Start a turtlesim node with a blue background
2. Spawn the second turtle
3. Change the color to purple
4. Change the color to pink after two seconds if the provided `background_r` argument is `200` and `use_provided_red` argument is `True`

<a id="modifying-launch-arguments"></a>

## Modifying launch arguments

YAML

If you want to change the provided launch arguments, you can either update the `background_r` variable in the `example_main_launch.yaml` or launch the `example_substitutions_launch.yaml` with preferred arguments.
To see arguments that may be given to the launch file, run the following command:

```
$ ros2 launch launch_tutorial example_substitutions_launch.yaml --show-args
```

XML

If you want to change the provided launch arguments, you can either update the `background_r` variable in the `example_main_launch.xml` or launch the `example_substitutions_launch.xml` with preferred arguments.
To see arguments that may be given to the launch file, run the following command:

```
$ ros2 launch launch_tutorial example_substitutions_launch.xml --show-args
```

Python

If you want to change the provided launch arguments, you can either update them in `launch_arguments` dictionary in the `example_main_launch.py` or launch the `example_substitutions_launch.py` with preferred arguments.
To see arguments that may be given to the launch file, run the following command:

```
$ ros2 launch launch_tutorial example_substitutions_launch.py --show-args
```

This will show the arguments that may be given to the launch file and their default values.

```
Arguments (pass arguments as '<name>:=<value>'):

    'turtlesim_ns':
        no description given
        (default: 'turtlesim1')

    'use_provided_red':
        no description given
        (default: 'False')

    'new_background_r':
        no description given
        (default: '200')
```

Now you can pass the desired arguments to the launch file as follows:

YAML

```
$ ros2 launch launch_tutorial example_substitutions_launch.yaml turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```

XML

```
$ ros2 launch launch_tutorial example_substitutions_launch.xml turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```

Python

```
$ ros2 launch launch_tutorial example_substitutions_launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```

<a id="boolean-substitutions"></a>
<a id="booleansubstitutions"></a>

## Boolean substitutions

In addition to `$(eval <python-expression>)`, a set of dedicated boolean substitutions is available for comparing values and combining the results.
They can be used anywhere a substitution is allowed, including the `if` and `unless` attributes of any action.

> [!NOTE]
>
> Comparison is performed on the string representation of each argument.

| XML / YAML name | Python class | Description |
| --- | --- | --- |
| `$(equals A B)` | `EqualsSubstitution` | Resolves to `'true'` if `A` equals `B`, otherwise `'false'`. |
| `$(not-equals A B)` | `NotEqualsSubstitution` | Resolves to `'true'` if `A` does not equal `B`, otherwise `'false'`. |
| `$(and A B)` | `AndSubstitution` | Logical AND of two boolean substitutions. |
| `$(or A B)` | `OrSubstitution` | Logical OR of two boolean substitutions. |
| `$(any A B ...)` | `AnySubstitution` | Resolves to `'true'` if any argument is true. |
| `$(all A B ...)` | `AllSubstitution` | Resolves to `'true'` only if every argument is true. |

The `if` predicate from the previous section can also be expressed using boolean substitutions instead of a Python expression:

XML

```
<executable cmd="ros2 param set /turtlesim background_r $(var new_background_r)"
            if="$(and $(equals $(var new_background_r) 200) $(var use_provided_red))"/>
```

YAML

```
- executable:
    cmd: ros2 param set /turtlesim background_r $(var new_background_r)
    if: $(and $(equals $(var new_background_r) 200) $(var use_provided_red))
```

Python

```
from launch.conditions import IfCondition
from launch.substitutions import AndSubstitution, EqualsSubstitution, LaunchConfiguration

ExecuteProcess(
    cmd=[[
        FindExecutable(name='ros2'),
        ' param set ',
        '/turtlesim background_r ',
        LaunchConfiguration('new_background_r'),
    ]],
    condition=IfCondition(
        AndSubstitution(
            EqualsSubstitution(LaunchConfiguration('new_background_r'), '200'),
            LaunchConfiguration('use_provided_red'),
        )
    ),
)
```

<a id="documentation"></a>

## Documentation

[The launch documentation](https://docs.ros.org/en/jazzy/p/launch/doc/source/architecture.html) provides detailed information about available substitutions.

<a id="summary"></a>

## Summary

In this tutorial, you learned about using substitutions in launch files.
You learned about their possibilities and capabilities to create reusable launch files.

You can now learn more about [using event handlers in launch files](using-event-handlers.md) which are used to define a complex set of rules which can be used to dynamically modify the launch file.
