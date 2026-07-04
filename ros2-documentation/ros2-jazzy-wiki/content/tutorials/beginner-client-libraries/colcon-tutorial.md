---
title: "Using colcon to build packages"
docname: "Tutorials/Beginner-Client-Libraries/Colcon-Tutorial"
source: "Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="using-colcon-to-build-packages"></a>
<a id="colcon"></a>

# Using `colcon` to build packages

Table of Contents

- [Background](#background)
- [Prerequisites](#prerequisites)

  - [Install colcon](#install-colcon)
  - [Install ROS 2](#install-ros-2)
- [Basics](#basics)

  - [Create a workspace](#create-a-workspace)
  - [Add some sources](#add-some-sources)
  - [Source an underlay](#source-an-underlay)
  - [Build the workspace](#build-the-workspace)
  - [Run tests](#run-tests)
  - [Source the environment](#source-the-environment)
  - [Try a demo](#try-a-demo)
- [Create your own package](#create-your-own-package)
- [Setup `colcon_cd`](#setup-colcon-cd)
- [Setup `colcon` tab completion](#setup-colcon-tab-completion)
- [Tips](#tips)
- [Setup `colcon` mixins](#setup-colcon-mixins)

**Goal:** Build a ROS 2 workspace with `colcon`.

**Tutorial level:** Beginner

**Time:** 20 minutes

This is a brief tutorial on how to create and build a ROS 2 workspace with `colcon`.
It is a practical tutorial and not designed to replace the core documentation.

<a id="background"></a>

## Background

`colcon` is an iteration on the ROS build tools `catkin_make`, `catkin_make_isolated`, `catkin_tools` and `ament_tools`.
For more information on the design of colcon see [this document](https://design.ros2.org/articles/build_tool.html).

The source code can be found in the [colcon GitHub organization](https://github.com/colcon).

<a id="prerequisites"></a>

## Prerequisites

<a id="install-colcon"></a>

### Install colcon

Ubuntu

```
$ sudo apt install python3-colcon-common-extensions
```

RHEL

```
$ sudo dnf install python3-colcon-common-extensions
```

macOS

```
$ python3 -m pip install colcon-common-extensions
```

Windows

```
$ pip install -U colcon-common-extensions
```

<a id="install-ros-2"></a>

### Install ROS 2

To build the samples, you will need to install ROS 2.

Follow the [installation instructions](../../installation/overview.md).

> [!ATTENTION]
>
> If installing from deb packages, this tutorial requires the [desktop installation](../../installation/ubuntu-install-debs.md#linux-install-debs-install-ros-2-packages).

<a id="basics"></a>

## Basics

A ROS workspace is a directory with a particular structure.
Commonly there is a `src` subdirectory.
Inside that subdirectory is where the source code of ROS packages will be located.
Typically the directory starts otherwise empty.

colcon performs out-of-source builds.
By default it will create the following directories as peers of the `src` directory:

- The `build` directory will be where intermediate files are stored.
  For each package a subfolder will be created in which e.g. CMake is being invoked.
- The `install` directory is where each package will be installed to.
  By default each package will be installed into a separate subdirectory.
- The `log` directory contains various logging information about each colcon invocation.

> [!NOTE]
>
> Compared to catkin there is no `devel` directory.

<a id="create-a-workspace"></a>

### Create a workspace

First, create a directory (`ros2_ws`) to contain our workspace:

Linux

```
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws
```

macOS

```
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws
```

Windows

```
$ md \dev\ros2_ws\src
$ cd \dev\ros2_ws
```

At this point the workspace contains a single empty directory `src`:

```
.
└── src

1 directory, 0 files
```

<a id="add-some-sources"></a>

### Add some sources

Let’s clone the [examples](https://github.com/ros2/examples) repository into the `src` directory of the workspace:

```
$ git clone https://github.com/ros2/examples src/examples -b jazzy
```

Now the workspace should have the source code to the ROS 2 examples:

```
.
└── src
    └── examples
        ├── CONTRIBUTING.md
        ├── LICENSE
        ├── rclcpp
        ├── rclpy
        └── README.md

4 directories, 3 files
```

<a id="source-an-underlay"></a>

### Source an underlay

It is important that we have sourced the environment for an existing ROS 2 installation that will provide our workspace with the necessary build dependencies for the example packages.
This is achieved by sourcing the setup script provided by a binary installation or a source installation, i.e. another colcon workspace (see [Installation](../../installation/overview.md)).
We call this environment an **underlay**.

Our workspace, `ros2_ws`, will be an **overlay** on top of the existing ROS 2 installation.
In general, it is recommended to use an overlay when you plan to iterate on a small number of packages, rather than putting all of your packages into the same workspace.

<a id="build-the-workspace"></a>

### Build the workspace

> [!ATTENTION]
>
> To build packages on Windows you need to be in a Visual Studio environment, see [Building the ROS 2 Code](../../installation/alternatives/windows-development-setup.md#windows-dev-build-ros2) for more details.

In the root of the workspace, run `colcon build`.
Since build types such as `ament_cmake` do not support the concept of the `devel` space and require the package to be installed, colcon supports the option `--symlink-install`.
This allows the installed files to be changed by changing the files in the `source` space (e.g. Python files or other non-compiled resources) for faster iteration.

Linux

```
$ colcon build --symlink-install
```

macOS

```
$ colcon build --symlink-install
```

Windows

```
$ colcon build --merge-install
```

Windows doesn’t allow long paths, so `merge-install` will combine all the paths into the `install` directory.
On Windows, you need special permissions to create symbolic links, so `--symlink-install` is not used by default.
To use it, you need to run the command as administrator or enable developer mode in system settings.

> [!TIP]
>
> Running `colcon build` may freeze the screen and mouse of systems that are CPU-, RAM- and I/O-limited (e.g., Raspberry Pi), so it might be useful to use the `--executor sequential` argument to build the packages one by one instead of using parallelism.
> See the [colcon documentation](https://colcon.readthedocs.io/en/released/reference/executor-arguments.html) for more arguments as needed.

After the build is finished, we should see the `build`, `install`, and `log` directories:

```
.
├── build
├── install
├── log
└── src

4 directories, 0 files
```

<a id="run-tests"></a>
<a id="colcon-run-the-tests"></a>

### Run tests

To run tests for the packages we just built, run the following:

Linux

```
$ colcon test
```

macOS

```
$ colcon test
```

Windows

Remember to use a `x64 Native Tools Command Prompt for VS 2019` for executing the following command, as we are going to build a workspace.

```
$ colcon test --merge-install
```

You also need to specify `--merge-install` here since we used it for building above.

<a id="source-the-environment"></a>
<a id="colcon-tutorial-source-the-environment"></a>

### Source the environment

When colcon has completed building successfully, the output will be in the `install` directory.
Before you can use any of the installed executables or libraries, you will need to add them to your path and library paths.
colcon will have generated bash/bat files in the `install` directory to help set up the environment.
These files will add all of the required elements to your path and library paths as well as provide any bash or shell commands exported by packages.

Linux

```
$ source install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

In a Windows command line interface:

```
$ call install\setup.bat
```

Or with Powershell:

```
$ install\setup.ps1
```

<a id="try-a-demo"></a>

### Try a demo

With the environment sourced, we can run executables built by colcon.
Let’s run a subscriber node from the examples:

```
$ ros2 run examples_rclcpp_minimal_subscriber subscriber_member_function
```

In another terminal, let’s run a publisher node (don’t forget to source the setup script):

```
$ ros2 run examples_rclcpp_minimal_publisher publisher_member_function
```

You should see messages from the publisher and subscriber with numbers incrementing.

<a id="create-your-own-package"></a>

## Create your own package

colcon uses the `package.xml` specification defined in [REP 149](https://reps.openrobotics.org/rep-0149/) ([format 2](https://reps.openrobotics.org/rep-0140/) is also supported).

colcon supports multiple build types.
The recommended build types are `ament_cmake` and `ament_python`.
Also supported are pure `cmake` packages.

An example of an `ament_python` build is the [ament\_index\_python package](https://github.com/ament/ament_index/tree/jazzy/ament_index_python) , where the setup.py is the primary entry point for building.

A package such as [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/jazzy/demo_nodes_cpp) uses the `ament_cmake` build type, and uses CMake as the build tool.

For convenience, you can use the tool `ros2 pkg create` to create a new package based on a template.
A full description of creating a package and how to use `ros2 pkg create` is in the upcoming tutorial [create a package](creating-your-first-ros2-package.md).

> [!NOTE]
>
> For `catkin` users, this is the equivalent of `catkin_create_package`.

<a id="setup-colcon-cd"></a>

## Setup `colcon_cd`

The command `colcon_cd` allows you to quickly change the current working directory of your shell to the directory of a package.
As an example `colcon_cd some_ros_package` would quickly bring you to the directory `~/ros2_ws/src/some_ros_package`.
To set up `colcon_cd` you need to run the following commands to modify your shell startup script:

Linux

```
$ echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
$ echo "export _colcon_cd_root=/opt/ros/jazzy/" >> ~/.bashrc
```

macOS

```
$ echo "source /usr/local/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
$ echo "export _colcon_cd_root=~/ros2_install" >> ~/.bashrc
```

Windows

Not yet available

Depending on the way you installed `colcon_cd` and where your workspace is, the instructions above may vary, please refer to [the documentation](https://colcon.readthedocs.io/en/released/user/installation.html#quick-directory-changes) for more details.
To undo this in Linux and macOS, locate your system’s shell startup script and remove the appended source and export commands.

<a id="setup-colcon-tab-completion"></a>

## Setup `colcon` tab completion

The `colcon` command supports command completion for bash and bash-like shells.
The `colcon-argcomplete` package must be installed, and [some setup may be required](https://colcon.readthedocs.io/en/released/user/installation.html#enable-completion) to make it work.

<a id="tips"></a>

## Tips

- If you do not want to build a specific package, then place an empty file named `COLCON_IGNORE` in the directory and it will not be indexed.
- If you want to avoid configuring and building tests in CMake packages you can pass: `--cmake-args -DBUILD_TESTING=0`.
- If you want to run a single particular test from a package:

  ```
  $ colcon test --packages-select YOUR_PKG_NAME --ctest-args -R YOUR_TEST_IN_PKG
  ```

<a id="setup-colcon-mixins"></a>

## Setup `colcon` mixins

Various command line options are tedious to write and/or difficult to remember.

For example, to change the CMake build type to debug, you normally use:

```
$ colcon build --cmake-args -DCMAKE_BUILD_TYPE=Debug
```

To make common command line options easier to invoke this repository makes these “shortcuts” available.

To install the default colcon mixins, run the following:

```
$ colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
$ colcon mixin update default
```

Then, try out using the `debug` mixin:

```
$ colcon build --mixin debug
```

For more details, see the [colcon mixin repository](https://github.com/colcon/colcon-mixin-repository).
