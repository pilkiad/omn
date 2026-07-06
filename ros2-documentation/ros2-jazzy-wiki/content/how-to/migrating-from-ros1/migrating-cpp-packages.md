---
title: "Migrating C++ Packages Reference"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-CPP-Packages"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-CPP-Packages.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating Interfaces](migrating-interfaces.md)

<a id="migrating-c-packages-reference"></a>

# Migrating C++ Packages Reference

Table of Contents

- [Build tool](#build-tool)
- [Update your `CMakeLists.txt` to use *ament\_cmake*](#update-your-cmakelists-txt-to-use-ament-cmake)

  - [Require a newer version of CMake](#require-a-newer-version-of-cmake)
  - [Set the build type to ament\_cmake](#set-the-build-type-to-ament-cmake)
  - [Add a call to `ament_package()`](#add-a-call-to-ament-package)
  - [Update `find_package()` calls](#update-find-package-calls)
  - [Use modern CMake targets](#use-modern-cmake-targets)
  - [Replace `catkin_package()` with various ament\_cmake calls](#replace-catkin-package-with-various-ament-cmake-calls)
  - [Generate messages](#generate-messages)
  - [Remove references to the devel space](#remove-references-to-the-devel-space)
  - [Unit tests](#unit-tests)
  - [Linters](#linters)
- [Update source code](#update-source-code)

  - [Messages, services, and actions](#messages-services-and-actions)
  - [Use of service objects](#use-of-service-objects)
  - [Usages of ros::Time](#usages-of-ros-time)
  - [Usages of ros::Rate](#usages-of-ros-rate)
  - [Boost](#boost)

This page shows how to migrate parts of a C++ package from ROS 1 to ROS 2.
If this is your first time migrating a C++ package, then read the [C++ migration example](migrating-cpp-package-example.md) first.
Afterwards, use this page as a reference while you migrate your own packages.

<a id="build-tool"></a>

## Build tool

Instead of using `catkin_make`, `catkin_make_isolated` or `catkin build` ROS 2 uses the command line tool [colcon](https://design.ros2.org/articles/build_tool.html) to build and install a set of packages.
See the [beginner tutorial](../../tutorials/beginner-client-libraries/colcon-tutorial.md) to get started with `colcon`.

<a id="update-your-cmakelists-txt-to-use-ament-cmake"></a>

## Update your `CMakeLists.txt` to use *ament\_cmake*

ROS 2 C++ packages use [CMake](https://cmake.org/) with convenience functions provided by [ament\_cmake](https://index.ros.org/p/ament_cmake/).
Apply the following changes to use `ament_cmake` instead of `catkin`.

<a id="require-a-newer-version-of-cmake"></a>

### Require a newer version of CMake

ROS 2 relies on newer versions of CMake than used by ROS 1.
Find the minimum version of CMake used by the ROS distribution you want to support in [REP 2000](https://reps.openrobotics.org/rep-2000/), and use that version at the top of your `CMakeLists.txt`.
For example, [3.14.4 is the minimum recommended support for ROS Humble](https://reps.openrobotics.org/rep-2000/#humble-hawksbill-may-2022-may-2027).

```
cmake_minimum_required(VERSION 3.14.4)
```

<a id="set-the-build-type-to-ament-cmake"></a>

### Set the build type to ament\_cmake

Remove any dependencies on `catkin` from your `package.xml`

```
# Remove this!
<buildtool_depend>catkin</buildtool_depend>
```

Add a new dependency on `ament_cmake_ros` ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L25)):

```
<buildtool_depend>ament_cmake_ros</buildtool_depend>
```

Add an `<export>` section to your `package.xml` if it does not have one already.
Set the `<build_type>` to `ament_cmake` ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L43-L45))

```
<export>
   <build_type>ament_cmake</build_type>
</export>
```

<a id="add-a-call-to-ament-package"></a>

### Add a call to `ament_package()`

Insert a call to `ament_package()` at the bottom of your `CMakeLists.txt` ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L127))

```
# Add this to the bottom of your CMakeLists.txt
ament_package()
```

<a id="update-find-package-calls"></a>

### Update `find_package()` calls

Replace the `find_package(catkin COMPONENTS ...)` call with individual `find_package()` calls ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L14-L18)):

For example, change this:

```
find_package(catkin REQUIRED COMPONENTS foo bar std_msgs)
find_package(baz REQUIRED)
```

To this:

```
find_package(ament_cmake_ros REQUIRED)
find_package(foo REQUIRED)
find_package(bar REQUIRED)
find_package(std_msgs REQUIRED)
find_package(baz REQUIRED)
```

<a id="use-modern-cmake-targets"></a>

### Use modern CMake targets

Prefer to use per-target CMake functions so that your package can export modern CMake targets.

If your `CMakeLists.txt` uses `include_directories()`, then delete those calls.

```
# Delete calls to include_directories like this one!
include_directories(include ${catkin_INCLUDE_DIRS})
```

Add a call `target_include_directories()` for every library in your package ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L24-L26)).

```
target_include_directories(my_library PUBLIC
   "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
   "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")
```

Change all `target_link_libraries()` calls to use modern CMake targets.
For example, if your package in ROS 1 uses old-style standard CMake variables like this.

```
target_link_libraries(my_library ${catkin_LIBRARIES} ${baz_LIBRARIES})
```

Then change it to use specific modern CMake targets instead.
Use `${package_name_TARGETS}` if the package you’re depending on is a message package such as `std_msgs`.

```
target_link_libraries(my_library PUBLIC foo::foo bar::bar ${std_msgs_TARGETS} baz::baz)
```

Choose `PUBLIC` or `PRIVATE` based on how the dependency is used by your library ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L27-L31)).

- Use `PUBLIC` if the dependency is needed by downstream users, for example, your library’s public API uses it.
- Use `PRIVATE` if the dependency is only used internally by your library.

<a id="replace-catkin-package-with-various-ament-cmake-calls"></a>

### Replace `catkin_package()` with various ament\_cmake calls

Imagine your `CMakeLists.txt` has a call to `catkin_package` like this:

```
catkin_package(
    INCLUDE_DIRS include
    LIBRARIES my_library
    CATKIN_DEPENDS foo bar std_msgs
    DEPENDS baz
)

install(TARGETS my_library
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
)
```

<a id="replacing-catkin-package-include-dirs"></a>

#### Replacing `catkin_package(INCLUDE_DIRS ...)`

If you’ve used modern CMake targets and `target_include_directories()`, you don’t need to do anything further.
Downstream users will get the include directories by depending on your modern CMake targets.

<a id="replacing-catkin-package-libraries"></a>

#### Replacing `catkin_package(LIBRARIES ...)`

Use `ament_export_targets()` and `install(TARGETS ... EXPORT ...)` to replace the `LIBRARIES` argument.

Use the `EXPORT` keyword when installing your `my_library` target ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L37-L41)).

```
install(TARGETS my_library EXPORT export_my_package
   ARCHIVE DESTINATION lib
   LIBRARY DESTINATION lib
   RUNTIME DESTINATION bin
)
```

The above is a good default for library targets.
If your package used different `CATKIN_*_DESTINATION` variables, convert them as follows:

| **catkin** | **ament\_cmake** |
| --- | --- |
| CATKIN\_GLOBAL\_BIN\_DESTINATION | bin |
| CATKIN\_GLOBAL\_INCLUDE\_DESTINATION | include |
| CATKIN\_GLOBAL\_LIB\_DESTINATION | lib |
| CATKIN\_GLOBAL\_LIBEXEC\_DESTINATION | lib |
| CATKIN\_GLOBAL\_SHARE\_DESTINATION | share |
| CATKIN\_PACKAGE\_BIN\_DESTINATION | lib/${PROJECT\_NAME} |
| CATKIN\_PACKAGE\_INCLUDE\_DESTINATION | include/${PROJECT\_NAME} |
| CATKIN\_PACKAGE\_LIB\_DESTINATION | lib |
| CATKIN\_PACKAGE\_SHARE\_DESTINATION | share/${PROJECT\_NAME} |

Add a call to `ament_export_targets()` with the same name you gave to the `EXPORT` keyword ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L124-L125)).

```
ament_export_targets(export_my_package)
```

<a id="replacing-catkin-package-catkin-depends-depends"></a>

#### Replacing `catkin_package(CATKIN_DEPENDS .. DEPENDS ..)`

Your package’s users must `find_package()` dependencies used by your package’s public API.
In ROS 1 this was done for downstream users with the `CATKIN_DEPENDS` and `DEPENDS` arguments.
Use [ament\_export\_dependencies](https://github.com/ament/ament_cmake/blob/jazzy/ament_cmake_export_dependencies/cmake/ament_export_dependencies.cmake) to do this in ROS 2.

```
ament_export_dependencies(
   foo
   bar
   std_msgs
   baz
)
```

<a id="generate-messages"></a>

### Generate messages

If your package contains both C++ code and ROS message, service, or action definitions, then consider splitting it into two packages:

- A package with only the ROS message, service, and/or action definitions
- A package with the C++ code

Add the following dependencies to the `package.xml` of the package that contains ROS messages:

1. Add a `<buildtool_depend>` on `rosidl_default_generators` ([example](https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L19))

   ```
   <buildtool_depend>rosidl_default_generators</buildtool_depend>
   ```
2. Add an `<exec_depend>` on `rosidl_default_runtime` ([example](https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L22))

   ```
   <exec_depend>rosidl_default_runtime</exec_depend>
   ```
3. Add a `<member_of_group>` tag with the group name `rosidl_interface_packages` ([example](https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L26))

   ```
   <member_of_group>rosidl_interface_packages</member_of_group>
   ```

In your `CMakeLists.txt`, replace the invocation of `add_message_files`, `add_service_files` and `generate_messages` with [rosidl\_generate\_interfaces](https://github.com/ros2/rosidl/blob/jazzy/rosidl_cmake/cmake/rosidl_generate_interfaces.cmake).
The first argument must be `${PROJECT_NAME}` due to [this bug](https://github.com/ros2/rosidl_typesupport/issues/120).

For example, if your ROS 1 package looks like this:

```
add_message_files(DIRECTORY msg FILES FooBar.msg Baz.msg)
add_service_files(DIRECTORY srv FILES Ping.srv)

add_action_files(DIRECTORY action FILES DoPong.action)
generate_messages(
   DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
)
```

Then change it to this ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2_msgs/CMakeLists.txt#L18-L25))

```
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/FooBar.msg"
  "msg/Baz.msg"
  "srv/Ping.srv"
  "action/DoPong.action"
  DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
)
```

<a id="remove-references-to-the-devel-space"></a>

### Remove references to the devel space

Remove any references to the *devel space* such as `CATKIN_DEVEL_PREFIX`.
There is no equivalent to the *devel space* in ROS 2.

<a id="unit-tests"></a>

### Unit tests

If your package uses [gtest](https://github.com/google/googletest) then:

- Replace `CATKIN_ENABLE_TESTING` with `BUILD_TESTING`.
- Replace `catkin_add_gtest` with `ament_add_gtest`.
- Add a `find_package()` for `ament_cmake_gtest` instead of `GTest`

For example, if your ROS 1 package adds tests like this:

```
if (CATKIN_ENABLE_TESTING)
  find_package(GTest REQUIRED)
  include_directories(${GTEST_INCLUDE_DIRS})
  catkin_add_gtest(my_test src/test/some_test.cpp)
  target_link_libraries(my_test
    # ...
    ${GTEST_LIBRARIES})
endif()
```

Then change it to this:

```
if (BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  ament_add_gtest(my_test src/test/test_something.cpp)
  target_link_libraries(my_test
    #...
   )
endif()
```

Add `<test_depend>ament_cmake_gtest</test_depend>` to your `package.xml` ([example](https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L35)).

```
<test_depend>ament_cmake_gtest</test_depend>
```

<a id="linters"></a>

### Linters

The ROS 2 code [style guide](../../project/contributing/developer-guide.md) differs from ROS 1.

If you choose to follow the ROS 2 style guide, then turn on automatic linter tests by adding these lines in a `if(BUILD_TESTING)` block:

```
if(BUILD_TESTING)
   find_package(ament_lint_auto REQUIRED)
   ament_lint_auto_find_test_dependencies()
   # ...
endif()
```

Add the following dependencies to your `package.xml`:

```
<test_depend>ament_lint_auto</test_depend>
<test_depend>ament_lint_common</test_depend>
```

<a id="update-source-code"></a>

## Update source code

<a id="messages-services-and-actions"></a>

### Messages, services, and actions

The namespace of ROS 2 messages, services, and actions use a subnamespace (`msg`, `srv`, or `action`, respectively) after the package name.
Therefore an include looks like: `#include <my_interfaces/msg/my_message.hpp>`.
The C++ type is then named: `my_interfaces::msg::MyMessage`.

Shared pointer types are provided as typedefs within the message structs: `my_interfaces::msg::MyMessage::SharedPtr` as well as `my_interfaces::msg::MyMessage::ConstSharedPtr`.

For more details please see the article about the [generated C++ interfaces](https://design.ros2.org/articles/generated_interfaces_cpp.html).

The migration requires includes to change by:

- inserting the subfolder `msg` between the package name and message datatype
- changing the included filename from CamelCase to underscore separation
- changing from `*.h` to `*.hpp`

```
// ROS 1 style is in comments, ROS 2 follows, uncommented.
// # include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/msg/point_stamped.hpp>

// geometry_msgs::PointStamped point_stamped;
geometry_msgs::msg::PointStamped point_stamped;
```

The migration requires code to insert the `msg` namespace into all instances.

<a id="use-of-service-objects"></a>

### Use of service objects

Service callbacks in ROS 2 do not have boolean return values.
Instead of returning false on failures, throwing exceptions is recommended.

```
// ROS 1 style is in comments, ROS 2 follows, uncommented.
// #include "nav_msgs/GetMap.h"
#include "nav_msgs/srv/get_map.hpp"

// bool service_callback(
//   nav_msgs::GetMap::Request & request,
//   nav_msgs::GetMap::Response & response)
void service_callback(
  const std::shared_ptr<nav_msgs::srv::GetMap::Request> request,
  std::shared_ptr<nav_msgs::srv::GetMap::Response> response)
{
  // ...
  // return true;  // or false for failure
}
```

<a id="usages-of-ros-time"></a>

### Usages of ros::Time

For usages of `ros::Time`:

- Replace all instances of `ros::Time` with `rclcpp::Time`
- If your messages or code makes use of std\_msgs::Time:

  - Convert all instances of std\_msgs::Time to builtin\_interfaces::msg::Time
  - Convert all `#include "std_msgs/time.h` to `#include "builtin_interfaces/msg/time.hpp"`
  - Convert all instances using the std\_msgs::Time field `nsec` to the builtin\_interfaces::msg::Time field `nanosec`

<a id="usages-of-ros-rate"></a>

### Usages of ros::Rate

There is an equivalent type `rclcpp::Rate` object which is basically a drop in replacement for `ros::Rate`.

<a id="boost"></a>

### Boost

Much of the functionality previously provided by Boost has been integrated into the C++ standard library.
As such we would like to take advantage of the new core features and avoid the dependency on boost where possible.

<a id="shared-pointers"></a>

#### Shared Pointers

To switch shared pointers from boost to standard C++ replace instances of:

- `#include <boost/shared_ptr.hpp>` with `#include <memory>`
- `boost::shared_ptr` with `std::shared_ptr`

There may also be variants such as `weak_ptr` which you want to convert as well.

Also it is recommended practice to use `using` instead of `typedef`.
`using` has the ability to work better in templated logic.
For details [see here](https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11)

<a id="thread-mutexes"></a>

#### Thread/Mutexes

Another common part of boost used in ROS codebases are mutexes in `boost::thread`.

- Replace `boost::mutex::scoped_lock` with `std::unique_lock<std::mutex>`
- Replace `boost::mutex` with `std::mutex`
- Replace `#include <boost/thread/mutex.hpp>` with `#include <mutex>`

<a id="unordered-map"></a>

#### Unordered Map

Replace:

- `#include <boost/unordered_map.hpp>` with `#include <unordered_map>`
- `boost::unordered_map` with `std::unordered_map`

<a id="function"></a>

#### function

Replace:

- `#include <boost/function.hpp>` with `#include <functional>`
- `boost::function` with `std::function`
