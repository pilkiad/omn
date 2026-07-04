---
title: "Iron Irwini Changelog"
docname: "Releases/Iron-Irwini-Complete-Changelog"
source: "Releases/Iron-Irwini-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="iron-irwini-changelog"></a>

# Iron Irwini Changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

Table of Contents

- [action\_msgs](#action-msgs)
- [action\_tutorials\_cpp](#action-tutorials-cpp)
- [action\_tutorials\_interfaces](#action-tutorials-interfaces)
- [action\_tutorials\_py](#action-tutorials-py)
- [actionlib\_msgs](#actionlib-msgs)
- [ament\_clang\_format](#ament-clang-format)
- [ament\_clang\_tidy](#ament-clang-tidy)
- [ament\_cmake](#ament-cmake)
- [ament\_cmake\_auto](#ament-cmake-auto)
- [ament\_cmake\_clang\_format](#ament-cmake-clang-format)
- [ament\_cmake\_clang\_tidy](#ament-cmake-clang-tidy)
- [ament\_cmake\_copyright](#ament-cmake-copyright)
- [ament\_cmake\_core](#ament-cmake-core)
- [ament\_cmake\_cppcheck](#ament-cmake-cppcheck)
- [ament\_cmake\_cpplint](#ament-cmake-cpplint)
- [ament\_cmake\_export\_definitions](#ament-cmake-export-definitions)
- [ament\_cmake\_export\_dependencies](#ament-cmake-export-dependencies)
- [ament\_cmake\_export\_include\_directories](#ament-cmake-export-include-directories)
- [ament\_cmake\_export\_interfaces](#ament-cmake-export-interfaces)
- [ament\_cmake\_export\_libraries](#ament-cmake-export-libraries)
- [ament\_cmake\_export\_link\_flags](#ament-cmake-export-link-flags)
- [ament\_cmake\_export\_targets](#ament-cmake-export-targets)
- [ament\_cmake\_flake8](#ament-cmake-flake8)
- [ament\_cmake\_gen\_version\_h](#ament-cmake-gen-version-h)
- [ament\_cmake\_gmock](#ament-cmake-gmock)
- [ament\_cmake\_google\_benchmark](#ament-cmake-google-benchmark)
- [ament\_cmake\_gtest](#ament-cmake-gtest)
- [ament\_cmake\_include\_directories](#ament-cmake-include-directories)
- [ament\_cmake\_libraries](#ament-cmake-libraries)
- [ament\_cmake\_lint\_cmake](#ament-cmake-lint-cmake)
- [ament\_cmake\_mypy](#ament-cmake-mypy)
- [ament\_cmake\_pclint](#ament-cmake-pclint)
- [ament\_cmake\_pep257](#ament-cmake-pep257)
- [ament\_cmake\_pycodestyle](#ament-cmake-pycodestyle)
- [ament\_cmake\_pyflakes](#ament-cmake-pyflakes)
- [ament\_cmake\_pytest](#ament-cmake-pytest)
- [ament\_cmake\_python](#ament-cmake-python)
- [ament\_cmake\_ros](#ament-cmake-ros)
- [ament\_cmake\_target\_dependencies](#ament-cmake-target-dependencies)
- [ament\_cmake\_test](#ament-cmake-test)
- [ament\_cmake\_uncrustify](#ament-cmake-uncrustify)
- [ament\_cmake\_vendor\_package](#ament-cmake-vendor-package)
- [ament\_cmake\_version](#ament-cmake-version)
- [ament\_cmake\_xmllint](#ament-cmake-xmllint)
- [ament\_copyright](#ament-copyright)
- [ament\_cppcheck](#ament-cppcheck)
- [ament\_cpplint](#ament-cpplint)
- [ament\_flake8](#ament-flake8)
- [ament\_index\_cpp](#ament-index-cpp)
- [ament\_index\_python](#ament-index-python)
- [ament\_lint](#ament-lint)
- [ament\_lint\_auto](#ament-lint-auto)
- [ament\_lint\_cmake](#ament-lint-cmake)
- [ament\_lint\_common](#ament-lint-common)
- [ament\_mypy](#ament-mypy)
- [ament\_package](#ament-package)
- [ament\_pclint](#ament-pclint)
- [ament\_pep257](#ament-pep257)
- [ament\_pycodestyle](#ament-pycodestyle)
- [ament\_pyflakes](#ament-pyflakes)
- [ament\_uncrustify](#ament-uncrustify)
- [ament\_xmllint](#ament-xmllint)
- [builtin\_interfaces](#builtin-interfaces)
- [camera\_calibration\_parsers](#camera-calibration-parsers)
- [camera\_info\_manager](#camera-info-manager)
- [class\_loader](#class-loader)
- [common\_interfaces](#common-interfaces)
- [composition](#composition)
- [composition\_interfaces](#composition-interfaces)
- [demo\_nodes\_cpp](#demo-nodes-cpp)
- [demo\_nodes\_cpp\_native](#demo-nodes-cpp-native)
- [demo\_nodes\_py](#demo-nodes-py)
- [diagnostic\_msgs](#diagnostic-msgs)
- [domain\_coordinator](#domain-coordinator)
- [dummy\_map\_server](#dummy-map-server)
- [dummy\_robot\_bringup](#dummy-robot-bringup)
- [dummy\_sensors](#dummy-sensors)
- [eigen3\_cmake\_module](#eigen3-cmake-module)
- [example\_interfaces](#example-interfaces)
- [examples\_rclcpp\_async\_client](#examples-rclcpp-async-client)
- [examples\_rclcpp\_cbg\_executor](#examples-rclcpp-cbg-executor)
- [examples\_rclcpp\_minimal\_action\_client](#examples-rclcpp-minimal-action-client)
- [examples\_rclcpp\_minimal\_action\_server](#examples-rclcpp-minimal-action-server)
- [examples\_rclcpp\_minimal\_client](#examples-rclcpp-minimal-client)
- [examples\_rclcpp\_minimal\_composition](#examples-rclcpp-minimal-composition)
- [examples\_rclcpp\_minimal\_publisher](#examples-rclcpp-minimal-publisher)
- [examples\_rclcpp\_minimal\_service](#examples-rclcpp-minimal-service)
- [examples\_rclcpp\_minimal\_subscriber](#examples-rclcpp-minimal-subscriber)
- [examples\_rclcpp\_minimal\_timer](#examples-rclcpp-minimal-timer)
- [examples\_rclcpp\_multithreaded\_executor](#examples-rclcpp-multithreaded-executor)
- [examples\_rclcpp\_wait\_set](#examples-rclcpp-wait-set)
- [examples\_rclpy\_executors](#examples-rclpy-executors)
- [examples\_rclpy\_guard\_conditions](#examples-rclpy-guard-conditions)
- [examples\_rclpy\_minimal\_action\_client](#examples-rclpy-minimal-action-client)
- [examples\_rclpy\_minimal\_action\_server](#examples-rclpy-minimal-action-server)
- [examples\_rclpy\_minimal\_client](#examples-rclpy-minimal-client)
- [examples\_rclpy\_minimal\_publisher](#examples-rclpy-minimal-publisher)
- [examples\_rclpy\_minimal\_service](#examples-rclpy-minimal-service)
- [examples\_rclpy\_minimal\_subscriber](#examples-rclpy-minimal-subscriber)
- [examples\_rclpy\_pointcloud\_publisher](#examples-rclpy-pointcloud-publisher)
- [examples\_tf2\_py](#examples-tf2-py)
- [fastrtps\_cmake\_module](#fastrtps-cmake-module)
- [foonathan\_memory\_vendor](#foonathan-memory-vendor)
- [geometry2](#geometry2)
- [geometry\_msgs](#geometry-msgs)
- [google\_benchmark\_vendor](#google-benchmark-vendor)
- [ignition\_cmake2\_vendor](#ignition-cmake2-vendor)
- [ignition\_math6\_vendor](#ignition-math6-vendor)
- [image\_tools](#image-tools)
- [image\_transport](#image-transport)
- [interactive\_markers](#interactive-markers)
- [intra\_process\_demo](#intra-process-demo)
- [kdl\_parser](#kdl-parser)
- [keyboard\_handler](#keyboard-handler)
- [laser\_geometry](#laser-geometry)
- [launch](#launch)
- [launch\_pytest](#launch-pytest)
- [launch\_ros](#launch-ros)
- [launch\_testing](#launch-testing)
- [launch\_testing\_ament\_cmake](#launch-testing-ament-cmake)
- [launch\_testing\_examples](#launch-testing-examples)
- [launch\_testing\_ros](#launch-testing-ros)
- [launch\_xml](#launch-xml)
- [launch\_yaml](#launch-yaml)
- [libcurl\_vendor](#libcurl-vendor)
- [libstatistics\_collector](#libstatistics-collector)
- [libyaml\_vendor](#libyaml-vendor)
- [lifecycle](#lifecycle)
- [lifecycle\_msgs](#lifecycle-msgs)
- [lifecycle\_py](#lifecycle-py)
- [logging\_demo](#logging-demo)
- [map\_msgs](#map-msgs)
- [mcap\_vendor](#mcap-vendor)
- [message\_filters](#message-filters)
- [mimick\_vendor](#mimick-vendor)
- [nav\_msgs](#nav-msgs)
- [orocos\_kdl\_vendor](#orocos-kdl-vendor)
- [osrf\_pycommon](#osrf-pycommon)
- [osrf\_testing\_tools\_cpp](#osrf-testing-tools-cpp)
- [pendulum\_control](#pendulum-control)
- [pendulum\_msgs](#pendulum-msgs)
- [performance\_test\_fixture](#performance-test-fixture)
- [pluginlib](#pluginlib)
- [pybind11\_vendor](#pybind11-vendor)
- [python\_cmake\_module](#python-cmake-module)
- [python\_orocos\_kdl\_vendor](#python-orocos-kdl-vendor)
- [python\_qt\_binding](#python-qt-binding)
- [qt\_dotgraph](#qt-dotgraph)
- [qt\_gui](#qt-gui)
- [qt\_gui\_app](#qt-gui-app)
- [qt\_gui\_core](#qt-gui-core)
- [qt\_gui\_cpp](#qt-gui-cpp)
- [qt\_gui\_py\_common](#qt-gui-py-common)
- [quality\_of\_service\_demo\_cpp](#quality-of-service-demo-cpp)
- [quality\_of\_service\_demo\_py](#quality-of-service-demo-py)
- [rcl](#rcl)
- [rcl\_action](#rcl-action)
- [rcl\_interfaces](#rcl-interfaces)
- [rcl\_lifecycle](#rcl-lifecycle)
- [rcl\_logging\_interface](#rcl-logging-interface)
- [rcl\_logging\_noop](#rcl-logging-noop)
- [rcl\_logging\_spdlog](#rcl-logging-spdlog)
- [rcl\_yaml\_param\_parser](#rcl-yaml-param-parser)
- [rclcpp](#rclcpp)
- [rclcpp\_action](#rclcpp-action)
- [rclcpp\_components](#rclcpp-components)
- [rclcpp\_lifecycle](#rclcpp-lifecycle)
- [rclpy](#rclpy)
- [rcpputils](#rcpputils)
- [rcutils](#rcutils)
- [rmw](#rmw)
- [rmw\_connextdds](#rmw-connextdds)
- [rmw\_connextdds\_common](#rmw-connextdds-common)
- [rmw\_connextddsmicro](#rmw-connextddsmicro)
- [rmw\_cyclonedds\_cpp](#rmw-cyclonedds-cpp)
- [rmw\_dds\_common](#rmw-dds-common)
- [rmw\_fastrtps\_cpp](#rmw-fastrtps-cpp)
- [rmw\_fastrtps\_dynamic\_cpp](#rmw-fastrtps-dynamic-cpp)
- [rmw\_fastrtps\_shared\_cpp](#rmw-fastrtps-shared-cpp)
- [rmw\_implementation](#rmw-implementation)
- [rmw\_implementation\_cmake](#rmw-implementation-cmake)
- [robot\_state\_publisher](#robot-state-publisher)
- [ros2action](#ros2action)
- [ros2bag](#ros2bag)
- [ros2cli](#ros2cli)
- [ros2cli\_common\_extensions](#ros2cli-common-extensions)
- [ros2cli\_test\_interfaces](#ros2cli-test-interfaces)
- [ros2component](#ros2component)
- [ros2doctor](#ros2doctor)
- [ros2interface](#ros2interface)
- [ros2launch](#ros2launch)
- [ros2lifecycle](#ros2lifecycle)
- [ros2lifecycle\_test\_fixtures](#ros2lifecycle-test-fixtures)
- [ros2multicast](#ros2multicast)
- [ros2node](#ros2node)
- [ros2param](#ros2param)
- [ros2pkg](#ros2pkg)
- [ros2run](#ros2run)
- [ros2service](#ros2service)
- [ros2test](#ros2test)
- [ros2topic](#ros2topic)
- [ros2trace](#ros2trace)
- [ros\_testing](#ros-testing)
- [rosbag2](#rosbag2)
- [rosbag2\_compression](#rosbag2-compression)
- [rosbag2\_compression\_zstd](#rosbag2-compression-zstd)
- [rosbag2\_cpp](#rosbag2-cpp)
- [rosbag2\_examples\_cpp](#rosbag2-examples-cpp)
- [rosbag2\_examples\_py](#rosbag2-examples-py)
- [rosbag2\_interfaces](#rosbag2-interfaces)
- [rosbag2\_performance\_benchmarking](#rosbag2-performance-benchmarking)
- [rosbag2\_performance\_benchmarking\_msgs](#rosbag2-performance-benchmarking-msgs)
- [rosbag2\_py](#rosbag2-py)
- [rosbag2\_storage](#rosbag2-storage)
- [rosbag2\_storage\_default\_plugins](#rosbag2-storage-default-plugins)
- [rosbag2\_storage\_mcap](#rosbag2-storage-mcap)
- [rosbag2\_storage\_sqlite3](#rosbag2-storage-sqlite3)
- [rosbag2\_test\_common](#rosbag2-test-common)
- [rosbag2\_test\_msgdefs](#rosbag2-test-msgdefs)
- [rosbag2\_tests](#rosbag2-tests)
- [rosbag2\_transport](#rosbag2-transport)
- [rosgraph\_msgs](#rosgraph-msgs)
- [rosidl\_adapter](#rosidl-adapter)
- [rosidl\_cli](#rosidl-cli)
- [rosidl\_cmake](#rosidl-cmake)
- [rosidl\_core\_generators](#rosidl-core-generators)
- [rosidl\_core\_runtime](#rosidl-core-runtime)
- [rosidl\_default\_generators](#rosidl-default-generators)
- [rosidl\_default\_runtime](#rosidl-default-runtime)
- [rosidl\_dynamic\_typesupport](#rosidl-dynamic-typesupport)
- [rosidl\_dynamic\_typesupport\_fastrtps](#rosidl-dynamic-typesupport-fastrtps)
- [rosidl\_generator\_c](#rosidl-generator-c)
- [rosidl\_generator\_cpp](#rosidl-generator-cpp)
- [rosidl\_generator\_dds\_idl](#rosidl-generator-dds-idl)
- [rosidl\_generator\_py](#rosidl-generator-py)
- [rosidl\_generator\_tests](#rosidl-generator-tests)
- [rosidl\_generator\_type\_description](#rosidl-generator-type-description)
- [rosidl\_parser](#rosidl-parser)
- [rosidl\_pycommon](#rosidl-pycommon)
- [rosidl\_runtime\_c](#rosidl-runtime-c)
- [rosidl\_runtime\_cpp](#rosidl-runtime-cpp)
- [rosidl\_runtime\_py](#rosidl-runtime-py)
- [rosidl\_typesupport\_c](#rosidl-typesupport-c)
- [rosidl\_typesupport\_cpp](#rosidl-typesupport-cpp)
- [rosidl\_typesupport\_fastrtps\_c](#rosidl-typesupport-fastrtps-c)
- [rosidl\_typesupport\_fastrtps\_cpp](#rosidl-typesupport-fastrtps-cpp)
- [rosidl\_typesupport\_interface](#rosidl-typesupport-interface)
- [rosidl\_typesupport\_introspection\_c](#rosidl-typesupport-introspection-c)
- [rosidl\_typesupport\_introspection\_cpp](#rosidl-typesupport-introspection-cpp)
- [rosidl\_typesupport\_introspection\_tests](#rosidl-typesupport-introspection-tests)
- [rosidl\_typesupport\_tests](#rosidl-typesupport-tests)
- [rpyutils](#rpyutils)
- [rqt](#rqt)
- [rqt\_action](#rqt-action)
- [rqt\_bag](#rqt-bag)
- [rqt\_bag\_plugins](#rqt-bag-plugins)
- [rqt\_console](#rqt-console)
- [rqt\_graph](#rqt-graph)
- [rqt\_gui](#rqt-gui)
- [rqt\_gui\_cpp](#rqt-gui-cpp)
- [rqt\_gui\_py](#rqt-gui-py)
- [rqt\_msg](#rqt-msg)
- [rqt\_plot](#rqt-plot)
- [rqt\_publisher](#rqt-publisher)
- [rqt\_py\_common](#rqt-py-common)
- [rqt\_py\_console](#rqt-py-console)
- [rqt\_reconfigure](#rqt-reconfigure)
- [rqt\_service\_caller](#rqt-service-caller)
- [rqt\_shell](#rqt-shell)
- [rqt\_srv](#rqt-srv)
- [rqt\_topic](#rqt-topic)
- [rti\_connext\_dds\_cmake\_module](#rti-connext-dds-cmake-module)
- [rttest](#rttest)
- [rviz2](#rviz2)
- [rviz\_assimp\_vendor](#rviz-assimp-vendor)
- [rviz\_common](#rviz-common)
- [rviz\_default\_plugins](#rviz-default-plugins)
- [rviz\_ogre\_vendor](#rviz-ogre-vendor)
- [rviz\_rendering](#rviz-rendering)
- [rviz\_rendering\_tests](#rviz-rendering-tests)
- [rviz\_visual\_testing\_framework](#rviz-visual-testing-framework)
- [sensor\_msgs](#sensor-msgs)
- [sensor\_msgs\_py](#sensor-msgs-py)
- [service\_msgs](#service-msgs)
- [shape\_msgs](#shape-msgs)
- [shared\_queues\_vendor](#shared-queues-vendor)
- [spdlog\_vendor](#spdlog-vendor)
- [sqlite3\_vendor](#sqlite3-vendor)
- [sros2](#sros2)
- [statistics\_msgs](#statistics-msgs)
- [std\_msgs](#std-msgs)
- [std\_srvs](#std-srvs)
- [stereo\_msgs](#stereo-msgs)
- [tango\_icons\_vendor](#tango-icons-vendor)
- [test\_cli](#test-cli)
- [test\_cli\_remapping](#test-cli-remapping)
- [test\_communication](#test-communication)
- [test\_interface\_files](#test-interface-files)
- [test\_launch\_ros](#test-launch-ros)
- [test\_launch\_testing](#test-launch-testing)
- [test\_msgs](#test-msgs)
- [test\_osrf\_testing\_tools\_cpp](#test-osrf-testing-tools-cpp)
- [test\_quality\_of\_service](#test-quality-of-service)
- [test\_rclcpp](#test-rclcpp)
- [test\_rmw\_implementation](#test-rmw-implementation)
- [test\_ros2trace](#test-ros2trace)
- [test\_security](#test-security)
- [test\_tf2](#test-tf2)
- [test\_tracetools](#test-tracetools)
- [test\_tracetools\_launch](#test-tracetools-launch)
- [tf2](#tf2)
- [tf2\_bullet](#tf2-bullet)
- [tf2\_eigen](#tf2-eigen)
- [tf2\_eigen\_kdl](#tf2-eigen-kdl)
- [tf2\_geometry\_msgs](#tf2-geometry-msgs)
- [tf2\_kdl](#tf2-kdl)
- [tf2\_msgs](#tf2-msgs)
- [tf2\_py](#tf2-py)
- [tf2\_ros](#tf2-ros)
- [tf2\_ros\_py](#tf2-ros-py)
- [tf2\_sensor\_msgs](#tf2-sensor-msgs)
- [tf2\_tools](#tf2-tools)
- [tlsf](#tlsf)
- [tlsf\_cpp](#tlsf-cpp)
- [topic\_monitor](#topic-monitor)
- [topic\_statistics\_demo](#topic-statistics-demo)
- [tracetools](#tracetools)
- [tracetools\_launch](#tracetools-launch)
- [tracetools\_trace](#tracetools-trace)
- [trajectory\_msgs](#trajectory-msgs)
- [turtlesim](#turtlesim)
- [type\_description\_interfaces](#type-description-interfaces)
- [unique\_identifier\_msgs](#unique-identifier-msgs)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [visualization\_msgs](#visualization-msgs)
- [yaml\_cpp\_vendor](#yaml-cpp-vendor)
- [zstd\_vendor](#zstd-vendor)

<a id="action-msgs"></a>

## [action\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/action_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- Add service\_msgs package ([#143](https://github.com/ros2/rcl_interfaces/issues/143))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Depend on rosidl\_core\_generators for packages required by actions ([#144](https://github.com/ros2/rcl_interfaces/issues/144))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Jacob Perron

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/iron/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- Add README’s for action\_tutorials. ([#576](https://github.com/ros2/demos/issues/576))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Fix two small bugs in the fibonacci C++ tutorial. ([#564](https://github.com/ros2/demos/issues/564))
- Contributors: Audrow Nash, Chris Lalancette, kagibson

<a id="action-tutorials-interfaces"></a>

## [action\_tutorials\_interfaces](https://github.com/ros2/demos/tree/iron/action_tutorials/action_tutorials_interfaces/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- A couple more upgrades to C++17. ([#609](https://github.com/ros2/demos/issues/609))
- Add README’s for action\_tutorials. ([#576](https://github.com/ros2/demos/issues/576))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Remove action\_msgs dependency ([#580](https://github.com/ros2/demos/issues/580))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, kagibson

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/iron/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- Add README’s for action\_tutorials. ([#576](https://github.com/ros2/demos/issues/576))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, kagibson

<a id="actionlib-msgs"></a>

## [actionlib\_msgs](https://github.com/ros2/common_interfaces/tree/iron/actionlib_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/iron/ament_clang_format/CHANGELOG.rst)

- ament\_clang\_format: use open braces for enum definitions ([#426](https://github.com/ament/ament_lint/issues/426))
- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, james-rms, methylDragon

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/iron/ament_clang_tidy/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- recommend use of –mixin compile-commands ([#371](https://github.com/ament/ament_lint/issues/371))
- Improve message and avoid missing new lines between reports from files ([#373](https://github.com/ament/ament_lint/issues/373))
- Contributors: Audrow Nash, William Woodall, methylDragon

<a id="ament-cmake"></a>

## [ament\_cmake](https://github.com/ament/ament_cmake/tree/iron/ament_cmake/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_auto/CHANGELOG.rst)

- Support INTERFACE on ament\_auto\_add\_library ([#420](https://github.com/ament/ament_cmake/issues/420))
- Fix ament\_auto\_add\_gtest’s parameter passing ([#421](https://github.com/ament/ament_cmake/issues/421))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411))
- Rolling: ament\_cmake\_auto should include dependencies as SYSTEM ([#385](https://github.com/ament/ament_cmake/issues/385))
- Contributors: Audrow Nash, Christopher Wecht, Joshua Whitley, Rin Iwai

<a id="ament-cmake-clang-format"></a>

## [ament\_cmake\_clang\_format](https://github.com/ament/ament_lint/tree/iron/ament_cmake_clang_format/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-clang-tidy"></a>

## [ament\_cmake\_clang\_tidy](https://github.com/ament/ament_lint/tree/iron/ament_cmake_clang_tidy/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-copyright"></a>

## [ament\_cmake\_copyright](https://github.com/ament/ament_lint/tree/iron/ament_cmake_copyright/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_lint\_auto] General file exclusion with AMENT\_LINT\_AUTO\_FILE\_EXCLUDE ([#386](https://github.com/ament/ament_lint/issues/386))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, methylDragon

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_core/CHANGELOG.rst)

- ament\_cmake\_uninstall\_target: Correct location of install\_manifest.txt ([#432](https://github.com/ament/ament_cmake/issues/432))
- Use file(GENERATE OUTPUT) to create dsv files ([#416](https://github.com/ament/ament_cmake/issues/416)) Using file(WRITE) and file(APPEND) causes the modification stamp of the file to be changed each time CMake configures, resluting in an ‘Installing’ message rather than an ‘Up-to-date’ message even though the file content is identical. Using file(GENERATE OUTPUT) updates the timestamp of the file only if the content changes.
- Warn when trying to symlink install an INTERFACE\_LIBRARY ([#417](https://github.com/ament/ament_cmake/issues/417))
- Workaround to exclude Clion’s cmake folders from colcon test ([#410](https://github.com/ament/ament_cmake/issues/410)) - Add AMENT\_IGNORE to CMAKE\_BINARY\_DIR to avoid picking up cmake specific folders created by CLion in `colcon build` and `colcon test` commands
- if (NOT ${UNDEFINED\_VAR}) gets evaluated to false, so change to if (NOT UNDEFINED\_VAR) so it evaluates to true. ([#407](https://github.com/ament/ament_cmake/issues/407))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Implement ament\_add\_default\_options ([#390](https://github.com/ament/ament_cmake/issues/390))
- Contributors: Audrow Nash, Kenji Brameld, Michael Orlov, Scott K Logan, Shane Loretz, Silvio Traversaro, methylDragon

<a id="ament-cmake-cppcheck"></a>

## [ament\_cmake\_cppcheck](https://github.com/ament/ament_lint/tree/iron/ament_cmake_cppcheck/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_lint\_auto] General file exclusion with AMENT\_LINT\_AUTO\_FILE\_EXCLUDE ([#386](https://github.com/ament/ament_lint/issues/386))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, methylDragon

<a id="ament-cmake-cpplint"></a>

## [ament\_cmake\_cpplint](https://github.com/ament/ament_lint/tree/iron/ament_cmake_cpplint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_lint\_auto] General file exclusion with AMENT\_LINT\_AUTO\_FILE\_EXCLUDE ([#386](https://github.com/ament/ament_lint/issues/386))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, methylDragon

<a id="ament-cmake-export-definitions"></a>

## [ament\_cmake\_export\_definitions](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_definitions/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-dependencies"></a>

## [ament\_cmake\_export\_dependencies](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_dependencies/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-include-directories"></a>

## [ament\_cmake\_export\_include\_directories](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_include_directories/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-interfaces"></a>

## [ament\_cmake\_export\_interfaces](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_interfaces/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-libraries"></a>

## [ament\_cmake\_export\_libraries](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_libraries/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-link-flags"></a>

## [ament\_cmake\_export\_link\_flags](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_link_flags/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-export-targets"></a>

## [ament\_cmake\_export\_targets](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_export_targets/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Support new target export template introduced with CMake 3.24 ([#395](https://github.com/ament/ament_cmake/issues/395))
- Fix the order in which Export.cmake files are included ([#256](https://github.com/ament/ament_cmake/issues/256))
- Contributors: Audrow Nash, Timo Röhling

<a id="ament-cmake-flake8"></a>

## [ament\_cmake\_flake8](https://github.com/ament/ament_lint/tree/iron/ament_cmake_flake8/CHANGELOG.rst)

- Add flake8 linter ignore support ([#424](https://github.com/ament/ament_lint/issues/424))
- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, RFRIEDM-Trimble, methylDragon

<a id="ament-cmake-gen-version-h"></a>

## [ament\_cmake\_gen\_version\_h](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_gen_version_h/CHANGELOG.rst)

- Changed version gte macro to make it MSVC compatible. Fix [#433](https://github.com/ament/ament_cmake/issues/433) ([#434](https://github.com/ament/ament_cmake/issues/434))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash, iquarobotics

<a id="ament-cmake-gmock"></a>

## [ament\_cmake\_gmock](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_gmock/CHANGELOG.rst)

- Fix compiler warnings related to gtest/gmock ([#408](https://github.com/ament/ament_cmake/issues/408)) \* Suppress compiler warnings when building gmock definition of implicit copy constructor … is deprecated because it has a user-declared copy assignment operator [-Wdeprecated-copy] \* Declare gtest/gmock include dirs as SYSTEM PRIVATE for test targets
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash, Robert Haschke

<a id="ament-cmake-google-benchmark"></a>

## [ament\_cmake\_google\_benchmark](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_google_benchmark/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_gtest/CHANGELOG.rst)

- Fix compiler warnings related to gtest/gmock ([#408](https://github.com/ament/ament_cmake/issues/408)) \* Suppress compiler warnings when building gmock definition of implicit copy constructor … is deprecated because it has a user-declared copy assignment operator [-Wdeprecated-copy] \* Declare gtest/gmock include dirs as SYSTEM PRIVATE for test targets
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash, Robert Haschke

<a id="ament-cmake-include-directories"></a>

## [ament\_cmake\_include\_directories](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_include_directories/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-libraries"></a>

## [ament\_cmake\_libraries](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_libraries/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-lint-cmake"></a>

## [ament\_cmake\_lint\_cmake](https://github.com/ament/ament_lint/tree/iron/ament_cmake_lint_cmake/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-mypy"></a>

## [ament\_cmake\_mypy](https://github.com/ament/ament_lint/tree/iron/ament_cmake_mypy/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-pclint"></a>

## [ament\_cmake\_pclint](https://github.com/ament/ament_lint/tree/iron/ament_cmake_pclint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-pep257"></a>

## [ament\_cmake\_pep257](https://github.com/ament/ament_lint/tree/iron/ament_cmake_pep257/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-pycodestyle"></a>

## [ament\_cmake\_pycodestyle](https://github.com/ament/ament_lint/tree/iron/ament_cmake_pycodestyle/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-pyflakes"></a>

## [ament\_cmake\_pyflakes](https://github.com/ament/ament_lint/tree/iron/ament_cmake_pyflakes/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-pytest"></a>

## [ament\_cmake\_pytest](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_pytest/CHANGELOG.rst)

- Fix test skipping logic for missing pytest module ([#441](https://github.com/ament/ament_cmake/issues/441))
- Add missing buildtool\_depend on python3-pytest ([#440](https://github.com/ament/ament_cmake/issues/440))
- ament\_cmake\_pytest needs a buildtool\_depend on ament\_cmake\_test. ([#439](https://github.com/ament/ament_cmake/issues/439))
- Fix pytest-cov version detection with pytest >=7.0.0 ([#436](https://github.com/ament/ament_cmake/issues/436))
- use the error handler replace to allow non-utf8 to be decoded ([#381](https://github.com/ament/ament_cmake/issues/381))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Add NOCAPTURE option to ament\_add\_pytest\_test ([#393](https://github.com/ament/ament_cmake/issues/393))
- Contributors: Audrow Nash, Chris Lalancette, Christophe Bedard, El Jawad Alaa, Jacob Perron, Scott K Logan

<a id="ament-cmake-python"></a>

## [ament\_cmake\_python](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_python/CHANGELOG.rst)

- Support Debian-specific install dir for ament\_cmake\_python ([#431](https://github.com/ament/ament_cmake/issues/431))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Document ament\_cmake\_python ([#387](https://github.com/ament/ament_cmake/issues/387))
- Contributors: Audrow Nash, Shane Loretz, Timo Röhling

<a id="ament-cmake-ros"></a>

## [ament\_cmake\_ros](https://github.com/ros2/ament_cmake_ros/tree/iron/ament_cmake_ros/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#16](https://github.com/ros2/ament_cmake_ros/issues/16))
- Update maintainers ([#15](https://github.com/ros2/ament_cmake_ros/issues/15))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_target_dependencies/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-test"></a>

## [ament\_cmake\_test](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_test/CHANGELOG.rst)

- use the error handler replace to allow non-utf8 to be decoded ([#381](https://github.com/ament/ament_cmake/issues/381))
- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash, El Jawad Alaa

<a id="ament-cmake-uncrustify"></a>

## [ament\_cmake\_uncrustify](https://github.com/ament/ament_lint/tree/iron/ament_cmake_uncrustify/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_lint\_auto] General file exclusion with AMENT\_LINT\_AUTO\_FILE\_EXCLUDE ([#386](https://github.com/ament/ament_lint/issues/386))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, methylDragon

<a id="ament-cmake-vendor-package"></a>

## [ament\_cmake\_vendor\_package](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_vendor_package/CHANGELOG.rst)

- Fix the version number of ament\_cmake\_vendor\_package.
- Add ament\_cmake\_vendor\_package package ([#429](https://github.com/ament/ament_cmake/issues/429))
- Contributors: Chris Lalancette, Scott K Logan

<a id="ament-cmake-version"></a>

## [ament\_cmake\_version](https://github.com/ament/ament_cmake/tree/iron/ament_cmake_version/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#411](https://github.com/ament/ament_cmake/issues/411)) \* Update maintainers to Michael Jeronimo
- Contributors: Audrow Nash

<a id="ament-cmake-xmllint"></a>

## [ament\_cmake\_xmllint](https://github.com/ament/ament_lint/tree/iron/ament_cmake_xmllint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/iron/ament_copyright/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Support for matching license header within multiline comment block ([#361](https://github.com/ament/ament_lint/issues/361))
- Improved licencse matching ([#358](https://github.com/ament/ament_lint/issues/358))
- Updated regex and adding test cases for copyright search ([#363](https://github.com/ament/ament_lint/issues/363))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, Will, methylDragon

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/iron/ament_cppcheck/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/iron/ament_cpplint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_cpplint] Process errors without linenums ([#385](https://github.com/ament/ament_lint/issues/385))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Consider files with ‘.hh’ extension as C++ headers ([#374](https://github.com/ament/ament_lint/issues/374))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Jacob Perron, methylDragon

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/iron/ament_flake8/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Fix exclude regression ([#387](https://github.com/ament/ament_lint/issues/387))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-index-cpp"></a>

## [ament\_index\_cpp](https://github.com/ament/ament_index/tree/iron/ament_index_cpp/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#89](https://github.com/ament/ament_index/issues/89))
- Contributors: Audrow Nash

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/iron/ament_index_python/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#89](https://github.com/ament/ament_index/issues/89))
- Contributors: Audrow Nash

<a id="ament-lint"></a>

## [ament\_lint](https://github.com/ament/ament_lint/tree/iron/ament_lint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/iron/ament_lint_auto/CHANGELOG.rst)

- Add flake8 linter ignore support ([#424](https://github.com/ament/ament_lint/issues/424))
- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_lint\_auto] General file exclusion with AMENT\_LINT\_AUTO\_FILE\_EXCLUDE ([#386](https://github.com/ament/ament_lint/issues/386))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, RFRIEDM-Trimble, methylDragon

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/iron/ament_lint_cmake/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-lint-common"></a>

## [ament\_lint\_common](https://github.com/ament/ament_lint/tree/iron/ament_lint_common/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/iron/ament_mypy/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/iron/CHANGELOG.rst)

- Add support for comment lines in dsv files ([#139](https://github.com/ament/ament_package/issues/139))
- [rolling] Update maintainers - 2022-11-07 ([#138](https://github.com/ament/ament_package/issues/138))
- Mirror rolling to master
- Remove unused isolated prefix level templates ([#133](https://github.com/ament/ament_package/issues/133))
- Contributors: Audrow Nash, Scott K Logan, Shane Loretz

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/iron/ament_pclint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-pep257"></a>

## [ament\_pep257](https://github.com/ament/ament_lint/tree/iron/ament_pep257/CHANGELOG.rst)

- updating ref to pep257 docs ([#433](https://github.com/ament/ament_lint/issues/433))
- Added underscore to ignore new pydocstyle item ([#428](https://github.com/ament/ament_lint/issues/428))
- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- [ament\_pep257][master] redirecting error prints to stderr ([#390](https://github.com/ament/ament_lint/issues/390))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, Christian Henkel, Cristóbal Arroyo, Mirco Colosi (CR/AAS3), methylDragon

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/iron/ament_pycodestyle/CHANGELOG.rst)

- ament\_pycodestyle - fix crash caused by reporting on ignored errors ([#435](https://github.com/ament/ament_lint/issues/435))
- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, Shane Loretz, methylDragon

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/iron/ament_pyflakes/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/iron/ament_uncrustify/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/iron/ament_xmllint/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#421](https://github.com/ament/ament_lint/issues/421))
- Update maintainers ([#379](https://github.com/ament/ament_lint/issues/379))
- Contributors: Audrow Nash, methylDragon

<a id="builtin-interfaces"></a>

## [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/iron/builtin_interfaces/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Depend on rosidl\_core\_generators for packages required by actions ([#144](https://github.com/ros2/rcl_interfaces/issues/144))
- Fix documented range ([#139](https://github.com/ros2/rcl_interfaces/issues/139))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Tully Foote

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/iron/camera_calibration_parsers/CHANGELOG.rst)

- Update image\_common to C++17. ([#267](https://github.com/ros-perception/image_common/issues/267))
- Add alias library targets for all libraries ([#259](https://github.com/ros-perception/image_common/issues/259))
- Add support for missing ROI and binning fields ([#254](https://github.com/ros-perception/image_common/issues/254))
- Contributors: AndreasR30, Chris Lalancette, RFRIEDM-Trimble

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/iron/camera_info_manager/CHANGELOG.rst)

- Update image\_common to C++17. ([#267](https://github.com/ros-perception/image_common/issues/267))
- Add alias library targets for all libraries ([#259](https://github.com/ros-perception/image_common/issues/259))
- Add lifecycle node compatibility to camera\_info\_manager ([#190](https://github.com/ros-perception/image_common/issues/190))
- Contributors: Chris Lalancette, RFRIEDM-Trimble, Ramon Wijnands

<a id="class-loader"></a>

## [class\_loader](https://github.com/ros/class_loader/tree/iron/CHANGELOG.rst)

- make sanitizer happy ([#205](https://github.com/ros/class_loader/issues/205))
- [rolling] Update maintainers - 2022-11-07 ([#206](https://github.com/ros/class_loader/issues/206))
- Remove appveyor configuration. ([#204](https://github.com/ros/class_loader/issues/204))
- Just fix a typo in a comment. ([#203](https://github.com/ros/class_loader/issues/203))
- make the meta-object alive in the lifecycle of the registered plugin ([#201](https://github.com/ros/class_loader/issues/201))
- Mirror rolling to ros2
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette

<a id="common-interfaces"></a>

## [common\_interfaces](https://github.com/ros2/common_interfaces/tree/iron/common_interfaces/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/iron/composition/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- Added README.md for composition ([#598](https://github.com/ros2/demos/issues/598))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- fix memory leak ([#585](https://github.com/ros2/demos/issues/585))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Gary Bey, Patrick Wspanialy

<a id="composition-interfaces"></a>

## [composition\_interfaces](https://github.com/ros2/rcl_interfaces/tree/iron/composition_interfaces/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Contributors: Audrow Nash, Chris Lalancette

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/iron/demo_nodes_cpp/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Add matched event demo for rclcpp and rclpy ([#607](https://github.com/ros2/demos/issues/607))
- Fix the set\_parameters\_callback example program. ([#608](https://github.com/ros2/demos/issues/608))
- [demo\_nodes\_cpp] Add YAML launch demos for topics ([#605](https://github.com/ros2/demos/issues/605))
- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- Service introspection ([#602](https://github.com/ros2/demos/issues/602)) \* Add in a rclcpp and rclpy demo of introspection.
- Added README.md for demo\_cpp\_nodes ([#599](https://github.com/ros2/demos/issues/599))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Demo for pre and post set parameter callback support ([#565](https://github.com/ros2/demos/issues/565)) \* local parameter callback support
- counter starts from 1, not 2. ([#562](https://github.com/ros2/demos/issues/562))
- add a demo of content filter listener ([#557](https://github.com/ros2/demos/issues/557))
- Contributors: Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Damien LaRocque, Deepanshu Bansal, Gary Bey, Patrick Wspanialy, Tomoya Fujita

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/iron/demo_nodes_cpp_native/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Added README.md for demo\_cpp\_nodes\_native ([#597](https://github.com/ros2/demos/issues/597))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Make demo\_nodes\_cpp\_native install stuff only when it builds ([#590](https://github.com/ros2/demos/issues/590))
- Contributors: Audrow Nash, Chris Lalancette, Gary Bey, Shane Loretz

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/iron/demo_nodes_py/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Add matched event demo for rclcpp and rclpy ([#607](https://github.com/ros2/demos/issues/607))
- Enable document generation using rosdoc2 ([#606](https://github.com/ros2/demos/issues/606))
- Service introspection ([#602](https://github.com/ros2/demos/issues/602))
- Added README.md for demo\_nodes\_py ([#600](https://github.com/ros2/demos/issues/600))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Demo for pre and post set parameter callback support ([#565](https://github.com/ros2/demos/issues/565))
- Add demo for rclpy parameter client ([#566](https://github.com/ros2/demos/issues/566))
- Exit with code 0 if ExternalShutdownException is raised ([#581](https://github.com/ros2/demos/issues/581))
- Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette, Deepanshu Bansal, Gary Bey, Jacob Perron, Yadu

<a id="diagnostic-msgs"></a>

## [diagnostic\_msgs](https://github.com/ros2/common_interfaces/tree/iron/diagnostic_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="domain-coordinator"></a>

## [domain\_coordinator](https://github.com/ros2/ament_cmake_ros/tree/iron/domain_coordinator/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#16](https://github.com/ros2/ament_cmake_ros/issues/16))
- Update maintainers ([#15](https://github.com/ros2/ament_cmake_ros/issues/15))
- Contributors: Audrow Nash, methylDragon

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/iron/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Added README.md for dummy\_map\_server ([#572](https://github.com/ros2/demos/issues/572))
- Contributors: Audrow Nash, Chris Lalancette, Gary Bey

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/iron/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Patrick Wspanialy

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/iron/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Fix unstable LaserScan status for rviz2 ([#616](https://github.com/ros2/demos/issues/616))
- Added README.md for dummy\_sensors ([#573](https://github.com/ros2/demos/issues/573))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Gary Bey

<a id="eigen3-cmake-module"></a>

## [eigen3\_cmake\_module](https://github.com/ros2/eigen3_cmake_module/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#6](https://github.com/ros2/eigen3_cmake_module/issues/6))
- Mirror rolling to master
- Update maintainers ([#4](https://github.com/ros2/eigen3_cmake_module/issues/4))
- Contributors: Audrow Nash, methylDragon

<a id="example-interfaces"></a>

## [example\_interfaces](https://github.com/ros2/example_interfaces/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#17](https://github.com/ros2/example_interfaces/issues/17))
- Remove action\_msgs dependency ([#16](https://github.com/ros2/example_interfaces/issues/16))
- Mirror rolling to master
- Contributors: Audrow Nash, Jacob Perron

<a id="examples-rclcpp-async-client"></a>

## [examples\_rclcpp\_async\_client](https://github.com/ros2/examples/tree/iron/rclcpp/services/async_client/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-cbg-executor"></a>

## [examples\_rclcpp\_cbg\_executor](https://github.com/ros2/examples/tree/iron/rclcpp/executors/cbg_executor/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-action-client"></a>

## [examples\_rclcpp\_minimal\_action\_client](https://github.com/ros2/examples/tree/iron/rclcpp/actions/minimal_action_client/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-action-server"></a>

## [examples\_rclcpp\_minimal\_action\_server](https://github.com/ros2/examples/tree/iron/rclcpp/actions/minimal_action_server/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-client"></a>

## [examples\_rclcpp\_minimal\_client](https://github.com/ros2/examples/tree/iron/rclcpp/services/minimal_client/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-composition"></a>

## [examples\_rclcpp\_minimal\_composition](https://github.com/ros2/examples/tree/iron/rclcpp/composition/minimal_composition/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-publisher"></a>

## [examples\_rclcpp\_minimal\_publisher](https://github.com/ros2/examples/tree/iron/rclcpp/topics/minimal_publisher/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-service"></a>

## [examples\_rclcpp\_minimal\_service](https://github.com/ros2/examples/tree/iron/rclcpp/services/minimal_service/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/iron/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- add ContentFilteredTopic example. ([#341](https://github.com/ros2/examples/issues/341))
- Contributors: Audrow Nash, Chris Lalancette, Tomoya Fujita

<a id="examples-rclcpp-minimal-timer"></a>

## [examples\_rclcpp\_minimal\_timer](https://github.com/ros2/examples/tree/iron/rclcpp/timers/minimal_timer/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-multithreaded-executor"></a>

## [examples\_rclcpp\_multithreaded\_executor](https://github.com/ros2/examples/tree/iron/rclcpp/executors/multithreaded_executor/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Chris Lalancette

<a id="examples-rclcpp-wait-set"></a>

## [examples\_rclcpp\_wait\_set](https://github.com/ros2/examples/tree/iron/rclcpp/wait_set/CHANGELOG.rst)

- Update the examples to C++17. ([#353](https://github.com/ros2/examples/issues/353))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Add test linting to wait\_set and fix issues. ([#346](https://github.com/ros2/examples/issues/346)) ([#347](https://github.com/ros2/examples/issues/347))
- Contributors: Audrow Nash, Chris Lalancette, mergify[bot]

<a id="examples-rclpy-executors"></a>

## [examples\_rclpy\_executors](https://github.com/ros2/examples/tree/iron/rclpy/executors/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-guard-conditions"></a>

## [examples\_rclpy\_guard\_conditions](https://github.com/ros2/examples/tree/iron/rclpy/guard_conditions/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-minimal-action-client"></a>

## [examples\_rclpy\_minimal\_action\_client](https://github.com/ros2/examples/tree/iron/rclpy/actions/minimal_action_client/CHANGELOG.rst)

- Enable document generation using rosdoc2 for ament\_python pkgs ([#357](https://github.com/ros2/examples/issues/357)) \* Add missing action\_msgs dep \* Add exec\_deps for launch\_testing\_examples
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash, Yadu

<a id="examples-rclpy-minimal-action-server"></a>

## [examples\_rclpy\_minimal\_action\_server](https://github.com/ros2/examples/tree/iron/rclpy/actions/minimal_action_server/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-minimal-client"></a>

## [examples\_rclpy\_minimal\_client](https://github.com/ros2/examples/tree/iron/rclpy/services/minimal_client/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-minimal-publisher"></a>

## [examples\_rclpy\_minimal\_publisher](https://github.com/ros2/examples/tree/iron/rclpy/topics/minimal_publisher/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-minimal-service"></a>

## [examples\_rclpy\_minimal\_service](https://github.com/ros2/examples/tree/iron/rclpy/services/minimal_service/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-minimal-subscriber"></a>

## [examples\_rclpy\_minimal\_subscriber](https://github.com/ros2/examples/tree/iron/rclpy/topics/minimal_subscriber/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-rclpy-pointcloud-publisher"></a>

## [examples\_rclpy\_pointcloud\_publisher](https://github.com/ros2/examples/tree/iron/rclpy/topics/pointcloud_publisher/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Contributors: Audrow Nash

<a id="examples-tf2-py"></a>

## [examples\_tf2\_py](https://github.com/ros2/geometry2/tree/iron/examples_tf2_py/CHANGELOG.rst)

- Enable document generation using rosdoc2 for ament\_python pkgs ([#587](https://github.com/ros2/geometry2/issues/587))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Yadu

<a id="fastrtps-cmake-module"></a>

## [fastrtps\_cmake\_module](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/iron/fastrtps_cmake_module/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#93](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/93))
- Contributors: Audrow Nash

<a id="foonathan-memory-vendor"></a>

## [foonathan\_memory\_vendor](https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst)

- Added support for QNX 7.1 build (#65)
- Update upstream to release 0.7-3 (#62)(#63)
- Fix CMake minimum required version (#60)

<a id="geometry2"></a>

## [geometry2](https://github.com/ros2/geometry2/tree/iron/geometry2/CHANGELOG.rst)

- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/iron/geometry_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="google-benchmark-vendor"></a>

## [google\_benchmark\_vendor](https://github.com/ament/google_benchmark_vendor/tree/iron/CHANGELOG.rst)

- Actually update to 1.6.1. ([#25](https://github.com/ament/google_benchmark_vendor/issues/25)) We claimed we were, but in fact we were pinned to the 1.5.3 git hash.
- Remove set but unused variable ([#24](https://github.com/ament/google_benchmark_vendor/issues/24)) Clang checks -Wunused-but-set-variable. This fails the build with -Werror also enabled.
- [rolling] Update maintainers - 2022-11-07 ([#22](https://github.com/ament/google_benchmark_vendor/issues/22))
- Mirror rolling to main
- Contributors: Audrow Nash, Chris Lalancette, Michael Carroll

<a id="ignition-cmake2-vendor"></a>

## [ignition\_cmake2\_vendor](https://github.com/gazebo-release/gz_cmake2_vendor/tree/iron/CHANGELOG.rst)

- Set target version to 2.14.0 ([#5](https://github.com/gazebo-release/gz_cmake2_vendor/issues/5))
- Mirror rolling to main
- Contributors: Audrow Nash, Yadu

<a id="ignition-math6-vendor"></a>

## [ignition\_math6\_vendor](https://github.com/gazebo-release/gz_math6_vendor/tree/iron/CHANGELOG.rst)

- Forward CMAKE\_PREFIX\_PATH when building vendor package ([#8](https://github.com/gazebo-release/gz_math6_vendor/issues/8))
- Contributors: Scott K Logan

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/iron/image_tools/CHANGELOG.rst)

- Added README.md for image\_tools - [Clean] ([#596](https://github.com/ros2/demos/issues/596))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette, Gary Bey

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/iron/image_transport/CHANGELOG.rst)

- Update image\_common to C++17. ([#267](https://github.com/ros-perception/image_common/issues/267))
- Add alias library targets for all libraries ([#259](https://github.com/ros-perception/image_common/issues/259))
- Remove subscriber and publisher impl methods without options ([#252](https://github.com/ros-perception/image_common/issues/252))
- Deprecate impl without options ([#249](https://github.com/ros-perception/image_common/issues/249))
- opt-in to qos overriding for publisher ([#246](https://github.com/ros-perception/image_common/issues/246))
- Add qos option to override qos ([#208](https://github.com/ros-perception/image_common/issues/208))
- Contributors: Brian, Chris Lalancette, Daisuke Nishimatsu, Kenji Brameld, RFRIEDM-Trimble

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/iron/CHANGELOG.rst)

- Update interactive\_markers to C++17. ([#99](https://github.com/ros-visualization/interactive_markers/issues/99))
- Update maintainers ([#98](https://github.com/ros-visualization/interactive_markers/issues/98))
- Mirror rolling to ros2
- update maintainer ([#92](https://github.com/ros-visualization/interactive_markers/issues/92))
- Contributors: Audrow Nash, Chris Lalancette, Dharini Dutia

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/iron/intra_process_demo/CHANGELOG.rst)

- Fix executable name in README ([#619](https://github.com/ros2/demos/issues/619))
- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Added README.md for intra\_process\_demo ([#595](https://github.com/ros2/demos/issues/595))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette, Gary Bey, Yadunund

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/iron/kdl_parser/CHANGELOG.rst)

- Switch some tests to use unique pointers instead of raw pointers. ([#74](https://github.com/ros/kdl_parser/issues/74))
- log link children as DEBUG instead of INFO ([#71](https://github.com/ros/kdl_parser/issues/71))
- Enable the kdl\_parser tests in ROS 2 ([#68](https://github.com/ros/kdl_parser/issues/68))
- Add in a LICENSE file and fix up copyright headers ([#66](https://github.com/ros/kdl_parser/issues/66))
- Use orocos\_kdl\_vendor and orocos-kdl target ([#64](https://github.com/ros/kdl_parser/issues/64))
- Use the rcutils logger instead of printf ([#65](https://github.com/ros/kdl_parser/issues/65))
- Contributors: Chris Lalancette, Joseph Schornak, Scott K Logan, yuraSomatic

<a id="keyboard-handler"></a>

## [keyboard\_handler](https://github.com/ros-tooling/keyboard_handler/tree/iron/keyboard_handler/CHANGELOG.rst)

- Force exit from main thread on signal handling in `keyboard_handler` ([#23](https://github.com/ros-tooling/keyboard_handler/issues/23))
- Contributors: Michael Orlov

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/iron/CHANGELOG.rst)

- Update laser\_geometry to C++17. ([#90](https://github.com/ros-perception/laser_geometry/issues/90))
- Update Maintainers ([#88](https://github.com/ros-perception/laser_geometry/issues/88))
- Mirror rolling to ros2
- Contributors: Audrow Nash, Chris Lalancette

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/iron/launch/CHANGELOG.rst)

- Document LaunchService.{run,run\_async}() return value ([#702](https://github.com/ros2/launch/issues/702))
- [rosdoc2] Fix document generation on buildfarm ([#701](https://github.com/ros2/launch/issues/701))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#697](https://github.com/ros2/launch/issues/697))
- Remove the import of Literal from entity.py. ([#694](https://github.com/ros2/launch/issues/694))
- Fix flake8 errors. ([#695](https://github.com/ros2/launch/issues/695))
- add symlink to latest log directory ([#686](https://github.com/ros2/launch/issues/686))
- Improve type checking ([#679](https://github.com/ros2/launch/issues/679))
- Fixed typos ([#692](https://github.com/ros2/launch/issues/692))
- Pass modules to PythonExpression ([#655](https://github.com/ros2/launch/issues/655))
- Allow ReadyToTest() usage in event handler ([#665](https://github.com/ros2/launch/issues/665))
- Expose emulate\_tty to xml and yaml launch ([#669](https://github.com/ros2/launch/issues/669))
- Expose sigterm\_timeout and sigkill\_timeout to xml frontend ([#667](https://github.com/ros2/launch/issues/667))
- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Expect deprecation warnings in tests ([#657](https://github.com/ros2/launch/issues/657))
- Fix the restoring of os.environ to maintain type. ([#656](https://github.com/ros2/launch/issues/656))
- Implement Any, All, Equals, and NotEquals substitutions ([#649](https://github.com/ros2/launch/issues/649))
- add LaunchLogDir substitution, replacing log\_dir frontend only substitution ([#652](https://github.com/ros2/launch/issues/652))
- Add special cases to coerce “1” and “0” to bool when using bool coercion only ([#651](https://github.com/ros2/launch/issues/651))
- Update launch/test/launch/test\_execute\_local.py
- Added unit test ensuring that output dictionary works with ExecuteLocal
- Addresses issue [#588](https://github.com/ros2/launch/issues/588), allowing dict for ‘output’
- Remove unused variables. ([#612](https://github.com/ros2/launch/issues/612))
- Expose shutdown action to xml frontend ([#611](https://github.com/ros2/launch/issues/611))
- Contributors: Aditya Pande, Alejandro Hernández Cordero, Audrow Nash, Blake Anderson, Chris Lalancette, Christophe Bedard, Hervé Audren, Jacob Perron, Matthew Elwin, Michael Jeronimo, Nikolai Morin, Welte, William Woodall, Yadu, methylDragon

<a id="launch-pytest"></a>

## [launch\_pytest](https://github.com/ros2/launch/tree/iron/launch_pytest/CHANGELOG.rst)

- Fixed typos ([#692](https://github.com/ros2/launch/issues/692))
- Drop unused data\_files entry for example\_processes ([#680](https://github.com/ros2/launch/issues/680))
- Spelling correction
- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Geoffrey Biggs, Scott K Logan

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/iron/launch_ros/CHANGELOG.rst)

- Use SomeEntitiesType for type checking. ([#358](https://github.com/ros2/launch_ros/issues/358))
- Fix normalize\_parameters\_dict for multiple nodes in the same namespace ([#347](https://github.com/ros2/launch_ros/issues/347))
- Implement None check for ComposableNodeContainer ([#341](https://github.com/ros2/launch_ros/issues/341))
- Add LifecyleTransition action ([#317](https://github.com/ros2/launch_ros/issues/317))
- Improve evaluate\_paramenter\_dict exceptions error message ([#320](https://github.com/ros2/launch_ros/issues/320))
- Ensure load\_composable\_nodes respects condition ([#339](https://github.com/ros2/launch_ros/issues/339))
- fix: return text value to avoid exception ([#338](https://github.com/ros2/launch_ros/issues/338))
- [rolling] Update maintainers - 2022-11-07 ([#331](https://github.com/ros2/launch_ros/issues/331))
- RosTimer -> ROSTimer and PushRosNamespace -> PushROSNamespace, to follow PEP8 ([#326](https://github.com/ros2/launch_ros/issues/326))
- add SetROSLogDir action ([#325](https://github.com/ros2/launch_ros/issues/325))
- Support default values in parameter substitution ([#313](https://github.com/ros2/launch_ros/issues/313))
- Run condition for composable nodes ([#311](https://github.com/ros2/launch_ros/issues/311))
- Contributors: Aditya Pande, Alexey Merzlyakov, Audrow Nash, Chris Lalancette, Christoph Hellmann Santos, Daisuke Nishimatsu, Felipe Gomes de Melo, Kenji Miyake, William Woodall, methylDragon

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/iron/launch_testing/CHANGELOG.rst)

- Improve type checking ([#679](https://github.com/ros2/launch/issues/679))
- Fixed typos ([#692](https://github.com/ros2/launch/issues/692))
- Allow ReadyToTest() usage in event handler ([#665](https://github.com/ros2/launch/issues/665))
- Inherit markers from generate\_test\_description ([#670](https://github.com/ros2/launch/issues/670))
- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Fix Typo ([#641](https://github.com/ros2/launch/issues/641))
- ReadyToTest action timeout using decorator ([#625](https://github.com/ros2/launch/issues/625))
- Switch to using a comprehension for process\_names. ([#614](https://github.com/ros2/launch/issues/614))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Deepanshu Bansal, Hervé Audren, Kenji Brameld, Nikolai Morin, Scott K Logan

<a id="launch-testing-ament-cmake"></a>

## [launch\_testing\_ament\_cmake](https://github.com/ros2/launch/tree/iron/launch_testing_ament_cmake/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Contributors: Audrow Nash

<a id="launch-testing-examples"></a>

## [launch\_testing\_examples](https://github.com/ros2/examples/tree/iron/launch_testing/launch_testing_examples/CHANGELOG.rst)

- Enable document generation using rosdoc2 for ament\_python pkgs ([#357](https://github.com/ros2/examples/issues/357))
- increase the timeout for window platform to avoid flaky test ([#355](https://github.com/ros2/examples/issues/355))
- [rolling] Update maintainers - 2022-11-07 ([#352](https://github.com/ros2/examples/issues/352))
- Increase the WaitForNode timeout. ([#350](https://github.com/ros2/examples/issues/350))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Yadu

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/iron/launch_testing_ros/CHANGELOG.rst)

- Increase the timeouts in wait\_for\_topic\_launch\_test. ([#360](https://github.com/ros2/launch_ros/issues/360))
- Enable document generation using rosdoc2 ([#359](https://github.com/ros2/launch_ros/issues/359))
- exit() methods should not reraise the passed-in exception ([#357](https://github.com/ros2/launch_ros/issues/357))
- Inherit markers from generate\_test\_description ([#330](https://github.com/ros2/launch_ros/issues/330))
- [rolling] Update maintainers - 2022-11-07 ([#331](https://github.com/ros2/launch_ros/issues/331))
- Fix long wait during shutdown in WaitForTopics ([#314](https://github.com/ros2/launch_ros/issues/314))
- Contributors: Audrow Nash, Chris Lalancette, Giorgio Pintaudi, Keng12, Scott K Logan, Yadu

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/iron/launch_xml/CHANGELOG.rst)

- Fixed typos ([#692](https://github.com/ros2/launch/issues/692))
- Expose emulate\_tty to xml and yaml launch ([#669](https://github.com/ros2/launch/issues/669))
- Expose sigterm\_timeout and sigkill\_timeout to xml frontend ([#667](https://github.com/ros2/launch/issues/667))
- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Contributors: Aditya Pande, Alejandro Hernández Cordero, Audrow Nash

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/iron/launch_yaml/CHANGELOG.rst)

- Expose emulate\_tty to xml and yaml launch ([#669](https://github.com/ros2/launch/issues/669))
- Expose sigterm\_timeout and sigkill\_timeout to xml frontend ([#667](https://github.com/ros2/launch/issues/667))
- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Contributors: Aditya Pande, Audrow Nash

<a id="libcurl-vendor"></a>

## [libcurl\_vendor](https://github.com/ros/resource_retriever/tree/iron/libcurl_vendor/CHANGELOG.rst)

- merge libcurl\_vendor build instructions ([#81](https://github.com/ros/resource_retriever/issues/81))
- Sets CMP0135 policy behavior to NEW ([#79](https://github.com/ros/resource_retriever/issues/79))
- Fixes policy CMP0135 warning for CMake >= 3.24
- Contributors: Cristóbal Arroyo, Crola1702, schrodinbug

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/iron/CHANGELOG.rst)

- Bump hmarr/auto-approve-action from 3.2.0 to 3.2.1
- Mark benchmark \_ as unused. ([#158](https://github.com/ros-tooling/libstatistics_collector/issues/158))
- Bump hmarr/auto-approve-action from 3.1.0 to 3.2.0
- Bump ros-tooling/action-ros-ci from 0.2 to 0.3
- Bump pascalgn/automerge-action from 0.15.5 to 0.15.6
- Update libstatistics\_collector to C++17. ([#154](https://github.com/ros-tooling/libstatistics_collector/issues/154))
- Remove unnecessary build dependency on std\_msgs. ([#145](https://github.com/ros-tooling/libstatistics_collector/issues/145))
- Bump pascalgn/automerge-action from 0.15.2 to 0.15.3
- Cleanup the CI jobs on this repository. ([#146](https://github.com/ros-tooling/libstatistics_collector/issues/146))
- Check if message has a “header” field with a stamp subfield of type builtin\_interfaces::msg::Time ([#54](https://github.com/ros-tooling/libstatistics_collector/issues/54))
- Mirror rolling to master
- Contributors: Audrow Nash, Chris Lalancette, Scott Mende, dependabot[bot]

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/iron/CHANGELOG.rst)

- Fix system package dependency ([#54](https://github.com/ros2/libyaml_vendor/issues/54))
- Update libyaml\_vendor to C++17. ([#55](https://github.com/ros2/libyaml_vendor/issues/55))
- [rolling] Update maintainers - 2022-11-07 ([#53](https://github.com/ros2/libyaml_vendor/issues/53))
- Remove a warning message. ([#51](https://github.com/ros2/libyaml_vendor/issues/51))
- check if libyaml is already present before building it (take 2) ([#45](https://github.com/ros2/libyaml_vendor/issues/45))
- Mirror rolling to master
- Support WindowsStore builds for ROS2 ([#50](https://github.com/ros2/libyaml_vendor/issues/50)) \* libyaml for uwp
- Contributors: Audrow Nash, Chris Lalancette, Lou Amadio, Scott K Logan, Silvio Traversaro

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/iron/lifecycle/CHANGELOG.rst)

- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette, Patrick Wspanialy

<a id="lifecycle-msgs"></a>

## [lifecycle\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/lifecycle_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- lifecycle\_msgs: remove non-ASCII chars from field comments ([#147](https://github.com/ros2/rcl_interfaces/issues/147))
- Contributors: Audrow Nash, Chris Lalancette, G.A. vd. Hoorn

<a id="lifecycle-py"></a>

## [lifecycle\_py](https://github.com/ros2/demos/tree/iron/lifecycle_py/CHANGELOG.rst)

- Enable document generation using rosdoc2 ([#606](https://github.com/ros2/demos/issues/606))
- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- Cleanup lifecycle\_py to conform to ROS 2 standards. ([#604](https://github.com/ros2/demos/issues/604))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Install the launch file for lifecycle\_py. ([#586](https://github.com/ros2/demos/issues/586))
- Contributors: Audrow Nash, Chris Lalancette, Patrick Wspanialy, Yadu

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/iron/logging_demo/CHANGELOG.rst)

- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Change dependency from ‘rosidl\_cmake’ to ‘rosidl\_default\_generators’ ([#578](https://github.com/ros2/demos/issues/578))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="map-msgs"></a>

## [map\_msgs](https://github.com/ros-planning/navigation_msgs/tree/iron/map_msgs/CHANGELOG.rst)

- Update maintainers
- Contributors: Audrow Nash, Steve Macenski

<a id="mcap-vendor"></a>

## [mcap\_vendor](https://github.com/ros2/rosbag2/tree/iron/mcap_vendor/CHANGELOG.rst)

- mcap\_vendor: add readme with versioning procedure ([#1230](https://github.com/ros2/rosbag2/issues/1230))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- mcap\_vendor: only install public headers ([#1207](https://github.com/ros2/rosbag2/issues/1207))
- Fixes policy CMP0135 warning for CMake >= 3.24 for mcap\_vendor ([#1208](https://github.com/ros2/rosbag2/issues/1208))
- mcap\_vendor: download MCAP source via tarball ([#1204](https://github.com/ros2/rosbag2/issues/1204))
- rosbag2\_cpp: test more than one storage plugin ([#1196](https://github.com/ros2/rosbag2/issues/1196))
- rosbag2\_storage\_mcap: merge into rosbag2 repo ([#1163](https://github.com/ros2/rosbag2/issues/1163))
- Fix Windows build ([#73](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/73)) Update mcap version to newest windows-compatible release. Add visibility macros for tests. Add clang-format preprocessor indentation for visibility\_control to be readable.
- mcap\_vendor: update to v0.6.0 ([#69](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/69))
- Cleanup in `mcap_vendor` package ([#62](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/62))
- Switch to using the vendored zstd library. ([#59](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/59))
- Support timestamp-ordered playback ([#50](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/50))
- Support regex topic filtering
- Add all lz4 sources to fix undefined symbols at runtime ([#46](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/46))
- Upgrade mcap to fix LZ4 error and segfault ([#42](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/42)) Incorporates fixes from <https://github.com/foxglove/mcap/pull/478> and <https://github.com/foxglove/mcap/pull/482>
- Add missing buildtool\_depend on git ([#37](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/37)) This vendor package uses git to fetch sources for other packages. It should declare a dependency on that build tool. This should address the current cause of RPM build failures for RHEL: <https://build.ros2.org/view/Rbin_rhel_el864/job/Rbin_rhel_el864__mcap_vendor__rhel_8_x86_64__binary/>
- Test Foxy & Galactic in CI, fix missing test\_depends in mcap\_vendor/package.xml ([#33](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/33))
- fix: minor issues ([#31](https://github.com/wep21/rosbag2_storage_mcap/issues/31)) \* remove unnecessary block \* use target\_link\_libraries instead of ament\_target\_dependencies \* remove ros environment \* add prefix to compile definition
- Update email address for Foxglove maintainers ([#32](https://github.com/wep21/rosbag2_storage_mcap/issues/32))
- Added mcap\_vendor package. Updated CMakeLists.txt to fetch dependencies with FetchContent rather than Conan.
- Contributors: Chris Lalancette, Cristóbal Arroyo, Daisuke Nishimatsu, Emerson Knapp, Jacob Bandes-Storch, James Smith, Michael Orlov, Scott K Logan, james-rms

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/iron/CHANGELOG.rst)

- Update message\_filters to C++17. ([#88](https://github.com/ros2/message_filters/issues/88))
- Fix cache.h std::placeholder namespace ([#87](https://github.com/ros2/message_filters/issues/87))
- [rolling] Update maintainers - 2022-11-07 ([#85](https://github.com/ros2/message_filters/issues/85))
- Add a simpler aproximate time sync policy: ApproximateEpsilonTime ([#84](https://github.com/ros2/message_filters/issues/84))
- Add latest time zero-order-hold sync policy ([#73](https://github.com/ros2/message_filters/issues/73))
- Fix python examples and add a new example in documentation ([#79](https://github.com/ros2/message_filters/issues/79))
- Mirror rolling to master
- Adding fix to subscribe() call with raw node pointer and subscriber options ([#76](https://github.com/ros2/message_filters/issues/76))
- Corrected function arguments in example description ([#35](https://github.com/ros2/message_filters/issues/35))
- Changed invocation to `add` to conform template syntax ([#1388](https://github.com/ros2/message_filters/issues/1388))
- fix sphinx warning ([#1371](https://github.com/ros2/message_filters/issues/1371))
- change invocation to `add` to conform template syntax ([#1388](https://github.com/ros/ros_comm/issues/1388))
- fix sphinx warning ([#1371](https://github.com/ros/ros_comm/issues/1371))
- Contributors: Audrow Nash, Carlos Andrés Álvarez Restrepo, Chris Lalancette, Haoru Xue, Ivan Santiago Paunovic, Martin Ganeff, Steve Macenski, andermi

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#29](https://github.com/ros2/mimick_vendor/issues/29))
- Mirror rolling to master
- Contributors: Audrow Nash

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/iron/nav_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="orocos-kdl-vendor"></a>

## [orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/iron/orocos_kdl_vendor/CHANGELOG.rst)

- Make sure to quote orocos variables when setting targets. ([#12](https://github.com/ros2/orocos_kdl_vendor/issues/12))
- Ensure orocos-kdl is available as a target ([#10](https://github.com/ros2/orocos_kdl_vendor/issues/10))
- Ensure orocos-kdl target references Eigen ([#6](https://github.com/ros2/orocos_kdl_vendor/issues/6))
- Contributors: Chris Lalancette, Scott K Logan

<a id="osrf-pycommon"></a>

## [osrf\_pycommon](https://github.com/osrf/osrf_pycommon/tree/master/CHANGELOG.rst)

- [master] Update maintainers - 2022-11-07 ([#89](https://github.com/osrf/osrf_pycommon/issues/89))
- Declare test dependencies in [test] extra ([#86](https://github.com/osrf/osrf_pycommon/issues/86))
- Contributors: Audrow Nash, Scott K Logan

<a id="osrf-testing-tools-cpp"></a>

## [osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/iron/osrf_testing_tools_cpp/CHANGELOG.rst)

- Fix mpark/variant conditional for MSVC ([#77](https://github.com/osrf/osrf_testing_tools_cpp/issues/77))
- Changing C++ Compile Version ([#76](https://github.com/osrf/osrf_testing_tools_cpp/issues/76))
- Update maintainers ([#74](https://github.com/osrf/osrf_testing_tools_cpp/issues/74))
- Sets CMP0135 policy behavior to NEW ([#73](https://github.com/osrf/osrf_testing_tools_cpp/issues/73))
- Fixes policy CMP0135 warning in CMake 3.24 ([#71](https://github.com/osrf/osrf_testing_tools_cpp/issues/71))
- Add cstring include. ([#70](https://github.com/osrf/osrf_testing_tools_cpp/issues/70))
- Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Lucas Wendland, Scott K Logan

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/iron/pendulum_control/CHANGELOG.rst)

- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/iron/pendulum_msgs/CHANGELOG.rst)

- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- A couple more upgrades to C++17. ([#609](https://github.com/ros2/demos/issues/609))
- Added README.md for pendulum\_msgs. ([#577](https://github.com/ros2/demos/issues/577))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette, Gary Bey

<a id="performance-test-fixture"></a>

## [performance\_test\_fixture](https://github.com/ros2/performance_test_fixture/tree/iron/CHANGELOG.rst)

- Resolve use-after-free compiler warnings ([#24](https://github.com/ros2/performance_test_fixture/issues/24))
- Update performance\_test\_fixture to C++17. ([#21](https://github.com/ros2/performance_test_fixture/issues/21))
- [rolling] Update maintainers - 2022-11-07 ([#20](https://github.com/ros2/performance_test_fixture/issues/20))
- Mirror rolling to main
- Add “cstring” to the list of includes ([#19](https://github.com/ros2/performance_test_fixture/issues/19))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/iron/pluginlib/CHANGELOG.rst)

- Update maintainers
- Contributors: Audrow Nash

<a id="pybind11-vendor"></a>

## [pybind11\_vendor](https://github.com/ros2/pybind11_vendor/tree/iron/CHANGELOG.rst)

- Add a modified patch from upstream to support Python 3.11 ([#22](https://github.com/ros2/pybind11_vendor/issues/22))
- Add missing buildtool dependency on git ([#19](https://github.com/ros2/pybind11_vendor/issues/19))
- Update maintainers ([#17](https://github.com/ros2/pybind11_vendor/issues/17))
- Force pybind11 to find Python 3. ([#15](https://github.com/ros2/pybind11_vendor/issues/15))
- Mirror rolling to master
- Update maintainers ([#14](https://github.com/ros2/pybind11_vendor/issues/14))
- Update to pybind11 2.9.1.
- Rename patch file for history continuity.
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Steven! Ragnarök, methylDragon

<a id="python-cmake-module"></a>

## [python\_cmake\_module](https://github.com/ros2/python_cmake_module/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#13](https://github.com/ros2/python_cmake_module/issues/13))
- Mirror rolling to master
- Contributors: Audrow Nash

<a id="python-orocos-kdl-vendor"></a>

## [python\_orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/iron/python_orocos_kdl_vendor/CHANGELOG.rst)

- Fixes policy CMP0135 warning for CMake >= 3.24 ([#16](https://github.com/ros2/orocos_kdl_vendor/issues/16))
- Workaround pybind11 CMake error ([#9](https://github.com/ros2/orocos_kdl_vendor/issues/9))
- Contributors: Cristóbal Arroyo, Jacob Perron

<a id="python-qt-binding"></a>

## [python\_qt\_binding](https://github.com/ros-visualization/python_qt_binding/tree/iron/CHANGELOG.rst)

- Fix to allow ninja to use make for generators ([#123](https://github.com/ros-visualization/python_qt_binding/issues/123))
- Fix flake8 linter regression ([#125](https://github.com/ros-visualization/python_qt_binding/issues/125))
- Remove pyqt from default binding order for macOS ([#118](https://github.com/ros-visualization/python_qt_binding/issues/118))
- Demote missing SIP message from WARNING to STATUS ([#122](https://github.com/ros-visualization/python_qt_binding/issues/122))
- [rolling] Update maintainers - 2022-11-07 ([#120](https://github.com/ros-visualization/python_qt_binding/issues/120))
- Contributors: Audrow Nash, Christoph Hellmann Santos, Cristóbal Arroyo, Michael Carroll, Rhys Mainwaring, Scott K Logan

<a id="qt-dotgraph"></a>

## [qt\_dotgraph](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_dotgraph/CHANGELOG.rst)

- Add in LICENSE file
- Cast drawLine input arguments to int ([#264](https://github.com/ros-visualization/qt_gui_core/issues/264)) ([#265](https://github.com/ros-visualization/qt_gui_core/issues/265))
- Contributors: Chris Lalancette, mergify[bot]

<a id="qt-gui"></a>

## [qt\_gui](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_gui/CHANGELOG.rst)

- Add in LICENSE file
- Fix flake8 errors introduced by the previous commit. ([#262](https://github.com/ros-visualization/qt_gui_core/issues/262))
- Enable basic help information if no plugins are running ([#261](https://github.com/ros-visualization/qt_gui_core/issues/261))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="qt-gui-app"></a>

## [qt\_gui\_app](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_gui_app/CHANGELOG.rst)

- Add in LICENSE file
- Contributors: Chris Lalancette

<a id="qt-gui-core"></a>

## [qt\_gui\_core](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_gui_core/CHANGELOG.rst)

- Add in LICENSE file
- Contributors: Chris Lalancette

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_gui_cpp/CHANGELOG.rst)

- Fix ClassLoader warning by unloading plugin providers. ([#275](https://github.com/ros-visualization/qt_gui_core/issues/275))
- Chen Lihui
- fix shiboken error ([#267](https://github.com/ros-visualization/qt_gui_core/issues/267))
- Conditionally run import tests when generators are built ([#269](https://github.com/ros-visualization/qt_gui_core/issues/269))
- Add in LICENSE file
- Contributors: Chris Lalancette, Christoph Hellmann Santos, Michael Carroll, Rhys Mainwaring, Scott K Logan

<a id="qt-gui-py-common"></a>

## [qt\_gui\_py\_common](https://github.com/ros-visualization/qt_gui_core/tree/iron/qt_gui_py_common/CHANGELOG.rst)

- Add in LICENSE file
- Contributors: Chris Lalancette

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/iron/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/iron/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Use non-deprecated rclpy import. ([#617](https://github.com/ros2/demos/issues/617))
- Change all ROS2 -> ROS 2. ([#610](https://github.com/ros2/demos/issues/610))
- Enable document generation using rosdoc2 ([#606](https://github.com/ros2/demos/issues/606))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Exit with code 0 if ExternalShutdownException is raised ([#581](https://github.com/ros2/demos/issues/581))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Yadu

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/iron/rcl/CHANGELOG.rst)

- Honor ROS\_LOCALHOST\_ONLY if enabled. ([#1071](https://github.com/ros2/rcl/issues/1071))
- fix flaky test ([#1063](https://github.com/ros2/rcl/issues/1063))
- Add enable\_type\_description\_service node option - API only ([#1060](https://github.com/ros2/rcl/issues/1060))
- Dynamic Subscription (BONUS: Allocators): rcl ([#1057](https://github.com/ros2/rcl/issues/1057))
- Runtime Interface Reflection: rcl ([#1025](https://github.com/ros2/rcl/issues/1025))
- [rcl] Improve handling of dynamic discovery ([#1023](https://github.com/ros2/rcl/issues/1023))
- Use get\_type\_hash\_func for typesupports ([#1055](https://github.com/ros2/rcl/issues/1055))
- publish for rosout topic multiple times to avoid flaky test ([#1054](https://github.com/ros2/rcl/issues/1054))
- Switch to target\_link\_libraries in rcl. ([#1051](https://github.com/ros2/rcl/issues/1051))
- Calculate type hash from TypeDescription (rep2011) ([#1027](https://github.com/ros2/rcl/issues/1027))
- Implement matched event ([#1033](https://github.com/ros2/rcl/issues/1033))
- use user-defined allocator to configure logging. ([#1047](https://github.com/ros2/rcl/issues/1047))
- user defined allocator should be used for rosout publisher. ([#1044](https://github.com/ros2/rcl/issues/1044))
- Add in inconsistent\_topic implementation. ([#1024](https://github.com/ros2/rcl/issues/1024))
- doc update, ROS message accessibility depends on RMW implementation. ([#1043](https://github.com/ros2/rcl/issues/1043))
- Fix some warnings from clang. ([#1042](https://github.com/ros2/rcl/issues/1042))
- avoid unnecessary copy for rcutils\_char\_array\_vsprintf. ([#1035](https://github.com/ros2/rcl/issues/1035))
- Service introspection ([#997](https://github.com/ros2/rcl/issues/997))
- Cache disable flag to avoid reading environmental variable. ([#1029](https://github.com/ros2/rcl/issues/1029))
- use parent logger ([#921](https://github.com/ros2/rcl/issues/921))
- Add timer on reset callback ([#995](https://github.com/ros2/rcl/issues/995))
- Update rcl to C++17. ([#1031](https://github.com/ros2/rcl/issues/1031))
- Make sure to check the return value of rcl\_clock\_init in tests. ([#1030](https://github.com/ros2/rcl/issues/1030))
- Implement rcl\_clock\_time\_started ([#1021](https://github.com/ros2/rcl/issues/1021))
- Make sure to reset errors more places in the tests. ([#1020](https://github.com/ros2/rcl/issues/1020)) This makes it so we don’t get as many warnings when the tests are running.
- [rolling] Update maintainers - 2022-11-07 ([#1017](https://github.com/ros2/rcl/issues/1017))
- Small cleanups to rcl ([#1013](https://github.com/ros2/rcl/issues/1013))
- use int64\_t for period. ([#1010](https://github.com/ros2/rcl/issues/1010))
- fixed rcl\_wait return error when timer cancelled ([#1003](https://github.com/ros2/rcl/issues/1003))
- remove duplicate packages in find\_package and reorder ([#994](https://github.com/ros2/rcl/issues/994))
- Fix buffer overflow in argument parsing caused by lexer returning length beyond length of string ([#979](https://github.com/ros2/rcl/issues/979))
- Fix leak in test\_subscription\_content\_filter\_options.cpp ([#978](https://github.com/ros2/rcl/issues/978))
- Contributors: Audrow Nash, Barry Xu, Brian, Chen Lihui, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Shane Loretz, Tomoya Fujita, mauropasse, methylDragon, 정찬희

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/iron/rcl_action/CHANGELOG.rst)

- doc update, ROS message accessibility depends on RMW implementation. ([#1043](https://github.com/ros2/rcl/issues/1043))
- Update rcl to C++17. ([#1031](https://github.com/ros2/rcl/issues/1031))
- Reduce result\_timeout to 10 seconds. ([#1012](https://github.com/ros2/rcl/issues/1012))
- [rolling] Update maintainers - 2022-11-07 ([#1017](https://github.com/ros2/rcl/issues/1017))
- Contributors: Audrow Nash, Chris Lalancette, Tomoya Fujita

<a id="rcl-interfaces"></a>

## [rcl\_interfaces](https://github.com/ros2/rcl_interfaces/tree/iron/rcl_interfaces/CHANGELOG.rst)

- Add interfaces for logging service. ([#154](https://github.com/ros2/rcl_interfaces/issues/154))
- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Contributors: Audrow Nash, Chris Lalancette, Lei Liu

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/iron/rcl_lifecycle/CHANGELOG.rst)

- Update rcl to C++17. ([#1031](https://github.com/ros2/rcl/issues/1031))
- [rolling] Update maintainers - 2022-11-07 ([#1017](https://github.com/ros2/rcl/issues/1017))
- Contributors: Audrow Nash, Chris Lalancette

<a id="rcl-logging-interface"></a>

## [rcl\_logging\_interface](https://github.com/ros2/rcl_logging/tree/iron/rcl_logging_interface/CHANGELOG.rst)

- Update rcl\_logging to C++17. ([#98](https://github.com/ros2/rcl_logging/issues/98))
- Updated maintainers - 2022-11-07 ([#96](https://github.com/ros2/rcl_logging/issues/96))
- Contributors: Audrow Nash, Chris Lalancette

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/iron/rcl_logging_noop/CHANGELOG.rst)

- Update rcl\_logging to C++17. ([#98](https://github.com/ros2/rcl_logging/issues/98))
- Updated maintainers - 2022-11-07 ([#96](https://github.com/ros2/rcl_logging/issues/96))
- Contributors: Audrow Nash, Chris Lalancette

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/iron/rcl_logging_spdlog/CHANGELOG.rst)

- Mark the benchmark \_ as unused. ([#99](https://github.com/ros2/rcl_logging/issues/99))
- Update rcl\_logging to C++17. ([#98](https://github.com/ros2/rcl_logging/issues/98))
- change flushing behavior for spdlog log files, and add env var to use old style (no explicit flushing) ([#95](https://github.com/ros2/rcl_logging/issues/95)) \* now flushes every ERROR message and periodically every 5 seconds \* can set `RCL_LOGGING_SPDLOG_EXPERIMENTAL_OLD_FLUSHING_BEHAVIOR=1` to get old behavior
- Updated maintainers - 2022-11-07 ([#96](https://github.com/ros2/rcl_logging/issues/96))
- Disable cppcheck for rcl\_logging\_spdlog. ([#93](https://github.com/ros2/rcl_logging/issues/93))
- ament\_export\_dependencies any package with targets we linked against ([#89](https://github.com/ros2/rcl_logging/issues/89))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz, William Woodall

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/iron/rcl_yaml_param_parser/CHANGELOG.rst)

- Fix some warnings from clang. ([#1042](https://github.com/ros2/rcl/issues/1042))
- Cleanup the dependencies in rcl\_yaml\_param\_parser. ([#1014](https://github.com/ros2/rcl/issues/1014))
- Update rcl to C++17. ([#1031](https://github.com/ros2/rcl/issues/1031))
- Support yaml string tag ‘!!str’ ([#999](https://github.com/ros2/rcl/issues/999))
- [rolling] Update maintainers - 2022-11-07 ([#1017](https://github.com/ros2/rcl/issues/1017))
- Contributors: Audrow Nash, Barry Xu, Chris Lalancette

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/iron/rclcpp/CHANGELOG.rst)

- Fix delivered message kind ([#2175](https://github.com/ros2/rclcpp/issues/2175)) ([#2178](https://github.com/ros2/rclcpp/issues/2178))
- Add support for logging service. ([#2122](https://github.com/ros2/rclcpp/issues/2122))
- Picking ABI-incompatible executor changes ([#2170](https://github.com/ros2/rclcpp/issues/2170))
- add events-executor and timers-manager in rclcpp ([#2155](https://github.com/ros2/rclcpp/issues/2155))
- Create common structures for executors to use ([#2143](https://github.com/ros2/rclcpp/issues/2143))
- Implement deliver message kind ([#2168](https://github.com/ros2/rclcpp/issues/2168))
- applied tracepoints for ring\_buffer ([#2091](https://github.com/ros2/rclcpp/issues/2091))
- Dynamic Subscription (REP-2011 Subset): Stubs for rclcpp ([#2165](https://github.com/ros2/rclcpp/issues/2165))
- Add type\_hash to cpp TopicEndpointInfo ([#2137](https://github.com/ros2/rclcpp/issues/2137))
- Trigger the intraprocess guard condition with data ([#2164](https://github.com/ros2/rclcpp/issues/2164))
- Minor grammar fix ([#2149](https://github.com/ros2/rclcpp/issues/2149))
- Fix unnecessary allocations in executor.cpp ([#2135](https://github.com/ros2/rclcpp/issues/2135))
- add Logger::get\_effective\_level(). ([#2141](https://github.com/ros2/rclcpp/issues/2141))
- Remove deprecated header ([#2139](https://github.com/ros2/rclcpp/issues/2139))
- Implement matched event ([#2105](https://github.com/ros2/rclcpp/issues/2105))
- use allocator via init\_options argument. ([#2129](https://github.com/ros2/rclcpp/issues/2129))
- Fixes to silence some clang warnings. ([#2127](https://github.com/ros2/rclcpp/issues/2127))
- Documentation improvements on the executor ([#2125](https://github.com/ros2/rclcpp/issues/2125))
- Avoid losing waitable handles while using MultiThreadedExecutor ([#2109](https://github.com/ros2/rclcpp/issues/2109))
- Hook up the incompatible type event inside of rclcpp ([#2069](https://github.com/ros2/rclcpp/issues/2069))
- Update all rclcpp packages to C++17. ([#2121](https://github.com/ros2/rclcpp/issues/2121))
- Fix clang warning: bugprone-use-after-move ([#2116](https://github.com/ros2/rclcpp/issues/2116))
- Fix memory leak in tracetools::get\_symbol() ([#2104](https://github.com/ros2/rclcpp/issues/2104))
- Service introspection ([#1985](https://github.com/ros2/rclcpp/issues/1985))
- Allow publishing borrowed messages with intra-process enabled ([#2108](https://github.com/ros2/rclcpp/issues/2108))
- to fix flaky test about TestTimeSource.callbacks ([#2111](https://github.com/ros2/rclcpp/issues/2111))
- to create a sublogger while getting child of Logger ([#1717](https://github.com/ros2/rclcpp/issues/1717))
- Fix documentation of Context class ([#2107](https://github.com/ros2/rclcpp/issues/2107))
- fixes for rmw callbacks in qos\_event class ([#2102](https://github.com/ros2/rclcpp/issues/2102))
- Add support for timers on reset callback ([#1979](https://github.com/ros2/rclcpp/issues/1979))
- Topic node guard condition in executor ([#2074](https://github.com/ros2/rclcpp/issues/2074))
- Fix bug on the disorder of calling shutdown callback ([#2097](https://github.com/ros2/rclcpp/issues/2097))
- Add default constructor to NodeInterfaces ([#2094](https://github.com/ros2/rclcpp/issues/2094))
- Fix clock state cached time to be a copy, not a reference. ([#2092](https://github.com/ros2/rclcpp/issues/2092))
- Fix -Wmaybe-uninitialized warning ([#2081](https://github.com/ros2/rclcpp/issues/2081))
- Fix the keep\_last warning when using system defaults. ([#2082](https://github.com/ros2/rclcpp/issues/2082))
- Add in a fix for older compilers. ([#2075](https://github.com/ros2/rclcpp/issues/2075))
- Implement Unified Node Interface (NodeInterfaces class) ([#2041](https://github.com/ros2/rclcpp/issues/2041))
- Do not throw exception if trying to dequeue an empty intra-process buffer ([#2061](https://github.com/ros2/rclcpp/issues/2061))
- Move event callback binding to PublisherBase and SubscriptionBase ([#2066](https://github.com/ros2/rclcpp/issues/2066))
- Implement validity checks for rclcpp::Clock ([#2040](https://github.com/ros2/rclcpp/issues/2040))
- Explicitly set callback type ([#2059](https://github.com/ros2/rclcpp/issues/2059))
- Fix logging macros to build with msvc and cpp20 ([#2063](https://github.com/ros2/rclcpp/issues/2063))
- Add clock type to node\_options ([#1982](https://github.com/ros2/rclcpp/issues/1982))
- Fix nullptr dereference in prune\_requests\_older\_than ([#2008](https://github.com/ros2/rclcpp/issues/2008))
- Remove templating on to\_rcl\_subscription\_options ([#2056](https://github.com/ros2/rclcpp/issues/2056))
- Fix SharedFuture from async\_send\_request never becoming valid ([#2044](https://github.com/ros2/rclcpp/issues/2044))
- Add in a warning for a KeepLast depth of 0. ([#2048](https://github.com/ros2/rclcpp/issues/2048))
- Mark rclcpp::Clock::now() as const ([#2050](https://github.com/ros2/rclcpp/issues/2050))
- Fix a case that did not throw ParameterUninitializedException ([#2036](https://github.com/ros2/rclcpp/issues/2036))
- Update maintainers ([#2043](https://github.com/ros2/rclcpp/issues/2043))
- MultiThreadExecutor number of threads is at least 2+ in default. ([#2032](https://github.com/ros2/rclcpp/issues/2032))
- Fix bug that a callback not reached ([#1640](https://github.com/ros2/rclcpp/issues/1640))
- Set the minimum number of threads of the Multithreaded executor to 2 ([#2030](https://github.com/ros2/rclcpp/issues/2030))
- check thread whether joinable before join ([#2019](https://github.com/ros2/rclcpp/issues/2019))
- Set cpplint test timeout to 3 minutes ([#2022](https://github.com/ros2/rclcpp/issues/2022))
- Make sure to include-what-you-use in the node\_interfaces. ([#2018](https://github.com/ros2/rclcpp/issues/2018))
- Do not clear entities callbacks on destruction ([#2002](https://github.com/ros2/rclcpp/issues/2002))
- fix mismatched issue if using zero\_allocate ([#1995](https://github.com/ros2/rclcpp/issues/1995))
- Make ParameterService and Sync/AsyncParameterClient accept rclcpp::QoS ([#1978](https://github.com/ros2/rclcpp/issues/1978))
- support regex match for parameter client ([#1992](https://github.com/ros2/rclcpp/issues/1992))
- operator+= and operator-= for Duration ([#1988](https://github.com/ros2/rclcpp/issues/1988))
- Revert “Revert “Add a create\_timer method to Node and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))” ([#2009](https://github.com/ros2/rclcpp/issues/2009)) ([#2010](https://github.com/ros2/rclcpp/issues/2010))
- force compiler warning if callback handles not captured ([#2000](https://github.com/ros2/rclcpp/issues/2000))
- Revert “Add a `create_timer` method to `Node` and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))” ([#2009](https://github.com/ros2/rclcpp/issues/2009))
- Add a `create_timer` method to `Node` and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))
- [docs] add note about callback lifetime for {on, post}\_set\_parameter\_callback ([#1981](https://github.com/ros2/rclcpp/issues/1981))
- fix memory leak ([#1994](https://github.com/ros2/rclcpp/issues/1994))
- Support pre-set and post-set parameter callbacks in addition to on-set-parameter-callback. ([#1947](https://github.com/ros2/rclcpp/issues/1947))
- Make create\_service accept rclcpp::QoS ([#1969](https://github.com/ros2/rclcpp/issues/1969))
- Make create\_client accept rclcpp::QoS ([#1964](https://github.com/ros2/rclcpp/issues/1964))
- Fix the documentation for rclcpp::ok to be accurate. ([#1965](https://github.com/ros2/rclcpp/issues/1965))
- use regex for wildcard matching ([#1839](https://github.com/ros2/rclcpp/issues/1839))
- Revert “Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))” ([#1956](https://github.com/ros2/rclcpp/issues/1956))
- Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))
- test adjustment for LoanedMessage. ([#1951](https://github.com/ros2/rclcpp/issues/1951))
- fix virtual dispatch issues identified by clang-tidy ([#1816](https://github.com/ros2/rclcpp/issues/1816))
- Remove unused on\_parameters\_set\_callback\_ ([#1945](https://github.com/ros2/rclcpp/issues/1945))
- Fix subscription.is\_serialized() for callbacks with message info ([#1950](https://github.com/ros2/rclcpp/issues/1950))
- wait for subscriptions on another thread. ([#1940](https://github.com/ros2/rclcpp/issues/1940))
- Fix documentation of `RCLCPP\_[INFO,WARN,...]` ([#1943](https://github.com/ros2/rclcpp/issues/1943))
- Always trigger guard condition waitset ([#1923](https://github.com/ros2/rclcpp/issues/1923))
- Add statistics for handle\_loaned\_message ([#1927](https://github.com/ros2/rclcpp/issues/1927))
- Drop wrong template specialization ([#1926](https://github.com/ros2/rclcpp/issues/1926))
- Update get\_parameter\_from\_event to follow the function description ([#1922](https://github.com/ros2/rclcpp/issues/1922))
- Add ‘best available’ QoS enum values and methods ([#1920](https://github.com/ros2/rclcpp/issues/1920))
- use reinterpret\_cast for function pointer conversion. ([#1919](https://github.com/ros2/rclcpp/issues/1919))
- Contributors: Alberto Soragna, Alexander Hans, Alexis Paques, Andrew Symington, Audrow Nash, Barry Xu, Brian, Chen Lihui, Chris Lalancette, Christophe Bedard, Christopher Wecht, Cristóbal Arroyo, Daniel Reuter, Deepanshu Bansal, Emerson Knapp, Hubert Liberacki, Ivan Santiago Paunovic, Jacob Perron, Jeffery Hsu, Jochen Sprickerhof, Lei Liu, Mateusz Szczygielski, Michael Carroll, Miguel Company, Nikolai Morin, Shane Loretz, Silvio Traversaro, Tomoya Fujita, Tyler Weaver, William Woodall, Yadu, andrei, mauropasse, mergify[bot], methylDragon, schrodinbug, uupks, ymski

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/iron/rclcpp_action/CHANGELOG.rst)

- extract the result response before the callback is issued. ([#2132](https://github.com/ros2/rclcpp/issues/2132))
- Update all rclcpp packages to C++17. ([#2121](https://github.com/ros2/rclcpp/issues/2121))
- Fix the GoalUUID to\_string representation ([#1999](https://github.com/ros2/rclcpp/issues/1999))
- Explicitly set callback type ([#2059](https://github.com/ros2/rclcpp/issues/2059))
- Update maintainers ([#2043](https://github.com/ros2/rclcpp/issues/2043))
- Do not clear entities callbacks on destruction ([#2002](https://github.com/ros2/rclcpp/issues/2002))
- Revert “Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))” ([#1956](https://github.com/ros2/rclcpp/issues/1956))
- Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))
- Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki, Nathan Wiebe Neufeldt, Tomoya Fujita, William Woodall, mauropasse

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/iron/rclcpp_components/CHANGELOG.rst)

- Update all rclcpp packages to C++17. ([#2121](https://github.com/ros2/rclcpp/issues/2121))
- Improve component\_manager\_isolated shutdown ([#2085](https://github.com/ros2/rclcpp/issues/2085))
- Update maintainers ([#2043](https://github.com/ros2/rclcpp/issues/2043))
- use unique ptr and remove unuseful container ([#2013](https://github.com/ros2/rclcpp/issues/2013))
- Revert “Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))” ([#1956](https://github.com/ros2/rclcpp/issues/1956))
- Introduce executors new spin\_for method, replace spin\_until\_future\_complete with spin\_until\_complete. ([#1821](https://github.com/ros2/rclcpp/issues/1821)) ([#1874](https://github.com/ros2/rclcpp/issues/1874))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Hubert Liberacki, Michael Carroll, William Woodall

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/iron/rclcpp_lifecycle/CHANGELOG.rst)

- Add support for logging service. ([#2122](https://github.com/ros2/rclcpp/issues/2122))
- Support publishing loaned messages in LifecyclePublisher ([#2159](https://github.com/ros2/rclcpp/issues/2159))
- Fixes to silence some clang warnings. ([#2127](https://github.com/ros2/rclcpp/issues/2127))
- Update all rclcpp packages to C++17. ([#2121](https://github.com/ros2/rclcpp/issues/2121))
- Use the correct macro for LifecycleNode::get\_fully\_qualified\_name ([#2117](https://github.com/ros2/rclcpp/issues/2117))
- add get\_fully\_qualified\_name to rclcpp\_lifecycle ([#2115](https://github.com/ros2/rclcpp/issues/2115))
- Implement Unified Node Interface (NodeInterfaces class) ([#2041](https://github.com/ros2/rclcpp/issues/2041))
- Add clock type to node\_options ([#1982](https://github.com/ros2/rclcpp/issues/1982))
- Update maintainers ([#2043](https://github.com/ros2/rclcpp/issues/2043))
- LifecycleNode on\_configure doc fix. ([#2034](https://github.com/ros2/rclcpp/issues/2034))
- Bugfix 20210810 get current state ([#1756](https://github.com/ros2/rclcpp/issues/1756))
- Make lifecycle impl get\_current\_state() const. ([#2031](https://github.com/ros2/rclcpp/issues/2031))
- Cleanup the lifecycle implementation ([#2027](https://github.com/ros2/rclcpp/issues/2027))
- Cleanup the rclcpp\_lifecycle dependencies. ([#2021](https://github.com/ros2/rclcpp/issues/2021))
- Revert “Revert “Add a create\_timer method to Node and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))” ([#2009](https://github.com/ros2/rclcpp/issues/2009)) ([#2010](https://github.com/ros2/rclcpp/issues/2010))
- Revert “Add a `create_timer` method to `Node` and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))” ([#2009](https://github.com/ros2/rclcpp/issues/2009))
- Add a `create_timer` method to `Node` and `LifecycleNode` classes ([#1975](https://github.com/ros2/rclcpp/issues/1975))
- Support pre-set and post-set parameter callbacks in addition to on-set-parameter-callback. ([#1947](https://github.com/ros2/rclcpp/issues/1947))
- Make create\_service accept rclcpp::QoS ([#1969](https://github.com/ros2/rclcpp/issues/1969))
- Make create\_client accept rclcpp::QoS ([#1964](https://github.com/ros2/rclcpp/issues/1964))
- Contributors: Andrew Symington, Audrow Nash, Chris Lalancette, Deepanshu Bansal, Ivan Santiago Paunovic, Jeffery Hsu, Lei Liu, Michael Babenko, Shane Loretz, Steve Macenski, Tomoya Fujita, methylDragon

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/iron/rclpy/CHANGELOG.rst)

- Fix type in Node init args ([#1115](https://github.com/ros2/rclpy/issues/1115)) ([#1122](https://github.com/ros2/rclpy/issues/1122))
- Logging service support ([#1102](https://github.com/ros2/rclpy/issues/1102))
- Use custom sourcedir for conf.py ([#1109](https://github.com/ros2/rclpy/issues/1109))
- ServerGoalHandle should be destroyed before removing. ([#1113](https://github.com/ros2/rclpy/issues/1113))
- Fix unnecessary list comprehension flake8 ([#1112](https://github.com/ros2/rclpy/issues/1112))
- Stub type hash value line in TopicEndpointInfo string ([#1110](https://github.com/ros2/rclpy/issues/1110))
- Support documentation generation using rosdoc2 ([#1103](https://github.com/ros2/rclpy/issues/1103))
- Fix Time and Duration raising exception when compared to another type ([#1007](https://github.com/ros2/rclpy/issues/1007))
- Make rcl\_interfaces a build and exec dependency. ([#1100](https://github.com/ros2/rclpy/issues/1100))
- Solving Atomic undefined on OSX with clang ([#1096](https://github.com/ros2/rclpy/issues/1096))
- Implement matched event ([#1083](https://github.com/ros2/rclpy/issues/1083))
- Update service.py documentation ([#1094](https://github.com/ros2/rclpy/issues/1094))
- Allow space or empty strings when using ros2 param set ([#1093](https://github.com/ros2/rclpy/issues/1093))
- Hook up the incompatible type event inside of rclpy ([#1058](https://github.com/ros2/rclpy/issues/1058))
- Switch to using module instead of module\_ ([#1090](https://github.com/ros2/rclpy/issues/1090))
- Add in subscription.get\_publisher\_count() ([#1089](https://github.com/ros2/rclpy/issues/1089))
- Service introspection ([#988](https://github.com/ros2/rclpy/issues/988))
- to create a sublogger while getting child of Logger ([#1084](https://github.com/ros2/rclpy/issues/1084))
- Fix [#983](https://github.com/ros2/rclpy/issues/983) by saving future and checking for + raising any exceptions ([#1073](https://github.com/ros2/rclpy/issues/1073))
- Force C++17 support on. ([#1076](https://github.com/ros2/rclpy/issues/1076))
- Use RCPPUTILS\_SCOPE\_EXIT to cleanup unparsed\_indices\_c. ([#1075](https://github.com/ros2/rclpy/issues/1075))
- Explicitly link atomic when building with Clang ([#1065](https://github.com/ros2/rclpy/issues/1065))
- Fix test\_publisher linter for pydocstyle 6.2.2 ([#1063](https://github.com/ros2/rclpy/issues/1063))
- Add default preset qos profile ([#1062](https://github.com/ros2/rclpy/issues/1062))
- Add on\_parameter\_event method to the AsyncParameterClient. ([#1061](https://github.com/ros2/rclpy/issues/1061))
- Add documentation page for rclpy.clock ([#1055](https://github.com/ros2/rclpy/issues/1055))
- Rewrite test code without depending on parameter client ([#1045](https://github.com/ros2/rclpy/issues/1045))
- Add parallel callback test ([#1044](https://github.com/ros2/rclpy/issues/1044))
- decorator should not be callable. ([#1050](https://github.com/ros2/rclpy/issues/1050))
- typo fix. ([#1049](https://github.com/ros2/rclpy/issues/1049))
- Add in a warning for a depth of 0 with KEEP\_LAST. ([#1048](https://github.com/ros2/rclpy/issues/1048))
- Add feature of wait for message ([#953](https://github.com/ros2/rclpy/issues/953)). ([#960](https://github.com/ros2/rclpy/issues/960))
- Document rclpy.time.Time class ([#1040](https://github.com/ros2/rclpy/issues/1040))
- Deal with ParameterUninitializedException for parameter service ([#1033](https://github.com/ros2/rclpy/issues/1033))
- Improve documentation in rclpy.utilities ([#1038](https://github.com/ros2/rclpy/issues/1038))
- Document rclpy.utilities.remove\_ros\_args ([#1036](https://github.com/ros2/rclpy/issues/1036))
- Fix incorrect comparsion on whether parameter type is NOT\_SET ([#1032](https://github.com/ros2/rclpy/issues/1032))
- [rolling] Update maintainers ([#1035](https://github.com/ros2/rclpy/issues/1035))
- Set the default number of threads of the MultiThreadedExecutor to 2 ([#1031](https://github.com/ros2/rclpy/issues/1031))
- Update the rclpy method documentation. ([#1026](https://github.com/ros2/rclpy/issues/1026))
- Revert “Raise user handler exception in MultiThreadedExecutor. ([#984](https://github.com/ros2/rclpy/issues/984))” ([#1017](https://github.com/ros2/rclpy/issues/1017))
- Waitable should check callback\_group if it can be executed. ([#1001](https://github.com/ros2/rclpy/issues/1001))
- support wildcard matching for params file ([#987](https://github.com/ros2/rclpy/issues/987))
- Raise user handler exception in MultiThreadedExecutor. ([#984](https://github.com/ros2/rclpy/issues/984))
- Add wait\_for\_node method ([#930](https://github.com/ros2/rclpy/issues/930))
- Create sublogger for action server and action client ([#982](https://github.com/ros2/rclpy/issues/982))
- Support for pre-set and post-set parameter callback. ([#966](https://github.com/ros2/rclpy/issues/966))
- fix gcc 7.5 build errors ([#977](https://github.com/ros2/rclpy/issues/977))
- make \_on\_parameter\_event return result correctly ([#817](https://github.com/ros2/rclpy/issues/817))
- Fix a small typo in documentation. ([#967](https://github.com/ros2/rclpy/issues/967))
- Add Parameter Client ([#959](https://github.com/ros2/rclpy/issues/959))
- Change sphinx theme to readthedocs ([#950](https://github.com/ros2/rclpy/issues/950))
- Name and type in descriptor(s) is ignored via declare\_parameter(s). ([#957](https://github.com/ros2/rclpy/issues/957))
- Typo fix ([#951](https://github.com/ros2/rclpy/issues/951))
- Add py.typed to package ([#946](https://github.com/ros2/rclpy/issues/946))
- Fix rclpy.shutdown() from hanging when triggered from callback ([#947](https://github.com/ros2/rclpy/pull/947))
- Check if the context is already shutdown. ([#939](https://github.com/ros2/rclpy/issues/939))
- Avoid causing infinite loop when message is empty ([#935](https://github.com/ros2/rclpy/issues/935))
- Expose ‘best available’ QoS policies ([#928](https://github.com/ros2/rclpy/issues/928))
- remove feedback callback when the goal has been completed. ([#927](https://github.com/ros2/rclpy/issues/927))
- Allow to create a subscription with a callback that also receives the message info ([#922](https://github.com/ros2/rclpy/issues/922))
- Contributors: Achille Verheye, Audrow Nash, Barry Xu, Brian, Brian Chen, Chen Lihui, Chris Lalancette, Cristóbal Arroyo, Deepanshu Bansal, Emerson Knapp, Erki Suurjaak, Felix Divo, Florian Vahl, Gonzo, GuiHome, Ivan Santiago Paunovic, Jacob Perron, Lei Liu, Lucas Wendland, Michael Carroll, Sebastian Freitag, Seulbae Kim, Shane Loretz, Steve Nogar, Takeshi Ishita, Tomoya Fujita, Tony Najjar, Yadu, Yuki Igarashi, mergify[bot]

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/iron/CHANGELOG.rst)

- Add missing header for strlen ([#169](https://github.com/ros2/rcpputils/issues/169))
- issue-167 ([#172](https://github.com/ros2/rcpputils/issues/172))
- [rolling] Update maintainers - 2022-11-07 ([#166](https://github.com/ros2/rcpputils/issues/166))
- require C++17 and deprecate the rcppmath namespace ([#165](https://github.com/ros2/rcpputils/issues/165))
- Mirror rolling to master
- Fix possible race condition in create\_directories() ([#162](https://github.com/ros2/rcpputils/issues/162))
- Contributors: Artem Shumov, Audrow Nash, Sebastian Freitag, William Woodall, bijoua29

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/iron/CHANGELOG.rst)

- fix memory leak ([#423](https://github.com/ros2/rcutils/issues/423))
- Add convenience error handling macros ([#421](https://github.com/ros2/rcutils/issues/421))
- Calculate the next power-of-two for the user in hash\_map\_init. ([#420](https://github.com/ros2/rcutils/issues/420))
- update cast to modern style ([#418](https://github.com/ros2/rcutils/issues/418))
- Remove deprecated header get\_env.h ([#417](https://github.com/ros2/rcutils/issues/417))
- Updates to rcutils to make rosdoc2 generation happier. ([#416](https://github.com/ros2/rcutils/issues/416))
- add RCUTILS\_LOGGING\_AUTOINIT\_WITH\_ALLOCATOR. ([#415](https://github.com/ros2/rcutils/issues/415))
- Fix memory leak in string\_map.c in rcutils ([#411](https://github.com/ros2/rcutils/issues/411))
- avoid unnecessary copy for rcutils\_char\_array\_vsprintf. ([#412](https://github.com/ros2/rcutils/issues/412))
- Add missing stddef include for size\_t ([#410](https://github.com/ros2/rcutils/issues/410))
- Add SHA256 utility implementation ([#408](https://github.com/ros2/rcutils/issues/408))
- Upgrade rcutils to C++17. ([#392](https://github.com/ros2/rcutils/issues/392))
- [rolling] Update maintainers - 2022-11-07 ([#404](https://github.com/ros2/rcutils/issues/404))
- Fix build on OpenHarmony ([#395](https://github.com/ros2/rcutils/issues/395))
- regression of thread-safety for logging macros ([#393](https://github.com/ros2/rcutils/issues/393))
- add portable nonnull macros ([#382](https://github.com/ros2/rcutils/issues/382))
- Fix memory leak when adding the same key to the logger hash map multiple times ([#391](https://github.com/ros2/rcutils/issues/391))
- time\_unix: uses ZEPHYR\_VERSION\_CODE instead ([#390](https://github.com/ros2/rcutils/issues/390))
- Cleanup time\_unix.c ([#389](https://github.com/ros2/rcutils/issues/389))
- time\_unix: namespace zephyr headers ([#383](https://github.com/ros2/rcutils/issues/383))
- Restrict overmatching MACH ifdef to only trigger on OSX and Mach ([#386](https://github.com/ros2/rcutils/issues/386))
- Optimize rcutils\_logging\_get\_logger\_effective\_level() ([#381](https://github.com/ros2/rcutils/issues/381))
- Change syntax \_\_VAR\_ARGS\_\_ to \_\_VA\_ARGS\_\_ ([#376](https://github.com/ros2/rcutils/issues/376))
- Fix a bug in hash\_map\_get\_next\_key\_and\_data. ([#375](https://github.com/ros2/rcutils/issues/375))
- More fixes from review.
- Fixes from review.
- Make g\_rcutils\_logging\_output\_handler static.
- Make g\_rcutils\_logging\_default\_logger\_level static.
- Optimize rcutils\_find\_lastn where possible.
- Don’t bother computing the hash\_map key if the hash map is empty.
- Make sure to expand char\_array by at least 1.5x.
- Optimize index computation in hash\_map\_find.
- Improve the performance of rcutils\_logging\_format\_message. ([#372](https://github.com/ros2/rcutils/issues/372))
- Get rid of unnecessary ret variable.
- Get rid of unnecessary ifdef cplusplus checks in the C file.
- Get rid of unnecessary rcutils\_custom\_add\_{gtest,gmock}
- Get rid of unnecessary and unused RMW switching for logging tests.
- Remove unnecessary IS\_OUTPUT\_COLORIZED macro.
- Rename logging internal structures to use our new convention.
- Make all of the logging ‘expand’ methods static.
- Fix up error checking for RCUTILS\_CONSOLE\_STDOUT\_LINE\_BUFFERED.
- Cleanup error handling for the RCUTILS\_CONSOLE\_OUTPUT\_FORMAT checks.
- Revamp error handling in rcutils\_logging\_initialize\_with\_allocator.
- Revamp rcutils\_logging\_initialize\_with\_allocator.
- Make a few logging global variables static.
- Optimize calls via the RCUTILS\_LOG macros. ([#369](https://github.com/ros2/rcutils/issues/369))
- time\_unix: add zephyr posix time ([#368](https://github.com/ros2/rcutils/issues/368))
- Optimize the implementation of rcutils\_char\_array\_strncpy. ([#367](https://github.com/ros2/rcutils/issues/367))
- strdup.c: fix arbitrary length overread ([#366](https://github.com/ros2/rcutils/issues/366))
- Mirror rolling to master
- strdup.c: fix 1 byte buffer overread ([#363](https://github.com/ros2/rcutils/issues/363))
- Clarify duration arg description in logging macros ([#359](https://github.com/ros2/rcutils/issues/359))
- Update rcutils\_steady\_time\_now to return the same data as std::chrono ([#357](https://github.com/ros2/rcutils/issues/357))
- Contributors: AIxWall, Abrar Rahman Protyasha, Audrow Nash, Chen Lihui, Chris Lalancette, Emerson Knapp, Felipe Neves, Jacob Perron, Mario Prats, Maximilian Downey Twiss, Nikolai Morin, Tomoya Fujita, William Woodall, Yakumoo, guijan, methylDragon

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/iron/rmw/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw ([#353](https://github.com/ros2/rmw/issues/353))
- Runtime Interface Reflection: rmw ([#340](https://github.com/ros2/rmw/issues/340))
- [rmw] Improve handling of dynamic discovery ([#338](https://github.com/ros2/rmw/issues/338))
- rmw\_send\_reqponse returns RMW\_RET\_TIMEOUT. ([#350](https://github.com/ros2/rmw/issues/350))
- Add a note about asynchronicity of discovery. ([#352](https://github.com/ros2/rmw/issues/352))
- Add matched event support ([#331](https://github.com/ros2/rmw/issues/331))
- Add type hash to rmw\_topic\_endpoint\_info\_t (rep2011) ([#348](https://github.com/ros2/rmw/issues/348))
- Add in inconsistent topic defines and data structures. ([#339](https://github.com/ros2/rmw/issues/339))
- Update documented expectations for GIDs ([#335](https://github.com/ros2/rmw/issues/335))
- Fix rmw->rwm typo ([#347](https://github.com/ros2/rmw/issues/347))
- Add rmw count clients, services ([#334](https://github.com/ros2/rmw/issues/334))
- make writer\_guid uint8\_t[] instead of int8\_t for consistency with rmw\_gid\_t ([#329](https://github.com/ros2/rmw/issues/329))
- Update rmw to C++17. ([#346](https://github.com/ros2/rmw/issues/346))
- Reduce GID storage to 16 bytes. ([#345](https://github.com/ros2/rmw/issues/345))
- Move the RMW\_CHECK\_TYPE\_IDENTIFIERS\_MATCH macro to a C header. ([#343](https://github.com/ros2/rmw/issues/343))
- [rolling] Update maintainers - 2022-11-07 ([#337](https://github.com/ros2/rmw/issues/337))
- Remove unused test\_loaned\_message\_sequence.cpp ([#336](https://github.com/ros2/rmw/issues/336))
- callback can be NULL to clear in Listener APIs. ([#332](https://github.com/ros2/rmw/issues/332))
- Add rmw\_get\_gid\_for\_client method ([#327](https://github.com/ros2/rmw/issues/327))
- Add ‘best available’ QoS policies ([#320](https://github.com/ros2/rmw/issues/320)) The best available policy should select the highest level of service for the QoS setting while matching with the majority of endpoints. For example, in the case of a DDS middleware subscription, this means: \* Prefer reliable reliability if all existing publishers on the same topic are reliable, otherwise use best effort. \* Prefer transient local durability if all existing publishers on the same topic are transient local, otherwise use volatile. \* Prefer manual by topic liveliness if all existing publishers on the same topic are manual by topic, otherwise use automatic. \* Use a deadline that is equal to the largest deadline of existing publishers on the same topic. \* Use a liveliness lease duration that is equal to the largest lease duration of existing publishers on the same topic.
- Move statuses definitions to rmw/events\_statuses/ ([#232](https://github.com/ros2/rmw/issues/232))
- Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Jacob Perron, Lee, Minju, Nikolai Morin, Tomoya Fujita, William Woodall, methylDragon

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/iron/rmw_connextdds/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_connextdds ([#115](https://github.com/ros2/rmw_connextdds/issues/115))
- Revert “Refactor serialization support to use allocators and refs”
- Refactor serialization support to use allocators and refs
- Add stubs for new rmw interfaces ([#111](https://github.com/ros2/rmw_connextdds/issues/111))
- Add rmw\_get\_gid\_for\_client impl ([#92](https://github.com/ros2/rmw_connextdds/issues/92))
- Switch ROS2 -> ROS 2 everywhere ([#83](https://github.com/ros2/rmw_connextdds/issues/83))
- Contributors: Brian, Chris Lalancette, methylDragon

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/iron/rmw_connextdds_common/CHANGELOG.rst)

- [rmw\_connextdds] New RMW discovery options ([#108](https://github.com/ros2/rmw_connextdds/issues/108))
- Call get\_type\_hash\_func ([#113](https://github.com/ros2/rmw_connextdds/issues/113))
- Type hash distribution during discovery (rep2011) ([#104](https://github.com/ros2/rmw_connextdds/issues/104))
- Implement matched event ([#101](https://github.com/ros2/rmw_connextdds/issues/101))
- Add in implementation of inconsistent topic. ([#103](https://github.com/ros2/rmw_connextdds/issues/103))
- Add rmw\_get\_gid\_for\_client impl ([#92](https://github.com/ros2/rmw_connextdds/issues/92))
- Fix assert statement to allow the seconds field of a DDS\_Duration\_t to be zero ([#88](https://github.com/ros2/rmw_connextdds/issues/88))
- Handle ‘best\_available’ QoS policies in common ([#85](https://github.com/ros2/rmw_connextdds/issues/85))
- Resolve build error with RTI Connext DDS 5.3.1 ([#82](https://github.com/ros2/rmw_connextdds/issues/82))
- Contributors: Andrea Sorbini, Barry Xu, Brian, Chris Lalancette, Emerson Knapp, Grey, Jose Luis Rivero, Michael Carroll, Michael Jeronimo

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/iron/rmw_connextddsmicro/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_connextdds ([#115](https://github.com/ros2/rmw_connextdds/issues/115))
- Add stubs for new rmw interfaces ([#111](https://github.com/ros2/rmw_connextdds/issues/111))
- Add rmw\_get\_gid\_for\_client impl ([#92](https://github.com/ros2/rmw_connextdds/issues/92))
- Switch ROS2 -> ROS 2 everywhere ([#83](https://github.com/ros2/rmw_connextdds/issues/83))
- Contributors: Brian, Chris Lalancette, methylDragon

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/iron/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_cyclonedds ([#451](https://github.com/ros2/rmw_cyclonedds/issues/451))
- Add stubs for new rmw interfaces ([#447](https://github.com/ros2/rmw_cyclonedds/issues/447))
- [rmw\_cyclonedds] Improve handling of dynamic discovery ([#429](https://github.com/ros2/rmw_cyclonedds/issues/429))
- Call get\_type\_hash\_func ([#448](https://github.com/ros2/rmw_cyclonedds/issues/448))
- Type hash distribution in discovery (rep2011) ([#437](https://github.com/ros2/rmw_cyclonedds/issues/437))
- Disable inconsistent topic events. ([#444](https://github.com/ros2/rmw_cyclonedds/issues/444))
- Implement matched event ([#435](https://github.com/ros2/rmw_cyclonedds/issues/435))
- Implement inconsistent topic. ([#431](https://github.com/ros2/rmw_cyclonedds/issues/431))
- Make sure to add semicolons to the CHECK\_TYPE\_IDENTIFIER\_MATCH. ([#432](https://github.com/ros2/rmw_cyclonedds/issues/432))
- [rolling] Update maintainers - 2022-11-07 ([#428](https://github.com/ros2/rmw_cyclonedds/issues/428))
- Export CycloneDDS dependency ([#424](https://github.com/ros2/rmw_cyclonedds/issues/424))
- add NULL check before accessing object. ([#423](https://github.com/ros2/rmw_cyclonedds/issues/423))
- Add rmw\_get\_gid\_for\_client impl ([#402](https://github.com/ros2/rmw_cyclonedds/issues/402))
- Makes topic\_name a const ref
- Adds topic name to error msg when create\_topic fails
- Improve error message when create\_topic fails ([#405](https://github.com/ros2/rmw_cyclonedds/issues/405))
- Change wrong use of %d to print uint32\_t to PRIu32 ([#253](https://github.com/ros2/rmw_cyclonedds/issues/253))
- Add cstring include. ([#393](https://github.com/ros2/rmw_cyclonedds/issues/393))
- Handle ‘best\_available’ QoS policies ([#389](https://github.com/ros2/rmw_cyclonedds/issues/389))
- Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Jose Luis Rivero, Shane Loretz, Tomoya Fujita, Tully Foote, Voldivh, eboasson, methylDragon

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/iron/rmw_dds_common/CHANGELOG.rst)

- Type hash in GraphCache, user\_data encoding tools ([#70](https://github.com/ros2/rmw_dds_common/issues/70))
- Mark benchmark \_ as unused. ([#71](https://github.com/ros2/rmw_dds_common/issues/71))
- Update rmw\_dds\_common to C++17. ([#69](https://github.com/ros2/rmw_dds_common/issues/69))
- Change Gid.msg to be 16 bytes. ([#68](https://github.com/ros2/rmw_dds_common/issues/68))
- Minor cleanups of test\_qos. ([#67](https://github.com/ros2/rmw_dds_common/issues/67))
- [rolling] Update maintainers - 2022-11-07 ([#65](https://github.com/ros2/rmw_dds_common/issues/65))
- build shared lib only if BUILD\_SHARED\_LIBS is set ([#62](https://github.com/ros2/rmw_dds_common/issues/62))
- Update maintainers ([#61](https://github.com/ros2/rmw_dds_common/issues/61))
- Add functions for resolving ‘best available’ QoS policies ([#60](https://github.com/ros2/rmw_dds_common/issues/60)) Given a QoS profile and set of endpoints for the same topic, overwrite any policies set to BEST\_AVAILABLE with a policy such that it matches all endpoints while maintaining a high level of service. Add testable functions for updating BEST\_AVAILABLE policies, \* qos\_profile\_get\_best\_available\_for\_subscription \* qos\_profile\_get\_best\_available\_for\_publisher and add convenience functions that actual query the graph for RMW implementations to use, \* qos\_profile\_get\_best\_available\_for\_topic\_subscription \* qos\_profile\_get\_best\_available\_for\_topic\_publisher
- Contributors: Audrow Nash, Chris Lalancette, Emerson Knapp, Jacob Perron, hannes09, methylDragon

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/iron/rmw_fastrtps_cpp/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_fastrtps ([#687](https://github.com/ros2/rmw_fastrtps/issues/687))
- Runtime Interface Reflection: rmw\_fastrtps ([#655](https://github.com/ros2/rmw_fastrtps/issues/655))
- [rmw\_fastrtps] Improve handling of dynamic discovery ([#653](https://github.com/ros2/rmw_fastrtps/issues/653))
- Call get\_type\_hash\_func ([#680](https://github.com/ros2/rmw_fastrtps/issues/680))
- Type hash distribution in discovery (rep2011) ([#671](https://github.com/ros2/rmw_fastrtps/issues/671))
- Implement inconsistent topic event ([#654](https://github.com/ros2/rmw_fastrtps/issues/654))
- Update all rmw\_fastrtps packages to C++17. ([#674](https://github.com/ros2/rmw_fastrtps/issues/674))
- Rewrite how Topics are tracked in rmw\_fastrtps\_cpp. ([#669](https://github.com/ros2/rmw_fastrtps/issues/669))
- Allow loaned messages without data-sharing ([#568](https://github.com/ros2/rmw_fastrtps/issues/568))
- Fix incoherent dissociate\_writer to dissociate\_reader ([#647](https://github.com/ros2/rmw_fastrtps/issues/647)) ([#649](https://github.com/ros2/rmw_fastrtps/issues/649))
- [rolling] Update maintainers - 2022-11-07 ([#643](https://github.com/ros2/rmw_fastrtps/issues/643))
- Add rmw\_get\_gid\_for\_client impl ([#631](https://github.com/ros2/rmw_fastrtps/issues/631))
- Use Fast-DDS Waitsets instead of listeners ([#619](https://github.com/ros2/rmw_fastrtps/issues/619))
- Remove rosidl\_cmake dependency ([#629](https://github.com/ros2/rmw_fastrtps/issues/629))
- Revert “add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))” ([#612](https://github.com/ros2/rmw_fastrtps/issues/612))
- add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))
- Allow null arguments in the EventsExecutor parameters ([#602](https://github.com/ros2/rmw_fastrtps/issues/602))
- Add RMW\_CHECKS to rmw\_fastrtps\_cpp EventsExecutor implementation
- Handle ‘best\_available’ QoS policies ([#598](https://github.com/ros2/rmw_fastrtps/issues/598))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Jacob Perron, Jose Luis Rivero, Miguel Company, Oscarchoi, Ricardo González, Tomoya Fujita, methylDragon

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/iron/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_fastrtps ([#687](https://github.com/ros2/rmw_fastrtps/issues/687))
- Runtime Interface Reflection: rmw\_fastrtps ([#655](https://github.com/ros2/rmw_fastrtps/issues/655))
- [rmw\_fastrtps] Improve handling of dynamic discovery ([#653](https://github.com/ros2/rmw_fastrtps/issues/653))
- Call get\_type\_hash\_func ([#680](https://github.com/ros2/rmw_fastrtps/issues/680))
- Type hash distribution in discovery (rep2011) ([#671](https://github.com/ros2/rmw_fastrtps/issues/671))
- Implement inconsistent topic event ([#654](https://github.com/ros2/rmw_fastrtps/issues/654))
- Update all rmw\_fastrtps packages to C++17. ([#674](https://github.com/ros2/rmw_fastrtps/issues/674))
- Rewrite how Topics are tracked in rmw\_fastrtps\_cpp. ([#669](https://github.com/ros2/rmw_fastrtps/issues/669))
- Allow loaned messages without data-sharing ([#568](https://github.com/ros2/rmw_fastrtps/issues/568))
- Fix incoherent dissociate\_writer to dissociate\_reader ([#647](https://github.com/ros2/rmw_fastrtps/issues/647)) ([#649](https://github.com/ros2/rmw_fastrtps/issues/649))
- [rolling] Update maintainers - 2022-11-07 ([#643](https://github.com/ros2/rmw_fastrtps/issues/643))
- Add rmw\_get\_gid\_for\_client impl ([#631](https://github.com/ros2/rmw_fastrtps/issues/631))
- Use Fast-DDS Waitsets instead of listeners ([#619](https://github.com/ros2/rmw_fastrtps/issues/619))
- Revert “add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))” ([#612](https://github.com/ros2/rmw_fastrtps/issues/612))
- add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))
- Allow null arguments in the EventsExecutor parameters ([#602](https://github.com/ros2/rmw_fastrtps/issues/602))
- Add EventExecutor to rmw\_fastrtps\_dynamic\_cpp
- Fix cpplint error ([#601](https://github.com/ros2/rmw_fastrtps/issues/601))
- Handle ‘best\_available’ QoS policies ([#598](https://github.com/ros2/rmw_fastrtps/issues/598))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Jacob Perron, Jose Luis Rivero, Miguel Company, Oscarchoi, Ricardo González, Tomoya Fujita, methylDragon

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/iron/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Fix matched event issues ([#683](https://github.com/ros2/rmw_fastrtps/issues/683))
- Dynamic Subscription (BONUS: Allocators): rmw\_fastrtps ([#687](https://github.com/ros2/rmw_fastrtps/issues/687))
- Check for triggered guard conditions before waiting ([#685](https://github.com/ros2/rmw_fastrtps/issues/685))
- Runtime Interface Reflection: rmw\_fastrtps ([#655](https://github.com/ros2/rmw_fastrtps/issues/655))
- [rmw\_fastrtps] Improve handling of dynamic discovery ([#653](https://github.com/ros2/rmw_fastrtps/issues/653))
- Type hash distribution in discovery (rep2011) ([#671](https://github.com/ros2/rmw_fastrtps/issues/671))
- Implement matched event ([#645](https://github.com/ros2/rmw_fastrtps/issues/645))
- Implement inconsistent topic event ([#654](https://github.com/ros2/rmw_fastrtps/issues/654))
- Update all rmw\_fastrtps packages to C++17. ([#674](https://github.com/ros2/rmw_fastrtps/issues/674))
- Rewrite how Topics are tracked in rmw\_fastrtps\_cpp. ([#669](https://github.com/ros2/rmw_fastrtps/issues/669))
- Delay lock on message callback setters ([#657](https://github.com/ros2/rmw_fastrtps/issues/657))
- Make sure to add semicolons to the CHECK\_TYPE\_IDENTIFIER\_MATCH. ([#658](https://github.com/ros2/rmw_fastrtps/issues/658))
- Allow loaned messages without data-sharing ([#568](https://github.com/ros2/rmw_fastrtps/issues/568))
- Fix incoherent dissociate\_writer to dissociate\_reader ([#647](https://github.com/ros2/rmw_fastrtps/issues/647)) ([#649](https://github.com/ros2/rmw_fastrtps/issues/649))
- [rolling] Update maintainers - 2022-11-07 ([#643](https://github.com/ros2/rmw_fastrtps/issues/643))
- Remove duplicated code ([#637](https://github.com/ros2/rmw_fastrtps/issues/637))
- Call callbacks only if unread count > 0 ([#634](https://github.com/ros2/rmw_fastrtps/issues/634))
- Add rmw\_get\_gid\_for\_client impl ([#631](https://github.com/ros2/rmw_fastrtps/issues/631))
- Use Fast-DDS Waitsets instead of listeners ([#619](https://github.com/ros2/rmw_fastrtps/issues/619))
- Take all available samples on service/client on\_data\_available. ([#616](https://github.com/ros2/rmw_fastrtps/issues/616))
- Revert “add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))” ([#612](https://github.com/ros2/rmw_fastrtps/issues/612))
- add line feed for RCUTILS\_SAFE\_FWRITE\_TO\_STDERR ([#608](https://github.com/ros2/rmw_fastrtps/issues/608))
- Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Michael Carroll, Miguel Company, Oscarchoi, Ricardo González, Tomoya Fujita, mauropasse, methylDragon

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/iron/rmw_implementation/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rmw\_implementation ([#219](https://github.com/ros2/rmw_implementation/issues/219))
- Runtime Interface Reflection: rmw\_implementation ([#215](https://github.com/ros2/rmw_implementation/issues/215))
- Mark the benchmark \_ variables as unused. ([#218](https://github.com/ros2/rmw_implementation/issues/218))
- Update rmw\_implementation to C++17. ([#214](https://github.com/ros2/rmw_implementation/issues/214))
- [rolling] Update maintainers - 2022-11-07 ([#212](https://github.com/ros2/rmw_implementation/issues/212))
- Build-time RMW selection does not need ament\_index\_cpp ([#210](https://github.com/ros2/rmw_implementation/issues/210))
- Add rmw\_get\_gid\_for\_client & tests ([#206](https://github.com/ros2/rmw_implementation/issues/206))
- Contributors: Audrow Nash, Brian, Chris Lalancette, G.A. vd. Hoorn, methylDragon

<a id="rmw-implementation-cmake"></a>

## [rmw\_implementation\_cmake](https://github.com/ros2/rmw/tree/iron/rmw_implementation_cmake/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#337](https://github.com/ros2/rmw/issues/337))
- Contributors: Audrow Nash

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/iron/CHANGELOG.rst)

- Update robot\_state\_publisher to C++17. ([#204](https://github.com/ros/robot_state_publisher/issues/204))
- [rolling] Update maintainers - 2022-11-07 ([#203](https://github.com/ros/robot_state_publisher/issues/203))
- Mirror rolling to ros2
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/iron/ros2action/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/iron/ros2bag/CHANGELOG.rst)

- Cleanup the help text for ros2 bag record. ([#1329](https://github.com/ros2/rosbag2/issues/1329)) ([#1333](https://github.com/ros2/rosbag2/issues/1333))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#1260](https://github.com/ros2/rosbag2/issues/1260))
- CLI: Get storage-specific values from plugin ([#1209](https://github.com/ros2/rosbag2/issues/1209))
- Fix up some of the wording in the record help text. ([#1228](https://github.com/ros2/rosbag2/issues/1228))
- Add topic\_name option to info verb ([#1217](https://github.com/ros2/rosbag2/issues/1217))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- rosbag2\_py: parametrize tests across storage plugins ([#1203](https://github.com/ros2/rosbag2/issues/1203))
- Added option to change node name for the recorder from the Python API ([#1180](https://github.com/ros2/rosbag2/issues/1180))
- rosbag2\_cpp: test more than one storage plugin ([#1196](https://github.com/ros2/rosbag2/issues/1196))
- rosbag2\_storage: expose default storage ID as method ([#1146](https://github.com/ros2/rosbag2/issues/1146))
- Fix for ros2 bag play exit with non-zero code on SIGINT ([#1126](https://github.com/ros2/rosbag2/issues/1126))
- ros2bag: move storage preset validation to sqlite3 plugin ([#1135](https://github.com/ros2/rosbag2/issues/1135))
- Add option to prevent message loss while converting ([#1058](https://github.com/ros2/rosbag2/issues/1058))
- Added support for excluding topics via regular expressions ([#1046](https://github.com/ros2/rosbag2/issues/1046))
- Readers/info can accept a single bag storage file, and detect its storage id automatically ([#1072](https://github.com/ros2/rosbag2/issues/1072))
- Add short -v option to ros2 bag list for verbose ([#1065](https://github.com/ros2/rosbag2/issues/1065))
- Use a single variable for evaluating the filter regex ([#1053](https://github.com/ros2/rosbag2/issues/1053))
- Add additional mode of publishing sim time updates triggered by replayed messages ([#1050](https://github.com/ros2/rosbag2/issues/1050))
- Renamed –topics-regex to –regex and -e in Player class to be consistent with Recorder ([#1045](https://github.com/ros2/rosbag2/issues/1045))
- Use first available writer in recording if default `sqlite3` not available. ([#1044](https://github.com/ros2/rosbag2/issues/1044))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Added support for filtering topics via regular expressions on Playback ([#1034](https://github.com/ros2/rosbag2/issues/1034))
- Fix incorrect boundary check for `playback_duration` and `play_until_timestamp` ([#1032](https://github.com/ros2/rosbag2/issues/1032))
- Adds play until timestamp functionality ([#1005](https://github.com/ros2/rosbag2/issues/1005))
- Add CLI verb for burst mode of playback ([#980](https://github.com/ros2/rosbag2/issues/980))
- Add play-for specified number of seconds functionality ([#960](https://github.com/ros2/rosbag2/issues/960))
- Make unpublished topics unrecorded by default ([#968](https://github.com/ros2/rosbag2/issues/968))
- Contributors: Agustin Alba Chicar, Chris Lalancette, DensoADAS, Emerson Knapp, EsipovPA, Esteve Fernandez, Geoffrey Biggs, Hunter L.Allen, Keisuke Shima, Michael Orlov, Sean Kelly, Tony Peng, Yadu, james-rms, kylemarcey, mergify[bot], ricardo-manriquez

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/iron/ros2cli/CHANGELOG.rst)

- Set automatically\_declare\_parameters\_from\_overrides in DirectNode. ([#813](https://github.com/ros2/ros2cli/issues/813))
- Enable document generation using rosdoc2 ([#811](https://github.com/ros2/ros2cli/issues/811))
- Fix linters ([#808](https://github.com/ros2/ros2cli/issues/808))
- add timeout option for ros2param to find node. ([#802](https://github.com/ros2/ros2cli/issues/802))
- Save method list via connection check to XMLRPC server. ([#796](https://github.com/ros2/ros2cli/issues/796))
- ZSH argcomplete: call compinit only if needed ([#750](https://github.com/ros2/ros2cli/issues/750))
- Fix network aware node issue ([#785](https://github.com/ros2/ros2cli/issues/785))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- XMLRPC server accepts request from all local IP addresses. ([#729](https://github.com/ros2/ros2cli/issues/729))
- Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Ivan Santiago Paunovic, Tomoya Fujita, Yadu, mjbogusz

<a id="ros2cli-common-extensions"></a>

## [ros2cli\_common\_extensions](https://github.com/ros2/ros2cli_common_extensions/tree/iron/ros2cli_common_extensions/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#7](https://github.com/ros2/ros2cli_common_extensions/issues/7))
- Update maintainers ([#6](https://github.com/ros2/ros2cli_common_extensions/issues/6))
- Contributors: Audrow Nash, methylDragon

<a id="ros2cli-test-interfaces"></a>

## [ros2cli\_test\_interfaces](https://github.com/ros2/ros2cli/tree/iron/ros2cli_test_interfaces/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Remove action\_msgs dependency ([#743](https://github.com/ros2/ros2cli/issues/743))
- Contributors: Audrow Nash, Jacob Perron

<a id="ros2component"></a>

## [ros2component](https://github.com/ros2/ros2cli/tree/iron/ros2component/CHANGELOG.rst)

- Enable document generation using rosdoc2 ([#811](https://github.com/ros2/ros2cli/issues/811))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Fix the component load help to mention load, not unload. ([#756](https://github.com/ros2/ros2cli/issues/756))
- Remove unused arguments from ros2 component types. ([#711](https://github.com/ros2/ros2cli/issues/711))
- Contributors: Audrow Nash, Chris Lalancette, Yadu

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/iron/ros2doctor/CHANGELOG.rst)

- Shutdown ros2doctor hello when ctrl-c is received ([#829](https://github.com/ros2/ros2cli/issues/829))
- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- Enable document generation using rosdoc2 ([#811](https://github.com/ros2/ros2cli/issues/811)) \* Fix warnings for ros2component, ros2doctor, ros2interface, and ros2node
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette, Michael Carroll, Yadu

<a id="ros2interface"></a>

## [ros2interface](https://github.com/ros2/ros2cli/tree/iron/ros2interface/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- Enable document generation using rosdoc2 ([#811](https://github.com/ros2/ros2cli/issues/811))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette, Yadu

<a id="ros2launch"></a>

## [ros2launch](https://github.com/ros2/launch_ros/tree/iron/ros2launch/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#331](https://github.com/ros2/launch_ros/issues/331))
- Contributors: Audrow Nash

<a id="ros2lifecycle"></a>

## [ros2lifecycle](https://github.com/ros2/ros2cli/tree/iron/ros2lifecycle/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2lifecycle-test-fixtures"></a>

## [ros2lifecycle\_test\_fixtures](https://github.com/ros2/ros2cli/tree/iron/ros2lifecycle_test_fixtures/CHANGELOG.rst)

- Update the ros2cli test fixture to C++17. ([#789](https://github.com/ros2/ros2cli/issues/789))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2multicast"></a>

## [ros2multicast](https://github.com/ros2/ros2cli/tree/iron/ros2multicast/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Add –group and –port options to ros2 multicast ([#770](https://github.com/ros2/ros2cli/issues/770))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ros2node"></a>

## [ros2node](https://github.com/ros2/ros2cli/tree/iron/ros2node/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- Enable document generation using rosdoc2 ([#811](https://github.com/ros2/ros2cli/issues/811)) \* Fix warnings for ros2component, ros2doctor, ros2interface, and ros2node
- Fix linters ([#808](https://github.com/ros2/ros2cli/issues/808))
- add timeout option for ros2param to find node. ([#802](https://github.com/ros2/ros2cli/issues/802))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Updated wording in list.py ([#775](https://github.com/ros2/ros2cli/issues/775))
- Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Michael Wrock, Tomoya Fujita, Yadu

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/iron/ros2param/CHANGELOG.rst)

- remove deprecated options ([#824](https://github.com/ros2/ros2cli/issues/824))
- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- add timeout option for ros2param to find node. ([#802](https://github.com/ros2/ros2cli/issues/802))
- Fix printing of integer and double arrays. ([#804](https://github.com/ros2/ros2cli/issues/804))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- refactor: make ros2param use rclpy.parameter\_client ([#716](https://github.com/ros2/ros2cli/issues/716))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Tomoya Fujita

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/iron/ros2pkg/CHANGELOG.rst)

- Fix typo in ros2pkg warning message. ([#828](https://github.com/ros2/ros2cli/issues/828))
- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- resolve [#790](https://github.com/ros2/ros2cli/issues/790) ([#801](https://github.com/ros2/ros2cli/issues/801))
- Add alias library targets for CMake ([#718](https://github.com/ros2/ros2cli/issues/718))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld, RFRIEDM-Trimble, Tomoya Fujita

<a id="ros2run"></a>

## [ros2run](https://github.com/ros2/ros2cli/tree/iron/ros2run/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/iron/ros2service/CHANGELOG.rst)

- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- Contributors: Audrow Nash, Chris Lalancette

<a id="ros2test"></a>

## [ros2test](https://github.com/ros2/ros_testing/tree/iron/ros2test/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#12](https://github.com/ros2/ros_testing/issues/12))
- update maintainer
- Contributors: Audrow Nash, Dharini Dutia, quarkytale

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/iron/ros2topic/CHANGELOG.rst)

- remove deprecated options ([#824](https://github.com/ros2/ros2cli/issues/824))
- Make all of the dependencies in pure Python packages exec\_depend. ([#823](https://github.com/ros2/ros2cli/issues/823))
- Expect type hash cli output in test ([#822](https://github.com/ros2/ros2cli/issues/822))
- Fix the type annotation in pub.py. ([#814](https://github.com/ros2/ros2cli/issues/814))
- Switch to using new event\_handler instead of qos\_event. ([#787](https://github.com/ros2/ros2cli/issues/787))
- avoid flaky test that subscriber might not receive the message ([#810](https://github.com/ros2/ros2cli/issues/810))
- Adds a `--max-wait-time` option to `ros2 topic pub` ([#800](https://github.com/ros2/ros2cli/issues/800))
- Fix some flake8 warnings related to style. ([#805](https://github.com/ros2/ros2cli/issues/805))
- Adds a timeout feature to rostopic echo ([#792](https://github.com/ros2/ros2cli/issues/792))
- Refactor common types ([#791](https://github.com/ros2/ros2cli/issues/791))
- Allow configuring liveliness in ros2 topic echo and pub ([#788](https://github.com/ros2/ros2cli/issues/788))
- Extend timeout to shutdown the command line process. ([#783](https://github.com/ros2/ros2cli/issues/783))
- [rolling] Update maintainers - 2022-11-07 ([#776](https://github.com/ros2/ros2cli/issues/776))
- a couple of typo fixes. ([#774](https://github.com/ros2/ros2cli/issues/774))
- Add support use\_sim\_time for ros2 topic hz/bw/pub. ([#754](https://github.com/ros2/ros2cli/issues/754))
- Use set\_message\_fields from rosidl\_runtime\_py ([#761](https://github.com/ros2/ros2cli/issues/761))
- Expand auto to the current time when passed to a Header field ([#749](https://github.com/ros2/ros2cli/issues/749))
- Add verbose option to echo that also prints the associated message info ([#707](https://github.com/ros2/ros2cli/issues/707))
- update docs for bandwidth functions. ([#709](https://github.com/ros2/ros2cli/issues/709))
- Split the bandwidth functions into a get and print. ([#708](https://github.com/ros2/ros2cli/issues/708))
- Contributors: Arjo Chakravarty, Audrow Nash, Chen Lihui, Chris Lalancette, Emerson Knapp, Esteve Fernandez, Ivan Santiago Paunovic, Lei Liu, Tomoya Fujita

<a id="ros2trace"></a>

## [ros2trace](https://github.com/ros2/ros2_tracing/tree/iron/ros2trace/CHANGELOG.rst)

- Move ros2trace tests to new test\_ros2trace package ([#63](https://github.com/ros2/ros2_tracing/issues/63))
- Error out if trace already exists unless ‘append’ option is used ([#58](https://github.com/ros2/ros2_tracing/issues/58))
- Improve ‘ros2 trace’ command error handling & add end-to-end tests ([#54](https://github.com/ros2/ros2_tracing/issues/54))
- Contributors: Christophe Bedard

<a id="ros-testing"></a>

## [ros\_testing](https://github.com/ros2/ros_testing/tree/iron/ros_testing/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#12](https://github.com/ros2/ros_testing/issues/12))
- update maintainer
- Contributors: Audrow Nash, Dharini Dutia, quarkytale

<a id="rosbag2"></a>

## [rosbag2](https://github.com/ros2/rosbag2/tree/iron/rosbag2/CHANGELOG.rst)

- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Move sqlite3 storage implementation to rosbag2\_storage\_sqlite3 package ([#1113](https://github.com/ros2/rosbag2/issues/1113))
- Contributors: Emerson Knapp, Michael Orlov

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/iron/rosbag2_compression/CHANGELOG.rst)

- Add in a missing cstdint include. ([#1321](https://github.com/ros2/rosbag2/issues/1321)) ([#1322](https://github.com/ros2/rosbag2/issues/1322))
- Fix warning from ClassLoader in sequential compression reader and writer ([#1299](https://github.com/ros2/rosbag2/issues/1299)) ([#1316](https://github.com/ros2/rosbag2/issues/1316))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- Add `update_metadata(BagMetadata)` API for storage plugin interface ([#1149](https://github.com/ros2/rosbag2/issues/1149))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- Add option to prevent message loss while converting ([#1058](https://github.com/ros2/rosbag2/issues/1058))
- set default metadata of compressed message (in case compressor does not set it) ([#1060](https://github.com/ros2/rosbag2/issues/1060))
- Speed optimization: Preparing copyless publish/subscribing by using const message for writing ([#1010](https://github.com/ros2/rosbag2/issues/1010))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS, Emerson Knapp, Hunter L. Allen, Joshua Hampp, Michael Orlov, Tony Peng, james-rms, mergify[bot]

<a id="rosbag2-compression-zstd"></a>

## [rosbag2\_compression\_zstd](https://github.com/ros2/rosbag2/tree/iron/rosbag2_compression_zstd/CHANGELOG.rst)

- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Speed optimization: Preparing copyless publish/subscribing by using const message for writing ([#1010](https://github.com/ros2/rosbag2/issues/1010))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS, Joshua Hampp, Michael Orlov

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/iron/rosbag2_cpp/CHANGELOG.rst)

- Add recorder stop() API ([#1300](https://github.com/ros2/rosbag2/issues/1300)) ([#1334](https://github.com/ros2/rosbag2/issues/1334))
- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- Fix for flaky `TimeControllerClockTest::unpaused_sleep_returns_true` test ([#1290](https://github.com/ros2/rosbag2/issues/1290))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Fix rwm->rmw spelling ([#1249](https://github.com/ros2/rosbag2/issues/1249))
- Expose more Writer methods in python interface ([#1220](https://github.com/ros2/rosbag2/issues/1220))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Parametrize all rosbag2\_tests for both supported storage plugins ([#1221](https://github.com/ros2/rosbag2/issues/1221))
- rosbag2\_cpp: test more than one storage plugin ([#1196](https://github.com/ros2/rosbag2/issues/1196))
- Replace language for “db3”/”db”/”database” ([#1194](https://github.com/ros2/rosbag2/issues/1194))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- Remove explicit sqlite3 from code ([#1166](https://github.com/ros2/rosbag2/issues/1166))
- Add `update_metadata(BagMetadata)` API for storage plugin interface ([#1149](https://github.com/ros2/rosbag2/issues/1149))
- Reader and writer can use default storage by not specifying ([#1167](https://github.com/ros2/rosbag2/issues/1167))
- rosbag2\_storage: expose default storage ID as method ([#1146](https://github.com/ros2/rosbag2/issues/1146))
- Don’t reopen file for every seek if we don’t have to. Search directionally for the correct file ([#1117](https://github.com/ros2/rosbag2/issues/1117))
- Add SplitBagfile recording service. ([#1115](https://github.com/ros2/rosbag2/issues/1115))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- Replace `std::filesystem::path(..)` with `rcpputils::fs::path(..)` ([#1104](https://github.com/ros2/rosbag2/issues/1104))
- Fix issue where sequentialwriter only sets metadata duration to the duration of the final file ([#1098](https://github.com/ros2/rosbag2/issues/1098))
- Delete obsolete compression\_options.cpp from rosbag2\_cpp ([#1078](https://github.com/ros2/rosbag2/issues/1078))
- Readers/info can accept a single bag storage file, and detect its storage id automatically ([#1072](https://github.com/ros2/rosbag2/issues/1072))
- Remove deprecated rosbag2\_cpp/storage\_options.hpp, for post-Humble releases ([#1064](https://github.com/ros2/rosbag2/issues/1064))
- Speed optimization: Preparing copyless publish/subscribing by using const message for writing ([#1010](https://github.com/ros2/rosbag2/issues/1010))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Notification of significant events during bag recording and playback ([#908](https://github.com/ros2/rosbag2/issues/908))
- Bugfix for “Playing the bags recorded with split by duration/size is playing only the last recorded .db3.” ([#1022](https://github.com/ros2/rosbag2/issues/1022))
- Improve test\_time\_controller test ([#1012](https://github.com/ros2/rosbag2/issues/1012))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, DensoADAS, Emerson Knapp, Geoffrey Biggs, Hunter L. Allen, Jorge Perez, Joshua Hampp, Kaju-Bubanja, Michael Orlov, Tony Peng, james-rms, mergify[bot], rshanor

<a id="rosbag2-examples-cpp"></a>

## [rosbag2\_examples\_cpp](https://github.com/ros2/rosbag2/tree/iron/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst)

- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Add API samples on main branch - Rolling C++ API examples ([#1068](https://github.com/ros2/rosbag2/issues/1068))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Michael Orlov, james-rms

<a id="rosbag2-examples-py"></a>

## [rosbag2\_examples\_py](https://github.com/ros2/rosbag2/tree/iron/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst)

- Fix a warning from python setuptools. ([#1312](https://github.com/ros2/rosbag2/issues/1312)) ([#1314](https://github.com/ros2/rosbag2/issues/1314))
- Add API samples for Python [rebased] ([#1253](https://github.com/ros2/rosbag2/issues/1253)) \* Add API samples for Python \* Package Renaming and Move \* linting + copyright \* more linting ——— Co-authored-by: Geoffrey Biggs <[gbiggs@killbots.net](mailto:gbiggs%40killbots.net)>
- Contributors: David V. Lu!!, mergify[bot]

<a id="rosbag2-interfaces"></a>

## [rosbag2\_interfaces](https://github.com/ros2/rosbag2/tree/iron/rosbag2_interfaces/CHANGELOG.rst)

- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Add SplitBagfile recording service. ([#1115](https://github.com/ros2/rosbag2/issues/1115))
- Adds stop operation for rosbag2::Player ([#1007](https://github.com/ros2/rosbag2/issues/1007))
- Notification of significant events during bag recording and playback ([#908](https://github.com/ros2/rosbag2/issues/908))
- Adds play until timestamp functionality ([#1005](https://github.com/ros2/rosbag2/issues/1005))
- Add CLI verb for burst mode of playback ([#980](https://github.com/ros2/rosbag2/issues/980))
- Add play-for specified number of seconds functionality ([#960](https://github.com/ros2/rosbag2/issues/960))
- Contributors: Agustin Alba Chicar, Chris Lalancette, Geoffrey Biggs, Michael Orlov, Misha Shalem, rshanor

<a id="rosbag2-performance-benchmarking"></a>

## [rosbag2\_performance\_benchmarking](https://github.com/ros2/rosbag2/tree/iron/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst)

- Add tests for rosbag2\_performance\_benchmarking pkg ([#1268](https://github.com/ros2/rosbag2/issues/1268))
- Fix expectations for rosbag2 return code in rosbag2\_performance\_benchmarking ([#1267](https://github.com/ros2/rosbag2/issues/1267))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use thread pool to run benchmark publishers in rosbag2\_performance\_benchmarking ([#1250](https://github.com/ros2/rosbag2/issues/1250))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Skip ament\_package() call when not building rosbag2\_performance\_benchmarking ([#1242](https://github.com/ros2/rosbag2/issues/1242))
- Add option to specify a message type ([#1153](https://github.com/ros2/rosbag2/issues/1153))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Replace language for “db3”/”db”/”database” ([#1194](https://github.com/ros2/rosbag2/issues/1194))
- Remove explicit sqlite3 from code ([#1166](https://github.com/ros2/rosbag2/issues/1166))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Michael Orlov, Shane Loretz, carlossvg

<a id="rosbag2-performance-benchmarking-msgs"></a>

## [rosbag2\_performance\_benchmarking\_msgs](https://github.com/ros2/rosbag2/tree/iron/rosbag2_performance/rosbag2_performance_benchmarking_msgs/CHANGELOG.rst)

- Add tests for rosbag2\_performance\_benchmarking pkg ([#1268](https://github.com/ros2/rosbag2/issues/1268))
- Skip ament\_package() call when not building rosbag2\_performance\_benchmarking ([#1242](https://github.com/ros2/rosbag2/issues/1242))
- [rolling] Bump to 0.19.0 ([#1232](https://github.com/ros2/rosbag2/issues/1232))
- Add option to specify a message type ([#1153](https://github.com/ros2/rosbag2/issues/1153))
- Contributors: Audrow Nash, Michael Orlov, Shane Loretz, carlossvg

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/iron/rosbag2_py/CHANGELOG.rst)

- Add binding to close the writer ([#1339](https://github.com/ros2/rosbag2/issues/1339)) ([#1340](https://github.com/ros2/rosbag2/issues/1340))
- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- Store message definitions in SQLite3 storage plugin ([#1293](https://github.com/ros2/rosbag2/issues/1293))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Expose more Writer methods in python interface ([#1220](https://github.com/ros2/rosbag2/issues/1220))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- rosbag2\_py: parametrize tests across storage plugins ([#1203](https://github.com/ros2/rosbag2/issues/1203))
- Added option to change node name for the recorder from the Python API ([#1180](https://github.com/ros2/rosbag2/issues/1180))
- Replace language for “db3”/”db”/”database” ([#1194](https://github.com/ros2/rosbag2/issues/1194))
- Remove explicit sqlite3 from code ([#1166](https://github.com/ros2/rosbag2/issues/1166))
- Move python get\_default\_storage\_id to storage module instead of writer ([#1165](https://github.com/ros2/rosbag2/issues/1165))
- rosbag2\_storage: expose default storage ID as method ([#1146](https://github.com/ros2/rosbag2/issues/1146))
- rosbag2\_py: set defaults for config when bag rewriting ([#1121](https://github.com/ros2/rosbag2/issues/1121))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- expose py Reader metadata, improve `rosbag2_py.BagMetadata` usability ([#1082](https://github.com/ros2/rosbag2/issues/1082))
- Added support for excluding topics via regular expressions ([#1046](https://github.com/ros2/rosbag2/issues/1046))
- Use a single variable for evaluating the filter regex ([#1053](https://github.com/ros2/rosbag2/issues/1053))
- Add additional mode of publishing sim time updates triggered by replayed messages ([#1050](https://github.com/ros2/rosbag2/issues/1050))
- Renamed –topics-regex to –regex and -e in Player class to be consistent with Recorder ([#1045](https://github.com/ros2/rosbag2/issues/1045))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Added support for filtering topics via regular expressions on Playback ([#1034](https://github.com/ros2/rosbag2/issues/1034))
- Adds play until timestamp functionality ([#1005](https://github.com/ros2/rosbag2/issues/1005))
- Add CLI verb for burst mode of playback ([#980](https://github.com/ros2/rosbag2/issues/980))
- Add play-for specified number of seconds functionality ([#960](https://github.com/ros2/rosbag2/issues/960))
- Make unpublished topics unrecorded by default ([#968](https://github.com/ros2/rosbag2/issues/968))
- Fix test rosbag2\_py test compatibility with Python < 3.8 ([#987](https://github.com/ros2/rosbag2/issues/987))
- Contributors: Agustin Alba Chicar, Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Esteve Fernandez, Geoffrey Biggs, Hunter L. Allen, Michael Orlov, Scott K Logan, Sean Kelly, Tony Peng, james-rms, kylemarcey, mergify[bot], ricardo-manriquez

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/iron/rosbag2_storage/CHANGELOG.rst)

- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- Remove explicit sqlite3 from code ([#1166](https://github.com/ros2/rosbag2/issues/1166))
- Add `update_metadata(BagMetadata)` API for storage plugin interface ([#1149](https://github.com/ros2/rosbag2/issues/1149))
- rosbag2\_storage: expose default storage ID as method ([#1146](https://github.com/ros2/rosbag2/issues/1146))
- Don’t reopen file for every seek if we don’t have to. Search directionally for the correct file ([#1117](https://github.com/ros2/rosbag2/issues/1117))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- Remove YAML\_CPP\_DLL define ([#964](https://github.com/ros2/rosbag2/issues/964))
- Added support for excluding topics via regular expressions ([#1046](https://github.com/ros2/rosbag2/issues/1046))
- Readers/info can accept a single bag storage file, and detect its storage id automatically ([#1072](https://github.com/ros2/rosbag2/issues/1072))
- Use a single variable for evaluating the filter regex ([#1053](https://github.com/ros2/rosbag2/issues/1053))
- Speed optimization: Preparing copyless publish/subscribing by using const message for writing ([#1010](https://github.com/ros2/rosbag2/issues/1010))
- Renamed –topics-regex to –regex and -e in Player class to be consistent with Recorder ([#1045](https://github.com/ros2/rosbag2/issues/1045))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Added support for filtering topics via regular expressions on Playback ([#1034](https://github.com/ros2/rosbag2/issues/1034))
- Contributors: Akash, Chris Lalancette, Daisuke Nishimatsu, DensoADAS, Emerson Knapp, Esteve Fernandez, Hunter L. Allen, Joshua Hampp, Michael Orlov, Tony Peng, james-rms

<a id="rosbag2-storage-default-plugins"></a>

## [rosbag2\_storage\_default\_plugins](https://github.com/ros2/rosbag2/tree/iron/rosbag2_storage_default_plugins/CHANGELOG.rst)

- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Move sqlite3 storage implementation to rosbag2\_storage\_sqlite3 package ([#1113](https://github.com/ros2/rosbag2/issues/1113))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- Add support for old db3 schema used on distros prior to Foxy ([#1090](https://github.com/ros2/rosbag2/issues/1090))
- Added support for excluding topics via regular expressions ([#1046](https://github.com/ros2/rosbag2/issues/1046))
- Contributors: Emerson Knapp, Esteve Fernandez, Michael Orlov, james-rms

<a id="rosbag2-storage-mcap"></a>

## [rosbag2\_storage\_mcap](https://github.com/ros2/rosbag2/tree/iron/rosbag2_storage_mcap/CHANGELOG.rst)

- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- CLI: Get storage-specific values from plugin ([#1209](https://github.com/ros2/rosbag2/issues/1209))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- rosbag2\_cpp: test more than one storage plugin ([#1196](https://github.com/ros2/rosbag2/issues/1196))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- rosbag2\_storage\_mcap: merge into rosbag2 repo ([#1163](https://github.com/ros2/rosbag2/issues/1163))
- mcap\_storage: ‘none’ is a valid storage preset profile ([#86](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/86))
- mcap\_storage: handle update\_metadata call ([#83](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/83))
- Update clang-format rules to fit ROS 2 style guide ([#80](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/80))
- Revert “read\_order: throw exception from set\_read\_order for unsupported orders”
- read\_order: throw exception from set\_read\_order for unsupported orders
- Fix compile flags to work on rosbag\_storage:0.17.x ([#78](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/78))
- Fix Windows build ([#73](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/73))
- set defaults for SQLite plugin parity ([#68](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/68))
- rosbag2\_storage\_mcap: add storage preset profiles ([#57](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/57))
- rename test\_fixture\_interfaces package to testdata ([#64](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/64))
- Switch to using the vendored zstd library. ([#59](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/59))
- Add set\_read\_order reader API ([#54](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/54))
- Some minor improvements in rosbag2\_storage\_mcap after review ([#58](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/58))
- Revert “rosbag2\_storage\_mcap: add storage preset profiles”
- rosbag2\_storage\_mcap: add storage preset profiles
- Store IDL message definitions in Schema records when no MSG definition is available ([#43](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/43))
- Support timestamp-ordered playback ([#50](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/50))
- Support regex topic filtering
- Add all lz4 sources to fix undefined symbols at runtime ([#46](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/46))
- Upgrade mcap to fix LZ4 error and segfault ([#42](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/42))
- Fix build for Foxy ([#34](https://github.com/ros-tooling/rosbag2_storage_mcap/issues/34))
- fix: minor issues ([#31](https://github.com/wep21/rosbag2_storage_mcap/issues/31)) \* remove unnecessary block \* use target\_link\_libraries instead of ament\_target\_dependencies \* remove ros environment \* add prefix to compile definition
- Update email address for Foxglove maintainers ([#32](https://github.com/wep21/rosbag2_storage_mcap/issues/32))
- Added mcap\_vendor package. Updated CMakeLists.txt to fetch dependencies with FetchContent rather than Conan.
- CMake build script will now execute pip install conan automatically.
- [1.0.0] Use Summary section for get\_metadata() and seek(), implement remaining methods ([#17](https://github.com/wep21/rosbag2_storage_mcap/issues/17))
- feat: add play impl ([#16](https://github.com/wep21/rosbag2_storage_mcap/issues/16))
- chore: refine package.xml ([#15](https://github.com/wep21/rosbag2_storage_mcap/issues/15))
- Don’t throw when READ\_WRITE mode is used; add .mcap file extension to recorded files ([#14](https://github.com/wep21/rosbag2_storage_mcap/issues/14))
- Add dynamic message definition lookup ([#13](https://github.com/wep21/rosbag2_storage_mcap/issues/13))
- Switch C++ formatter to clang-format ([#12](https://github.com/wep21/rosbag2_storage_mcap/issues/12))
- Merge pull request [#7](https://github.com/wep21/rosbag2_storage_mcap/issues/7) from ros-tooling/jhurliman/reader-writer
- uninitialized struct
- lint
- lint
- lint
- Reader and writer implementation
- Merge pull request [#6](https://github.com/wep21/rosbag2_storage_mcap/issues/6) from wep21/add-metadata-impl
- feat: add metadata impl
- Merge pull request [#5](https://github.com/wep21/rosbag2_storage_mcap/issues/5) from wep21/mcap-storage-impl
- chore: update cmake minimum version
- chore: install mcap header
- chore: include mcap header
- fix: move fetch content into rosbag2 storage mcap
- Merge pull request [#3](https://github.com/wep21/rosbag2_storage_mcap/issues/3) from ros-tooling/emersonknapp/mcap\_plugin\_skeleton
- Add rosbag2\_storage\_mcap skeleton
- Contributors: Andrew Symington, Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Jacob Bandes-Storch, James Smith, John Hurliman, Michael Orlov, james-rms, wep21

<a id="rosbag2-storage-sqlite3"></a>

## [rosbag2\_storage\_sqlite3](https://github.com/ros2/rosbag2/tree/iron/rosbag2_storage_sqlite3/CHANGELOG.rst)

- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- Store message definitions in SQLite3 storage plugin ([#1293](https://github.com/ros2/rosbag2/issues/1293))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- CLI: Get storage-specific values from plugin ([#1209](https://github.com/ros2/rosbag2/issues/1209))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Remove sqlite3-specific info from main README, make it more storage agnostic and point to plugin-specific README ([#1193](https://github.com/ros2/rosbag2/issues/1193))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- Add `update_metadata(BagMetadata)` API for storage plugin interface ([#1149](https://github.com/ros2/rosbag2/issues/1149))
- Store db schema version and ROS\_DISTRO name in db3 files ([#1156](https://github.com/ros2/rosbag2/issues/1156))
- ros2bag: move storage preset validation to sqlite3 plugin ([#1135](https://github.com/ros2/rosbag2/issues/1135))
- Move sqlite3 storage implementation to rosbag2\_storage\_sqlite3 package ([#1113](https://github.com/ros2/rosbag2/issues/1113))
- Use a single variable for evaluating the filter regex ([#1053](https://github.com/ros2/rosbag2/issues/1053))
- Renamed –topics-regex to –regex and -e in Player class to be consistent with Recorder ([#1045](https://github.com/ros2/rosbag2/issues/1045))
- Added support for filtering topics via regular expressions on Playback ([#1034](https://github.com/ros2/rosbag2/issues/1034))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Esteve Fernandez, Michael Orlov, james-rms

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/iron/rosbag2_test_common/CHANGELOG.rst)

- Address flakiness in rosbag2\_play\_end\_to\_end tests ([#1297](https://github.com/ros2/rosbag2/issues/1297)) ([#1330](https://github.com/ros2/rosbag2/issues/1330))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- rosbag2\_py: parametrize tests across storage plugins ([#1203](https://github.com/ros2/rosbag2/issues/1203))
- Fix for ros2 bag play exit with non-zero code on SIGINT ([#1126](https://github.com/ros2/rosbag2/issues/1126))
- Split up the include of rclcpp.hpp ([#1027](https://github.com/ros2/rosbag2/issues/1027))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Michael Orlov, james-rms, mergify[bot]

<a id="rosbag2-test-msgdefs"></a>

## [rosbag2\_test\_msgdefs](https://github.com/ros2/rosbag2/tree/iron/rosbag2_test_msgdefs/CHANGELOG.rst)

- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265)) The intention of this PR is to move the message-definition-finding capability outside of rosbag2\_storage\_mcap, and allow any rosbag2 storage plugin to store message definitions.
- Contributors: james-rms

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/iron/rosbag2_tests/CHANGELOG.rst)

- Address flakiness in rosbag2\_play\_end\_to\_end tests ([#1297](https://github.com/ros2/rosbag2/issues/1297)) ([#1330](https://github.com/ros2/rosbag2/issues/1330))
- Add type\_hash in MessageDefinition struct ([#1296](https://github.com/ros2/rosbag2/issues/1296))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Parametrize all rosbag2\_tests for both supported storage plugins ([#1221](https://github.com/ros2/rosbag2/issues/1221))
- Make rosbag2\_tests agnostic to storage implementation ([#1192](https://github.com/ros2/rosbag2/issues/1192))
- Get rid from attempt to open DB file in `wait_for_db()` test fixture ([#1141](https://github.com/ros2/rosbag2/issues/1141))
- Fix for ros2 bag play exit with non-zero code on SIGINT ([#1126](https://github.com/ros2/rosbag2/issues/1126))
- Move sqlite3 storage implementation to rosbag2\_storage\_sqlite3 package ([#1113](https://github.com/ros2/rosbag2/issues/1113))
- Readers/info can accept a single bag storage file, and detect its storage id automatically ([#1072](https://github.com/ros2/rosbag2/issues/1072))
- Add the ability to record any key/value pair in ‘custom’ field in metadata.yaml ([#1038](https://github.com/ros2/rosbag2/issues/1038))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Emerson Knapp, Hunter L. Allen, Michael Orlov, Tony Peng, james-rms, mergify[bot]

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/iron/rosbag2_transport/CHANGELOG.rst)

- Change subscriptions from GenericSubscripton to SubscriptionBase ([#1338](https://github.com/ros2/rosbag2/issues/1338))
- Add recorder stop() API ([#1300](https://github.com/ros2/rosbag2/issues/1300)) ([#1334](https://github.com/ros2/rosbag2/issues/1334))
- Read message definitions from input files in bag\_rewrite ([#1295](https://github.com/ros2/rosbag2/issues/1295))
- Add message definition read API ([#1292](https://github.com/ros2/rosbag2/issues/1292))
- Move rosbag2\_transport::Recorder implementation to pimpl ([#1291](https://github.com/ros2/rosbag2/issues/1291))
- rosbag2\_storage: add type description hash to topic metadata ([#1272](https://github.com/ros2/rosbag2/issues/1272))
- rosbag2\_cpp: move local message definition source out of MCAP plugin ([#1265](https://github.com/ros2/rosbag2/issues/1265))
- Use RMW methods to initialize endpoint info instead of brace initializer to guard against upcoming struct change ([#1257](https://github.com/ros2/rosbag2/issues/1257))
- Update rosbag2 to C++17. ([#1238](https://github.com/ros2/rosbag2/issues/1238))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#1202](https://github.com/ros2/rosbag2/issues/1202))
- Print “Hidden topics are not recorded” only once. ([#1225](https://github.com/ros2/rosbag2/issues/1225))
- rosbag2\_storage: set MCAP as default plugin ([#1160](https://github.com/ros2/rosbag2/issues/1160))
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- rosbag2\_transport: parametrize test\_rewrite ([#1206](https://github.com/ros2/rosbag2/issues/1206))
- rosbag2\_cpp: test more than one storage plugin ([#1196](https://github.com/ros2/rosbag2/issues/1196))
- Replace language for “db3”/”db”/”database” ([#1194](https://github.com/ros2/rosbag2/issues/1194))
- set\_read\_order: return success ([#1177](https://github.com/ros2/rosbag2/issues/1177))
- Remove explicit sqlite3 from code ([#1166](https://github.com/ros2/rosbag2/issues/1166))
- Add pause and resume service calls for rosbag2 recorder ([#1131](https://github.com/ros2/rosbag2/issues/1131))
- Redesign record\_services tests to make them more deterministic ([#1122](https://github.com/ros2/rosbag2/issues/1122))
- Add SplitBagfile recording service. ([#1115](https://github.com/ros2/rosbag2/issues/1115))
- Reverse read order API and sqlite storage implementation ([#1083](https://github.com/ros2/rosbag2/issues/1083))
- make recorder node composable by inheritance ([#1093](https://github.com/ros2/rosbag2/issues/1093))
- Mark `test_play_services` as xfail for FastRTPS and CycloneDDS ([#1091](https://github.com/ros2/rosbag2/issues/1091))
- fixed typo ([#1057](https://github.com/ros2/rosbag2/issues/1057))
- Fix hangout in rosbag2 player and recorder when pressing `CTRL+C` ([#1081](https://github.com/ros2/rosbag2/issues/1081))
- Added support for excluding topics via regular expressions ([#1046](https://github.com/ros2/rosbag2/issues/1046))
- Use a single variable for evaluating the filter regex ([#1053](https://github.com/ros2/rosbag2/issues/1053))
- Add additional mode of publishing sim time updates triggered by replayed messages ([#1050](https://github.com/ros2/rosbag2/issues/1050))
- Speed optimization: Preparing copyless publish/subscribing by using const message for writing ([#1010](https://github.com/ros2/rosbag2/issues/1010))
- Renamed –topics-regex to –regex and -e in Player class to be consistent with Recorder ([#1045](https://github.com/ros2/rosbag2/issues/1045))
- Refactor play until and duration tests ([#1024](https://github.com/ros2/rosbag2/issues/1024))
- Added support for filtering topics via regular expressions on Playback ([#1034](https://github.com/ros2/rosbag2/issues/1034))
- Adds stop operation for rosbag2::Player ([#1007](https://github.com/ros2/rosbag2/issues/1007))
- Fix incorrect boundary check for `playback_duration` and `play_until_timestamp` ([#1032](https://github.com/ros2/rosbag2/issues/1032))
- Split up the include of rclcpp.hpp ([#1027](https://github.com/ros2/rosbag2/issues/1027))
- Notification of significant events during bag recording and playback ([#908](https://github.com/ros2/rosbag2/issues/908))
- Adds play until timestamp functionality ([#1005](https://github.com/ros2/rosbag2/issues/1005))
- Add CLI verb for burst mode of playback ([#980](https://github.com/ros2/rosbag2/issues/980))
- Add on play message callbacks to the `rosbag2::Player` class ([#1004](https://github.com/ros2/rosbag2/issues/1004))
- Add play-for specified number of seconds functionality ([#960](https://github.com/ros2/rosbag2/issues/960))
- Reduce message spam when topics to be recorded do not exist ([#1018](https://github.com/ros2/rosbag2/issues/1018))
- Address flakiness in record\_all\_with\_sim\_time test ([#1014](https://github.com/ros2/rosbag2/issues/1014))
- Add debug instrumentation for `test_play_services` ([#1013](https://github.com/ros2/rosbag2/issues/1013))
- Fix for rosbag2::Player freeze when pressing ctrl+c in pause mode ([#1002](https://github.com/ros2/rosbag2/issues/1002))
- Add the /bigobj flag to Windows Debug builds. ([#1009](https://github.com/ros2/rosbag2/issues/1009))
- Make unpublished topics unrecorded by default ([#968](https://github.com/ros2/rosbag2/issues/968))
- Make peek\_next\_message\_from\_queue return a SharedPtr. ([#993](https://github.com/ros2/rosbag2/issues/993))
- Change the topic names in test\_record.cpp ([#988](https://github.com/ros2/rosbag2/issues/988))
- Contributors: Agustin Alba Chicar, Bernardo Taveira, Brian, Chris Lalancette, Cristóbal Arroyo, Daisuke Nishimatsu, DensoADAS, Emerson Knapp, Esteve Fernandez, Geoffrey Biggs, Jorge Perez, Joshua Hampp, Michael Orlov, Misha Shalem, Sean Kelly, Tony Peng, james-rms, kylemarcey, mergify[bot], rshanor

<a id="rosgraph-msgs"></a>

## [rosgraph\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/rosgraph_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Contributors: Audrow Nash, Chris Lalancette

<a id="rosidl-adapter"></a>

## [rosidl\_adapter](https://github.com/ros2/rosidl/tree/iron/rosidl_adapter/CHANGELOG.rst)

- rosidl\_adapter/cmake/rosidl\_adapt\_interfaces.cmake: Make ament free ([#709](https://github.com/ros2/rosidl/issues/709))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- Adding tests for unicode support in message comments. ([#720](https://github.com/ros2/rosidl/issues/720))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Add action2idl script ([#654](https://github.com/ros2/rosidl/issues/654))
- Contributors: Audrow Nash, Brian, Guilherme Henrique Galelli Christmann, John Daktylidis, Yasushi SHOJI

<a id="rosidl-cli"></a>

## [rosidl\_cli](https://github.com/ros2/rosidl/tree/iron/rosidl_cli/CHANGELOG.rst)

- Fix warnings ([#726](https://github.com/ros2/rosidl/issues/726))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Contributors: Audrow Nash, Yadu

<a id="rosidl-cmake"></a>

## [rosidl\_cmake](https://github.com/ros2/rosidl/tree/iron/rosidl_cmake/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Skip rosidl\_generate\_interfaces dependency export on SKIP\_INSTALL. ([#708](https://github.com/ros2/rosidl/issues/708))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Fix comment in camel case conversion function ([#683](https://github.com/ros2/rosidl/issues/683))
- Protect rosidl\_target\_interfaces from using NOTFOUND in include\_directories ([#679](https://github.com/ros2/rosidl/issues/679))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron, Jose Luis Rivero, Shane Loretz

<a id="rosidl-core-generators"></a>

## [rosidl\_core\_generators](https://github.com/ros2/rosidl_core/tree/iron/rosidl_core_generators/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#2](https://github.com/ros2/rosidl_core/issues/2))
- Add generators and runtime configuration packages ([#1](https://github.com/ros2/rosidl_core/issues/1)) Moved (and renamed) from rosidl\_defaults. Related PR: <https://github.com/ros2/rosidl_defaults/pull/22>
- Contributors: Audrow Nash, Jacob Perron

<a id="rosidl-core-runtime"></a>

## [rosidl\_core\_runtime](https://github.com/ros2/rosidl_core/tree/iron/rosidl_core_runtime/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#2](https://github.com/ros2/rosidl_core/issues/2))
- Add generators and runtime configuration packages ([#1](https://github.com/ros2/rosidl_core/issues/1)) Moved (and renamed) from rosidl\_defaults. Related PR: <https://github.com/ros2/rosidl_defaults/pull/22>
- Contributors: Audrow Nash, Jacob Perron

<a id="rosidl-default-generators"></a>

## [rosidl\_default\_generators](https://github.com/ros2/rosidl_defaults/tree/iron/rosidl_default_generators/CHANGELOG.rst)

- add service\_msgs depend ([#24](https://github.com/ros2/rosidl_defaults/issues/24))
- [rolling] Update maintainers - 2022-11-07 ([#25](https://github.com/ros2/rosidl_defaults/issues/25))
- Move dependencies to rosidl\_core and depend on action\_msgs ([#22](https://github.com/ros2/rosidl_defaults/issues/22)) Move implementation to new packages rosidl\_core\_generators and rosidl\_runtime\_generators The new packages are located in a separate repository: <https://github.com/ros2/rosidl_core.git> rosidl\_defaults now depends on the new packages, plus message definitions required for Actions (namely action\_msgs). This allows users to avoid having to explictly depend on action\_msgs.
- Contributors: Audrow Nash, Brian, Jacob Perron

<a id="rosidl-default-runtime"></a>

## [rosidl\_default\_runtime](https://github.com/ros2/rosidl_defaults/tree/iron/rosidl_default_runtime/CHANGELOG.rst)

- add service\_msgs depend ([#24](https://github.com/ros2/rosidl_defaults/issues/24))
- [rolling] Update maintainers - 2022-11-07 ([#25](https://github.com/ros2/rosidl_defaults/issues/25))
- Move dependencies to rosidl\_core and depend on action\_msgs ([#22](https://github.com/ros2/rosidl_defaults/issues/22)) Move implementation to new packages rosidl\_core\_generators and rosidl\_runtime\_generators The new packages are located in a separate repository: <https://github.com/ros2/rosidl_core.git> rosidl\_defaults now depends on the new packages, plus message definitions required for Actions (namely action\_msgs). This allows users to avoid having to explictly depend on action\_msgs.
- Contributors: Audrow Nash, Brian, Jacob Perron

<a id="rosidl-dynamic-typesupport"></a>

## [rosidl\_dynamic\_typesupport](https://github.com/ros2/rosidl_dynamic_typesupport/tree/iron/CHANGELOG.rst)

- Fix up the exports for rosidl\_dynamic\_typesupport. ([#5](https://github.com/ros2/rosidl_dynamic_typesupport/issues/5))
- Refactor dynamic message type support impl to use allocators ([#2](https://github.com/ros2/rosidl_dynamic_typesupport/issues/2))
- Runtime Interface Reflection: rosidl\_dynamic\_typesupport ([#1](https://github.com/ros2/rosidl_dynamic_typesupport/issues/1))
- Contributors: Chris Lalancette, William Woodall, methylDragon

<a id="rosidl-dynamic-typesupport-fastrtps"></a>

## [rosidl\_dynamic\_typesupport\_fastrtps](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/tree/iron/CHANGELOG.rst)

- Remove more unnecessary semicolons ([#4](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/4))
- Dynamic Subscription (BONUS: Allocators): rosidl\_dynamic\_typesupport\_fastrtps ([#3](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/3))
- Remove unnecessary semicolons. ([#2](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/2))
- Runtime Interface Reflection: rosidl\_dynamic\_typesupport\_fastrtps ([#1](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/1))
- Contributors: Chris Lalancette, methylDragon

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/iron/rosidl_generator_c/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_generator\_c/cpp tests to a separate package ([#701](https://github.com/ros2/rosidl/issues/701))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Add namespaced ALIAS target to easily consume generated libraries via add\_subdirectory ([#605](https://github.com/ros2/rosidl/issues/605))
- Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron, Silvio Traversaro

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/iron/rosidl_generator_cpp/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_generator\_c/cpp tests to a separate package ([#701](https://github.com/ros2/rosidl/issues/701))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Add namespaced ALIAS target to easily consume generated libraries via add\_subdirectory ([#605](https://github.com/ros2/rosidl/issues/605))
- Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron, Silvio Traversaro

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/iron/rosidl_generator_dds_idl/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#60](https://github.com/ros2/rosidl_dds/issues/60))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#59](https://github.com/ros2/rosidl_dds/issues/59))
- Contributors: Audrow Nash, Jacob Perron

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/iron/rosidl_generator_py/CHANGELOG.rst)

- Hides the assertions that checks the data types of the message fields. ([#194](https://github.com/ros2/rosidl_python/issues/194))
- Service introspection ([#178](https://github.com/ros2/rosidl_python/issues/178))
- [rolling] Update maintainers - 2022-11-07 ([#189](https://github.com/ros2/rosidl_python/issues/189))
- Remove stray numpy import ([#185](https://github.com/ros2/rosidl_python/issues/185))
- man\_farmer:
  :   Fix NaN values bound numpy windows version ([#182](https://github.com/ros2/rosidl_python/issues/182))
- Allow NaN values to pass floating point bounds check. ([#167](https://github.com/ros2/rosidl_python/issues/167))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#177](https://github.com/ros2/rosidl_python/issues/177))
- Change decode error mode to replace ([#176](https://github.com/ros2/rosidl_python/issues/176))
- Merge pull request [#173](https://github.com/ros2/rosidl_python/issues/173) from ros2/quarkytale/fix\_import\_order
- fix flake
- sorting after conversion
- Revert “Use modern cmake targets to avoid absolute paths to appear in binary archives ([#160](https://github.com/ros2/rosidl_python/issues/160))” ([#166](https://github.com/ros2/rosidl_python/issues/166))
- Use modern cmake targets to avoid absolute paths to appear in binary archives ([#160](https://github.com/ros2/rosidl_python/issues/160))
- michel as author
- adding maintainer
- Contributors: Audrow Nash, Ben Wolsieffer, Brian, Cristóbal Arroyo, Dharini Dutia, Eloy Briceno, Ivan Santiago Paunovic, Jacob Perron, Tomoya Fujita, quarkytale, Øystein Sture

<a id="rosidl-generator-tests"></a>

## [rosidl\_generator\_tests](https://github.com/ros2/rosidl/tree/iron/rosidl_generator_tests/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700)) \* add service event message
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_generator\_c/cpp tests to a separate package ([#701](https://github.com/ros2/rosidl/issues/701))
- Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron

<a id="rosidl-generator-type-description"></a>

## [rosidl\_generator\_type\_description](https://github.com/ros2/rosidl/tree/iron/rosidl_generator_type_description/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- Contributors: Emerson Knapp

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/iron/rosidl_parser/CHANGELOG.rst)

- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Always include whitespace in string literals ([#688](https://github.com/ros2/rosidl/issues/688))
- Contributors: Audrow Nash, Brian, Shane Loretz

<a id="rosidl-pycommon"></a>

## [rosidl\_pycommon](https://github.com/ros2/rosidl/tree/iron/rosidl_pycommon/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Contributors: Audrow Nash, Emerson Knapp, Jacob Perron

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/iron/rosidl_runtime_c/CHANGELOG.rst)

- Dynamic Subscription (BONUS: Allocators): rosidl ([#737](https://github.com/ros2/rosidl/issues/737))
- Runtime Interface Reflection: rosidl ([#728](https://github.com/ros2/rosidl/issues/728))
- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Copied type\_description\_interfaces structs (rep2011) ([#732](https://github.com/ros2/rosidl/issues/732))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Contributors: Audrow Nash, Brian, Emerson Knapp, methylDragon

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/iron/rosidl_runtime_cpp/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Copied type\_description\_interfaces structs (rep2011) ([#732](https://github.com/ros2/rosidl/issues/732))
- Fix a few more clang analysis problems. ([#731](https://github.com/ros2/rosidl/issues/731))
- Return reference from BoundedVector::emplace\_back ([#730](https://github.com/ros2/rosidl/issues/730))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- fix conversion to ‘std::streamsize’ {aka ‘long int’} from ‘size\_t’ {aka ‘long unsigned int’} may change the sign of the result ([#715](https://github.com/ros2/rosidl/issues/715))
- Contributors: Alexander Hans, Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, ralwing

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/iron/CHANGELOG.rst)

- Replace the use \_\_slots\_\_ for the appropiate API ([#23](https://github.com/ros2/rosidl_runtime_py/issues/23))
- fix(typing): `get_interface_packages` returns a dict ([#22](https://github.com/ros2/rosidl_runtime_py/issues/22))
- [rolling] Update maintainers - 2022-11-07 ([#21](https://github.com/ros2/rosidl_runtime_py/issues/21))
- Expand timestamps for std\_msgs.msg.Header and builtin\_interfaces.msg.Time if ‘auto’ and ‘now’ are passed as values ([#19](https://github.com/ros2/rosidl_runtime_py/issues/19))
- Document a missing parameter in message\_to\_yaml. ([#18](https://github.com/ros2/rosidl_runtime_py/issues/18))
- Mirror rolling to master
- Contributors: Audrow Nash, Chris Lalancette, Eloy Briceno, Esteve Fernandez, 兰陈昕

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/iron/rosidl_typesupport_c/CHANGELOG.rst)

- Type Description Nested Support ([#141](https://github.com/ros2/rosidl_typesupport/issues/141))
- Fix rosidl\_typesupport\_c/cpp exec dependencies. ([#140](https://github.com/ros2/rosidl_typesupport/issues/140))
- Type hashes in typesupport (rep2011) ([#135](https://github.com/ros2/rosidl_typesupport/issues/135))
- Mark benchmark \_ as UNUSED. ([#134](https://github.com/ros2/rosidl_typesupport/issues/134))
- Service introspection ([#127](https://github.com/ros2/rosidl_typesupport/issues/127))
- Update rosidl\_typesupport to C++17. ([#131](https://github.com/ros2/rosidl_typesupport/issues/131))
- [rolling] Update maintainers - 2022-11-07 ([#130](https://github.com/ros2/rosidl_typesupport/issues/130))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#126](https://github.com/ros2/rosidl_typesupport/issues/126))
- [service introspection] Use stddef.h instead of cstddef ([#125](https://github.com/ros2/rosidl_typesupport/issues/125))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/iron/rosidl_typesupport_cpp/CHANGELOG.rst)

- Type Description Nested Support ([#141](https://github.com/ros2/rosidl_typesupport/issues/141))
- Fix rosidl\_typesupport\_c/cpp exec dependencies. ([#140](https://github.com/ros2/rosidl_typesupport/issues/140))
- Type hashes in typesupport (rep2011) ([#135](https://github.com/ros2/rosidl_typesupport/issues/135))
- Mark benchmark \_ as UNUSED. ([#134](https://github.com/ros2/rosidl_typesupport/issues/134))
- Service introspection ([#127](https://github.com/ros2/rosidl_typesupport/issues/127))
- Update rosidl\_typesupport to C++17. ([#131](https://github.com/ros2/rosidl_typesupport/issues/131))
- [rolling] Update maintainers - 2022-11-07 ([#130](https://github.com/ros2/rosidl_typesupport/issues/130))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#126](https://github.com/ros2/rosidl_typesupport/issues/126))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/iron/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- Type Description Nested Support ([#101](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/101))
- Type hashes on typesupport (rep2011) ([#98](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/98))
- Expose type hash to typesupport structs (rep2011) ([#95](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/95))
- Mark benchmark \_ as UNUSED. ([#96](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/96))
- Service introspection ([#92](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/92))
- Update rosidl\_typesupport\_fastrtps to C++17. ([#94](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/94))
- [rolling] Update maintainers - 2022-11-07 ([#93](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/93))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#91](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/91))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/iron/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- Type Description Nested Support ([#101](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/101))
- Type hashes on typesupport (rep2011) ([#98](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/98))
- Depend on ament\_cmake\_ros to default SHARED to ON ([#99](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/99))
- Expose type hash to typesupport structs (rep2011) ([#95](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/95))
- Mark benchmark \_ as UNUSED. ([#96](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/96))
- Service introspection ([#92](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/92))
- Update rosidl\_typesupport\_fastrtps to C++17. ([#94](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/94))
- [rolling] Update maintainers - 2022-11-07 ([#93](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/93))
- Replace rosidl\_cmake imports with rosidl\_pycommon ([#91](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/91))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron, Tyler Weaver

<a id="rosidl-typesupport-interface"></a>

## [rosidl\_typesupport\_interface](https://github.com/ros2/rosidl/tree/iron/rosidl_typesupport_interface/CHANGELOG.rst)

- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Contributors: Audrow Nash, Brian

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/iron/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Fix build export dependencies in C introspection package ([#695](https://github.com/ros2/rosidl/issues/695))
- Add namespaced ALIAS target to easily consume generated libraries via add\_subdirectory ([#605](https://github.com/ros2/rosidl/issues/605))
- Contributors: Audrow Nash, Brian, Emerson Knapp, Jacob Perron, Silvio Traversaro

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/iron/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Type Description Codegen and Typesupport (rep2011) ([#727](https://github.com/ros2/rosidl/issues/727))
- Expose type hash on typesupports (rep2011) ([#729](https://github.com/ros2/rosidl/issues/729))
- Type hash in interface codegen (rep2011) ([#722](https://github.com/ros2/rosidl/issues/722))
- Make sure to add the event message to typesupport introspection cpp. ([#724](https://github.com/ros2/rosidl/issues/724))
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Move rosidl\_cmake Python module to a new package rosidl\_pycommon ([#696](https://github.com/ros2/rosidl/issues/696)) Deprecate the Python module in rosidl\_cmake and move the implementation to the new package rosidl\_pycommon.
- Add namespaced ALIAS target to easily consume generated libraries via add\_subdirectory ([#605](https://github.com/ros2/rosidl/issues/605))
- Contributors: Audrow Nash, Brian, Chris Lalancette, Emerson Knapp, Jacob Perron, Silvio Traversaro

<a id="rosidl-typesupport-introspection-tests"></a>

## [rosidl\_typesupport\_introspection\_tests](https://github.com/ros2/rosidl/tree/iron/rosidl_typesupport_introspection_tests/CHANGELOG.rst)

- Fix a few more clang analysis problems. ([#731](https://github.com/ros2/rosidl/issues/731)) In particular, make sure to mark the fact that we are C++17 (as the emplace\_back signature changed), and also add in a few more (void)\_ for benchmark tests.
- [service introspection] generate service\_event messages ([#700](https://github.com/ros2/rosidl/issues/700))
- [rolling] Update maintainers - 2022-11-07 ([#717](https://github.com/ros2/rosidl/issues/717))
- Contributors: Audrow Nash, Brian, Chris Lalancette

<a id="rosidl-typesupport-tests"></a>

## [rosidl\_typesupport\_tests](https://github.com/ros2/rosidl_typesupport/tree/iron/rosidl_typesupport_tests/CHANGELOG.rst)

- typesupport\_tests needs to be updated to C++17 ([#137](https://github.com/ros2/rosidl_typesupport/issues/137))
- Fix Typesupport Introspection tests ([#133](https://github.com/ros2/rosidl_typesupport/issues/133))
- Make rosidl\_typesupport\_tests depend on rosidl\_generator\_cpp. ([#132](https://github.com/ros2/rosidl_typesupport/issues/132))
- Service introspection ([#127](https://github.com/ros2/rosidl_typesupport/issues/127))
- Contributors: Brian, Chris Lalancette, Cristóbal Arroyo, Lucas Wendland

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#10](https://github.com/ros2/rpyutils/issues/10))
- Mirror rolling to master
- updating maintainer
- Contributors: Audrow Nash, Dharini Dutia

<a id="rqt"></a>

## [rqt](https://github.com/ros-visualization/rqt/tree/iron/rqt/CHANGELOG.rst)

- fix build of `rqt` with `setuptools>=v61.0.0` ([#271](https://github.com/ros-visualization/rqt/issues/271))
- [rolling] Update maintainers - 2022-11-07 ([#283](https://github.com/ros-visualization/rqt/issues/283))
- Fix up the package description. ([#250](https://github.com/ros-visualization/rqt/issues/250))
- Contributors: Audrow Nash, Chris Lalancette, Daniel Reuter, Dharini Dutia, quarkytale

<a id="rqt-action"></a>

## [rqt\_action](https://github.com/ros-visualization/rqt_action/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#14](https://github.com/ros-visualization/rqt_action/issues/14))
- Small cleanups to the rqt\_action plugin ([#13](https://github.com/ros-visualization/rqt_action/issues/13))
- Mirror rolling to ros2
- Contributors: Audrow Nash, Chris Lalancette

<a id="rqt-bag"></a>

## [rqt\_bag](https://github.com/ros-visualization/rqt_bag/tree/iron/rqt_bag/CHANGELOG.rst)

- Use default storage id ([#140](https://github.com/ros-visualization/rqt_bag/issues/140))
- Use rosbag2\_py API instead of direct bag parsing
- [rolling] Update maintainers - 2022-11-07 ([#132](https://github.com/ros-visualization/rqt_bag/issues/132))
- For get\_entry\_after, bump by 1 nanosecond otherwise always get the same message equal to the timestamp
- Use rosbag2\_py.reader for all message queries, remove sqlite3 direct usage
- Cleanup for review
- Improved logging
- Use a rosbag2\_py.Reader to get bag metadata
- Disable reading from bag while recording - use direct caching to index for timeline
- Increase publishing checkbox size ([#122](https://github.com/ros-visualization/rqt_bag/issues/122))
- Fix toggle thumbnails button ([#117](https://github.com/ros-visualization/rqt_bag/issues/117))
- ensure data types match what PyQt expects ([#118](https://github.com/ros-visualization/rqt_bag/issues/118))
- Visualize topics being published and highlight topic being selected ([#116](https://github.com/ros-visualization/rqt_bag/issues/116))
- Be able to scroll up and down, not only zoom-in and out the timeline ([#114](https://github.com/ros-visualization/rqt_bag/issues/114))
- [Fixes] Fix crash when no qos metadata, make scroll bar appear if needed, add gitignore ([#113](https://github.com/ros-visualization/rqt_bag/issues/113))
- Fix the types being passed into QFont and QColor. ([#109](https://github.com/ros-visualization/rqt_bag/issues/109))
- Fix tuples for bisect calls ([#67](https://github.com/ros-visualization/rqt_bag/issues/67)) ([#76](https://github.com/ros-visualization/rqt_bag/issues/76))
- fix long topic names ([#114](https://github.com/ros-visualization/rqt_common_plugins/issues/114))
- fix zoom behavior ([#76](https://github.com/ros-visualization/rqt_common_plugins/issues/76))
- Contributors: Audrow Nash, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Kenji Brameld, Yadunund

<a id="rqt-bag-plugins"></a>

## [rqt\_bag\_plugins](https://github.com/ros-visualization/rqt_bag/tree/iron/rqt_bag_plugins/CHANGELOG.rst)

- Changes the use of \_\_slots\_\_ for the field and field type getter ([#138](https://github.com/ros-visualization/rqt_bag/issues/138))
- [rolling] Update maintainers - 2022-11-07 ([#132](https://github.com/ros-visualization/rqt_bag/issues/132))
- Contributors: Audrow Nash, Eloy Briceno

<a id="rqt-console"></a>

## [rqt\_console](https://github.com/ros-visualization/rqt_console/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#39](https://github.com/ros-visualization/rqt_console/issues/39))
- added new maintainer
- Contributors: Arne Hitzmann, Audrow Nash

<a id="rqt-graph"></a>

## [rqt\_graph](https://github.com/ros-visualization/rqt_graph/tree/iron/CHANGELOG.rst)

- Refresh rosgraph when params checkbox is clicked ([#87](https://github.com/ros-visualization/rqt_graph/issues/87))
- [rolling] Update maintainers - 2022-11-07 ([#83](https://github.com/ros-visualization/rqt_graph/issues/83))
- Minor cleanup ([#80](https://github.com/ros-visualization/rqt_graph/issues/80))
- Mirror rolling to galactic-devel
- graph load/save into DOT file corrections for py3 ([#78](https://github.com/ros-visualization/rqt_graph/issues/78))
- Remove repeated prefixes from buttons
- Contributors: Audrow Nash, Chris Lalancette, David V. Lu!!, Yadunund, mergify[bot]

<a id="rqt-gui"></a>

## [rqt\_gui](https://github.com/ros-visualization/rqt/tree/iron/rqt_gui/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#283](https://github.com/ros-visualization/rqt/issues/283))
- Display basic help information when no plugins are loaded ([#268](https://github.com/ros-visualization/rqt/issues/268))
- Contributors: Audrow Nash, Dharini Dutia, Michael Jeronimo, quarkytale

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/iron/rqt_gui_cpp/CHANGELOG.rst)

- Update rqt to C++17. ([#285](https://github.com/ros-visualization/rqt/issues/285))
- [rolling] Update maintainers - 2022-11-07 ([#283](https://github.com/ros-visualization/rqt/issues/283))
- Contributors: Audrow Nash, Chris Lalancette, Dharini Dutia, quarkytale

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/iron/rqt_gui_py/CHANGELOG.rst)

- Fix an exception raised when terminating with Ctrl+c ([#292](https://github.com/ros-visualization/rqt/issues/292))
- [rolling] Update maintainers - 2022-11-07 ([#283](https://github.com/ros-visualization/rqt/issues/283))
- Contributors: Audrow Nash, Chen Lihui, Dharini Dutia, quarkytale

<a id="rqt-msg"></a>

## [rqt\_msg](https://github.com/ros-visualization/rqt_msg/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#17](https://github.com/ros-visualization/rqt_msg/issues/17))
- Contributors: Audrow Nash

<a id="rqt-plot"></a>

## [rqt\_plot](https://github.com/ros-visualization/rqt_plot/tree/iron/CHANGELOG.rst)

- Fix regression from #87 ([#91](https://github.com/ros-visualization/rqt_plot/issues/91))
- Changes the use of \_\_slots\_\_ for the field and field type getter ([#87](https://github.com/ros-visualization/rqt_plot/issues/87))
- [rolling] Update maintainers - 2022-11-07 ([#83](https://github.com/ros-visualization/rqt_plot/issues/83))
- Fix fixed-size Array visualization ([#81](https://github.com/ros-visualization/rqt_plot/issues/81))
- Contributors: Audrow Nash, Eloy Briceno, Jacob Perron, Michael Jeronimo, Yadunund

<a id="rqt-publisher"></a>

## [rqt\_publisher](https://github.com/ros-visualization/rqt_publisher/tree/iron/CHANGELOG.rst)

- Changes the use of \_\_slots\_\_ for the field and field type getter
- [rolling] Update maintainers - 2022-11-07 ([#36](https://github.com/ros-visualization/rqt_publisher/issues/36))
- Minor cleanups in rqt\_publisher for ROS 2 ([#35](https://github.com/ros-visualization/rqt_publisher/issues/35))
- Delete sync to foxy-devel workflow
- Merge pull request [#33](https://github.com/ros-visualization/rqt_publisher/issues/33) from NBadyal/improve-evaluation-of-types
- Use regex matching to strip errors from input
- Change slot\_type verification strategy
- Mirror rolling to foxy-devel
- Contributors: Audrow Nash, Chris Lalancette, Geoffrey Biggs, Michael Jeronimo, Nicholas Badyal, Voldivh

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/iron/rqt_py_common/CHANGELOG.rst)

- Changes the use of \_\_slots\_\_ for the field and field type getter ([#289](https://github.com/ros-visualization/rqt/issues/289))
- [rolling] Update maintainers - 2022-11-07 ([#283](https://github.com/ros-visualization/rqt/issues/283))
- Contributors: Audrow Nash, Dharini Dutia, Eloy Briceno, quarkytale

<a id="rqt-py-console"></a>

## [rqt\_py\_console](https://github.com/ros-visualization/rqt_py_console/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#13](https://github.com/ros-visualization/rqt_py_console/issues/13))
- Contributors: Audrow Nash, Jacob Perron

<a id="rqt-reconfigure"></a>

## [rqt\_reconfigure](https://github.com/ros-visualization/rqt_reconfigure/tree/iron/CHANGELOG.rst)

- reorder imports to fix flake8 warning ([#129](https://github.com/ros-visualization/rqt_reconfigure/issues/129))
- Fixed validator locale when float value is not bound in a range. ([#121](https://github.com/ros-visualization/rqt_reconfigure/issues/121))
- get parameter type from descriptor
- [rolling] Update maintainers - 2022-11-07 ([#122](https://github.com/ros-visualization/rqt_reconfigure/issues/122))
- Cleanup mislabeled BSD license ([#66](https://github.com/ros-visualization/rqt_reconfigure/issues/66))
- Add support for array types ([#108](https://github.com/ros-visualization/rqt_reconfigure/issues/108))
- Fix float slider step size ([#117](https://github.com/ros-visualization/rqt_reconfigure/issues/117))
- update maintainer
- Fixed package to run with ros2 run ([#81](https://github.com/ros-visualization/rqt_reconfigure/issues/81))
- fix updating range limits ([#108](https://github.com/ros-visualization/rqt_common_plugins/issues/108))
- Improvement; “GUI hangs for awhile or completely, when any one of nodes doesn’t return any value” ([#81](https://github.com/ros-visualization/rqt_common_plugins/issues/81))
- Contributors: Aris Synodinos, Audrow Nash, Christian Rauch, Dharini Dutia, Florian Vahl, Jacob Perron, Shrijit Singh, Tully Foote, quarkytale

<a id="rqt-service-caller"></a>

## [rqt\_service\_caller](https://github.com/ros-visualization/rqt_service_caller/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#25](https://github.com/ros-visualization/rqt_service_caller/issues/25))
- Contributors: Audrow Nash, Jacob Perron

<a id="rqt-shell"></a>

## [rqt\_shell](https://github.com/ros-visualization/rqt_shell/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#17](https://github.com/ros-visualization/rqt_shell/issues/17))
- Contributors: Audrow Nash, Jacob Perron

<a id="rqt-srv"></a>

## [rqt\_srv](https://github.com/ros-visualization/rqt_srv/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#10](https://github.com/ros-visualization/rqt_srv/issues/10))
- Contributors: Audrow Nash, Jacob Perron

<a id="rqt-topic"></a>

## [rqt\_topic](https://github.com/ros-visualization/rqt_topic/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#43](https://github.com/ros-visualization/rqt_topic/issues/43))
- Implement bandwidth monitoring ([#40](https://github.com/ros-visualization/rqt_topic/issues/40))
- Fix the display of array type elements. ([#41](https://github.com/ros-visualization/rqt_topic/issues/41))
- Fix removal of topics while they are being monitored. ([#39](https://github.com/ros-visualization/rqt_topic/issues/39))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/iron/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Use unified approach for checking the existence of environment variables ([#117](https://github.com/ros2/rmw_connextdds/issues/117))
- Contributors: Christopher Wecht

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/iron/rttest/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#121](https://github.com/ros2/realtime_support/issues/121))
- Addressing issues found in Humble testing ([#116](https://github.com/ros2/realtime_support/issues/116))
- Contributors: Audrow Nash, Michael Carroll

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/iron/rviz2/CHANGELOG.rst)

- Make rviz1\_to\_rviz2.py accept configs with missing values ([#945](https://github.com/ros2/rviz/issues/945))
- Update rviz to C++17. ([#939](https://github.com/ros2/rviz/issues/939))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Add rviz1\_to\_rviz2.py conversion script ([#882](https://github.com/ros2/rviz/issues/882))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="rviz-assimp-vendor"></a>

## [rviz\_assimp\_vendor](https://github.com/ros2/rviz/tree/iron/rviz_assimp_vendor/CHANGELOG.rst)

- If vendored assimp is present, always prefer that ([#970](https://github.com/ros2/rviz/issues/970))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#898](https://github.com/ros2/rviz/issues/898))
- Contributors: Audrow Nash, Cristóbal Arroyo, Scott K Logan

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/iron/rviz_common/CHANGELOG.rst)

- Update Frame shortcut ([#958](https://github.com/ros2/rviz/issues/958)) \* Update Frame shortcut
- Update rviz to C++17. ([#939](https://github.com/ros2/rviz/issues/939))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Remove YAML\_CPP\_DLL define ([#831](https://github.com/ros2/rviz/issues/831))
- Document getTransform() time behavior ([#893](https://github.com/ros2/rviz/issues/893))
- Ogre 1.12.10 upgrade ([#878](https://github.com/ros2/rviz/issues/878))
- Add RVIZ\_COMMON\_PUBLIC macro ([#865](https://github.com/ros2/rviz/issues/865))
- Add time jump handler ([#752](https://github.com/ros2/rviz/issues/752)) ([#791](https://github.com/ros2/rviz/issues/791))
- Make sure not to dereference a null Renderable pointer. ([#850](https://github.com/ros2/rviz/issues/850))
- Contributors: Akash, Audrow Nash, Chris Lalancette, David V. Lu!!, Kenji Brameld, Marcel Zeilinger, Shane Loretz, juchajam

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/iron/rviz_default_plugins/CHANGELOG.rst)

- Fix ODR errors with gmock ([#967](https://github.com/ros2/rviz/issues/967))
- Update Frame shortcut ([#958](https://github.com/ros2/rviz/issues/958))
- point\_marker: fix bug where the number of rendered points accumulates over time ([#949](https://github.com/ros2/rviz/issues/949))
- Update rviz to C++17. ([#939](https://github.com/ros2/rviz/issues/939))
- Fix tolerance calculation precision ([#934](https://github.com/ros2/rviz/issues/934))
- Fix MeshResourceMarker for mesh with color-based embedded material ([#928](https://github.com/ros2/rviz/issues/928))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Add Map Display binary option ([#846](https://github.com/ros2/rviz/issues/846))
- Delete frame\_locked\_markers when reusing marker ([#907](https://github.com/ros2/rviz/issues/907))
- Consider region of interest in CameraDisplay ([#864](https://github.com/ros2/rviz/issues/864))
- std::copy fix - OccupancyGridUpdate - Data is not being processed correctly ([#895](https://github.com/ros2/rviz/issues/895))
- Set error status when duplicate markers are in the same MarkerArray ([#891](https://github.com/ros2/rviz/issues/891))
- Make Axes display use latest transform ([#892](https://github.com/ros2/rviz/issues/892))
- Show link names in inertia error message ([#874](https://github.com/ros2/rviz/issues/874))
- Ogre 1.12.10 upgrade ([#878](https://github.com/ros2/rviz/issues/878))
- Use make\_shared to construct PointCloud2 ([#869](https://github.com/ros2/rviz/issues/869))
- Fix include order ([#858](https://github.com/ros2/rviz/issues/858))
- Contributors: AndreasR30, Audrow Nash, Chris Lalancette, David V. Lu!!, Eric, Hunter L. Allen, Jacob Perron, Kenji Brameld, Patrick Roncagliolo, Shane Loretz, Timon Engelke, Xavier BROQUERE, Xenofon Karamanos, methylDragon

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/iron/rviz_ogre_vendor/CHANGELOG.rst)

- Fix build failures on macOS + Apple Silicon ([#944](https://github.com/ros2/rviz/issues/944))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Remove broken rviz\_ogre\_vendor::RenderSystem\_GL target ([#920](https://github.com/ros2/rviz/issues/920))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#898](https://github.com/ros2/rviz/issues/898))
- Ogre 1.12.10 upgrade ([#878](https://github.com/ros2/rviz/issues/878))
- Make resource file paths relative ([#862](https://github.com/ros2/rviz/issues/862))
- Use CMAKE\_STAGING\_PREFIX for staging OGRE installation ([#861](https://github.com/ros2/rviz/issues/861))
- Contributors: Audrow Nash, Cristóbal Arroyo, Kenji Brameld, Scott K Logan, Shane Loretz, Yadu

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/iron/rviz_rendering/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- add test to ensure binary STL files from SOLIDWORKS get imported without a warning ([#917](https://github.com/ros2/rviz/issues/917))
- Ogre 1.12.10 upgrade ([#878](https://github.com/ros2/rviz/issues/878))
- Stop using glsl150 resources for now. ([#851](https://github.com/ros2/rviz/issues/851))
- Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/iron/rviz_rendering_tests/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- add test to ensure binary STL files from SOLIDWORKS get imported without a warning ([#917](https://github.com/ros2/rviz/issues/917))
- Contributors: Audrow Nash, Kenji Brameld

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/iron/rviz_visual_testing_framework/CHANGELOG.rst)

- Update rviz to C++17. ([#939](https://github.com/ros2/rviz/issues/939))
- [rolling] Update maintainers - 2022-11-07 ([#923](https://github.com/ros2/rviz/issues/923))
- Ogre 1.12.10 upgrade ([#878](https://github.com/ros2/rviz/issues/878))
- Contributors: Audrow Nash, Chris Lalancette, Kenji Brameld

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/iron/sensor_msgs/CHANGELOG.rst)

- update YUV format codes and documentation ([#214](https://github.com/ros2/common_interfaces/issues/214))
- sensor\_msgs/Range lacks variance field ([#181](https://github.com/ros2/common_interfaces/issues/181))
- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Replaced non-ASCII dash symbol with ASCII dash ([#208](https://github.com/ros2/common_interfaces/issues/208))
- Add NV21 and NV24 to colour formats ([#205](https://github.com/ros2/common_interfaces/issues/205))
- Update BatteryState.msg ([#206](https://github.com/ros2/common_interfaces/issues/206))
- use regex for matching cv types ([#202](https://github.com/ros2/common_interfaces/issues/202))
- Fix outdated file path for image\_encodings ([#200](https://github.com/ros2/common_interfaces/issues/200))
- Use uint32\_t for pointcloud2 resize method ([#195](https://github.com/ros2/common_interfaces/issues/195))
- Retain width and height after resize for master ([#193](https://github.com/ros2/common_interfaces/issues/193))
- Contributors: Audrow Nash, Borong Yuan, Chris Lalancette, Christian Rauch, El Jawad Alaa, Geoffrey Biggs, Ivan Zatevakhin, Kenji Brameld, Tianyu Li

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/iron/sensor_msgs_py/CHANGELOG.rst)

- Add missing dep for sensor\_msgs\_py ([#217](https://github.com/ros2/common_interfaces/issues/217))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Add support for non standard point step sizes ([#199](https://github.com/ros2/common_interfaces/issues/199))
- Remove reference to old implementation ([#198](https://github.com/ros2/common_interfaces/issues/198))
- Contributors: Audrow Nash, Florian Vahl, Yadu

<a id="service-msgs"></a>

## [service\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/service_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- Add service\_msgs package ([#143](https://github.com/ros2/rcl_interfaces/issues/143))
- Contributors: Brian, Chris Lalancette

<a id="shape-msgs"></a>

## [shape\_msgs](https://github.com/ros2/common_interfaces/tree/iron/shape_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Fix SolidPrimitive.msg to contain a single Polygon ([#189](https://github.com/ros2/common_interfaces/issues/189))
- Contributors: Audrow Nash, Chris Lalancette, M. Fatih Cırıt

<a id="shared-queues-vendor"></a>

## [shared\_queues\_vendor](https://github.com/ros2/rosbag2/tree/iron/shared_queues_vendor/CHANGELOG.rst)

- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#1084](https://github.com/ros2/rosbag2/issues/1084))
- Contributors: Cristóbal Arroyo, Michael Orlov

<a id="spdlog-vendor"></a>

## [spdlog\_vendor](https://github.com/ros2/spdlog_vendor/tree/iron/CHANGELOG.rst)

- Update to spdlog 1.9.2 ([#33](https://github.com/ros2/spdlog_vendor/issues/33))
- [rolling] Update maintainers - 2022-11-07 ([#31](https://github.com/ros2/spdlog_vendor/issues/31))
- Update to spdlog 1.9.1 ([#27](https://github.com/ros2/spdlog_vendor/issues/27))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#30](https://github.com/ros2/spdlog_vendor/issues/30))
- build shared lib only if BUILD\_SHARED\_LIBS is set ([#29](https://github.com/ros2/spdlog_vendor/issues/29))
- Mirror rolling to master
- xml tag order
- updating maintainer
- Contributors: Audrow Nash, Chris Lalancette, Cristóbal Arroyo, Dharini Dutia, Scott K Logan, hannes09

<a id="sqlite3-vendor"></a>

## [sqlite3\_vendor](https://github.com/ros2/rosbag2/tree/iron/sqlite3_vendor/CHANGELOG.rst)

- Update to sqlite3 3.37.2 ([#1274](https://github.com/ros2/rosbag2/issues/1274)) This matches version distributed in Ubuntu Jammy.
- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#1084](https://github.com/ros2/rosbag2/issues/1084))
- Contributors: Cristóbal Arroyo, Michael Orlov, Scott K Logan

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/iron/sros2/CHANGELOG.rst)

- Fix SSH commands in SROS2\_Linux.md ([#286](https://github.com/ros2/sros2/issues/286))
- Make type of get\_package\_share\_directory apparent for sphinx ([#284](https://github.com/ros2/sros2/issues/284))
- Contributors: Boris Boutillier, Yadu

<a id="statistics-msgs"></a>

## [statistics\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/statistics_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Contributors: Audrow Nash, Chris Lalancette

<a id="std-msgs"></a>

## [std\_msgs](https://github.com/ros2/common_interfaces/tree/iron/std_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="std-srvs"></a>

## [std\_srvs](https://github.com/ros2/common_interfaces/tree/iron/std_srvs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="stereo-msgs"></a>

## [stereo\_msgs](https://github.com/ros2/common_interfaces/tree/iron/stereo_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tango-icons-vendor"></a>

## [tango\_icons\_vendor](https://github.com/ros-visualization/tango_icons_vendor/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#10](https://github.com/ros-visualization/tango_icons_vendor/issues/10))
- Mirror rolling to master
- Contributors: Audrow Nash

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/iron/test_cli/CHANGELOG.rst)

- Update the system tests to C++17. ([#510](https://github.com/ros2/system_tests/issues/510))
- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Contributors: Audrow Nash, Chris Lalancette

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/iron/test_cli_remapping/CHANGELOG.rst)

- Update the system tests to C++17. ([#510](https://github.com/ros2/system_tests/issues/510))
- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Contributors: Audrow Nash, Chris Lalancette

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/iron/test_communication/CHANGELOG.rst)

- Update the system tests to C++17. ([#510](https://github.com/ros2/system_tests/issues/510))
- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Revert “Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))” ([#504](https://github.com/ros2/system_tests/issues/504))
- Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))
- Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki, William Woodall

<a id="test-interface-files"></a>

## [test\_interface\_files](https://github.com/ros2/test_interface_files/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#21](https://github.com/ros2/test_interface_files/issues/21))
- Mirror rolling to master
- Contributors: Audrow Nash

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/iron/test_launch_ros/CHANGELOG.rst)

- Enable document generation using rosdoc2 ([#359](https://github.com/ros2/launch_ros/issues/359))
- Fix normalize\_parameters\_dict for multiple nodes in the same namespace ([#347](https://github.com/ros2/launch_ros/issues/347))
- Implement None check for ComposableNodeContainer ([#341](https://github.com/ros2/launch_ros/issues/341))
- Add LifecyleTransition action ([#317](https://github.com/ros2/launch_ros/issues/317))
- Ensure load\_composable\_nodes respects condition ([#339](https://github.com/ros2/launch_ros/issues/339))
- [rolling] Update maintainers - 2022-11-07 ([#331](https://github.com/ros2/launch_ros/issues/331))
- RosTimer -> ROSTimer and PushRosNamespace -> PushROSNamespace, to follow PEP8 ([#326](https://github.com/ros2/launch_ros/issues/326))
- add SetROSLogDir action ([#325](https://github.com/ros2/launch_ros/issues/325))
- Support default values in parameter substitution ([#313](https://github.com/ros2/launch_ros/issues/313))
- Run condition for composable nodes ([#311](https://github.com/ros2/launch_ros/issues/311))
- Load composable nodes in sequence ([#315](https://github.com/ros2/launch_ros/issues/315))
- Contributors: Aditya Pande, Alexey Merzlyakov, Audrow Nash, Christoph Hellmann Santos, Kenji Miyake, Shane Loretz, William Woodall, Yadu, methylDragon

<a id="test-launch-testing"></a>

## [test\_launch\_testing](https://github.com/ros2/launch/tree/iron/test_launch_testing/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#671](https://github.com/ros2/launch/issues/671))
- Contributors: Audrow Nash

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/iron/test_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/rcl_interfaces/issues/215)) ([#151](https://github.com/ros2/rcl_interfaces/issues/151))
- [rolling] Update maintainers - 2022-11-07 ([#150](https://github.com/ros2/rcl_interfaces/issues/150))
- Depend on rosidl\_core\_generators for packages required by actions ([#144](https://github.com/ros2/rcl_interfaces/issues/144))
- Make the functions in the header static inline ([#140](https://github.com/ros2/rcl_interfaces/issues/140))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="test-osrf-testing-tools-cpp"></a>

## [test\_osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/iron/test_osrf_testing_tools_cpp/CHANGELOG.rst)

- Changing C++ Compile Version ([#76](https://github.com/osrf/osrf_testing_tools_cpp/issues/76))
- Update maintainers ([#74](https://github.com/osrf/osrf_testing_tools_cpp/issues/74))
- Contributors: Audrow Nash, Lucas Wendland

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/iron/test_quality_of_service/CHANGELOG.rst)

- Fix ODR errors with gtest ([#514](https://github.com/ros2/system_tests/issues/514))
- Avoid flaky test ([#513](https://github.com/ros2/system_tests/issues/513))
- Update the system tests to C++17. ([#510](https://github.com/ros2/system_tests/issues/510))
- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Pass rclcpp::QoS to create\_service ([#507](https://github.com/ros2/system_tests/issues/507))
- Pass rclcpp::QoS to create\_client ([#506](https://github.com/ros2/system_tests/issues/506))
- Remove Werror from test\_quality\_of\_service. ([#503](https://github.com/ros2/system_tests/issues/503))
- Revert “Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))” ([#504](https://github.com/ros2/system_tests/issues/504))
- Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))
- Add tests for ‘best available’ QoS policies ([#501](https://github.com/ros2/system_tests/issues/501))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Hubert Liberacki, Jacob Perron, Shane Loretz, William Woodall, methylDragon

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/iron/test_rclcpp/CHANGELOG.rst)

- Update the system tests to C++17. ([#510](https://github.com/ros2/system_tests/issues/510))
- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Pass rclcpp::QoS to create\_service ([#507](https://github.com/ros2/system_tests/issues/507))
- Pass rclcpp::QoS to create\_client ([#506](https://github.com/ros2/system_tests/issues/506))
- Revert “Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))” ([#504](https://github.com/ros2/system_tests/issues/504))
- Replace deprecated spin\_until\_future\_complete with spin\_until\_complete ([#499](https://github.com/ros2/system_tests/issues/499))
- Contributors: Audrow Nash, Chris Lalancette, Hubert Liberacki, Shane Loretz, William Woodall

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/iron/test_rmw_implementation/CHANGELOG.rst)

- Add tests for rmw matched event ([#216](https://github.com/ros2/rmw_implementation/issues/216))
- Update rmw\_implementation to C++17. ([#214](https://github.com/ros2/rmw_implementation/issues/214))
- [rolling] Update maintainers - 2022-11-07 ([#212](https://github.com/ros2/rmw_implementation/issues/212))
- Add rmw\_get\_gid\_for\_client & tests ([#206](https://github.com/ros2/rmw_implementation/issues/206))
- Contributors: Audrow Nash, Barry Xu, Brian, Chris Lalancette

<a id="test-ros2trace"></a>

## [test\_ros2trace](https://github.com/ros2/ros2_tracing/tree/iron/test_ros2trace/CHANGELOG.rst)

- Move ros2trace tests to new test\_ros2trace package ([#63](https://github.com/ros2/ros2_tracing/issues/63))
- Contributors: Christophe Bedard

<a id="test-security"></a>

## [test\_security](https://github.com/ros2/system_tests/tree/iron/test_security/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#509](https://github.com/ros2/system_tests/issues/509))
- Contributors: Audrow Nash

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/iron/test_tf2/CHANGELOG.rst)

- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Chris Lalancette

<a id="test-tracetools"></a>

## [test\_tracetools](https://github.com/ros2/ros2_tracing/tree/iron/test_tracetools/CHANGELOG.rst)

- Disable tracing on Android ([#72](https://github.com/ros2/ros2_tracing/issues/72))
- Add intra-process tracepoints ([#30](https://github.com/ros2/ros2_tracing/issues/30))
- Allow requiring minimum lttng package version for is\_lttng\_installed ([#59](https://github.com/ros2/ros2_tracing/issues/59))
- Disable tracing on macOS ([#53](https://github.com/ros2/ros2_tracing/issues/53))
- Include tracepoints by default on Linux ([#31](https://github.com/ros2/ros2_tracing/issues/31))
- Fix memory leak in tracetools::get\_symbol() ([#43](https://github.com/ros2/ros2_tracing/issues/43))
- Update tracing to C++17. ([#33](https://github.com/ros2/ros2_tracing/issues/33))
- Contributors: Chris Lalancette, Christophe Bedard, Przemysław Dąbrowski, ymski

<a id="test-tracetools-launch"></a>

## [test\_tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/iron/test_tracetools_launch/CHANGELOG.rst)

- Error out if trace already exists unless ‘append’ option is used ([#58](https://github.com/ros2/ros2_tracing/issues/58))
- Make subbuffer size configurable with Trace action ([#51](https://github.com/ros2/ros2_tracing/issues/51))
- Allow requiring minimum lttng package version for is\_lttng\_installed ([#59](https://github.com/ros2/ros2_tracing/issues/59))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#50](https://github.com/ros2/ros2_tracing/issues/50))
- Contributors: Christophe Bedard, Christopher Wecht, Yadu

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/iron/tf2/CHANGELOG.rst)

- Fix error code returned in BufferCore::walkToTopParent ([#602](https://github.com/ros2/geometry2/issues/602))
- Depend on ament\_cmake\_ros to default SHARED to ON ([#591](https://github.com/ros2/geometry2/issues/591))
- Fix a potential crash in TimeCache::findClosest ([#592](https://github.com/ros2/geometry2/issues/592))
- Extend TimeCache API to provide rich ExtrapolationException infos ([#586](https://github.com/ros2/geometry2/issues/586))
- Update geometry2 to C++17 ([#584](https://github.com/ros2/geometry2/issues/584))
- Include required header Scalar.h ([#559](https://github.com/ros2/geometry2/issues/559))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Chris Lalancette, Patrick Roncagliolo, Shane Loretz, Tyler Weaver

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/iron/tf2_bullet/CHANGELOG.rst)

- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/iron/tf2_eigen/CHANGELOG.rst)

- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/iron/tf2_eigen_kdl/CHANGELOG.rst)

- Update geometry2 to C++17 ([#584](https://github.com/ros2/geometry2/issues/584))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Use orocos\_kdl\_vendor and orocos-kdl target ([#534](https://github.com/ros2/geometry2/issues/534))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/iron/tf2_geometry_msgs/CHANGELOG.rst)

- Add do\_transform\_polygon\_stamped ([#582](https://github.com/ros2/geometry2/issues/582))
- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Add torque due to force offset ([#538](https://github.com/ros2/geometry2/issues/538))
- Use orocos\_kdl\_vendor and orocos-kdl target ([#534](https://github.com/ros2/geometry2/issues/534))
- Contributors: Audrow Nash, Chris Lalancette, Paul Gesel, Scott K Logan, Tony Najjar

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/iron/tf2_kdl/CHANGELOG.rst)

- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Use orocos\_kdl\_vendor and orocos-kdl target ([#534](https://github.com/ros2/geometry2/issues/534))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

<a id="tf2-msgs"></a>

## [tf2\_msgs](https://github.com/ros2/geometry2/tree/iron/tf2_msgs/CHANGELOG.rst)

- Update geometry2 to C++17 ([#584](https://github.com/ros2/geometry2/issues/584))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Remove action\_msgs dependency ([#547](https://github.com/ros2/geometry2/issues/547))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/iron/tf2_py/CHANGELOG.rst)

- Update geometry2 to C++17 ([#584](https://github.com/ros2/geometry2/issues/584))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/iron/tf2_ros/CHANGELOG.rst)

- Destroy callback group before node ([#595](https://github.com/ros2/geometry2/issues/595))
- Enable TransformListener node-based constructor in Intra-process enabled components ([#572](https://github.com/ros2/geometry2/issues/572))
- Fix use-after-free bug in BufferServer::cancelCB ([#579](https://github.com/ros2/geometry2/issues/579))
- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- add constructor to static tf broadcaster accepting node interfaces ([#576](https://github.com/ros2/geometry2/issues/576))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Switching from sstream to c string formatting to fix ros arg issue ([#557](https://github.com/ros2/geometry2/issues/557))
- allow construction of tf broadcaster from node object (not a pointer) ([#555](https://github.com/ros2/geometry2/issues/555))
- Allow to construct `TransformBroadcaster` and `TransformListener` from node interfaces ([#552](https://github.com/ros2/geometry2/issues/552))
- Suppress spam from calling canTransform ([#529](https://github.com/ros2/geometry2/issues/529))
- Contributors: Alberto Soragna, Alexander Hans, Audrow Nash, Chris Lalancette, Gonzo, Michael Carroll, Patrick Roncagliolo

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/iron/tf2_ros_py/CHANGELOG.rst)

- Update sys.path with wokring directory ([#594](https://github.com/ros2/geometry2/issues/594))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#587](https://github.com/ros2/geometry2/issues/587))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Use pytest rather than unittest to enable repeat ([#558](https://github.com/ros2/geometry2/issues/558))
- Contributors: Audrow Nash, Michael Carroll, Yadu

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/iron/tf2_sensor_msgs/CHANGELOG.rst)

- Update the demos to C++17. ([#578](https://github.com/ros2/geometry2/issues/578))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- feat: export tf2 sensor msgs target ([#536](https://github.com/ros2/geometry2/issues/536))
- tf2\_sensor\_msgs find the right Python executable. ([#525](https://github.com/ros2/geometry2/issues/525))
- Add missing ament\_cmake\_pytest package needed because of newly-enabled test ([#520](https://github.com/ros2/geometry2/issues/520))
- Port point cloud transformation to numpy ([#507](https://github.com/ros2/geometry2/issues/507))
- Contributors: Audrow Nash, Chris Lalancette, Daisuke Nishimatsu, Florian Vahl, Jorge Perez, Michael Jeronimo

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/iron/tf2_tools/CHANGELOG.rst)

- Enable document generation using rosdoc2 for ament\_python pkgs ([#587](https://github.com/ros2/geometry2/issues/587))
- Update maintainers ([#560](https://github.com/ros2/geometry2/issues/560))
- Contributors: Audrow Nash, Yadu

<a id="tlsf"></a>

## [tlsf](https://github.com/ros2/tlsf/tree/iron/tlsf/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#13](https://github.com/ros2/tlsf/issues/13))
- Update maintainers ([#12](https://github.com/ros2/tlsf/issues/12))
- Contributors: Audrow Nash, methylDragon

<a id="tlsf-cpp"></a>

## [tlsf\_cpp](https://github.com/ros2/realtime_support/tree/iron/tlsf_cpp/CHANGELOG.rst)

- Update realtime support to C++17. ([#122](https://github.com/ros2/realtime_support/issues/122))
- [rolling] Update maintainers - 2022-11-07 ([#121](https://github.com/ros2/realtime_support/issues/121))
- Addressing issues found in Humble testing ([#116](https://github.com/ros2/realtime_support/issues/116))
- Contributors: Audrow Nash, Chris Lalancette, Michael Carroll

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/iron/topic_monitor/CHANGELOG.rst)

- update launch file name format to match documentation ([#588](https://github.com/ros2/demos/issues/588))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Patrick Wspanialy

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/iron/topic_statistics_demo/CHANGELOG.rst)

- Update the demos to C++17. ([#594](https://github.com/ros2/demos/issues/594))
- [rolling] Update maintainers - 2022-11-07 ([#589](https://github.com/ros2/demos/issues/589))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tracetools"></a>

## [tracetools](https://github.com/ros2/ros2_tracing/tree/iron/tracetools/CHANGELOG.rst)

- Disable tracing on Android ([#72](https://github.com/ros2/ros2_tracing/issues/72))
- Add intra-process tracepoints ([#30](https://github.com/ros2/ros2_tracing/issues/30))
- Improve tracetools rosdoc2/doxygen output ([#57](https://github.com/ros2/ros2_tracing/issues/57))
- Update README and other documentation ([#55](https://github.com/ros2/ros2_tracing/issues/55))
- Disable tracing on macOS ([#53](https://github.com/ros2/ros2_tracing/issues/53))
- Include tracepoints by default on Linux ([#31](https://github.com/ros2/ros2_tracing/issues/31))
- Explicitly link against dl for dladdr() ([#48](https://github.com/ros2/ros2_tracing/issues/48))
- Fix memory leak in tracetools::get\_symbol() ([#43](https://github.com/ros2/ros2_tracing/issues/43))
- Add TRACEPOINT\_ENABLED() and DO\_TRACEPOINT() macros ([#46](https://github.com/ros2/ros2_tracing/issues/46))
- Update tracing to C++17. ([#33](https://github.com/ros2/ros2_tracing/issues/33))
- Add new rclcpp\_subscription\_init tracepoint to support new intra-process comms
- Contributors: Chris Lalancette, Christophe Bedard, Przemysław Dąbrowski, ymski

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/iron/tracetools_launch/CHANGELOG.rst)

- Error out if trace already exists unless ‘append’ option is used ([#58](https://github.com/ros2/ros2_tracing/issues/58))
- Improve ‘ros2 trace’ command error handling & add end-to-end tests ([#54](https://github.com/ros2/ros2_tracing/issues/54))
- Make subbuffer size configurable with Trace action ([#51](https://github.com/ros2/ros2_tracing/issues/51))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#50](https://github.com/ros2/ros2_tracing/issues/50))
- Remove deprecated context\_names parameter ([#38](https://github.com/ros2/ros2_tracing/issues/38))
- Contributors: Christophe Bedard, Christopher Wecht, Yadu

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://github.com/ros2/ros2_tracing/tree/iron/tracetools_trace/CHANGELOG.rst)

- Error out if trace already exists unless ‘append’ option is used ([#58](https://github.com/ros2/ros2_tracing/issues/58))
- Improve ‘ros2 trace’ command error handling & add end-to-end tests ([#54](https://github.com/ros2/ros2_tracing/issues/54))
- Make subbuffer size configurable with Trace action ([#51](https://github.com/ros2/ros2_tracing/issues/51))
- Add intra-process tracepoints ([#30](https://github.com/ros2/ros2_tracing/issues/30))
- Allow requiring minimum lttng package version for is\_lttng\_installed ([#59](https://github.com/ros2/ros2_tracing/issues/59))
- Include tracepoints by default on Linux ([#31](https://github.com/ros2/ros2_tracing/issues/31))
- Enable document generation using rosdoc2 for ament\_python pkgs ([#50](https://github.com/ros2/ros2_tracing/issues/50))
- Replace distutils.version.StrictVersion with packaging.version.Version ([#42](https://github.com/ros2/ros2_tracing/issues/42))
- Remove deprecated context\_names parameter ([#38](https://github.com/ros2/ros2_tracing/issues/38))
- Contributors: Christophe Bedard, Christopher Wecht, Yadu, ymski

<a id="trajectory-msgs"></a>

## [trajectory\_msgs](https://github.com/ros2/common_interfaces/tree/iron/trajectory_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/iron/turtlesim/CHANGELOG.rst)

- Remove the range constraints from the holonomic parameter. ([#150](https://github.com/ros/ros_tutorials/issues/150)) ([#151](https://github.com/ros/ros_tutorials/issues/151))
- Add icon ([#148](https://github.com/ros/ros_tutorials/issues/148)) ([#149](https://github.com/ros/ros_tutorials/issues/149))
- Update turtlesim to C++17. ([#146](https://github.com/ros/ros_tutorials/issues/146))
- [rolling] Update maintainers - 2022-11-07 ([#145](https://github.com/ros/ros_tutorials/issues/145))
- Add parameter to enable holonomic motion ([#131](https://github.com/ros/ros_tutorials/issues/131))
- Add humble turtle ([#140](https://github.com/ros/ros_tutorials/issues/140))
- Contributors: Audrow Nash, Chris Lalancette, Daisuke Sato, mergify[bot]

<a id="type-description-interfaces"></a>

## [type\_description\_interfaces](https://github.com/ros2/rcl_interfaces/tree/iron/type_description_interfaces/CHANGELOG.rst)

- Add GetTypeDescription.srv (rep2011) ([#153](https://github.com/ros2/rcl_interfaces/issues/153))
- new package and interfaces for describing other types ([#146](https://github.com/ros2/rcl_interfaces/issues/146))
- Contributors: Emerson Knapp, William Woodall

<a id="unique-identifier-msgs"></a>

## [unique\_identifier\_msgs](https://github.com/ros2/unique_identifier_msgs/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#26](https://github.com/ros2/unique_identifier_msgs/issues/26))
- Depend on rosidl\_core instead of rosidl\_defaults ([#24](https://github.com/ros2/unique_identifier_msgs/issues/24))
- Mirror rolling to master
- Update maintainers ([#22](https://github.com/ros2/unique_identifier_msgs/issues/22))
- Contributors: Audrow Nash, Jacob Perron, methylDragon

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/iron/urdf/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#35](https://github.com/ros2/urdf/issues/35))
- [urdf] package.xml: add missing exec\_depend to urdf\_parser\_plugin ([#34](https://github.com/ros2/urdf/issues/34))
- Provide copy and move constructors for `model` ([#33](https://github.com/ros2/urdf/issues/33))
- Add linter tests and fix errors ([#30](https://github.com/ros2/urdf/issues/30))
- fix [#30](https://github.com/ros/robot_model/issues/30)
- Contributors: Audrow Nash, Daniel Reuter, Tobias Neumann

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/iron/urdf_parser_plugin/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#35](https://github.com/ros2/urdf/issues/35))
- Contributors: Audrow Nash

<a id="visualization-msgs"></a>

## [visualization\_msgs](https://github.com/ros2/common_interfaces/tree/iron/visualization_msgs/CHANGELOG.rst)

- Update common\_interfaces to C++17. ([#215](https://github.com/ros2/common_interfaces/issues/215))
- [rolling] Update maintainers - 2022-11-07 ([#210](https://github.com/ros2/common_interfaces/issues/210))
- Contributors: Audrow Nash, Chris Lalancette

<a id="yaml-cpp-vendor"></a>

## [yaml\_cpp\_vendor](https://github.com/ros2/yaml_cpp_vendor/tree/iron/CHANGELOG.rst)

- [rolling] Update maintainers - 2022-11-07 ([#40](https://github.com/ros2/yaml_cpp_vendor/issues/40))
- Export YAML\_CPP\_DLL define on Windows ([#30](https://github.com/ros2/yaml_cpp_vendor/issues/30)) ([#38](https://github.com/ros2/yaml_cpp_vendor/issues/38))
- Sets CMP0135 policy behavior to NEW ([#36](https://github.com/ros2/yaml_cpp_vendor/issues/36))
- Fixes policy CMP0135 warning for CMake >= 3.24 ([#35](https://github.com/ros2/yaml_cpp_vendor/issues/35))
- build shared lib only if BUILD\_SHARED\_LIBS is set ([#34](https://github.com/ros2/yaml_cpp_vendor/issues/34))
- Mirror rolling to master
- Contributors: Audrow Nash, Cristóbal Arroyo, Jacob Perron, hannes09

<a id="zstd-vendor"></a>

## [zstd\_vendor](https://github.com/ros2/rosbag2/tree/iron/zstd_vendor/CHANGELOG.rst)

- Add Michael Orlov as maintainer in rosbag2 packages ([#1215](https://github.com/ros2/rosbag2/issues/1215))
- Bump zstd to 1.4.8 in zstd\_vendor package ([#1132](https://github.com/ros2/rosbag2/issues/1132))
- Fix/zstd vendor does not find system zstd ([#1111](https://github.com/ros2/rosbag2/issues/1111))
- Contributors: DasRoteSkelett, Michael Orlov
