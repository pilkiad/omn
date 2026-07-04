---
title: "Using Python Packages with ROS 2"
docname: "How-To-Guides/Using-Python-Packages"
source: "How-To-Guides/Using-Python-Packages.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="using-python-packages-with-ros-2"></a>
<a id="pythonpackages"></a>

# Using Python Packages with ROS 2

**Goal:** Explain how to interoperate with other Python packages from the ROS 2 ecosystem.

Contents

- [Installing via `rosdep`](#installing-via-rosdep)
- [Installing via a package manager](#installing-via-a-package-manager)
- [Installing via a virtual environment](#installing-via-a-virtual-environment)
> [!NOTE]
>
> A cautionary note, if you intended to use pre-packaged binaries (either `deb` files, or the binary archive distributions), the Python interpreter must match what was used to build the original binaries.
> If you intend to use something like `virtualenv` or `pipenv`, make sure to use the system interpreter.
> If you use something like `conda`, it is very likely that the interpreter will not match the system interpreter and will be incompatible with ROS 2 binaries.

<a id="installing-via-rosdep"></a>

## Installing via `rosdep`

The fastest way to include third-party python packages is to use their corresponding rosdep keys, if available.
`rosdep` keys can be checked via:

- <https://github.com/ros/rosdistro/blob/master/rosdep/base.yaml>
- <https://github.com/ros/rosdistro/blob/master/rosdep/python.yaml>

These `rosdep` keys can be added to your `package.xml` file, which indicates to the build system that your package (and dependent packages) depend on those keys.
In a new workspace, you can also quickly install all rosdep keys with:

```
$ rosdep install -yr --from-paths ./path/to/your/workspace
```

If there aren’t currently `rosdep` keys for the package that you are interested in, it is possible to add them by following the [rosdep key contribution guide](http://docs.ros.org/en/independent/api/rosdep/html/contributing_rules.html).

To learn more about the `rosdep` tool and how it works, consult the [rosdep documentation](http://docs.ros.org/en/independent/api/rosdep/html/).

<a id="installing-via-a-package-manager"></a>

## Installing via a package manager

If you don’t want to make a rosdep key, but the package is available in your system package manager (eg `apt`), you can install and use the package that way:

```
$ sudo apt install python3-serial
```

If the package is available on [The Python Package Index (PyPI)](https://pypi.org/) and you want to install globally on your system:

```
$ python3 -m pip install -U pyserial
```

If the package is available on PyPI and you want to install locally to your user:

```
$ python3 -m pip install -U --user pyserial
```

<a id="installing-via-a-virtual-environment"></a>

## Installing via a virtual environment

First, create a Colcon workspace:

```
$ mkdir -p ~/colcon_venv/src
$ cd ~/colcon_venv/
```

Then setup your virtual environment:

```
$ virtualenv -p python3 ./venv # Make a virtual env and activate it
$ source ./venv/bin/activate
$ touch ./venv/COLCON_IGNORE # Make sure that colcon does not try to build the venv
```

Next, install the Python packages that you want in your virtual environment:

```
$ python3 -m pip install gtsam pyserial… etc
```

Now you can build your workspace and run your python node that depends on packages installed in your virtual environment.

```
$ source /opt/ros/jazzy/setup.bash # Source Jazzy and build
$ colcon build
```

> [!NOTE]
>
> If you want to release your package using Bloom, you should add the packages you require to `rosdep`, see the [rosdep key contribution guide](http://docs.ros.org/en/independent/api/rosdep/html/contributing_rules.html).
