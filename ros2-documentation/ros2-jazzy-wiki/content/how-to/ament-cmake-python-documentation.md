---
title: "ament_cmake_python user documentation"
docname: "How-To-Guides/Ament-CMake-Python-Documentation"
source: "How-To-Guides/Ament-CMake-Python-Documentation.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md) | [Cross-compilation](cross-compilation.md)

<a id="ament-cmake-python-user-documentation"></a>

# ament\_cmake\_python user documentation

`ament_cmake_python` is a package that provides CMake functions for packages of the `ament_cmake` build type that contain Python code.
See the [ament\_cmake user documentation](ament-cmake-documentation.md) for more information.

> [!NOTE]
>
> Pure Python packages should use the `ament_python` build type in most cases.
> To create an `ament_python` package, see [Creating your first ROS 2 package](../tutorials/beginner-client-libraries/creating-your-first-ros2-package.md).
> `ament_cmake_python` should only be used in cases where that is not possible, like when mixing C/C++ and Python code.

Table of Contents

- [Basics](#basics)

  - [Basic project outline](#basic-project-outline)
  - [Using ament\_cmake\_python](#using-ament-cmake-python)
  - [Using ament\_cmake\_pytest](#using-ament-cmake-pytest)

<a id="basics"></a>

## Basics

<a id="basic-project-outline"></a>

### Basic project outline

The outline of a package called “my\_project” with the `ament_cmake` build type that uses `ament_cmake_python` looks like:

```
.
└── my_project
    ├── CMakeLists.txt
    ├── package.xml
    └── my_project
        ├── __init__.py
        └── my_script.py
```

The `__init__.py` file can be empty, but it is needed to [make Python treat the directory containing it as a package](https://docs.python.org/3/tutorial/modules.html#packages).
There can also be a `src` or `include` directory alongside the `CMakeLists.txt` which holds C/C++ code.

<a id="using-ament-cmake-python"></a>

### Using ament\_cmake\_python

The package must declare a dependency on `ament_cmake_python` in its `package.xml`.

```
<buildtool_depend>ament_cmake_python</buildtool_depend>
```

The `CMakeLists.txt` should contain:

```
find_package(ament_cmake_python REQUIRED)
# ...
ament_python_install_package(${PROJECT_NAME})
```

The argument to `ament_python_install_package()` is the name of the directory alongside the `CMakeLists.txt` that contains the Python file.
In this case, it is `my_project`, or `${PROJECT_NAME}`.

> [!WARNING]
>
> Calling `rosidl_generate_interfaces` and `ament_python_install_package` in the same CMake project does not work.
> See this [Github issue](https://github.com/ros2/rosidl_python/issues/141) for more info.
> It is best practice to instead separate out the message generation into a separate package.

Then, another Python package that correctly depends on `my_project` can use it as a normal Python module:

```
from my_project.my_script import my_function
```

Assuming `my_script.py` contains a function called `my_function()`.

<a id="using-ament-cmake-pytest"></a>

### Using ament\_cmake\_pytest

The package `ament_cmake_pytest` is used to make tests discoverable to `cmake`.
The package must declare a test dependency on `ament_cmake_pytest` in its `package.xml`.

```
<test_depend>ament_cmake_pytest</test_depend>
```

Say the package has a file structure like below, with tests in the `tests` folder.

```
.
├── CMakeLists.txt
├── my_project
│   └── my_script.py
├── package.xml
└── tests
    ├── test_a.py
    └── test_b.py
```

The `CMakeLists.txt` should contain:

```
if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  set(_pytest_tests
    tests/test_a.py
    tests/test_b.py
    # Add other test files here
  )
  foreach(_test_path ${_pytest_tests})
    get_filename_component(_test_name ${_test_path} NAME_WE)
    ament_add_pytest_test(${_test_name} ${_test_path}
      APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
      TIMEOUT 60
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    )
  endforeach()
endif()
```

Compared to the usage of ament\_python, which supports automatic test discovery, ament\_cmake\_pytest must be called with the path to each test file.
The timeout can be reduced as needed.

Now, you can invoke your tests with the [standard colcon testing commands](../tutorials/intermediate/testing/cli.md).
