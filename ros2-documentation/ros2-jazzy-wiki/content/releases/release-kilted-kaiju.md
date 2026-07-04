---
title: "Kilted Kaiju (codename ‘kilted’; May, 2025)"
docname: "Releases/Release-Kilted-Kaiju"
source: "Releases/Release-Kilted-Kaiju.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="kilted-kaiju-codename-kilted-may-2025"></a>
<a id="kilted-release"></a>

# Kilted Kaiju (codename ‘kilted’; May, 2025)

Table of Contents

- [Supported Platforms](#supported-platforms)
- [Installation](#installation)
- [Supported Gazebo Release](#supported-gazebo-release)
- [New features in this ROS 2 release](#new-features-in-this-ros-2-release)

  - [`ament_cmake_ros`](#ament-cmake-ros)
  - [`common_interfaces`](#common-interfaces)
  - [`ros2cli`](#ros2cli)
  - [`rclcpp`](#rclcpp)
  - [`rclpy`](#rclpy)
  - [`Rosbag2`](#rosbag2)
  - [`rosidl_rust`](#rosidl-rust)
  - [`ros2`](#ros2)
- [Changes since the Jazzy release](#changes-since-the-jazzy-release)

  - [`common_interfaces`](#id1)
  - [`rclcpp`](#id2)
  - [`rmw_connextdds_cpp`](#rmw-connextdds-cpp)
  - [`Connextmicro`](#connextmicro)
  - [`rosidl_dynamic_typesupport`](#rosidl-dynamic-typesupport)
  - [`rmw_fastrtps_cpp`](#rmw-fastrtps-cpp)
  - [ament\_target\_dependencies is deprecated](#ament-target-dependencies-is-deprecated)
  - [`launch`](#launch)
  - [`rmw_zenoh_cpp`](#rmw-zenoh-cpp)
- [Development progress](#development-progress)
- [Release Timeline](#release-timeline)

*Kilted Kaiju* is the eleventh release of ROS 2.
What follows is highlights of the important changes and features in Kilted Kaiju since the last release.
For a list of all of the changes since Jazzy, see the [long form changelog](kilted-kaiju-complete-changelog.md)

<a id="supported-platforms"></a>

## Supported Platforms

Kilted Kaiju supports the following platforms according to [the platform support tiers](../project/platform-support-tiers.md):

Tier 1 platforms:

- Ubuntu 24.04 (Noble): `amd64` and `arm64`
- Windows 10 (Visual Studio 2019): `amd64`

Tier 2 platforms:

- RHEL 9: `amd64`

Tier 3 platforms:

- macOS: `amd64`
- Debian Bookworm: `amd64`

Targeted platforms:

| Architecture | Ubuntu Noble (24.04) | Windows 10 (VS2019) | RHEL 9 | macOS | Debian Bookworm (12) | OpenEmbedded / Yocto Project |
| --- | --- | --- | --- | --- | --- | --- |
| amd64 | Tier 1 [d][a][s] | Tier 1 [a][s] | Tier 2 [d][a][s] | Tier 3 [s] | Tier 3 [s] | Tier 3 [s] |
| arm64 | Tier 1 [d][a][s] |  |  |  | Tier 3 [s] | Tier 3 [s] |
| arm32 | Tier 3 [s] |  |  |  | Tier 3 [s] | Tier 3 [s] |

The following indicators show what delivery mechanisms are available for
each platform.

" [d] " Distribution-specific (Debian, RPM, etc.) packages will be
provided for this platform for packages submitted to the rosdistro.

" [a] " Binary releases are provided as a single archive per
platform containing all packages in the Jazzy ROS 2 repos file[^14].

" [s] " Compilation from source.

Middleware Implementation Support:

| Middleware Library | Middleware Provider | Support Level | Platforms | Architectures |
| --- | --- | --- | --- | --- |
| rmw\_fastrtps\_cpp\* | eProsima Fast-DDS | Tier 1 | All Platforms | All Architectures |
| rmw\_connextdds | RTI Connext | Tier 1 | Ubuntu, Windows, and macOS | All Architectures except arm64 |
| rmw\_cyclonedds\_cpp | Eclipse Cyclone DDS | Tier 1 | All Platforms | All Architectures |
| rmw\_zenoh\_cpp | Eclipse Zenoh | Tier 1 | All Platforms | All Architectures |
| rmw\_fastrtps\_dynamic\_cpp | eProsima Fast-DDS | Tier 2 | All Platforms | All Architectures |
| rmw\_gurumdds\_cpp | GurumNetworks GurumDDS | Tier 3 | Ubuntu and Windows | All Architectures except arm32 |

" \* " means default RMW implementation.

Middleware implementation support is dependent upon the platform support
tier. For example a Tier 1 middleware implementation on a Tier 2
platform can only receive Tier 2 support.

Minimum language requirements:

- C++17
- Python 3.9

Dependency Requirements:

|  | Required Support | | Recommended Support | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Package | Ubuntu Noble | Windows 10\*\* | RHEL 9 | macOS\*\* | Debian Bookworm | OpenEmbedded\*\* |
| CMake | 3.28.3 | 3.28.3 | 3.26.5 | 3.31.1 | 3.25.1 | 3.22.3 |
| EmPY | 3.3.4 | 3.3.4 | 3.3.4a | 3.3.4 | | |
| Gazebo | Ionic\* | N/A | N/A | Ionic\* | Ionic\* | N/A |
| NumPy | 1.26.4 | 1.26.4 | 1.20.1 | 2.1.3 | 1.24.2 | N/A |
| Ogre | 1.12.10 | | | | | N/A |
| OpenCV | 4.6.0 | 4.9.0 | 4.6.0 | 4.10.0 | 4.6.0 | 4.1.0 / 3.2.0\*\*\* |
| OpenSSL | 3.0.13 | 3.3.2 | 3.2.2 | 1.1.1w | 3.0.15 | 1.1.1d / 1.1.1b\*\*\* |
| Python | 3.12.3 | 3.12.3 | 3.9.19 | 3.13.0 | 3.11.2 | 3.8.2 / 3.7.5\*\*\* |
| Qt | 5.15.13 | 5.15.8 | 5.15.9 | 5.15.16 | 5.15.8 | 5.14.1 / 5.12.5\*\*\* |
|  | | **Linux only** | | | | |
| PCL | 1.14.0 | N/A | 1.12.0 | 1.14.1 | 1.13.0 | 1.10.0 |
| **RMW Middleware** | | | | | | |
| Connext DDS | 7.3.0.0 | | | | | N/A | |
| Cyclone DDS | 0.10.5 | | | | | |
| Fast-DDS | 2.14.4 | | | | | |
| Gurum DDS | 4.2.0 | | N/A | | | |
| Zenoh | 1.0.4 | | | | | |

" \* " means that this is not the upstream version (available on the
official Operating System repositories) but a package distributed by
OSRF or the community (package built and distributed on custom
repositories).

" \*\* " means that the dependency may see multiple version changes,
because the dependency uses a package manager that continually updates
the dependency without a stable API.

" \*\*\* " webOS OSE provides this different version.

This document only captures the version at the first release of a ROS
distribution and will not be updated as the dependencies move forward.
These versions are thus a low watermark.

Package manager use for dependencies:

- Ubuntu, Debian: apt, pip
- Windows: pixi/conda, pip
- macOS: Homebrew, pip
- RHEL: dnf
- OpenEmbedded: opkg

Build System Support:

- ament\_cmake
- cargo
- cmake
- setuptools

<a id="installation"></a>

## Installation

[Install Kilted Kaiju](https://docs.ros.org/en/kilted/Installation.html)

<a id="supported-gazebo-release"></a>

## Supported Gazebo Release

For Kilted Kaiju, the recommended Gazebo release is [Ionic](https://gazebosim.org/docs/ionic/ros_installation).

<a id="new-features-in-this-ros-2-release"></a>

## New features in this ROS 2 release

<a id="ament-cmake-ros"></a>

### `ament_cmake_ros`

<a id="add-rmw-test-fixture-for-supporting-rmw-isolated-testing"></a>

#### Add rmw\_test\_fixture for supporting RMW-isolated testing

Included two new packages which provide an extensible mechanism for creating a test fixture for RMW-based communication isolation.
It is modeled closely after the rmw and rmw\_implementation API.

The `rmw_test_fixture` package currently provides only the API, which could be implemented by an RMW provider for configuring their RMW for a test to run.

The `rmw_test_fixture_implementation` package provides the entry point for discovering, loading, and invoking the appropriate extension.

See <https://github.com/ros2/ament_cmake_ros/pull/21> for more details.

<a id="common-interfaces"></a>

### `common_interfaces`

<a id="new-nav-msgs-goals-message"></a>

#### New nav\_msgs/Goals message

A new message type, [nav\_msgs/msg/Goals](https://docs.ros.org/en/jazzy/p/nav_msgs/msg/Goals.html), has been introduced to support an array of navigation goals within the nav\_msgs package.

See <https://github.com/ros2/common_interfaces/pull/269> for more details.

<a id="ros2cli"></a>

### `ros2cli`

<a id="action-introspection"></a>

#### Action introspection

This allows to instrospect an action with the command line.
Using `ros2cli` tools: `ros2 action echo <action name>`.

See <https://github.com/ros2/ros2cli/pull/978> for more information.

<a id="rclcpp"></a>

### `rclcpp`

<a id="action-generic-client"></a>

#### Action generic client

Support action generic client, this is used to support actions in rosbag2.

See <https://github.com/ros2/rclcpp/pull/2759> for more details.

<a id="rclpy"></a>

### `rclpy`

<a id="static-type-checking"></a>

#### Static Type Checking

Added static type hints to `ActionClient` and `ActionServer`.

See <https://github.com/ros2/rclpy/pull/1349> for more details.

Add support for [generics](https://typing.python.org/en/latest/reference/generics.html) in `pub/sub/client/server/actions`, `Future/Task`, and `Parameter`.

`Publisher`, `Subscription`, `Server`, `Task`, and `Parameter` should need no updates to add support for generics.

`Client` will need to be updated to resemble the following to get the improved type checking.

```
self._get_parameter_client: Client[GetParameters.Request,
                                   GetParameters.Response] = self.node.create_client(
                                    GetParameters, '/get_parameters',
                                    qos_profile=qos_profile, callback_group=callback_group)
```

`ActionClient` will need to be updated to resemble the following to get the improved type checking.

```
ac: ActionClient[Fibonacci.Goal,
                 Fibonacci.Result,
                 Fibonacci.Feedback] = ActionClient(self.node, Fibonacci, 'fibonacci')
```

`Future` will need to be updated to resemble the following to get the improved type checking.

```
log_msgs_future: Future[bool] = Future()
```

See <https://github.com/ros2/rclpy/pull/1239>, <https://github.com/ros2/rclpy/pull/1275>, <https://github.com/ros2/rclpy/pull/1246>, and <https://github.com/ros2/rclpy/pull/1254/files> for more details.

Various other small improvements and corrections have also been made throughout all of `rclpy`.

Python types can be statically checked using [ament\_mypy](https://github.com/ament/ament_lint/tree/kilted/ament_mypy) which wraps [mypy](https://www.mypy-lang.org/).

<a id="eventsexecutor"></a>

#### EventsExecutor

Support an experimental events executor for `rclpy`, which is a port of the original `rclcpp` events executor concept.

See <https://github.com/ros2/rclpy/pull/1391> for more details.

<a id="rosbag2"></a>

### `Rosbag2`

<a id="action-introspection-rosbag2-support"></a>

#### Action introspection Rosbag2 support

Allow to record and play actions from a rosbag.

See <https://github.com/ros2/rosbag2/pull/1955> for more information.
Design document <https://github.com/ros2/rosbag2/pull/1928>.

<a id="progress-bar-for-ros2-bag-play"></a>

#### Progress bar for `ros2 bag play`

Added a progress bar for `ros2 bag play` CLI, showing the bag time and duration, similar to
what is seen in ROS 1.

See <https://github.com/ros2/rosbag2/pull/1836> for more details.

<a id="added-support-for-replaying-multiple-bags-with-ros2-bag-play-cli"></a>

#### Added support for replaying multiple bags with `ros2 bag play` CLI

To replay multiple bags, use the new `-i, --input` CLI option:

```
$ ros2 bag play -i bag1 -i bag2 -i bag3 [storage_id]
```

See <https://github.com/ros2/rosbag2/pull/1848> for more information.

<a id="added-support-for-replaying-messages-chronologically-based-on-their-publication-timestamp"></a>

#### Added support for replaying messages chronologically based on their publication timestamp

This is exposed through `ros2 bag play` with a new `--message-order {received,sent}` option.
The default behavior is to play messages in the order they were received.

See <https://github.com/ros2/rosbag2/pull/1876> for more information.

<a id="make-snapshot-writing-into-a-new-file-each-time-it-is-triggered"></a>

#### Make snapshot writing into a new file each time it is triggered

See <https://github.com/ros2/rosbag2/pull/1842> for more details.

<a id="new-sort-cli-option-in-the-ros2-bag-info-command"></a>

#### New `--sort` CLI option in the `ros2 bag info` command

With new `--sort` CLI option user will be able to sort topics, services and actions by name, topic type or number of recorded messages.

See <https://github.com/ros2/rosbag2/pull/1804> for more details.

<a id="show-size-contribution-of-each-topic-with-ros2-bag-info"></a>

#### Show size contribution of each topic with `ros2 bag info`

With new `--size-contribution` option together with `ros2 bag info -v` user will be able to see the size contribution of each topic in the bag file.

See <https://github.com/ros2/rosbag2/pull/1726> for more information.

<a id="added-log-level-option-to-ros2-bag-play-and-ros2-bag-record-to-allow-printing-debug-messages"></a>

#### Added `--log-level` option to `ros2 bag play` and `ros2 bag record` to allow printing debug messages

See <https://github.com/ros2/rosbag2/pull/1625> for more details.

<a id="rosidl-rust"></a>

### `rosidl_rust`

<a id="added-rosidl-rust"></a>

#### Added `rosidl_rust`

A Rust idl generator was added to the list of default code generators.

See <https://github.com/ros2/ros2/pull/1674> for more details.

<a id="ros2"></a>

### `ros2`

<a id="switch-to-using-pixi-conda-for-windows"></a>

#### Switch to using Pixi/Conda for Windows

This allows to easily manage dependencies, and to update them in the future.
The installation process is significantly simplified.
Instead of dozens of steps to install dependencies, it is just a couple of commands.
It is much easier to update dependencies.
The dependencies are installed in individual workspaces, with no “global” installation.

See <https://github.com/ros2/ci/pull/802> and <https://github.com/ros2/ros2/pull/1642> for more details.
Visit [Windows source install instructions](../installation/alternatives/windows-development-setup.md) to install it on Windows.

<a id="support-topic-instances-in-dds-topics"></a>

#### Support topic instances in DDS topics

Topic instances are a way of multiplexing the transmission of updates of several objects of the same logical kind over the same resource, i.e. the topic.

See <https://github.com/ros2/ros2/issues/1538> for more information.
You can also check the documentation: <https://github.com/ros2/design/pull/340/files>.

<a id="changes-since-the-jazzy-release"></a>

## Changes since the Jazzy release

<a id="id1"></a>

### `common_interfaces`

<a id="added-nv12-to-pixel-formats"></a>

#### Added NV12 to pixel formats

Added NV12 to pixel formats, which is a common output format of hardware-accelerated decoders.

See <https://github.com/ros2/common_interfaces/pull/253> for more details.

<a id="id2"></a>

### `rclcpp`

<a id="consistent-behavior-for-subordinate-nodes"></a>

#### Consistent behavior for Subordinate nodes

Inconsistent behavior of subordinate nodes was fixed.
The subordinate node is a secondary node associated with a primary node, that shares the same underlying context and resources while maintaining a separate name and namespace.
The behavioral modification may affect existing applications relying on the previous implementation:

1. Generic clients created from a subordinate node now correctly respect the subordinate node’s sub-namespace
2. Parameters obtained using a subordinate node now correctly use the (parent) node’s `rclcpp::node_interfaces::NodeParametersInterface`

See <https://github.com/ros2/rclcpp/pull/2822> for more details.

<a id="rmw-connextdds-cpp"></a>

### `rmw_connextdds_cpp`

<a id="version-bumped-to-7-3"></a>

#### Version bumped to 7.3

The RTI Connext DDS version was bumped to 7.3.0.

See <https://github.com/ros2/ci/pull/811> for more details.

<a id="connextmicro"></a>

### `Connextmicro`

<a id="deprecated-connextmicro"></a>

#### deprecated Connextmicro

The RTI Connext Micro RMW package, `rmw_connextddsmicro`, is going to stop receiving updates in Kilted Kaiju, and be removed in a future ROS 2 release.

See <https://github.com/ros2/rmw_connextdds/pull/182> for more information.

<a id="rosidl-dynamic-typesupport"></a>

### `rosidl_dynamic_typesupport`

<a id="removing-support-for-float128"></a>

#### Removing support for float128

Removed support for float128 because there are inconsistencies in the definition.

See <https://github.com/ros2/rosidl_dynamic_typesupport/issues/11> for more details.

<a id="rmw-fastrtps-cpp"></a>

### `rmw_fastrtps_cpp`

<a id="renaming-package-from-fastrtps-to-fastdds"></a>

#### Renaming package from fastrtps to fastdds

`fastrtps` was renamed to `fastdds`.
The names of the rmw implementations stay the same.
XML Profile ENV strings will change.

See <https://github.com/ros2/ros2/pull/1641> for more details.

<a id="ament-target-dependencies-is-deprecated"></a>

### ament\_target\_dependencies is deprecated

The CMake macro `ament_target_dependencies()` has been deprecated in favor of `target_link_libraries()` with modern CMake targets.
The macro still works, but it emits a CMake deprecation warning at build time like this:

```
CMake Deprecation Warning at [...]/ament_cmake_target_dependencies/share/ament_cmake_target_dependencies/cmake/ament_target_dependencies.cmake:89 (message):
ament_target_dependencies() is deprecated.  Use target_link_libraries()
with modern CMake targets instead.  Try replacing this call with:

    target_link_libraries([...] PUBLIC
    [...]
    )
```

Try replacing the `ament_target_dependencies()` call with the `target_link_libraries()` call suggested by the warning.

For more information see [ament/ament\_cmake#572](https://github.com/ament/ament_cmake/pull/572) and [ament/ament\_cmake#292](https://github.com/ament/ament_cmake/issues/292).

<a id="launch"></a>

### `launch`

<a id="pathjoinsubstitution"></a>

#### `PathJoinSubstitution`

`PathJoinSubstitution` now supports concatenating strings or substitutions into a single path component.
For example:

```
PathJoinSubstitution(['robot_description', 'urdf', [LaunchConfiguration('model'), '.xacro']])
```

If the `model` launch configuration was set to `my_model`, this would result in a path equal to:

```
'robot_description/urdf/my_model.xacro'
```

For more information, see [ros2/launch#835](https://github.com/ros2/launch/issues/835) and [ros2/launch#838](https://github.com/ros2/launch/pull/838).

<a id="rmw-zenoh-cpp"></a>

### `rmw_zenoh_cpp`

<a id="tier-1"></a>

#### `Tier 1`

The `rmw_zenoh_cpp` is now considered Tier 1.
There are many PRs (summarized in [ros2/rmw\_zenoh#265](https://github.com/ros2/rmw_zenoh/issues/265)) in the ROS 2 core packages, such as:

> - Make the rmw pass all core tests.
> - Implement and document security
> - Make it work in the Tier 1 platforms.
> - Added Quality declarations
> - Added to REP 2005
> - A dedicated nightly CI job
> - Among others

For more information see <https://github.com/ros2/rmw_zenoh/issues/265>.

<a id="development-progress"></a>

## Development progress

For progress on the development of Kiltled Kaiju, see [this project board](https://github.com/orgs/ros2/projects/63).

For the broad process followed by Kilted Kaiju, see the [process description page](release-process.md).

<a id="release-timeline"></a>

## Release Timeline

> December, 2024 - Platform decisions
> :   REP 2000 is updated with the target platforms and major dependency versions.
>
> Mon. April 7, 2025 - Alpha + RMW freeze
> :   Preliminary testing and stabilization of ROS Base [[1]](#id8) packages, and API and feature freeze for RMW provider packages.
>
> Mon. April 14, 2025 - Freeze
> :   API and feature freeze for ROS Base [[1]](#id8) packages in Rolling Ridley.
>     Only bug fix releases should be made after this point.
>     New packages can be released independently.
>
> Mon. April 21, 2025 - Branch
> :   Branch from Rolling Ridley.
>     `rosdistro` is reopened for Rolling PRs for ROS Base [[1]](#id8) packages.
>     Kilted development shifts from `ros-rolling-*` packages to `ros-kilted-*` packages.
>
> Mon. April 28, 2025 - Beta
> :   Updated releases of ROS Desktop [[2]](#id9) packages available.
>     Call for general testing.
>
> Thu, May 1, 2025 - Kick off of Tutorial Party
> :   Tutorials hosted at <https://github.com/ros2/kilted_tutorial_party> are open for community testing.
>
> Mon. May 12, 2025 - Release Candidate
> :   Release Candidate packages are built.
>     Updated releases of ROS Desktop [[2]](#id9) packages available.
>
> Mon. May 19, 2025 - Distro Freeze
> :   Freeze all Kilted branches on all [ROS 2 desktop packages](https://reps.openrobotics.org/rep-2001/#kilted-kaiju-may-2025-november-2026) and `rosdistro`.
>     No pull requests for any `kilted` branch or targeting `kilted/distribution.yaml` in `rosdistro` repo will be merged.
>
> Fri. May 23, 2025 - General Availability
> :   Release announcement.
>     [ROS 2 desktop packages](https://reps.openrobotics.org/rep-2001/#kilted-kaiju-may-2025-november-2026) source freeze is lifted and `rosdistro` is reopened for Kilted pull requests.

[1]
([1](#id3),[2](#id4),[3](#id5))

The `ros_base` variant is described in [REP 2001 (ros-base)](https://reps.openrobotics.org/rep-2001/#ros-base).

[2]
([1](#id6),[2](#id7))

The `desktop` variant is described in [REP 2001 (desktop-variants)](https://reps.openrobotics.org/rep-2001/#desktop-variants).
