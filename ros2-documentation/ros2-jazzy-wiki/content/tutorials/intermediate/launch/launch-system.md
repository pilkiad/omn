---
title: "Integrating launch files into ROS 2 packages"
docname: "Tutorials/Intermediate/Launch/Launch-system"
source: "Tutorials/Intermediate/Launch/Launch-system.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="integrating-launch-files-into-ros-2-packages"></a>

# Integrating launch files into ROS 2 packages

**Goal:** Add a launch file to a ROS 2 package

**Tutorial level:** Intermediate

**Time:** 10 minutes

Contents

- [Prerequisites](#prerequisites)
- [Background](#background)
- [Tasks](#tasks)

  - [1 Create a package](#create-a-package)
  - [2 Creating the structure to hold launch files](#creating-the-structure-to-hold-launch-files)
  - [3 Writing the launch file](#writing-the-launch-file)
  - [4 Building and running the launch file](#building-and-running-the-launch-file)
- [Documentation](#documentation)

<a id="prerequisites"></a>

## Prerequisites

You should have gone through the tutorial on how to [create a ROS 2 package](../../beginner-client-libraries/creating-your-first-ros2-package.md).

As always, don’t forget to source ROS 2 in [every new terminal you open](../../beginner-cli-tools/configuring-ros2-environment.md).

<a id="background"></a>

## Background

In the [previous tutorial](creating-launch-files.md), we saw how to write a standalone launch file.
This tutorial will show how to add a launch file to an existing package, and the conventions typically used.

<a id="tasks"></a>

## Tasks

<a id="create-a-package"></a>

### 1 Create a package

Create a workspace for the package to live in:

Linux

```
$ mkdir -p launch_ws/src
$ cd launch_ws/src
```

macOS

```
$ mkdir -p launch_ws/src
$ cd launch_ws/src
```

Windows

```
$ md launch_ws\src
$ cd launch_ws\src
```

Python package

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 py_launch_example
```

C++ package

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_launch_example
```

<a id="creating-the-structure-to-hold-launch-files"></a>

### 2 Creating the structure to hold launch files

By convention, all launch files for a package are stored in the `launch` directory inside of the package.
Make sure to create a `launch` directory at the top-level of the package you created above.

Python package

For Python packages, the directory containing your package should look like this:

```
src/
  py_launch_example/
    launch/
    package.xml
    py_launch_example/
    resource/
    setup.cfg
    setup.py
    test/
```

To enable colcon to locate and utilize our launch files, we need to inform Python’s setup tools of their presence.
To achieve this, open the `setup.py` file, add the necessary `import` statements at the top, and include the launch files into the `data_files` parameter of `setup`:

```
import os
from glob import glob
# Other imports ...

package_name = 'py_launch_example'

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

For C++ packages, we will only be adjusting the `CMakeLists.txt` file by adding:

```
# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)
```

to the end of the file (but before `ament_package()`).

<a id="writing-the-launch-file"></a>

### 3 Writing the launch file

XML launch file

Inside your `launch` directory, create a new launch file called `my_script_launch.xml`.
`_launch.xml` is recommended, but not required, as the file suffix for XML launch files.

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="demo_nodes_cpp" exec="talker" name="talker"/>
</launch>
```

YAML launch file

Inside your `launch` directory, create a new launch file called `my_script_launch.yaml`.
`_launch.yaml` is recommended, but not required, as the file suffix for YAML launch files.

```
%YAML 1.2
---
launch:
  - node:
      pkg: "demo_nodes_cpp"
      exec: "talker"
      name: "talker"
```

Python launch file

Inside your `launch` directory, create a new launch file called `my_script_launch.py`.
`_launch.py` is recommended, but not required, as the file suffix for Python launch files.
However, the launch file name needs to end with `launch.py` to be recognized and autocompleted by `ros2 launch`.

Your launch file should define the `generate_launch_description()` function which returns a `launch.LaunchDescription()` to be used by the `ros2 launch` verb.

```
import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker'),
    ])
```

<a id="building-and-running-the-launch-file"></a>

### 4 Building and running the launch file

Go to the top-level of the workspace, and build it:

```
$ colcon build
```

After the `colcon build` has been successful and you’ve sourced the workspace, you should be able to run the launch file as follows:

Python package

XML launch file

```
$ ros2 launch py_launch_example my_script_launch.xml
```

YAML launch file

```
$ ros2 launch py_launch_example my_script_launch.yaml
```

Python launch file

```
$ ros2 launch py_launch_example my_script_launch.py
```

C++ package

XML launch file

```
$ ros2 launch cpp_launch_example my_script_launch.xml
```

YAML launch file

```
$ ros2 launch cpp_launch_example my_script_launch.yaml
```

Python launch file

```
$ ros2 launch cpp_launch_example my_script_launch.py
```

<a id="documentation"></a>

## Documentation

[The launch documentation](https://docs.ros.org/en/jazzy/p/launch/architecture.html) provides more details on concepts that are also used in `launch_ros`.

Additional documentation/examples of launch capabilities are forthcoming.
See the source code (<https://github.com/ros2/launch> and <https://github.com/ros2/launch_ros>) in the meantime.
