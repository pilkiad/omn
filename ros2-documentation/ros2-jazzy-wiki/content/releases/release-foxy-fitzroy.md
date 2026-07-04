---
title: "Foxy Fitzroy ( foxy )"
docname: "Releases/Release-Foxy-Fitzroy"
source: "Releases/Release-Foxy-Fitzroy.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="foxy-fitzroy-foxy"></a>

# Foxy Fitzroy (`foxy`)

Table of Contents

- [Supported Platforms](#supported-platforms)
- [Installation](#installation)
- [New features in this ROS 2 release](#new-features-in-this-ros-2-release)
- [Changes in Patch Release 8 (2022-09-28)](#changes-in-patch-release-8-2022-09-28)

  - [Launch GroupAction scopes environment](#launch-groupaction-scopes-environment)
- [Changes in Patch Release 7 (2022-02-08)](#changes-in-patch-release-7-2022-02-08)

  - [Launch set\_env frontend behavior change](#launch-set-env-frontend-behavior-change)
  - [Fix launch frontend parser](#fix-launch-frontend-parser)
  - [Fix memory leaks and undefined behavior in rmw\_fastrtps\_dynamic\_cpp](#fix-memory-leaks-and-undefined-behavior-in-rmw-fastrtps-dynamic-cpp)
- [Changes in Patch Release 2 (2020-08-07)](#changes-in-patch-release-2-2020-08-07)

  - [Bug in static\_transform\_publisher](#bug-in-static-transform-publisher)
- [Changes since the Eloquent release](#changes-since-the-eloquent-release)

  - [Classic CMake vs. modern CMake](#classic-cmake-vs-modern-cmake)
  - [ament\_export\_interfaces replaced by ament\_export\_targets](#ament-export-interfaces-replaced-by-ament-export-targets)
  - [rosidl\_generator\_c|cpp namespace / API changes](#rosidl-generator-c-cpp-namespace-api-changes)
  - [Default working directory for ament\_add\_test](#default-working-directory-for-ament-add-test)
  - [Default Console Logging Format](#default-console-logging-format)
  - [Default Console Logging Output Stream](#default-console-logging-output-stream)
  - [launch\_ros](#launch-ros)
  - [rclcpp](#rclcpp)
  - [rclcpp\_action](#rclcpp-action)
  - [rclpy](#rclpy)
  - [rmw\_connext\_cpp](#rmw-connext-cpp)
  - [rviz](#rviz)
  - [std\_msgs](#std-msgs)
  - [Security features](#security-features)
- [Known Issues](#known-issues)
- [Timeline before the release](#timeline-before-the-release)

*Foxy Fitzroy* is the sixth release of ROS 2.

<a id="supported-platforms"></a>

## Supported Platforms

Foxy Fitzroy supports the following platforms according to [the platform support tiers](../project/platform-support-tiers.md):

Tier 1 platforms:

- Ubuntu 20.04 (Focal): `amd64` and `arm64`
- Mac macOS 10.14 (Mojave)
- Windows 10 (Visual Studio 2019)

Tier 3 platforms:

- Ubuntu 20.04 (Focal): `arm32`
- Debian Buster (10): `amd64`, `arm64` and `arm32`
- OpenEmbedded Thud (2.6) / webOS OSE: `arm32` and `x86`

Targeted platforms:

| Architecture | Ubuntu Focal (20.04) | MacOS Mojave (10.14) | Windows 10 (VS2019) | Debian Buster (10) | OpenEmbedded / webOS OSE |
| --- | --- | --- | --- | --- | --- |
| amd64 | Tier 1 [d][a][s] | Tier 1 [a][s] | Tier 1 [a][s] | Tier 3 [s] |  |
| arm64 | Tier 1 [d][a][s] |  |  | Tier 3 [s] | Tier 3 [s] |
| arm32 | Tier 3 [s] |  |  | Tier 3 [s] | Tier 3 [s] |

The following indicators show what delivery mechanisms are available for
each platform.

" [d] " Debian packages will be provided for this platform for
packages submitted to the rosdistro.

" [a] " Binary releases are provided as a single archive per
platform containing all packages in the Foxy ROS 2 repos file[^9].

" [s] " Compilation from source.

Middleware Implementation Support:

| Middleware Library | Middleware Provider | Support Level | Platforms | Architectures |
| --- | --- | --- | --- | --- |
| rmw\_fastrtps\_cpp\* | eProsima Fast-RTPS | Tier 1 | All Platforms | All Architectures |
| rmw\_cyclonedds\_cpp | Eclipse Cyclone DDS | Tier 1 | All Platforms | All Architectures |
| rmw\_connext\_cpp | RTI Connext | Tier 1 | All Platforms except Debian and OpenEmbedded | All Architectures except arm64/arm32 |
| rmw\_fastrtps\_dynamic\_cpp | eProsima Fast-RTPS | Tier 2 | All Platforms | All Architectures |
| rmw\_gurumdds\_cpp | GurumNetworks GurumDDS | Tier 3 | Ubuntu and Windows | All Architectures except arm32 |

" \* " means default RMW implementation.

Middleware implementation support is dependent upon the platform support
tier. For example a Tier 1 middleware implementation on a Tier 2
platform can only receive Tier 2 support.

Minimum language requirements:

- C++14
- Python 3.7

Dependency Requirements:

|  | Required Support | | | Recommended Support | |
| --- | --- | --- | --- | --- | --- |
| Package | Ubuntu Focal | MacOS\*\* | Windows 10\*\* | Debian Buster | OpenEmbedded\*\* |
| CMake | 3.16.3 | 3.14.4 | 3.14.4 | 3.13.4 | 3.16.1 / 3.12.2\*\*\*\* |
| EmPY | 3.3.2 | | | | |
| Gazebo | 11.0.0\* | 11.0.0 | N/A | 11.0.0\* | N/A |
| Ignition | Citadel\* | | N/A | Citadel\* | N/A |
| Ogre | 1.10\* | | | | N/A |
| OpenCV | 4.2.0 | 4.2.0 | 3.4.6\* | 3.2.0 | 4.1.0 / 3.2.0\*\*\*\* |
| OpenSSL | 1.1.1d | 1.1.1f | 1.1.1f | 1.1.1d | 1.1.1d / 1.1.1b\*\*\*\* |
| Poco | 1.9.2 | 1.9.0 | 1.8.0\* | 1.9.0 | 1.9.4 |
| Python | 3.8.0 | 3.8.2 | 3.8.0 | 3.7.3 | 3.8.2 / 3.7.5\*\*\*\* |
| Qt | 5.12.5 | 5.12.3 | 5.10.0 | 5.11.3 | 5.14.1 / 5.12.5\*\*\*\* |
|  | | **Linux only** | | | |
| PCL | 1.10.0 | N/A | N/A | 1.9.1 | 1.10.0 |
| **RMW DDS Middleware Providers** | | | | | |
| Connext DDS | 5.3.1 | | | N/A | |
| Cyclone DDS | 0.7.x (Coquette) | | | | |
| Fast-RTPS | 2.0.x | | | | |
| Gurum DDS | 2.7.x | N/A | 2.7.x | N/A | |

" \* " means that this is not the upstream version (available on the
official Operating System repositories) but a package distributed by
OSRF or the community (package built and distributed on custom
repositories).

" \*\* " Rolling distributions will see multiple version changes of
these dependencies during their lifetime. The versions shown for
OpenEmbedded are those provided by the 3.1 Dunfell release series; the
versions provided by the other supported release series are listed here:
<<https://github.com/ros/meta-ros/wiki/Package-Version-Differences>> .
Note that the OpenEmbedded releases series for which a ROS distro has
support will change during its support time frame, as per the
OpenEmbedded support policy shown here:
<<https://github.com/ros/meta-ros/wiki/Policies#openembedded-release-series-support>>
. However, it will always be supported by least one stable OpenEmbedded
release series.

" \*\*\*\* " webOS OSE provides this different version.

This document only captures the version at the first release of a ROS
distribution and will not be updated as the dependencies move forward.
These versions are thus a low watermark.

Package manager use for dependencies:

- Ubuntu, Debian: apt
- MacOS: Homebrew, pip
- Windows: Chocolatey, pip
- OpenEmbedded: opkg

Build System Support:

- ament\_cmake
- cmake
- setuptools

<a id="installation"></a>

## Installation

[Install Foxy Fitzroy](https://docs.ros.org/en/foxy/Installation.html)

<a id="new-features-in-this-ros-2-release"></a>

## New features in this ROS 2 release

During the development the [Foxy meta-ticket](https://github.com/ros2/ros2/issues/830) on GitHub contains an up-to-date state of the ongoing high-level tasks as well as references specific tickets with more details.

<a id="changes-in-patch-release-8-2022-09-28"></a>

## Changes in Patch Release 8 (2022-09-28)

<a id="launch-groupaction-scopes-environment"></a>

### Launch GroupAction scopes environment

The `SetEnvironmentVariable` action is now scoped to any `GroupAction` it is returned from.

For example, consider the following launch files,

Python

```
import launch
from launch.actions import SetEnvironmentVariable
from launch.actions import GroupAction
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        SetEnvironmentVariable(name='my_env_var', value='1'),
        Node(package='foo', executable='foo', output='screen'),
        GroupAction([
            SetEnvironmentVariable(name='my_env_var', value='2'),
        ]),
    ])
```

XML

```
<launch>
  <set_env name="my_env_var" value="1"/>
  <node pkg="foo" exec="foo" output="screen" />
  <group>
    <set_env name="my_env_var" value="2"/>
  </group>
</launch>
```

Before patch release 8, the node `foo` will start with `my_env_var=2`, but now it will start with `my_env_var=1`.

To opt-out of the new behavior, you can set the argument `scoped=False` on the `GroupAction`.

Related tickets:

- [ros2#1244](https://github.com/ros2/ros2/issues/1244)
- [launch#630](https://github.com/ros2/launch/pull/630)

<a id="changes-in-patch-release-7-2022-02-08"></a>

## Changes in Patch Release 7 (2022-02-08)

<a id="launch-set-env-frontend-behavior-change"></a>

### Launch set\_env frontend behavior change

[launch#468](https://github.com/ros2/launch/pull/468) inadvertently changed behavior to the scope of the `set_env` action in frontend launch files.
Changes to environment variables using the `set_env` action are no longer scoped to parent `group` actions, and instead apply globally.
Since it was backported, the change affects this release.

We consider this change a regression and intend to fix the behavior in the next patch release and in future ROS distributions.
We also plan to fix the behavior in Python launch files, which have never scoped setting environment variables properly.

Related issues:

- [ros2#1244](https://github.com/ros2/ros2/issues/1244)
- [launch#597](https://github.com/ros2/launch/issues/597)

<a id="fix-launch-frontend-parser"></a>

### Fix launch frontend parser

A refactor of the launch frontend parser fixed some [issues parsing special characters](https://github.com/ros2/launch_ros/issues/214).
As a result, there has been a small behavior change when it comes to parsing strings.
For example, previously to pass a number as a string you would have to add extra quotation marks (two sets of quotation marks were needed if using a substitution):

```
<!-- results in the string value "'3'" -->
<param name="foo" value="''3''"/>
```

After the refactor, the above will result in the the string `"''3''"` (note the extra set of quotation marks).
Now, users should use the `type` attribute to signal that the value should be interpreted as a string:

```
<param name="foo" value="3" type="str"/>
```

Related pull requests:

- [launch#530](https://github.com/ros2/launch/pull/530)
- [launch\_ros#265](https://github.com/ros2/launch_ros/pull/265)

<a id="fix-memory-leaks-and-undefined-behavior-in-rmw-fastrtps-dynamic-cpp"></a>

### Fix memory leaks and undefined behavior in rmw\_fastrtps\_dynamic\_cpp

API was changed in the following header files:

- `rmw_fastrtps_dynamic_cpp/TypeSupport.hpp`
- `rmw_fastrtps_dynamic_cpp/TypeSupport_impl.hpp`

Though technically they are publically accessible, it is unlikely people are using them directly.
Therefore, we decided to break API in order to fix memory leaks and undefined behavior.

The fix was originally submitted in [rmw\_fastrtps#429](https://github.com/ros2/rmw_fastrtps/pull/429) and later backported to Foxy in [rmw\_fastrtps#577](https://github.com/ros2/rmw_fastrtps/pull/577).

<a id="changes-in-patch-release-2-2020-08-07"></a>

## Changes in Patch Release 2 (2020-08-07)

<a id="bug-in-static-transform-publisher"></a>

### Bug in static\_transform\_publisher

During the development of Foxy, a bug was introduced into the tf2\_ros static\_transform\_publisher program.
The implementation of the order of the Euler angles passed to static\_transform\_publisher disagrees with the documentation.
Foxy patch release 2 [fixes](https://github.com/ros2/geometry2/pull/296) the order so that the implementation agrees with the documentation (yaw, pitch, roll).
For users who have started using the initial Foxy release or patch release 1, this means that any launch files that use static\_transform\_publisher will have to have the command-line order swapped according to the new order.
For users who are coming from ROS 2 Dashing, ROS 2 Eloquent, or ROS 1, no changes need to be made to port to Foxy patch release 2.

<a id="changes-since-the-eloquent-release"></a>

## Changes since the Eloquent release

<a id="classic-cmake-vs-modern-cmake"></a>

### Classic CMake vs. modern CMake

In “classic” CMake a package provides CMake variables like `<pkgname>_INCLUDE_DIRS` and `<pkgname>_LIBRARIES` when being `find_package()`-ed.
With `ament_cmake` that is achieved by calling `ament_export_include_directories` and `ament_export_libraries`.
In combination with `ament_export_dependencies`, `ament_cmake` ensures that all include directories and libraries of recursive dependencies are concatenated and included in these variables.

In “modern” CMake a package provides an interface target instead (commonly named `<pkgname>::<pkgname>`) which in itself encapsulates all recursive dependencies.
In order to export a library target to use modern CMake `ament_export_targets` needs to be called with an export name which is also used when installing the libraries using `install(TARGETS <libA> <libB> EXPORT <export_name> ...)`.
The exported interface targets are available through the CMake variable `<pkgname>_TARGETS`.
For library targets to be exportable like this they must not rely on classic functions affecting global state like `include_directories()` but set the include directories on the target itself - for the build as well as install environment - using generator expressions, e.g. `target_include_directories(<target> PUBLIC "$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>" "$<INSTALL_INTERFACE:include>")`.

When `ament_target_dependencies` is used to add dependencies to a library target the function uses modern CMake targets when they are available.
Otherwise it falls back to using classic CMake variables.
As a consequence you should only export modern CMake targets if all dependencies are also providing modern CMake targets.
**Otherwise the exported interface target will contain the absolute paths to include directories / libraries in the generated CMake logic which makes the package non-relocatable.**

For examples how packages have been updated to modern CMake in Foxy see [ros2/ros2#904](https://github.com/ros2/ros2/issues/904).

<a id="ament-export-interfaces-replaced-by-ament-export-targets"></a>

### ament\_export\_interfaces replaced by ament\_export\_targets

The CMake function `ament_export_interfaces` from the package `ament_cmake_export_interfaces` has been deprecated in favor of the function `ament_export_targets` in the new package `ament_cmake_export_targets`.
See the GitHub ticket [ament/ament\_cmake#237](https://github.com/ament/ament_cmake/issues/237) for more context.

<a id="rosidl-generator-c-cpp-namespace-api-changes"></a>

### rosidl\_generator\_c|cpp namespace / API changes

The packages `rosidl_generator_c` and `rosidl_generator_cpp` have been refactored with many headers and sources moved into the new packages `rosidl_runtime_c` and `rosidl_runtime_cpp`.
The intention is to remove run dependencies on the generator packages and therefore the code generation tools using Python.
While moving the headers the include paths / namespaces were updated accordingly so in many cases changing include directives from the generator package to the runtime package is sufficient.

The generated C / C++ code has also been refactored.
The files ending in `__struct.h|hpp`, `__functions.h`, `__traits.hpp`, etc. have been moved into a subdirectory `detail` but most code only includes the header named after the interface without any of these suffixes.

Some types regarding string and sequence bounds have also been renamed to match the naming conventions but they aren’t expected to be used in user code (above RMW implementation and type support packages)

For more information see [ros2/rosidl#446 (for C)](https://github.com/ros2/rosidl/issues/446) and [ros2/rosidl#447 (for C++)](https://github.com/ros2/rosidl/issues/447).

<a id="default-working-directory-for-ament-add-test"></a>

### Default working directory for ament\_add\_test

The default working directory for tests added with `ament_add_test` has been changed to `CMAKE_CURRENT_BINARY_DIR` to match the behavior of CMake `add_test`.
Either update the tests to work with the new default or pass `WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}` to restore the previous value.

<a id="default-console-logging-format"></a>

### Default Console Logging Format

The default console logging output format was changed to include the timestamp by default, see:

- <https://github.com/ros2/rcutils/pull/190>
- <https://discourse.ros.org/t/ros2-logging-format/11549>

<a id="default-console-logging-output-stream"></a>

### Default Console Logging Output Stream

As of Foxy, all logging messages at all severity levels get logged to stderr by default.
This ensures that logging messages come out immediately, and brings the ROS 2 logging system into alignment with most other logging systems.
It is possible to change the stream to stdout at runtime via the RCUTILS\_LOGGING\_USE\_STDOUT environment variable, but all logging messages will still go to the same stream.
See <https://github.com/ros2/rcutils/pull/196> for more details.

<a id="launch-ros"></a>

### launch\_ros

<a id="node-name-and-namespace-parameters-changed"></a>

#### Node name and namespace parameters changed

The `Node` action parameters related to naming have been changed:

- `node_name` has been renamed to `name`
- `node_namespace` has been renamed to `namespace`
- `node_executable` has been renamed to `executable`
- `exec_name` has been added for naming the process associated with the node.
  Previously, users would have used the `name` keyword argument.

The old parameters have been deprecated.

These changes were made to make the launch frontend more idiomatic.
For example, instead of

```
<node pkg="demo_nodes_cpp" exec="talker" node-name="foo" />
```

we can now write

```
<node pkg="demo_nodes_cpp" exec="talker" name="foo" />
```

This change also applies to `ComposableNodeContainer`, `ComposableNode`, and `LifecycleNode`.
For examples, see the [relevant changes to the demos.](https://github.com/ros2/demos/pull/431)

[Related pull request in launch\_ros.](https://github.com/ros2/launch_ros/pull/122)

<a id="rclcpp"></a>

### rclcpp

<a id="change-in-advanced-subscription-callback-signature"></a>

#### Change in Advanced Subscription Callback Signature

With the pull request <https://github.com/ros2/rclcpp/pull/1047> the signature of callbacks which receive the message info with the message has changed.
Previously it used the `rmw` type `rmw_message_info_t`, but now uses the `rclcpp` type `rclcpp::MessageInfo`.
The required changes are straightforward, and can be seen demonstrated in these pull requests:

- <https://github.com/ros2/system_tests/pull/423/files>
- <https://github.com/ros2/rosbag2/pull/375/files>
- <https://github.com/ros2/ros1_bridge/pull/253/files>

<a id="change-in-serialized-message-callback-signature"></a>

#### Change in Serialized Message Callback Signature

The pull request [ros2/rclcpp#1081](https://github.com/ros2/rclcpp/pull/1081) introduces a new signature of the callbacks for retrieving ROS messages in serialized form.
The previously used C-Struct [rcl\_serialized\_message\_t](https://github.com/ros2/rmw/blob/foxy/rmw/include/rmw/serialized_message.h) is being superseded by a C++ data type [rclcpp::SerializedMessage](https://github.com/ros2/rclcpp/blob/foxy/rclcpp/include/rclcpp/serialized_message.hpp).

The example nodes in `demo_nodes_cpp`, namely `talker_serialized_message` as well as `listener_serialized_message` reflect these changes.

<a id="breaking-change-in-node-interface-getters-signature"></a>

#### Breaking change in Node Interface getters’ signature

With pull request [ros2/rclcpp#1069](https://github.com/ros2/rclcpp/pull/1069), the signature of node interface getters has been modified to return shared ownership of node interfaces (i.e. an `std::shared_ptr`) instead of a non-owning raw pointer.
Required changes in downstream packages that relied on the previous signature are simple and straightforward: use the `std::shared_ptr::get()` method.

<a id="deprecate-set-on-parameters-set-callback"></a>

#### Deprecate set\_on\_parameters\_set\_callback

Instead, use the `rclcpp::Node` methods `add_on_set_parameters_callback` and `remove_on_set_parameters_callback` for adding and removing functions that are called when parameters are set.

Related pull request: <https://github.com/ros2/rclcpp/pull/1123>

<a id="breaking-change-in-publisher-getter-signature"></a>

#### Breaking change in Publisher getter signature

With pull request [ros2/rclcpp#1119](https://github.com/ros2/rclcpp/pull/1119), the signature of publisher handle getter has been modified to return shared ownership of the underlying rcl structure (i.e. an `std::shared_ptr`) instead of a non-owning raw pointer.
This was necessary to fix a segfault in certain circumstances.
Required changes in downstream packages that relied on the previous signature are simple and straightforward: use the `std::shared_ptr::get()` method.

<a id="rclcpp-action"></a>

### rclcpp\_action

<a id="deprecate-clientgoalhandle-async-result"></a>

#### Deprecate ClientGoalHandle::async\_result()

Using this API, it is possible to run into a race condition causing an exception to be thrown.
Instead, prefer to use `Client::async_get_result()`, which is safer.

See [ros2/rclcpp#1120](https://github.com/ros2/rclcpp/pull/1120) and the connected issue for more info.

<a id="rclpy"></a>

### rclpy

<a id="support-for-multiple-on-parameter-set-callbacks"></a>

#### Support for multiple on parameter set callbacks

Use the `Node` methods `add_on_set_parameters_callback` and `remove_on_set_parameters_callback` for adding and removing functions that are called when parameters are set.

The method `set_parameters_callback` has been deprecated.

Related pull requests: <https://github.com/ros2/rclpy/pull/457>, <https://github.com/ros2/rclpy/pull/504>

<a id="rmw-connext-cpp"></a>

### rmw\_connext\_cpp

<a id="connext-5-1-locator-kinds-compatibility-mode"></a>

#### Connext 5.1 locator kinds compatibility mode

Up to and including `Eloquent`, `rmw_connext_cpp` was setting `dds.transport.use_510_compatible_locator_kinds` property to `true`.
This property is not being forced anymore, and shared transport communication between `Foxy` and previous releases will stop working.
Logs similar to:

```
PRESParticipant_checkTransportInfoMatching:Warning: discovered remote participant 'RTI Administration Console' using the 'shmem' transport with class ID 16777216.
This class ID does not match the class ID 2 of the same transport in the local participant 'talker'.
These two participants will not communicate over the 'shmem' transport.
Check the value of the property 'dds.transport.use_510_compatible_locator_kinds' in the local participant.
See https://community.rti.com/kb/what-causes-error-discovered-remote-participant for additional info.
```

will be observed when this incompatibility happens.

If compatibility is needed, it can be set up in an external QoS profiles files containing:

```
<participant_qos>
   <property>
      <value>
            <element>
               <name>
                  dds.transport.use_510_compatible_locator_kinds
               </name>
               <value>1</value>
            </element>
      </value>
   </property>
</participant_qos>
```

Remember to set the `NDDS_QOS_PROFILES` environment variable to the QoS profiles file path.
For more information, see `How to Change Transport Settings in 5.2.0 Applications for Compatibility with 5.1.0` section of [Transport\_Compatibility](https://community.rti.com/static/documentation/connext-dds/5.2.0/doc/manuals/connext_dds/html_files/RTI_ConnextDDS_CoreLibraries_ReleaseNotes/Content/ReleaseNotes/Transport_Compatibility.htm).

<a id="rviz"></a>

### rviz

<a id="tools-timestamp-messages-using-ros-time"></a>

#### Tools timestamp messages using ROS time

‘2D Pose Estimate’, ‘2D Nav Goal’, and ‘Publish Point’ tools now timestamp their messages using ROS time instead of system time, in order for the `use_sim_time` parameter to have an effect on them.

Related pull request: <https://github.com/ros2/rviz/pull/519>

<a id="std-msgs"></a>

### std\_msgs

<a id="deprecation-of-messages"></a>

#### Deprecation of messages

Although discouraged for a long time we have officially deprecated the following messages in `std_msgs`.
There are copies in [example\_interfaces](https://index.ros.org/p/example_interfaces)

- `std_msgs/msg/Bool`
- `std_msgs/msg/Byte`
- `std_msgs/msg/ByteMultiArray`
- `std_msgs/msg/Char`
- `std_msgs/msg/Float32`
- `std_msgs/msg/Float32MultiArray`
- `std_msgs/msg/Float64`
- `std_msgs/msg/Float64MultiArray`
- `std_msgs/msg/Int16`
- `std_msgs/msg/Int16MultiArray`
- `std_msgs/msg/Int32`
- `std_msgs/msg/Int32MultiArray`
- `std_msgs/msg/Int64`
- `std_msgs/msg/Int64MultiArray`
- `std_msgs/msg/Int8`
- `std_msgs/msg/Int8MultiArray`
- `std_msgs/msg/MultiArrayDimension`
- `std_msgs/msg/MultiArrayLayout`
- `std_msgs/msg/String`
- `std_msgs/msg/UInt16`
- `std_msgs/msg/UInt16MultiArray`
- `std_msgs/msg/UInt32`
- `std_msgs/msg/UInt32MultiArray`
- `std_msgs/msg/UInt64`
- `std_msgs/msg/UInt64MultiArray`
- `std_msgs/msg/UInt8`
- `std_msgs/msg/UInt8MultiArray`

<a id="security-features"></a>

### Security features

<a id="use-of-security-enclaves"></a>

#### Use of security enclaves

As of Foxy, domain participants are no longer mapped directly to ROS nodes.
As a result, ROS 2 security features (which are specific to domain participants) are also no longer mapped directly to ROS nodes.
Instead, Foxy introduces the concept of a security “enclave”, where an “enclave” is a process or group of processes that will share the same identity and access control rules.

This means that security artifacts are **not** retrieved based on the node name anymore but based on the Security enclave name.
A node enclave name can be set by using the ROS argument `--enclave`, e.g. `ros2 run demo_nodes_py talker --ros-args --enclave /my_enclave`

Related design document: <https://github.com/ros2/design/pull/274>

Note that permissions files are limited by the underlying transport packet size, so grouping many permissions under the same enclave will **not** work if the resulting permissions file exceed 64kB.
Related issue [[ros2/sros2#228]](https://github.com/ros2/sros2/issues/228)

<a id="renaming-of-the-environment-variables"></a>

#### Renaming of the environment variables

Environment variables renaming

| Name in Eloquent | Name in Foxy |
| --- | --- |
| ROS\_SECURITY\_ROOT\_DIRECTORY | ROS\_SECURITY\_KEYSTORE |
| ROS\_SECURITY\_NODE\_DIRECTORY | ROS\_SECURITY\_ENCLAVE\_OVERRIDE |

<a id="known-issues"></a>

## Known Issues

- [[ros2/ros2#922]](https://github.com/ros2/ros2/issues/922) Services’ performance is flaky for `rclcpp` nodes using eProsima Fast-RTPS or ADLINK CycloneDDS as RMW implementation.
  Specifically, service clients sometimes do not receive the response from servers.
- [[ros2/rclcpp#1212]](https://github.com/ros2/rclcpp/issues/1212) Ready reentrant Waitable objects can attempt to execute multiple times.

<a id="timeline-before-the-release"></a>

## Timeline before the release

A few milestones leading up to the release:

> > [!NOTE]
> >
> > The dates below reflect an extension by roughly two weeks due to the coronavirus pandemic.
>
> Wed. April 22nd, 2020
> :   API and feature freeze for `ros_core` [[1]](#id5) packages.
>     Note that this includes `rmw`, which is a recursive dependency of `ros_core`.
>     Only bug fix releases should be made after this point.
>     New packages can be released independently.
>
> Mon. April 29th, 2020 (beta)
> :   Updated releases of `desktop` [[2]](#id6) packages available.
>     Testing of the new features.
>
> Wed. May 27th, 2020 (release candidate)
> :   Updated releases of `desktop` [[2]](#id6) packages available.
>
> Wed. June 3rd, 2020
> :   Freeze rosdistro.
>     No PRs for Foxy on the rosdistro repo will be merged (reopens after the release announcement).

[[1](#id2)]

The `ros_core` variant described in the [variants](https://github.com/ros2/variants) repository.

[2]
([1](#id3),[2](#id4))

The `desktop` variant described in the [variants](https://github.com/ros2/variants) repository.
