---
title: "Jazzy Jalisco changelog"
docname: "Releases/Jazzy-Jalisco-Complete-Changelog"
source: "Releases/Jazzy-Jalisco-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="jazzy-jalisco-changelog"></a>

# Jazzy Jalisco changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

Table of Contents

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
- [camera\_calibration\_parsers](#camera-calibration-parsers)
- [camera\_info\_manager](#camera-info-manager)
- [class\_loader](#class-loader)
- [common\_interfaces](#common-interfaces)
- [composition](#composition)
- [demo\_nodes\_cpp](#demo-nodes-cpp)
- [demo\_nodes\_cpp\_native](#demo-nodes-cpp-native)
- [demo\_nodes\_py](#demo-nodes-py)
- [diagnostic\_msgs](#diagnostic-msgs)
- [dummy\_map\_server](#dummy-map-server)
- [dummy\_robot\_bringup](#dummy-robot-bringup)
- [dummy\_sensors](#dummy-sensors)
- [example\_interfaces](#example-interfaces)
- [examples\_rclcpp\_minimal\_subscriber](#examples-rclcpp-minimal-subscriber)
- [examples\_rclcpp\_wait\_set](#examples-rclcpp-wait-set)
- [foonathan\_memory\_vendor](#foonathan-memory-vendor)
- [geometry\_msgs](#geometry-msgs)
- [google\_benchmark\_vendor](#google-benchmark-vendor)
- [gz\_cmake\_vendor](#gz-cmake-vendor)
- [gz\_math\_vendor](#gz-math-vendor)
- [gz\_utils\_vendor](#gz-utils-vendor)
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
- [launch\_testing\_examples](#launch-testing-examples)
- [launch\_testing\_ros](#launch-testing-ros)
- [launch\_xml](#launch-xml)
- [launch\_yaml](#launch-yaml)
- [libcurl\_vendor](#libcurl-vendor)
- [liblz4\_vendor](#liblz4-vendor)
- [libstatistics\_collector](#libstatistics-collector)
- [libyaml\_vendor](#libyaml-vendor)
- [lifecycle](#lifecycle)
- [lifecycle\_py](#lifecycle-py)
- [logging\_demo](#logging-demo)
- [lttngpy](#lttngpy)
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
- [pluginlib](#pluginlib)
- [pybind11\_vendor](#pybind11-vendor)
- [python\_cmake\_module](#python-cmake-module)
- [python\_orocos\_kdl\_vendor](#python-orocos-kdl-vendor)
- [python\_qt\_binding](#python-qt-binding)
- [qt\_dotgraph](#qt-dotgraph)
- [qt\_gui](#qt-gui)
- [qt\_gui\_cpp](#qt-gui-cpp)
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
- [resource\_retriever](#resource-retriever)
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
- [robot\_state\_publisher](#robot-state-publisher)
- [ros2action](#ros2action)
- [ros2bag](#ros2bag)
- [ros2cli](#ros2cli)
- [ros2cli\_test\_interfaces](#ros2cli-test-interfaces)
- [ros2component](#ros2component)
- [ros2doctor](#ros2doctor)
- [ros2interface](#ros2interface)
- [ros2param](#ros2param)
- [ros2pkg](#ros2pkg)
- [ros2service](#ros2service)
- [ros2topic](#ros2topic)
- [ros2trace](#ros2trace)
- [rosbag2\_compression](#rosbag2-compression)
- [rosbag2\_compression\_zstd](#rosbag2-compression-zstd)
- [rosbag2\_cpp](#rosbag2-cpp)
- [rosbag2\_examples\_cpp](#rosbag2-examples-cpp)
- [rosbag2\_examples\_py](#rosbag2-examples-py)
- [rosbag2\_interfaces](#rosbag2-interfaces)
- [rosbag2\_performance\_benchmarking](#rosbag2-performance-benchmarking)
- [rosbag2\_py](#rosbag2-py)
- [rosbag2\_storage](#rosbag2-storage)
- [rosbag2\_storage\_mcap](#rosbag2-storage-mcap)
- [rosbag2\_storage\_sqlite3](#rosbag2-storage-sqlite3)
- [rosbag2\_test\_common](#rosbag2-test-common)
- [rosbag2\_test\_msgdefs](#rosbag2-test-msgdefs)
- [rosbag2\_tests](#rosbag2-tests)
- [rosbag2\_transport](#rosbag2-transport)
- [rosidl\_cmake](#rosidl-cmake)
- [rosidl\_dynamic\_typesupport](#rosidl-dynamic-typesupport)
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
- [rosidl\_typesupport\_introspection\_c](#rosidl-typesupport-introspection-c)
- [rosidl\_typesupport\_introspection\_cpp](#rosidl-typesupport-introspection-cpp)
- [rosidl\_typesupport\_introspection\_tests](#rosidl-typesupport-introspection-tests)
- [rosidl\_typesupport\_tests](#rosidl-typesupport-tests)
- [rpyutils](#rpyutils)
- [rqt](#rqt)
- [rqt\_bag](#rqt-bag)
- [rqt\_bag\_plugins](#rqt-bag-plugins)
- [rqt\_console](#rqt-console)
- [rqt\_graph](#rqt-graph)
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
- [shape\_msgs](#shape-msgs)
- [shared\_queues\_vendor](#shared-queues-vendor)
- [spdlog\_vendor](#spdlog-vendor)
- [sqlite3\_vendor](#sqlite3-vendor)
- [sros2](#sros2)
- [std\_msgs](#std-msgs)
- [std\_srvs](#std-srvs)
- [stereo\_msgs](#stereo-msgs)
- [test\_cli](#test-cli)
- [test\_cli\_remapping](#test-cli-remapping)
- [test\_communication](#test-communication)
- [test\_launch\_ros](#test-launch-ros)
- [test\_launch\_testing](#test-launch-testing)
- [test\_msgs](#test-msgs)
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
- [tf2\_py](#tf2-py)
- [tf2\_ros](#tf2-ros)
- [tf2\_ros\_py](#tf2-ros-py)
- [tf2\_sensor\_msgs](#tf2-sensor-msgs)
- [tf2\_tools](#tf2-tools)
- [topic\_monitor](#topic-monitor)
- [topic\_statistics\_demo](#topic-statistics-demo)
- [tracetools](#tracetools)
- [tracetools\_launch](#tracetools-launch)
- [tracetools\_read](#tracetools-read)
- [tracetools\_test](#tracetools-test)
- [tracetools\_trace](#tracetools-trace)
- [trajectory\_msgs](#trajectory-msgs)
- [turtlesim](#turtlesim)
- [uncrustify\_vendor](#uncrustify-vendor)
- [unique\_identifier\_msgs](#unique-identifier-msgs)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [visualization\_msgs](#visualization-msgs)
- [yaml\_cpp\_vendor](#yaml-cpp-vendor)
- [zstd\_vendor](#zstd-vendor)

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/jazzy/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Fix format-security warning with clang. ([#663](https://github.com/ros2/demos/issues/663))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael Jeronimo

<a id="action-tutorials-interfaces"></a>

## [action\_tutorials\_interfaces](https://github.com/ros2/demos/tree/jazzy/action_tutorials/action_tutorials_interfaces/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/jazzy/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Add tests to action\_tutorials\_py. ([#664](https://github.com/ros2/demos/issues/664))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="actionlib-msgs"></a>

## [actionlib\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/actionlib_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/jazzy/ament_clang_format/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/jazzy/ament_clang_tidy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Fix a warning from newer versions of flake8. ([#469](https://github.com/ament/ament_lint/issues/469))
- remove AMENT\_IGNORE check in clang-tidy when looking for compilation db ([#441](https://github.com/ament/ament_lint/issues/441))
- Contributors: Alberto Soragna, Chris Lalancette, Michael Jeronimo

<a id="ament-cmake"></a>

## [ament\_cmake](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_auto/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Add ament\_auto\_add\_gmock to ament\_cmake\_auto ([#482](https://github.com/ament/ament_cmake/issues/482))
- Contributors: Jordan Palacios, Michael Jeronimo

<a id="ament-cmake-clang-format"></a>

## [ament\_cmake\_clang\_format](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_clang_format/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-clang-tidy"></a>

## [ament\_cmake\_clang\_tidy](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_clang_tidy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Provide –header-filter and –jobs to CMake. ([#450](https://github.com/ament/ament_lint/issues/450))
- Contributors: Michael Jeronimo, Roderick Taylor

<a id="ament-cmake-copyright"></a>

## [ament\_cmake\_copyright](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_copyright/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_core/CHANGELOG.rst)

- Set hints to find the python version we actually want. ([#508](https://github.com/ament/ament_cmake/issues/508))
- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Use CMAKE\_CURRENT\_BINARY\_DIR instead of CMAKE\_BINARY\_DIR in ament\_generate\_environment ([#485](https://github.com/ament/ament_cmake/issues/485))
- Fix CMake error when entire ament projects are added via add\_subdirectory ([#484](https://github.com/ament/ament_cmake/issues/484))
- Contributors: Chris Lalancette, Michael Jeronimo, Silvio Traversaro

<a id="ament-cmake-cppcheck"></a>

## [ament\_cmake\_cppcheck](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_cppcheck/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-cpplint"></a>

## [ament\_cmake\_cpplint](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_cpplint/CHANGELOG.rst)

- Increased cpplint timeout by default on Windows ([#486](https://github.com/ament/ament_lint/issues/486))
- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Alejandro Hernández Cordero, Michael Jeronimo

<a id="ament-cmake-export-definitions"></a>

## [ament\_cmake\_export\_definitions](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_definitions/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-dependencies"></a>

## [ament\_cmake\_export\_dependencies](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_dependencies/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-include-directories"></a>

## [ament\_cmake\_export\_include\_directories](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_include_directories/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-interfaces"></a>

## [ament\_cmake\_export\_interfaces](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_interfaces/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-libraries"></a>

## [ament\_cmake\_export\_libraries](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_libraries/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-link-flags"></a>

## [ament\_cmake\_export\_link\_flags](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_link_flags/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-export-targets"></a>

## [ament\_cmake\_export\_targets](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_export_targets/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Add NAMESPACE support to ament\_export\_targets ([#498](https://github.com/ament/ament_cmake/issues/498))
- Contributors: Michael Jeronimo, Ryan

<a id="ament-cmake-flake8"></a>

## [ament\_cmake\_flake8](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_flake8/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-gen-version-h"></a>

## [ament\_cmake\_gen\_version\_h](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_gen_version_h/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Update to C++17 ([#488](https://github.com/ament/ament_cmake/issues/488))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-cmake-gmock"></a>

## [ament\_cmake\_gmock](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_gmock/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Split ament\_add\_gmock into \_executable and \_test. ([#497](https://github.com/ament/ament_cmake/issues/497))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-cmake-google-benchmark"></a>

## [ament\_cmake\_google\_benchmark](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_google_benchmark/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_gtest/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Split ament\_add\_gmock into \_executable and \_test. ([#497](https://github.com/ament/ament_cmake/issues/497))
- ament\_add\_gtest\_test: add TEST\_NAME parameter ([#492](https://github.com/ament/ament_cmake/issues/492))
- Contributors: Chris Lalancette, Christopher Wecht, Michael Jeronimo

<a id="ament-cmake-include-directories"></a>

## [ament\_cmake\_include\_directories](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_include_directories/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-libraries"></a>

## [ament\_cmake\_libraries](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_libraries/CHANGELOG.rst)

- perf: faster ament\_libraries\_deduplicate implementation ([#448](https://github.com/ament/ament_cmake/issues/448)) Co-authored-by: Scott K Logan <[logans@cottsay.net](mailto:logans%40cottsay.net)>
- Subtle fix for ament\_libraries\_deduplicate tests ([#516](https://github.com/ament/ament_cmake/issues/516))
- Add some basic tests to ament\_cmake\_libraries ([#512](https://github.com/ament/ament_cmake/issues/512))
- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo, Scott K Logan, Vincent Richard

<a id="ament-cmake-lint-cmake"></a>

## [ament\_cmake\_lint\_cmake](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_lint_cmake/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-mypy"></a>

## [ament\_cmake\_mypy](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_mypy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-pclint"></a>

## [ament\_cmake\_pclint](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_pclint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-pep257"></a>

## [ament\_cmake\_pep257](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_pep257/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-pycodestyle"></a>

## [ament\_cmake\_pycodestyle](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_pycodestyle/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-pyflakes"></a>

## [ament\_cmake\_pyflakes](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_pyflakes/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-cmake-pytest"></a>

## [ament\_cmake\_pytest](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_pytest/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-python"></a>

## [ament\_cmake\_python](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_python/CHANGELOG.rst)

- Add in a comment explaining where Python3::Interpreter comes from. ([#510](https://github.com/ament/ament_cmake/issues/510))
- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_target_dependencies/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Fix `ament_target_dependencies` ([#452](https://github.com/ament/ament_cmake/issues/452))
- Contributors: Michael Jeronimo, Vincent Richard

<a id="ament-cmake-test"></a>

## [ament\_cmake\_test](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_test/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Recursively check for errors/failures in produced JUnit result XMLs ([#446](https://github.com/ament/ament_cmake/issues/446))
- Contributors: Michael Jeronimo, Nick Morales

<a id="ament-cmake-uncrustify"></a>

## [ament\_cmake\_uncrustify](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_uncrustify/CHANGELOG.rst)

- Added Timeout to ament\_uncrustify ([#485](https://github.com/ament/ament_lint/issues/485))
- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Alejandro Hernández Cordero, Michael Jeronimo

<a id="ament-cmake-vendor-package"></a>

## [ament\_cmake\_vendor\_package](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_vendor_package/CHANGELOG.rst)

- Add more CMake variables to pass to vendor projects ([#519](https://github.com/ament/ament_cmake/issues/519))
- Fix patch file dependencies in ament\_cmake\_vendor\_package ([#520](https://github.com/ament/ament_cmake/issues/520))
- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Always set CMAKE\_C[XX]\_COMPILER for vendor packages if needed ([#476](https://github.com/ament/ament_cmake/issues/476))
- Switch to CMake ‘braket arguments’ ([#461](https://github.com/ament/ament_cmake/issues/461))
- Replace ‘git’ dep with ‘vcstool’ ([#462](https://github.com/ament/ament_cmake/issues/462))
- Add support for specifying a patch directory in ament\_vendor ([#449](https://github.com/ament/ament_cmake/issues/449))
- Contributors: Christophe Bedard, Michael Jeronimo, Scott K Logan

<a id="ament-cmake-version"></a>

## [ament\_cmake\_version](https://github.com/ament/ament_cmake/tree/jazzy/ament_cmake_version/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#503](https://github.com/ament/ament_cmake/issues/503))
- Contributors: Michael Jeronimo

<a id="ament-cmake-xmllint"></a>

## [ament\_cmake\_xmllint](https://github.com/ament/ament_lint/tree/jazzy/ament_cmake_xmllint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/jazzy/ament_copyright/CHANGELOG.rst)

- Small fixes for modern flake8. ([#484](https://github.com/ament/ament_lint/issues/484))
- Fix add-copyright year function ([#466](https://github.com/ament/ament_lint/issues/466))
- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Chris Lalancette, Lloyd Pearson, Michael Jeronimo

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/jazzy/ament_cppcheck/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Add in checks to ament\_cppcheck code. ([#472](https://github.com/ament/ament_lint/issues/472))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/jazzy/ament_cpplint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Pass –output argument to cpplint ([#453](https://github.com/ament/ament_lint/issues/453))
- Contributors: Michael Jeronimo, Vladimir Ivan

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/jazzy/ament_flake8/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Changes to make ament\_flake8 work with v6+ ([#459](https://github.com/ament/ament_lint/issues/459))
- Add additional dependencies to ament\_flake8. ([#454](https://github.com/ament/ament_lint/issues/454))
- Fix compatibility with flake8 version 5 ([#410](https://github.com/ament/ament_lint/issues/410))
- Contributors: Chris Lalancette, Michael Carroll, Michael Jeronimo, Timo Röhling

<a id="ament-index-cpp"></a>

## [ament\_index\_cpp](https://github.com/ament/ament_index/tree/jazzy/ament_index_cpp/CHANGELOG.rst)

- Update quality declaration documents ([#94](https://github.com/ament/ament_index/issues/94))
- only append search paths on first PackageNotFound ([#91](https://github.com/ament/ament_index/issues/91))
- Update to C++17 ([#90](https://github.com/ament/ament_index/issues/90))
- Contributors: Chris Lalancette, Christophe Bedard, Lucas Walter

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/jazzy/ament_index_python/CHANGELOG.rst)

- Update quality declaration documents ([#94](https://github.com/ament/ament_index/issues/94))
- Add type annotations to python files. ([#93](https://github.com/ament/ament_index/issues/93))
- Contributors: Christophe Bedard, Michael Carlstrom

<a id="ament-lint"></a>

## [ament\_lint](https://github.com/ament/ament_lint/tree/jazzy/ament_lint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Add an ament\_lint test dependency on python3-pytest. ([#473](https://github.com/ament/ament_lint/issues/473))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/jazzy/ament_lint_auto/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/jazzy/ament_lint_cmake/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-lint-common"></a>

## [ament\_lint\_common](https://github.com/ament/ament_lint/tree/jazzy/ament_lint_common/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/jazzy/ament_mypy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Fix a flake8 warning in ament\_mypy. ([#470](https://github.com/ament/ament_lint/issues/470)) No need for parentheses around an assert.
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/jazzy/CHANGELOG.rst)

- Migrate from legacy importlib-resources ([#143](https://github.com/ament/ament_package/issues/143))
- Add setuptools dependency back in. ([#141](https://github.com/ament/ament_package/issues/141))
- Make python dependencies exec\_depend. ([#140](https://github.com/ament/ament_package/issues/140))
- Contributors: Chris Lalancette, Isabel Paredes

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/jazzy/ament_pclint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-pep257"></a>

## [ament\_pep257](https://github.com/ament/ament_lint/tree/jazzy/ament_pep257/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Convert linenumber to string when printing errors ([#443](https://github.com/ament/ament_lint/issues/443))
- Contributors: Michael Jeronimo, Robert Brothers

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/jazzy/ament_pycodestyle/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/jazzy/ament_pyflakes/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Contributors: Michael Jeronimo

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/jazzy/ament_uncrustify/CHANGELOG.rst)

- Adds uncrustify 0.78.1 config ([#475](https://github.com/ament/ament_lint/issues/475))
- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- Fix a flake8 warning in ament\_uncrustify. ([#471](https://github.com/ament/ament_lint/issues/471))
- Contributors: Chris Lalancette, Marco A. Gutierrez, Michael Jeronimo

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/jazzy/ament_xmllint/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#474](https://github.com/ament/ament_lint/issues/474))
- (ament\_xmllint) add extensions argument ([#456](https://github.com/ament/ament_lint/issues/456))
- Contributors: Matthijs van der Burgh, Michael Jeronimo

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/jazzy/camera_calibration_parsers/CHANGELOG.rst)

- Update to yaml-cpp 0.8.0. ([#305](https://github.com/ros-perception/image_common/issues/305))
- Switch from rcpputils::fs to std::filesystem ([#300](https://github.com/ros-perception/image_common/issues/300))
- Removed C headers: camera\_info\_manager camera\_calibration\_parsers ([#290](https://github.com/ros-perception/image_common/issues/290))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/jazzy/camera_info_manager/CHANGELOG.rst)

- Switch from rcpputils::fs to std::filesystem ([#300](https://github.com/ros-perception/image_common/issues/300))
- Removed C headers: camera\_info\_manager camera\_calibration\_parsers ([#290](https://github.com/ros-perception/image_common/issues/290))
- Contributors: Alejandro Hernández Cordero, Christophe Bedard

<a id="class-loader"></a>

## [class\_loader](https://github.com/ros/class_loader/tree/jazzy/CHANGELOG.rst)

- Remove all uses of ament\_target\_dependencies. ([#210](https://github.com/ros/class_loader/issues/210))
- Update to C++17 ([#209](https://github.com/ros/class_loader/issues/209))
- Contributors: Chris Lalancette

<a id="common-interfaces"></a>

## [common\_interfaces](https://github.com/ros2/common_interfaces/tree/jazzy/common_interfaces/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/jazzy/composition/CHANGELOG.rst)

- [composition] add launch action console output in the verify section ([#677](https://github.com/ros2/demos/issues/677)) ([#681](https://github.com/ros2/demos/issues/681)) (cherry picked from commit 34d29db73e78a84a174ad8699a2d646b0eeb1cdf) Co-authored-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Contributors: Felipe Gomes de Melo, Michael Jeronimo, mergify[bot]

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/jazzy/demo_nodes_cpp/CHANGELOG.rst)

- [demo\_nodes\_cpp] some readme and executable name fixups ([#678](https://github.com/ros2/demos/issues/678)) ([#688](https://github.com/ros2/demos/issues/688)) (cherry picked from commit aa8df8904b864d063e31fd5b953ffe561c7a9fe0) Co-authored-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Fix gcc warnings when building with optimizations. ([#672](https://github.com/ros2/demos/issues/672)) ([#673](https://github.com/ros2/demos/issues/673)) \* Fix gcc warnings when building with optimizations. When building the allocator\_tutorial\_pmr demo with -O2, gcc is throwing an error saying that new and delete are mismatched. This is something of a misnomer, however; the real problem is that the global new override we have in that demo is actually implemented incorrectly. In particular, the documentation at <https://en.cppreference.com/w/cpp/memory/new/operator_new> very clearly specifies that operator new either has to return a valid pointer, or throw an exception on error. Our version wasn’t throwing the exception, so change it to throw std::bad\_alloc if std::malloc fails. While we are in here, also fix another small possible is where std::malloc could return nullptr on a zero-sized object, thus throwing an exception it shouldn’t. \* Always inline the new and delete operators. That’s because gcc 13 has a bug where it can sometimes inline one or the other, and then it detects that they mismatch. For gcc and clang, just force them to always be inline in this demo. \* Switch to NOINLINE instead. Both clang and MSVC don’t like inlining these, so instead ensure that they are *not* inlined. This also works because the problem is when new is inlined but not delete (or vice-versa). As long as they are both not inlined, this should fix the warning. (cherry picked from commit 957ddbb9f04f55cabd8496e8d74eb35ee4d29105) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- A few uncrustify fixes for 0.78. ([#667](https://github.com/ros2/demos/issues/667))
- Allow users to configure the executor for executables in `demo_nodes_cpp` ([#666](https://github.com/ros2/demos/issues/666))
- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Added extra documentation and clarifications. ([#651](https://github.com/ros2/demos/issues/651))
- Add in support for both the PMR and custom allocator tutorials. ([#655](https://github.com/ros2/demos/issues/655))
- Replacing old-style C++ allocator with a polymorphic memory resource (PMR) ([#653](https://github.com/ros2/demos/issues/653))
- Remove unnecessary captures in the various demos. ([#647](https://github.com/ros2/demos/issues/647))
- Dramatically speed up the demo\_nodes\_cpp tests ([#641](https://github.com/ros2/demos/issues/641))
- Switch to using RCLCPP logging macros in the lifecycle package. ([#644](https://github.com/ros2/demos/issues/644))
- failed to call introspection\_client ([#643](https://github.com/ros2/demos/issues/643))
- Small cleanups to the demos when running through them. ([#639](https://github.com/ros2/demos/issues/639))
- Cleanup demo\_nodes\_cpp CMake and dependencies ([#638](https://github.com/ros2/demos/issues/638))
- Change the service introspection parameter off value to ‘disabled’ ([#634](https://github.com/ros2/demos/issues/634))
- Add demos for using logger service ([#611](https://github.com/ros2/demos/issues/611))
- Contributors: Ali Ashkani Nia, Barry Xu, Chen Lihui, Chris Lalancette, Michael Jeronimo, Yadu, jrutgeer, mergify[bot]

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/jazzy/demo_nodes_cpp_native/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/jazzy/demo_nodes_py/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Change the service introspection parameter off value to ‘disabled’ ([#634](https://github.com/ros2/demos/issues/634)) With this we can avoid the tricky bits around YAML interpretation of ‘off’ as a boolean.
- Add demos for using logger service ([#611](https://github.com/ros2/demos/issues/611))
- Contributors: Barry Xu, Chris Lalancette, Michael Jeronimo

<a id="diagnostic-msgs"></a>

## [diagnostic\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/diagnostic_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/jazzy/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/jazzy/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Switch to file-content launch substitution ([#627](https://github.com/ros2/demos/issues/627))
- Contributors: Michael Jeronimo, Scott K Logan

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/jazzy/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Update dummy\_sensors readme to echo the correct topic ([#675](https://github.com/ros2/demos/issues/675)) ([#684](https://github.com/ros2/demos/issues/684)) (cherry picked from commit eec5c12ea95dfaaa230f9f1a8e9cff9b09dde5d5) Co-authored-by: jmackay2 <[1.732mackay@gmail.com](mailto:1.732mackay%40gmail.com)>
- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Fix unstable LaserScan status for rviz2 ([#614](https://github.com/ros2/demos/issues/614))
- Contributors: Chen Lihui, Michael Jeronimo, mergify[bot]

<a id="example-interfaces"></a>

## [example\_interfaces](https://github.com/ros2/example_interfaces/tree/jazzy/CHANGELOG.rst)

- Update to C++17. ([#18](https://github.com/ros2/example_interfaces/issues/18))
- Contributors: Chris Lalancette

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/jazzy/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- fix: Fixed compilation after API change of TimerBase::execute ([#375](https://github.com/ros2/examples/issues/375)) Co-authored-by: Janosch Machowinski <[J.Machowinski@cellumation.com](mailto:J.Machowinski%40cellumation.com)>
- Split lambda and subscriber def in minimal example ([#363](https://github.com/ros2/examples/issues/363))
- Contributors: Felipe Gomes de Melo, jmachowinski

<a id="examples-rclcpp-wait-set"></a>

## [examples\_rclcpp\_wait\_set](https://github.com/ros2/examples/tree/jazzy/rclcpp/wait_set/CHANGELOG.rst)

- fix: Fixed compilation after API change of TimerBase::execute ([#375](https://github.com/ros2/examples/issues/375)) Co-authored-by: Janosch Machowinski <[J.Machowinski@cellumation.com](mailto:J.Machowinski%40cellumation.com)>
- Contributors: jmachowinski

<a id="foonathan-memory-vendor"></a>

## [foonathan\_memory\_vendor](https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst)

- Improve mechanism to find an installation of foonathan\_memory (#67)
- Added support for QNX 7.1 build (#65)

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/geometry_msgs/CHANGELOG.rst)

- Remove references to index.ros.org. ([#244](https://github.com/ros2/common_interfaces/issues/244))
- Create new messages with all fields needed to define a velocity and transform it ([#240](https://github.com/ros2/common_interfaces/issues/240)) Co-authored-by: Dr. Denis <[denis@stoglrobotics.de](mailto:denis%40stoglrobotics.de)> Co-authored-by: Addisu Z. Taddese <[addisuzt@intrinsic.ai](mailto:addisuzt%40intrinsic.ai)> Co-authored-by: Tully Foote <[tullyfoote@intrinsic.ai](mailto:tullyfoote%40intrinsic.ai)>
- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- adding IDs to geometry\_msgs/Polygon, PolygonStamped ([#232](https://github.com/ros2/common_interfaces/issues/232))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Steve Macenski

<a id="google-benchmark-vendor"></a>

## [google\_benchmark\_vendor](https://github.com/ament/google_benchmark_vendor/tree/jazzy/CHANGELOG.rst)

- Update to 1.8.3. ([#29](https://github.com/ament/google_benchmark_vendor/issues/29))
- Contributors: Marco A. Gutierrez

<a id="gz-cmake-vendor"></a>

## [gz\_cmake\_vendor](https://github.com/gazebo-release/gz_cmake_vendor/tree/jazzy/CHANGELOG.rst)

- Update vendored version to 3.5.3
- Use an alias target for root library
- Add support for the `<pkg>::<pkg>` and `<pkg>::all` targets, fix sourcing of dsv files
- Update vendored version to 3.5.2
- Update vendored package version
- Patch the pkg-config directory in the gz-cmake code. ([#4](https://github.com/gazebo-release/gz_cmake_vendor/issues/4)) \* Patch the pkg-config directory in the gz-cmake code. When building on the ROS 2 buildfarm, we aren’t setting some of the CMAKE\_PREFIX variables. This means that using CMAKE\_INSTALL\_FULL\_LIBDIR actually creates a path like /opt/ros/rolling/… , which makes debuild upset. However, we actually need the FULL\_LIBDIR in order to calculate the relative path between it and the INSTALL\_PREFIX. Work around this by having two variables; the pkgconfig\_install\_dir (relative), used to install the files, and pkgconfig\_abs\_install\_dir (absolute), used to calculate the relative path between them. This should fix the build on the buildfarm. I’ll note that we are doing it here and not in gz-cmake proper because of knock-on effects to downstream gazebo. If this is successful we may end up merging it there, at which point we can drop this patch. \* Update GzPackage as well. ———
- Require calling find\_package on the underlying package ([#3](https://github.com/gazebo-release/gz_cmake_vendor/issues/3)) This also changes the version of the vendor package to 0.0.1 and adds the version of the vendored package in the description
- Fix linter ([#2](https://github.com/gazebo-release/gz_cmake_vendor/issues/2))
- Use `<depend>` on upstream package so that dependency is exported
- Update maintainer
- Add package.xml and CMakeLists ([#1](https://github.com/gazebo-release/gz_cmake_vendor/issues/1))
- Initial import
- Contributors: Addisu Z. Taddese, Chris Lalancette

<a id="gz-math-vendor"></a>

## [gz\_math\_vendor](https://github.com/gazebo-release/gz_math_vendor/tree/jazzy/CHANGELOG.rst)

- Use an alias target for root library
- Add support for the `<pkg>::<pkg>` and `<pkg>::all` targets, fix sourcing of dsv files
- Disable SWIG to fix CMake warning
- Disable pybind11 for now
- Require calling find\_package on the underlying package ([#2](https://github.com/gazebo-release/gz_math_vendor/issues/2))
- Fix linter ([#1](https://github.com/gazebo-release/gz_math_vendor/issues/1))
- Remove Nate
- Update maintainers
- Initial import
- Contributors: Addisu Z. Taddese

<a id="gz-utils-vendor"></a>

## [gz\_utils\_vendor](https://github.com/gazebo-release/gz_utils_vendor/tree/jazzy/CHANGELOG.rst)

- Use an alias target for root library
- Add support for the `<pkg>::<pkg>` and `<pkg>::all` targets, fix sourcing of dsv files
- Require calling find\_package on the underlying package ([#2](https://github.com/gazebo-release/gz_utils_vendor/issues/2))
- Fix linter ([#1](https://github.com/gazebo-release/gz_utils_vendor/issues/1))
- Initial import
- Contributors: Addisu Z. Taddese

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/jazzy/image_tools/CHANGELOG.rst)

- A few uncrustify fixes for 0.78. ([#667](https://github.com/ros2/demos/issues/667))
- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael Jeronimo

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/jazzy/image_transport/CHANGELOG.rst)

- Added rclcpp component to Republish ([#275](https://github.com/ros-perception/image_common/issues/275))
- Add QoS option reliability to republisher qos params ([#296](https://github.com/ros-perception/image_common/issues/296))
- implement CameraSubscriber::getNumPublishers ([#297](https://github.com/ros-perception/image_common/issues/297))
- Add missing definition for CameraPublisher::publish overload ([#278](https://github.com/ros-perception/image_common/issues/278))
- Advertize and subscribe with custom qos ([#288](https://github.com/ros-perception/image_common/issues/288))
- Removed C headers ([#289](https://github.com/ros-perception/image_common/issues/289))
- Switch to using the override keyword for simple\_publisher\_plugin. ([#285](https://github.com/ros-perception/image_common/issues/285))
- feat: enable plugin allowlist ([#264](https://github.com/ros-perception/image_common/issues/264))
- Expose option to set callback groups ([#274](https://github.com/ros-perception/image_common/issues/274))
- add support for lazy subscribers ([#272](https://github.com/ros-perception/image_common/issues/272))
- Contributors: Aditya Pande, Alejandro Hernández Cordero, Carlos Andrés Álvarez Restrepo, Chris Lalancette, Daisuke Nishimatsu, Michael Ferguson, s-hall

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/jazzy/CHANGELOG.rst)

- Shorten the length of a lambda. ([#106](https://github.com/ros-visualization/interactive_markers/issues/106))
- Fixed C++20 warning that ‘++’ expression of ‘volatile’-qualified type is deprecated ([#102](https://github.com/ros-visualization/interactive_markers/issues/102))
- Cleanup of interactive markers ([#101](https://github.com/ros-visualization/interactive_markers/issues/101))
- Contributors: AiVerisimilitude, Chris Lalancette

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/jazzy/intra_process_demo/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Fix executable name in README ([#618](https://github.com/ros2/demos/issues/618))
- Contributors: Felipe Gomes de Melo, Michael Jeronimo, Yadunund

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/jazzy/kdl_parser/CHANGELOG.rst)

- Update to C++17. ([#82](https://github.com/ros/kdl_parser/issues/82))
- Contributors: Chris Lalancette

<a id="keyboard-handler"></a>

## [keyboard\_handler](https://github.com/ros-tooling/keyboard_handler/tree/jazzy/keyboard_handler/CHANGELOG.rst)

- Shorten lambdas so newer uncrustify is happier. ([#42](https://github.com/ros-tooling/keyboard_handler/issues/42))
- Fixed C++20 warning implicit capture of this in lambda ([#41](https://github.com/ros-tooling/keyboard_handler/issues/41))
- Update to C++17. ([#37](https://github.com/ros-tooling/keyboard_handler/issues/37))
- Contributors: AiVerisimilitude, Chris Lalancette

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/jazzy/CHANGELOG.rst)

- Switch to target\_link\_libraries. ([#92](https://github.com/ros-perception/laser_geometry/issues/92))
- Contributors: Chris Lalancette

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/jazzy/launch/CHANGELOG.rst)

- (launch) fix describe of PathJoinSubstitution ([#771](https://github.com/ros2/launch/issues/771))
- Small fixes for modern flake8. ([#772](https://github.com/ros2/launch/issues/772))
- Cleanup some type annotations.
- Rework task exceptions loop. ([#755](https://github.com/ros2/launch/issues/755))
- add format overriding by environment variables ([#722](https://github.com/ros2/launch/issues/722))
- Add exception type to error output ([#753](https://github.com/ros2/launch/issues/753))
- Let XML executables/nodes be “required” (like in ROS 1) ([#751](https://github.com/ros2/launch/issues/751))
- Add conditional substitution ([#734](https://github.com/ros2/launch/issues/734))
- Add maximum times for a process to respawn ([#696](https://github.com/ros2/launch/issues/696))
- Add in a timeout for launch pytests. ([#725](https://github.com/ros2/launch/issues/725))
- Fix remaining occurrences of “There is no current event loop” ([#723](https://github.com/ros2/launch/issues/723))
- Update the launch code for newer flake8 and mypy. ([#719](https://github.com/ros2/launch/issues/719))
- Remove the deprecated some\_actions\_type.py ([#718](https://github.com/ros2/launch/issues/718))
- Improve launch file parsing error messages ([#626](https://github.com/ros2/launch/issues/626))
- Add file-content launch substitution ([#708](https://github.com/ros2/launch/issues/708))
- Contributors: Chris Lalancette, David Yackzan, Marc Bestmann, Matthew Elwin, Matthijs van der Burgh, Nick Lamprianidis, Santti4go, Scott K Logan, Timon Engelke

<a id="launch-pytest"></a>

## [launch\_pytest](https://github.com/ros2/launch/tree/jazzy/launch_pytest/CHANGELOG.rst)

- Switch tryfirst/trylast to hookimpl.
- Contributors: Chris Lalancette

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/jazzy/launch_ros/CHANGELOG.rst)

- Fix: typing. Iterable doesn’t have \_\_getitem\_\_ ([#393](https://github.com/ros2/launch_ros/issues/393))
- Cleanup some type annotations. ([#392](https://github.com/ros2/launch_ros/issues/392))
- Create py.typed to mark this library as typed ([#379](https://github.com/ros2/launch_ros/issues/379))
- Remove create\_future implementation. ([#372](https://github.com/ros2/launch_ros/issues/372))
- cache lookup of importlib metadata in Node action ([#365](https://github.com/ros2/launch_ros/issues/365))
- Get rid of unnecessary checks in composable\_node\_container. ([#364](https://github.com/ros2/launch_ros/issues/364))
- Contributors: Chris Lalancette, Jonas Otto, Matthijs van der Burgh, William Woodall

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/jazzy/launch_testing/CHANGELOG.rst)

- Fix a warning in modern unittest. ([#773](https://github.com/ros2/launch/issues/773)) Newer versions of unittest no longer store an errors list; instead, they store a result, which then stores an error list. Update the code here to be able to deal with either version.
- Add consider\_namespace\_packages=False ([#766](https://github.com/ros2/launch/issues/766))
- to open expected outpout file with an encoding parameter ([#717](https://github.com/ros2/launch/issues/717))
- Contributors: Chen Lihui, Chris Lalancette, Tony Najjar

<a id="launch-testing-examples"></a>

## [launch\_testing\_examples](https://github.com/ros2/examples/tree/jazzy/launch_testing/launch_testing_examples/CHANGELOG.rst)

- Cleanup the launch\_testing\_examples. ([#374](https://github.com/ros2/examples/issues/374))
- Refactor WaitForNodes class. ([#373](https://github.com/ros2/examples/issues/373))
- Contributors: Chris Lalancette

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/jazzy/launch_testing_ros/CHANGELOG.rst)

- Make launch\_testing\_ros examples more robust. ([#394](https://github.com/ros2/launch_ros/issues/394))
- added type hinting to launch\_testing\_ros/test/examples ([#386](https://github.com/ros2/launch_ros/issues/386))
- Handle spin() ExternalShutdownException. ([#378](https://github.com/ros2/launch_ros/issues/378))
- Increase the timeout in wait\_for\_topic\_launch\_test. ([#377](https://github.com/ros2/launch_ros/issues/377))
- `WaitForTopics`: get content of messages for each topic ([#353](https://github.com/ros2/launch_ros/issues/353))
- Contributors: Chris Lalancette, Giorgio Pintaudi, Yaswanth

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/jazzy/launch_xml/CHANGELOG.rst)

- launch\_xml: fix xml syntax in README ([#770](https://github.com/ros2/launch/issues/770))
- Let XML executables/nodes be “required” (like in ROS 1) ([#751](https://github.com/ros2/launch/issues/751)) \* Let XML nodes be “required” Essentially on\_exit=”shutdown” is equivalent to ROS 1 required=”true”. This feature is implemented using the python launchfile on\_exit mechanism. Right now “shutdown” is the only action accepted by on\_exit, but theoretically more “on\_exit” actions could be added later. Example: <executable cmd=”ls” on\_exit=”shutdown”/> \* Added tests for yaml
- Improve launch file parsing error messages ([#626](https://github.com/ros2/launch/issues/626))
- Contributors: Matthew Elwin, Steve Peters, Timon Engelke

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/jazzy/launch_yaml/CHANGELOG.rst)

- Fix flake8 warnings in launch\_yaml. ([#756](https://github.com/ros2/launch/issues/756))
- Let XML executables/nodes be “required” (like in ROS 1) ([#751](https://github.com/ros2/launch/issues/751)) \* Let XML nodes be “required” Essentially on\_exit=”shutdown” is equivalent to ROS 1 required=”true”. This feature is implemented using the python launchfile on\_exit mechanism. Right now “shutdown” is the only action accepted by on\_exit, but theoretically more “on\_exit” actions could be added later. Example: <executable cmd=”ls” on\_exit=”shutdown”/> \* Added tests for yaml
- Improve launch file parsing error messages ([#626](https://github.com/ros2/launch/issues/626))
- Contributors: Chris Lalancette, Matthew Elwin, Timon Engelke

<a id="libcurl-vendor"></a>

## [libcurl\_vendor](https://github.com/ros/resource_retriever/tree/jazzy/libcurl_vendor/CHANGELOG.rst)

- Add “lib” to the Windows curl search path. ([#96](https://github.com/ros/resource_retriever/issues/96)) ([#97](https://github.com/ros/resource_retriever/issues/97)) In CMake 3.3, a commit made it so that the find\_package module in CMake had a compatibility mode where it would automatically search for packages in a <prefix>/lib subdirectory. In CMake 3.6, this compatibility mode was reverted for all platforms *except* Windows. That means that since CMake 3.3, we haven’t actually been using the path as specified in `curl_DIR`, but we have instead been inadvertently relying on that fallback behavior. In CMake 3.28, that compatibilty mode was also removed for Windows, meaning that we are now failing to find\_package(curl) in downstream packages (like resource\_retriever). Fix this by adding in the “lib” directory that always should have been there. I’ll note that this *only* affects our Windows builds, because this code is in a if(WIN32) block. (cherry picked from commit 1839d583190eb9dcf339eaaf6bebe632d94664a6) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Switch to ament\_cmake\_vendor\_package ([#86](https://github.com/ros/resource_retriever/issues/86))
- Contributors: Scott K Logan, mergify[bot]

<a id="liblz4-vendor"></a>

## [liblz4\_vendor](https://github.com/ros2/rosbag2/tree/jazzy/liblz4_vendor/CHANGELOG.rst)

- Make sure to build\_export\_depend liblz4-dev. ([#1614](https://github.com/ros2/rosbag2/issues/1614))
- Switch to using ament\_vendor\_package for lz4. ([#1583](https://github.com/ros2/rosbag2/issues/1583))
- Contributors: Chris Lalancette

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/jazzy/CHANGELOG.rst)

- Bump pascalgn/automerge-action from 0.16.2 to 0.16.3
- Bump codecov/codecov-action from 4.1.1 to 4.2.0
- Fixes for newer uncrustify. ([#186](https://github.com/ros-tooling/libstatistics_collector/issues/186))
- Bump actions/upload-artifact from 3 to 4
- Switch to using target\_link\_libraries everywhere. ([#174](https://github.com/ros-tooling/libstatistics_collector/issues/174))
- Bump rolling to 1.6.3 ([#173](https://github.com/ros-tooling/libstatistics_collector/issues/173))
- Bump actions/checkout from 3 to 4 ([#169](https://github.com/ros-tooling/libstatistics_collector/issues/169))
- Add API to use message\_info instead unserialized message ([#170](https://github.com/ros-tooling/libstatistics_collector/issues/170))
- Bump codecov/codecov-action from 3.1.3 to 3.1.4
- Bump actions/checkout from 3 to 4 ([#169](https://github.com/ros-tooling/libstatistics_collector/issues/169))
- Add API to use message\_info instead unserialized message ([#170](https://github.com/ros-tooling/libstatistics_collector/issues/170))
- Bump codecov/codecov-action from 3.1.3 to 3.1.4
- Add in missing cstdint include. ([#165](https://github.com/ros-tooling/libstatistics_collector/issues/165))
- Bump codecov/codecov-action from 3.1.2 to 3.1.3
- Contributors: Chris Lalancette, Lucas Wendland, Michael Orlov, dependabot[bot]

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/jazzy/CHANGELOG.rst)

- Update quality declaration documents ([#62](https://github.com/ros2/libyaml_vendor/issues/62))
- remove rcpputils and rcutils dependency ([#61](https://github.com/ros2/libyaml_vendor/issues/61))
- Set to C++17. ([#59](https://github.com/ros2/libyaml_vendor/issues/59))
- Switch to ament\_cmake\_vendor\_package ([#58](https://github.com/ros2/libyaml_vendor/issues/58))
- Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura, Scott K Logan

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/jazzy/lifecycle/CHANGELOG.rst)

- A few uncrustify fixes for 0.78. ([#667](https://github.com/ros2/demos/issues/667))
- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Switch to using RCLCPP logging macros in the lifecycle package. ([#644](https://github.com/ros2/demos/issues/644))
- Contributors: Chris Lalancette, Felipe Gomes de Melo, Michael Jeronimo

<a id="lifecycle-py"></a>

## [lifecycle\_py](https://github.com/ros2/demos/tree/jazzy/lifecycle_py/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/jazzy/logging_demo/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Migrate std::bind calls to lambda expressions ([#659](https://github.com/ros2/demos/issues/659))
- Contributors: Felipe Gomes de Melo, Michael Jeronimo

<a id="lttngpy"></a>

## [lttngpy](https://github.com/ros2/ros2_tracing/tree/jazzy/lttngpy/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Fixes for newer uncrustify ([#101](https://github.com/ros2/ros2_tracing/issues/101))
- Fix Python not being found for lttngpy in Windows debug mode ([#87](https://github.com/ros2/ros2_tracing/issues/87))
- Switch to custom lttng-ctl Python bindings ([#81](https://github.com/ros2/ros2_tracing/issues/81))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="map-msgs"></a>

## [map\_msgs](https://github.com/ros-planning/navigation_msgs/tree/jazzy/map_msgs/CHANGELOG.rst)

- Update maintainer list in package.xml files
- Update to C++17
- Contributors: Chris Lalancette, Michael Jeronimo, Steve Macenski

<a id="mcap-vendor"></a>

## [mcap\_vendor](https://github.com/ros2/rosbag2/tree/jazzy/mcap_vendor/CHANGELOG.rst)

- Switch to using ament\_vendor\_package for lz4. ([#1583](https://github.com/ros2/rosbag2/issues/1583))
- Switch to target\_link\_libraries everywhere. ([#1504](https://github.com/ros2/rosbag2/issues/1504))
- Update mcap to v1.1.0 ([#1361](https://github.com/ros2/rosbag2/issues/1361))
- Contributors: Chris Lalancette, Emerson Knapp

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/jazzy/CHANGELOG.rst)

- Update TimeSynchronizer usage example. ([#115](https://github.com/ros2/message_filters/issues/115))
- Remove ‘using’ keyword in message\_filters ([#106](https://github.com/ros2/message_filters/issues/106))
- Remove the use of ament\_target\_dependencies. ([#105](https://github.com/ros2/message_filters/issues/105))
- Fixes pointed out by clang ([#104](https://github.com/ros2/message_filters/issues/104))
- Mark subscription cb parameter const ([#103](https://github.com/ros2/message_filters/issues/103))
- Update the HasHeader check to be more specific. ([#101](https://github.com/ros2/message_filters/issues/101))
- TypeAdapters support ([#95](https://github.com/ros2/message_filters/issues/95)) ([#96](https://github.com/ros2/message_filters/issues/96))
- Cleanup a few minor things in the filters. ([#100](https://github.com/ros2/message_filters/issues/100))
- Fix python examples ([#99](https://github.com/ros2/message_filters/issues/99))
- feat: add signal time functions to ExactTime policy ([#94](https://github.com/ros2/message_filters/issues/94))
- Contributors: Chris Lalancette, Patrick Roncagliolo, Ricardo de Azambuja, Russ, rkeating-planted

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/jazzy/CHANGELOG.rst)

- Bump vendored mimick version for [ros2/Mimick#32](https://github.com/ros2/Mimick/issues/32) ([#35](https://github.com/ros2/mimick_vendor/issues/35))
- Update to the commit that fixes mmk\_noreturn. ([#34](https://github.com/ros2/mimick_vendor/issues/34))
- Update to the commit the fixes exe stack on macOS. ([#33](https://github.com/ros2/mimick_vendor/issues/33))
- Update to the comment that fixes the executable stack. ([#32](https://github.com/ros2/mimick_vendor/issues/32))
- Update to take advantage of TARGET\_ARCH ([#28](https://github.com/ros2/mimick_vendor/issues/28))
- Switch to ament\_cmake\_vendor\_package ([#31](https://github.com/ros2/mimick_vendor/issues/31))
- Contributors: Chris Lalancette, Michael Carroll, Scott K Logan

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/nav_msgs/CHANGELOG.rst)

- Removed TODO ([#243](https://github.com/ros2/common_interfaces/issues/243))
- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="orocos-kdl-vendor"></a>

## [orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/jazzy/orocos_kdl_vendor/CHANGELOG.rst)

- Ensure that orocos\_kdl\_vendor doesn’t accidentally find itself. ([#27](https://github.com/ros2/orocos_kdl_vendor/issues/27)) ([#28](https://github.com/ros2/orocos_kdl_vendor/issues/28)) When initially building the orocos\_kdl\_vendor package (on platforms where it actually builds), it turns out that it places a valid cmake configuration in the build directory. In turn, that means that a subsequent rebuild will find this configuration in the build directory, and throw the rest of the logic off. This only seems to be a problem with CMake 3.29 and later, though I can’t say exactly why at the moment. Workaround this problem by writing the configuration out to a temporary file, and then moving it into the final place with the final name. (cherry picked from commit 7aad6d1ad9fa54f3a48f1f194a85127e362c8ade) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Update to the latest orocos\_kdl\_kinematics commit. ([#25](https://github.com/ros2/orocos_kdl_vendor/issues/25))
- Switch to ament\_cmake\_vendor\_package ([#20](https://github.com/ros2/orocos_kdl_vendor/issues/20))
- Contributors: Chris Lalancette, Scott K Logan, mergify[bot]

<a id="osrf-pycommon"></a>

## [osrf\_pycommon](https://github.com/osrf/osrf_pycommon/tree/master/CHANGELOG.rst)

- Catch all of the spurious warnings from get\_event\_loop. ([#94](https://github.com/osrf/osrf_pycommon/issues/94))
- Add bookworm as a python3 target ([#91](https://github.com/osrf/osrf_pycommon/issues/91))
- Suppress warning for specifically handled behavior ([#87](https://github.com/osrf/osrf_pycommon/issues/87))
- Update supported platforms ([#93](https://github.com/osrf/osrf_pycommon/issues/93))
- Add GitHub Actions CI workflow ([#88](https://github.com/osrf/osrf_pycommon/issues/88))
- Contributors: Chris Lalancette, Scott K Logan, Tully Foote

<a id="osrf-testing-tools-cpp"></a>

## [osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/jazzy/osrf_testing_tools_cpp/CHANGELOG.rst)

- Upgrade to Google test 1.14.0 ([#84](https://github.com/osrf/osrf_testing_tools_cpp/issues/84))
- Contributors: Chris Lalancette

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/jazzy/pendulum_control/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- [pendulum\_control Install targets to project lib ([#624](https://github.com/ros2/demos/issues/624))
- Contributors: Michael Jeronimo, Yadu

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/jazzy/pendulum_msgs/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/jazzy/pluginlib/CHANGELOG.rst)

- Switch from rcpputils::fs to std::filesystem ([#254](https://github.com/ros/pluginlib/issues/254))
- Remove redundant throw of a std::runtime\_error ([#232](https://github.com/ros/pluginlib/issues/232))
- Update to C++17 ([#251](https://github.com/ros/pluginlib/issues/251))
- Fix wShadow compile warning ([#250](https://github.com/ros/pluginlib/issues/250))
- Contributors: Chris Lalancette, Christophe Bedard, Hunter L. Allen, Steve Macenski

<a id="pybind11-vendor"></a>

## [pybind11\_vendor](https://github.com/ros2/pybind11_vendor/tree/jazzy/CHANGELOG.rst)

- Update to pybind11 2.11.1 ([#28](https://github.com/ros2/pybind11_vendor/issues/28))
- Add Apache 2.0 LICENSE file ([#27](https://github.com/ros2/pybind11_vendor/issues/27))
- Switch to ament\_cmake\_vendor\_package ([#24](https://github.com/ros2/pybind11_vendor/issues/24))
- Contributors: Chris Lalancette, Michael Carroll, Scott K Logan

<a id="python-cmake-module"></a>

## [python\_cmake\_module](https://github.com/ros2/python_cmake_module/tree/jazzy/CHANGELOG.rst)

- Use FindPython3 instead of FindPythonInterp ([#7](https://github.com/ros2/python_cmake_module/issues/7))
- Contributors: Shane Loretz

<a id="python-orocos-kdl-vendor"></a>

## [python\_orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/jazzy/python_orocos_kdl_vendor/CHANGELOG.rst)

- Update to the latest orocos\_kdl\_kinematics commit. ([#25](https://github.com/ros2/orocos_kdl_vendor/issues/25))
- Contributors: Chris Lalancette

<a id="python-qt-binding"></a>

## [python\_qt\_binding](https://github.com/ros-visualization/python_qt_binding/tree/jazzy/CHANGELOG.rst)

- Suppress warning from Shiboken2. (backport [#137](https://github.com/ros-visualization/python_qt_binding/issues/137)) ([#138](https://github.com/ros-visualization/python_qt_binding/issues/138)) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)> Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Switch to C++17 for SIP and Shiboken ([#135](https://github.com/ros-visualization/python_qt_binding/issues/135))
- Set hints to find the python version we actually want. ([#134](https://github.com/ros-visualization/python_qt_binding/issues/134))
- Remove unnecessary parentheses around assert. ([#133](https://github.com/ros-visualization/python_qt_binding/issues/133))
- Switch to FindPython3 in the shiboken\_helper.cmake. ([#132](https://github.com/ros-visualization/python_qt_binding/issues/132))
- Cleanup of the sip\_configure.py file. ([#131](https://github.com/ros-visualization/python_qt_binding/issues/131))
- Update the SIP support so we can deal with a broken RHEL-9. ([#129](https://github.com/ros-visualization/python_qt_binding/issues/129))
- Contributors: Chris Lalancette, Christophe Bedard, mergify[bot]

<a id="qt-dotgraph"></a>

## [qt\_dotgraph](https://github.com/ros-visualization/qt_gui_core/tree/jazzy/qt_dotgraph/CHANGELOG.rst)

- Handle empty dotcode nodes. ([#290](https://github.com/ros-visualization/qt_gui_core/issues/290))
- Small fix for modern flake8. ([#289](https://github.com/ros-visualization/qt_gui_core/issues/289))
- Contributors: Chris Lalancette

<a id="qt-gui"></a>

## [qt\_gui](https://github.com/ros-visualization/qt_gui_core/tree/jazzy/qt_gui/CHANGELOG.rst)

- Remove unnecessary parentheses for assert. ([#286](https://github.com/ros-visualization/qt_gui_core/issues/286))
- (qt\_gui) extended theme logic to get icons ([#279](https://github.com/ros-visualization/qt_gui_core/issues/279))
- Contributors: Chris Lalancette, Matthijs van der Burgh

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/jazzy/qt_gui_cpp/CHANGELOG.rst)

- Switch from rcpputils::fs to std::filesystem ([#288](https://github.com/ros-visualization/qt_gui_core/issues/288))
- Set hints to find the python version we actually want. ([#287](https://github.com/ros-visualization/qt_gui_core/issues/287))
- Update to C++17 ([#278](https://github.com/ros-visualization/qt_gui_core/issues/278))
- fix unload warning ([#274](https://github.com/ros-visualization/qt_gui_core/issues/274))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/jazzy/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Explicit time conversion ([#657](https://github.com/ros2/demos/issues/657))
- Cleanup the interactive quality of service demos. ([#637](https://github.com/ros2/demos/issues/637))
- More quality of service demo cleanup ([#632](https://github.com/ros2/demos/issues/632))
- Fix small typos in the incompatible\_qos demos. ([#629](https://github.com/ros2/demos/issues/629))
- Contributors: AiVerisimilitude, Chris Lalancette, Michael Jeronimo

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/jazzy/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- More quality of service demo cleanup ([#632](https://github.com/ros2/demos/issues/632))
- Fix small typos in the incompatible\_qos demos. ([#629](https://github.com/ros2/demos/issues/629))
- Fix the quality\_of\_service\_demo\_py output to look like the C++ one. ([#626](https://github.com/ros2/demos/issues/626))
- Use non-deprecated rclpy import. ([#615](https://github.com/ros2/demos/issues/615))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/jazzy/rcl/CHANGELOG.rst)

- Fix up rmw\_cyclonedds timestamp testing. ([#1156](https://github.com/ros2/rcl/issues/1156)) ([#1157](https://github.com/ros2/rcl/issues/1157)) We are about to fix it so that rmw\_cyclonedds has receive\_timestamp support, so we also need to enable that support here in rcl. We actually rewrite the logic a bit because now the only combination that doesn’t work is rmw\_connextdds on Windows. (cherry picked from commit 6d53d24a863c3e9e4a41e9fe5f550271210d9d9d) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Fixed warnings - strict-prototypes ([#1148](https://github.com/ros2/rcl/issues/1148)) ([#1150](https://github.com/ros2/rcl/issues/1150))
- chore: Minor style improvements ([#1147](https://github.com/ros2/rcl/issues/1147)) Co-authored-by: Janosch Machowinski <[J.Machowinski@cellumation.com](mailto:J.Machowinski%40cellumation.com)>
- improved rcl\_wait in the area of timeout computation and spurious wakeups ([#1146](https://github.com/ros2/rcl/issues/1146)) Added special handling for timers with a clock that has time override enabled. For these timer we should not compute a timeout, as the waitset is waken up by the associated guard condition. Before this change, the waitset could wait up, because of an expected ready timer, that was acutally not ready, as the time update to the ROS\_TIME had not yet arrived.
- Add tracepoint for publish\_serialized\_publish ([#1136](https://github.com/ros2/rcl/issues/1136)) \* Add tracepoint for publish\_serialized\_publish \* Add: tracepoint for rcl\_take\_serialized\_message ———
- Revert “improved rcl\_wait in the area of timeout computation and spurious wakeups ([#1135](https://github.com/ros2/rcl/issues/1135))” ([#1142](https://github.com/ros2/rcl/issues/1142)) This reverts commit 3c6c5dc47dac23d70722a60b2c0a387d2e71b71d.
- improved rcl\_wait in the area of timeout computation and spurious wakeups ([#1135](https://github.com/ros2/rcl/issues/1135)) \* feat: Allow usage of rcl\_timer\_clock with const rcl\_timer\_t\* \* fix: Fixed purious wake-ups on ROS\_TIME timers with ROS\_TIME enabled Added special handling for timers with a clock that has time override enabled. For theses timer we should not compute a timeout, as the waitset is waken up by the associated guard condition. Before this change, the waitset could wait up, because of an expected ready timer, that was acutally not ready, as the time update to the ROS\_TIME had not yet arrived. \* feat: Added rcl\_timer\_get\_next\_call\_time \* fix(rcl\_wait): Improved timeout computation in case of many timers This commit changes the computation of the timer timeout, to be more precise, in the case, of many registered timers. ——— Co-authored-by: Janosch Machowinski <[j.machowinski@nospam.org](mailto:j.machowinski%40nospam.org)>
- Generate version header using ament\_generate\_version\_header(..) ([#1141](https://github.com/ros2/rcl/issues/1141))
- Add rcl\_timer\_call\_with\_info function that retrieves the expected and the actual timer trigger times ([#1113](https://github.com/ros2/rcl/issues/1113)) Co-authored-by: Alexis Tsogias <[a.tsogias@cellumation.com](mailto:a.tsogias%40cellumation.com)> Co-authored-by: Michael Carroll <[carroll.michael@gmail.com](mailto:carroll.michael%40gmail.com)> Co-authored-by: Tomoya Fujita <[Tomoya.Fujita@sony.com](mailto:Tomoya.Fujita%40sony.com)>
- document out parameters for rcl\_get\_node\_names and rcl\_get\_node\_names\_with\_enclaves ([#1137](https://github.com/ros2/rcl/issues/1137)) \* document out params for rcl\_get\_node\_names Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Cleanups for uncrustify 0.78. ([#1134](https://github.com/ros2/rcl/issues/1134)) Mostly this is expanding macros, as this is just easier to read anyway. But we also mark one section as INDENT-OFF.
- Re-order rcl\_logging\_interface include ([#1133](https://github.com/ros2/rcl/issues/1133))
- Remove unnecessary macros. ([#1132](https://github.com/ros2/rcl/issues/1132)) These really don’t add anything, and allows us to avoid some changes in macro formatting between Ubuntu 22.04 and Ubuntu 24.04.
- Update quality declaration documents ([#1131](https://github.com/ros2/rcl/issues/1131))
- add unit tests for –log-file-name argument. ([#1130](https://github.com/ros2/rcl/issues/1130))
- support `--log-file-name` to ros args. ([#1127](https://github.com/ros2/rcl/issues/1127))
- Make sure to disable a test\_node test on RHEL. ([#1124](https://github.com/ros2/rcl/issues/1124))
- remove static function rcl\_ret\_from\_rcutils\_ret(). ([#1122](https://github.com/ros2/rcl/issues/1122))
- Remove AMENT\_DEPENDENCIES from rcl\_add\_custom\_gtest. ([#1119](https://github.com/ros2/rcl/issues/1119))
- Remove unncecessary dependencies in tests ([#1114](https://github.com/ros2/rcl/issues/1114))
- a rosout publisher of a node might not exist ([#1115](https://github.com/ros2/rcl/issues/1115))
- Set disable loan to on by default. ([#1110](https://github.com/ros2/rcl/issues/1110))
- Return service from node\_type\_description\_service\_init ([#1112](https://github.com/ros2/rcl/issues/1112))
- next\_call\_time will always be greater than now after calling rcl\_timer\_call. ([#1089](https://github.com/ros2/rcl/issues/1089))
- Add rcl count clients, servicec & tests ([#1011](https://github.com/ros2/rcl/issues/1011))
- Improve the reliability of test\_get\_type\_description\_service. ([#1107](https://github.com/ros2/rcl/issues/1107))
- Remove most remaining uses of ament\_target\_dependencies. ([#1102](https://github.com/ros2/rcl/issues/1102))
- Just remove rcpputils::fs dependency ([#1105](https://github.com/ros2/rcl/issues/1105))
- Decouple rosout publisher init from node init. ([#1065](https://github.com/ros2/rcl/issues/1065))
- Cleanup the error handling in rcl\_node\_init. ([#1099](https://github.com/ros2/rcl/issues/1099))
- Fix a clang warning for suspicious string concatentation. ([#1101](https://github.com/ros2/rcl/issues/1101))
- add the link to the topic name rules. ([#1100](https://github.com/ros2/rcl/issues/1100))
- Cut down the amount of time for test\_logging\_rosout. ([#1098](https://github.com/ros2/rcl/issues/1098))
- Simplify local\_namespace handling in rcl\_node\_init. ([#1097](https://github.com/ros2/rcl/issues/1097))
- Reduce the number of tests we run ([#1096](https://github.com/ros2/rcl/issues/1096))
- Adding duplicate node information ([#1088](https://github.com/ros2/rcl/issues/1088))
- Revamp the test\_get\_type\_description\_service. ([#1095](https://github.com/ros2/rcl/issues/1095))
- Cleanup network flow endpoints test. ([#1094](https://github.com/ros2/rcl/issues/1094))
- Reduce the failure timeout time for namespaces. ([#1093](https://github.com/ros2/rcl/issues/1093))
- Shorten wait time for a subscription not being ready. ([#1092](https://github.com/ros2/rcl/issues/1092))
- rcl\_send\_response returns RCL\_RET\_TIMEOUT. ([#1048](https://github.com/ros2/rcl/issues/1048))
- Move test\_namespace into the correct directory. ([#1087](https://github.com/ros2/rcl/issues/1087))
- Reset errors in tests to reduce warnings ([#1085](https://github.com/ros2/rcl/issues/1085))
- Cleanup error reporting in the type hash code. ([#1084](https://github.com/ros2/rcl/issues/1084))
- Instrument loaned message publication code path ([#1083](https://github.com/ros2/rcl/issues/1083))
- Add `~/get_type_description` service (rep2011) ([#1052](https://github.com/ros2/rcl/issues/1052))
- Modifies timers API to select autostart state ([#1004](https://github.com/ros2/rcl/issues/1004))
- test publisher/subscription with the c/cpp typesupport for test\_msgs::msg::array ([#1074](https://github.com/ros2/rcl/issues/1074))
- validation result should be used to print the error message. ([#1077](https://github.com/ros2/rcl/issues/1077))
- improve error msg of `rcl_expand_topic_name` ([#1076](https://github.com/ros2/rcl/issues/1076))
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#1058](https://github.com/ros2/rcl/issues/1058))
- fix comment ([#1073](https://github.com/ros2/rcl/issues/1073))
- localhost\_only prevails auto discovery options if enabled. ([#1069](https://github.com/ros2/rcl/issues/1069))
- Avoid dynamic allocation of message before sending over rosout ([#1067](https://github.com/ros2/rcl/issues/1067))
- clarify `rcl_node_init` return code ([#1066](https://github.com/ros2/rcl/issues/1066))
- Fix a format-security warning when building with clang. ([#1064](https://github.com/ros2/rcl/issues/1064))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Christopher Wecht, Eloy Briceno, Eric W, Felix Penzlin, G.A. vd. Hoorn, Hans-Joachim Krauch, Kenta Yonekura, Lee, Lucas Wendland, Michael Carroll, Minju, Thiemo Kohrt, Tomoya Fujita, h-suzuki-isp, jmachowinski, mergify[bot]

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/jazzy/rcl_action/CHANGELOG.rst)

- Generate version header using ament\_generate\_version\_header(..) ([#1141](https://github.com/ros2/rcl/issues/1141))
- add RCL\_RET\_TIMEOUT to action service response. ([#1138](https://github.com/ros2/rcl/issues/1138)) \* add RCL\_RET\_TIMEOUT to action service response. \* address review comment. ———
- Update quality declaration documents ([#1131](https://github.com/ros2/rcl/issues/1131))
- Remove most remaining uses of ament\_target\_dependencies. ([#1102](https://github.com/ros2/rcl/issues/1102))
- Add `~/get_type_description` service (rep2011) ([#1052](https://github.com/ros2/rcl/issues/1052))
- Modifies timers API to select autostart state ([#1004](https://github.com/ros2/rcl/issues/1004))
- Contributors: Chris Lalancette, Christophe Bedard, Eloy Briceno, G.A. vd. Hoorn, Hans-Joachim Krauch, Tomoya Fujita

<a id="rcl-interfaces"></a>

## [rcl\_interfaces](https://github.com/ros2/rcl_interfaces/tree/jazzy/rcl_interfaces/CHANGELOG.rst)

- Update the Log.msg constant types. ([#161](https://github.com/ros2/rcl_interfaces/issues/161))
- Update the comments for SetParametersResult to reflect reality. ([#159](https://github.com/ros2/rcl_interfaces/issues/159))
- Contributors: Chris Lalancette

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/jazzy/rcl_lifecycle/CHANGELOG.rst)

- Fixed warnings - strict-prototypes ([#1148](https://github.com/ros2/rcl/issues/1148)) ([#1150](https://github.com/ros2/rcl/issues/1150))
- Generate version header using ament\_generate\_version\_header(..) ([#1141](https://github.com/ros2/rcl/issues/1141))
- Update quality declaration documents ([#1131](https://github.com/ros2/rcl/issues/1131))
- Remove most remaining uses of ament\_target\_dependencies. ([#1102](https://github.com/ros2/rcl/issues/1102))
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#1058](https://github.com/ros2/rcl/issues/1058))
- Contributors: Chris Lalancette, Christophe Bedard, G.A. vd. Hoorn, mergify[bot]

<a id="rcl-logging-interface"></a>

## [rcl\_logging\_interface](https://github.com/ros2/rcl_logging/tree/jazzy/rcl_logging_interface/CHANGELOG.rst)

- Check allocator validity in some rcl\_logging functions ([#116](https://github.com/ros2/rcl_logging/issues/116)) If the allocator is zero-initialized, it may cause a segfault when it is used later in the functions.
- Use (void) in declaration of param-less function ([#114](https://github.com/ros2/rcl_logging/issues/114))
- add file\_name\_prefix parameter to external log configuration. ([#109](https://github.com/ros2/rcl_logging/issues/109))
- Migrate to std::filesystem ([#104](https://github.com/ros2/rcl_logging/issues/104))
- Remove the last uses of ament\_target\_dependencies in this repo. ([#102](https://github.com/ros2/rcl_logging/issues/102))
- Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura, Scott K Logan, Tomoya Fujita

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/jazzy/rcl_logging_noop/CHANGELOG.rst)

- add file\_name\_prefix parameter to external log configuration. ([#109](https://github.com/ros2/rcl_logging/issues/109))
- Remove the last uses of ament\_target\_dependencies in this repo. ([#102](https://github.com/ros2/rcl_logging/issues/102))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/jazzy/rcl_logging_spdlog/CHANGELOG.rst)

- Check allocator validity in some rcl\_logging functions ([#116](https://github.com/ros2/rcl_logging/issues/116)) If the allocator is zero-initialized, it may cause a segfault when it is used later in the functions.
- Cleanup the tests. ([#115](https://github.com/ros2/rcl_logging/issues/115)) \* Cleanup the tests. There are a few different fixes in here: 1. Move away from using “popen” to get the list of files in a directory. Instead, switch to using the C++ std::filesystem directory iterator and doing the work ourselves, which is portable and much less error-prone. 2. Set the ROS\_LOG\_DIR for all of the tests in here. This should make the test resistant to being run in parallel with other tests. 3. Consistently use rcpputils::set\_env\_var, rather than a mix of rcpputils and rcutils.
- Update quality declaration document ([#112](https://github.com/ros2/rcl_logging/issues/112))
- Re-order rcl\_logging\_interface include ([#111](https://github.com/ros2/rcl_logging/issues/111))
- add file\_name\_prefix parameter to external log configuration. ([#109](https://github.com/ros2/rcl_logging/issues/109))
- Migrate to std::filesystem ([#104](https://github.com/ros2/rcl_logging/issues/104))
- Remove the last uses of ament\_target\_dependencies in this repo. ([#102](https://github.com/ros2/rcl_logging/issues/102))
- Contributors: Chris Lalancette, Christophe Bedard, Kenta Yonekura, Scott K Logan, Tomoya Fujita

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/jazzy/rcl_yaml_param_parser/CHANGELOG.rst)

- Generate version header using ament\_generate\_version\_header(..) ([#1141](https://github.com/ros2/rcl/issues/1141))
- Update quality declaration documents ([#1131](https://github.com/ros2/rcl/issues/1131))
- Fix for incorrect integer value conversion on Windows ([#1126](https://github.com/ros2/rcl/issues/1126))
- Just remove rcpputils::fs dependency ([#1105](https://github.com/ros2/rcl/issues/1105))
- Contributors: Christophe Bedard, G.A. vd. Hoorn, Kenta Yonekura, Michael Orlov

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/jazzy/rclcpp/CHANGELOG.rst)

- add impl pointer for ExecutorOptions ([#2523](https://github.com/ros2/rclcpp/issues/2523)) ([#2525](https://github.com/ros2/rclcpp/issues/2525)) \* add impl pointer for ExecutorOptions (cherry picked from commit 343b29b617b163ad72b9fe3f6441dd4ed3d3af09) Co-authored-by: William Woodall <[william@osrfoundation.org](mailto:william%40osrfoundation.org)>
- Fixup Executor::spin\_all() regression fix ([#2517](https://github.com/ros2/rclcpp/issues/2517)) ([#2521](https://github.com/ros2/rclcpp/issues/2521)) \* test(Executors): Added tests for busy waiting Checks if executors are busy waiting while they should block in spin\_some or spin\_all. \* fix: Reworked spinAll test This test was strange. It looked like, it assumed that spin\_all did not return instantly. Also it was racy, as the thread could terminate instantly. \* fix(Executor): Fixed spin\_all not returning instantly is no work was available \* Update rclcpp/test/rclcpp/executors/test\_executors.cpp \* test(executors): Added test for busy waiting while calling spin \* fix(executor): Reset wait\_result on every call to spin\_some\_impl Before, the method would not recollect available work in case of spin\_some, spin\_all. This would lead to the method behaving differently than to what the documentation states. \* restore previous test logic for now \* refactor spin\_some\_impl’s logic and improve busy wait tests \* added some more comments about the implementation ——— Co-authored-by: Janosch Machowinski <[J.Machowinski@cellumation.com](mailto:J.Machowinski%40cellumation.com)> Co-authored-by: jmachowinski <[jmachowinski@users.noreply.github.com](mailto:jmachowinski%40users.noreply.github.com)> Co-authored-by: Tomoya Fujita <[Tomoya.Fujita@sony.com](mailto:Tomoya.Fujita%40sony.com)> Co-authored-by: William Woodall <[william@osrfoundation.org](mailto:william%40osrfoundation.org)>
- Revise the description of service configure\_introspection() ([#2511](https://github.com/ros2/rclcpp/issues/2511)) ([#2513](https://github.com/ros2/rclcpp/issues/2513))
- Remove references to index.ros.org. ([#2504](https://github.com/ros2/rclcpp/issues/2504))
- Reduce overhead for inheriting from rclcpp::Executor when base functionality is not reused ([#2506](https://github.com/ros2/rclcpp/issues/2506))
- [wjwwood] Updated “Data race fixes” ([#2500](https://github.com/ros2/rclcpp/issues/2500)) \* Fix callback group logic in executor \* fix: Fixed unnecessary copy of wait\_set \* fix(executor): Fixed race conditions with rebuild of wait\_sets Before this change, the rebuild of wait set would be triggered after the wait set was waken up. With bad timing, this could lead to the rebuild not happening with multi threaded executor. \* fix(Executor): Fixed lost of entities rebuild request \* chore: Added assert for not set callback\_group in execute\_any\_executable \* Add test for cbg getting reset Co-authored-by: Janosch Machowinski <[j.machowinski@nospam.org](mailto:j.machowinski%40nospam.org)> \* chore: renamed test cases to snake\_case \* style \* fixup test to avoid polling and short timeouts \* fix: Use correct notify\_waitable\_ instance \* fix(StaticSingleThreadedExecutor): Added missing special case handling for current\_notify\_waitable\_ \* fix(TestCallbackGroup): Fixed test after change to timers ——— Co-authored-by: Janosch Machowinski <[j.machowinski@cellumation.com](mailto:j.machowinski%40cellumation.com)> Co-authored-by: Michael Carroll <[mjcarroll@intrinsic.ai](mailto:mjcarroll%40intrinsic.ai)> Co-authored-by: Janosch Machowinski <[j.machowinski@nospam.org](mailto:j.machowinski%40nospam.org)>
- fixup var names to snake case ([#2501](https://github.com/ros2/rclcpp/issues/2501))
- Added optional TimerInfo to timer callback ([#2343](https://github.com/ros2/rclcpp/issues/2343)) Co-authored-by: Alexis Tsogias <[a.tsogias@cellumation.com](mailto:a.tsogias%40cellumation.com)> Co-authored-by: Janosch Machowinski <[J.Machowinski@cellumation.com](mailto:J.Machowinski%40cellumation.com)>
- Fix uninitialized memory in test ([#2498](https://github.com/ros2/rclcpp/issues/2498)) When I added in the tests for large messages, I made a mistake and reserved space in the strings, but didn’t actually expand it. Thus, we were writing into uninitialized memory. Fix this by just using the correct constructor for string, which will allocate and initialize the memory properly.
- Ensure waitables handle guard condition retriggering ([#2483](https://github.com/ros2/rclcpp/issues/2483)) Co-authored-by: Michael Carroll <[mjcarroll@intrinsic.ai](mailto:mjcarroll%40intrinsic.ai)>
- fix: init concatenated\_vector with begin() & end() ([#2492](https://github.com/ros2/rclcpp/issues/2492)) \* this commit will fix the warning [-Wstringop-overflow=] [#2461](https://github.com/ros2/rclcpp/issues/2461)
- Use the same context for the specified node in rclcpp::spin functions ([#2433](https://github.com/ros2/rclcpp/issues/2433)) \* Use the same conext for the specified node in rclcpp::spin\_xx functions \* Add test for spinning with non-default-context \* Format code ———
- Disable compare-function-pointers in test\_utilities ([#2489](https://github.com/ros2/rclcpp/issues/2489))
- address ambiguous auto variable. ([#2481](https://github.com/ros2/rclcpp/issues/2481))
- Increase the cppcheck timeout to 1200 seconds ([#2484](https://github.com/ros2/rclcpp/issues/2484))
- Removed test\_timers\_manager clang warning ([#2479](https://github.com/ros2/rclcpp/issues/2479))
- Flaky timer test fix ([#2469](https://github.com/ros2/rclcpp/issues/2469)) \* fix(time\_source): Fixed possible race condition \* fix(test\_executors\_time\_cancel\_behaviour): Fixed multiple race conditions ——— Co-authored-by: Janosch Machowinski <[j.machowinski@nospam.org](mailto:j.machowinski%40nospam.org)>
- Add tracepoint for generic publisher/subscriber ([#2448](https://github.com/ros2/rclcpp/issues/2448))
- update rclcpp::Waitable API to use references and const ([#2467](https://github.com/ros2/rclcpp/issues/2467))
- Utilize rclcpp::WaitSet as part of the executors ([#2142](https://github.com/ros2/rclcpp/issues/2142)) \* Deprecate callback\_group call taking context \* Add base executor objects that can be used by implementors \* Template common operations \* Address reviewer feedback: \* Add callback to EntitiesCollector constructor \* Make function to check automatically added callback groups take a list \* Lint \* Address reviewer feedback and fix templates \* Lint and docs \* Make executor own the notify waitable \* Add pending queue to collector, remove from waitable Also change node’s get\_guard\_condition to return shared\_ptr \* Change interrupt guard condition to shared\_ptr Check if guard condition is valid before adding it to the waitable \* Lint and docs \* Utilize rclcpp::WaitSet as part of the executors \* Don’t exchange atomic twice \* Fix add\_node and add more tests \* Make get\_notify\_guard\_condition follow API tick-tock \* Improve callback group tick-tocking \* Don’t lock twice \* Address reviewer feedback \* Add thread safety annotations and make locks consistent \* @wip \* Reset callback groups for multithreaded executor \* Avoid many small function calls when building executables \* Re-trigger guard condition if buffer has data \* Address reviewer feedback \* Trace points \* Remove tracepoints \* Reducing diff \* Reduce diff \* Uncrustify \* Restore tests \* Back to weak\_ptr and reduce test time \* reduce diff and lint \* Restore static single threaded tests that weren’t working before \* Restore more tests \* Fix multithreaded test \* Fix assert \* Fix constructor test \* Change ready\_executables signature back \* Don’t enforce removing callback groups before nodes \* Remove the “add\_valid\_node” API \* Only notify if the trigger condition is valid \* Only trigger if valid and needed \* Fix spin\_some/spin\_all implementation \* Restore single threaded executor \* Picking ABI-incompatible executor changes \* Add PIMPL \* Additional waitset prune \* Fix bad merge \* Expand test timeout \* Introduce method to clear expired entities from a collection \* Make sure to call remove\_expired\_entities(). \* Prune queued work when callback group is removed \* Prune subscriptions from dynamic storage \* Styles fixes. \* Re-trigger guard conditions \* Condense to just use watiable.take\_data \* Lint \* Address reviewer comments (nits) \* Lock mutex when copying \* Refactors to static single threaded based on reviewers \* More small refactoring \* Lint \* Lint \* Add ready executable accessors to WaitResult \* Make use of accessors from wait\_set \* Fix tests \* Fix more tests \* Tidy up single threaded executor implementation \* Don’t null out timer, rely on call \* change how timers are checked from wait result in executors \* peak -> peek \* fix bug in next\_waitable logic \* fix bug in StaticSTE that broke the add callback groups to executor tests \* style ——— Co-authored-by: Chris Lalancette <clalancette@gmail.com> Co-authored-by: William Woodall <william@osrfoundation.org>
- fix flakiness in TestTimersManager unit-test ([#2468](https://github.com/ros2/rclcpp/issues/2468)) the previous version of the test was relying on the assumption that a timer with 1ms period gets called at least 6 times if the main thread waits 15ms. this is true most of the times, but it’s not guaranteed, especially when running the test on windows CI servers. the new version of the test makes no assumptions on how much time it takes for the timers manager to invoke the timers, but rather focuses on ensuring that they are called the right amount of times, which is what’s important for the purpose of the test
- fix spin\_some\_max\_duration unit-test for events-executor ([#2465](https://github.com/ros2/rclcpp/issues/2465))
- refactor and improve the parameterized spin\_some tests for executors ([#2460](https://github.com/ros2/rclcpp/issues/2460)) \* refactor and improve the spin\_some parameterized tests for executors \* disable spin\_some\_max\_duration for the StaticSingleThreadedExecutor and EventsExecutor \* fixup and clarify the docstring for Executor::spin\_some() \* style \* review comments ———
- enable simulation clock for timer canceling test. ([#2458](https://github.com/ros2/rclcpp/issues/2458)) \* enable simulation clock for timer canceling test. \* move MainExecutorTypes to test\_executors\_timer\_cancel\_behavior.cpp. ———
- Revert “relax the test simulation rate for timer canceling tests. ([#2453](https://github.com/ros2/rclcpp/issues/2453))” ([#2456](https://github.com/ros2/rclcpp/issues/2456)) This reverts commit 1c350d0d7fb9c7158e0a39057112486ddbd38e9a.
- relax the test simulation rate for timer canceling tests. ([#2453](https://github.com/ros2/rclcpp/issues/2453))
- Fix TypeAdapted publishing with large messages. ([#2443](https://github.com/ros2/rclcpp/issues/2443)) Mostly by ensuring we aren’t attempting to store large messages on the stack. Also add in tests. I verified that before these changes, the tests failed, while after them they succeed.
- Implement generic client ([#2358](https://github.com/ros2/rclcpp/issues/2358)) \* Implement generic client \* Fix the incorrect parameter declaration \* Deleted copy constructor and assignment for FutureAndRequestId \* Update codes after rebase \* Address review comments \* Address review comments from iuhilnehc-ynos \* Correct an error in a description \* Fix window build errors \* Address review comments from William \* Add doc strings to create\_generic\_client ———
- Rule of five: implement move operators ([#2425](https://github.com/ros2/rclcpp/issues/2425))
- Various cleanups to deal with uncrustify 0.78. ([#2439](https://github.com/ros2/rclcpp/issues/2439)) These should also work with uncrustify 0.72.
- Remove the set\_deprecated signatures in any\_subscription\_callback. ([#2431](https://github.com/ros2/rclcpp/issues/2431)) These have been deprecated since April 2021, so it is safe to remove them now.
- fix doxygen syntax for NodeInterfaces ([#2428](https://github.com/ros2/rclcpp/issues/2428))
- Set hints to find the python version we actually want. ([#2426](https://github.com/ros2/rclcpp/issues/2426)) The comment in the commit explains the reasoning behind it.
- Update quality declaration documents ([#2427](https://github.com/ros2/rclcpp/issues/2427))
- feat: add/minus for msg::Time and rclcpp::Duration ([#2419](https://github.com/ros2/rclcpp/issues/2419)) \* feat: add/minus for msg::Time and rclcpp::Duration
- Split test\_executors up into smaller chunks. ([#2421](https://github.com/ros2/rclcpp/issues/2421))
- [events executor] - Fix Behavior with Timer Cancel ([#2375](https://github.com/ros2/rclcpp/issues/2375))
- Removed deprecated header ([#2413](https://github.com/ros2/rclcpp/issues/2413))
- Make sure to mark RingBuffer methods as ‘override’. ([#2410](https://github.com/ros2/rclcpp/issues/2410))
- Increase the cppcheck timeout to 600 seconds. ([#2409](https://github.com/ros2/rclcpp/issues/2409))
- Add transient local durability support to publisher and subscriptions when using intra-process communication ([#2303](https://github.com/ros2/rclcpp/issues/2303))
- Stop storing the context in the guard condition. ([#2400](https://github.com/ros2/rclcpp/issues/2400))
- Updated GenericSubscription to AnySubscriptionCallback ([#1928](https://github.com/ros2/rclcpp/issues/1928))
- make type support helper supported for service ([#2209](https://github.com/ros2/rclcpp/issues/2209))
- Adding QoS to subscription options ([#2323](https://github.com/ros2/rclcpp/issues/2323))
- Switch to target\_link\_libraries. ([#2374](https://github.com/ros2/rclcpp/issues/2374))
- aligh with rcl that a rosout publisher of a node might not exist ([#2357](https://github.com/ros2/rclcpp/issues/2357))
- Fix data race in EventHandlerBase ([#2349](https://github.com/ros2/rclcpp/issues/2349))
- Support users holding onto shared pointers in the message memory pool ([#2336](https://github.com/ros2/rclcpp/issues/2336))
- fix (signal\_handler.hpp): spelling ([#2356](https://github.com/ros2/rclcpp/issues/2356))
- Updates to not use std::move in some places. ([#2353](https://github.com/ros2/rclcpp/issues/2353))
- rclcpp::Time::max() clock type support. ([#2352](https://github.com/ros2/rclcpp/issues/2352))
- Serialized Messages with Topic Statistics ([#2274](https://github.com/ros2/rclcpp/issues/2274))
- Add a custom deleter when constructing rcl\_service\_t ([#2351](https://github.com/ros2/rclcpp/issues/2351))
- Disable the loaned messages inside the executor. ([#2335](https://github.com/ros2/rclcpp/issues/2335))
- Use message\_info in SubscriptionTopicStatistics instead of typed message ([#2337](https://github.com/ros2/rclcpp/issues/2337))
- Add missing ‘enable\_rosout’ comments ([#2345](https://github.com/ros2/rclcpp/issues/2345))
- Adjust rclcpp usage of type description service ([#2344](https://github.com/ros2/rclcpp/issues/2344))
- address rate related flaky tests. ([#2329](https://github.com/ros2/rclcpp/issues/2329))
- Fixes pointed out by the clang analyzer. ([#2339](https://github.com/ros2/rclcpp/issues/2339))
- Remove useless ROSRate class ([#2326](https://github.com/ros2/rclcpp/issues/2326))
- add clients & services count ([#2072](https://github.com/ros2/rclcpp/issues/2072))
- remove invalid sized allocation test for SerializedMessage. ([#2330](https://github.com/ros2/rclcpp/issues/2330))
- Adding API to copy all parameters from one node to another ([#2304](https://github.com/ros2/rclcpp/issues/2304))
- Add locking to protect the TimeSource::NodeState::node\_base\_ ([#2320](https://github.com/ros2/rclcpp/issues/2320))
- Update SignalHandler get\_global\_signal\_handler to avoid complex types in static memory ([#2316](https://github.com/ros2/rclcpp/issues/2316))
- Removing Old Connext Tests ([#2313](https://github.com/ros2/rclcpp/issues/2313))
- Documentation for list\_parameters ([#2315](https://github.com/ros2/rclcpp/issues/2315))
- Decouple rosout publisher init from node init. ([#2174](https://github.com/ros2/rclcpp/issues/2174))
- fix the depth to relative in list\_parameters ([#2300](https://github.com/ros2/rclcpp/issues/2300))
- Fix the return type of Rate::period. ([#2301](https://github.com/ros2/rclcpp/issues/2301))
- Update API docs links in package READMEs ([#2302](https://github.com/ros2/rclcpp/issues/2302))
- Cleanup flaky timers\_manager tests. ([#2299](https://github.com/ros2/rclcpp/issues/2299))
- Topic correct typeadapter deduction ([#2294](https://github.com/ros2/rclcpp/issues/2294))
- Fix C++20 allocator construct deprecation ([#2292](https://github.com/ros2/rclcpp/issues/2292))
- Make Rate to select the clock to work with ([#2123](https://github.com/ros2/rclcpp/issues/2123))
- Correct the position of a comment. ([#2290](https://github.com/ros2/rclcpp/issues/2290))
- Remove unnecessary lambda captures in the tests. ([#2289](https://github.com/ros2/rclcpp/issues/2289))
- Add rcl\_logging\_interface as an explicit dependency. ([#2284](https://github.com/ros2/rclcpp/issues/2284))
- Revamp list\_parameters to be more efficient and easier to read. ([#2282](https://github.com/ros2/rclcpp/issues/2282))
- Do not crash Executor when send\_response fails due to client failure. ([#2276](https://github.com/ros2/rclcpp/issues/2276))
- Adding Custom Unknown Type Error ([#2272](https://github.com/ros2/rclcpp/issues/2272))
- Add a pimpl inside rclcpp::Node for future distro backports ([#2228](https://github.com/ros2/rclcpp/issues/2228))
- Remove an unused variable from the events executor tests. ([#2270](https://github.com/ros2/rclcpp/issues/2270))
- Add spin\_all shortcut ([#2246](https://github.com/ros2/rclcpp/issues/2246))
- Adding Missing Group Exceptions ([#2256](https://github.com/ros2/rclcpp/issues/2256))
- Change associated clocks storage to unordered\_set ([#2257](https://github.com/ros2/rclcpp/issues/2257))
- associated clocks should be protected by mutex. ([#2255](https://github.com/ros2/rclcpp/issues/2255))
- Instrument loaned message publication code path ([#2240](https://github.com/ros2/rclcpp/issues/2240))
- Implement get\_node\_type\_descriptions\_interface for lifecyclenode and add smoke test for it ([#2237](https://github.com/ros2/rclcpp/issues/2237))
- Add new node interface TypeDescriptionsInterface to provide GetTypeDescription service ([#2224](https://github.com/ros2/rclcpp/issues/2224))
- Move always\_false\_v to detail namespace ([#2232](https://github.com/ros2/rclcpp/issues/2232))
- Revamp the test\_subscription.cpp tests. ([#2227](https://github.com/ros2/rclcpp/issues/2227))
- warning: comparison of integer expressions of different signedness ([#2219](https://github.com/ros2/rclcpp/issues/2219))
- Modifies timers API to select autostart state ([#2005](https://github.com/ros2/rclcpp/issues/2005))
- Enable callback group tests for connextdds ([#2182](https://github.com/ros2/rclcpp/issues/2182))
- Fix up misspellings of “receive”. ([#2208](https://github.com/ros2/rclcpp/issues/2208))
- Remove flaky stressAddRemoveNode test ([#2206](https://github.com/ros2/rclcpp/issues/2206))
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#2162](https://github.com/ros2/rclcpp/issues/2162))
- remove nolint since ament\_cpplint updated for the c++17 header ([#2198](https://github.com/ros2/rclcpp/issues/2198))
- Feature/available capacity of ipm ([#2173](https://github.com/ros2/rclcpp/issues/2173))
- add mutex to protect events\_executor current entity collection ([#2187](https://github.com/ros2/rclcpp/issues/2187))
- Declare rclcpp callbacks before the rcl entities ([#2024](https://github.com/ros2/rclcpp/issues/2024))
- Fix race condition in events-executor ([#2177](https://github.com/ros2/rclcpp/issues/2177))
- Add missing stdexcept include ([#2186](https://github.com/ros2/rclcpp/issues/2186))
- Fix a format-security warning when building with clang ([#2171](https://github.com/ros2/rclcpp/issues/2171))
- Fix delivered message kind ([#2175](https://github.com/ros2/rclcpp/issues/2175))
- Contributors: AiVerisimilitude, Alberto Soragna, Alejandro Hernández Cordero, Alexey Merzlyakov, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Christopher Wecht, DensoADAS, Eloy Briceno, Emerson Knapp, Homalozoa X, HuaTsai, Jeffery Hsu, Jiaqi Li, Jonas Otto, Kotaro Yoshimoto, Lee, Luca Della Vedova, Lucas Wendland, Matt Condino, Michael Carroll, Michael Orlov, Minju, Nathan Wiebe Neufeldt, Steve Macenski, Tim Clephas, Tomoya Fujita, Tony Najjar, Tully Foote, William Woodall, Zard-C, h-suzuki-isp, jmachowinski, mauropasse, mergify[bot], methylDragon, Øystein Sture

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/jazzy/rclcpp_action/CHANGELOG.rst)

- Remove references to index.ros.org. ([#2504](https://github.com/ros2/rclcpp/issues/2504))
- Callback after cancel ([#2281](https://github.com/ros2/rclcpp/issues/2281)) \* feat(Client): Added function to stop callbacks of a goal handle This function allows us to drop the handle in a locked context. If we do not do this within a lock, there will be a race condition between the deletion of the shared\_ptr of the handle and the result / feedback callbacks. \* fix: make Client goal handle recursive This fixes deadlocks due to release of goal handles in callbacks etc. \* fix(ActionGoalClient): Fixed memory leak for nominal case This fixes a memory leak due to a self reference in the ClientGoalHandle. Note, this fix will only work, if the ClientGoalHandle ever receives a result callback. \* doc: Updated documentation of rclcpp\_action::Client::async\_send\_goal \* docs: Made the async\_send\_goal documentation more explicit Co-authored-by: Janosch Machowinski <J.Machowinski@cellumation.com>
- Remake of “fix: Fixed race condition in action server between is\_ready and take” ([#2495](https://github.com/ros2/rclcpp/issues/2495)) Some background information: is\_ready, take\_data and execute data may be called from different threads in any order. The code in the old state expected them to be called in series, without interruption. This lead to multiple race conditions, as the state of the pimpl objects was altered by the three functions in a non thread safe way. Co-authored-by: Janosch Machowinski <[j.machowinski@nospam.org](mailto:j.machowinski%40nospam.org)>
- update rclcpp::Waitable API to use references and const ([#2467](https://github.com/ros2/rclcpp/issues/2467))
- Do not generate the exception when action service response timeout. ([#2464](https://github.com/ros2/rclcpp/issues/2464)) \* Do not generate the exception when action service response timeout. \* address review comment. ———
- Modify rclcpp\_action::GoalUUID hashing algorithm ([#2441](https://github.com/ros2/rclcpp/issues/2441)) \* Add unit tests for hashing rclcpp\_action::GoalUUID’s \* Use the FNV-1a hash algorithm for Goal UUID
- Various cleanups to deal with uncrustify 0.78. ([#2439](https://github.com/ros2/rclcpp/issues/2439)) These should also work with uncrustify 0.72.
- Update quality declaration documents ([#2427](https://github.com/ros2/rclcpp/issues/2427))
- Switch to target\_link\_libraries. ([#2374](https://github.com/ros2/rclcpp/issues/2374))
- Update API docs links in package READMEs ([#2302](https://github.com/ros2/rclcpp/issues/2302))
- fix(ClientGoalHandle): Made mutex recursive to prevent deadlocks ([#2267](https://github.com/ros2/rclcpp/issues/2267))
- Correct the position of a comment. ([#2290](https://github.com/ros2/rclcpp/issues/2290))
- Fix a typo in a comment. ([#2283](https://github.com/ros2/rclcpp/issues/2283))
- doc fix: call `canceled` only after goal state is in canceling. ([#2266](https://github.com/ros2/rclcpp/issues/2266))
- Contributors: Chris Lalancette, Christophe Bedard, Jiaqi Li, Tomoya Fujita, William Woodall, jmachowinski, mauropasse

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/jazzy/rclcpp_components/CHANGELOG.rst)

- Remove references to index.ros.org. ([#2504](https://github.com/ros2/rclcpp/issues/2504))
- Add EXECUTOR docs ([#2440](https://github.com/ros2/rclcpp/issues/2440))
- Update quality declaration documents ([#2427](https://github.com/ros2/rclcpp/issues/2427))
- crash on no class found ([#2415](https://github.com/ros2/rclcpp/issues/2415)) \* crash on no class found \* error on no class found instead of no callback groups Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Switch to target\_link\_libraries. ([#2374](https://github.com/ros2/rclcpp/issues/2374))
- feat(rclcpp\_components): support events executor in node main template ([#2366](https://github.com/ros2/rclcpp/issues/2366))
- fix(rclcpp\_components): increase the service queue sizes in component\_container ([#2363](https://github.com/ros2/rclcpp/issues/2363))
- Add missing header required by the rclcpp::NodeOptions type ([#2324](https://github.com/ros2/rclcpp/issues/2324))
- Update API docs links in package READMEs ([#2302](https://github.com/ros2/rclcpp/issues/2302))
- Contributors: Adam Aposhian, Chris Lalancette, Christophe Bedard, Daisuke Nishimatsu, Ignacio Vizzo, M. Fatih Cırıt, Ruddick Lawrence

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/jazzy/rclcpp_lifecycle/CHANGELOG.rst)

- Revert “call shutdown in LifecycleNode dtor to avoid leaving the device in un… ([#2450](https://github.com/ros2/rclcpp/issues/2450))” ([#2522](https://github.com/ros2/rclcpp/issues/2522)) ([#2524](https://github.com/ros2/rclcpp/issues/2524)) This reverts commit 04ea0bb00293387791522590b7347a2282cda290. (cherry picked from commit 42b0b5775b4e68718c5949308c9e1a059930ded7) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Remove references to index.ros.org. ([#2504](https://github.com/ros2/rclcpp/issues/2504))
- call shutdown in LifecycleNode dtor to avoid leaving the device in un… ([#2450](https://github.com/ros2/rclcpp/issues/2450)) \* call shutdown in LifecycleNode dtor to avoid leaving the device in unknown state. \* add test to verify LifecycleNode::shutdown is called on destructor. ———
- Update quality declaration documents ([#2427](https://github.com/ros2/rclcpp/issues/2427))
- Increase timeout for rclcpp\_lifecycle to 360 ([#2395](https://github.com/ros2/rclcpp/issues/2395))
- Fix rclcpp\_lifecycle inclusion on Windows. ([#2331](https://github.com/ros2/rclcpp/issues/2331))
- add clients & services count ([#2072](https://github.com/ros2/rclcpp/issues/2072))
- Update API docs links in package READMEs ([#2302](https://github.com/ros2/rclcpp/issues/2302))
- add logger level service to lifecycle node. ([#2277](https://github.com/ros2/rclcpp/issues/2277))
- Stop using constref signature of benchmark DoNotOptimize. ([#2238](https://github.com/ros2/rclcpp/issues/2238))
- Implement get\_node\_type\_descriptions\_interface for lifecyclenode and add smoke test for it ([#2237](https://github.com/ros2/rclcpp/issues/2237))
- Switch lifecycle to use the RCLCPP macros. ([#2233](https://github.com/ros2/rclcpp/issues/2233))
- Add new node interface TypeDescriptionsInterface to provide GetTypeDescription service ([#2224](https://github.com/ros2/rclcpp/issues/2224))
- Contributors: Chris Lalancette, Christophe Bedard, Emerson Knapp, Jorge Perez, Lee, Minju, Tomoya Fujita, mergify[bot]

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/jazzy/rclpy/CHANGELOG.rst)

- Clock.py types. ([#1244](https://github.com/ros2/rclpy/issues/1244)) \* Start typing time.py \* Testing out Enum wrapper for ClockType \* convert to rcl\_clock\_type\_t \* Update create\_time\_point \* add types to logging\_service \* Add types to duration.py \* Add newlines for class definintions \* update type alias name \* Update to use Protocols \* Add types to time.py \* Add types \* Fix import order \* Started typing clock.py \* Move typealias import
- pybind11 definition doc typo fixes. ([#1270](https://github.com/ros2/rclpy/issues/1270))
- Fix small flake8 error in rclpy. ([#1267](https://github.com/ros2/rclpy/issues/1267)) Newer versions of flake8 complain that using ‘str’ as a variable shadows a builtin. Just make it ‘s’.
- Allow specifying qos ([#1225](https://github.com/ros2/rclpy/issues/1225))
- update RCL\_RET\_TIMEOUT error handling with action service response. ([#1258](https://github.com/ros2/rclpy/issues/1258))
- Add types to time\_source.py ([#1259](https://github.com/ros2/rclpy/issues/1259))
- Small fixes for modern flake8. ([#1264](https://github.com/ros2/rclpy/issues/1264))
- Add types to qos\_overriding\_options.py ([#1248](https://github.com/ros2/rclpy/issues/1248))
- Add types to context.py ([#1240](https://github.com/ros2/rclpy/issues/1240))
- Add back Type hash \_\_slots\_\_ and add test cases. ([#1245](https://github.com/ros2/rclpy/issues/1245))
- Revert “Add types to TypeHash and moved away from \_\_slots\_\_ usage ([#1232](https://github.com/ros2/rclpy/issues/1232))” ([#1243](https://github.com/ros2/rclpy/issues/1243))
- Time.py Types ([#1237](https://github.com/ros2/rclpy/issues/1237))
- Add types to TypeHash and moved away from \_\_slots\_\_ usage ([#1232](https://github.com/ros2/rclpy/issues/1232))
- Add Static Typing to Validate files ([#1230](https://github.com/ros2/rclpy/issues/1230))
- Add types to duration.py ([#1233](https://github.com/ros2/rclpy/issues/1233))
- added python3-yaml ([#1242](https://github.com/ros2/rclpy/issues/1242))
- Add types to exceptions.py ([#1241](https://github.com/ros2/rclpy/issues/1241))
- Add types ([#1231](https://github.com/ros2/rclpy/issues/1231))
- Creates Enum wrapper for ClockType and ClockChange ([#1235](https://github.com/ros2/rclpy/issues/1235))
- Add types to expand\_topic\_name ([#1238](https://github.com/ros2/rclpy/issues/1238))
- Add types to logging\_service.py ([#1227](https://github.com/ros2/rclpy/issues/1227))
- Add types to logging.py ([#1226](https://github.com/ros2/rclpy/issues/1226))
- forbid parameter to be declared statically without initialization. ([#1216](https://github.com/ros2/rclpy/issues/1216))
- Remove parentheses from assert statements. ([#1213](https://github.com/ros2/rclpy/issues/1213))
- Add doc-string warnings for destroy methods for services. ([#1205](https://github.com/ros2/rclpy/issues/1205))
- Add doc-string warnings for destroy() methods ([#1204](https://github.com/ros2/rclpy/issues/1204))
- Add an optional timeout\_sec input to Client.call() to fix issue <https://github.com/ros2/rclpy/issues/1181> ([#1188](https://github.com/ros2/rclpy/issues/1188))
- aligh with rcl that a rosout publisher of a node might not exist ([#1196](https://github.com/ros2/rclpy/issues/1196))
- call ok() to see if rclpy and context is initialized. ([#1198](https://github.com/ros2/rclpy/issues/1198))
- Adjust python usage of the type\_description service API ([#1192](https://github.com/ros2/rclpy/issues/1192))
- Document that spin\_once() should not be called from multiple threads ([#1079](https://github.com/ros2/rclpy/issues/1079))
- making optional things Optional ([#1182](https://github.com/ros2/rclpy/issues/1182))
- Use timeout object to avoid callback losing in wait\_for\_ready\_callbacks ([#1165](https://github.com/ros2/rclpy/issues/1165))
- Fix to issue <https://github.com/ros2/rclpy/issues/1179> ([#1180](https://github.com/ros2/rclpy/issues/1180))
- Add count services, clients & test ([#1024](https://github.com/ros2/rclpy/issues/1024))
- 1105 parameter event handler ([#1135](https://github.com/ros2/rclpy/issues/1135))
- unregister\_sigterm\_signal\_handler should be called. ([#1170](https://github.com/ros2/rclpy/issues/1170))
- Handle take failure in wait\_for\_message ([#1172](https://github.com/ros2/rclpy/issues/1172))
- Decouple rosout publisher init from node init. ([#1121](https://github.com/ros2/rclpy/issues/1121))
- Fix \_list\_parameters\_callback & test ([#1161](https://github.com/ros2/rclpy/issues/1161))
- add list\_parameters & test ([#1124](https://github.com/ros2/rclpy/issues/1124))
- Support to get remapped service name ([#1156](https://github.com/ros2/rclpy/issues/1156))
- a couple of typo fixes. ([#1158](https://github.com/ros2/rclpy/issues/1158))
- Fix get\_type\_description service bug and add a unit test ([#1155](https://github.com/ros2/rclpy/issues/1155))
- Fix an inherent race in execution vs. destruction. ([#1150](https://github.com/ros2/rclpy/issues/1150))
- Cleanup of test\_node.py. ([#1153](https://github.com/ros2/rclpy/issues/1153))
- Avoid generating the exception when rcl\_send\_response times out. ([#1136](https://github.com/ros2/rclpy/issues/1136))
- Store time source clocks in a set ([#1146](https://github.com/ros2/rclpy/issues/1146))
- Fix spin\_once\_until\_future\_complete to quit when the future finishes. ([#1143](https://github.com/ros2/rclpy/issues/1143))
- get\_type\_description service ([#1139](https://github.com/ros2/rclpy/issues/1139))
- Add in the ability to start timers paused. ([#1138](https://github.com/ros2/rclpy/issues/1138))
- Modifies ros\_timer\_init for ros\_timer\_init2 ([#999](https://github.com/ros2/rclpy/issues/999))
- Fix/param namespace association 894 ([#1132](https://github.com/ros2/rclpy/issues/1132))
- Include type hash in topic endpoint info ([#1104](https://github.com/ros2/rclpy/issues/1104))
- Fix iteration over modified list ([#1129](https://github.com/ros2/rclpy/issues/1129))
- making optional things Optional ([#974](https://github.com/ros2/rclpy/issues/974))
- Fix type signature of Client.wait\_for\_service ([#1128](https://github.com/ros2/rclpy/issues/1128))
- Fix action server crash when the client goes away. ([#1114](https://github.com/ros2/rclpy/issues/1114))
- Turn Executor into a ContextManager ([#1118](https://github.com/ros2/rclpy/issues/1118))
- Turn Context into a ContextManager ([#1117](https://github.com/ros2/rclpy/issues/1117))
- Fix type in Node init args ([#1115](https://github.com/ros2/rclpy/issues/1115))
- Contributors: AndyZe, Anton Kesy, Barry Xu, Brian, Chen Lihui, Chris Lalancette, Eloy Briceno, Emerson Knapp, EsipovPA, Felix Divo, Hans-Joachim Krauch, KKSTB, Lee, Luca Della Vedova, M. Hofstätter, Michael Carlstrom, Michael Carroll, Minju, Russ, SnIcK, Steve Peters, Tim Clephas, Tomoya Fujita, mhidalgo-bdai

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/jazzy/CHANGELOG.rst)

- Generate version header with ament\_generate\_version\_header function ([#190](https://github.com/ros2/rcpputils/issues/190))
- Update docs for rcpputils::split functions ([#188](https://github.com/ros2/rcpputils/issues/188))
- Included tl\_expected ([#185](https://github.com/ros2/rcpputils/issues/185))
- Switch to using target\_link\_libraries. ([#183](https://github.com/ros2/rcpputils/issues/183))
- Add a missing header due to missing PATH\_MAX variable ([#181](https://github.com/ros2/rcpputils/issues/181))
- Add unique\_lock implementation with clang thread safety annotations ([#180](https://github.com/ros2/rcpputils/issues/180))
- Add in a missing cstdint. ([#178](https://github.com/ros2/rcpputils/issues/178))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Emerson Knapp, Sai Kishor Kothakota, wojciechmadry

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/jazzy/CHANGELOG.rst)

- Removed warnings - strict-prototypes ([#461](https://github.com/ros2/rcutils/issues/461)) ([#465](https://github.com/ros2/rcutils/issues/465))
- Increase timeout repl\_str test ([#463](https://github.com/ros2/rcutils/issues/463)) ([#464](https://github.com/ros2/rcutils/issues/464))
- validate the allocator before use. ([#455](https://github.com/ros2/rcutils/issues/455)) \* validate the allocator before use. \* address review comments. - validate allocator only if the function specifically uses. - argument null check comes before validation of value. ———
- feat: Add human readable date to logging formats ([#441](https://github.com/ros2/rcutils/issues/441))
- Updates for uncrustify 0.78. ([#454](https://github.com/ros2/rcutils/issues/454))
- Set hints to find the python version we actually want. ([#451](https://github.com/ros2/rcutils/issues/451))
- Bring ament\_add\_gtest/target\_link\_libraries back together ([#452](https://github.com/ros2/rcutils/issues/452))
- Change ‘ROS2’ to ‘ROS 2’ in quality declaration ([#453](https://github.com/ros2/rcutils/issues/453))
- Allow parsing of escape sequence in log format ([#443](https://github.com/ros2/rcutils/issues/443))
- Clean up unused references to mimick/mocking in tests ([#450](https://github.com/ros2/rcutils/issues/450))
- Fix if(TARGET …) condition for test ([#447](https://github.com/ros2/rcutils/issues/447))
- Zero-initialize rcutils\_string\_array\_t in test\_string\_array ([#446](https://github.com/ros2/rcutils/issues/446))
- Use rcutils\_string\_array\_init in rcutils\_split & handle alloc fail ([#445](https://github.com/ros2/rcutils/issues/445))
- Make rcutils\_split() return RCUTILS\_RET\_BAD\_ALLOC if alloc fails ([#444](https://github.com/ros2/rcutils/issues/444))
- Remove two last uses of ament\_target\_dependencies. ([#440](https://github.com/ros2/rcutils/issues/440))
- time\_win32: Update dead link ([#438](https://github.com/ros2/rcutils/issues/438))
- memmove for overlaping memory ([#434](https://github.com/ros2/rcutils/issues/434))
- make escape characters work ([#426](https://github.com/ros2/rcutils/issues/426))
- Remove unused ‘max’ functions from sha256.c ([#429](https://github.com/ros2/rcutils/issues/429))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Kaju-Bubanja, Marc Bestmann, Silvio Traversaro, Tomoya Fujita, Tyler Weaver, mergify[bot]

<a id="resource-retriever"></a>

## [resource\_retriever](https://github.com/ros/resource_retriever/tree/jazzy/resource_retriever/CHANGELOG.rst)

- Update resource retreiver to use rule of five ([#95](https://github.com/ros/resource_retriever/issues/95))
- Use default ament\_lint\_auto ([#92](https://github.com/ros/resource_retriever/issues/92))
- Switch to target\_link\_libraries. ([#89](https://github.com/ros/resource_retriever/issues/89))
- Update to C++17 ([#88](https://github.com/ros/resource_retriever/issues/88))
- Contributors: Chris Lalancette, Michael Carroll

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/jazzy/rmw/CHANGELOG.rst)

- Removed warnings - strict-prototypes ([#365](https://github.com/ros2/rmw/issues/365)) ([#366](https://github.com/ros2/rmw/issues/366))
- Switch to target\_link\_libraries. ([#361](https://github.com/ros2/rmw/issues/361))
- Remove unnecessary c++14 flag. ([#360](https://github.com/ros2/rmw/issues/360))
- definition of local means being in the same context. ([#359](https://github.com/ros2/rmw/issues/359))
- typo fix. ([#355](https://github.com/ros2/rmw/issues/355))
- Contributors: Chris Lalancette, Tomoya Fujita, mergify[bot]

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/jazzy/rmw_connextdds/CHANGELOG.rst)

- Add rmw count clients services impl ([#93](https://github.com/ros2/rmw_connextdds/issues/93))
- Cleanup context implementation ([#131](https://github.com/ros2/rmw_connextdds/issues/131))
- Update to C++17 ([#125](https://github.com/ros2/rmw_connextdds/issues/125))
- Contributors: Chris Lalancette, Lee, Minju

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/jazzy/rmw_connextdds_common/CHANGELOG.rst)

- Revert “Mitigate discovery race condition between clients and services ([#132](https://github.com/ros2/rmw_connextdds/issues/132))” ([#146](https://github.com/ros2/rmw_connextdds/issues/146)) This reverts commit 7c95abbfc4559b293ebf5e94e20250bdd99d3ac6.
- Mitigate discovery race condition between clients and services ([#132](https://github.com/ros2/rmw_connextdds/issues/132)) \* Mitigate discovery race condition between clients and services.
- Add: tracepoint for subscribe serialized\_message ([#145](https://github.com/ros2/rmw_connextdds/issues/145)) \* Add: tracepoint for take\_serialized\_message \* Fix: TRACETOOLS\_TRACEPOINT args \* Update rmw\_connextdds\_common/src/common/rmw\_subscription.cpp Co-authored-by: Christophe Bedard <[bedard.christophe@gmail.com](mailto:bedard.christophe%40gmail.com)>
- Support Fast CDR v2 ([#141](https://github.com/ros2/rmw_connextdds/issues/141))
- Fix the rmw\_connextdds\_common build with gcc 13.2. ([#142](https://github.com/ros2/rmw_connextdds/issues/142)) The most important fix here is to #include <cstdint>, but also make sure we #include for all used STL functions.
- Fix basic request reply mapping for ConnextDDS Pro ([#139](https://github.com/ros2/rmw_connextdds/issues/139))
- Add ros2\_tracing tracepoints ([#120](https://github.com/ros2/rmw_connextdds/issues/120))
- avoid using dds common public mutex directly ([#134](https://github.com/ros2/rmw_connextdds/issues/134))
- Fix a couple of warnings pointed out by clang. ([#133](https://github.com/ros2/rmw_connextdds/issues/133))
- Add rmw count clients services impl ([#93](https://github.com/ros2/rmw_connextdds/issues/93))
- Conditional internal API access to support Connext 7+ ([#121](https://github.com/ros2/rmw_connextdds/issues/121))
- Cleanup context implementation ([#131](https://github.com/ros2/rmw_connextdds/issues/131))
- Fix RMW\_Connext\_Client::is\_service\_available for micro ([#130](https://github.com/ros2/rmw_connextdds/issues/130))
- Update to C++17 ([#125](https://github.com/ros2/rmw_connextdds/issues/125))
- Pass parameters in the correct order to DDS\_DataReader\_read in rmw\_connextdds\_count\_unread\_samples for micro ([#129](https://github.com/ros2/rmw_connextdds/issues/129))
- Optimize QoS to improve responsiveness of reliable endpoints ([#26](https://github.com/ros2/rmw_connextdds/issues/26))
- Clear out errors once we have handled them. ([#126](https://github.com/ros2/rmw_connextdds/issues/126))
- Add support for listener callbacks ([#76](https://github.com/ros2/rmw_connextdds/issues/76))
- Contributors: Andrea Sorbini, Chen Lihui, Chris Lalancette, Christopher Wecht, Lee, Miguel Company, Minju, h-suzuki-isp

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/jazzy/rmw_connextddsmicro/CHANGELOG.rst)

- Add rmw count clients services impl ([#93](https://github.com/ros2/rmw_connextdds/issues/93))
- Cleanup context implementation ([#131](https://github.com/ros2/rmw_connextdds/issues/131))
- Update to C++17 ([#125](https://github.com/ros2/rmw_connextdds/issues/125))
- Contributors: Chris Lalancette, Lee, Minju

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/jazzy/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Set received\_timestamp to system\_clock::now() in message\_info ([#491](https://github.com/ros2/rmw_cyclonedds/issues/491)) ([#493](https://github.com/ros2/rmw_cyclonedds/issues/493)) \* Set received\_timestamp to steady\_clock::now() in message\_info \* Use ‘system\_clock’ instead of ‘steady\_clock’ \* Also update receive\_timestamp for services. (cherry picked from commit 76c9d8f38a03d160b258902af6d1d06f6ed9391e) Co-authored-by: Michael Orlov <[morlovmr@gmail.com](mailto:morlovmr%40gmail.com)>
- Add tracepoint for publish/subscribe serialized message ([#485](https://github.com/ros2/rmw_cyclonedds/issues/485)) Co-authored-by: eboasson <[eb@ilities.com](mailto:eb%40ilities.com)>
- Remove a bunch of unnecessary macros. ([#482](https://github.com/ros2/rmw_cyclonedds/issues/482))
- compare string contents but string pointer addresses. ([#481](https://github.com/ros2/rmw_cyclonedds/issues/481))
- Add timestamp to rmw\_publish tracepoint ([#454](https://github.com/ros2/rmw_cyclonedds/issues/454))
- avoid using dds common public mutex directly ([#474](https://github.com/ros2/rmw_cyclonedds/issues/474))
- Add rmw count clients,services impl ([#427](https://github.com/ros2/rmw_cyclonedds/issues/427))
- Minor revamp of the CMakeLists.txt. ([#468](https://github.com/ros2/rmw_cyclonedds/issues/468))
- Clear out errors once we have handled them. ([#464](https://github.com/ros2/rmw_cyclonedds/issues/464))
- Instrument loaned message publication code path
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#450](https://github.com/ros2/rmw_cyclonedds/issues/450))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Christopher Wecht, Lee, Minju, Tomoya Fujita, h-suzuki-isp, mergify[bot]

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/jazzy/rmw_dds_common/CHANGELOG.rst)

- Add pkcs11 support to get\_security\_files ([#66](https://github.com/ros2/rmw_dds_common/issues/66))
- make a new private mutex and add updating graph methods ([#73](https://github.com/ros2/rmw_dds_common/issues/73))
- Just remove rcpputils::fs dependency ([#72](https://github.com/ros2/rmw_dds_common/issues/72))
- Contributors: Chen Lihui, Kenta Yonekura, Miguel Company

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/jazzy/rmw_fastrtps_cpp/CHANGELOG.rst)

- Support Fast CDR v2 ([#746](https://github.com/ros2/rmw_fastrtps/issues/746)) \* Require fastcdr version 2 \* Changes to build rmw\_fastrtps\_shared\_cpp \* Changes to build rmw\_fastrtps\_cpp \* Changes to build rmw\_fastrtps\_dynamic\_cpp
- Capture `std::bad_alloc` on deserializeROSmessage. ([#665](https://github.com/ros2/rmw_fastrtps/issues/665))
- Switch to target\_link\_libraries for linking. ([#734](https://github.com/ros2/rmw_fastrtps/issues/734))
- avoid using dds common public mutex directly ([#725](https://github.com/ros2/rmw_fastrtps/issues/725))
- Add rmw\_count clients,services impl ([#641](https://github.com/ros2/rmw_fastrtps/issues/641))
- Improve node graph delivery by using a unique listening port ([#711](https://github.com/ros2/rmw_fastrtps/issues/711))
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#686](https://github.com/ros2/rmw_fastrtps/issues/686))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Lee, Miguel Company, Minju

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/jazzy/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Support Fast CDR v2 ([#746](https://github.com/ros2/rmw_fastrtps/issues/746)) \* Require fastcdr version 2 \* Changes to build rmw\_fastrtps\_shared\_cpp \* Changes to build rmw\_fastrtps\_cpp \* Changes to build rmw\_fastrtps\_dynamic\_cpp
- compare string contents but string pointer addresses. ([#744](https://github.com/ros2/rmw_fastrtps/issues/744))
- Improve wide string (de)serialization in rwm\_dynamic\_fastrtps\_cpp ([#740](https://github.com/ros2/rmw_fastrtps/issues/740)) \* Move type support headers to src \* Fix references to moved headers \* move macros.hpp to src/serialization\_helpers.hpp \* Move other non-api headers \* Move common code into serialize\_wide\_string. \* Move common code into deserialize\_wide\_string. \* Move serialization into serialization\_helpers.hpp \* Move deserialization into serialization\_helpers.hpp \* Fix header guards \* Linters \* Do not account for extra character on serialized size calculation \* Remove dependency on rosidl\_typesupport\_fastrtps\_c(pp) ———
- Capture `std::bad_alloc` on deserializeROSmessage. ([#665](https://github.com/ros2/rmw_fastrtps/issues/665))
- Switch to target\_link\_libraries for linking. ([#734](https://github.com/ros2/rmw_fastrtps/issues/734))
- avoid using dds common public mutex directly ([#725](https://github.com/ros2/rmw_fastrtps/issues/725))
- Account for alignment on is\_plain calculations. ([#716](https://github.com/ros2/rmw_fastrtps/issues/716))
- Add rmw\_count clients,services impl ([#641](https://github.com/ros2/rmw_fastrtps/issues/641))
- Improve node graph delivery by using a unique listening port ([#711](https://github.com/ros2/rmw_fastrtps/issues/711))
- Contributors: Chen Lihui, Chris Lalancette, Lee, Miguel Company, Minju, Tomoya Fujita

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/jazzy/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Allow pkcs11 when calling rmw\_dds\_common::get\_security\_files. ([#565](https://github.com/ros2/rmw_fastrtps/issues/565)) Co-authored-by: Miguel Company <[MiguelCompany@eprosima.com](mailto:MiguelCompany%40eprosima.com)>
- Add tracepoint for publish/subscribe serialized\_message ([#748](https://github.com/ros2/rmw_fastrtps/issues/748)) \* Add: tracepoint for generic pub/sub \* Fix: correspond to PR 454 \* Fix: change write to write\_to\_timestamp ———
- Support Fast CDR v2 ([#746](https://github.com/ros2/rmw_fastrtps/issues/746)) \* Require fastcdr version 2 \* Changes to build rmw\_fastrtps\_shared\_cpp \* Changes to build rmw\_fastrtps\_cpp \* Changes to build rmw\_fastrtps\_dynamic\_cpp
- Remove an unnecessary constructor. ([#743](https://github.com/ros2/rmw_fastrtps/issues/743)) We can just use brace initialization here, and this allows us to side-step an uncrustify issue with the constructor.
- Add timestamp to rmw\_publish tracepoint ([#694](https://github.com/ros2/rmw_fastrtps/issues/694))
- Switch to Unix line endings. ([#736](https://github.com/ros2/rmw_fastrtps/issues/736))
- Switch to target\_link\_libraries for linking. ([#734](https://github.com/ros2/rmw_fastrtps/issues/734))
- Quiet compiler warning in Release mode. ([#730](https://github.com/ros2/rmw_fastrtps/issues/730))
- avoid using dds common public mutex directly ([#725](https://github.com/ros2/rmw_fastrtps/issues/725))
- Add rmw\_count clients,services impl ([#641](https://github.com/ros2/rmw_fastrtps/issues/641))
- Switch to using rclcpp::unique\_lock. ([#712](https://github.com/ros2/rmw_fastrtps/issues/712))
- Use DataWriter Qos to configure max\_blocking\_time on rmw\_send\_response ([#704](https://github.com/ros2/rmw_fastrtps/issues/704))
- Clear out errors once we have handled them. ([#701](https://github.com/ros2/rmw_fastrtps/issues/701))
- Instrument loaned message publication code path ([#698](https://github.com/ros2/rmw_fastrtps/issues/698))
- Add in a missing data\_reader check when creating subscription. ([#697](https://github.com/ros2/rmw_fastrtps/issues/697))
- Use TRACETOOLS\_ prefix for tracepoint-related macros ([#686](https://github.com/ros2/rmw_fastrtps/issues/686))
- typo fix. ([#693](https://github.com/ros2/rmw_fastrtps/issues/693))
- address clang nightly build error. ([#689](https://github.com/ros2/rmw_fastrtps/issues/689))
- Check for errors while doing an rmw\_discovery\_options\_copy. ([#690](https://github.com/ros2/rmw_fastrtps/issues/690))
- Contributors: Chen Lihui, Chris Lalancette, Christophe Bedard, Christopher Wecht, IkerLuengo, Lee, Miguel Company, Minju, Tomoya Fujita, h-suzuki-isp

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/jazzy/rmw_implementation/CHANGELOG.rst)

- Update quality declaration document ([#225](https://github.com/ros2/rmw_implementation/issues/225)) ([#226](https://github.com/ros2/rmw_implementation/issues/226))
- Switch to using target\_link\_libraries everywhere. ([#222](https://github.com/ros2/rmw_implementation/issues/222))
- Add rmw\_count\_clients,services & test ([#208](https://github.com/ros2/rmw_implementation/issues/208))
- Contributors: Chris Lalancette, Lee, Minju, mergify[bot]

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/jazzy/CHANGELOG.rst)

- Fix reload after a description with a mimic joint ([#212](https://github.com/ros/robot_state_publisher/issues/212))
- Remove ament\_target\_dependencies. ([#209](https://github.com/ros/robot_state_publisher/issues/209))
- Improve log messages ([#206](https://github.com/ros/robot_state_publisher/issues/206))
- Contributors: Chris Lalancette, Guillaume Doisy, Nick Lamprianidis

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/jazzy/ros2action/CHANGELOG.rst)

- call get\_action\_interfaces() properly. ([#898](https://github.com/ros2/ros2cli/issues/898)) ([#900](https://github.com/ros2/ros2cli/issues/900)) (cherry picked from commit 305ef763b83e42ebddc4802ac788869d178b6e93) Co-authored-by: Tomoya Fujita <[Tomoya.Fujita@sony.com](mailto:Tomoya.Fujita%40sony.com)>
- support `ros2 action type <action name>`. ([#894](https://github.com/ros2/ros2cli/issues/894)) \* support `ros2 action type <action name>`. \* add review comments. ———
- Load a message/request/goal from standard input ([#844](https://github.com/ros2/ros2cli/issues/844))
- Contributors: Tomoya Fujita, mergify[bot], ymd-stella

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/jazzy/ros2bag/CHANGELOG.rst)

- Add option to disable recorder keyboard controls ([#1607](https://github.com/ros2/rosbag2/issues/1607))
- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Added exclude-topic-types to record ([#1582](https://github.com/ros2/rosbag2/issues/1582))
- Overhaul in the rosbag2\_transport::TopicFilter class and relevant tests ([#1585](https://github.com/ros2/rosbag2/issues/1585))
- Filter topic by type ([#1577](https://github.com/ros2/rosbag2/issues/1577))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Add python3-yaml as a dependency ([#1490](https://github.com/ros2/rosbag2/issues/1490))
- Fix the description of paramter ‘–topics’ for play ([#1426](https://github.com/ros2/rosbag2/issues/1426))
- When using sim time, wait for /clock before beginning recording ([#1378](https://github.com/ros2/rosbag2/issues/1378))
- Revert “Don’t record sim-time messages before first /clock ([#1354](https://github.com/ros2/rosbag2/issues/1354))” ([#1377](https://github.com/ros2/rosbag2/issues/1377))
- Don’t record sim-time messages before first /clock ([#1354](https://github.com/ros2/rosbag2/issues/1354))
- Fix wrong descritpion for ‘–ignore-leaf-topics’ ([#1344](https://github.com/ros2/rosbag2/issues/1344))
- Cleanup the help text for ros2 bag record. ([#1329](https://github.com/ros2/rosbag2/issues/1329))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Bernd Pfrommer, Chris Lalancette, Emerson Knapp, Michael Orlov, Michal Sojka

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/jazzy/ros2cli/CHANGELOG.rst)

- ros2cli.node.daemon : try getting fdsize from /proc for open fd limit ([#888](https://github.com/ros2/ros2cli/issues/888))
- Fix the SIGTERM handling in the ros2 daemon. ([#887](https://github.com/ros2/ros2cli/issues/887))
- Replace unmaintained `netifaces` library to avoid local wheel builds ([#875](https://github.com/ros2/ros2cli/issues/875))
- make handles not inheritable to prevent from blocking durning tab-completion ([#852](https://github.com/ros2/ros2cli/issues/852))
- Add ros2 service info ([#771](https://github.com/ros2/ros2cli/issues/771))
- catch ExternalShutdownException ros2cli main. ([#854](https://github.com/ros2/ros2cli/issues/854))
- Load a message/request/goal from standard input ([#844](https://github.com/ros2/ros2cli/issues/844))
- Fix tests with get\_type\_description service and param present ([#838](https://github.com/ros2/ros2cli/issues/838))
- Add marshalling functions for rclpy.type\_hash.TypeHash (rep2011) ([#816](https://github.com/ros2/ros2cli/issues/816))
- [service introspection] ros2 service echo ([#745](https://github.com/ros2/ros2cli/issues/745))
- Contributors: Brian, Chen Lihui, Chris Lalancette, Emerson Knapp, Hans-Joachim Krauch, Laurenz, Lee, Minju, Tomoya Fujita, akssri-sony, ymd-stella

<a id="ros2cli-test-interfaces"></a>

## [ros2cli\_test\_interfaces](https://github.com/ros2/ros2cli/tree/jazzy/ros2cli_test_interfaces/CHANGELOG.rst)

- Update to C++17 ([#848](https://github.com/ros2/ros2cli/issues/848))
- Contributors: Chris Lalancette

<a id="ros2component"></a>

## [ros2component](https://github.com/ros2/ros2cli/tree/jazzy/ros2component/CHANGELOG.rst)

- Warning: get\_parameter\_value() is deprecated. ([#866](https://github.com/ros2/ros2cli/issues/866))
- Contributors: Tomoya Fujita

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/jazzy/ros2doctor/CHANGELOG.rst)

- Remove references to <https://index.ros.org> ([#897](https://github.com/ros2/ros2cli/issues/897))
- (ros2doctor) fix PackageCheck ([#860](https://github.com/ros2/ros2cli/issues/860)) \* (ros2doctor)(package) improve result string generation
- Shutdown ros2doctor hello when ctrl-c is received ([#826](https://github.com/ros2/ros2cli/issues/826))
- Contributors: Chris Lalancette, Matthijs van der Burgh, Michael Carroll

<a id="ros2interface"></a>

## [ros2interface](https://github.com/ros2/ros2cli/tree/jazzy/ros2interface/CHANGELOG.rst)

- Add interface type filters to ros2 interface package ([#765](https://github.com/ros2/ros2cli/issues/765))
- Contributors: David V. Lu!!

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/jazzy/ros2param/CHANGELOG.rst)

- ros2 param dump should handle empty list as exception. ([#881](https://github.com/ros2/ros2cli/issues/881))
- Warning: get\_parameter\_value() is deprecated. ([#866](https://github.com/ros2/ros2cli/issues/866))
- Fix tests with get\_type\_description service and param present ([#838](https://github.com/ros2/ros2cli/issues/838))
- Update ros2 param dump dosctring. ([#837](https://github.com/ros2/ros2cli/issues/837))
- Contributors: Emerson Knapp, Murilo M Marinho, Tomoya Fujita

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/jazzy/ros2pkg/CHANGELOG.rst)

- Update the package template for our new include directories. ([#847](https://github.com/ros2/ros2cli/issues/847))
- Fix typo in ros2pkg warning message. ([#827](https://github.com/ros2/ros2cli/issues/827))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/jazzy/ros2service/CHANGELOG.rst)

- Add ros2 service info ([#771](https://github.com/ros2/ros2cli/issues/771))
- Load a message/request/goal from standard input ([#844](https://github.com/ros2/ros2cli/issues/844))
- Fix tests with get\_type\_description service and param present ([#838](https://github.com/ros2/ros2cli/issues/838))
- [service introspection] ros2 service echo ([#745](https://github.com/ros2/ros2cli/issues/745))
- Contributors: Brian, Emerson Knapp, Lee, Minju, ymd-stella

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/jazzy/ros2topic/CHANGELOG.rst)

- Remove parentheses from assert statement. ([#878](https://github.com/ros2/ros2cli/issues/878))
- Load a message/request/goal from standard input ([#844](https://github.com/ros2/ros2cli/issues/844))
- Add marshalling functions for rclpy.type\_hash.TypeHash (rep2011) ([#816](https://github.com/ros2/ros2cli/issues/816))
- [service introspection] ros2 service echo ([#745](https://github.com/ros2/ros2cli/issues/745))
- Contributors: Brian, Chris Lalancette, Hans-Joachim Krauch, ymd-stella

<a id="ros2trace"></a>

## [ros2trace](https://github.com/ros2/ros2_tracing/tree/jazzy/ros2trace/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Create start/pause/resume/stop sub-commands for ‘ros2 trace’ ([#70](https://github.com/ros2/ros2_tracing/issues/70))
- Switch <depend> to <exec\_depend> in pure Python packages ([#67](https://github.com/ros2/ros2_tracing/issues/67))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_compression/CHANGELOG.rst)

- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Add default initialization for CompressionOptions ([#1539](https://github.com/ros2/rosbag2/issues/1539))
- Add option to set compression threads priority ([#1457](https://github.com/ros2/rosbag2/issues/1457))
- Fixes pointed out by clang. ([#1493](https://github.com/ros2/rosbag2/issues/1493))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- Add in a missing cstdint include. ([#1321](https://github.com/ros2/rosbag2/issues/1321))
- Fix warning from ClassLoader in sequential compression reader and writer ([#1299](https://github.com/ros2/rosbag2/issues/1299))
- Contributors: Arne B, Chris Lalancette, Michael Orlov, Patrick Roncagliolo, Roman Sokolkov, jmachowinski

<a id="rosbag2-compression-zstd"></a>

## [rosbag2\_compression\_zstd](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_compression_zstd/CHANGELOG.rst)

- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Contributors: Chris Lalancette, Roman Sokolkov

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_cpp/CHANGELOG.rst)

- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- call cv.wait\_until only if necessary. ([#1521](https://github.com/ros2/rosbag2/issues/1521))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Switch to target\_link\_libraries everywhere. ([#1504](https://github.com/ros2/rosbag2/issues/1504))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- ros2 bag convert now excludes messages not in [start\_time;end\_time] ([#1455](https://github.com/ros2/rosbag2/issues/1455))
- Replace TSAUniqueLock implementation with rcpputils::unique\_lock ([#1454](https://github.com/ros2/rosbag2/issues/1454))
- Add BagSplitInfo service call on bag close ([#1422](https://github.com/ros2/rosbag2/issues/1422))
- Rewrite TimeControllerClockTest.unpaused\_sleep\_returns\_true to be correct ([#1384](https://github.com/ros2/rosbag2/issues/1384))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Don’t crash when type definition cannot be found ([#1350](https://github.com/ros2/rosbag2/issues/1350))
- Add recorder stop() API ([#1300](https://github.com/ros2/rosbag2/issues/1300))
- Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael Orlov, Patrick Roncagliolo, Peter Favrholdt, Roman Sokolkov, Tomoya Fujita, jmachowinski

<a id="rosbag2-examples-cpp"></a>

## [rosbag2\_examples\_cpp](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst)

- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- Contributors: Michael Orlov, Patrick Roncagliolo

<a id="rosbag2-examples-py"></a>

## [rosbag2\_examples\_py](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst)

- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Fix a warning from python setuptools. ([#1312](https://github.com/ros2/rosbag2/issues/1312))
- Contributors: Chris Lalancette, Michael Orlov

<a id="rosbag2-interfaces"></a>

## [rosbag2\_interfaces](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_interfaces/CHANGELOG.rst)

- Add node name to the Read(Write)SplitEvent message ([#1609](https://github.com/ros2/rosbag2/issues/1609))
- Contributors: Michael Orlov

<a id="rosbag2-performance-benchmarking"></a>

## [rosbag2\_performance\_benchmarking](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst)

- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Add option to set compression threads priority ([#1457](https://github.com/ros2/rosbag2/issues/1457))
- Add per group statistics for rosbag2\_performance\_benchmarking report ([#1306](https://github.com/ros2/rosbag2/issues/1306))
- Set CPU affinity for producers and recorder from benchmark parameters ([#1305](https://github.com/ros2/rosbag2/issues/1305))
- Add CPU usage to rosbag2\_performance\_benchmarking results report ([#1304](https://github.com/ros2/rosbag2/issues/1304))
- Add config option to use storage\_id parameter in benchmark\_launch.py ([#1303](https://github.com/ros2/rosbag2/issues/1303))
- Contributors: Chris Lalancette, Michael Orlov, jmachowinski

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_py/CHANGELOG.rst)

- Add option to disable recorder keyboard controls ([#1607](https://github.com/ros2/rosbag2/issues/1607))
- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Switch rclpy to be an exec\_depend here. ([#1606](https://github.com/ros2/rosbag2/issues/1606))
- Gracefully handle SIGINT and SIGTERM signals for play and burst CLI ([#1557](https://github.com/ros2/rosbag2/issues/1557))
- Added exclude-topic-types to record ([#1582](https://github.com/ros2/rosbag2/issues/1582))
- Fix for false negative tests in rosbag2\_py ([#1592](https://github.com/ros2/rosbag2/issues/1592))
- Update rosbag2\_py stubs ([#1593](https://github.com/ros2/rosbag2/issues/1593))
- Add Python stubs for rosbag2\_py ([#1459](https://github.com/ros2/rosbag2/issues/1459)) ([#1569](https://github.com/ros2/rosbag2/issues/1569))
- Filter topic by type ([#1577](https://github.com/ros2/rosbag2/issues/1577))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Install signal handlers in recorder only inside record method ([#1464](https://github.com/ros2/rosbag2/issues/1464))
- add missing import otherwise it doesnt compile ([#1524](https://github.com/ros2/rosbag2/issues/1524))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Make `rosbag2_transport::Player::play()` run in a separate thread ([#1503](https://github.com/ros2/rosbag2/issues/1503))
- Switch to target\_link\_libraries everywhere. ([#1504](https://github.com/ros2/rosbag2/issues/1504))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- ros2 bag convert now excludes messages not in [start\_time;end\_time] ([#1455](https://github.com/ros2/rosbag2/issues/1455))
- Add support for compression to python API ([#1425](https://github.com/ros2/rosbag2/issues/1425))
- Gracefully handle SIGINT and SIGTERM in rosbag2 recorder ([#1301](https://github.com/ros2/rosbag2/issues/1301))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Add binding to close the writer ([#1339](https://github.com/ros2/rosbag2/issues/1339))
- Contributors: Alejandro Hernández Cordero, Andrew Symington, Barry Xu, Bernd Pfrommer, Chris Lalancette, Emerson Knapp, Michael Orlov, Mikael Arguedas, Patrick Roncagliolo, Peter Favrholdt, Roman Sokolkov, Yadu, jmachowinski

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_storage/CHANGELOG.rst)

- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Remove rcpputils::fs dependencies from rosbag2\_storages ([#1558](https://github.com/ros2/rosbag2/issues/1558))
- Improve performance in SqliteStorage::get\_bagfile\_size() ([#1516](https://github.com/ros2/rosbag2/issues/1516))
- Make Player and Recorder Composable ([#902](https://github.com/ros2/rosbag2/issues/902)) ([#1419](https://github.com/ros2/rosbag2/issues/1419))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- ros2 bag convert now excludes messages not in [start\_time;end\_time] ([#1455](https://github.com/ros2/rosbag2/issues/1455))
- Fix missing cstdint include ([#1383](https://github.com/ros2/rosbag2/issues/1383))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael Orlov, Patrick Roncagliolo, Peter Favrholdt, Roman Sokolkov, Zac Stanton, jmachowinski

<a id="rosbag2-storage-mcap"></a>

## [rosbag2\_storage\_mcap](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_storage_mcap/CHANGELOG.rst)

- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Check existence of a file before passing it to the mcap reader ([#1594](https://github.com/ros2/rosbag2/issues/1594))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Use rw\_lock to protect mcap metadata lists. ([#1561](https://github.com/ros2/rosbag2/issues/1561))
- Remove rcpputils::fs dependencies from rosbag2\_storages ([#1558](https://github.com/ros2/rosbag2/issues/1558))
- remove unused headers ([#1544](https://github.com/ros2/rosbag2/issues/1544))
- Link and compile against rosbag2\_storage\_mcap: Fixed issue 1492 ([#1496](https://github.com/ros2/rosbag2/issues/1496))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- Store serialized metadata in MCAP file ([#1423](https://github.com/ros2/rosbag2/issues/1423))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christopher Wecht, Emerson Knapp, Michael Orlov, Patrick Roncagliolo, Roman Sokolkov, Tomoya Fujita, jmachowinski, uupks

<a id="rosbag2-storage-sqlite3"></a>

## [rosbag2\_storage\_sqlite3](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_storage_sqlite3/CHANGELOG.rst)

- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Remove rcpputils::fs dependencies from rosbag2\_storages ([#1558](https://github.com/ros2/rosbag2/issues/1558))
- Change an incorrect TSA annotation. ([#1552](https://github.com/ros2/rosbag2/issues/1552))
- Improve performance in SqliteStorage::get\_bagfile\_size() ([#1516](https://github.com/ros2/rosbag2/issues/1516))
- Update rosbag2\_storage\_sqlite3 to C++17. ([#1501](https://github.com/ros2/rosbag2/issues/1501))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- Stop inheriting from std::iterator. ([#1424](https://github.com/ros2/rosbag2/issues/1424))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Store metadata in db3 file ([#1294](https://github.com/ros2/rosbag2/issues/1294))
- Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michael Orlov, Patrick Roncagliolo, Roman Sokolkov, jmachowinski

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_test_common/CHANGELOG.rst)

- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Add extra checks in execute\_and\_wait\_until\_completion(..) ([#1346](https://github.com/ros2/rosbag2/issues/1346))
- Address flakiness in rosbag2\_play\_end\_to\_end tests ([#1297](https://github.com/ros2/rosbag2/issues/1297))
- Contributors: Barry Xu, Chris Lalancette, Michael Orlov

<a id="rosbag2-test-msgdefs"></a>

## [rosbag2\_test\_msgdefs](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_test_msgdefs/CHANGELOG.rst)

- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Don’t crash when type definition cannot be found ([#1350](https://github.com/ros2/rosbag2/issues/1350)) \* Don’t fail when type definition cannot be found
- Contributors: Barry Xu, Emerson Knapp

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_tests/CHANGELOG.rst)

- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Added exclude-topic-types to record ([#1582](https://github.com/ros2/rosbag2/issues/1582))
- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Filter topic by type ([#1577](https://github.com/ros2/rosbag2/issues/1577))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Improve performance in SqliteStorage::get\_bagfile\_size() ([#1516](https://github.com/ros2/rosbag2/issues/1516))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Mark play\_end\_to\_end test as xfail in Windows ([#1452](https://github.com/ros2/rosbag2/issues/1452))
- Implement storing and loading ROS\_DISTRO from metadata.yaml and mcap files ([#1241](https://github.com/ros2/rosbag2/issues/1241))
- Address flakiness in rosbag2\_play\_end\_to\_end tests ([#1297](https://github.com/ros2/rosbag2/issues/1297))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Cristóbal Arroyo, Emerson Knapp, Michael Orlov, Roman Sokolkov, jmachowinski

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/jazzy/rosbag2_transport/CHANGELOG.rst)

- Removed warnings - unqualified-std-cast-call ([#1618](https://github.com/ros2/rosbag2/issues/1618)) ([#1622](https://github.com/ros2/rosbag2/issues/1622))
- Add node name to the Read(Write)SplitEvent message ([#1609](https://github.com/ros2/rosbag2/issues/1609))
- Add option to disable recorder keyboard controls ([#1607](https://github.com/ros2/rosbag2/issues/1607))
- Support service 2/2 — rosbag2 service play ([#1481](https://github.com/ros2/rosbag2/issues/1481))
- Use middleware send and receive timestamps from message\_info during recording ([#1531](https://github.com/ros2/rosbag2/issues/1531))
- Update to use yaml-cpp version 0.8.0. ([#1605](https://github.com/ros2/rosbag2/issues/1605))
- Gracefully handle SIGINT and SIGTERM signals for play and burst CLI ([#1557](https://github.com/ros2/rosbag2/issues/1557))
- Added exclude-topic-types to record ([#1582](https://github.com/ros2/rosbag2/issues/1582))
- Use std::filesystem instead of rcpputils::fs ([#1576](https://github.com/ros2/rosbag2/issues/1576))
- Add transactional state mutex for RecorderImpl class. ([#1547](https://github.com/ros2/rosbag2/issues/1547))
- Overhaul in the rosbag2\_transport::TopicFilter class and relevant tests ([#1585](https://github.com/ros2/rosbag2/issues/1585))
- Filter topic by type ([#1577](https://github.com/ros2/rosbag2/issues/1577))
- fix: use size\_t instead of uint64\_t in play\_options YAML converter ([#1575](https://github.com/ros2/rosbag2/issues/1575))
- Make some changes for newer versions of uncrustify. ([#1578](https://github.com/ros2/rosbag2/issues/1578))
- Add topic\_id returned by storage to the TopicMetadata ([#1538](https://github.com/ros2/rosbag2/issues/1538))
- Workaround for flaky test\_play\_services running with fastrtps ([#1556](https://github.com/ros2/rosbag2/issues/1556))
- Add proper message for –start-paused ([#1537](https://github.com/ros2/rosbag2/issues/1537))
- `Recording stopped` prints only once. ([#1530](https://github.com/ros2/rosbag2/issues/1530))
- Cleanup the rosbag2\_transport tests ([#1518](https://github.com/ros2/rosbag2/issues/1518))
- Implement service recording and display info about recorded services ([#1480](https://github.com/ros2/rosbag2/issues/1480))
- Add option to set compression threads priority ([#1457](https://github.com/ros2/rosbag2/issues/1457))
- Bugfix for incorrect playback rate changes when pressing buttons ([#1513](https://github.com/ros2/rosbag2/issues/1513))
- Make Player and Recorder Composable ([#902](https://github.com/ros2/rosbag2/issues/902)) ([#1419](https://github.com/ros2/rosbag2/issues/1419))
- Clang fixes for the latest PlayerImpl code. ([#1507](https://github.com/ros2/rosbag2/issues/1507))
- Make `rosbag2_transport::Player::play()` run in a separate thread ([#1503](https://github.com/ros2/rosbag2/issues/1503))
- Switch to target\_link\_libraries everywhere. ([#1504](https://github.com/ros2/rosbag2/issues/1504))
- Use enum values for offered\_qos\_profiles in code and string names in serialized metadata ([#1476](https://github.com/ros2/rosbag2/issues/1476))
- Redesign Player class with PIMPL idiom ([#1447](https://github.com/ros2/rosbag2/issues/1447))
- Don’t warn for unknown types if topics are not selected ([#1466](https://github.com/ros2/rosbag2/issues/1466))
- Remove unused concurrentqueue implementation. ([#1465](https://github.com/ros2/rosbag2/issues/1465))
- Fix uninitialized value pointed out by clang static analysis. ([#1440](https://github.com/ros2/rosbag2/issues/1440))
- Fix the build with rmw\_fastrtps\_dynamic. ([#1416](https://github.com/ros2/rosbag2/issues/1416))
- Fix for rosbag2\_transport::Recorder failures due to the unhandled exceptions ([#1382](https://github.com/ros2/rosbag2/issues/1382))
- When using sim time, wait for /clock before beginning recording ([#1378](https://github.com/ros2/rosbag2/issues/1378))
- Fix for possible freeze in Recorder::stop() ([#1381](https://github.com/ros2/rosbag2/issues/1381))
- Revert “Don’t record sim-time messages before first /clock ([#1354](https://github.com/ros2/rosbag2/issues/1354))” ([#1377](https://github.com/ros2/rosbag2/issues/1377))
- Don’t record sim-time messages before first /clock ([#1354](https://github.com/ros2/rosbag2/issues/1354))
- Fix a clang warning about uninitialized variable. ([#1370](https://github.com/ros2/rosbag2/issues/1370))
- [bugfix] for parameters not passing to recorder’s node from child component ([#1360](https://github.com/ros2/rosbag2/issues/1360))
- Change subscriptions from GenericSubscripton to SubscriptionBase ([#1337](https://github.com/ros2/rosbag2/issues/1337))
- Add recorder stop() API ([#1300](https://github.com/ros2/rosbag2/issues/1300))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Bernd Pfrommer, Chris Lalancette, Christoph Fröhlich, Daisuke Nishimatsu, Emerson Knapp, Michael Orlov, Patrick Roncagliolo, Roman Sokolkov, Tomoya Fujita, jmachowinski, mergify[bot]

<a id="rosidl-cmake"></a>

## [rosidl\_cmake](https://github.com/ros2/rosidl/tree/jazzy/rosidl_cmake/CHANGELOG.rst)

- Improve deprecation notice of rosidl\_target\_interface to give a hint on how to update the code ([#788](https://github.com/ros2/rosidl/issues/788))
- Add rosidl\_find\_package\_idl helper function ([#754](https://github.com/ros2/rosidl/issues/754))
- Remove unused splitting of .srv files in CMake ([#753](https://github.com/ros2/rosidl/issues/753))
- Contributors: Alexis Paques, Mike Purvis, Shane Loretz

<a id="rosidl-dynamic-typesupport"></a>

## [rosidl\_dynamic\_typesupport](https://github.com/ros2/rosidl_dynamic_typesupport/tree/jazzy/CHANGELOG.rst)

- uchar: fix conditional include/typedef ([#10](https://github.com/ros2/rosidl_dynamic_typesupport/issues/10))
- uchar: use \_\_has\_include(..) on separate line ([#8](https://github.com/ros2/rosidl_dynamic_typesupport/issues/8))
- Refactor the handling of nested types. ([#7](https://github.com/ros2/rosidl_dynamic_typesupport/issues/7))
- Add C++ version check to char16 definition ([#3](https://github.com/ros2/rosidl_dynamic_typesupport/issues/3))
- Contributors: Antonio Cuadros, Chris Lalancette, G.A. vd. Hoorn

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/jazzy/rosidl_generator_c/CHANGELOG.rst)

- Fixed warnings - strict-prototypes ([#800](https://github.com/ros2/rosidl/issues/800)) ([#802](https://github.com/ros2/rosidl/issues/802))
- Set hints to find the python version we actually want. ([#785](https://github.com/ros2/rosidl/issues/785))
- Add rosidl\_find\_package\_idl helper function ([#754](https://github.com/ros2/rosidl/issues/754))
- Fix IWYU for clangd in C and C++ ([#742](https://github.com/ros2/rosidl/issues/742))
- Contributors: Alexis Paques, Chris Lalancette, Mike Purvis, mergify[bot]

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/jazzy/rosidl_generator_cpp/CHANGELOG.rst)

- Set hints to find the python version we actually want. ([#785](https://github.com/ros2/rosidl/issues/785))
- Fix constant generation for C++ floats ([#772](https://github.com/ros2/rosidl/issues/772))
- Add rosidl\_find\_package\_idl helper function ([#754](https://github.com/ros2/rosidl/issues/754))
- Fixed visibility control file added to wrong header list variable. ([#755](https://github.com/ros2/rosidl/issues/755))
- Fix deprecation warnings for message constants ([#750](https://github.com/ros2/rosidl/issues/750))
- Generate typesupport declarations for actions, messages and services ([#703](https://github.com/ros2/rosidl/issues/703))
- Fix IWYU for clangd in C and C++ ([#742](https://github.com/ros2/rosidl/issues/742))
- Contributors: Alexis Paques, Chris Lalancette, Emerson Knapp, Mike Purvis, Stefan Fabian

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/jazzy/rosidl_generator_dds_idl/CHANGELOG.rst)

- Remove unnecessary parentheses. ([#61](https://github.com/ros2/rosidl_dds/issues/61))
- Contributors: Chris Lalancette

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/jazzy/rosidl_generator_py/CHANGELOG.rst)

- Revert install of .so files into python path ([#211](https://github.com/ros2/rosidl_python/issues/211)) There seems that some regression might have happened after [#195](https://github.com/ros2/rosidl_python/issues/195). When removing those 2 lines, we avoid to install the .so files in lib *and* python path.
- Prototype code for seeing if FindPython3 is usable for rosidl\_python ([#140](https://github.com/ros2/rosidl_python/issues/140))
- Add in a missing space. ([#203](https://github.com/ros2/rosidl_python/issues/203))
- Install compiled libraries only to ‘lib’ ([#195](https://github.com/ros2/rosidl_python/issues/195))
- Fix: Missing dependency that causes cmake error in downstream (resolves <https://github.com/ros2/rosidl_python/issues/198>) ([#199](https://github.com/ros2/rosidl_python/issues/199))
- Contributors: Chris Lalancette, Isaac Saito, Matthias Schoepfer, Scott K Logan, Shane Loretz

<a id="rosidl-generator-tests"></a>

## [rosidl\_generator\_tests](https://github.com/ros2/rosidl/tree/jazzy/rosidl_generator_tests/CHANGELOG.rst)

- Fixed warnings - strict-prototypes ([#800](https://github.com/ros2/rosidl/issues/800)) ([#802](https://github.com/ros2/rosidl/issues/802))
- Increased the cpplint timeout to 300 seconds ([#797](https://github.com/ros2/rosidl/issues/797))
- Fixes for modern uncrustify. ([#793](https://github.com/ros2/rosidl/issues/793))
- Fix constant generation for C++ floats ([#772](https://github.com/ros2/rosidl/issues/772))
- Fix same named types overriding typesources ([#759](https://github.com/ros2/rosidl/issues/759))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Emerson Knapp, mergify[bot]

<a id="rosidl-generator-type-description"></a>

## [rosidl\_generator\_type\_description](https://github.com/ros2/rosidl/tree/jazzy/rosidl_generator_type_description/CHANGELOG.rst)

- Set hints to find the python version we actually want. ([#785](https://github.com/ros2/rosidl/issues/785))
- Remove unnecessary parentheses. ([#783](https://github.com/ros2/rosidl/issues/783))
- Contributors: Chris Lalancette

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/jazzy/rosidl_parser/CHANGELOG.rst)

- Adding interfaces to support `@key` annotation ([#796](https://github.com/ros2/rosidl/issues/796)) Co-authored-by: Mario Dominguez <[mariodominguez@eprosima.com](mailto:mariodominguez%40eprosima.com)>
- Small fix for newer flake8 compatibility. ([#792](https://github.com/ros2/rosidl/issues/792))
- Remove unnecessary parentheses. ([#783](https://github.com/ros2/rosidl/issues/783))
- Contributors: Chris Lalancette, Miguel Company

<a id="rosidl-pycommon"></a>

## [rosidl\_pycommon](https://github.com/ros2/rosidl/tree/jazzy/rosidl_pycommon/CHANGELOG.rst)

- Remove unnecessary parentheses. ([#783](https://github.com/ros2/rosidl/issues/783))
- Fix same named types overriding typesources ([#759](https://github.com/ros2/rosidl/issues/759))
- Contributors: Chris Lalancette, Emerson Knapp

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/jazzy/rosidl_runtime_c/CHANGELOG.rst)

- Switch to target\_link\_libraries. ([#776](https://github.com/ros2/rosidl/issues/776))
- Set the C++ version to 17. ([#761](https://github.com/ros2/rosidl/issues/761))
- Mark \_ in benchmark tests as unused. ([#741](https://github.com/ros2/rosidl/issues/741)) This helps clang static analysis.
- Contributors: Chris Lalancette

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/jazzy/rosidl_runtime_cpp/CHANGELOG.rst)

- Suppress a warning around BoundedVector. ([#803](https://github.com/ros2/rosidl/issues/803)) ([#804](https://github.com/ros2/rosidl/issues/804)) The comment has more explanation, but in short GCC 13 has false positives around some warnings, so we suppress it for BoundedVector. (cherry picked from commit 858e76adb03edba00469b91d50dd5fe0dcb34236) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Contributors: mergify[bot]

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/jazzy/CHANGELOG.rst)

- Some fixes for modern flake8. ([#25](https://github.com/ros2/rosidl_runtime_py/issues/25))
- Contributors: Chris Lalancette

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/jazzy/rosidl_typesupport_c/CHANGELOG.rst)

- Fixed warnings - strict-prototypes ([#155](https://github.com/ros2/rosidl_typesupport/issues/155)) ([#156](https://github.com/ros2/rosidl_typesupport/issues/156))
- compare string contents but string pointer addresses. ([#153](https://github.com/ros2/rosidl_typesupport/issues/153))
- Set hints to find the python version we actually want. ([#150](https://github.com/ros2/rosidl_typesupport/issues/150))
- Don’t override user provided compile definitions ([#145](https://github.com/ros2/rosidl_typesupport/issues/145))
- Contributors: Chris Lalancette, Emerson Knapp, Tomoya Fujita, mergify[bot]

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/jazzy/rosidl_typesupport_cpp/CHANGELOG.rst)

- compare string contents but string pointer addresses. ([#153](https://github.com/ros2/rosidl_typesupport/issues/153))
- Set hints to find the python version we actually want. ([#150](https://github.com/ros2/rosidl_typesupport/issues/150))
- Don’t override user provided compile definitions ([#145](https://github.com/ros2/rosidl_typesupport/issues/145))
- Added C interfaces to obtain service and action type support. ([#143](https://github.com/ros2/rosidl_typesupport/issues/143))
- Contributors: Chris Lalancette, Emerson Knapp, Stefan Fabian, Tomoya Fujita

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/jazzy/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- Adding interfaces to support `@key` annotation ([#116](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/116)) Co-authored-by: Mario Dominguez <[mariodominguez@eprosima.com](mailto:mariodominguez%40eprosima.com)>
- Support Fast CDR v2 ([#114](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/114))
- Improve wide string (de)serialization ([#113](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/113))
- Set hints to find the python version we actually want. ([#112](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/112)) Co-authored-by: Michael Carroll <[michael@openrobotics.org](mailto:michael%40openrobotics.org)>
- Update to C++17 ([#111](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/111))
- Account for alignment on `is_plain` calculations ([#108](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/108))
- Contributors: Chris Lalancette, Miguel Company

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/jazzy/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- Fix how header template works to prevent double-inclusion ([#117](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/117)) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Adding interfaces to support `@key` annotation ([#116](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/116)) Co-authored-by: Mario Dominguez <[mariodominguez@eprosima.com](mailto:mariodominguez%40eprosima.com)>
- Support Fast CDR v2 ([#114](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/114))
- Improve wide string (de)serialization ([#113](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/113))
- Set hints to find the python version we actually want. ([#112](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/112)) Co-authored-by: Michael Carroll <[michael@openrobotics.org](mailto:michael%40openrobotics.org)>
- Update to C++17 ([#111](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/111))
- Account for alignment on `is_plain` calculations ([#108](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/108))
- Avoid redundant declarations in generated code for services and actions ([#102](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/102))
- Contributors: Chris Lalancette, Emerson Knapp, Michael Carroll, Miguel Company

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/jazzy/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Fixed warnings - strict-prototypes ([#800](https://github.com/ros2/rosidl/issues/800)) ([#802](https://github.com/ros2/rosidl/issues/802))
- Adding interfaces to support `@key` annotation ([#796](https://github.com/ros2/rosidl/issues/796)) Co-authored-by: Mario Dominguez <[mariodominguez@eprosima.com](mailto:mariodominguez%40eprosima.com)>
- Set hints to find the python version we actually want. ([#785](https://github.com/ros2/rosidl/issues/785))
- Add rosidl\_find\_package\_idl helper function ([#754](https://github.com/ros2/rosidl/issues/754))
- update comment ([#757](https://github.com/ros2/rosidl/issues/757))
- Contributors: Chen Lihui, Chris Lalancette, Miguel Company, Mike Purvis, mergify[bot]

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/jazzy/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Adding interfaces to support `@key` annotation ([#796](https://github.com/ros2/rosidl/issues/796)) Co-authored-by: Mario Dominguez <[mariodominguez@eprosima.com](mailto:mariodominguez%40eprosima.com)>
- Set hints to find the python version we actually want. ([#785](https://github.com/ros2/rosidl/issues/785))
- Switch to target\_link\_libraries. ([#776](https://github.com/ros2/rosidl/issues/776))
- Add rosidl\_find\_package\_idl helper function ([#754](https://github.com/ros2/rosidl/issues/754))
- update comment ([#757](https://github.com/ros2/rosidl/issues/757))
- Fix deprecation warnings for message constants ([#750](https://github.com/ros2/rosidl/issues/750))
- Contributors: Chen Lihui, Chris Lalancette, Emerson Knapp, Miguel Company, Mike Purvis

<a id="rosidl-typesupport-introspection-tests"></a>

## [rosidl\_typesupport\_introspection\_tests](https://github.com/ros2/rosidl/tree/jazzy/rosidl_typesupport_introspection_tests/CHANGELOG.rst)

- One last uncrustify fix for newer uncrustify. ([#795](https://github.com/ros2/rosidl/issues/795))
- Disable zero-variadic-macro-arguments warning when using clang. ([#768](https://github.com/ros2/rosidl/issues/768))
- Fixed C++20 warning implicit capture of this in lambda ([#766](https://github.com/ros2/rosidl/issues/766))
- Contributors: AiVerisimilitude, Chris Lalancette

<a id="rosidl-typesupport-tests"></a>

## [rosidl\_typesupport\_tests](https://github.com/ros2/rosidl_typesupport/tree/jazzy/rosidl_typesupport_tests/CHANGELOG.rst)

- Suppress uncrustify on long lines. ([#152](https://github.com/ros2/rosidl_typesupport/issues/152))
- Contributors: Chris Lalancette

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/jazzy/CHANGELOG.rst)

- correct the URL and f-strings format ([#11](https://github.com/ros2/rpyutils/issues/11))
- Contributors: Chen Lihui

<a id="rqt"></a>

## [rqt](https://github.com/ros-visualization/rqt/tree/jazzy/rqt/CHANGELOG.rst)

- Add a test dependency on pytest. ([#306](https://github.com/ros-visualization/rqt/issues/306))
- Contributors: Chris Lalancette

<a id="rqt-bag"></a>

## [rqt\_bag](https://github.com/ros-visualization/rqt_bag/tree/jazzy/rqt_bag/CHANGELOG.rst)

- Add in copyright tests to rqt\_bag. ([#154](https://github.com/ros-visualization/rqt_bag/issues/154))
- Add a test dependency on pytest. ([#153](https://github.com/ros-visualization/rqt_bag/issues/153))
- Revert “Add a dependency on pytest to rqt\_bag and rqt\_bag\_plugins. (#… ([#151](https://github.com/ros-visualization/rqt_bag/issues/151))
- Update maintainer to myself. ([#150](https://github.com/ros-visualization/rqt_bag/issues/150))
- Update maintainer list in package.xml files ([#149](https://github.com/ros-visualization/rqt_bag/issues/149))
- Add a dependency on pytest to rqt\_bag and rqt\_bag\_plugins. ([#148](https://github.com/ros-visualization/rqt_bag/issues/148))
- [ros2] Enable Save ([#142](https://github.com/ros-visualization/rqt_bag/issues/142))
- Call close ([#141](https://github.com/ros-visualization/rqt_bag/issues/141))
- Use default storage id ([#139](https://github.com/ros-visualization/rqt_bag/issues/139))
- Contributors: Chris Lalancette, Michael Jeronimo, Yadu, Yadunund

<a id="rqt-bag-plugins"></a>

## [rqt\_bag\_plugins](https://github.com/ros-visualization/rqt_bag/tree/jazzy/rqt_bag_plugins/CHANGELOG.rst)

- Add a test dependency on pytest. ([#153](https://github.com/ros-visualization/rqt_bag/issues/153))
- Revert “Add a dependency on pytest to rqt\_bag and rqt\_bag\_plugins. (#… ([#151](https://github.com/ros-visualization/rqt_bag/issues/151))
- Update maintainer to myself. ([#150](https://github.com/ros-visualization/rqt_bag/issues/150))
- Update maintainer list in package.xml files ([#149](https://github.com/ros-visualization/rqt_bag/issues/149))
- Add a dependency on pytest to rqt\_bag and rqt\_bag\_plugins. ([#148](https://github.com/ros-visualization/rqt_bag/issues/148))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="rqt-console"></a>

## [rqt\_console](https://github.com/ros-visualization/rqt_console/tree/jazzy/CHANGELOG.rst)

- Add a test dependency on pytest. ([#45](https://github.com/ros-visualization/rqt_console/issues/45))
- Contributors: Arne Hitzmann, Chris Lalancette

<a id="rqt-graph"></a>

## [rqt\_graph](https://github.com/ros-visualization/rqt_graph/tree/jazzy/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#92](https://github.com/ros-visualization/rqt_graph/issues/92))
- Add a test dependency on python3-pytest. ([#91](https://github.com/ros-visualization/rqt_graph/issues/91))
- Refresh rosgraph when params checkbox is clicked ([#86](https://github.com/ros-visualization/rqt_graph/issues/86))
- Contributors: Chris Lalancette, Michael Jeronimo, Yadunund

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/jazzy/rqt_gui_cpp/CHANGELOG.rst)

- Switch to target\_link\_libraries. ([#297](https://github.com/ros-visualization/rqt/issues/297))
- Contributors: Chris Lalancette

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/jazzy/rqt_gui_py/CHANGELOG.rst)

- fix an exception raised while press ctrl+c to exit ([#291](https://github.com/ros-visualization/rqt/issues/291))
- Contributors: Chen Lihui

<a id="rqt-msg"></a>

## [rqt\_msg](https://github.com/ros-visualization/rqt_msg/tree/jazzy/CHANGELOG.rst)

- Add in python3-pytest test dependency. ([#19](https://github.com/ros-visualization/rqt_msg/issues/19))
- Small cleanups to rqt\_msg ([#16](https://github.com/ros-visualization/rqt_msg/issues/16))
- Contributors: Chris Lalancette

<a id="rqt-plot"></a>

## [rqt\_plot](https://github.com/ros-visualization/rqt_plot/tree/jazzy/CHANGELOG.rst)

- Add in copyright tests to rqt\_bag. ([#95](https://github.com/ros-visualization/rqt_plot/issues/95))
- Add a test dependency on pytest. ([#94](https://github.com/ros-visualization/rqt_plot/issues/94))
- Add in a pytest dependency for running tests. ([#92](https://github.com/ros-visualization/rqt_plot/issues/92))
- Fix regression from #87 ([#90](https://github.com/ros-visualization/rqt_plot/issues/90))
- Contributors: Chris Lalancette, Yadunund

<a id="rqt-publisher"></a>

## [rqt\_publisher](https://github.com/ros-visualization/rqt_publisher/tree/jazzy/CHANGELOG.rst)

- Use raw strings for regular expressions. ([#44](https://github.com/ros-visualization/rqt_publisher/issues/44))
- Switch maintainer to me. ([#43](https://github.com/ros-visualization/rqt_publisher/issues/43))
- Update maintainer list in package.xml files ([#42](https://github.com/ros-visualization/rqt_publisher/issues/42))
- Add in a test dependency on pytest. ([#41](https://github.com/ros-visualization/rqt_publisher/issues/41))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/jazzy/rqt_py_common/CHANGELOG.rst)

- Allow to autocomplete namespaced topics ([#299](https://github.com/ros-visualization/rqt/issues/299))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-py-console"></a>

## [rqt\_py\_console](https://github.com/ros-visualization/rqt_py_console/tree/jazzy/CHANGELOG.rst)

- Add in test dependency on pytest. ([#16](https://github.com/ros-visualization/rqt_py_console/issues/16))
- Fix a crash in the rqt\_py\_console dialog box. ([#15](https://github.com/ros-visualization/rqt_py_console/issues/15))
- Contributors: Chris Lalancette

<a id="rqt-reconfigure"></a>

## [rqt\_reconfigure](https://github.com/ros-visualization/rqt_reconfigure/tree/jazzy/CHANGELOG.rst)

- Explicitly add a pytest test dependency. ([#141](https://github.com/ros-visualization/rqt_reconfigure/issues/141))
- Remove unnecessary parentheses around if statements. ([#140](https://github.com/ros-visualization/rqt_reconfigure/issues/140))
- Fixed executor conflict ([#126](https://github.com/ros-visualization/rqt_reconfigure/issues/126))
- Add param filtering ([#128](https://github.com/ros-visualization/rqt_reconfigure/issues/128))
- Fix handling of namespaces in the node tree ([#132](https://github.com/ros-visualization/rqt_reconfigure/issues/132))
- Contributors: Aleksander Szymański, Chris Lalancette, Devarsi Rawal, Nick Lamprianidis

<a id="rqt-service-caller"></a>

## [rqt\_service\_caller](https://github.com/ros-visualization/rqt_service_caller/tree/jazzy/CHANGELOG.rst)

- Add in a pytest test dependency. ([#28](https://github.com/ros-visualization/rqt_service_caller/issues/28))
- Contributors: Chris Lalancette

<a id="rqt-shell"></a>

## [rqt\_shell](https://github.com/ros-visualization/rqt_shell/tree/jazzy/CHANGELOG.rst)

- Change maintainer to clalancette. ([#21](https://github.com/ros-visualization/rqt_shell/issues/21))
- Add in pytest test dependency. ([#19](https://github.com/ros-visualization/rqt_shell/issues/19))
- Contributors: Chris Lalancette, Michael Jeronimo

<a id="rqt-srv"></a>

## [rqt\_srv](https://github.com/ros-visualization/rqt_srv/tree/jazzy/CHANGELOG.rst)

- Add explicit dependency to python3-pytest. ([#12](https://github.com/ros-visualization/rqt_srv/issues/12))
- Minor cleanups in rqt\_srv for ROS 2 ([#9](https://github.com/ros-visualization/rqt_srv/issues/9))
- Contributors: Chris Lalancette

<a id="rqt-topic"></a>

## [rqt\_topic](https://github.com/ros-visualization/rqt_topic/tree/jazzy/CHANGELOG.rst)

- Small fix for modern flake8. ([#50](https://github.com/ros-visualization/rqt_topic/issues/50))
- Add explicit python3-pytest dependency. ([#48](https://github.com/ros-visualization/rqt_topic/issues/48))
- Contributors: Chris Lalancette

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/jazzy/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Use unified approach for checking the existence of environment variables ([#105](https://github.com/ros2/rmw_connextdds/issues/105))
- Contributors: Christopher Wecht

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/jazzy/rttest/CHANGELOG.rst)

- Update to C++17 ([#124](https://github.com/ros2/realtime_support/issues/124))
- Contributors: Chris Lalancette

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/jazzy/rviz2/CHANGELOG.rst)

- Add “R” key as shortcut for resetTime ([#1088](https://github.com/ros2/rviz/issues/1088))
- Switch to target\_link\_libraries. ([#1098](https://github.com/ros2/rviz/issues/1098))
- Contributors: Chris Lalancette, Paul Erik Frivold

<a id="rviz-assimp-vendor"></a>

## [rviz\_assimp\_vendor](https://github.com/ros2/rviz/tree/jazzy/rviz_assimp_vendor/CHANGELOG.rst)

- Removed assimp warnings ([#1191](https://github.com/ros2/rviz/issues/1191)) ([#1192](https://github.com/ros2/rviz/issues/1192)) (cherry picked from commit e8dd485d19a35d3abba905020741973e613334e3) Co-authored-by: Alejandro Hernández Cordero <[alejandro@openrobotics.org](mailto:alejandro%40openrobotics.org)>
- Update the vendored package path. ([#1184](https://github.com/ros2/rviz/issues/1184)) Since we just updated to assimp 5.3, we also need to update the path we look for it. This should fix the build with clang which is currently failing.
- Update assimp vendor to 5.3.1 ([#1182](https://github.com/ros2/rviz/issues/1182)) This matches what is in Ubuntu 24.04.
- Update to assimp 5.2.2 ([#968](https://github.com/ros2/rviz/issues/968))
- Fix the vendoring flags for clang compilation. ([#1003](https://github.com/ros2/rviz/issues/1003))
- Switch to ament\_cmake\_vendor\_package ([#995](https://github.com/ros2/rviz/issues/995))
- Contributors: Chris Lalancette, Scott K Logan, mergify[bot]

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/jazzy/rviz_common/CHANGELOG.rst)

- Update to yaml-cpp 0.8.0 ([#1183](https://github.com/ros2/rviz/issues/1183)) yaml-cpp 0.8.0 has a proper CMake target, i.e. yaml-cpp::yaml-cpp. Use that here.
- Remove regex\_filter\_property.hpp from the moc lines. ([#1172](https://github.com/ros2/rviz/issues/1172)) Since it has no SLOTS or SIGNALS, we don’t need to run MOC on it. That will both speed up the compilation and remove a warning when building.
- Added regex filter field for TF display ([#1032](https://github.com/ros2/rviz/issues/1032))
- Fix camera display overlay ([#1151](https://github.com/ros2/rviz/issues/1151))
- Fixes for uncrustify 0.78. ([#1155](https://github.com/ros2/rviz/issues/1155)) Mostly what we do here is to disable the indentation on certain constructs that are different between 0.72 and 0.78. It isn’t my preferred solution, but since it only affects a small amount of code (and most of that in macros), this seems acceptable to me.
- Append measured subscription frequency to topic status ([#1113](https://github.com/ros2/rviz/issues/1113))
- Implement reset time service ([#1109](https://github.com/ros2/rviz/issues/1109))
- Add “R” key as shortcut for resetTime ([#1088](https://github.com/ros2/rviz/issues/1088))
- Add fullscreen startup option ([#1097](https://github.com/ros2/rviz/issues/1097))
- Switch to target\_link\_libraries. ([#1098](https://github.com/ros2/rviz/issues/1098))
- Initialize more of the visualization\_manager members. ([#1090](https://github.com/ros2/rviz/issues/1090))
- Explicit time conversions and comparisons ([#1087](https://github.com/ros2/rviz/issues/1087))
- Rolling namespace in title ([#1074](https://github.com/ros2/rviz/issues/1074))
- Removed unused code ([#1044](https://github.com/ros2/rviz/issues/1044))
- Remove unused LineEditWithButton::simulateReturnPressed() ([#1040](https://github.com/ros2/rviz/issues/1040))
- Remove warning in depth\_cloud\_mld.cpp ([#1021](https://github.com/ros2/rviz/issues/1021))
- Added DepthCloud default plugin ([#996](https://github.com/ros2/rviz/issues/996))
- Stop inheriting from std::iterator. ([#1013](https://github.com/ros2/rviz/issues/1013)) In C++17, inheriting from std::iterator has been deprecated: https://www.fluentcpp.com/2018/05/08/std-iterator-deprecated/ Here, switch away from inheriting and just define the interface ourselves (which is the current recommended best practice). This removes some warnings when building with gcc 13.1.1
- use static QCoreApplication::processEvents() function without a QApplication instance ([#924](https://github.com/ros2/rviz/issues/924))
- Re-implemented setName for tools ([#989](https://github.com/ros2/rviz/issues/989))
- Add a libqt5-svg dependency to rviz\_common. ([#992](https://github.com/ros2/rviz/issues/992))
- Remove onHelpWiki. ([#985](https://github.com/ros2/rviz/issues/985))
- Clean Code ([#975](https://github.com/ros2/rviz/issues/975))
- Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Chris Lalancette, Felix Exner (fexner), Hyunseok, Markus Bader, Paul Erik Frivold, Yadu, Yannis Gerlach, mosfet80

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/jazzy/rviz_default_plugins/CHANGELOG.rst)

- Make sure to export all rviz\_default\_plugins dependencies. ([#1181](https://github.com/ros2/rviz/issues/1181))
- Increase the cpplint timeout to 180 seconds. ([#1179](https://github.com/ros2/rviz/issues/1179))
- Switch to gz\_math\_vendor. ([#1177](https://github.com/ros2/rviz/issues/1177))
- Fixed camera info warning ([#1175](https://github.com/ros2/rviz/issues/1175))
- Added CameraInfo display ([#1166](https://github.com/ros2/rviz/issues/1166))
- apply origin rotation to inertia box visualization ([#1171](https://github.com/ros2/rviz/issues/1171))
- Added regex filter field for TF display ([#1032](https://github.com/ros2/rviz/issues/1032))
- Added point\_cloud\_transport ([#1008](https://github.com/ros2/rviz/issues/1008))
- Select QoS reliability policy in DepthCloud Plugin ([#1159](https://github.com/ros2/rviz/issues/1159))
- Fixed crash on DepthCloud plugin ([#1161](https://github.com/ros2/rviz/issues/1161))
- Fixes for uncrustify 0.78. ([#1155](https://github.com/ros2/rviz/issues/1155)) Mostly what we do here is to disable the indentation on certain constructs that are different between 0.72 and 0.78. It isn’t my preferred solution, but since it only affects a small amount of code (and most of that in macros), this seems acceptable to me.
- Fixed crash on DepthCloudPlugin ([#1133](https://github.com/ros2/rviz/issues/1133))
- Wrench accepth nan values fix ([#1141](https://github.com/ros2/rviz/issues/1141))
- DepthCloud plugin: Append measured subscription frequency to topic status ([#1137](https://github.com/ros2/rviz/issues/1137))
- Added Cache to camera display for TimeExact ([#1138](https://github.com/ros2/rviz/issues/1138))
- Fixed transport name in DepthCloud plugin ([#1134](https://github.com/ros2/rviz/issues/1134))
- Fix time-syncing message ([#1121](https://github.com/ros2/rviz/issues/1121))
- Switch from ROS\_TIME to SYSTEM\_TIME on rclcpp::Time construction ([#1117](https://github.com/ros2/rviz/issues/1117))
- Append measured subscription frequency to topic status ([#1113](https://github.com/ros2/rviz/issues/1113))
- Fix typo ([#1104](https://github.com/ros2/rviz/issues/1104))
- Fix potencial leak / seg fault ([#726](https://github.com/ros2/rviz/issues/726))
- Fixed screw display ([#1093](https://github.com/ros2/rviz/issues/1093))
- Explicit time conversions and comparisons ([#1087](https://github.com/ros2/rviz/issues/1087))
- Handle missing effort limit in URDF ([#1084](https://github.com/ros2/rviz/issues/1084))
- (robot) fix styling of log msg ([#1080](https://github.com/ros2/rviz/issues/1080))
- Fix image display wrapping ([#1038](https://github.com/ros2/rviz/issues/1038))
- removed enableInteraction reference ([#1075](https://github.com/ros2/rviz/issues/1075))
- Fix ODR violations in interactive\_marker displays. ([#1068](https://github.com/ros2/rviz/issues/1068))
- Improve error handling in LaserScanDisplay ([#1035](https://github.com/ros2/rviz/issues/1035))
- Fix implicit capture of “this” warning in C++20 ([#1053](https://github.com/ros2/rviz/issues/1053))
- Removed unused code ([#1044](https://github.com/ros2/rviz/issues/1044))
- Fixed AccelStamped, TwistStamped and Wrench icons ([#1041](https://github.com/ros2/rviz/issues/1041))
- Fix the flakey rviz\_rendering tests ([#1026](https://github.com/ros2/rviz/issues/1026))
- Don’t pass screw\_display.hpp to the moc generator. ([#1018](https://github.com/ros2/rviz/issues/1018)) Since it isn’t a Qt class, you get a warning from moc: Note: No relevant classes found. No output generated. Just skip adding it to the moc list here, which gets rid of the warning.
- Added DepthCloud default plugin ([#996](https://github.com/ros2/rviz/issues/996))
- Added TwistStamped and AccelStamped default plugins ([#991](https://github.com/ros2/rviz/issues/991))
- Added Effort plugin ([#990](https://github.com/ros2/rviz/issues/990))
- Improve the compilation time of rviz\_default\_plugins ([#1007](https://github.com/ros2/rviz/issues/1007))
- Switch to ament\_cmake\_vendor\_package ([#995](https://github.com/ros2/rviz/issues/995))
- Modify access specifier to protected or public for the scope of processMessage() member function ([#984](https://github.com/ros2/rviz/issues/984))
- Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Austin Moore, Chris Lalancette, Christoph Fröhlich, Hyunseok, Jonas Otto, Lewe Christiansen, Matthijs van der Burgh, Patrick Roncagliolo, Scott K Logan, Yadu

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/jazzy/rviz_ogre_vendor/CHANGELOG.rst)

- Update zlib into CMakeLists.txt ([#1128](https://github.com/ros2/rviz/issues/1128)) ([#1195](https://github.com/ros2/rviz/issues/1195)) Changes in 1.3 (18 Aug 2023) - Remove K&R function definitions and zlib2ansi - Fix bug in deflateBound() for level 0 and memLevel 9 - Fix bug when gzungetc() is used immediately after gzopen() - Fix bug when using gzflush() with a very small buffer - Fix crash when gzsetparams() attempted for transparent write - Fix test/example.c to work with FORCE\_STORED - Rewrite of zran in examples (see zran.c version history) - Fix minizip to allow it to open an empty zip file - Fix reading disk number start on zip64 files in minizip - Fix logic error in minizip argument processing - Add minizip testing to Makefile - Read multiple bytes instead of byte-by-byte in minizip unzip.c - Add memory sanitizer to configure (–memory) - Various portability improvements - Various documentation improvements - Various spelling and typo corrections Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)> (cherry picked from commit 32eb8b9404927883247e868ab0c7d62b80df2ed1) Co-authored-by: mosfet80 <[realeandrea@yahoo.it](mailto:realeandrea%40yahoo.it)>
- Change an rviz\_ogre\_vendor dependency to libfreetype-dev. ([#1167](https://github.com/ros2/rviz/issues/1167)) The situation is complicated, but in versions of Ubuntu prior to Focal and versions of Debian prior to Bookworm, the name of the library was ‘libfreetype6-dev’. Since Focal and Bookworm, the name of the library is ‘libfreetype-dev’. While ‘libfreetype-dev’ provides a “virtual package” for ‘libfreetype6-dev’, we should really use the new canonical name. Further, there is currently a bug on ros\_buildfarm where it doesn’t properly deal with “virtual packages” like this. This is currently preventing this package from building on Ubuntu Noble. That bug is being worked on separately. Finally, I’ll note that we already have a libfreetype-dev key in rosdep, so we just switch to using that here which should work around the bug on the buildfarm, and also use the correct canonical name going forward.
- fix: modify typo in cmake args for mac ([#1160](https://github.com/ros2/rviz/issues/1160))
- feat: support macos ([#1156](https://github.com/ros2/rviz/issues/1156))
- Suppress a couple more of clang warnings in rviz\_ogre\_vendor. ([#1102](https://github.com/ros2/rviz/issues/1102))
- Fix the vendoring flags for clang compilation. ([#1003](https://github.com/ros2/rviz/issues/1003)) Several of the flags are not available on clang, so don’t add them there. This fixes the clang build for me locally.
- Switch to ament\_cmake\_vendor\_package ([#995](https://github.com/ros2/rviz/issues/995))
- CMake: rename FeatureSummary.cmake to avoid name clashes ([#953](https://github.com/ros2/rviz/issues/953))
- FIX CVE in external libraries ([#961](https://github.com/ros2/rviz/issues/961))
- Contributors: Chris Lalancette, Daisuke Nishimatsu, Gökçe Aydos, Scott K Logan, mergify[bot], mosfet80

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/jazzy/rviz_rendering/CHANGELOG.rst)

- Added CameraInfo display ([#1166](https://github.com/ros2/rviz/issues/1166))
- Fix camera display overlay ([#1151](https://github.com/ros2/rviz/issues/1151))
- Fixes for uncrustify 0.78. ([#1155](https://github.com/ros2/rviz/issues/1155)) Mostly what we do here is to disable the indentation on certain constructs that are different between 0.72 and 0.78. It isn’t my preferred solution, but since it only affects a small amount of code (and most of that in macros), this seems acceptable to me.
- fixed MovableText::getWorldTransforms transform ([#1118](https://github.com/ros2/rviz/issues/1118))
- Switch to target\_link\_libraries. ([#1098](https://github.com/ros2/rviz/issues/1098))
- Update rviz\_rendering and rviz\_rendering\_tests to C++17. ([#1096](https://github.com/ros2/rviz/issues/1096))
- Include MeshShape class ([#1064](https://github.com/ros2/rviz/issues/1064))
- Use assimp to load stl ([#1063](https://github.com/ros2/rviz/issues/1063))
- RVIZ\_RENDERING\_PUBLIC to export class RenderSystem ([#1072](https://github.com/ros2/rviz/issues/1072))
- Restore the maybe-uninitialized flag in covariance\_visual.hpp ([#1071](https://github.com/ros2/rviz/issues/1071))
- Fix up warnings when building with clang. ([#1070](https://github.com/ros2/rviz/issues/1070))
- Use buildsystem info to get the ros\_package\_name ([#1062](https://github.com/ros2/rviz/issues/1062))
- make box-mode point cloud shader lighter on top than bottom ([#1058](https://github.com/ros2/rviz/issues/1058))
- Removed warning when building in release mode ([#1057](https://github.com/ros2/rviz/issues/1057))
- Fixed low FPS when sending point markers ([#1049](https://github.com/ros2/rviz/issues/1049))
- Removed unused code ([#1044](https://github.com/ros2/rviz/issues/1044))
- Fix the flakey rviz\_rendering tests ([#1026](https://github.com/ros2/rviz/issues/1026))
- Added TwistStamped and AccelStamped default plugins ([#991](https://github.com/ros2/rviz/issues/991))
- Added Effort plugin ([#990](https://github.com/ros2/rviz/issues/990))
- load GLB meshes ([#1001](https://github.com/ros2/rviz/issues/1001))
- Fixed camera default plusin crash ([#999](https://github.com/ros2/rviz/issues/999))
- Clean Code ([#975](https://github.com/ros2/rviz/issues/975)) \* Clean Code
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Felix F Xu, Morgan Quigley, Yaswanth, mosfet80

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/jazzy/rviz_rendering_tests/CHANGELOG.rst)

- Remove the loading\_ascii\_stl\_files\_fail ([#1125](https://github.com/ros2/rviz/issues/1125))
- Update rviz\_rendering and rviz\_rendering\_tests to C++17. ([#1096](https://github.com/ros2/rviz/issues/1096))
- Use assimp to load stl ([#1063](https://github.com/ros2/rviz/issues/1063))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/jazzy/rviz_visual_testing_framework/CHANGELOG.rst)

- Improve the compilation time of rviz\_default\_plugins ([#1007](https://github.com/ros2/rviz/issues/1007))
- Contributors: Chris Lalancette

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/sensor_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- [J-Turtle] Fix uninitialized values in NavSatFix and add missing NavSatStatus UNKNOWN ([#220](https://github.com/ros2/common_interfaces/issues/220)) \* Fix unitialized values in NavSatFix and add missing UNKNOWN \* Fixes [#196](https://github.com/ros2/common_interfaces/issues/196) \* Fix default initialization instead of constants \* Define SERVICE\_UNKNOWN Co-authored-by: Tully Foote <[tully.foote@gmail.com](mailto:tully.foote%40gmail.com)> Co-authored-by: Martin Pecka <[peci1@seznam.cz](mailto:peci1%40seznam.cz)>
- Use target qualifier for checking the cpp typesupport exists ([#238](https://github.com/ros2/common_interfaces/issues/238))
- sensor\_msgs/CompressedImage: updated description of format field ([#231](https://github.com/ros2/common_interfaces/issues/231))
- Return true for isColor if format is YUYV or UYUV ([#229](https://github.com/ros2/common_interfaces/issues/229))
- Contributors: Chris Lalancette, Kenji Brameld, Ryan

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/jazzy/sensor_msgs_py/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Allow pointcloud create\_cloud function to set specific point\_step ([#223](https://github.com/ros2/common_interfaces/issues/223))
- Fix read\_points\_numpy field\_names parameter
- Contributors: Chris Lalancette, George Broughton

<a id="shape-msgs"></a>

## [shape\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/shape_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="shared-queues-vendor"></a>

## [shared\_queues\_vendor](https://github.com/ros2/rosbag2/tree/jazzy/shared_queues_vendor/CHANGELOG.rst)

- Remove unused concurrentqueue implementation. ([#1465](https://github.com/ros2/rosbag2/issues/1465)) rosbag2 only depends on the readerwriter queue.
- Contributors: Chris Lalancette

<a id="spdlog-vendor"></a>

## [spdlog\_vendor](https://github.com/ros2/spdlog_vendor/tree/jazzy/CHANGELOG.rst)

- Removed spdlog\_vendor warnings ([#36](https://github.com/ros2/spdlog_vendor/issues/36)) ([#37](https://github.com/ros2/spdlog_vendor/issues/37)) (cherry picked from commit 4510d9ab4389f84daac77210f3fdf8aab372b938) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Upgrade to v1.12.0. ([#35](https://github.com/ros2/spdlog_vendor/issues/35))
- Switch to ament\_cmake\_vendor\_package ([#34](https://github.com/ros2/spdlog_vendor/issues/34))
- Contributors: Marco A. Gutierrez, Scott K Logan, mergify[bot]

<a id="sqlite3-vendor"></a>

## [sqlite3\_vendor](https://github.com/ros2/rosbag2/tree/jazzy/sqlite3_vendor/CHANGELOG.rst)

- Switch to ament\_cmake\_vendor\_package ([#1400](https://github.com/ros2/rosbag2/issues/1400))
- Contributors: Scott K Logan

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/jazzy/sros2/CHANGELOG.rst)

- Fix linux tutorial: cloning example policies and set of default policies for a node ([#295](https://github.com/ros2/sros2/issues/295)) ([#296](https://github.com/ros2/sros2/issues/296)) \* clone policies to temporary dir as subversion hack doesnt work anymore \* add get\_type\_description service to policies \* update MacOS similarly \* update all permissions with new topics \* dont rule out cycloneDDS \* example of enclave override Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)> (cherry picked from commit ca6bb12cc650b73e7ccfc0fa789d8b49358d44ad) Co-authored-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Use modern PKCS7 to sign the certificate bytes. ([#290](https://github.com/ros2/sros2/issues/290))
- Fix a number of warnings on Ubuntu 24.04. ([#289](https://github.com/ros2/sros2/issues/289))
- Fix SSH commands in SROS2\_Linux.md ([#286](https://github.com/ros2/sros2/issues/286))
- Contributors: Boris Boutillier, Chris Lalancette, mergify[bot]

<a id="std-msgs"></a>

## [std\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/std_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="std-srvs"></a>

## [std\_srvs](https://github.com/ros2/common_interfaces/tree/jazzy/std_srvs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="stereo-msgs"></a>

## [stereo\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/stereo_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/jazzy/test_cli/CHANGELOG.rst)

- Switch to target\_link\_libraries everywhere. ([#532](https://github.com/ros2/system_tests/issues/532))
- Contributors: Chris Lalancette

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/jazzy/test_cli_remapping/CHANGELOG.rst)

- Switch to target\_link\_libraries everywhere. ([#532](https://github.com/ros2/system_tests/issues/532))
- Contributors: Chris Lalancette

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/jazzy/test_communication/CHANGELOG.rst)

- Small fix for modern flake8. ([#539](https://github.com/ros2/system_tests/issues/539))
- Switch to target\_link\_libraries everywhere. ([#532](https://github.com/ros2/system_tests/issues/532))
- Add integration test for nested messages. ([#530](https://github.com/ros2/system_tests/issues/530))
- Adjust for new rclcpp::Rate API ([#516](https://github.com/ros2/system_tests/issues/516))
- Contributors: Alexey Merzlyakov, Chris Lalancette

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/jazzy/test_launch_ros/CHANGELOG.rst)

- Small fixes for modern flake8. ([#395](https://github.com/ros2/launch_ros/issues/395))
- add “–log-file-name” command line argument for test. ([#387](https://github.com/ros2/launch_ros/issues/387))
- Fix an assert in the test\_launch\_ros tests. ([#367](https://github.com/ros2/launch_ros/issues/367))
- Fix misspelled “receive”. ([#362](https://github.com/ros2/launch_ros/issues/362))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="test-launch-testing"></a>

## [test\_launch\_testing](https://github.com/ros2/launch/tree/jazzy/test_launch_testing/CHANGELOG.rst)

- Update to C++17 ([#742](https://github.com/ros2/launch/issues/742))
- Contributors: Chris Lalancette

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/jazzy/test_msgs/CHANGELOG.rst)

- Increase the timeout for the test\_msgs rosidl\_generated\_cpp cpplint. ([#163](https://github.com/ros2/rcl_interfaces/issues/163)) This should make it much more likely to succeed on Windows.
- Fix for invalid conversion from const char8\_t\* to char for C++20 ([#160](https://github.com/ros2/rcl_interfaces/issues/160))
- Contributors: AiVerisimilitude, Chris Lalancette

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/jazzy/test_quality_of_service/CHANGELOG.rst)

- Cleanup header includes in test\_quality\_of\_service. ([#533](https://github.com/ros2/system_tests/issues/533))
- Switch to target\_link\_libraries everywhere. ([#532](https://github.com/ros2/system_tests/issues/532))
- Fix test QoS on macOS by moving qos\_utilities.cpp to the four tests; fixes [#517](https://github.com/ros2/system_tests/issues/517) ([#518](https://github.com/ros2/system_tests/issues/518))
- Contributors: Chris Lalancette, PhDittmann

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/jazzy/test_rclcpp/CHANGELOG.rst)

- Addressed TODO in test\_local\_parameters ([#545](https://github.com/ros2/system_tests/issues/545))
- Actually skip the gtest\_subscription test on Connext. ([#544](https://github.com/ros2/system_tests/issues/544))
- Increased time in test\_multithreaded ([#543](https://github.com/ros2/system_tests/issues/543))
- Improve the node\_name test. ([#538](https://github.com/ros2/system_tests/issues/538))
- Change up the formatting in the test\_rclcpp tests. ([#537](https://github.com/ros2/system_tests/issues/537))
- Revamp test\_rclcpp to compile far few files. ([#535](https://github.com/ros2/system_tests/issues/535))
- Mark gtest\_subscription\_\_rmw\_connextdds xfail. ([#531](https://github.com/ros2/system_tests/issues/531))
- refactor corrected depth check for prefix in parameter\_fixtures.hpp ([#529](https://github.com/ros2/system_tests/issues/529))
- Remove an unnecessary capture in test\_rclcpp. ([#527](https://github.com/ros2/system_tests/issues/527))
- Cleanup of the CMakeLists.txt for test\_rclcpp. ([#526](https://github.com/ros2/system_tests/issues/526))
- Add a fix for the tests given the new type description parameter ([#520](https://github.com/ros2/system_tests/issues/520))
- Changes ros\_timer\_init for ros\_timer\_init2 ([#508](https://github.com/ros2/system_tests/issues/508))
- refactor the multi\_access\_publisher test to avoid dead locks ([#515](https://github.com/ros2/system_tests/issues/515))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Eloy Briceno, Emerson Knapp, Lee, Minju, William Woodall

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/jazzy/test_rmw_implementation/CHANGELOG.rst)

- Compile the test\_rmw\_implementation tests fewer times. ([#224](https://github.com/ros2/rmw_implementation/issues/224))
- Switch to using target\_link\_libraries everywhere. ([#222](https://github.com/ros2/rmw_implementation/issues/222))
- Add rmw\_count\_clients,services & test ([#208](https://github.com/ros2/rmw_implementation/issues/208))
- Contributors: Chris Lalancette, Lee, Minju

<a id="test-ros2trace"></a>

## [test\_ros2trace](https://github.com/ros2/ros2_tracing/tree/jazzy/test_ros2trace/CHANGELOG.rst)

- Add explicit context fields test to test\_ros2trace ([#107](https://github.com/ros2/ros2_tracing/issues/107))
- Allow tracing tests to be run in parallel with other tests ([#95](https://github.com/ros2/ros2_tracing/issues/95))
- Make test\_ros2trace depend on test\_tracetools\_launch.
- Switch to custom lttng-ctl Python bindings ([#81](https://github.com/ros2/ros2_tracing/issues/81))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="test-security"></a>

## [test\_security](https://github.com/ros2/system_tests/tree/jazzy/test_security/CHANGELOG.rst)

- Update to C++17 ([#528](https://github.com/ros2/system_tests/issues/528))
- Switch to target\_link\_libraries everywhere. ([#532](https://github.com/ros2/system_tests/issues/532))
- Adjust for new rclcpp::Rate API ([#516](https://github.com/ros2/system_tests/issues/516))
- Extract sros\_artifacts fixture into a CMake script ([#525](https://github.com/ros2/system_tests/issues/525))
- Use test fixtures to create SROS artifacts ([#522](https://github.com/ros2/system_tests/issues/522))
- Contributors: Alexey Merzlyakov, Chris Lalancette, Scott K Logan

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/jazzy/test_tf2/CHANGELOG.rst)

- Compile fix for upcomming changes to rclcpp::Executor ([#668](https://github.com/ros2/geometry2/issues/668))
- Adding addition BUILD\_TESTING requirement ([#660](https://github.com/ros2/geometry2/issues/660))
- normalize quaternions on tf2\_eigen ([#644](https://github.com/ros2/geometry2/issues/644))
- Contributors: Lucas Wendland, Paul Gesel, jmachowinski

<a id="test-tracetools"></a>

## [test\_tracetools](https://github.com/ros2/ros2_tracing/tree/jazzy/test_tracetools/CHANGELOG.rst)

- Improve tracetools\_test and simplify test\_tracetools code ([#109](https://github.com/ros2/ros2_tracing/issues/109))
- Install test\_tracetools\_mark\_process ([#113](https://github.com/ros2/ros2_tracing/issues/113))
- Remove unnecessary <string> include ([#111](https://github.com/ros2/ros2_tracing/issues/111))
- Include <string> in mark\_process.cpp ([#110](https://github.com/ros2/ros2_tracing/issues/110))
- Remove unnecessary print in test ([#108](https://github.com/ros2/ros2_tracing/issues/108))
- Add test for GenericPublisher/Subscriber ([#97](https://github.com/ros2/ros2_tracing/issues/97))
- Use lttng\_ust\_tracef instead of lttng\_ust\_\_tracef ([#103](https://github.com/ros2/ros2_tracing/issues/103))
- Use a memcmp for the expected symbol name. ([#100](https://github.com/ros2/ros2_tracing/issues/100))
- Fix the build on RHEL-9. ([#98](https://github.com/ros2/ros2_tracing/issues/98))
- Allow tracing tests to be run in parallel with other tests ([#95](https://github.com/ros2/ros2_tracing/issues/95))
- Fix interference between test\_tracetools and ros2lifecycle tests ([#96](https://github.com/ros2/ros2_tracing/issues/96))
- Make tracing test assert messages more descriptive ([#93](https://github.com/ros2/ros2_tracing/issues/93))
- Update tests and docs after new rmw\_publish timestamp field ([#90](https://github.com/ros2/ros2_tracing/issues/90))
- Switch to target\_link\_libraries in test\_tracetools. ([#83](https://github.com/ros2/ros2_tracing/issues/83))
- Improve test coverage of rclcpp\_callback\_register in test\_tracetools ([#69](https://github.com/ros2/ros2_tracing/issues/69))
- Disable tracing on Android ([#71](https://github.com/ros2/ros2_tracing/issues/71))
- Contributors: Chris Lalancette, Christophe Bedard, Przemysław Dąbrowski, h-suzuki-isp

<a id="test-tracetools-launch"></a>

## [test\_tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/jazzy/test_tracetools_launch/CHANGELOG.rst)

- Improve tracing configuration error reporting ([#85](https://github.com/ros2/ros2_tracing/issues/85))
- Contributors: Christophe Bedard

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/jazzy/tf2/CHANGELOG.rst)

- Enable Twist interpolator ([#646](https://github.com/ros2/geometry2/issues/646)) Co-authored-by: Tully Foote <[tullyfoote@intrinsic.ai](mailto:tullyfoote%40intrinsic.ai)>
- Warning Message Intervals for canTransform ([#663](https://github.com/ros2/geometry2/issues/663))
- Nacho/minor fixes tf2 cache ([#658](https://github.com/ros2/geometry2/issues/658))
- Removing console\_bridge ([#655](https://github.com/ros2/geometry2/issues/655))
- Fix constantly increasing memory in std::list ([#636](https://github.com/ros2/geometry2/issues/636))
- Update the tf2 documentation ([#638](https://github.com/ros2/geometry2/issues/638))
- Fix error code returned in BufferCore::walkToTopParent ([#601](https://github.com/ros2/geometry2/issues/601))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ignacio Vizzo, Lucas Wendland, Patrick Roncagliolo

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/jazzy/tf2_bullet/CHANGELOG.rst)

- Removed obsolete headers ([#645](https://github.com/ros2/geometry2/issues/645))
- Contributors: Alejandro Hernández Cordero

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/jazzy/tf2_eigen/CHANGELOG.rst)

- Removed obsolete headers ([#645](https://github.com/ros2/geometry2/issues/645))
- normalize quaternions on tf2\_eigen ([#644](https://github.com/ros2/geometry2/issues/644))
- Fix clang build warnings. ([#628](https://github.com/ros2/geometry2/issues/628))
- Add another reference for twist transformation. Comment correction. ([#620](https://github.com/ros2/geometry2/issues/620))
- Contributors: Alejandro Hernández Cordero, AndyZe, Chris Lalancette, Paul Gesel

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/jazzy/tf2_eigen_kdl/CHANGELOG.rst)

- Fix installation directory of .dll files in tf2\_eigen\_kdl ([#657](https://github.com/ros2/geometry2/issues/657))
- Remove unnecessary use of ament\_target\_dependencies. ([#637](https://github.com/ros2/geometry2/issues/637)) We can just use target\_link\_libraries instead.
- Fix clang build warnings. ([#628](https://github.com/ros2/geometry2/issues/628))
- Contributors: Chris Lalancette, Silvio Traversaro

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/jazzy/tf2_geometry_msgs/CHANGELOG.rst)

- Enable Twist interpolator ([#646](https://github.com/ros2/geometry2/issues/646)) Co-authored-by: Tully Foote <[tullyfoote@intrinsic.ai](mailto:tullyfoote%40intrinsic.ai)>
- Removed obsolete headers ([#645](https://github.com/ros2/geometry2/issues/645))
- Add doTransform support for Point32, Polygon and PolygonStamped (backport [#616](https://github.com/ros2/geometry2/issues/616)) ([#619](https://github.com/ros2/geometry2/issues/619))
- Contributors: Alejandro Hernández Cordero, mergify[bot]

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/jazzy/tf2_kdl/CHANGELOG.rst)

- Removed obsolete headers ([#645](https://github.com/ros2/geometry2/issues/645))
- Contributors: Alejandro Hernández Cordero

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/jazzy/tf2_py/CHANGELOG.rst)

- Enable Twist interpolator ([#646](https://github.com/ros2/geometry2/issues/646)) Co-authored-by: Tully Foote <[tullyfoote@intrinsic.ai](mailto:tullyfoote%40intrinsic.ai)>
- Contributors: Alejandro Hernández Cordero

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/jazzy/tf2_ros/CHANGELOG.rst)

- Compile fix for upcomming changes to rclcpp::Executor ([#668](https://github.com/ros2/geometry2/issues/668))
- Enable Twist interpolator ([#646](https://github.com/ros2/geometry2/issues/646)) Co-authored-by: Tully Foote <[tullyfoote@intrinsic.ai](mailto:tullyfoote%40intrinsic.ai)>
- Adding NodeInterfaces to Buffer ([#656](https://github.com/ros2/geometry2/issues/656))
- Reformat some code to make uncrustify happier. ([#654](https://github.com/ros2/geometry2/issues/654))
- Enable intra-process ([#649](https://github.com/ros2/geometry2/issues/649)) ([#642](https://github.com/ros2/geometry2/issues/642))
- Avoid unecessary time conversions. ([#635](https://github.com/ros2/geometry2/issues/635))
- Expose TF2 listener CB ([#632](https://github.com/ros2/geometry2/issues/632))
- Fix invalid timer handle exception ([#474](https://github.com/ros2/geometry2/issues/474))
- Fix for [#589](https://github.com/ros2/geometry2/issues/589) - Should be able to transform with default timeout ([#593](https://github.com/ros2/geometry2/issues/593))
- Enable StaticTransformBroadcaster in Intra-process enabled components ([#607](https://github.com/ros2/geometry2/issues/607))
- Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Chris Lalancette, Cliff Wu, Lucas Wendland, Patrick Roncagliolo, Steve Macenski, jmachowinski, vineet131

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/jazzy/tf2_ros_py/CHANGELOG.rst)

- Transform Data Callback Python ([#664](https://github.com/ros2/geometry2/issues/664))
- Make sure to cache transforms in tf2\_ros\_py. ([#634](https://github.com/ros2/geometry2/issues/634))
- Remove ‘efficient copy’ prints ([#625](https://github.com/ros2/geometry2/issues/625))
- Add time jump callback ([#608](https://github.com/ros2/geometry2/issues/608))
- Contributors: Chris Lalancette, Erich L Foster, Lucas Wendland, Matthijs van der Burgh

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/jazzy/tf2_sensor_msgs/CHANGELOG.rst)

- Removed obsolete headers ([#645](https://github.com/ros2/geometry2/issues/645))
- Fix clang build warnings. ([#628](https://github.com/ros2/geometry2/issues/628))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/jazzy/tf2_tools/CHANGELOG.rst)

- [view\_frames] log filenames after it’s been determined ([#674](https://github.com/ros2/geometry2/issues/674)) ([#675](https://github.com/ros2/geometry2/issues/675)) (cherry picked from commit 24643fce510d8cc836fe6e5277a1d3f86a21af04) Co-authored-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Add in tests for tf2\_tools. ([#647](https://github.com/ros2/geometry2/issues/647))
- Contributors: Chris Lalancette, mergify[bot]

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/jazzy/topic_monitor/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- fix readme for topic\_monitor. ([#630](https://github.com/ros2/demos/issues/630))
- Contributors: Michael Jeronimo, Tomoya Fujita

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/jazzy/topic_statistics_demo/CHANGELOG.rst)

- Update maintainer list in package.xml files ([#665](https://github.com/ros2/demos/issues/665))
- Contributors: Michael Jeronimo

<a id="tracetools"></a>

## [tracetools](https://github.com/ros2/ros2_tracing/tree/jazzy/tracetools/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Switch to ament\_generate\_version\_header for tracetools ([#112](https://github.com/ros2/ros2_tracing/issues/112))
- Fixes for newer uncrustify ([#101](https://github.com/ros2/ros2_tracing/issues/101))
- Update tests and docs after new rmw\_publish timestamp field ([#90](https://github.com/ros2/ros2_tracing/issues/90))
- Add timestamp to rmw\_publish tracepoint ([#74](https://github.com/ros2/ros2_tracing/issues/74))
- Add TRACETOOLS\_ prefix to tracepoint-related public macros ([#56](https://github.com/ros2/ros2_tracing/issues/56))
- Disable tracing on Android ([#71](https://github.com/ros2/ros2_tracing/issues/71))
- Add new rclcpp\_subscription\_init tracepoint to support new intra-process comms
- Contributors: Chris Lalancette, Christophe Bedard, Christopher Wecht, Przemysław Dąbrowski

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/jazzy/tracetools_launch/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Use single underscore for private vars in Python ([#92](https://github.com/ros2/ros2_tracing/issues/92))
- Improve tracing configuration error reporting ([#85](https://github.com/ros2/ros2_tracing/issues/85))
- Fix warnings when using mypy 1.8.0. ([#89](https://github.com/ros2/ros2_tracing/issues/89))
- Remove extra single quote in LdPreload debug log ([#79](https://github.com/ros2/ros2_tracing/issues/79))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="tracetools-read"></a>

## [tracetools\_read](https://github.com/ros2/ros2_tracing/tree/jazzy/tracetools_read/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Improve tracetools\_test and simplify test\_tracetools code ([#109](https://github.com/ros2/ros2_tracing/issues/109))
- Allow tracing tests to be run in parallel with other tests ([#95](https://github.com/ros2/ros2_tracing/issues/95))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="tracetools-test"></a>

## [tracetools\_test](https://github.com/ros2/ros2_tracing/tree/jazzy/tracetools_test/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Improve tracetools\_test and simplify test\_tracetools code ([#109](https://github.com/ros2/ros2_tracing/issues/109))
- Improve assertEventOrder failure output ([#106](https://github.com/ros2/ros2_tracing/issues/106))
- Allow tracing tests to be run in parallel with other tests ([#95](https://github.com/ros2/ros2_tracing/issues/95))
- Fix interference between test\_tracetools and ros2lifecycle tests ([#96](https://github.com/ros2/ros2_tracing/issues/96))
- Make tracing test assert messages more descriptive ([#93](https://github.com/ros2/ros2_tracing/issues/93))
- Fix use of mutable default arg in tracetools\_test ([#84](https://github.com/ros2/ros2_tracing/issues/84))
- Switch <depend> to <exec\_depend> in pure Python packages ([#67](https://github.com/ros2/ros2_tracing/issues/67))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://github.com/ros2/ros2_tracing/tree/jazzy/tracetools_trace/CHANGELOG.rst)

- Replace all occurences of index.ros.org ([#114](https://github.com/ros2/ros2_tracing/issues/114))
- Improve tracing configuration error reporting ([#85](https://github.com/ros2/ros2_tracing/issues/85))
- Add a space in between not and parentheses. ([#88](https://github.com/ros2/ros2_tracing/issues/88))
- Switch to custom lttng-ctl Python bindings ([#81](https://github.com/ros2/ros2_tracing/issues/81))
- Create start/pause/resume/stop sub-commands for ‘ros2 trace’ ([#70](https://github.com/ros2/ros2_tracing/issues/70))
- Detect issue with LTTng and Docker and report error when tracing ([#66](https://github.com/ros2/ros2_tracing/issues/66))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="trajectory-msgs"></a>

## [trajectory\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/trajectory_msgs/CHANGELOG.rst)

- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/jazzy/turtlesim/CHANGELOG.rst)

- Add icon for Jazzy. ([#167](https://github.com/ros/ros_tutorials/issues/167)) ([#168](https://github.com/ros/ros_tutorials/issues/168)) (cherry picked from commit 014955e15a6ac3b1649cbf21e11c8547ebd47af7) Co-authored-by: Marco A. Gutierrez <[marcogg@marcogg.com](mailto:marcogg%40marcogg.com)>
- [teleop\_turtle\_key] update usage string to match keys captured by keyboard ([#165](https://github.com/ros/ros_tutorials/issues/165)) ([#166](https://github.com/ros/ros_tutorials/issues/166)) On windows it will stay uppercase but shouldn’t impact users compared to current situation (cherry picked from commit e2853cac87f0c62db6294e5bc351e5b52fcd1ae1) Co-authored-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Shorten the callback definition for uncrustify. ([#163](https://github.com/ros/ros_tutorials/issues/163))
- Use same QoS for all topic pub/subs ([#161](https://github.com/ros/ros_tutorials/issues/161))
- Remove all uses of ament\_target\_dependencies. ([#159](https://github.com/ros/ros_tutorials/issues/159))
- Crop galactic.png and rolling.png to 45x45. ([#158](https://github.com/ros/ros_tutorials/issues/158))
- Remove the unused member variable last\_state\_ ([#156](https://github.com/ros/ros_tutorials/issues/156))
- Added common tests ([#154](https://github.com/ros/ros_tutorials/issues/154))
- Heavy cleanup of the draw\_square tutorial. ([#152](https://github.com/ros/ros_tutorials/issues/152)) \* Heavy cleanup of the draw\_square tutorial. In particular: 1. Make it conform to the current ROS 2 style. 2. Add in copyright information. 3. Refactor the entire code into a class, which tidies it up quite a bit and removes a bunch of globals. 4. Make sure to wait for the reset to complete before trying to move the turtle.
- Remove the range constraints from the holonomic parameter. ([#150](https://github.com/ros/ros_tutorials/issues/150))
- Add icon ([#148](https://github.com/ros/ros_tutorials/issues/148))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jason O’Kane, Yadu, mergify[bot]

<a id="uncrustify-vendor"></a>

## [uncrustify\_vendor](https://github.com/ament/uncrustify_vendor/tree/jazzy/CHANGELOG.rst)

- Update to uncrustify 0.78.1 ([#37](https://github.com/ament/uncrustify_vendor/issues/37)) \* Update to uncrustify 0.78.1 \* Fix the uncrustify version detection logic. And make sure we are at least 0.78.
- Switch to ament\_cmake\_vendor\_package ([#34](https://github.com/ament/uncrustify_vendor/issues/34))
- Contributors: Chris Lalancette, Scott K Logan

<a id="unique-identifier-msgs"></a>

## [unique\_identifier\_msgs](https://github.com/ros2/unique_identifier_msgs/tree/jazzy/CHANGELOG.rst)

- Update to C++17 ([#27](https://github.com/ros2/unique_identifier_msgs/issues/27))
- Contributors: Chris Lalancette

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/jazzy/urdf/CHANGELOG.rst)

- Switch to target\_link\_libraries ([#36](https://github.com/ros2/urdf/issues/36))
- Contributors: Chris Lalancette

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/jazzy/urdf_parser_plugin/CHANGELOG.rst)

- Switch to target\_link\_libraries ([#36](https://github.com/ros2/urdf/issues/36))
- Contributors: Chris Lalancette

<a id="visualization-msgs"></a>

## [visualization\_msgs](https://github.com/ros2/common_interfaces/tree/jazzy/visualization_msgs/CHANGELOG.rst)

- Remove references to index.ros.org. ([#244](https://github.com/ros2/common_interfaces/issues/244))
- Adds ARROW\_STRIP to Marker.msg ([#242](https://github.com/ros2/common_interfaces/issues/242))
- Clarify the license. ([#241](https://github.com/ros2/common_interfaces/issues/241)) In particular, every package in this repository is Apache 2.0 licensed except for sensor\_msgs\_py. So move the CONTRIBUTING.md and LICENSE files down into the individual packages, and make sure that sensor\_msgs\_py has the correct CONTRIBUTING.md file (it already had the correct LICENSE file).
- Contributors: Chris Lalancette, Tom Noble

<a id="yaml-cpp-vendor"></a>

## [yaml\_cpp\_vendor](https://github.com/ros2/yaml_cpp_vendor/tree/jazzy/CHANGELOG.rst)

- Removed warnigns ([#49](https://github.com/ros2/yaml_cpp_vendor/issues/49)) ([#50](https://github.com/ros2/yaml_cpp_vendor/issues/50)) (cherry picked from commit 4b6808fd0f9b0b5e05928c0c8e44fd976a043d33) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Upgrade to yaml-cpp 0.8.0 ([#48](https://github.com/ros2/yaml_cpp_vendor/issues/48)) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Support yaml-cpp >= 0.8.0 ([#46](https://github.com/ros2/yaml_cpp_vendor/issues/46))
- Disable the -Wshadow warning when building under clang. ([#45](https://github.com/ros2/yaml_cpp_vendor/issues/45))
- Switch to ament\_cmake\_vendor\_package ([#43](https://github.com/ros2/yaml_cpp_vendor/issues/43))
- Revamp the extras file to find the correct version. ([#42](https://github.com/ros2/yaml_cpp_vendor/issues/42))
- Contributors: Chris Lalancette, Marco A. Gutierrez, Scott K Logan, Silvio Traversaro, mergify[bot]

<a id="zstd-vendor"></a>

## [zstd\_vendor](https://github.com/ros2/rosbag2/tree/jazzy/zstd_vendor/CHANGELOG.rst)

- Updated zstd to 1.5.5 ([#1617](https://github.com/ros2/rosbag2/issues/1617)) ([#1624](https://github.com/ros2/rosbag2/issues/1624))
- Switch to ament\_cmake\_vendor\_package ([#1400](https://github.com/ros2/rosbag2/issues/1400))
- Contributors: Scott K Logan, mergify[bot]
