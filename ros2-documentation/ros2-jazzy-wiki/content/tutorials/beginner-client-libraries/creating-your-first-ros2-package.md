---
title: "Creating a package"
docname: "Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package"
source: "Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="creating-a-package"></a>
<a id="createpkg"></a>

# Creating a package

**Goal:** Create a new package using either CMake or Python, and run its executable.

**Tutorial level:** Beginner

**Time:** 15 minutes

Contents

- [Background](#background)

  - [1 What is a ROS 2 package?](#what-is-a-ros-2-package)
  - [2 What makes up a ROS 2 package?](#what-makes-up-a-ros-2-package)
  - [3 Packages in a workspace](#packages-in-a-workspace)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a package](#create-a-package)
  - [2 Build a package](#build-a-package)
  - [3 Source the setup file](#source-the-setup-file)
  - [4 Use the package](#use-the-package)
  - [5 Examine package contents](#examine-package-contents)
  - [6 Customize package.xml](#customize-package-xml)
- [Summary](#summary)
- [Next steps](#next-steps)

<a id="background"></a>

## Background

<a id="what-is-a-ros-2-package"></a>

### 1 What is a ROS 2 package?

A package is an organizational unit for your ROS 2 code.
If you want to be able to install your code or share it with others, then you’ll need it organized in a package.
With packages, you can release your ROS 2 work and allow others to build and use it easily.

Package creation in ROS 2 uses ament as its build system and colcon as its build tool.
You can create a package using either CMake or Python, which are officially supported, though other build types do exist.

<a id="what-makes-up-a-ros-2-package"></a>

### 2 What makes up a ROS 2 package?

ROS 2 Python and CMake packages each have their own minimum required contents:

CMake

- `CMakeLists.txt` file that describes how to build the code within the package
- `include/<package_name>` directory containing the public headers for the package
- `package.xml` file containing meta information about the package
- `src` directory containing the source code for the package

Python

- `package.xml` file containing meta information about the package
- `resource/<package_name>` marker file for the package
- `setup.cfg` is required when a package has executables, so `ros2 run` can find them
- `setup.py` containing instructions for how to install the package
- `<package_name>` - a directory with the same name as your package, used by ROS 2 tools to find your package, contains `__init__.py`

The simplest possible package may have a file structure that looks like:

CMake

```
my_package/
     CMakeLists.txt
     include/my_package/
     package.xml
     src/
```

Python

```
my_package/
      package.xml
      resource/my_package
      setup.cfg
      setup.py
      my_package/
```

<a id="packages-in-a-workspace"></a>

### 3 Packages in a workspace

A single workspace can contain as many packages as you want, each in their own folder.
You can also have packages of different build types in one workspace (CMake, Python, etc.).
You cannot have nested packages.

Best practice is to have a `src` folder within your workspace, and to create your packages in there.
This keeps the top level of the workspace “clean”.

A trivial workspace might look like:

```
workspace_folder/
    src/
      cpp_package_1/
          CMakeLists.txt
          include/cpp_package_1/
          package.xml
          src/

      py_package_1/
          package.xml
          resource/py_package_1
          setup.cfg
          setup.py
          py_package_1/
      ...
      cpp_package_n/
          CMakeLists.txt
          include/cpp_package_n/
          package.xml
          src/
```

<a id="prerequisites"></a>

## Prerequisites

You should have a ROS 2 workspace after following the instructions in the [previous tutorial](creating-a-workspace.md).
You will create your package in this workspace.

<a id="tasks"></a>

## Tasks

<a id="create-a-package"></a>

### 1 Create a package

First, [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md).

Let’s use the workspace you created in the [previous tutorial](creating-a-workspace.md#new-directory), `ros2_ws`, for your new package.

Make sure you are in the `src` folder before running the package creation command.

Linux

```
$ cd ~/ros2_ws/src
```

macOS

```
$ cd ~/ros2_ws/src
```

Windows

```
$ cd \ros2_ws\src
```

The command syntax for creating a new package in ROS 2 is:

CMake

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
```

Python

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
```

For this tutorial, you will use the optional arguments `--node-name` and `--license`.
`--node-name` option creates a simple Hello World type executable in the package, and `--license` declares the license information for the package.

Enter the following command in your terminal:

CMake

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name my_node my_package
```

Python

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_node my_package
```

You will now have a new folder within your workspace’s `src` directory called `my_package`.

After running the command, your terminal will return the message:

CMake

```
going to create a new package
package name: my_package
destination directory: /home/user/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['<name> <email>']
licenses: ['Apache-2.0']
build type: ament_cmake
dependencies: []
node_name: my_node
creating folder ./my_package
creating ./my_package/package.xml
creating source and include folder
creating folder ./my_package/src
creating folder ./my_package/include/my_package
creating ./my_package/CMakeLists.txt
creating ./my_package/src/my_node.cpp
```

Python

```
going to create a new package
package name: my_package
destination directory: /home/user/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['<name> <email>']
licenses: ['Apache-2.0']
build type: ament_python
dependencies: []
node_name: my_node
creating folder ./my_package
creating ./my_package/package.xml
creating source folder
creating folder ./my_package/my_package
creating ./my_package/setup.py
creating ./my_package/setup.cfg
creating folder ./my_package/resource
creating ./my_package/resource/my_package
creating ./my_package/my_package/__init__.py
creating folder ./my_package/test
creating ./my_package/test/test_copyright.py
creating ./my_package/test/test_flake8.py
creating ./my_package/test/test_pep257.py
creating ./my_package/my_package/my_node.py
```

You can see the automatically generated files for the new package.

<a id="build-a-package"></a>

### 2 Build a package

Putting packages in a workspace is especially valuable because you can build many packages at once by running `colcon build` in the workspace root.
Otherwise, you would have to build each package individually.

Return to the root of your workspace:

Linux

```
$ cd ~/ros2_ws
```

macOS

```
$ cd ~/ros2_ws
```

Windows

```
$ cd \ros2_ws
```

Now you can build your packages:

Linux

```
$ colcon build
```

macOS

```
$ colcon build
```

Windows

```
$ colcon build --merge-install
```

Windows doesn’t allow long paths, so `merge-install` will combine all the paths into the `install` directory.

Recall from the last tutorial that you also have the `ros_tutorials` packages in your `ros2_ws`.
You might have noticed that running `colcon build` also built the `turtlesim` package.
That’s fine when you only have a few packages in your workspace, but when there are many packages, `colcon build` can take a long time.

To build only the `my_package` package next time, you can run:

```
$ colcon build --packages-select my_package
```

<a id="source-the-setup-file"></a>

### 3 Source the setup file

To use your new package and executable, first open a new terminal and source your main ROS 2 installation.

Then, from inside the `ros2_ws` directory, run the following command to source your workspace:

Linux

```
$ source install/local_setup.bash
```

macOS

```
$ . install/local_setup.bash
```

Windows

```
$ call install/local_setup.bat
```

Now that your workspace has been added to your path, you will be able to use your new package’s executables.

<a id="use-the-package"></a>

### 4 Use the package

To run the executable you created using the `--node-name` argument during package creation, enter the command:

```
$ ros2 run my_package my_node
```

Which will return a message to your terminal:

CMake

```
hello world my_package package
```

Python

```
Hi from my_package.
```

<a id="examine-package-contents"></a>

### 5 Examine package contents

Inside `ros2_ws/src/my_package`, you will see the files and folders that `ros2 pkg create` automatically generated:

CMake

```
CMakeLists.txt  include  package.xml  src
```

`my_node.cpp` is inside the `src` directory.
This is where all your custom C++ nodes will go in the future.

Python

```
my_package  package.xml  resource  setup.cfg  setup.py  test
```

`my_node.py` is inside the `my_package` directory.
This is where all your custom Python nodes will go in the future.

<a id="customize-package-xml"></a>

### 6 Customize package.xml

You may have noticed in the return message after creating your package that the fields `description` and `license` contain `TODO` notes.
That’s because the package description and license declaration are not automatically set, but are required if you ever want to release your package.
The `maintainer` field may also need to be filled in.

From `ros2_ws/src/my_package`, open `package.xml` using your preferred text editor:

CMake

```
<?xml version="1.0"?>
<?xml-model
   href="http://download.ros.org/schema/package_format3.xsd"
   schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
 <name>my_package</name>
 <version>0.0.0</version>
 <description>TODO: Package description</description>
 <maintainer email="user@todo.todo">user</maintainer>
 <license>TODO: License declaration</license>

 <buildtool_depend>ament_cmake</buildtool_depend>

 <test_depend>ament_lint_auto</test_depend>
 <test_depend>ament_lint_common</test_depend>

 <export>
   <build_type>ament_cmake</build_type>
 </export>
</package>
```

Python

```
<?xml version="1.0"?>
<?xml-model
   href="http://download.ros.org/schema/package_format3.xsd"
   schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
 <name>my_package</name>
 <version>0.0.0</version>
 <description>TODO: Package description</description>
 <maintainer email="user@todo.todo">user</maintainer>
 <license>TODO: License declaration</license>

 <test_depend>ament_copyright</test_depend>
 <test_depend>ament_flake8</test_depend>
 <test_depend>ament_pep257</test_depend>
 <test_depend>python3-pytest</test_depend>

 <export>
   <build_type>ament_python</build_type>
 </export>
</package>
```

Input your name and email on the `maintainer` line if it hasn’t been automatically populated for you.
Then, edit the `description` line to summarize the package:

```
<description>Beginner client libraries tutorials practice package</description>
```

Then, update the `license` line.
You can read more about open source licenses [here](https://opensource.org/licenses/alphabetical).
Since this package is only for practice, it’s safe to use any license.
We’ll use `Apache-2.0`:

```
<license>Apache-2.0</license>
```

Don’t forget to save once you’re done editing.

Below the license tag, you will see some tag names ending with `_depend`.
This is where your `package.xml` would list its dependencies on other packages, for colcon to search for.
`my_package` is simple and doesn’t have any dependencies, but you will see this space being utilized in upcoming tutorials.

CMake

You’re all done for now!

Python

The `setup.py` file contains the same description, maintainer and license fields as `package.xml`, so you need to set those as well.
They need to match exactly in both files.
The version and name (`package_name`) also need to match exactly, and should be automatically populated in both files.

Open `setup.py` with your preferred text editor.

```
from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
 name=package_name,
 version='0.0.0',
 packages=find_packages(exclude=['test']),
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 maintainer='TODO',
 maintainer_email='TODO',
 description='TODO: Package description',
 license='TODO: License declaration',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'my_node = my_py_pkg.my_node:main'
     ],
   },
)
```

Edit the `maintainer`, `maintainer_email`, and `description` lines to match `package.xml`.

Don’t forget to save the file.

<a id="summary"></a>

## Summary

You’ve created a package to organize your code and make it easy to use for others.

Your package was automatically populated with the necessary files, and then you used colcon to build it so you can use its executables in your local environment.

<a id="next-steps"></a>

## Next steps

Next, let’s add something meaningful to a package.
You’ll start with a simple publisher/subscriber system, which you can choose to write in either [C++](writing-a-simple-cpp-publisher-and-subscriber.md) or [Python](writing-a-simple-py-publisher-and-subscriber.md).
