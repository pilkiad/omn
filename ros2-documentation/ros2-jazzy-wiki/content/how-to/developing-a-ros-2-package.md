---
title: "Developing a ROS 2 package"
docname: "How-To-Guides/Developing-a-ROS-2-Package"
source: "How-To-Guides/Developing-a-ROS-2-Package.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="developing-a-ros-2-package"></a>

# Developing a ROS 2 package

Table of Contents

- [Prerequisites](#prerequisites)
- [Creating a package](#creating-a-package)

  - [C++ Packages](#c-packages)
  - [Python Packages](#python-packages)
  - [Combined C++ and Python Packages](#combined-c-and-python-packages)

This tutorial will teach you how to create your first ROS 2 application.
It is intended for developers who want to learn how to create custom packages in ROS 2, not for people who want to use ROS 2 with its existing packages.

<a id="prerequisites"></a>

## Prerequisites

- [Install ROS](../installation/overview.md)
- [Install colcon](https://colcon.readthedocs.io/en/released/user/installation.html)
- Setup your workspace by sourcing your ROS 2 installation.

<a id="creating-a-package"></a>

## Creating a package

All ROS 2 packages begin by running the command

```
$ ros2 pkg create --license Apache-2.0 <pkg-name> --dependencies [deps]
```

in your workspace (usually `~/ros2_ws/src`).

To create a package for a specific client library:

C++

```
$ ros2 pkg create  --build-type ament_cmake --license Apache-2.0 <pkg-name> --dependencies [deps]
```

Python

```
$ ros2 pkg create  --build-type ament_python --license Apache-2.0 <pkg-name> --dependencies [deps]
```

You can then update the `package.xml` with your package info such as dependencies, descriptions, and authorship.

<a id="c-packages"></a>

### C++ Packages

You will mostly use the `add_executable()` CMake macro along with

```
ament_target_dependencies(<executable-name> [dependencies])
```

to create executable nodes and link dependencies.

To install your launch files and nodes, you can use the `install()` macro placed towards the end of the file but before the `ament_package()` macro.

An example for launch files and nodes:

```
# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install nodes
install(
  TARGETS [node-names]
  DESTINATION lib/${PROJECT_NAME}
)
```

<a id="python-packages"></a>

### Python Packages

ROS 2 follows Python’s standard module distribution process that uses `setuptools`.
For Python packages, the `setup.py` file complements a C++ package’s `CMakeLists.txt`.
More details on distribution can be found in the [official documentation](https://docs.python.org/3/distributing/index.html#distributing-index).

In your ROS 2 package, you should have a `setup.cfg` file which looks like:

```
[develop]
script_dir=$base/lib/<package-name>
[install]
install_scripts=$base/lib/<package-name>
```

and a `setup.py` file that looks like:

```
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    # Packages to export
    packages=find_packages(exclude=['test']),
    # Files we want to install, specifically launch files
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    # This is important as well
    install_requires=['setuptools'],
    zip_safe=True,
    author='ROS 2 Developer',
    author_email='ros2@ros.com',
    maintainer='ROS 2 Developer',
    maintainer_email='ros2@ros.com',
    keywords=['foo', 'bar'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: TODO',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='My awesome package.',
    license='TODO',
    # Like the CMakeLists add_executable macro, you can add your python
    # scripts here.
    entry_points={
        'console_scripts': [
            'my_script = my_package.my_script:main'
        ],
    },
)
```

<a id="combined-c-and-python-packages"></a>

### Combined C++ and Python Packages

When writing a package with both C++ and Python code, the `setup.py` file and `setup.cfg` file are not used.
Instead, use [ament\_cmake\_python](ament-cmake-python-documentation.md).
