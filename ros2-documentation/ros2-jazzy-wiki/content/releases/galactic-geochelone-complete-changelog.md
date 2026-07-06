---
title: "Galactic Geochelone changelog"
docname: "Releases/Galactic-Geochelone-Complete-Changelog"
source: "Releases/Galactic-Geochelone-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="galactic-geochelone-changelog"></a>

# Galactic Geochelone changelog

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
- [ament\_cmake\_gmock](#ament-cmake-gmock)
- [ament\_cmake\_google\_benchmark](#ament-cmake-google-benchmark)
- [ament\_cmake\_gtest](#ament-cmake-gtest)
- [ament\_cmake\_include\_directories](#ament-cmake-include-directories)
- [ament\_cmake\_libraries](#ament-cmake-libraries)
- [ament\_cmake\_lint\_cmake](#ament-cmake-lint-cmake)
- [ament\_cmake\_mypy](#ament-cmake-mypy)
- [ament\_cmake\_nose](#ament-cmake-nose)
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
- [cyclonedds](#cyclonedds)
- [demo\_nodes\_cpp](#demo-nodes-cpp)
- [demo\_nodes\_cpp\_native](#demo-nodes-cpp-native)
- [demo\_nodes\_py](#demo-nodes-py)
- [diagnostic\_msgs](#diagnostic-msgs)
- [domain\_coordinator](#domain-coordinator)
- [dummy\_map\_server](#dummy-map-server)
- [dummy\_robot\_bringup](#dummy-robot-bringup)
- [dummy\_sensors](#dummy-sensors)
- [example\_interfaces](#example-interfaces)
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
- [geometry2](#geometry2)
- [geometry\_msgs](#geometry-msgs)
- [google\_benchmark\_vendor](#google-benchmark-vendor)
- [image\_common](#image-common)
- [image\_tools](#image-tools)
- [image\_transport](#image-transport)
- [interactive\_markers](#interactive-markers)
- [intra\_process\_demo](#intra-process-demo)
- [kdl\_parser](#kdl-parser)
- [laser\_geometry](#laser-geometry)
- [launch](#launch)
- [launch\_ros](#launch-ros)
- [launch\_testing](#launch-testing)
- [launch\_testing\_ament\_cmake](#launch-testing-ament-cmake)
- [launch\_testing\_ros](#launch-testing-ros)
- [launch\_xml](#launch-xml)
- [launch\_yaml](#launch-yaml)
- [libcurl\_vendor](#libcurl-vendor)
- [libstatistics\_collector](#libstatistics-collector)
- [libyaml\_vendor](#libyaml-vendor)
- [lifecycle](#lifecycle)
- [lifecycle\_msgs](#lifecycle-msgs)
- [logging\_demo](#logging-demo)
- [map\_msgs](#map-msgs)
- [message\_filters](#message-filters)
- [mimick\_vendor](#mimick-vendor)
- [nav\_msgs](#nav-msgs)
- [osrf\_pycommon](#osrf-pycommon)
- [osrf\_testing\_tools\_cpp](#osrf-testing-tools-cpp)
- [pendulum\_control](#pendulum-control)
- [pendulum\_msgs](#pendulum-msgs)
- [performance\_test\_fixture](#performance-test-fixture)
- [pluginlib](#pluginlib)
- [pybind11\_vendor](#pybind11-vendor)
- [python\_cmake\_module](#python-cmake-module)
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
- [rcl\_logging\_log4cxx](#rcl-logging-log4cxx)
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
- [rmw\_implementation\_cmake](#rmw-implementation-cmake)
- [robot\_state\_publisher](#robot-state-publisher)
- [ros1\_bridge](#ros1-bridge)
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
- [ros\_testing](#ros-testing)
- [rosbag2](#rosbag2)
- [rosbag2\_compression](#rosbag2-compression)
- [rosbag2\_compression\_zstd](#rosbag2-compression-zstd)
- [rosbag2\_cpp](#rosbag2-cpp)
- [rosbag2\_interfaces](#rosbag2-interfaces)
- [rosbag2\_performance\_benchmarking](#rosbag2-performance-benchmarking)
- [rosbag2\_py](#rosbag2-py)
- [rosbag2\_storage](#rosbag2-storage)
- [rosbag2\_storage\_default\_plugins](#rosbag2-storage-default-plugins)
- [rosbag2\_test\_common](#rosbag2-test-common)
- [rosbag2\_tests](#rosbag2-tests)
- [rosbag2\_transport](#rosbag2-transport)
- [rosgraph\_msgs](#rosgraph-msgs)
- [rosidl\_adapter](#rosidl-adapter)
- [rosidl\_cli](#rosidl-cli)
- [rosidl\_cmake](#rosidl-cmake)
- [rosidl\_default\_generators](#rosidl-default-generators)
- [rosidl\_default\_runtime](#rosidl-default-runtime)
- [rosidl\_generator\_c](#rosidl-generator-c)
- [rosidl\_generator\_cpp](#rosidl-generator-cpp)
- [rosidl\_generator\_dds\_idl](#rosidl-generator-dds-idl)
- [rosidl\_generator\_py](#rosidl-generator-py)
- [rosidl\_parser](#rosidl-parser)
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
- [rqt\_top](#rqt-top)
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
- [test\_quality\_of\_service](#test-quality-of-service)
- [test\_rclcpp](#test-rclcpp)
- [test\_rmw\_implementation](#test-rmw-implementation)
- [test\_security](#test-security)
- [test\_tf2](#test-tf2)
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
- [tracetools\_test](#tracetools-test)
- [tracetools\_trace](#tracetools-trace)
- [trajectory\_msgs](#trajectory-msgs)
- [turtlesim](#turtlesim)
- [unique\_identifier\_msgs](#unique-identifier-msgs)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [visualization\_msgs](#visualization-msgs)
- [yaml\_cpp\_vendor](#yaml-cpp-vendor)
- [zstd\_vendor](#zstd-vendor)

<a id="action-msgs"></a>

## [action\_msgs](https://github.com/ros2/rcl_interfaces/tree/galactic/action_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/galactic/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Update logging macros ([#476](https://github.com/ros2/demos/issues/476))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Update goal response callback signature ([#463](https://github.com/ros2/demos/issues/463))
- Contributors: Audrow Nash, Jacob Perron, Michael Jeronimo

<a id="action-tutorials-interfaces"></a>

## [action\_tutorials\_interfaces](https://github.com/ros2/demos/tree/galactic/action_tutorials/action_tutorials_interfaces/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/galactic/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#502](https://github.com/ros2/demos/issues/502))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Ivan Santiago Paunovic, Michael Jeronimo

<a id="actionlib-msgs"></a>

## [actionlib\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/actionlib_msgs/CHANGELOG.rst)

- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Contributors: Michel Hidalgo

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/galactic/ament_clang_format/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Add clang-format-version option to ament\_clang\_format ([#282](https://github.com/ament/ament_lint/issues/282))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan, Tyler Weaver

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/galactic/ament_clang_tidy/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Add multiprocessing support to ament\_clang\_tidy ([#288](https://github.com/ament/ament_lint/issues/288)) \* add multiprocessing support \* fix stylistic lint issues
- Add –packages-select argument to ament\_clang\_tidy ([#287](https://github.com/ament/ament_lint/issues/287)) Add comment explaining handling quoted list of space separated package names Update documentation for ament\_clang\_tidy
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei, Tyler Weaver

<a id="ament-cmake"></a>

## [ament\_cmake](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_auto/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-clang-format"></a>

## [ament\_cmake\_clang\_format](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_clang_format/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-clang-tidy"></a>

## [ament\_cmake\_clang\_tidy](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_clang_tidy/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- add TIMEOUT argument to ament\_cmake\_clang\_tidy ([#298](https://github.com/ament/ament_lint/issues/298))
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Fix documentation for ament\_cmake\_clang\_tidy ([#285](https://github.com/ament/ament_lint/issues/285))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei, Tyler Weaver

<a id="ament-cmake-copyright"></a>

## [ament\_cmake\_copyright](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_copyright/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- increase default timeout for CMake copyright linter to 120s ([#261](https://github.com/ament/ament_lint/issues/261))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dirk Thomas, Scott K Logan

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_core/CHANGELOG.rst)

- Merge pull request [#287](https://github.com/ament/ament_cmake/issues/287) from ament/mjeronimo/add-condition-support \* Check condition attr in package.xml dependencies The condition attribute was already parsed when reading the XML file. Just needed to check the condition when adding dependencies to the list for a particular key/target. Fixes [#266](https://github.com/ament/ament_cmake/issues/266) \* Address Dirk’s code review feedback
- Address Dirk’s code review feedback
- Check condition attr in package.xml dependencies The condition attribute was already parsed when reading the XML file. Just needed to check the condition when adding dependencies to the list for a particular key/target. Fixes [#266](https://github.com/ament/ament_cmake/issues/266)
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michael Jeronimo, Michel Hidalgo

<a id="ament-cmake-cppcheck"></a>

## [ament\_cmake\_cppcheck](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_cppcheck/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Increase the ament\_cppcheck timeout to 5 minutes. ([#271](https://github.com/ament/ament_lint/issues/271)) This will avoid timeouts on some slower platforms that we’ve started to see.
- parse LANGUAGE argument case insensitive ([#255](https://github.com/ament/ament_lint/issues/255))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Karsten Knese, Scott K Logan

<a id="ament-cmake-cpplint"></a>

## [ament\_cmake\_cpplint](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_cpplint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-export-definitions"></a>

## [ament\_cmake\_export\_definitions](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_definitions/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-export-dependencies"></a>

## [ament\_cmake\_export\_dependencies](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_dependencies/CHANGELOG.rst)

- fix cmake list(TRANSFORM ) is only available from version 3.12, ([#296](https://github.com/ament/ament_cmake/issues/296)) convert to string instead
- fix imported targets with multiple configuration ([#290](https://github.com/ament/ament_cmake/issues/290)) \* fix imported targets with multiple configuration \* taking into account DEBUG\_CONFIGURATIONS global variable
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo, siposcsaba89

<a id="ament-cmake-export-include-directories"></a>

## [ament\_cmake\_export\_include\_directories](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_include_directories/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-export-interfaces"></a>

## [ament\_cmake\_export\_interfaces](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_interfaces/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-export-libraries"></a>

## [ament\_cmake\_export\_libraries](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_libraries/CHANGELOG.rst)

- Fix variable name in ament\_export\_libraries.cmake ([#314](https://github.com/ament/ament_cmake/issues/314))
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Alejandro Hernández Cordero, Michel Hidalgo

<a id="ament-cmake-export-link-flags"></a>

## [ament\_cmake\_export\_link\_flags](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_link_flags/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-export-targets"></a>

## [ament\_cmake\_export\_targets](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_export_targets/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-flake8"></a>

## [ament\_cmake\_flake8](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_flake8/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang

<a id="ament-cmake-gmock"></a>

## [ament\_cmake\_gmock](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_gmock/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-google-benchmark"></a>

## [ament\_cmake\_google\_benchmark](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_google_benchmark/CHANGELOG.rst)

- Serialize benchmarks within CTest by default ([#308](https://github.com/ament/ament_cmake/issues/308))
- Handle runtime failures in Google Benchmark ([#294](https://github.com/ament/ament_cmake/issues/294)) This change will handle runtime failures in Google Benchmark by propagating error information from Google Benchmark to both CTest and the Jenkins benchmark plugin.
- Use consistent string format and resolve flake8 ([#295](https://github.com/ament/ament_cmake/issues/295)) Follow-up to a5fb3112b5c46c42b1824c96af4171d469eb13bf
- Make ament\_cmake\_test a dep of ament\_cmake\_google\_benchmark ([#293](https://github.com/ament/ament_cmake/issues/293))
- Catch JSONDecodeError and printout some debug info ([#291](https://github.com/ament/ament_cmake/issues/291))
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Make AMENT\_RUN\_PERFORMANCE\_TESTS a CMake option ([#280](https://github.com/ament/ament_cmake/issues/280))
- Skip performance tests using a CMake variable ([#278](https://github.com/ament/ament_cmake/issues/278)) These tests can be fairly heavy, so we don’t want to run them by default. It would be better if there was a way to skip the tests by default in such a way that they could be specifically un-skipped at runtime, but I can’t find a mechanism in CMake or CTest that would allow us to achieve that behavior without leveraging environment variables.
- Handle Google Benchmark ‘aggregate’ results ([#276](https://github.com/ament/ament_cmake/issues/276)) Previously, I assumed all results generated by Google Benchmark were of ‘iteration’ type. Now that I have more experience with Google Benchmark, I’ve started generating aggregate results, which contain some different properties. This change adds support for aggregate results and should make it easy to add any other result schemas we encounter in the future. For forward-compatibility, unsupported types will generate a warning message but will not fail the test. This makes the conversion tolerant to Google Benchmark adding new measures for existing mechanisms.
- Initial Google Benchmark results conversion ([#275](https://github.com/ament/ament_cmake/issues/275))
- Handle missing results file for Google Benchmark ([#265](https://github.com/ament/ament_cmake/issues/265))
- Initial ament\_cmake\_google\_benchmark package ([#261](https://github.com/ament/ament_cmake/issues/261))
- Contributors: Michel Hidalgo, Scott K Logan, brawner

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_gtest/CHANGELOG.rst)

- Disable gtest warning when building in Release ([#298](https://github.com/ament/ament_cmake/issues/298)) <https://github.com/google/googletest/issues/1303>
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- [ament\_cmake\_gtest] ensure gtest to consume the correct headers. ([#267](https://github.com/ament/ament_cmake/issues/267)) \* ensure gtest to consume the correct headers. \* add another patch.
- Contributors: Michel Hidalgo, Sean Yen, Victor Lopez

<a id="ament-cmake-include-directories"></a>

## [ament\_cmake\_include\_directories](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_include_directories/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-libraries"></a>

## [ament\_cmake\_libraries](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_libraries/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-lint-cmake"></a>

## [ament\_cmake\_lint\_cmake](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_lint_cmake/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- ament\_lint\_cmake: default linelength in argumentparser for consistency ([#306](https://github.com/ament/ament_lint/issues/306))
- 0.10.3
- Fix ament\_lint\_cmake line length expression ([#236](https://github.com/ament/ament_lint/issues/236)) This regular expression is using the re.VERBOSE flag, meaning that characters after an un-escaped ‘#’ character are interpreted as a comment and are not part of the expression. Also set the default maximum line length to 140 columns.
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Make CMake linter line length configurable ([#235](https://github.com/ament/ament_lint/issues/235)) Co-authored-by: Miaofei <[miaofei@amazon.com](mailto:miaofei%40amazon.com)>
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Emerson Knapp, Scott K Logan

<a id="ament-cmake-mypy"></a>

## [ament\_cmake\_mypy](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_mypy/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang

<a id="ament-cmake-nose"></a>

## [ament\_cmake\_nose](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_nose/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-pclint"></a>

## [ament\_cmake\_pclint](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pclint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-pep257"></a>

## [ament\_cmake\_pep257](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pep257/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-pycodestyle"></a>

## [ament\_cmake\_pycodestyle](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pycodestyle/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-pyflakes"></a>

## [ament\_cmake\_pyflakes](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pyflakes/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-cmake-pytest"></a>

## [ament\_cmake\_pytest](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_pytest/CHANGELOG.rst)

- Fix ament\_get\_pytest\_cov\_version for newer versions of pytest ([#315](https://github.com/ament/ament_cmake/issues/315))
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Christophe Bedard, Michel Hidalgo

<a id="ament-cmake-python"></a>

## [ament\_cmake\_python](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_python/CHANGELOG.rst)

- Symlink setup.cfg and sources before building Python egg-info ([#327](https://github.com/ament/ament_cmake/issues/327))
- Simplify ament\_python\_install\_package() macro. ([#326](https://github.com/ament/ament_cmake/issues/326)) Do not delegate to setuptools, install egg-info manually.
- Escape $ENV{DESTDIR} everywhere in ament\_python\_install\_package() ([#324](https://github.com/ament/ament_cmake/issues/324)) Follow up after f80071e2216e766f7bf1b0792493a5f6523e9226
- Use DESTDIR on ament\_python\_install\_package() ([#323](https://github.com/ament/ament_cmake/issues/323)) \* Use DESTDIR on ament\_python\_install\_package()
- Make ament\_python\_install\_package() install a flat Python egg ([#316](https://github.com/ament/ament_cmake/issues/316))
- [ament\_cmake\_python] ament\_cmake\_python\_get\_python\_install\_dir public ([#300](https://github.com/ament/ament_cmake/issues/300)) \* [ament\_cmake\_python] make the ament\_cmake\_python\_get\_python\_install\_dir a public interface.
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo, Naveau

<a id="ament-cmake-ros"></a>

## [ament\_cmake\_ros](https://github.com/ros2/ament_cmake_ros/tree/galactic/ament_cmake_ros/CHANGELOG.rst)

- Update package maintainers. ([#11](https://github.com/ros2/ament_cmake_ros/issues/11))
- Contributors: Michel Hidalgo

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_target_dependencies/CHANGELOG.rst)

- Force SYSTEM keyword in ament\_target\_dependencies() at the start. ([#303](https://github.com/ament/ament_cmake/issues/303))
- Add SYSTEM keyword option to ament\_target\_dependencies ([#297](https://github.com/ament/ament_cmake/issues/297)) \* Add SYSTEM keyword option to ament\_target\_dependencies \* Add documentation of SYSTEM keyword for ament\_target\_dependencies
- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- ordered interface include dirs and use privately to ensure workspace order ([#260](https://github.com/ament/ament_cmake/issues/260))
- Contributors: Andre Nguyen, Dirk Thomas, Michel Hidalgo

<a id="ament-cmake-test"></a>

## [ament\_cmake\_test](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_test/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Fix skipped test reporting in CTest ([#279](https://github.com/ament/ament_cmake/issues/279)) This is a follow-up to c67cdf2. When the SKIP\_RETURN\_CODE gets set to 0, the value is interpreted as ‘false’, and the test property is never actually added.
- limit test time to three decimals ([#271](https://github.com/ament/ament_cmake/issues/271))
- Add actual test time to xUnit result files ([#270](https://github.com/ament/ament_cmake/issues/270)) \* Add actual test time to xUnit result files Fixes [#269](https://github.com/ament/ament_cmake/issues/269) \* Report test\_time even with skipped test \* Set time attribute for testcase element
- Add SKIP\_RETURN\_CODE argument to ament\_add\_test ([#264](https://github.com/ament/ament_cmake/issues/264)) This makes the `run_test.py` wrapper aware of the `SKIP_RETURN_CODE` property on CTest tests. In the existing implementation, the wrapper detects that no result file was generated and overrides the special return code coming from the test, making the the CTest feature fail completely. This change makes the wrapper script aware of the special return code, and when detected, will write a ‘skipped’ result file instead of a ‘failed’ result file, and pass along the special return code as-is. Now the gtest result and the ctest results both show the test as ‘skipped’ when the special return flag is used. Note that none of this behavior is enabled by default, which is important because we wouldn’t want a test to fail and return a code which we’ve decided is the special ‘skip’ return code. Only tests which are aware of this feature should use it.
- Contributors: Dirk Thomas, Michel Hidalgo, Ruffin, Scott K Logan

<a id="ament-cmake-uncrustify"></a>

## [ament\_cmake\_uncrustify](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_uncrustify/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- parse LANGUAGE argument case insensitive ([#255](https://github.com/ament/ament_lint/issues/255))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Karsten Knese, Scott K Logan

<a id="ament-cmake-version"></a>

## [ament\_cmake\_version](https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_version/CHANGELOG.rst)

- Update package maintainers. ([#286](https://github.com/ament/ament_cmake/issues/286))
- Contributors: Michel Hidalgo

<a id="ament-cmake-xmllint"></a>

## [ament\_cmake\_xmllint](https://github.com/ament/ament_lint/tree/galactic/ament_cmake_xmllint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/galactic/ament_copyright/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- Use non-blind except for open() ([#307](https://github.com/ament/ament_lint/issues/307))
- Add optional file header style ([#304](https://github.com/ament/ament_lint/issues/304)) \* Add optional file header style \* Fix test on ament\_copyright
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- add mit-0 as a valid license to ament\_copyright ([#284](https://github.com/ament/ament_lint/issues/284))
- Support Python 3.8-provided importlib.metadata ([#290](https://github.com/ament/ament_lint/issues/290)) The importlib\_metadata package is a backport of the importlib.metadata module from Python 3.8. Fedora (and possibly others) no longer package importlib\_metadata because they ship Python versions which have the functionality built-in.
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- added bsd 2 clause simplified license to ament\_copyright ([#267](https://github.com/ament/ament_lint/issues/267)) \* added bsd 2 clause simplified license to ament\_copyright
- Remove use of pkg\_resources from ament\_lint. ([#260](https://github.com/ament/ament_lint/issues/260)) Replace it with the use of the more modern importlib\_metadata library. There are a couple of reasons to do this: 1. pkg\_resources is quite slow to import; on my machine, just firing up the python interpreter takes ~35ms, while firing up the python interpreter and importing pkg\_resources takes ~175ms. Firing up the python interpreter and importing importlib\_metadata takes ~70ms. Removing 100ms per invocation of the command-line both makes it speedier for users, and will speed up our tests (which call out to the command-line quite a lot). 2. pkg\_resources is somewhat deprecated and being replaced by importlib. <https://importlib-metadata.readthedocs.io/en/latest/using.html> describes some of it Note: By itself, this change is not enough to completely remove our dependence on pkg\_resources. We’ll also have to do something about the console\_scripts that setup.py generates. That will be a separate effort.
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Alfi Maulana, Audrow Nash, Chris Lalancette, Christophe Bedard, Claire Wang, Evan Flynn, M. Mei, Scott K Logan

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/galactic/ament_cppcheck/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Fix file exclusion behavior in ament\_cppcheck and ament\_cpplint ([#299](https://github.com/ament/ament_lint/issues/299)) \* fix exclude behavior in ament\_cppcheck and ament\_cpplint \* fix flake8 errors \* add missing realpath() conversion
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Suppress unknownMacro ([#268](https://github.com/ament/ament_lint/issues/268)) cppcheck creates an unknownMacro error when it cannot resolve a macro. Since we don’t pass in all dependent headers, we don’t expect all macros to be discoverable by cppcheck.
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dan Rose, M. Mei, Scott K Logan

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/galactic/ament_cpplint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Fix file exclusion behavior in ament\_cppcheck and ament\_cpplint ([#299](https://github.com/ament/ament_lint/issues/299)) \* fix exclude behavior in ament\_cppcheck and ament\_cpplint \* fix flake8 errors \* add missing realpath() conversion
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, M. Mei, Scott K Logan

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/galactic/ament_flake8/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang

<a id="ament-index-cpp"></a>

## [ament\_index\_cpp](https://github.com/ament/ament_index/tree/galactic/ament_index_cpp/CHANGELOG.rst)

- Remove Claire as the maintainer. ([#71](https://github.com/ament/ament_index/issues/71))
- Change links from index.ros.org -> docs.ros.org ([#70](https://github.com/ament/ament_index/issues/70))
- Add Audrow as a maintainer ([#68](https://github.com/ament/ament_index/issues/68))
- update maintainers ([#67](https://github.com/ament/ament_index/issues/67))
- Update QD to Quality Level 1 ([#66](https://github.com/ament/ament_index/issues/66))
- add rational why ament\_index pkgs don’t have explicit performance tests ([#65](https://github.com/ament/ament_index/issues/65))
- Fixed Doxygen warnings ([#63](https://github.com/ament/ament_index/issues/63))
- Remove the Quality Level from the README.md. ([#62](https://github.com/ament/ament_index/issues/62))
- Update QD ament\_index\_cpp to QL 2 ([#59](https://github.com/ament/ament_index/issues/59))
- Add Security Vulnerability Policy pointing to REP-2006. ([#57](https://github.com/ament/ament_index/issues/57))
- [Quality Declaration] Update Version Stability to stable version ([#58](https://github.com/ament/ament_index/issues/58))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Claire Wang, Dirk Thomas, brawner

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/galactic/ament_index_python/CHANGELOG.rst)

- Remove Claire as the maintainer. ([#71](https://github.com/ament/ament_index/issues/71))
- Change links from index.ros.org -> docs.ros.org ([#70](https://github.com/ament/ament_index/issues/70))
- Add Audrow as a maintainer ([#68](https://github.com/ament/ament_index/issues/68))
- update maintainers ([#67](https://github.com/ament/ament_index/issues/67))
- add rational why ament\_index pkgs don’t have explicit performance tests ([#65](https://github.com/ament/ament_index/issues/65))
- Remove the Quality Level from the README.md. ([#62](https://github.com/ament/ament_index/issues/62))
- Fix document link ([#61](https://github.com/ament/ament_index/issues/61))
- [Quality Declaration] Update Version Stability to stable version ([#58](https://github.com/ament/ament_index/issues/58))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Claire Wang, Dirk Thomas, Matthijs van der Burgh

<a id="ament-lint"></a>

## [ament\_lint](https://github.com/ament/ament_lint/tree/galactic/ament_lint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/galactic/ament_lint_auto/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Use correct lint package dependencies ([#278](https://github.com/ament/ament_lint/issues/278))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Esteve Fernandez, Scott K Logan

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/galactic/ament_lint_cmake/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- ament\_lint\_cmake: default linelength in argumentparser for consistency ([#306](https://github.com/ament/ament_lint/issues/306))
- 0.10.3
- Fix ament\_lint\_cmake line length expression ([#236](https://github.com/ament/ament_lint/issues/236)) This regular expression is using the re.VERBOSE flag, meaning that characters after an un-escaped ‘#’ character are interpreted as a comment and are not part of the expression. Also set the default maximum line length to 140 columns.
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Make CMake linter line length configurable ([#235](https://github.com/ament/ament_lint/issues/235)) Co-authored-by: Miaofei <[miaofei@amazon.com](mailto:miaofei%40amazon.com)>
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Emerson Knapp, Scott K Logan

<a id="ament-lint-common"></a>

## [ament\_lint\_common](https://github.com/ament/ament_lint/tree/galactic/ament_lint_common/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/galactic/ament_mypy/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/galactic/CHANGELOG.rst)

- Revert “Generate Setuptools Dict Helper Method ([#126](https://github.com/ament/ament_package/issues/126))” ([#131](https://github.com/ament/ament_package/issues/131))
- Generate Setuptools Dict Helper Method ([#126](https://github.com/ament/ament_package/issues/126))
- Add Audrow as a maintainer ([#127](https://github.com/ament/ament_package/issues/127))
- Support Python 3.8-provided importlib.metadata ([#124](https://github.com/ament/ament_package/issues/124))
- Declare missing dependency on python3-importlib-resources ([#123](https://github.com/ament/ament_package/issues/123))
- make AMENT\_TRACE\_SETUP\_FILES output sourceable ([#120](https://github.com/ament/ament_package/issues/120))
- update maintainers
- Switch ament\_package to using importlib. ([#118](https://github.com/ament/ament_package/issues/118))
- Add pytest.ini so local tests don’t display warning ([#117](https://github.com/ament/ament_package/issues/117))
- add configure-time flag to skip parent\_prefix\_path ([#115](https://github.com/ament/ament_package/issues/115))
- Contributors: Audrow Nash, Chris Lalancette, David V. Lu!!, Dirk Thomas, Mabel Zhang, Scott K Logan

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/galactic/ament_pclint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Add pytest marks to ament\_pclint tests. ([#202](https://github.com/ament/ament_lint/issues/202)) \* Add pytest marks to ament\_pclint tests. \* fix failed tests Co-authored-by: Miaofei <[miaofei@amazon.com](mailto:miaofei%40amazon.com)>
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan, Steven! Ragnarök

<a id="ament-pep257"></a>

## [ament\_pep257](https://github.com/ament/ament_lint/tree/galactic/ament_pep257/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- remove use of “extend” action in argparse ([#262](https://github.com/ament/ament_lint/issues/262))
- Expand ignores to pep257 definition. ([#241](https://github.com/ament/ament_lint/issues/241)) \* Expand ignores to pep257 definition. (ament [#240](https://github.com/ament/ament_lint/issues/240)) \* add ‘–allow-undocumented’ flag to enforce pep257 \* restore existing default error codes to check \* fix no-ignores logic \* expose options from pydocstyle \* allow user to explicitly set convention to “ament” \* fix typo in populating argv for pydocstyle \* reformat ament convention list \* Add help info for ament convention
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- remove match args to allow pydocstyle defaults ([#243](https://github.com/ament/ament_lint/issues/243))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan, Ted Kern

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/galactic/ament_pycodestyle/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/galactic/ament_pyflakes/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/galactic/ament_uncrustify/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Allow ‘C++’ as language, but convert it to ‘CPP’ ([#302](https://github.com/ament/ament_lint/issues/302))
- Allow correct languages on uncrustify ([#272](https://github.com/ament/ament_lint/issues/272)) \* Allow correct languages on uncrustify. \* Update dictionary.
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Miguel Company, Scott K Logan

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/galactic/ament_xmllint/CHANGELOG.rst)

- Remove Claire as a maintainer. ([#312](https://github.com/ament/ament_lint/issues/312)) \* Remove Claire as a maintainer. \* Remove dead email addresses. \* Remove more dead email addresses. \* Switch setup.py maintainer to Audrow.
- 0.10.3
- Add Audrow as a maintainer ([#294](https://github.com/ament/ament_lint/issues/294))
- Drop trailing tab from package manifests ([#291](https://github.com/ament/ament_lint/issues/291)) Follow-up to 8bf194aa1ac282db5483dd0d3fefff8f325b0db8
- Update maintainer ([#274](https://github.com/ament/ament_lint/issues/274)) \* update maintainer \* add authors
- Add pytest.ini so local tests don’t display warning. ([#259](https://github.com/ament/ament_lint/issues/259))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Scott K Logan

<a id="builtin-interfaces"></a>

## [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/galactic/builtin_interfaces/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Document that Time and Duration are explictly ROS Time ([#103](https://github.com/ros2/rcl_interfaces/issues/103))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, Tully Foote, brawner, shonigmann

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/ros2/camera_calibration_parsers/CHANGELOG.rst)

- Fix formatting and include paths for linters ([#157](https://github.com/ros-perception/image_common/issues/157))
- ROS2 Using the filesystem helper in rcpputils ([#133](https://github.com/ros-perception/image_common/issues/133))
- [Windows][ros2] Avoid build break for Visual Studio 2019 v16.3 ([#135](https://github.com/ros-perception/image_common/issues/135))
- Camera Calibration Parsers ROS2 Port ([#105](https://github.com/ros-perception/image_common/issues/105))
- Image Transport ROS2 port ([#84](https://github.com/ros-perception/image_common/issues/84))
- Use Boost\_LIBRARIES instead of Boost\_PYTHON\_LIBRARY This was causing issues when building with python3 since then `Boost_PYTHON_LIBRARY` is not set, instead cmake sets `Boost_PYTHON3_LIBRARY`. So instead of adding each library separately, using `Boost_LIBRARIES` seems to be better. For reference, from the cmake docs: `` ` Boost_LIBRARIES        - Boost component libraries to be linked Boost\_<C>_LIBRARY      - Libraries to link for component <C> ` ``
- Properly detect Boost Python 2 or 3 This fixes [#59](https://github.com/ros-perception/image_common/issues/59)
- 1.11.11
- update changelogs
- Add install target for python wrapper library
- Only link against needed Boost libraries 9829b02 introduced a python dependency into find\_package(Boost..) which results in ${Boost\_LIBRARIES} containing boost\_python and such a dependency to libpython at link time. With this patch we only link against the needed libraries.
- Add python wrapper for readCalibration. Reads .ini or .yaml calibration file and returns camera name and sensor\_msgs/cameraInfo.
- Use $catkin\_EXPORTED\_TARGETS
- Remove no-longer-neccessary flags to allow OS X to use 0.3 and 0.5 of yaml-cpp.
- remove buggy CMake message
- fix [#39](https://github.com/ros-perception/image_common/issues/39)
- make sure test does not fail
- [camera\_calibration\_parsers] Better error message when calib file can’t be written
- add rosbash as a test dependency
- add a test dependency now that we have tests
- parse distortion of arbitraty length in INI This fixes [#33](https://github.com/ros-perception/image_common/issues/33)
- add a test to parse INI calibration files with 5 or 8 D param
- Add yaml-cpp case for building on Android
- Fix catkin\_make failure (due to yaml-cpp deps) for mac os
- fix bad yaml-cpp usage in certain conditions fixes [#24](https://github.com/ros-perception/image_common/issues/24)
- add a dependency on pkg-config to have it work on Indigo
- fix YAML CPP 0.5.x compatibility
- Contributors: Andreas Klintberg, Gary Servin, Helen Oleynikova, Isaac IY Saito, Jochen Sprickerhof, Kartik Mohta, Markus Roth, Martin Idel, Michael Carroll, Sean Yen, Vincent Rabaud, Yifei Zhang

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/ros2/camera_info_manager/CHANGELOG.rst)

- Fix formatting and include paths for linters ([#157](https://github.com/ros-perception/image_common/issues/157))
- Enable Windows build. ([#159](https://github.com/ros-perception/image_common/issues/159))
- Fix abort criteria for setCameraInfoService callback ([#132](https://github.com/ros-perception/image_common/issues/132))
- camera\_info\_manager ROS2 port ([#94](https://github.com/ros-perception/image_common/issues/94))
- Image Transport ROS2 port ([#84](https://github.com/ros-perception/image_common/issues/84))
- Fix the find\_package(catkin) redundancy
- Add a dependency between the test and the test executable
- Add camera\_calibration\_parsers dependency to camera\_info\_manager
- 1.11.11
- update changelogs
- Return empty CameraInfo when !ros::ok()
- Return empty CameraInfo when !ros::ok()
- fix compilation on Fedora, fixes [#42](https://github.com/ros-perception/image_common/issues/42)
- simplify target\_link\_libraries That should fix [#35](https://github.com/ros-perception/image_common/issues/35)
- Add public member function to manually set camera info ([#19](https://github.com/ros-perception/image_common/issues/19))
- make rostest in CMakeLists optional ([ros/rosdistro#3010](https://github.com/ros/rosdistro/issues/3010))
- check for CATKIN\_ENABLE\_TESTING
- add Jack as maintainer
- add gtest libraries linkage
- fix the rostest dependency
- fix catkin gtest and rostest problem
- fix unit test dependencies
- Removed duplicated test dependancy Test dependencies should never duplicate build or run dependencies.
- fix the urls
- Updated package.xml file(s) to handle new catkin buildtool\_depend requirement
- remove the brief attribute
- fix bad folder/libraries
- add missing rostest dependency
- fix bad dependency
- fix dependencies
- add catkin as a dependency
- comply to the catkin API
- add missing linkage
- install the include directories
- fix build issues
- make the libraries public
- API documentation review update
- suppress misleading camera\_info\_manager error messages [#5273]
- remove deprecated global CameraInfoManager symbol for Fuerte (#4971)
- Revert to using boost::mutex, not boost::recursive\_mutex.
- Hack saveCalibrationFile() to stat() the containing directory and attempt to create it if necessary. Test for this case.
- Reload camera info when camera name changes.
- Implement most new Electric API changes, with test cases.
- Add ${ROS\_HOME} expansion, with unit test cases. Do not use “$$” for a single ‘$’, look for “${” instead.
- Use case-insensitive comparisons for parsing URL tags (#4761). Add unit test cases to cover this. Add unit test case for camera name containing video mode.
- add test for resolving an empty URL
- Deprecate use of global CameraInfoManager symbol in E-turtle (#4786). Modify unit tests accordingly.
- provide camera\_info\_manager namespace, fixes #4760
- Add support for “package://” URLs.
- Fixed tests to work with new CameraInfo.
- Moved image\_common from camera\_drivers.
- Contributors: Aaron Blasdel, Enrique Fernandez, Jack O’Quin, Jonathan Bohren, Joseph Schornak, Lukas Bulwahn, Martin Idel, Max Schettler, Michael Carroll, Sean Yen, Vincent Rabaud, blaise, mihelich, mirzashah

<a id="class-loader"></a>

## [class\_loader](https://github.com/ros/class_loader/tree/galactic/CHANGELOG.rst)

- Remove travis. ([#182](https://github.com/ros/class_loader/issues/182))
- Change index.ros.org -> docs.ros.org. ([#181](https://github.com/ros/class_loader/issues/181))
- Fix ternary null check found by clang static analysis ([#176](https://github.com/ros/class_loader/issues/176))
- Update QD to QL 1 ([#177](https://github.com/ros/class_loader/issues/177))
- Updated console\_bridge QL in QD
- Update package maintainers. ([#169](https://github.com/ros/class_loader/issues/169))
- enable building a static library ([#163](https://github.com/ros/class_loader/issues/163))
- Update Quality Declaration to reflect QL 2 ([#160](https://github.com/ros/class_loader/issues/160)).
- Increase coverage with a graveyard behavior test and unmanaged instance test ([#159](https://github.com/ros/class_loader/issues/159))
- Add Security Vulnerability Policy pointing to REP-2006. ([#157](https://github.com/ros/class_loader/issues/157))
- Clean up and improve documentation ([#156](https://github.com/ros/class_loader/issues/156))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, Michel Hidalgo, Stephen Brawner, ahcorde, brawner

<a id="common-interfaces"></a>

## [common\_interfaces](https://github.com/ros2/common_interfaces/tree/galactic/common_interfaces/CHANGELOG.rst)

- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Contributors: Michel Hidalgo

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/galactic/composition/CHANGELOG.rst)

- Fix leak([#480](https://github.com/ros2/demos/issues/480)) ([#481](https://github.com/ros2/demos/issues/481))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo, y-okumura-isp

<a id="composition-interfaces"></a>

## [composition\_interfaces](https://github.com/ros2/rcl_interfaces/tree/galactic/composition_interfaces/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="cyclonedds"></a>

## [cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds/tree/iceoryx/CHANGELOG.rst)

- DATA\_AVAILABLE was not always triggered when by a dispose and sometimes triggered in the absence of an observable state change (arrival of a dispose for an already-disposed instance where the dispose had not yet been read);
- Restores functionality of the “raw ethernet” mode as well as IPv6 with link-local addresses, both accidentally broken in 0.6.0;
- Fixes a crash in processing endpoint discovery data containing unrecognised locator kinds;
- Fixes type conversion for local historical data (e.g., mixed use of ROS 2 C/C++ type supports in combination with transient-local endpoints within a single process);
- Fixes a use-after-free of “lease” objects with manual-by-topic writers;
- Mark instance as “alive” in the reader history and generate an invalid sample to notify the application even if the sample itself is dropped because the same or a later one is present already (e.g., on reconnecting to a transient-local writer);
- Fix a crash when doing an instance lookup on a built-in topic using the key value;
- No longer auto-dispose instances as soon as some registered writer disappears, instead do it only when all of them have unregistered it;
- Fix performance of read\_instance and take\_instance by performing a proper instance lookup.

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/galactic/demo_nodes_cpp/CHANGELOG.rst)

- Fix small print issue in allocator tutorial. ([#509](https://github.com/ros2/demos/issues/509)) ([#512](https://github.com/ros2/demos/issues/512))
- Small fixes for even\_parameters\_node. ([#500](https://github.com/ros2/demos/issues/500))
- change ParameterEventHandler to take events as const ref instead of shared pointer ([#494](https://github.com/ros2/demos/issues/494))
- Fix integer type in RCLCPP\_\* macro printf. ([#492](https://github.com/ros2/demos/issues/492))
- Add a demo for the new ParameterEventHandler class ([#486](https://github.com/ros2/demos/issues/486))
- Filter qos overrides in paramter events demos ([#491](https://github.com/ros2/demos/issues/491))
- Update code now that parameter types are static by default ([#487](https://github.com/ros2/demos/issues/487))
- Update logging macros ([#476](https://github.com/ros2/demos/issues/476))
- Make sure to wait for the service before declaring events. ([#473](https://github.com/ros2/demos/issues/473))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Michael Jeronimo, William Woodall

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/galactic/demo_nodes_cpp_native/CHANGELOG.rst)

- Update demo\_nodes\_cpp\_native to new Fast DDS API ([#493](https://github.com/ros2/demos/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo, Miguel Company

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/galactic/demo_nodes_py/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#502](https://github.com/ros2/demos/issues/502))
- Update deprecated qos policy value names ([#468](https://github.com/ros2/demos/issues/468))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Ivan Santiago Paunovic, Michael Jeronimo

<a id="diagnostic-msgs"></a>

## [diagnostic\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/diagnostic_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="domain-coordinator"></a>

## [domain\_coordinator](https://github.com/ros2/ament_cmake_ros/tree/galactic/domain_coordinator/CHANGELOG.rst)

- Update package maintainers. ([#11](https://github.com/ros2/ament_cmake_ros/issues/11))
- Add pytest.ini to suppress warning output locally. ([#8](https://github.com/ros2/ament_cmake_ros/issues/8))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/galactic/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/galactic/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/galactic/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="example-interfaces"></a>

## [example\_interfaces](https://github.com/ros2/example_interfaces/tree/galactic/CHANGELOG.rst)

- Change links from index.ros.org -> docs.ros.org. ([#13](https://github.com/ros2/example_interfaces/issues/13))
- Update maintainer. ([#12](https://github.com/ros2/example_interfaces/issues/12))
- Contributors: Chris Lalancette, Jacob Perron

<a id="examples-rclcpp-cbg-executor"></a>

## [examples\_rclcpp\_cbg\_executor](https://github.com/ros2/examples/tree/galactic/rclcpp/executors/cbg_executor/CHANGELOG.rst)

- Fix clang warnings about type mismatches. ([#309](https://github.com/ros2/examples/issues/309))
- Support for cbg\_executor package on QNX ([#305](https://github.com/ros2/examples/issues/305))
- Demo for callback-group-level executor concept. ([#302](https://github.com/ros2/examples/issues/302))
- Contributors: Chris Lalancette, Ralph Lange, joshua-qnx

<a id="examples-rclcpp-minimal-action-client"></a>

## [examples\_rclcpp\_minimal\_action\_client](https://github.com/ros2/examples/tree/galactic/rclcpp/actions/minimal_action_client/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Update goal response callback signature ([#291](https://github.com/ros2/examples/issues/291))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="examples-rclcpp-minimal-action-server"></a>

## [examples\_rclcpp\_minimal\_action\_server](https://github.com/ros2/examples/tree/galactic/rclcpp/actions/minimal_action_server/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane Loretz

<a id="examples-rclcpp-minimal-client"></a>

## [examples\_rclcpp\_minimal\_client](https://github.com/ros2/examples/tree/galactic/rclcpp/services/minimal_client/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane Loretz

<a id="examples-rclcpp-minimal-composition"></a>

## [examples\_rclcpp\_minimal\_composition](https://github.com/ros2/examples/tree/galactic/rclcpp/composition/minimal_composition/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="examples-rclcpp-minimal-publisher"></a>

## [examples\_rclcpp\_minimal\_publisher](https://github.com/ros2/examples/tree/galactic/rclcpp/topics/minimal_publisher/CHANGELOG.rst)

- Unique network flows ([#296](https://github.com/ros2/examples/issues/296))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Chris Lalancette, Shane Loretz

<a id="examples-rclcpp-minimal-service"></a>

## [examples\_rclcpp\_minimal\_service](https://github.com/ros2/examples/tree/galactic/rclcpp/services/minimal_service/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane Loretz

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/galactic/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- Unique network flows ([#296](https://github.com/ros2/examples/issues/296))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Make sure to include what you use in all examples. ([#284](https://github.com/ros2/examples/issues/284))
- Remove a TODO in the not\_composable demo. ([#285](https://github.com/ros2/examples/issues/285))
- Add Topic Statistics Example ([#281](https://github.com/ros2/examples/issues/281))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Chris Lalancette, Devin Bonnie, Shane Loretz

<a id="examples-rclcpp-minimal-timer"></a>

## [examples\_rclcpp\_minimal\_timer](https://github.com/ros2/examples/tree/galactic/rclcpp/timers/minimal_timer/CHANGELOG.rst)

- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="examples-rclcpp-multithreaded-executor"></a>

## [examples\_rclcpp\_multithreaded\_executor](https://github.com/ros2/examples/tree/galactic/rclcpp/executors/multithreaded_executor/CHANGELOG.rst)

- Use `char *` in logging macros ([#295](https://github.com/ros2/examples/issues/295))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Added common linters ([#265](https://github.com/ros2/examples/issues/265))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Shane Loretz

<a id="examples-rclpy-executors"></a>

## [examples\_rclpy\_executors](https://github.com/ros2/examples/tree/galactic/rclpy/executors/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Contributors: Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-guard-conditions"></a>

## [examples\_rclpy\_guard\_conditions](https://github.com/ros2/examples/tree/galactic/rclpy/guard_conditions/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- [rclpy] Create a package with an example showing how guard conditions work ([#283](https://github.com/ros2/examples/issues/283))
- Contributors: Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-minimal-action-client"></a>

## [examples\_rclpy\_minimal\_action\_client](https://github.com/ros2/examples/tree/galactic/rclpy/actions/minimal_action_client/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Using asyncio with ros2 action client ([#301](https://github.com/ros2/examples/issues/301))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Added missing linting tests ([#287](https://github.com/ros2/examples/issues/287))
- Contributors: Allison Thackston, Ivan Santiago Paunovic, Shane Loretz, alemme

<a id="examples-rclpy-minimal-action-server"></a>

## [examples\_rclpy\_minimal\_action\_server](https://github.com/ros2/examples/tree/galactic/rclpy/actions/minimal_action_server/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Added missing linting tests ([#287](https://github.com/ros2/examples/issues/287))
- Contributors: Allison Thackston, Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-minimal-client"></a>

## [examples\_rclpy\_minimal\_client](https://github.com/ros2/examples/tree/galactic/rclpy/services/minimal_client/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Remove bare exception catching ([#299](https://github.com/ros2/examples/issues/299))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Contributors: Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-minimal-publisher"></a>

## [examples\_rclpy\_minimal\_publisher](https://github.com/ros2/examples/tree/galactic/rclpy/topics/minimal_publisher/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Contributors: Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-minimal-service"></a>

## [examples\_rclpy\_minimal\_service](https://github.com/ros2/examples/tree/galactic/rclpy/services/minimal_service/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Contributors: Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-minimal-subscriber"></a>

## [examples\_rclpy\_minimal\_subscriber](https://github.com/ros2/examples/tree/galactic/rclpy/topics/minimal_subscriber/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- Update maintainers ([#292](https://github.com/ros2/examples/issues/292))
- Contributors: Ivan Santiago Paunovic, Shane Loretz

<a id="examples-rclpy-pointcloud-publisher"></a>

## [examples\_rclpy\_pointcloud\_publisher](https://github.com/ros2/examples/tree/galactic/rclpy/topics/pointcloud_publisher/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#310](https://github.com/ros2/examples/issues/310))
- add pointcloud publisher example ([#276](https://github.com/ros2/examples/issues/276))
- Contributors: Evan Flynn, Ivan Santiago Paunovic

<a id="examples-tf2-py"></a>

## [examples\_tf2\_py](https://github.com/ros2/geometry2/tree/galactic/examples_tf2_py/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403)) ([#404](https://github.com/ros2/geometry2/issues/404))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Add pytest.ini so local tests don’t display warning ([#276](https://github.com/ros2/geometry2/issues/276))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="fastrtps-cmake-module"></a>

## [fastrtps\_cmake\_module](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/galactic/fastrtps_cmake_module/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#69](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/69))
- Use CMake config dirs as hint for header/library search ([#56](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/56))
- Update package maintainers ([#55](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/55))
- QD Update Version Stability to stable version ([#46](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/46))
- Contributors: Alejandro Hernández Cordero, Dirk Thomas, Michel Hidalgo, shonigmann

<a id="geometry2"></a>

## [geometry2](https://github.com/ros2/geometry2/tree/galactic/geometry2/CHANGELOG.rst)

- Port eigen\_kdl.h/cpp to ROS2 ([#311](https://github.com/ros2/geometry2/issues/311))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Contributors: Chris Lalancette, Jafar Abdi

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/geometry_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Finish up API documentation ([#123](https://github.com/ros2/common_interfaces/issues/123))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="google-benchmark-vendor"></a>

## [google\_benchmark\_vendor](https://github.com/ament/google_benchmark_vendor/tree/main/CHANGELOG.rst)

- Shrink the size of the tz\_offset variable. ([#13](https://github.com/ament/google_benchmark_vendor/issues/13))
- Update the patching to work on Windows without admin. ([#11](https://github.com/ament/google_benchmark_vendor/issues/11))
- Always preserve source permissions in vendor packages. ([#12](https://github.com/ament/google_benchmark_vendor/issues/12))
- Update package maintainers. ([#10](https://github.com/ament/google_benchmark_vendor/issues/10))
- Upgrade google benchmark from v1.5.1 to v1.5.2 to include QNX patch. ([#9](https://github.com/ament/google_benchmark_vendor/issues/9))
- Set the SOVERSION on benchmark libraries. ([#8](https://github.com/ament/google_benchmark_vendor/issues/8))
- Set minimum criteria for system package. ([#3](https://github.com/ament/google_benchmark_vendor/issues/3))
- Work around warnings building Google Benchmark w/Clang. ([#2](https://github.com/ament/google_benchmark_vendor/issues/2))
- Initial google\_benchmark\_vendor package. ([#1](https://github.com/ament/google_benchmark_vendor/issues/1))
- Initial commit.
- Contributors: Ahmed Sobhy, Chris Lalancette, Michel Hidalgo, Scott K Logan

<a id="image-common"></a>

## [image\_common](https://github.com/ros-perception/image_common/tree/ros2/image_common/CHANGELOG.rst)

- [ros2] image\_common metapackage ([#129](https://github.com/ros-perception/image_common/issues/129))
- 1.11.11
- update changelogs
- add Jack as maintainer
- comply to REP 0127
- add missing description
- define metapackage
- Contributors: Vincent Rabaud, chapulina

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/galactic/image_tools/CHANGELOG.rst)

- Initialize time stamp for published image messages ([#475](https://github.com/ros2/demos/issues/475))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Added more parameters for camera topic examples ([#465](https://github.com/ros2/demos/issues/465))
- Contributors: Jacob Perron, Michael Jeronimo

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/ros2/image_transport/CHANGELOG.rst)

- Fix formatting and include paths for linters ([#157](https://github.com/ros-perception/image_common/issues/157))
- Fix QoS initialization from RMW QoS profile ([#158](https://github.com/ros-perception/image_common/issues/158))
- add missing set header ([#140](https://github.com/ros-perception/image_common/issues/140))
- Update to use new count APIs ([#128](https://github.com/ros-perception/image_common/issues/128))
- use latest ros2 API ([#127](https://github.com/ros-perception/image_common/issues/127))
- Update ROS2 branch to account for new NodeOptions interface ([#120](https://github.com/ros-perception/image_common/issues/120))
- camera\_info\_manager ROS2 port ([#94](https://github.com/ros-perception/image_common/issues/94))
- Pointer api updates ([#104](https://github.com/ros-perception/image_common/issues/104))
- Fix rcutils API change by just removing it. ([#103](https://github.com/ros-perception/image_common/issues/103))
- [ROS2] corrections to remapping for raw images ([#97](https://github.com/ros-perception/image_common/issues/97))
- Make ROS2 ImageTransport conform to old api ([#88](https://github.com/ros-perception/image_common/issues/88))
- Image Transport ROS2 Port ([#84](https://github.com/ros-perception/image_common/issues/84))
- Disable image publisher plugins by name ([#60](https://github.com/ros-perception/image_common/issues/60)) \* Disable publisher plugins by name \* Now have per publisher blacklist instead of image\_transport wide.
- update to use non deprecated pluginlib macro
- Extend documentation of `getCameraInfoTopic` Document the fact that the `base_topic` argument must be resolved in order to build the correct camera info topic.
- Added cv::waitkey(10) for blank popup Without the cv::waitkey(10), it results in a blank popup which crashes/ leads to a black popup. This change corrects that problem. ROS Kinetic, Ubuntu 16.04.3
- Fix CMake of image\_transport/tutorial and polled\_camera Fix loads of problems with the CMakeLists.
- image\_transport/tutorial: Add dependency on generated msg Without this, build fails on Kinetic because ResizedImage.h has not been generated yet.
- image\_transport/tutorial: Add missing catkin\_INCLUDE\_DIRS Without this, compilation files on Kinetic because ros.h cannot be found.
- 1.11.11
- update changelogs
- fix linkage in tutorials
- Use $catkin\_EXPORTED\_TARGETS
- image\_transport: fix CameraSubscriber shutdown (circular shared\_ptr ref) CameraSubscriber uses a private boost::shared\_ptr to share an impl object between copied instances. In CameraSubscriber::CameraSubscriber(), it handed this shared\_ptr to boost::bind() and saved the created wall timer in the impl object, thus creating a circular reference. The impl object was therefore never freed. Fix that by passing a plain pointer to boost::bind().
- avoid a memory copy for the raw publisher
- add a way to publish an image with only the data pointer
- Make function inline to avoid duplicated names when linking statically
- add plugin examples for the tutorial
- update instructions for catkin
- remove uselessly linked library fixes [#28](https://github.com/ros-perception/image_common/issues/28)
- add a tutorial for image\_transport
- add Jack as maintainer
- update my email address
- fix the urls
- use the pluginlib script to remove some warnings
- added license headers to various cpp and h files
- get rid of the deprecated class\_loader interface
- CMakeLists.txt clean up
- Updated package.xml file(s) to handle new catkin buildtool\_depend requirement
- add the right link libraries
- Isolated plugins into their own library to follow new class\_loader/pluginlib guidelines.
- remove the brief attribute
- add xml file
- fix bad folder/libraries
- fix dependencies
- add catkin as a dependency
- comply to the catkin API
- install the include directories
- make the libraries public
- catkinize for Groovy
- Initial image\_common stack check-in, containing image\_transport.
- Contributors: Aaditya Saraiya, Aaron Blasdel, Carl Delsey, Gary Servin, Jacob Perron, Jochen Sprickerhof, Karsten Knese, Lucas Walter, Martin Guenther, Martin Idel, Max Schwarz, Michael Carroll, Mikael Arguedas, Mirza Shah, Thibaud Chupin, Vincent Rabaud, William Woodall, gerkey, kwc, mihelich, mirzashah, pmihelich, straszheim, vrabaud

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/galactic/CHANGELOG.rst)

- Cleanup bsd 3 clause license usage ([#61](https://github.com/ros-visualization/interactive_markers/issues/61))
- Add missing includes ([#81](https://github.com/ros-visualization/interactive_markers/issues/81))
- Update maintainers ([#79](https://github.com/ros-visualization/interactive_markers/issues/79))
- Increase test timeout necessary for Connext ([#77](https://github.com/ros-visualization/interactive_markers/issues/77))
- Fix clang warnings ([#75](https://github.com/ros-visualization/interactive_markers/issues/75))
- Remove explicit template parameter in `spin_until_future_complete` ([#72](https://github.com/ros-visualization/interactive_markers/issues/72))
- Contributors: Bjar Ne, Dirk Thomas, Jacob Perron, Sarthak Mittal, Tully Foote

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/galactic/intra_process_demo/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/galactic/kdl_parser/CHANGELOG.rst)

- Remove tinyxml dependency from kdl\_parser. ([#43](https://github.com/ros/kdl_parser/issues/43))
- Remove unused find\_library call ([#40](https://github.com/ros/kdl_parser/issues/40))
- Contributors: Chris Lalancette, Michael Carroll

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/galactic/CHANGELOG.rst)

- Use rclcpp::Duration::from\_seconds ([#72](https://github.com/ros-perception/laser_geometry/issues/72))
- update maintainers
- increase test timeout
- Contributors: Dirk Thomas, Ivan Santiago Paunovic, Jonathan Binney, Mabel Zhang

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/galactic/launch/CHANGELOG.rst)

- Only try to wrap the fd in a socket on Windows ([#498](https://github.com/ros2/launch/issues/498))
- Close the socket pair used for signal management ([#497](https://github.com/ros2/launch/issues/497))
- Remove is\_winsock\_handle() and instead test if wrapping the handle in a socket.socket() works ([#494](https://github.com/ros2/launch/issues/494))
- Add frontend substitution for logging directory ([#490](https://github.com/ros2/launch/issues/490))
- Add arg\_choice arg to DeclareLaunchArguments ([#483](https://github.com/ros2/launch/issues/483))
- Support Python 3.8-provided importlib.metadata ([#482](https://github.com/ros2/launch/issues/482))
- Workaround asyncio signal handling on Unix ([#479](https://github.com/ros2/launch/issues/479))
- Handle signals within the asyncio loop. ([#476](https://github.com/ros2/launch/issues/476))
- Support non-interactive launch.LaunchService runs ([#475](https://github.com/ros2/launch/issues/475))
- print stderr message when command failed ([#474](https://github.com/ros2/launch/issues/474))
- Add frontend support for LogInfo action ([#467](https://github.com/ros2/launch/issues/467))
- Validate unparsed attributes and subentities in launch\_xml and launch\_yaml ([#468](https://github.com/ros2/launch/issues/468))
- Fix bug in launch.actions.TimerAction.parse() ([#470](https://github.com/ros2/launch/issues/470))
- Allow configuring logging directory through environment variables ([#460](https://github.com/ros2/launch/issues/460))
- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Expose Timer action in launch xml ([#462](https://github.com/ros2/launch/issues/462))
- Fix dollar symbols in substitution grammar ([#461](https://github.com/ros2/launch/issues/461))
- Add new conditions for checking launch configuration values ([#453](https://github.com/ros2/launch/issues/453))
- Refactor launch service run\_async loop to wait on futures and queued events ([#449](https://github.com/ros2/launch/issues/449))
- Fix documentation typo ([#446](https://github.com/ros2/launch/issues/446))
- Fix type\_utils.extract\_type() function. ([#445](https://github.com/ros2/launch/issues/445))
- Handle empty strings in type coercion. ([#443](https://github.com/ros2/launch/issues/443))
- Consolidate type\_utils in a way that can be reused in substitution results that need to be coerced to a specific type ([#438](https://github.com/ros2/launch/issues/438))
- Delete unnecessary loading of ‘launch.frontend.interpolate\_substitution\_method’ entry point that was never used ([#434](https://github.com/ros2/launch/issues/434))
- Avoid side effect, defer until needed ([#432](https://github.com/ros2/launch/issues/432))
- Remove pkg\_resources, replace it with the use of the more modern importlib\* libraries. ([#430](https://github.com/ros2/launch/issues/430))
- Remove the asyncio.wait loop parameter. ([#429](https://github.com/ros2/launch/issues/429))
- Add pytest.ini so local tests don’t display warning ([#428](https://github.com/ros2/launch/issues/428))
- Defer shutdown if already running ([#427](https://github.com/ros2/launch/issues/427))
- Add respawn and respawn\_delay support ([#426](https://github.com/ros2/launch/issues/426))
- Fix up parser.py ([#414](https://github.com/ros2/launch/issues/414))
- Contributors: CHEN, Chris Lalancette, Christophe Bedard, Dan Rose, Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Michel Hidalgo, Scott K Logan, Takamasa Horibe, Victor Lopez

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/galactic/launch_ros/CHANGELOG.rst)

- Support Python 3.8 importlib.metadata, declare dependency ([#229](https://github.com/ros2/launch_ros/issues/229))
- Add options extensions to ros2launch and extensibility to the node action ([#216](https://github.com/ros2/launch_ros/issues/216))
- Make sure ParameterFile \_\_del\_\_ works without exception. ([#212](https://github.com/ros2/launch_ros/issues/212))
- Fix docblock in LoadComposableNodes ([#207](https://github.com/ros2/launch_ros/issues/207))
- Validate complex attributes of ‘node’ action ([#198](https://github.com/ros2/launch_ros/issues/198))
- Node.\_\_init\_\_() executable and ComposableNode.\_\_init\_\_() plugin arguments aren’t optional ([#197](https://github.com/ros2/launch_ros/issues/197))
- Remove constructors arguments deprecated since Foxy ([#190](https://github.com/ros2/launch_ros/issues/190))
- Make name and namespace mandatory in ComposableNodeContainer, remove deprecated alternatives ([#189](https://github.com/ros2/launch_ros/issues/189))
- Merge pull request [#183](https://github.com/ros2/launch_ros/issues/183) from ros2/update-maintainers Update the package.xml files with the latest Open Robotics maintainers
- Move previous maintainer to <author>
- Update the package.xml files with the latest Open Robotics maintainers
- Fix AttributeError when accessing component container name ([#177](https://github.com/ros2/launch_ros/issues/177))
- Handle any substitution types for SetParameter name argument ([#182](https://github.com/ros2/launch_ros/issues/182))
- Asynchronously wait for load node service response ([#174](https://github.com/ros2/launch_ros/issues/174))
- Fix case where list of composable nodes is zero ([#173](https://github.com/ros2/launch_ros/issues/173))
- Do not use event handler for loading composable nodes ([#170](https://github.com/ros2/launch_ros/issues/170))
- Fix race with launch context changes when loading composable nodes ([#166](https://github.com/ros2/launch_ros/issues/166))
- Substitutions in parameter files ([#168](https://github.com/ros2/launch_ros/issues/168))
- Fix documentation typo ([#167](https://github.com/ros2/launch_ros/issues/167))
- Fix problems when parsing a `Command` `Substitution` as a parameter value ([#137](https://github.com/ros2/launch_ros/issues/137))
- Add a way to set remapping rules for all nodes in the same scope ([#163](https://github.com/ros2/launch_ros/issues/163))
- Resolve libyaml warning when loading parameters from file ([#161](https://github.com/ros2/launch_ros/issues/161))
- Fix ComposableNode ignoring PushRosNamespace actions ([#162](https://github.com/ros2/launch_ros/issues/162))
- Add a SetParameter action that sets a parameter to all nodes in the same scope ([#158](https://github.com/ros2/launch_ros/issues/158))
- Make namespace parameter mandatory in LifecycleNode constructor ([#157](https://github.com/ros2/launch_ros/issues/157))
- Avoid using a wildcard to specify parameters if possible ([#154](https://github.com/ros2/launch_ros/issues/154))
- Fix no specified namespace ([#153](https://github.com/ros2/launch_ros/issues/153))
- Add pytest.ini so local tests don’t display warning ([#152](https://github.com/ros2/launch_ros/issues/152))
- Contributors: Chris Lalancette, Dereck Wonnacott, Geoffrey Biggs, Ivan Santiago Paunovic, Jacob Perron, Michael Jeronimo, Scott K Logan

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/galactic/launch_testing/CHANGELOG.rst)

- Use unittest.mock instead of mock ([#487](https://github.com/ros2/launch/issues/487))
- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Disable cleanup of test cases once they have been run ([#406](https://github.com/ros2/launch/issues/406))
- Fix max() with empty sequence ([#440](https://github.com/ros2/launch/issues/440))
- Use unittest.TestCase.id() for pytest failure reprs. ([#436](https://github.com/ros2/launch/issues/436))
- Use unittest.TestCase.id() to put together jUnit XML output. ([#435](https://github.com/ros2/launch/issues/435))
- Claim ownership ([#433](https://github.com/ros2/launch/issues/433))
- Contributors: Dirk Thomas, Michel Hidalgo, Scott K Logan, William Woodall

<a id="launch-testing-ament-cmake"></a>

## [launch\_testing\_ament\_cmake](https://github.com/ros2/launch/tree/galactic/launch_testing_ament_cmake/CHANGELOG.rst)

- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Add bsd license to launch due to files from roslaunch ([#456](https://github.com/ros2/launch/issues/456))
- Use launch\_test CMake target as output file basename ([#448](https://github.com/ros2/launch/issues/448))
- Find Python debug interpreter on Windows ([#437](https://github.com/ros2/launch/issues/437))
- Contributors: Dirk Thomas, Michel Hidalgo, William Woodall

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/galactic/launch_testing_ros/CHANGELOG.rst)

- Use underscores in setup.cfg instead of dashes. ([#227](https://github.com/ros2/launch_ros/issues/227))
- Merge pull request [#183](https://github.com/ros2/launch_ros/issues/183) from ros2/update-maintainers
- Move Pete to author, per clalancette
- Update the package.xml files with the latest Open Robotics maintainers
- Add pytest.ini so local tests don’t display warning ([#152](https://github.com/ros2/launch_ros/issues/152))
- Contributors: Chris Lalancette, Michael Jeronimo, Mike Purvis

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/galactic/launch_xml/CHANGELOG.rst)

- Add frontend support for LogInfo action ([#467](https://github.com/ros2/launch/issues/467))
- Validate unparsed attributes and subentities in launch\_xml and launch\_yaml ([#468](https://github.com/ros2/launch/issues/468))
- Add test for launch.actions.TimerAction ([#470](https://github.com/ros2/launch/issues/470))
- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Use new type\_utils functions ([#438](https://github.com/ros2/launch/issues/438))
- Add pytest.ini so local tests don’t display warning ([#428](https://github.com/ros2/launch/issues/428))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/galactic/launch_yaml/CHANGELOG.rst)

- Add frontend support for LogInfo action ([#467](https://github.com/ros2/launch/issues/467))
- Validate unparsed attributes and subentities in launch\_xml and launch\_yaml ([#468](https://github.com/ros2/launch/issues/468))
- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Use new type\_utils functions ([#438](https://github.com/ros2/launch/issues/438))
- Close YAML file when we’re done. ([#415](https://github.com/ros2/launch/issues/415))
- Add pytest.ini so local tests don’t display warning ([#428](https://github.com/ros2/launch/issues/428))
- Contributors: Chris Lalancette, Dan Rose, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo

<a id="libcurl-vendor"></a>

## [libcurl\_vendor](https://github.com/ros/resource_retriever/tree/galactic/libcurl_vendor/CHANGELOG.rst)

- Update libcurl\_vendor to the latest version (7.75.0). ([#60](https://github.com/ros/resource_retriever/issues/60))
- Add an override flag to force vendored build ([#58](https://github.com/ros/resource_retriever/issues/58))
- Update maintainers ([#53](https://github.com/ros/resource_retriever/issues/53))
- bump curl version to 7.68 ([#47](https://github.com/ros/resource_retriever/issues/47))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, Scott K Logan

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/galactic/CHANGELOG.rst)

- fix: measured values after the decimal point are truncated [#79](https://github.com/ros-tooling/libstatistics_collector/issues/79) ([#80](https://github.com/ros-tooling/libstatistics_collector/issues/80))
- Update linter to run on rolling+focal ([#81](https://github.com/ros-tooling/libstatistics_collector/issues/81))
- Add automerge.yml config file ([#70](https://github.com/ros-tooling/libstatistics_collector/issues/70))
- Update QD to QL 1 ([#68](https://github.com/ros-tooling/libstatistics_collector/issues/68))
- Updated QD ([#64](https://github.com/ros-tooling/libstatistics_collector/issues/64))
- Updated QD Performance tests ([#58](https://github.com/ros-tooling/libstatistics_collector/issues/58))
- Added benchmark test to libstatistics\_collector ([#57](https://github.com/ros-tooling/libstatistics_collector/issues/57)) \* Added benchmark test to libstatistics\_collector \* cppcheck supressed unknown macro warning - macos \* Reset heap counters \* Added feedback \* Remove unknownMacro suppression from CMakeLists.txt \* Added feedback \* moved benchmark test to test/benchmark \* Added feedback Co-authored-by: Devin Bonnie <[47613035+dabonnie@users.noreply.github.com](mailto:47613035+dabonnie%40users.noreply.github.com)>
- Report failed workflows ([#56](https://github.com/ros-tooling/libstatistics_collector/issues/56)) Allow codecov failures to be silent
- Add default CODEOWNERS file ([#55](https://github.com/ros-tooling/libstatistics_collector/issues/55))
- Remove repo activity from individual repositories in favor of centralized reporting ([#52](https://github.com/ros-tooling/libstatistics_collector/issues/52))
- Don’t attempt to report if originating from a fork ([#43](https://github.com/ros-tooling/libstatistics_collector/issues/43))
- Removed doxygen warnings ([#41](https://github.com/ros-tooling/libstatistics_collector/issues/41)) Co-authored-by: Anas Abou Allaban <[allabana@amazon.com](mailto:allabana%40amazon.com)>
- Add autoapprove action for dependabot ([#40](https://github.com/ros-tooling/libstatistics_collector/issues/40))
- Create Dependabot config file ([#31](https://github.com/ros-tooling/libstatistics_collector/issues/31)) \* Create Dependabot config file \* Randomize time of run Co-authored-by: dependabot-preview[bot] <27856297+dependabot-preview[bot]@users.noreply.github.com> Co-authored-by: Prajakta Gokhale <[prajaktg@amazon.com](mailto:prajaktg%40amazon.com)>
- Updated QD to 3 ([#30](https://github.com/ros-tooling/libstatistics_collector/issues/30))
- Add Security Vulnerability Policy pointing to REP-2006. ([#24](https://github.com/ros-tooling/libstatistics_collector/issues/24)) Co-authored-by: Emerson Knapp <[537409+emersonknapp@users.noreply.github.com](mailto:537409+emersonknapp%40users.noreply.github.com)>
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Devin Bonnie, Emerson Knapp, Lucas Han, Prajakta Gokhale, Stephen Brawner, hsgwa

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/galactic/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#38](https://github.com/ros2/libyaml_vendor/issues/38))
- Update libyaml\_vendor to 0.2.5. ([#37](https://github.com/ros2/libyaml_vendor/issues/37))
- Fix linker flags for tests when CMake < 3.13 ([#35](https://github.com/ros2/libyaml_vendor/issues/35))
- Always preserve source permissions in vendor packages ([#31](https://github.com/ros2/libyaml_vendor/issues/31))
- Fix target\_link\_directories/link\_directories in cmake ([#29](https://github.com/ros2/libyaml_vendor/issues/29))
- Included benchmark tests ([#20](https://github.com/ros2/libyaml_vendor/issues/20))
- Update Quality Declaration ([#23](https://github.com/ros2/libyaml_vendor/issues/23))
- Update package maintainers. ([#22](https://github.com/ros2/libyaml_vendor/issues/22))
- Bump QD to 3 and some minor style fixes ([#19](https://github.com/ros2/libyaml_vendor/issues/19))
- Add Security Vulnerability Policy pointing to REP-2006. ([#18](https://github.com/ros2/libyaml_vendor/issues/18))
- Add quality declaration libyaml\_vendor ([#12](https://github.com/ros2/libyaml_vendor/issues/12))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge Perez, Michel Hidalgo, Scott K Logan, shonigmann

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/galactic/lifecycle/CHANGELOG.rst)

- Cleanup the README.rst for the lifecycle demo. ([#508](https://github.com/ros2/demos/issues/508))
- change ParameterEventHandler to take events as const ref instead of shared pointer ([#494](https://github.com/ros2/demos/issues/494))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Add missing required parameter in LifecycleNode launch action ([#456](https://github.com/ros2/demos/issues/456))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael Jeronimo, William Woodall

<a id="lifecycle-msgs"></a>

## [lifecycle\_msgs](https://github.com/ros2/rcl_interfaces/tree/galactic/lifecycle_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/galactic/logging_demo/CHANGELOG.rst)

- Update logging macros ([#476](https://github.com/ros2/demos/issues/476))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Audrow Nash, Michael Jeronimo

<a id="map-msgs"></a>

## [map\_msgs](https://github.com/ros-planning/navigation_msgs/tree/galactic/map_msgs/CHANGELOG.rst)

- update maintainers
- Contributors: Mabel Zhang, Steve Macenski

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/galactic/CHANGELOG.rst)

- Find and export dependencies properly ([#54](https://github.com/ros2/message_filters/issues/54))
- Add pytest.ini so local tests don’t display warning ([#47](https://github.com/ros2/message_filters/issues/47))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/galactic/CHANGELOG.rst)

- Always preserve source permissions in vendor packages ([#19](https://github.com/ros2/mimick_vendor/issues/19))
- Suppress update of pinned git repository ([#17](https://github.com/ros2/mimick_vendor/issues/17))
- Don’t overwrite -Wno-dev CMake argument ([#18](https://github.com/ros2/mimick_vendor/issues/18))
- Add missing build tool dependency on ‘git’ ([#16](https://github.com/ros2/mimick_vendor/issues/16))
- Update tag for armv7l support. ([#15](https://github.com/ros2/mimick_vendor/issues/15))
- Update tag for new cmake version requirement ([#14](https://github.com/ros2/mimick_vendor/issues/14))
- Export include directories ([#13](https://github.com/ros2/mimick_vendor/issues/13))
- Update package maintainers ([#10](https://github.com/ros2/mimick_vendor/issues/10))
- Suppress cppcheck for MMK\_MANGLE\_ ([#8](https://github.com/ros2/mimick_vendor/issues/8))
- Change Mimick tagged version. ([#7](https://github.com/ros2/mimick_vendor/issues/7))
- Change tag to pull latest Mimick version ([#6](https://github.com/ros2/mimick_vendor/issues/6))
- Pin Mimick version. ([#5](https://github.com/ros2/mimick_vendor/issues/5))
- Change imported dep to match ROS 2 fork ([#4](https://github.com/ros2/mimick_vendor/issues/4))
- Avoid CMAKE\_BUILD\_TYPE warnings on Windows. ([#3](https://github.com/ros2/mimick_vendor/issues/3))
- Remove dep tag + add maintainer([#2](https://github.com/ros2/mimick_vendor/issues/2))
- Configure MSVC x64 builds when appropriate. ([#1](https://github.com/ros2/mimick_vendor/issues/1))
- First iteration vendor for Mimick library
- Contributors: Jorge Perez, Michel Hidalgo, Scott K Logan, Stephen Brawner, brawner

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/nav_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Add LoadMap service ([#129](https://github.com/ros2/common_interfaces/issues/129))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Finish up API documentation ([#123](https://github.com/ros2/common_interfaces/issues/123))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, Steve Macenski, brawner, shonigmann

<a id="osrf-pycommon"></a>

## [osrf\_pycommon](https://github.com/osrf/osrf_pycommon/tree/master/CHANGELOG.rst)

- Fix osrf.py\_common.process\_utils.get\_loop() implementation ([#70](https://github.com/osrf/osrf_pycommon/issues/70))
- Python 2/3 version conflict ([#69](https://github.com/osrf/osrf_pycommon/issues/69))
- remove jessie because we no longer support 3.4 ([#67](https://github.com/osrf/osrf_pycommon/issues/67))
- Remove deprecated use of asyncio.coroutine decorator. ([#64](https://github.com/osrf/osrf_pycommon/issues/64))
- Fix the \_\_str\_\_ method for windows terminal\_color. ([#65](https://github.com/osrf/osrf_pycommon/issues/65))
- Contributors: Chris Lalancette, Jochen Sprickerhof, Michel Hidalgo, William Woodall

<a id="osrf-testing-tools-cpp"></a>

## [osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/master/osrf_testing_tools_cpp/CHANGELOG.rst)

- [osrf\_testing\_tools\_cpp] Add warnings ([#54](https://github.com/osrf/osrf_testing_tools_cpp/issues/54))
- Update cmake minimum version to 2.8.12 ([#61](https://github.com/osrf/osrf_testing_tools_cpp/issues/61))
- Add googletest v1.10.0 ([#55](https://github.com/osrf/osrf_testing_tools_cpp/issues/55))
- Workarounds for Android ([#52](https://github.com/osrf/osrf_testing_tools_cpp/issues/52)) ([#60](https://github.com/osrf/osrf_testing_tools_cpp/issues/60))
- Change `WIN32` to `__WIN32` ([#53](https://github.com/osrf/osrf_testing_tools_cpp/issues/53))
- fix execinfo.h not found for QNX ([#50](https://github.com/osrf/osrf_testing_tools_cpp/issues/50))
- Contributors: Ahmed Sobhy, Audrow Nash, Dan Rose, Jacob Perron, Stephen Brawner

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/galactic/pendulum_control/CHANGELOG.rst)

- Replace rmw\_connext\_cpp with rmw\_connextdds ([#489](https://github.com/ros2/demos/issues/489))
- Remove ineffective log output ([#450](https://github.com/ros2/demos/issues/450)) ([#477](https://github.com/ros2/demos/issues/477))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Remove deprecated warning ([#459](https://github.com/ros2/demos/issues/459))
- Follow API/file name changes ([ros2/realtime\_support#94](https://github.com/ros2/realtime_support/issues/94)) ([#451](https://github.com/ros2/demos/issues/451))
- Contributors: Anas Abou Allaban, Andrea Sorbini, Michael Jeronimo, y-okumura-isp

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/galactic/pendulum_msgs/CHANGELOG.rst)

- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Michael Jeronimo

<a id="performance-test-fixture"></a>

## [performance\_test\_fixture](https://github.com/ros2/performance_test_fixture/tree/main/CHANGELOG.rst)

- Record calls to calloc, update tests ([#15](https://github.com/ros2/performance_test_fixture/issues/15))
- Make allocation counter atomic ([#13](https://github.com/ros2/performance_test_fixture/issues/13)) Even if the benchmark itself isn’t threaded, the process we’re testing could be. In any case, this should prevent those shenanigans from messing up the measurement.
- Add methods for pausing/resuming performance metrics ([#10](https://github.com/ros2/performance_test_fixture/issues/10)) \* Add methods for pausing/resuming performance metrics
- Add benchmarks to evaluate overhead ([#11](https://github.com/ros2/performance_test_fixture/issues/11)) \* Add benchmarks to evaluate overhead in performance tests
- Add namespace performance\_test\_fixture to .cpp ([#9](https://github.com/ros2/performance_test_fixture/issues/9))
- Export dependency on benchmark and osrf\_testing\_tools\_cpp ([#8](https://github.com/ros2/performance_test_fixture/issues/8))
- Update maintainers ([#7](https://github.com/ros2/performance_test_fixture/issues/7))
- Expose a function for resetting the heap counters ([#6](https://github.com/ros2/performance_test_fixture/issues/6))
- Stop recording memory operations sooner ([#5](https://github.com/ros2/performance_test_fixture/issues/5))
- Suppress memory tools warning if tests will be skipped ([#4](https://github.com/ros2/performance_test_fixture/issues/4))
- Export dependency on ament\_cmake\_google\_benchmark ([#3](https://github.com/ros2/performance_test_fixture/issues/3))
- Add missing dependency on ament\_cmake\_google\_benchmark ([#2](https://github.com/ros2/performance_test_fixture/issues/2))
- Initial ‘performance\_test\_fixture’ package ([#1](https://github.com/ros2/performance_test_fixture/issues/1))
- Initial commit
- Contributors: Alejandro Hernández Cordero, Scott K Logan, brawner

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/galactic/pluginlib/CHANGELOG.rst)

- Use rcpputils for the filesystem implementation. ([#212](https://github.com/ros/pluginlib/issues/212))
- Check for NULL in XMLElement::Attribute
- Check for NULL in XMLElement::GetText
- Check for NULL in XMLNode::Value
- Remove unused variable output\_library ([#211](https://github.com/ros/pluginlib/issues/211))
- Make Chris a maintainer of pluginlib. ([#210](https://github.com/ros/pluginlib/issues/210))
- Add QNX C++ fs library compiler option ([#205](https://github.com/ros/pluginlib/issues/205))
- Fix cmake 3.5 compatibility ([#203](https://github.com/ros/pluginlib/issues/203))
- Add function for same-package pluginlib tests ([#201](https://github.com/ros/pluginlib/issues/201))
- Remove deprecated boost functions ([#199](https://github.com/ros/pluginlib/issues/199))
- Contributors: Ahmed Sobhy, Chris Lalancette, Jeremie Deray, Karsten Knese, Shane Loretz

<a id="pybind11-vendor"></a>

## [pybind11\_vendor](https://github.com/ros2/pybind11_vendor/tree/foxy/CHANGELOG.rst)

- Update maintainers ([#7](https://github.com/ros2/pybind11_vendor/issues/7))
- Merge pull request [#3](https://github.com/ros2/pybind11_vendor/issues/3) from ros2/fix\_windows\_warning
- remove passing in CMAKE\_BUILD\_TYPE Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- cleanup Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- do not define CMAKE\_BUILD\_TYPE on windows Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- suppress all developer warnings Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- suppress warning on windows Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- attempt to fix windows warning Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- Disable building pybind11 tests ([#1](https://github.com/ros2/pybind11_vendor/issues/1)) Signed-off-by: Karsten Knese <[karsten@openrobotics.org](mailto:karsten%40openrobotics.org)>
- Update to pybind 2.5.0 ([#2](https://github.com/ros2/pybind11_vendor/issues/2)) Signed-off-by: Mabel Zhang <[mabel@openrobotics.org](mailto:mabel%40openrobotics.org)>
- Create pybind11 vendor package. Signed-off-by: Michael Carroll <[michael@openrobotics.org](mailto:michael%40openrobotics.org)>
- Contributors: Karsten Knese, Mabel Zhang, Michael Carroll, Shane Loretz

<a id="python-cmake-module"></a>

## [python\_cmake\_module](https://github.com/ros2/python_cmake_module/tree/galactic/CHANGELOG.rst)

- Update maintainers ([#2](https://github.com/ros2/python_cmake_module/issues/2))
- Contributors: Shane Loretz

<a id="python-qt-binding"></a>

## [python\_qt\_binding](https://github.com/ros-visualization/python_qt_binding/tree/main/CHANGELOG.rst)

- Add repo README
- Shorten some long lines of CMake ([#99](https://github.com/ros-visualization/python_qt_binding/issues/99))
- Update maintainers ([#96](https://github.com/ros-visualization/python_qt_binding/issues/96)) ([#98](https://github.com/ros-visualization/python_qt_binding/issues/98))
- Add pytest.ini so local tests don’t display warning ([#93](https://github.com/ros-visualization/python_qt_binding/issues/93))
- Contributors: Chris Lalancette, Scott K Logan, Shane Loretz

<a id="qt-dotgraph"></a>

## [qt\_dotgraph](https://github.com/ros-visualization/qt_gui_core/tree/galactic-devel/qt_dotgraph/CHANGELOG.rst)

- add API to set edge tooltip ([#237](https://github.com/ros-visualization/qt_gui_core/issues/237))

<a id="qt-gui"></a>

## [qt\_gui](https://github.com/ros-visualization/qt_gui_core/tree/galactic-devel/qt_gui/CHANGELOG.rst)

- Always prefer ‘Tango’ icon theme ([#250](https://github.com/ros-visualization/qt_gui_core/issues/250))
- Fix ‘dict\_keys’ object not subscriptable ([#243](https://github.com/ros-visualization/qt_gui_core/issues/243))
- allow hide title in standalone ([#235](https://github.com/ros-visualization/qt_gui_core/issues/235))
- add logic to load qt\_gui\_icons on windows and macOS ([#222](https://github.com/ros-visualization/qt_gui_core/issues/222))
- fix exporting perspective for Python 3.6 ([#228](https://github.com/ros-visualization/qt_gui_core/issues/228))
- remove tango-icon-theme dependency ([#224](https://github.com/ros-visualization/qt_gui_core/issues/224))
- Contributors: Michael Jeronimo, Scott K Logan

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/galactic-devel/qt_gui_cpp/CHANGELOG.rst)

- Fix duplicated QMap to QMultiMap ([#244](https://github.com/ros-visualization/qt_gui_core/issues/244))
- Switch to using the filesystem implementation in rcpputils. ([#239](https://github.com/ros-visualization/qt_gui_core/issues/239))
- avoid a warning about C++ plugins on Windows ([#232](https://github.com/ros-visualization/qt_gui_core/issues/232))
- qt\_gui\_cpp\_sip: declare private assignment operator for SIP ([#226](https://github.com/ros-visualization/qt_gui_core/issues/226))
- Contributors: Chris Lalancette, Homalozoa X

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/galactic/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Add demo of how to use qos overrides ([#474](https://github.com/ros2/demos/issues/474))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Update comments in quality\_of\_service\_demo\_cpp message\_lost\_talker and message\_lost\_listener ([#458](https://github.com/ros2/demos/issues/458))
- Add message lost status event demo using rclcpp ([#453](https://github.com/ros2/demos/issues/453))
- Contributors: Ivan Santiago Paunovic, Michael Jeronimo

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/galactic/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#502](https://github.com/ros2/demos/issues/502))
- QoS overrides demo in python ([#479](https://github.com/ros2/demos/issues/479))
- Update deprecated qos policy value names ([#468](https://github.com/ros2/demos/issues/468))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Add rclpy message lost status event demo ([#457](https://github.com/ros2/demos/issues/457))
- Contributors: Ivan Santiago Paunovic, Michael Jeronimo

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/galactic/rcl/CHANGELOG.rst)

- Fix up test\_network\_flow\_endpoints. ([#912](https://github.com/ros2/rcl/issues/912))
- Make test\_two\_timers\_ready\_before\_timeout less flaky ([#911](https://github.com/ros2/rcl/issues/911))
- Add publishing instrumentation ([#905](https://github.com/ros2/rcl/issues/905))
- Unique network flows ([#880](https://github.com/ros2/rcl/issues/880))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#909](https://github.com/ros2/rcl/issues/909))
- Add functions for waiting for publishers and subscribers ([#907](https://github.com/ros2/rcl/issues/907))
- Revert “Mark cyclonedds test\_service test as flakey ([#648](https://github.com/ros2/rcl/issues/648))” ([#904](https://github.com/ros2/rcl/issues/904))
- Guard against returning NULL or empty node names ([#570](https://github.com/ros2/rcl/issues/570))
- Remove exceptions for rmw\_connext\_cpp tests. ([#903](https://github.com/ros2/rcl/issues/903))
- Add support for rmw\_connextdds ([#895](https://github.com/ros2/rcl/issues/895))
- Put an argument list of ‘void’ where no arguments are expected. ([#899](https://github.com/ros2/rcl/issues/899))
- Cleanup documentation for doxygen. ([#896](https://github.com/ros2/rcl/issues/896))
- Reference test resources directly from source tree ([#554](https://github.com/ros2/rcl/issues/554))
- Re-add “Improve trigger test for graph guard condition ([#811](https://github.com/ros2/rcl/issues/811))” ([#884](https://github.com/ros2/rcl/issues/884))
- Revert “Improve trigger test for graph guard condition ([#811](https://github.com/ros2/rcl/issues/811))” ([#883](https://github.com/ros2/rcl/issues/883))
- Move the guard condition cleanup after removing callback. ([#877](https://github.com/ros2/rcl/issues/877))
- Make test\_subscription\_nominal\_string\_sequence more reliable ([#881](https://github.com/ros2/rcl/issues/881))
- Improve trigger test for graph guard condition ([#811](https://github.com/ros2/rcl/issues/811))
- Add NULL check in remap.c ([#879](https://github.com/ros2/rcl/issues/879))
- Add const to constant rcl\_context functions ([#872](https://github.com/ros2/rcl/issues/872))
- Fix another failing test on CentOS 7 ([#863](https://github.com/ros2/rcl/issues/863))
- Update QDs to QL 1 ([#866](https://github.com/ros2/rcl/issues/866))
- Address clang static analysis issues ([#865](https://github.com/ros2/rcl/issues/865))
- Fix flaky test\_info\_by\_topic ([#859](https://github.com/ros2/rcl/issues/859))
- Update QL ([#858](https://github.com/ros2/rcl/issues/858))
- Refactor for removing unnecessary source code ([#857](https://github.com/ros2/rcl/issues/857))
- Clarify storing of current\_time ([#850](https://github.com/ros2/rcl/issues/850))
- Make tests in test\_graph.cpp more reliable ([#854](https://github.com/ros2/rcl/issues/854))
- Fix for external log segfault after SIGINT ([#844](https://github.com/ros2/rcl/issues/844))
- Update tracetools QL and add to rcl\_lifecycle’s QD ([#845](https://github.com/ros2/rcl/issues/845))
- Make test logging rosout more reliable ([#846](https://github.com/ros2/rcl/issues/846))
- Return OK when finalizing zero-initialized contexts ([#842](https://github.com/ros2/rcl/issues/842))
- Zero initialize events an size\_of\_events members of rcl\_wait\_set\_t ([#841](https://github.com/ros2/rcl/issues/841))
- Update deprecated gtest macros ([#818](https://github.com/ros2/rcl/issues/818))
- Make sure to check the return value of rcl APIs. ([#838](https://github.com/ros2/rcl/issues/838))
- Add convenient node method to get a final topic/service name ([#835](https://github.com/ros2/rcl/issues/835))
- Remove redundant error formatting ([#834](https://github.com/ros2/rcl/issues/834))
- Fix memory leak in rcl\_subscription\_init()/rcl\_publisher\_init() ([#794](https://github.com/ros2/rcl/issues/794))
- Update maintainers ([#825](https://github.com/ros2/rcl/issues/825))
- Add a semicolon to RCUTILS\_LOGGING\_AUTOINIT. ([#816](https://github.com/ros2/rcl/issues/816))
- Improve error messages in rcl\_lifecycle ([#742](https://github.com/ros2/rcl/issues/742))
- Fix memory leak on serialized message in test\_publisher/subscription.cpp ([#801](https://github.com/ros2/rcl/issues/801))
- Fix memory leak because of mock test ([#800](https://github.com/ros2/rcl/issues/800))
- Spelling correction ([#798](https://github.com/ros2/rcl/issues/798))
- Fix that not to deallocate event impl in some failure case ([#790](https://github.com/ros2/rcl/issues/790))
- calling fini functions to avoid memory leak ([#791](https://github.com/ros2/rcl/issues/791))
- Bump rcl arguments’ API test coverage ([#777](https://github.com/ros2/rcl/issues/777))
- Fix rcl arguments’ API memory leaks and bugs ([#778](https://github.com/ros2/rcl/issues/778))
- Add coverage tests wait module ([#769](https://github.com/ros2/rcl/issues/769))
- Fix wait set allocation cleanup ([#770](https://github.com/ros2/rcl/issues/770))
- Improve test coverage in rcl ([#764](https://github.com/ros2/rcl/issues/764))
- Check if rcutils\_strdup() outcome immediately ([#768](https://github.com/ros2/rcl/issues/768))
- Cleanup rcl\_get\_secure\_root() implementation ([#762](https://github.com/ros2/rcl/issues/762))
- Add fault injection macros to rcl functions ([#727](https://github.com/ros2/rcl/issues/727))
- Yield rcl\_context\_fini() error codes ([#763](https://github.com/ros2/rcl/issues/763))
- Do not invalidate context before successful shutdown ([#761](https://github.com/ros2/rcl/issues/761))
- Zero initialize guard condition on failed init ([#760](https://github.com/ros2/rcl/issues/760))
- Adding tests to arguments API ([#752](https://github.com/ros2/rcl/issues/752))
- Extend rcl\_expand\_topic\_name() API test coverage ([#758](https://github.com/ros2/rcl/issues/758))
- Add coverage tests 94% to service API ([#756](https://github.com/ros2/rcl/issues/756))
- Clean up rcl\_expand\_topic\_name() implementation ([#757](https://github.com/ros2/rcl/issues/757))
- Complete rcl enclave validation API coverage ([#751](https://github.com/ros2/rcl/issues/751))
- Cope with base function restrictions in mocks ([#753](https://github.com/ros2/rcl/issues/753))
- Fix allocation when copying arguments ([#748](https://github.com/ros2/rcl/issues/748))
- Complete rcl package’s logging API test coverage ([#747](https://github.com/ros2/rcl/issues/747))
- Improve coverage to 95% in domain id, init option, rmw implementation id and log level modules ([#744](https://github.com/ros2/rcl/issues/744))
- Fix rcl package’s logging API error code documentation and handling ([#746](https://github.com/ros2/rcl/issues/746))
- Fix bug error handling in get\_param\_files ([#743](https://github.com/ros2/rcl/issues/743))
- Complete subscription API test coverage ([#734](https://github.com/ros2/rcl/issues/734))
- increase timeouts in test\_services fixtures for Connext ([#745](https://github.com/ros2/rcl/issues/745))
- Tweaks to client.c and subscription.c for cleaner init/fini ([#728](https://github.com/ros2/rcl/issues/728))
- Improve error checking and handling in subscription APIs ([#739](https://github.com/ros2/rcl/issues/739))
- Add deallocate calls to free strdup allocated memory ([#737](https://github.com/ros2/rcl/issues/737))
- Add missing calls to rcl\_convert\_rmw\_ret\_to\_rcl\_ret ([#738](https://github.com/ros2/rcl/issues/738))
- Add mock tests, publisher 95% coverage ([#732](https://github.com/ros2/rcl/issues/732))
- Restore env variables set in the test\_failing\_configuration. ([#733](https://github.com/ros2/rcl/issues/733))
- Expose qos setting for /rosout ([#722](https://github.com/ros2/rcl/issues/722))
- Reformat rmw\_impl\_id\_check to call a testable function ([#725](https://github.com/ros2/rcl/issues/725))
- Add extra check for invalid event implementation ([#726](https://github.com/ros2/rcl/issues/726))
- Consolidate macro duplication ([#653](https://github.com/ros2/rcl/issues/653))
- Add test for subscription message lost event ([#705](https://github.com/ros2/rcl/issues/705))
- Add function rcl\_event\_is\_valid ([#720](https://github.com/ros2/rcl/issues/720))
- Move actual domain id from node to context ([#718](https://github.com/ros2/rcl/issues/718))
- Removed doxygen warnings ([#712](https://github.com/ros2/rcl/issues/712))
- Remove some dead code.
- Make sure to call rcl\_arguments\_fini at the end of the test.
- Add remap needed null check ([#711](https://github.com/ros2/rcl/issues/711))
- Make public init/fini rosout publisher ([#704](https://github.com/ros2/rcl/issues/704))
- Move rcl\_remap\_copy to public header ([#709](https://github.com/ros2/rcl/issues/709))
- Implement a generic way to change logging levels ([#664](https://github.com/ros2/rcl/issues/664))
- Remove domain\_id and localhost\_only from node\_options ([#708](https://github.com/ros2/rcl/issues/708))
- Add coverage tests ([#703](https://github.com/ros2/rcl/issues/703))
- Add bad arguments tests for coverage ([#698](https://github.com/ros2/rcl/issues/698))
- Remove unused internal prototypes ([#699](https://github.com/ros2/rcl/issues/699))
- Update quality declaration and coverage ([#674](https://github.com/ros2/rcl/issues/674))
- Add setter and getter for domain\_id in rcl\_init\_options\_t ([#678](https://github.com/ros2/rcl/issues/678))
- Remove unused pytest dependency from rcl. ([#695](https://github.com/ros2/rcl/issues/695))
- Fix link to latest API docs ([#692](https://github.com/ros2/rcl/issues/692))
- Keep domain id if ROS\_DOMAIN\_ID is invalid. ([#689](https://github.com/ros2/rcl/issues/689))
- Remove unused check context.c ([#691](https://github.com/ros2/rcl/issues/691))
- Add check rcl\_node\_options\_copy invalid out ([#671](https://github.com/ros2/rcl/issues/671))
- Update tracetools’ QL to 2 in rcl’s QD ([#690](https://github.com/ros2/rcl/issues/690))
- Improve subscription coverage ([#681](https://github.com/ros2/rcl/issues/681))
- Improve rcl timer test coverage ([#680](https://github.com/ros2/rcl/issues/680))
- Improve wait sets test coverage ([#683](https://github.com/ros2/rcl/issues/683))
- Improve rcl init test coverage. ([#684](https://github.com/ros2/rcl/issues/684))
- Improve clock test coverage. ([#685](https://github.com/ros2/rcl/issues/685))
- Add message lost event ([#673](https://github.com/ros2/rcl/issues/673))
- Minor fixes to rcl clock implementation. ([#688](https://github.com/ros2/rcl/issues/688))
- Improve enclave validation test coverage. ([#682](https://github.com/ros2/rcl/issues/682))
- Use RCL\_RET\_\* codes only. ([#686](https://github.com/ros2/rcl/issues/686))
- Fixed doxygen warnings ([#677](https://github.com/ros2/rcl/issues/677))
- Add tests for rcl package ([#668](https://github.com/ros2/rcl/issues/668))
- Remove logging\_external\_interface.h, provided by rcl\_logging\_interface package now ([#676](https://github.com/ros2/rcl/issues/676))
- Print RCL\_LOCALHOST\_ENV\_VAR if error happens via rcutils\_get\_env. ([#672](https://github.com/ros2/rcl/issues/672))
- Contributors: Ada-King, Alejandro Hernández Cordero, Ananya Muddukrishna, Andrea Sorbini, Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Dan Rose, Dirk Thomas, Geoffrey Biggs, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Lei Liu, Michel Hidalgo, Nikolai Morin, Scott K Logan, Stephen Brawner, Thijs Raymakers, brawner, shonigmann, tomoya

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/galactic/rcl_action/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#909](https://github.com/ros2/rcl/issues/909))
- Don’t expect RCL\_RET\_TIMEOUT to set an error string ([#900](https://github.com/ros2/rcl/issues/900))
- Add support for rmw\_connextdds ([#895](https://github.com/ros2/rcl/issues/895))
- Avoid setting error message twice. ([#887](https://github.com/ros2/rcl/issues/887))
- Address various clang static analysis fixes ([#864](https://github.com/ros2/rcl/issues/864))
- Update QDs to QL 1 ([#866](https://github.com/ros2/rcl/issues/866))
- Update QL ([#858](https://github.com/ros2/rcl/issues/858))
- Make sure to always check return values ([#840](https://github.com/ros2/rcl/issues/840))
- Update deprecated gtest macros ([#818](https://github.com/ros2/rcl/issues/818))
- Make sure to check the return value of rcl APIs. ([#838](https://github.com/ros2/rcl/issues/838))
- Update maintainers ([#825](https://github.com/ros2/rcl/issues/825))
- Store reference to rcl\_clock\_t instead of copy ([#797](https://github.com/ros2/rcl/issues/797))
- Use valid clock in case of issue in rcl\_timer\_init ([#795](https://github.com/ros2/rcl/issues/795))
- Add fault injection macros and unit tests to rcl\_action ([#730](https://github.com/ros2/rcl/issues/730))
- Change some EXPECT\_EQ to ASSERT\_EQ in test\_action\_server. ([#759](https://github.com/ros2/rcl/issues/759))
- Removed doxygen warnings ([#712](https://github.com/ros2/rcl/issues/712))
- Address issue 716 by zero initializing pointers and freeing memory ([#717](https://github.com/ros2/rcl/issues/717))
- Update quality declaration and coverage ([#674](https://github.com/ros2/rcl/issues/674))
- Fixed doxygen warnings ([#677](https://github.com/ros2/rcl/issues/677))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Audrow Nash, Chen Lihui, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz, Stephen Brawner, brawner, shonigmann

<a id="rcl-interfaces"></a>

## [rcl\_interfaces](https://github.com/ros2/rcl_interfaces/tree/galactic/rcl_interfaces/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Add field to the parameter description to specify dynamic/static typing. ([#118](https://github.com/ros2/rcl_interfaces/issues/118))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/galactic/rcl_lifecycle/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#909](https://github.com/ros2/rcl/issues/909))
- make rcl\_lifecycle\_com\_interface optional in lifecycle nodes ([#882](https://github.com/ros2/rcl/issues/882))
- Update QDs to QL 1 ([#866](https://github.com/ros2/rcl/issues/866))
- Update QL ([#858](https://github.com/ros2/rcl/issues/858))
- Make sure to always check return values ([#840](https://github.com/ros2/rcl/issues/840))
- Update tracetools QL and add to rcl\_lifecycle’s QD ([#845](https://github.com/ros2/rcl/issues/845))
- Add compiler warnings ([#830](https://github.com/ros2/rcl/issues/830))
- Make sure to check the return value of rcl APIs. ([#838](https://github.com/ros2/rcl/issues/838))
- Add lifecycle node state transition instrumentation ([#804](https://github.com/ros2/rcl/issues/804))
- Update maintainers ([#825](https://github.com/ros2/rcl/issues/825))
- Improve error messages in rcl\_lifecycle ([#742](https://github.com/ros2/rcl/issues/742))
- Fix test\_rcl\_lifecycle ([#788](https://github.com/ros2/rcl/issues/788))
- Add fault injection macros and unit tests to rcl\_lifecycle ([#731](https://github.com/ros2/rcl/issues/731))
- Remove std::cout line from test\_rcl\_lifecycle.cpp ([#773](https://github.com/ros2/rcl/issues/773))
- Set transition\_map->states/transition size to 0 on fini ([#729](https://github.com/ros2/rcl/issues/729))
- Topic fix rcl lifecycle test issue ([#715](https://github.com/ros2/rcl/issues/715))
- Removed doxygen warnings ([#712](https://github.com/ros2/rcl/issues/712))
- Update quality declaration and coverage ([#674](https://github.com/ros2/rcl/issues/674))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Barry Xu, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Karsten Knese, Lei Liu, Stephen Brawner, brawner, shonigmann

<a id="rcl-logging-interface"></a>

## [rcl\_logging\_interface](https://github.com/ros2/rcl_logging/tree/galactic/rcl_logging_interface/CHANGELOG.rst)

- Update QD to QL 1 ([#66](https://github.com/ros2/rcl_logging/issues/66))
- Use rcutils\_expand\_user in rcl\_logging\_get\_logging\_directory ([#59](https://github.com/ros2/rcl_logging/issues/59))
- Allow configuring logging directory through environment variables ([#53](https://github.com/ros2/rcl_logging/issues/53))
- Update the maintainers. ([#55](https://github.com/ros2/rcl_logging/issues/55))
- Add new package with rcl logging interface ([#41](https://github.com/ros2/rcl_logging/issues/41))
- Contributors: Chris Lalancette, Christophe Bedard, Stephen Brawner

<a id="rcl-logging-log4cxx"></a>

## [rcl\_logging\_log4cxx](https://github.com/ros2/rcl_logging/tree/galactic/rcl_logging_log4cxx/CHANGELOG.rst)

- Allow configuring logging directory through environment variables ([#53](https://github.com/ros2/rcl_logging/issues/53))
- Update the maintainers. ([#55](https://github.com/ros2/rcl_logging/issues/55))
- Remove unused pytest dependency. ([#43](https://github.com/ros2/rcl_logging/issues/43))
- Use new package with rcl logging interface ([#41](https://github.com/ros2/rcl_logging/issues/41))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/galactic/rcl_logging_noop/CHANGELOG.rst)

- Make internal dependencies private ([#60](https://github.com/ros2/rcl_logging/issues/60))
- Update the maintainers. ([#55](https://github.com/ros2/rcl_logging/issues/55))
- Remove unused pytest dependency. ([#43](https://github.com/ros2/rcl_logging/issues/43))
- Use new package with rcl logging interface ([#41](https://github.com/ros2/rcl_logging/issues/41))
- Contributors: Chris Lalancette, Shane Loretz

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/galactic/rcl_logging_spdlog/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#73](https://github.com/ros2/rcl_logging/issues/73))
- Include what you use ([#71](https://github.com/ros2/rcl_logging/issues/71))
- Update QD to QL 1 ([#66](https://github.com/ros2/rcl_logging/issues/66))
- Make sure to check return value from external\_initialize. ([#65](https://github.com/ros2/rcl_logging/issues/65))
- updated QD section 3.i and 3ii and spelling error ([#63](https://github.com/ros2/rcl_logging/issues/63))
- rcl\_logging\_spdlog: Increased QL to 2 in QD
- Updated spdlog QL in QD
- Make internal dependencies private ([#60](https://github.com/ros2/rcl_logging/issues/60))
- [rcl\_logging\_spdlog] Add warnings ([#54](https://github.com/ros2/rcl_logging/issues/54))
- Allow configuring logging directory through environment variables ([#53](https://github.com/ros2/rcl_logging/issues/53))
- Update the maintainers. ([#55](https://github.com/ros2/rcl_logging/issues/55))
- Added benchmark test to rcl\_logging\_spdlog ([#52](https://github.com/ros2/rcl_logging/issues/52))
- Used current\_path() function from rcpputils ([#51](https://github.com/ros2/rcl_logging/issues/51))
- Add fault injection unittest to increase coverage ([#49](https://github.com/ros2/rcl_logging/issues/49))
- Bump QD to level 3 and updated QD ([#44](https://github.com/ros2/rcl_logging/issues/44))
- Added Doxyfile and fixed related warnings ([#42](https://github.com/ros2/rcl_logging/issues/42))
- Use new package with rcl logging interface ([#41](https://github.com/ros2/rcl_logging/issues/41))
- Increased test coverage ([#40](https://github.com/ros2/rcl_logging/issues/40))
- Add Security Vulnerability Policy pointing to REP-2006.
- Rename Quality\_Declaration.md -> QUALITY\_DECLARATION.md
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Scott K Logan, Shane Loretz, Stephen Brawner, ahcorde, brawner, shonigmann

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/galactic/rcl_yaml_param_parser/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#909](https://github.com/ros2/rcl/issues/909))
- Enable compiler warnings ([#831](https://github.com/ros2/rcl/issues/831))
- Update QDs to QL 1 ([#866](https://github.com/ros2/rcl/issues/866))
- Rearrange test logic to avoid reference to null ([#862](https://github.com/ros2/rcl/issues/862))
- Update QL ([#858](https://github.com/ros2/rcl/issues/858))
- Make sure to initialize the end\_mark for yaml\_event\_t ([#849](https://github.com/ros2/rcl/issues/849))
- Check for valid node names in parameters files ([#809](https://github.com/ros2/rcl/issues/809))
- Update maintainers ([#825](https://github.com/ros2/rcl/issues/825))
- Updated performance section QD ([#817](https://github.com/ros2/rcl/issues/817))
- Several memory-related fixes for rcl\_variant\_t benchmarks ([#813](https://github.com/ros2/rcl/issues/813))
- Improved rcl\_yaml\_param\_parser benchmark test ([#810](https://github.com/ros2/rcl/issues/810))
- Added benchmark test to rcl\_yaml\_param\_parser ([#803](https://github.com/ros2/rcl/issues/803))
- Remove MAX\_NUM\_PARAMS\_PER\_NODE and MAX\_NUM\_NODE\_ENTRIES limitation. ([#802](https://github.com/ros2/rcl/issues/802))
- Add mocking unit tests for rcl\_yaml\_param\_parser (coverage part 3/3) ([#772](https://github.com/ros2/rcl/issues/772))
- Add fault-injection unit tests (coverage part 2/3) ([#766](https://github.com/ros2/rcl/issues/766))
- Add basic unit tests for refactored functions in rcl\_yaml\_param\_parser (coverage part 1/3) ([#771](https://github.com/ros2/rcl/issues/771))
- Fix yaml parser error when meets .nan (refactor on [#754](https://github.com/ros2/rcl/issues/754)) ([#781](https://github.com/ros2/rcl/issues/781))
- Refactor parser.c for better testability ([#754](https://github.com/ros2/rcl/issues/754))
- Don’t overwrite cur\_ns pointer if reallocation fails ([#780](https://github.com/ros2/rcl/issues/780))
- Fix mem leaks in unit test from 776 ([#779](https://github.com/ros2/rcl/issues/779))
- Fix rcl\_parse\_yaml\_file() error handling. ([#776](https://github.com/ros2/rcl/issues/776))
- Don’t overwrite string\_array pointer on reallocation failure ([#775](https://github.com/ros2/rcl/issues/775))
- Set yaml\_variant values to NULL on finalization ([#765](https://github.com/ros2/rcl/issues/765))
- Remove debugging statements. ([#755](https://github.com/ros2/rcl/issues/755))
- Removed doxygen warnings ([#712](https://github.com/ros2/rcl/issues/712))
- Update quality declaration and coverage ([#674](https://github.com/ros2/rcl/issues/674))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chen Lihui, Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, Stephen Brawner, brawner, shonigmann, tomoya

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/galactic/rclcpp/CHANGELOG.rst)

- Use OnShutdown callback handle instead of OnShutdown callback ([#1639](https://github.com/ros2/rclcpp/issues/1639)) ([#1650](https://github.com/ros2/rclcpp/issues/1650))
- use dynamic\_pointer\_cast to detect allocator mismatch in intra process manager ([#1643](https://github.com/ros2/rclcpp/issues/1643)) ([#1644](https://github.com/ros2/rclcpp/issues/1644))
- Increase cppcheck timeout to 500s ([#1634](https://github.com/ros2/rclcpp/issues/1634))
- Clarify node parameters docs ([#1631](https://github.com/ros2/rclcpp/issues/1631))
- Avoid returning loan when none was obtained. ([#1629](https://github.com/ros2/rclcpp/issues/1629))
- Use a different implementation of mutex two priorities ([#1628](https://github.com/ros2/rclcpp/issues/1628))
- Do not test the value of the history policy when testing the get\_publishers/subscriptions\_info\_by\_topic() methods ([#1626](https://github.com/ros2/rclcpp/issues/1626))
- Check first parameter type and range before calling the user validation callbacks ([#1627](https://github.com/ros2/rclcpp/issues/1627))
- Restore test exception for Connext ([#1625](https://github.com/ros2/rclcpp/issues/1625))
- Fix race condition in TimeSource clock thread setup ([#1623](https://github.com/ros2/rclcpp/issues/1623))
- remove deprecated code which was deprecated in foxy and should be removed in galactic ([#1622](https://github.com/ros2/rclcpp/issues/1622))
- Change index.ros.org -> docs.ros.org. ([#1620](https://github.com/ros2/rclcpp/issues/1620))
- Unique network flows ([#1496](https://github.com/ros2/rclcpp/issues/1496))
- Add spin\_some support to the StaticSingleThreadedExecutor ([#1338](https://github.com/ros2/rclcpp/issues/1338))
- Add publishing instrumentation ([#1600](https://github.com/ros2/rclcpp/issues/1600))
- Create load\_parameters and delete\_parameters methods ([#1596](https://github.com/ros2/rclcpp/issues/1596))
- refactor AnySubscriptionCallback and add/deprecate callback signatures ([#1598](https://github.com/ros2/rclcpp/issues/1598))
- Add generic publisher and generic subscription for serialized messages ([#1452](https://github.com/ros2/rclcpp/issues/1452))
- use context from `node_base\_` for clock executor. ([#1617](https://github.com/ros2/rclcpp/issues/1617))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#1615](https://github.com/ros2/rclcpp/issues/1615))
- Initialize integers in test\_parameter\_event\_handler.cpp to avoid undefined behavior ([#1609](https://github.com/ros2/rclcpp/issues/1609))
- Namespace tracetools C++ functions ([#1608](https://github.com/ros2/rclcpp/issues/1608))
- Revert “Namespace tracetools C++ functions ([#1603](https://github.com/ros2/rclcpp/issues/1603))” ([#1607](https://github.com/ros2/rclcpp/issues/1607))
- Namespace tracetools C++ functions ([#1603](https://github.com/ros2/rclcpp/issues/1603))
- Clock subscription callback group spins in its own thread ([#1556](https://github.com/ros2/rclcpp/issues/1556))
- Remove rmw\_connext\_cpp references. ([#1595](https://github.com/ros2/rclcpp/issues/1595))
- Add API for checking QoS profile compatibility ([#1554](https://github.com/ros2/rclcpp/issues/1554))
- Document misuse of parameters callback ([#1590](https://github.com/ros2/rclcpp/issues/1590))
- use const auto & to iterate over parameters ([#1593](https://github.com/ros2/rclcpp/issues/1593))
- Guard against integer overflow in duration conversion ([#1584](https://github.com/ros2/rclcpp/issues/1584))
- get\_parameters service should return empty if undeclared parameters are allowed ([#1514](https://github.com/ros2/rclcpp/issues/1514))
- Made ‘Context::shutdown\_reason’ function a const function ([#1578](https://github.com/ros2/rclcpp/issues/1578))
- Document design decisions that were made for statically typed parameters ([#1568](https://github.com/ros2/rclcpp/issues/1568))
- Fix doc typo in CallbackGroup constructor ([#1582](https://github.com/ros2/rclcpp/issues/1582))
- Enable qos parameter overrides for the /parameter\_events topic ([#1532](https://github.com/ros2/rclcpp/issues/1532))
- Add support for rmw\_connextdds ([#1574](https://github.com/ros2/rclcpp/issues/1574))
- Remove ‘struct’ from the rcl\_time\_jump\_t. ([#1577](https://github.com/ros2/rclcpp/issues/1577))
- Add tests for declaring statically typed parameters when undeclared parameters are allowed ([#1575](https://github.com/ros2/rclcpp/issues/1575))
- Quiet clang memory leak warning on “DoNotOptimize”. ([#1571](https://github.com/ros2/rclcpp/issues/1571))
- Add ParameterEventsSubscriber class ([#829](https://github.com/ros2/rclcpp/issues/829))
- When a parameter change is rejected, the parameters map shouldn’t be updated. ([#1567](https://github.com/ros2/rclcpp/pull/1567))
- Fix when to throw the NoParameterOverrideProvided exception. ([#1567](https://github.com/ros2/rclcpp/pull/1567))
- Fix SEGV caused by order of destruction of Node sub-interfaces ([#1469](https://github.com/ros2/rclcpp/issues/1469))
- Fix benchmark test failure introduced in [#1522](https://github.com/ros2/rclcpp/issues/1522) ([#1564](https://github.com/ros2/rclcpp/issues/1564))
- Fix documented example in create\_publisher ([#1558](https://github.com/ros2/rclcpp/issues/1558))
- Enforce static parameter types ([#1522](https://github.com/ros2/rclcpp/issues/1522))
- Allow timers to keep up the intended rate in MultiThreadedExecutor ([#1516](https://github.com/ros2/rclcpp/issues/1516))
- Fix UBSAN warnings in any\_subscription\_callback. ([#1551](https://github.com/ros2/rclcpp/issues/1551))
- Fix runtime error: reference binding to null pointer of type ([#1547](https://github.com/ros2/rclcpp/issues/1547))
- Reference test resources directly from source tree ([#1543](https://github.com/ros2/rclcpp/issues/1543))
- clear statistics after window reset ([#1531](https://github.com/ros2/rclcpp/issues/1531)) ([#1535](https://github.com/ros2/rclcpp/issues/1535))
- Fix a minor string error in the topic\_statistics test. ([#1541](https://github.com/ros2/rclcpp/issues/1541))
- Avoid `Resource deadlock avoided` if use intra\_process\_comms ([#1530](https://github.com/ros2/rclcpp/issues/1530))
- Avoid an object copy in parameter\_value.cpp. ([#1538](https://github.com/ros2/rclcpp/issues/1538))
- Assert that the publisher\_list size is 1. ([#1537](https://github.com/ros2/rclcpp/issues/1537))
- Don’t access objects after they have been std::move ([#1536](https://github.com/ros2/rclcpp/issues/1536))
- Update for checking correct variable ([#1534](https://github.com/ros2/rclcpp/issues/1534))
- Destroy msg extracted from LoanedMessage. ([#1305](https://github.com/ros2/rclcpp/issues/1305))
- Add instrumentation for linking a timer to a node ([#1500](https://github.com/ros2/rclcpp/issues/1500))
- Fix error when using IPC with StaticSingleThreadExecutor ([#1520](https://github.com/ros2/rclcpp/issues/1520))
- Change to using unique\_ptrs for DummyExecutor. ([#1517](https://github.com/ros2/rclcpp/issues/1517))
- Allow reconfiguring ‘clock’ topic qos ([#1512](https://github.com/ros2/rclcpp/issues/1512))
- Allow to add/remove nodes thread safely in rclcpp::Executor ([#1505](https://github.com/ros2/rclcpp/issues/1505))
- Call rclcpp::shutdown in test\_node for clean shutdown on Windows ([#1515](https://github.com/ros2/rclcpp/issues/1515))
- Reapply “Add get\_logging\_directory method to rclcpp::Logger ([#1509](https://github.com/ros2/rclcpp/issues/1509))” ([#1513](https://github.com/ros2/rclcpp/issues/1513))
- use describe\_parameters of parameter client for test ([#1499](https://github.com/ros2/rclcpp/issues/1499))
- Revert “Add get\_logging\_directory method to rclcpp::Logger ([#1509](https://github.com/ros2/rclcpp/issues/1509))” ([#1511](https://github.com/ros2/rclcpp/issues/1511))
- Add get\_logging\_directory method to rclcpp::Logger ([#1509](https://github.com/ros2/rclcpp/issues/1509))
- Better documentation for the QoS class ([#1508](https://github.com/ros2/rclcpp/issues/1508))
- Modify excluding callback duration from topic statistics ([#1492](https://github.com/ros2/rclcpp/issues/1492))
- Make the test of graph users more robust. ([#1504](https://github.com/ros2/rclcpp/issues/1504))
- Make sure to wait for graph change events in test\_node\_graph. ([#1503](https://github.com/ros2/rclcpp/issues/1503))
- add timeout to SyncParametersClient methods ([#1493](https://github.com/ros2/rclcpp/issues/1493))
- Fix wrong test expectations ([#1497](https://github.com/ros2/rclcpp/issues/1497))
- Update create\_publisher/subscription documentation, clarifying when a parameters interface is required ([#1494](https://github.com/ros2/rclcpp/issues/1494))
- Fix string literal warnings ([#1442](https://github.com/ros2/rclcpp/issues/1442))
- support describe\_parameters methods to parameter client. ([#1453](https://github.com/ros2/rclcpp/issues/1453))
- Add getters to rclcpp::qos and rclcpp::Policy enum classes ([#1467](https://github.com/ros2/rclcpp/issues/1467))
- Change nullptr checks to use ASSERT\_TRUE. ([#1486](https://github.com/ros2/rclcpp/issues/1486))
- Adjust logic around finding and erasing guard\_condition ([#1474](https://github.com/ros2/rclcpp/issues/1474))
- Update QDs to QL 1 ([#1477](https://github.com/ros2/rclcpp/issues/1477))
- Add performance tests for parameter transport ([#1463](https://github.com/ros2/rclcpp/issues/1463))
- Move ownership of shutdown\_guard\_condition to executors/graph\_listener ([#1404](https://github.com/ros2/rclcpp/issues/1404))
- Add options to automatically declare qos parameters when creating a publisher/subscription ([#1465](https://github.com/ros2/rclcpp/issues/1465))
- Add `take_data` to `Waitable` and `data` to `AnyExecutable` ([#1241](https://github.com/ros2/rclcpp/issues/1241))
- Add benchmarks for node parameters interface ([#1444](https://github.com/ros2/rclcpp/issues/1444))
- Remove allocation from executor::remove\_node() ([#1448](https://github.com/ros2/rclcpp/issues/1448))
- Fix test crashes on CentOS 7 ([#1449](https://github.com/ros2/rclcpp/issues/1449))
- Bump rclcpp packages to Quality Level 2 ([#1445](https://github.com/ros2/rclcpp/issues/1445))
- Added executor benchmark tests ([#1413](https://github.com/ros2/rclcpp/issues/1413))
- Add fully-qualified namespace to WeakCallbackGroupsToNodesMap ([#1435](https://github.com/ros2/rclcpp/issues/1435))
- Deprecate Duration(rcl\_duration\_value\_t) in favor of static Duration::from\_nanoseconds(rcl\_duration\_value\_t) ([#1432](https://github.com/ros2/rclcpp/issues/1432))
- Avoid parsing arguments twice in `rclcpp::init_and_remove_ros_arguments` ([#1415](https://github.com/ros2/rclcpp/issues/1415))
- Add service and client benchmarks ([#1425](https://github.com/ros2/rclcpp/issues/1425))
- Set CMakeLists to only use default rmw for benchmarks ([#1427](https://github.com/ros2/rclcpp/issues/1427))
- Update tracetools’ QL in rclcpp’s QD ([#1428](https://github.com/ros2/rclcpp/issues/1428))
- Add missing locking to the rclcpp\_action::ServerBase. ([#1421](https://github.com/ros2/rclcpp/issues/1421))
- Initial benchmark tests for rclcpp::init/shutdown create/destroy node ([#1411](https://github.com/ros2/rclcpp/issues/1411))
- Refactor test CMakeLists in prep for benchmarks ([#1422](https://github.com/ros2/rclcpp/issues/1422))
- Add methods in topic and service interface to resolve a name ([#1410](https://github.com/ros2/rclcpp/issues/1410))
- Update deprecated gtest macros ([#1370](https://github.com/ros2/rclcpp/issues/1370))
- Clear members for StaticExecutorEntitiesCollector to avoid shared\_ptr dependency ([#1303](https://github.com/ros2/rclcpp/issues/1303))
- Increase test timeouts of slow running tests with rmw\_connext\_cpp ([#1400](https://github.com/ros2/rclcpp/issues/1400))
- Avoid self dependency that not destoryed ([#1301](https://github.com/ros2/rclcpp/issues/1301))
- Update maintainers ([#1384](https://github.com/ros2/rclcpp/issues/1384))
- Add clock qos to node options ([#1375](https://github.com/ros2/rclcpp/issues/1375))
- Fix NodeOptions copy constructor ([#1376](https://github.com/ros2/rclcpp/issues/1376))
- Make sure to clean the external client/service handle. ([#1296](https://github.com/ros2/rclcpp/issues/1296))
- Increase coverage of WaitSetTemplate ([#1368](https://github.com/ros2/rclcpp/issues/1368))
- Increase coverage of guard\_condition.cpp to 100% ([#1369](https://github.com/ros2/rclcpp/issues/1369))
- Add coverage statement ([#1367](https://github.com/ros2/rclcpp/issues/1367))
- Tests for LoanedMessage with mocked loaned message publisher ([#1366](https://github.com/ros2/rclcpp/issues/1366))
- Add unit tests for qos and qos\_event files ([#1352](https://github.com/ros2/rclcpp/issues/1352))
- Finish coverage of publisher API ([#1365](https://github.com/ros2/rclcpp/issues/1365))
- Finish API coverage on executors. ([#1364](https://github.com/ros2/rclcpp/issues/1364))
- Add test for ParameterService ([#1355](https://github.com/ros2/rclcpp/issues/1355))
- Add time API coverage tests ([#1347](https://github.com/ros2/rclcpp/issues/1347))
- Add timer coverage tests ([#1363](https://github.com/ros2/rclcpp/issues/1363))
- Add in additional tests for parameter\_client.cpp coverage.
- Minor fixes to the parameter\_service.cpp file.
- reset rcl\_context shared\_ptr after calling rcl\_init sucessfully ([#1357](https://github.com/ros2/rclcpp/issues/1357))
- Improved test publisher - zero qos history depth value exception ([#1360](https://github.com/ros2/rclcpp/issues/1360))
- Covered resolve\_use\_intra\_process ([#1359](https://github.com/ros2/rclcpp/issues/1359))
- Improve test\_subscription\_options ([#1358](https://github.com/ros2/rclcpp/issues/1358))
- Add in more tests for init\_options coverage. ([#1353](https://github.com/ros2/rclcpp/issues/1353))
- Test the remaining node public API ([#1342](https://github.com/ros2/rclcpp/issues/1342))
- Complete coverage of Parameter and ParameterValue API ([#1344](https://github.com/ros2/rclcpp/issues/1344))
- Add in more tests for the utilities. ([#1349](https://github.com/ros2/rclcpp/issues/1349))
- Add in two more tests for expand\_topic\_or\_service\_name. ([#1350](https://github.com/ros2/rclcpp/issues/1350))
- Add tests for node\_options API ([#1343](https://github.com/ros2/rclcpp/issues/1343))
- Add in more coverage for expand\_topic\_or\_service\_name. ([#1346](https://github.com/ros2/rclcpp/issues/1346))
- Test exception in spin\_until\_future\_complete. ([#1345](https://github.com/ros2/rclcpp/issues/1345))
- Add coverage tests graph\_listener ([#1330](https://github.com/ros2/rclcpp/issues/1330))
- Add in unit tests for the Executor class.
- Allow mimick patching of methods with up to 9 arguments.
- Improve the error messages in the Executor class.
- Add coverage for client API ([#1329](https://github.com/ros2/rclcpp/issues/1329))
- Increase service coverage ([#1332](https://github.com/ros2/rclcpp/issues/1332))
- Make more of the static entity collector API private.
- Const-ify more of the static executor.
- Add more tests for the static single threaded executor.
- Many more tests for the static\_executor\_entities\_collector.
- Get one more line of code coverage in memory\_strategy.cpp
- Bugfix when adding callback group.
- Fix typos in comments.
- Remove deprecated executor::FutureReturnCode APIs. ([#1327](https://github.com/ros2/rclcpp/issues/1327))
- Increase coverage of publisher/subscription API ([#1325](https://github.com/ros2/rclcpp/issues/1325))
- Not finalize guard condition while destructing SubscriptionIntraProcess ([#1307](https://github.com/ros2/rclcpp/issues/1307))
- Expose qos setting for /rosout ([#1247](https://github.com/ros2/rclcpp/issues/1247))
- Add coverage for missing API (except executors) ([#1326](https://github.com/ros2/rclcpp/issues/1326))
- Include topic name in QoS mismatch warning messages ([#1286](https://github.com/ros2/rclcpp/issues/1286))
- Add coverage tests context functions ([#1321](https://github.com/ros2/rclcpp/issues/1321))
- Increase coverage of node\_interfaces, including with mocking rcl errors ([#1322](https://github.com/ros2/rclcpp/issues/1322))
- Make node\_graph::count\_graph\_users() const ([#1320](https://github.com/ros2/rclcpp/issues/1320))
- Add coverage for wait\_set\_policies ([#1316](https://github.com/ros2/rclcpp/issues/1316))
- Only exchange intra\_process waitable if nonnull ([#1317](https://github.com/ros2/rclcpp/issues/1317))
- Check waitable for nullptr during constructor ([#1315](https://github.com/ros2/rclcpp/issues/1315))
- Call vector.erase with end iterator overload ([#1314](https://github.com/ros2/rclcpp/issues/1314))
- Use best effort, keep last, history depth 1 QoS Profile for ‘/clock’ subscriptions ([#1312](https://github.com/ros2/rclcpp/issues/1312))
- Add tests type\_support module ([#1308](https://github.com/ros2/rclcpp/issues/1308))
- Replace std\_msgs with test\_msgs in executors test ([#1310](https://github.com/ros2/rclcpp/issues/1310))
- Add set\_level for rclcpp::Logger ([#1284](https://github.com/ros2/rclcpp/issues/1284))
- Remove unused private function (rclcpp::Node and rclcpp\_lifecycle::Node) ([#1294](https://github.com/ros2/rclcpp/issues/1294))
- Adding tests basic getters ([#1291](https://github.com/ros2/rclcpp/issues/1291))
- Adding callback groups in executor ([#1218](https://github.com/ros2/rclcpp/issues/1218))
- Refactor Subscription Topic Statistics Tests ([#1281](https://github.com/ros2/rclcpp/issues/1281))
- Add operator!= for duration ([#1236](https://github.com/ros2/rclcpp/issues/1236))
- Fix clock thread issue ([#1266](https://github.com/ros2/rclcpp/issues/1266)) ([#1267](https://github.com/ros2/rclcpp/issues/1267))
- Fix topic stats test, wait for more messages, only check the ones with samples ([#1274](https://github.com/ros2/rclcpp/issues/1274))
- Add get\_domain\_id method to rclcpp::Context ([#1271](https://github.com/ros2/rclcpp/issues/1271))
- Fixes for unit tests that fail under cyclonedds ([#1270](https://github.com/ros2/rclcpp/issues/1270))
- initialize\_logging\_ should be copied ([#1272](https://github.com/ros2/rclcpp/issues/1272))
- Use static\_cast instead of C-style cast for instrumentation ([#1263](https://github.com/ros2/rclcpp/issues/1263))
- Make parameter clients use template constructors ([#1249](https://github.com/ros2/rclcpp/issues/1249))
- Ability to configure domain\_id via InitOptions. ([#1165](https://github.com/ros2/rclcpp/issues/1165))
- Simplify and fix allocator memory strategy unit test for connext ([#1252](https://github.com/ros2/rclcpp/issues/1252))
- Use global namespace for parameter events subscription topic ([#1257](https://github.com/ros2/rclcpp/issues/1257))
- Increase timeouts for connext for long tests ([#1253](https://github.com/ros2/rclcpp/issues/1253))
- Adjust test\_static\_executor\_entities\_collector for rmw\_connext\_cpp ([#1251](https://github.com/ros2/rclcpp/issues/1251))
- Fix failing test with Connext since it doesn’t wait for discovery ([#1246](https://github.com/ros2/rclcpp/issues/1246))
- Fix node graph test with Connext and CycloneDDS returning actual data ([#1245](https://github.com/ros2/rclcpp/issues/1245))
- Warn about unused result of add\_on\_set\_parameters\_callback ([#1238](https://github.com/ros2/rclcpp/issues/1238))
- Unittests for memory strategy files, except allocator\_memory\_strategy ([#1189](https://github.com/ros2/rclcpp/issues/1189))
- EXPECT\_THROW\_EQ and ASSERT\_THROW\_EQ macros for unittests ([#1232](https://github.com/ros2/rclcpp/issues/1232))
- Add unit test for static\_executor\_entities\_collector ([#1221](https://github.com/ros2/rclcpp/issues/1221))
- Parameterize test executors for all executor types ([#1222](https://github.com/ros2/rclcpp/issues/1222))
- Unit tests for allocator\_memory\_strategy.cpp part 2 ([#1198](https://github.com/ros2/rclcpp/issues/1198))
- Unit tests for allocator\_memory\_strategy.hpp ([#1197](https://github.com/ros2/rclcpp/issues/1197))
- Derive and throw exception in spin\_some spin\_all for StaticSingleThreadedExecutor ([#1220](https://github.com/ros2/rclcpp/issues/1220))
- Make ring buffer thread-safe ([#1213](https://github.com/ros2/rclcpp/issues/1213))
- Add missing RCLCPP\_PUBLIC to ~StaticExecutorEntitiesCollector ([#1227](https://github.com/ros2/rclcpp/issues/1227))
- Document graph functions don’t apply remap rules ([#1225](https://github.com/ros2/rclcpp/issues/1225))
- Remove recreation of entities\_collector ([#1217](https://github.com/ros2/rclcpp/issues/1217))
- Fix rclcpp::NodeOptions::operator= ([#1211](https://github.com/ros2/rclcpp/issues/1211))
- Link against thread library where necessary ([#1210](https://github.com/ros2/rclcpp/issues/1210))
- Unit tests for node interfaces ([#1202](https://github.com/ros2/rclcpp/issues/1202))
- Remove usage of domain id in node options ([#1205](https://github.com/ros2/rclcpp/issues/1205))
- Remove deprecated set\_on\_parameters\_set\_callback function ([#1199](https://github.com/ros2/rclcpp/issues/1199))
- Fix conversion of negative durations to messages ([#1188](https://github.com/ros2/rclcpp/issues/1188))
- Fix implementation of NodeOptions::use\_global\_arguments() ([#1176](https://github.com/ros2/rclcpp/issues/1176))
- Bump to QD to level 3 and fixed links ([#1158](https://github.com/ros2/rclcpp/issues/1158))
- Fix pub/sub count API tests ([#1203](https://github.com/ros2/rclcpp/issues/1203))
- Update tracetools’ QL to 2 in rclcpp’s QD ([#1187](https://github.com/ros2/rclcpp/issues/1187))
- Fix exception message on rcl\_clock\_init ([#1182](https://github.com/ros2/rclcpp/issues/1182))
- Throw exception if rcl\_timer\_init fails ([#1179](https://github.com/ros2/rclcpp/issues/1179))
- Unit tests for some header-only functions/classes ([#1181](https://github.com/ros2/rclcpp/issues/1181))
- Callback should be perfectly-forwarded ([#1183](https://github.com/ros2/rclcpp/issues/1183))
- Add unit tests for logging functionality ([#1184](https://github.com/ros2/rclcpp/issues/1184))
- Add create\_publisher include to create\_subscription ([#1180](https://github.com/ros2/rclcpp/issues/1180))
- Check period duration in create\_wall\_timer ([#1178](https://github.com/ros2/rclcpp/issues/1178))
- Fix get\_node\_time\_source\_interface() docstring ([#988](https://github.com/ros2/rclcpp/issues/988))
- Add message lost subscription event ([#1164](https://github.com/ros2/rclcpp/issues/1164))
- Add spin\_all method to Executor ([#1156](https://github.com/ros2/rclcpp/issues/1156))
- Reorganize test directory and split CMakeLists.txt ([#1173](https://github.com/ros2/rclcpp/issues/1173))
- Check if context is valid when looping in spin\_some ([#1167](https://github.com/ros2/rclcpp/issues/1167))
- Add check for invalid topic statistics publish period ([#1151](https://github.com/ros2/rclcpp/issues/1151))
- Fix spin\_until\_future\_complete: check spinning value ([#1023](https://github.com/ros2/rclcpp/issues/1023))
- Fix doxygen warnings ([#1163](https://github.com/ros2/rclcpp/issues/1163))
- Fix reference to rclcpp in its Quality declaration ([#1161](https://github.com/ros2/rclcpp/issues/1161))
- Allow spin\_until\_future\_complete to accept any future like object ([#1113](https://github.com/ros2/rclcpp/issues/1113))
- Contributors: Ada-King, Alejandro Hernández Cordero, Ananya Muddukrishna, Andrea Sorbini, Audrow Nash, Barry Xu, BriceRenaudeau, Chen Lihui, Chris Lalancette, Christophe Bedard, Claire Wang, Colin MacKenzie, Daisuke Sato, Devin Bonnie, Dirk Thomas, DongheeYe, Ivan Santiago Paunovic, Jacob Perron, Jannik Abbenseth, Johannes Meyer, Jorge Perez, Karsten Knese, Louise Poubel, Miaofei Mei, Michel Hidalgo, Miguel Company, Morgan Quigley, Nikolai Morin, Pedro Pena, Sarthak Mittal, Scott K Logan, Shane Loretz, Stephen Brawner, Steven! Ragnarök, Tomoya Fujita, William Woodall, anaelle-sw, bpwilcox, brawner, eboasson, hsgwa, mauropasse, shonigmann, suab321321, tomoya

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/galactic/rclcpp_action/CHANGELOG.rst)

- Returns CancelResponse::REJECT while goal handle failed to transit to CANCELING state ([#1641](https://github.com/ros2/rclcpp/issues/1641)) ([#1653](https://github.com/ros2/rclcpp/issues/1653))
- Fix action server deadlock issue that caused by other mutexes locked in CancelCallback ([#1635](https://github.com/ros2/rclcpp/issues/1635)) ([#1646](https://github.com/ros2/rclcpp/issues/1646))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#1615](https://github.com/ros2/rclcpp/issues/1615))
- Add support for rmw\_connextdds ([#1574](https://github.com/ros2/rclcpp/issues/1574))
- node\_handle must be destroyed after client\_handle to prevent memory leak ([#1562](https://github.com/ros2/rclcpp/issues/1562))
- Finalize rcl\_handle to prevent leak ([#1528](https://github.com/ros2/rclcpp/issues/1528)) ([#1529](https://github.com/ros2/rclcpp/issues/1529))
- Fix [#1526](https://github.com/ros2/rclcpp/issues/1526). ([#1527](https://github.com/ros2/rclcpp/issues/1527))
- Fix action server deadlock ([#1285](https://github.com/ros2/rclcpp/issues/1285)) ([#1313](https://github.com/ros2/rclcpp/issues/1313))
- Goal response callback compatibility shim with deprecation of old signature ([#1495](https://github.com/ros2/rclcpp/issues/1495))
- [rclcpp\_action] Add warnings ([#1405](https://github.com/ros2/rclcpp/issues/1405))
- Update QDs to QL 1 ([#1477](https://github.com/ros2/rclcpp/issues/1477))
- Add `take_data` to `Waitable` and `data` to `AnyExecutable` ([#1241](https://github.com/ros2/rclcpp/issues/1241))
- Fix test crashes on CentOS 7 ([#1449](https://github.com/ros2/rclcpp/issues/1449))
- Bump rclcpp packages to Quality Level 2 ([#1445](https://github.com/ros2/rclcpp/issues/1445))
- Add rclcpp\_action action\_server benchmarks ([#1433](https://github.com/ros2/rclcpp/issues/1433))
- Benchmark rclcpp\_action action\_client ([#1429](https://github.com/ros2/rclcpp/issues/1429))
- Add missing locking to the rclcpp\_action::ServerBase. ([#1421](https://github.com/ros2/rclcpp/issues/1421))
- Increase test timeouts of slow running tests with rmw\_connext\_cpp ([#1400](https://github.com/ros2/rclcpp/issues/1400))
- Update maintainers ([#1384](https://github.com/ros2/rclcpp/issues/1384))
- Increase coverage rclcpp\_action to 95% ([#1290](https://github.com/ros2/rclcpp/issues/1290))
- Pass goal handle to goal response callback instead of a future ([#1311](https://github.com/ros2/rclcpp/issues/1311))
- Remove deprecated client goal handle method for getting result ([#1309](https://github.com/ros2/rclcpp/issues/1309))
- Increase test timeout necessary for Connext ([#1256](https://github.com/ros2/rclcpp/issues/1256))
- Bump to QD to level 3 and fixed links ([#1158](https://github.com/ros2/rclcpp/issues/1158))
- Add rcl\_action\_client\_options when creating action client. ([#1133](https://github.com/ros2/rclcpp/issues/1133))
- Fix doxygen warnings ([#1163](https://github.com/ros2/rclcpp/issues/1163))
- Increase rclcpp\_action test coverage ([#1153](https://github.com/ros2/rclcpp/issues/1153))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Audrow Nash, Chris Lalancette, Daisuke Sato, Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Kaven Yau, Louise Poubel, Michel Hidalgo, Stephen Brawner, Tomoya Fujita, William Woodall, brawner, shonigmann, tomoya, y-okumura-isp

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/galactic/rclcpp_components/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#1615](https://github.com/ros2/rclcpp/issues/1615))
- Use std compliant non-method std::filesystem::exists function ([#1502](https://github.com/ros2/rclcpp/issues/1502))
- Fix string literal warnings ([#1442](https://github.com/ros2/rclcpp/issues/1442))
- Update QDs to QL 1 ([#1477](https://github.com/ros2/rclcpp/issues/1477))
- Add benchmarks for components ([#1476](https://github.com/ros2/rclcpp/issues/1476))
- Bump rclcpp packages to Quality Level 2 ([#1445](https://github.com/ros2/rclcpp/issues/1445))
- Update maintainers ([#1384](https://github.com/ros2/rclcpp/issues/1384))
- ComponentManager: switch off parameter services and event publisher ([#1333](https://github.com/ros2/rclcpp/issues/1333))
- Bump to QD to level 3 and fixed links ([#1158](https://github.com/ros2/rclcpp/issues/1158))
- Include original exception in ComponentManagerException ([#1157](https://github.com/ros2/rclcpp/issues/1157))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Ivan Santiago Paunovic, Josh Langsfeld, Louise Poubel, Martijn Buijs, Scott K Logan, Stephen Brawner, Tomoya Fujita, shonigmann

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/galactic/rclcpp_lifecycle/CHANGELOG.rst)

- Add generic publisher and generic subscription for serialized messages ([#1452](https://github.com/ros2/rclcpp/issues/1452))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#1615](https://github.com/ros2/rclcpp/issues/1615))
- Fix flaky lifecycle node tests ([#1606](https://github.com/ros2/rclcpp/issues/1606))
- Clock subscription callback group spins in its own thread ([#1556](https://github.com/ros2/rclcpp/issues/1556))
- Delete debug messages ([#1602](https://github.com/ros2/rclcpp/issues/1602))
- add automatically\_add\_executor\_with\_node option ([#1594](https://github.com/ros2/rclcpp/issues/1594))
- make rcl\_lifecyle\_com\_interface optional in lifecycle nodes ([#1507](https://github.com/ros2/rclcpp/issues/1507))
- Add support for rmw\_connextdds ([#1574](https://github.com/ros2/rclcpp/issues/1574))
- Fix SEGV caused by order of destruction of Node sub-interfaces ([#1469](https://github.com/ros2/rclcpp/issues/1469))
- Enforce static parameter types ([#1522](https://github.com/ros2/rclcpp/issues/1522))
- add LifecycleNode::get\_transition\_graph to match services. ([#1472](https://github.com/ros2/rclcpp/issues/1472))
- Update QDs to QL 1 ([#1477](https://github.com/ros2/rclcpp/issues/1477))
- Benchmark lifecycle features ([#1462](https://github.com/ros2/rclcpp/issues/1462))
- Reserve vector capacities and use emplace\_back for constructing vectors ([#1464](https://github.com/ros2/rclcpp/issues/1464))
- [rclcpp\_lifecycle] Change uint8\_t iterator variables to size\_t ([#1461](https://github.com/ros2/rclcpp/issues/1461))
- Bump rclcpp packages to Quality Level 2 ([#1445](https://github.com/ros2/rclcpp/issues/1445))
- Increase test timeouts of slow running tests with rmw\_connext\_cpp ([#1400](https://github.com/ros2/rclcpp/issues/1400))
- Update maintainers ([#1384](https://github.com/ros2/rclcpp/issues/1384))
- Add clock qos to node options ([#1375](https://github.com/ros2/rclcpp/issues/1375))
- Increase test coverage of rclcpp\_lifecycle to 96% ([#1298](https://github.com/ros2/rclcpp/issues/1298))
- Log error instead of throwing exception in Transition and State reset(), mark no except ([#1297](https://github.com/ros2/rclcpp/issues/1297))
- Remove unused private function (rclcpp::Node and rclcpp\_lifecycle::Node) ([#1294](https://github.com/ros2/rclcpp/issues/1294))
- Remove rmw-dependent unit-test checks ([#1293](https://github.com/ros2/rclcpp/issues/1293))
- Added missing tests for rclcpp lifecycle ([#1240](https://github.com/ros2/rclcpp/issues/1240))
- Warn about unused result of add\_on\_set\_parameters\_callback ([#1238](https://github.com/ros2/rclcpp/issues/1238))
- Remove deprecated set\_on\_parameters\_set\_callback function ([#1199](https://github.com/ros2/rclcpp/issues/1199))
- Bump to QD to level 3 and fixed links ([#1158](https://github.com/ros2/rclcpp/issues/1158))
- Fix race in test\_lifecycle\_service\_client ([#1204](https://github.com/ros2/rclcpp/issues/1204))
- Fix doxygen warnings ([#1163](https://github.com/ros2/rclcpp/issues/1163))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, BriceRenaudeau, Claire Wang, Colin MacKenzie, Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Karsten Knese, Louise Poubel, Nikolai Morin, Stephen Brawner, anaelle-sw, brawner, shonigmann, tomoya

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/galactic/rclpy/CHANGELOG.rst)

- Break log function execution ASAP if configured severity is too high ([#776](https://github.com/ros2/rclpy/issues/776)) ([#783](https://github.com/ros2/rclpy/issues/783))
- typo fix. ([#768](https://github.com/ros2/rclpy/issues/768))
- Restore exceptions for Connext and message timestamps on Windows ([#765](https://github.com/ros2/rclpy/issues/765))
- Use correct type when creating test publisher ([#764](https://github.com/ros2/rclpy/issues/764))
- Add a test for destroy\_node while spinning ([#663](https://github.com/ros2/rclpy/issues/663))
- Add \_\_enter\_\_ and \_\_exit\_\_ to Waitable ([#761](https://github.com/ros2/rclpy/issues/761))
- Check if shutdown callback weak method is valid before calling it ([#754](https://github.com/ros2/rclpy/issues/754))
- Change index.ros.org -> docs.ros.org. ([#755](https://github.com/ros2/rclpy/issues/755))
- Use py::class\_ for rcl\_event\_t ([#750](https://github.com/ros2/rclpy/issues/750))
- Convert Clock to use a C++ Class ([#749](https://github.com/ros2/rclpy/issues/749))
- Convert Service to use C++ Class ([#747](https://github.com/ros2/rclpy/issues/747))
- Fix windows warning by using consistent types ([#753](https://github.com/ros2/rclpy/issues/753))
- Use py::class\_ for rmw\_service\_info\_t and rmw\_request\_id\_t ([#748](https://github.com/ros2/rclpy/issues/748))
- Convert Timer to use a C++ Class ([#745](https://github.com/ros2/rclpy/issues/745))
- Add PythonAllocator ([#746](https://github.com/ros2/rclpy/issues/746))
- Use py::class\_ for rmw\_qos\_profile\_t ([#741](https://github.com/ros2/rclpy/issues/741))
- Combine pybind11 modules into one ([#743](https://github.com/ros2/rclpy/issues/743))
- Use py::class\_ for rcl\_duration\_t ([#744](https://github.com/ros2/rclpy/issues/744))
- Fix bug in unique\_ptr type argument ([#742](https://github.com/ros2/rclpy/issues/742))
- Convert Client to use C++ Class ([#739](https://github.com/ros2/rclpy/issues/739))
- Converting last of \_rclpy.c to pybind11 ([#738](https://github.com/ros2/rclpy/issues/738))
- Make sure only non-empty std::vector of arguments are indexed ([#740](https://github.com/ros2/rclpy/issues/740))
- Use py::class\_ for rcl\_time\_point\_t ([#737](https://github.com/ros2/rclpy/issues/737))
- Convert logging mutex functions to pybind11 ([#735](https://github.com/ros2/rclpy/issues/735))
- Document misuse of of parameter callbacks ([#734](https://github.com/ros2/rclpy/issues/734))
- Convert QoS APIs to pybind11 ([#736](https://github.com/ros2/rclpy/issues/736))
- Add API for checking QoS profile compatibility ([#708](https://github.com/ros2/rclpy/issues/708))
- Replace rmw\_connext\_cpp with rmw\_connextdds ([#698](https://github.com/ros2/rclpy/issues/698))
- Convert last of pub/sub getters to pybind11 ([#733](https://github.com/ros2/rclpy/issues/733))
- Pybind 11: count\_subscribers and count\_publishers ([#732](https://github.com/ros2/rclpy/issues/732))
- Convert more node accessors to pybind11 ([#730](https://github.com/ros2/rclpy/issues/730))
- Pybind11-ify rclpy\_get\_node\_parameters ([#718](https://github.com/ros2/rclpy/issues/718))
- Modify parameter service behavior when allow\_undeclared\_parameters is false and the requested parameter doesn’t exist ([#661](https://github.com/ros2/rclpy/issues/661))
- Include pybind11 first to fix windows debug warning ([#731](https://github.com/ros2/rclpy/issues/731))
- Convert init/shutdown to pybind11 ([#715](https://github.com/ros2/rclpy/issues/715))
- Convert take API to pybind11 ([#721](https://github.com/ros2/rclpy/issues/721))
- Migrate qos event APIs to pybind11 ([#723](https://github.com/ros2/rclpy/issues/723))
- Remove pybind11 from rclpy common ([#727](https://github.com/ros2/rclpy/issues/727))
- Look up pybind11 package once ([#726](https://github.com/ros2/rclpy/issues/726))
- typo fix. ([#729](https://github.com/ros2/rclpy/issues/729))
- [pybind11] Node Accessors ([#719](https://github.com/ros2/rclpy/issues/719))
- Convert serialize/deserialize to pybind11 ([#712](https://github.com/ros2/rclpy/issues/712))
- Convert names\_and\_types graph APIs to pybind11 ([#717](https://github.com/ros2/rclpy/issues/717))
- Use Pybind11 for name functions ([#709](https://github.com/ros2/rclpy/issues/709))
- Better checks for valid msg and srv types ([#714](https://github.com/ros2/rclpy/issues/714))
- Convert duration to pybind11 ([#716](https://github.com/ros2/rclpy/issues/716))
- Convert wait\_set functions to pybind11 ([#706](https://github.com/ros2/rclpy/issues/706))
- Explicitly populate tuple with None ([#711](https://github.com/ros2/rclpy/issues/711))
- Change the time jump time type to just rcl\_time\_jump\_t. ([#707](https://github.com/ros2/rclpy/issues/707))
- Convert rclpy service functions to pybind11 ([#703](https://github.com/ros2/rclpy/issues/703))
- Bump the cppcheck timeout by 2 minutes ([#705](https://github.com/ros2/rclpy/issues/705))
- Convert subscription functions to pybind11 ([#696](https://github.com/ros2/rclpy/issues/696))
- Convert rclpy client functions to pybind11 ([#701](https://github.com/ros2/rclpy/issues/701))
- Fix static typing when allow undeclared ([#702](https://github.com/ros2/rclpy/issues/702))
- Convert publisher functions to pybind11 ([#695](https://github.com/ros2/rclpy/issues/695))
- Convert clock and time functions to pybind11 ([#699](https://github.com/ros2/rclpy/issues/699))
- Set destructor on QoS Profile struct ([#700](https://github.com/ros2/rclpy/issues/700))
- Convert timer functions to pybind11 ([#693](https://github.com/ros2/rclpy/issues/693))
- Convert guard conditions functions to pybind11 ([#692](https://github.com/ros2/rclpy/issues/692))
- Convert service info functions to pybind11 ([#694](https://github.com/ros2/rclpy/issues/694))
- Enforce static parameter types when dynamic typing is not specified ([#683](https://github.com/ros2/rclpy/issues/683))
- rclpy\_ok and rclpy\_create\_context to pybind11 ([#691](https://github.com/ros2/rclpy/issues/691))
- Include Pybind11 before Python.h ([#690](https://github.com/ros2/rclpy/issues/690))
- Clean up exceptions in \_rclpy\_action ([#685](https://github.com/ros2/rclpy/issues/685))
- Clean windows flags on \_rclpy\_pybind11 and \_rclpy\_action ([#688](https://github.com/ros2/rclpy/issues/688))
- Use pybind11 for \_rclpy\_handle ([#668](https://github.com/ros2/rclpy/issues/668))
- Split rclpy module for easier porting to pybind11 ([#675](https://github.com/ros2/rclpy/issues/675))
- Use Pybind11 to generate \_rclpy\_logging ([#659](https://github.com/ros2/rclpy/issues/659))
- Copy windows debug fixes for pybind11 ([#681](https://github.com/ros2/rclpy/issues/681))
- Use pybind11 for \_rclpy\_action ([#678](https://github.com/ros2/rclpy/issues/678))
- Update just pycapsule lib to use pybind11 ([#652](https://github.com/ros2/rclpy/issues/652))
- remove maintainer ([#682](https://github.com/ros2/rclpy/issues/682))
- Use Pybind11’s CMake code ([#667](https://github.com/ros2/rclpy/issues/667))
- Don’t call destroy\_node while spinning ([#674](https://github.com/ros2/rclpy/issues/674))
- Check the rcl\_action return value on cleanup. ([#672](https://github.com/ros2/rclpy/issues/672))
- Fix the NULL check for destroy\_ros\_message. ([#677](https://github.com/ros2/rclpy/issues/677))
- Use Py\_XDECREF for pynode\_names\_and\_namespaces ([#673](https://github.com/ros2/rclpy/issues/673))
- Use Py\_XDECREF for pyresult\_list. ([#670](https://github.com/ros2/rclpy/issues/670))
- Fix dead stores. ([#669](https://github.com/ros2/rclpy/issues/669))
- Fix two clang static analysis warnings. ([#664](https://github.com/ros2/rclpy/issues/664))
- Add method to get the current logging directory ([#657](https://github.com/ros2/rclpy/issues/657))
- Fix docstring indent error in create\_node ([#655](https://github.com/ros2/rclpy/issues/655))
- use only True to avoid confusion in autodoc config
- document QoS profile constants
- Merge pull request [#649](https://github.com/ros2/rclpy/issues/649) from ros2/clalancette/dont-except-while-sleep
- Fixes from review/CI.
- Make sure to catch the ROSInterruptException when calling rate.sleep.
- memory leak ([#643](https://github.com/ros2/rclpy/issues/643)) ([#645](https://github.com/ros2/rclpy/issues/645))
- Don’t throw an exception if timer canceled while sleeping.
- Wake executor in Node.create\_subscription() ([#647](https://github.com/ros2/rclpy/issues/647))
- Fix Enum not being comparable with ints in get\_parameter\_types service
- Qos configurability ([#635](https://github.com/ros2/rclpy/issues/635))
- Use Py\_XDECREF for pytopic\_names\_and\_types. ([#638](https://github.com/ros2/rclpy/issues/638))
- qos\_policy\_name\_from\_kind() should accept either a QoSPolicyKind or an int ([#637](https://github.com/ros2/rclpy/issues/637))
- Add method in Node to resolve a topic or service name ([#636](https://github.com/ros2/rclpy/issues/636))
- Deprecate verbose qos policy value names ([#634](https://github.com/ros2/rclpy/issues/634))
- Remove deprecated set\_parameters\_callback ([#633](https://github.com/ros2/rclpy/issues/633))
- Make sure to use Py\_XDECREF in rclpy\_get\_service\_names\_and\_types ([#632](https://github.com/ros2/rclpy/issues/632))
- Update maintainers ([#627](https://github.com/ros2/rclpy/issues/627))
- Add in semicolon on RCUTILS\_LOGGING\_AUTOINIT. ([#624](https://github.com/ros2/rclpy/issues/624))
- Add in the topic name when QoS events are fired. ([#621](https://github.com/ros2/rclpy/issues/621))
- Use best effort, keep last, history depth 1 QoS Profile for ‘/clock’ subscriptions ([#619](https://github.com/ros2/rclpy/issues/619))
- PARAM\_REL\_TOL documentation fix ([#559](https://github.com/ros2/rclpy/issues/559))
- Node get fully qualified name ([#598](https://github.com/ros2/rclpy/issues/598))
- MultiThreadedExecutor spin\_until\_future complete should not continue waiting when the future is done ([#605](https://github.com/ros2/rclpy/issues/605))
- skip test relying on source timestamps with Connext ([#615](https://github.com/ros2/rclpy/issues/615))
- Use the rpyutils shared import\_c\_library function. ([#610](https://github.com/ros2/rclpy/issues/610))
- Add ability to configure domain ID ([#596](https://github.com/ros2/rclpy/issues/596))
- Use absolute parameter events topic name ([#612](https://github.com/ros2/rclpy/issues/612))
- Destroy event handlers owned by publishers/subscriptions when calling publisher.destroy()/subscription.destroy() ([#603](https://github.com/ros2/rclpy/issues/603))
- Default incompatible qos callback should be set when there’s no user specified callback ([#601](https://github.com/ros2/rclpy/issues/601))
- relax rate jitter test for individual periods ([#602](https://github.com/ros2/rclpy/issues/602))
- add QoSProfile.\_\_str\_\_ ([#593](https://github.com/ros2/rclpy/issues/593))
- Add useful debug info when trying to publish the wrong type ([#581](https://github.com/ros2/rclpy/issues/581))
- Pass rcutils\_include\_dirs to cppcheck ([#577](https://github.com/ros2/rclpy/issues/577))
- wrap lines to shorten line length ([#586](https://github.com/ros2/rclpy/issues/586))
- fix moved troubleshooting url ([#579](https://github.com/ros2/rclpy/issues/579))
- improve error message if rclpy C extensions are not found ([#580](https://github.com/ros2/rclpy/issues/580))
- Add message lost subscription event ([#572](https://github.com/ros2/rclpy/issues/572))
- Fix executor behavior on shutdown ([#574](https://github.com/ros2/rclpy/issues/574))
- Add missing rcutils/macros.h header ([#573](https://github.com/ros2/rclpy/issues/573))
- Add `topic_name` property to Subscription ([#571](https://github.com/ros2/rclpy/issues/571))
- Add `topic_name` property to publisher ([#568](https://github.com/ros2/rclpy/issues/568))
- Fix and document rclpy\_handle\_get\_pointer\_from\_capsule() ([#569](https://github.com/ros2/rclpy/issues/569))
- Fix docstrings ([#566](https://github.com/ros2/rclpy/issues/566))
- Contributors: Addisu Z. Taddese, Alejandro Hernández Cordero, Andrea Sorbini, Audrow, Audrow Nash, Barry Xu, Chris Lalancette, Claire Wang, Dereck Wonnacott, Dirk Thomas, Emerson Knapp, Greg Balke, Gökçe Aydos, Ivan Santiago Paunovic, Jacob Perron, Loy, Michel Hidalgo, Scott K Logan, Shane Loretz, Tomoya Fujita, Tully Foote, Zhen Ju, ksuszka, ssumoo, tomoya

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/galactic/CHANGELOG.rst)

- Update quality declaration links ([#130](https://github.com/ros2/rcpputils/issues/130))
- Add functions for getting library path and filename ([#128](https://github.com/ros2/rcpputils/issues/128))
- Add path equality operators ([#127](https://github.com/ros2/rcpputils/issues/127))
- Add create\_temp\_directory filesystem helper ([#126](https://github.com/ros2/rcpputils/issues/126))
- Use new noexcept specifier. ([#123](https://github.com/ros2/rcpputils/issues/123))
- Add stream operator for paths to make it easier to log ([#120](https://github.com/ros2/rcpputils/issues/120))
- Path join operator is const ([#119](https://github.com/ros2/rcpputils/issues/119))
- No windows.h in header files ([#118](https://github.com/ros2/rcpputils/issues/118))
- Fix rcpputils::SharedLibrary tests. ([#117](https://github.com/ros2/rcpputils/issues/117))
- Update QD to QL 1 ([#114](https://github.com/ros2/rcpputils/issues/114))
- Make sure to not try to index into an empty path. ([#113](https://github.com/ros2/rcpputils/issues/113))
- Fix working with filesystem parent paths. ([#112](https://github.com/ros2/rcpputils/issues/112))
- Cleanup mislabeled BSD license ([#37](https://github.com/ros2/rcpputils/issues/37))
- overload functions for has\_symbol and get\_symbol with raw string literal ([#110](https://github.com/ros2/rcpputils/issues/110))
- Add an ASSERT to the pointer traits tests. ([#111](https://github.com/ros2/rcpputils/issues/111))
- replace custom get env login into rcutils\_get\_env(). ([#99](https://github.com/ros2/rcpputils/issues/99))
- Removed Github Actions ([#105](https://github.com/ros2/rcpputils/issues/105))
- Update the package.xml files with the latest Open Robotics maintainers ([#102](https://github.com/ros2/rcpputils/issues/102))
- Make sure that an existing path is a directory for create\_directories ([#98](https://github.com/ros2/rcpputils/issues/98))
- Transfer ownership to Open Robotics ([#100](https://github.com/ros2/rcpputils/issues/100))
- Ensure -fPIC is used when building a static lib ([#93](https://github.com/ros2/rcpputils/issues/93))
- Removed doxygen warnings ([#86](https://github.com/ros2/rcpputils/issues/86)) ([#87](https://github.com/ros2/rcpputils/issues/87))
- Add clamp header ([#85](https://github.com/ros2/rcpputils/issues/85))
- Removed doxygen warnings ([#86](https://github.com/ros2/rcpputils/issues/86))
- Split get\_env\_var() into header and implementation ([#83](https://github.com/ros2/rcpputils/issues/83))
- Add cstring include for strcmp ([#81](https://github.com/ros2/rcpputils/issues/81))
- filesystem helpers: adding remove\_all to remove non-empty directories ([#79](https://github.com/ros2/rcpputils/issues/79))
- Add scope\_exit helper ([#78](https://github.com/ros2/rcpputils/issues/78))
- Bump setup-ros to 0.0.23, action-ros-lint to 0.0.6, action-ros-ci to 0.0.17 ([#77](https://github.com/ros2/rcpputils/issues/77))
- Fix parent\_path() for empty paths and paths of length one ([#73](https://github.com/ros2/rcpputils/issues/73))
- Add get\_executable\_name() function ([#70](https://github.com/ros2/rcpputils/issues/70))
- Address memory leak in remove pointer test ([#72](https://github.com/ros2/rcpputils/issues/72))
- Add current\_path to filesystem\_helpers ([#63](https://github.com/ros2/rcpputils/issues/63))
- Align path combine behavior with C++17 ([#68](https://github.com/ros2/rcpputils/issues/68))
- Update quality declaration to QL 2 ([#71](https://github.com/ros2/rcpputils/issues/71))
- Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris Lalancette, Christophe Bedard, Devin Bonnie, Dirk Thomas, Emerson Knapp, Hunter L. Allen, Ivan Santiago Paunovic, Jacob Perron, Karsten Knese, Louise Poubel, Michael Jeronimo, Michel Hidalgo, Nikolai Morin, Scott K Logan, Simon Honigmann, Stephen Brawner, Tully Foote, Victor Lopez, William Woodall, tomoya

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/galactic/CHANGELOG.rst)

- Declare dependency on libatomic ([#338](https://github.com/ros2/rcutils/issues/338))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#335](https://github.com/ros2/rcutils/issues/335))
- Quiet down a warning in release mode. ([#334](https://github.com/ros2/rcutils/issues/334))
- Make the logging separate char an implementation detail. ([#332](https://github.com/ros2/rcutils/issues/332))
- Performance tests demo ([#288](https://github.com/ros2/rcutils/issues/288))
- Remove references of \_\_xstat ([#330](https://github.com/ros2/rcutils/issues/330))
- Update the documentation to be more consistent. ([#331](https://github.com/ros2/rcutils/issues/331))
- Shorten some excessively long lines of CMake ([#328](https://github.com/ros2/rcutils/issues/328))
- qnx-support: include sys/link.h & avoid using dlinfo ([#327](https://github.com/ros2/rcutils/issues/327))
- QNX uses XSI-compliant ([#326](https://github.com/ros2/rcutils/issues/326))
- Add an API for directory iteration ([#323](https://github.com/ros2/rcutils/issues/323))
- Fix a leak during error handling in dir size calculation ([#324](https://github.com/ros2/rcutils/issues/324))
- Fix rcutils\_shared\_library\_t path on Windows. ([#322](https://github.com/ros2/rcutils/issues/322))
- Check linker flags instead of assuming compiler correlation. ([#321](https://github.com/ros2/rcutils/issues/321))
- Improve shared library relative paths handling ([#320](https://github.com/ros2/rcutils/issues/320))
- Update rcutils\_calculate\_directory\_size() to support recursion ([#306](https://github.com/ros2/rcutils/issues/306))
- Updating QD to QL 1 ([#317](https://github.com/ros2/rcutils/issues/317))
- Address unused return values found in scan-build ([#316](https://github.com/ros2/rcutils/issues/316))
- use one copy for continuous area instead of loop copy ([#312](https://github.com/ros2/rcutils/issues/312))
- use a better way to check whether string is empty ([#315](https://github.com/ros2/rcutils/issues/315))
- Use helper funciton to copy string ([#314](https://github.com/ros2/rcutils/issues/314))
- Disable a Windows platform warning. ([#311](https://github.com/ros2/rcutils/issues/311))
- Fix format of code description on document ([#313](https://github.com/ros2/rcutils/issues/313))
- Make sure to check the return values of rcutils APIs. ([#302](https://github.com/ros2/rcutils/issues/302))
- Add rcutils\_expand\_user() to expand user directory in path ([#298](https://github.com/ros2/rcutils/issues/298))
- Update the maintainers. ([#299](https://github.com/ros2/rcutils/issues/299))
- Remove the temporary variable in RCUTILS\_LOGGING\_AUTOINIT ([#290](https://github.com/ros2/rcutils/issues/290))
- Add RCUTILS\_NO\_FAULT\_INJECTION() macro. ([#295](https://github.com/ros2/rcutils/issues/295))
- Inject faults on rcutils\_get\_env() and rcutils\_set\_env() call. ([#292](https://github.com/ros2/rcutils/issues/292))
- env.h and get\_env.h docblock fixes ([#291](https://github.com/ros2/rcutils/issues/291))
- Introduce rcutils\_strcasecmp, case insensitive string compare. ([#280](https://github.com/ros2/rcutils/issues/280))
- Stop using fprintf to avoid using file handles by changing as few lines of code as possible. ([#289](https://github.com/ros2/rcutils/issues/289))
- Defines QNX implementation for rcutils\_get\_platform\_library\_name ([#287](https://github.com/ros2/rcutils/issues/287))
- Add RCUTILS\_CAN\_SET\_ERROR\_MSG\_AND\_RETURN\_WITH\_ERROR\_OF() macro. ([#284](https://github.com/ros2/rcutils/issues/284)) To fault inject error messages as well as return codes.
- Change rcutils\_fault\_injection\_set\_count to use int64\_t ([#283](https://github.com/ros2/rcutils/issues/283))
- adds QNX support for rcutils\_get\_executable\_name ([#282](https://github.com/ros2/rcutils/issues/282))
- Add fault injection hooks to default allocator ([#277](https://github.com/ros2/rcutils/issues/277))
- Fault injection macros and functionality (plus example) ([#264](https://github.com/ros2/rcutils/issues/264))
- ensure -fPIC is used when building a static lib ([#276](https://github.com/ros2/rcutils/issues/276))
- Drop vsnprintf mocks entirely. ([#275](https://github.com/ros2/rcutils/issues/275)) Binary API is not portable across platforms and compilation config.
- Fix vsnprintf mocks for Release builds. ([#274](https://github.com/ros2/rcutils/issues/274))
- Improve test coverage mocking system calls ([#272](https://github.com/ros2/rcutils/issues/272))
- Use mimick/mimick.h header ([#273](https://github.com/ros2/rcutils/issues/273))
- Add mock test for rcutils/strerror ([#265](https://github.com/ros2/rcutils/issues/265))
- Add compiler option -Wconversion and add explicit casts for conversions that may alter the value or change the sign ([#263](https://github.com/ros2/rcutils/issues/263)) See <https://github.com/ros2/rcutils/pull/263#issuecomment-663252537>.
- Removed doxygen warnings ([#266](https://github.com/ros2/rcutils/issues/266)) ([#268](https://github.com/ros2/rcutils/issues/268))
- Removed doxygen warnings ([#266](https://github.com/ros2/rcutils/issues/266))
- Force \_GNU\_SOURCE if glibc is used. ([#267](https://github.com/ros2/rcutils/issues/267))
- Add parenthesis around the argument in time conversion macros defined in time.h ([#261](https://github.com/ros2/rcutils/issues/261))
- Add token join macros ([#262](https://github.com/ros2/rcutils/issues/262))
- Add rcutils\_string\_array\_sort function ([#248](https://github.com/ros2/rcutils/issues/248))
- Add rcutils\_string\_array\_resize function ([#247](https://github.com/ros2/rcutils/issues/247))
- Increase testing coverage of rcutils to 95% ([#258](https://github.com/ros2/rcutils/issues/258))
- Update QUALITY\_DECLARATION to reflect QL 2 status ([#260](https://github.com/ros2/rcutils/issues/260))
- Update version stability section of quality declaration for 1.0 ([#256](https://github.com/ros2/rcutils/issues/256))
- Contributors: Ahmed Sobhy, Alejandro Hernández Cordero, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Dirk Thomas, Felix Endres, Homalozoa X, Ivan Santiago Paunovic, Johannes Meyer, Jorge Perez, Karsten Knese, Michel Hidalgo, Scott K Logan, Stephen Brawner, Steven! Ragnarök, brawner, shonigmann, tomoya

<a id="resource-retriever"></a>

## [resource\_retriever](https://github.com/ros/resource_retriever/tree/galactic/resource_retriever/CHANGELOG.rst)

- Throw exception if package name is empty ([#54](https://github.com/ros/resource_retriever/issues/54))
- Update maintainers ([#53](https://github.com/ros/resource_retriever/issues/53))
- Add .hpp header and deprecate .h ([#51](https://github.com/ros/resource_retriever/issues/51))
- Add pytest.ini so local tests don’t display warning ([#48](https://github.com/ros/resource_retriever/issues/48))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/galactic/rmw/CHANGELOG.rst)

- Document which QoS policies are correctly read by rmw\_get\_publishers/subscriptions\_info\_by\_topic ([#308](https://github.com/ros2/rmw/issues/308))
- Unique network flows ([#294](https://github.com/ros2/rmw/issues/294))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#307](https://github.com/ros2/rmw/issues/307))
- Introduce RMW\_DURATION\_INFINITE constant and API return value promise ([#301](https://github.com/ros2/rmw/issues/301))
- Add declaration for function to check QoS profile compatibility ([#299](https://github.com/ros2/rmw/issues/299))
- Update the rmw\_take\_sequence documentation. ([#297](https://github.com/ros2/rmw/issues/297))
- Update rmw QD to QL 1 ([#289](https://github.com/ros2/rmw/issues/289))
- Extend rmw\_qos\_policy\_kind\_t, add functions to convert it to/from a string ([#285](https://github.com/ros2/rmw/issues/285))
- Add functions to convert between qos policy values and strings ([#284](https://github.com/ros2/rmw/issues/284))
- Update maintainers ([#282](https://github.com/ros2/rmw/issues/282))
- Update service request/response API documentation ([#279](https://github.com/ros2/rmw/issues/279))
- Update rmw\_get\_serialized\_message\_size docblock ([#281](https://github.com/ros2/rmw/issues/281))
- Update rmw\_service\_server\_is\_available doc ([#280](https://github.com/ros2/rmw/issues/280))
- Update wait and wait sets’ API documentation ([#275](https://github.com/ros2/rmw/issues/275))
- Update graph API documentation ([#272](https://github.com/ros2/rmw/issues/272))
- Update service server/client creation/destruction API documentation. ([#276](https://github.com/ros2/rmw/issues/276))
- Update rmw\_\*\_\*\_allocation return values ([#278](https://github.com/ros2/rmw/issues/278))
- Update gid API documentation ([#274](https://github.com/ros2/rmw/issues/274))
- Do not link against pthread on Android ([#267](https://github.com/ros2/rmw/issues/267))
- Update taking API documentation ([#271](https://github.com/ros2/rmw/issues/271))
- Update publishing API documentation ([#270](https://github.com/ros2/rmw/issues/270))
- Add fault injection macros for use in other packages ([#254](https://github.com/ros2/rmw/issues/254))
- Add bad\_alloc return to topic\_endpoint\_info functions ([#269](https://github.com/ros2/rmw/issues/269))
- Update publisher/subscription matched count API documentation ([#262](https://github.com/ros2/rmw/issues/262))
- Update publisher/subscription QoS query API documentation ([#263](https://github.com/ros2/rmw/issues/263))
- Extend rmw\_serialized\_message\_t tests ([#261](https://github.com/ros2/rmw/issues/261))
- Update serialization/deserialization API documentation ([#258](https://github.com/ros2/rmw/issues/258))
- Update subscription API documentation ([#256](https://github.com/ros2/rmw/issues/256))
- Update publisher creation/destruction API documentation ([#252](https://github.com/ros2/rmw/issues/252))
- Add actual domain id to rmw\_context\_t ([#251](https://github.com/ros2/rmw/issues/251))
- Update node creation/destruction API documentation. ([#249](https://github.com/ros2/rmw/issues/249))
- Correct parameter names to match documentation ([#250](https://github.com/ros2/rmw/issues/250))
- Remove domain\_id and localhost\_only from node API ([#248](https://github.com/ros2/rmw/issues/248))
- Require enclave upon rmw\_init() call. ([#247](https://github.com/ros2/rmw/issues/247))
- Update init/shutdown API documentation. ([#243](https://github.com/ros2/rmw/issues/243))
- Update init options API documentation. ([#244](https://github.com/ros2/rmw/issues/244))
- Add message lost subscription event ([#232](https://github.com/ros2/rmw/issues/232))
- Move statuses definitions to rmw/events\_statuses/\*.h ([#232](https://github.com/ros2/rmw/issues/232))
- Increase rmw testing coverage above 95% ([#238](https://github.com/ros2/rmw/issues/238))
- Handle zero-length names\_and\_types properly ([#239](https://github.com/ros2/rmw/issues/239))
- Add missing RMW\_PUBLIC to security\_options\_set\_root\_path ([#236](https://github.com/ros2/rmw/issues/236))
- Update Quality Declaration for QL 2 ([#233](https://github.com/ros2/rmw/issues/233))
- Add Security Vulnerability Policy pointing to REP-2006. ([#230](https://github.com/ros2/rmw/issues/230))
- Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Ivan Santiago Paunovic, Jacob Perron, Karsten Knese, Michel Hidalgo, Scott K Logan, Stephen Brawner, brawner, shonigmann

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/galactic/rmw_connextdds/CHANGELOG.rst)

- Use rmw\_qos\_profile\_unknown when adding entity to graph ([#28](https://github.com/rticommunity/rmw_connextdds/issues/28))
- Resolve issues identified while investigating [#21](https://github.com/rticommunity/rmw_connextdds/issues/21) ([#22](https://github.com/rticommunity/rmw_connextdds/issues/22))
- Use Rolling in README’s Quick Start
- Improved implementation of client::is\_service\_available for Connext Pro
- Only add request header to typecode with Basic req/rep profile
- Remove commented/unused code
- Avoid topic name validation in get\_info functions
- Reduce shutdown period to 10ms
- Pass HistoryQosPolicy to graph cache
- Reset error string after looking up type support
- Remove DDS-based WaitSet implementation
- Merge pull request [#13](https://github.com/rticommunity/rmw_connextdds/issues/13) from Ericsson/unique\_network\_flows
- Refactor common API
- Update branch `master` to support Rolling only ([#15](https://github.com/rticommunity/rmw_connextdds/issues/15))
- Add ability to override of endpoint qos settings based on topic name.
- Optimize QoS for reliable large data.
- Only trigger data condition if samples were loaned from reader.
- Alternative WaitSet implementation based on C++ std, selectable at compile-time.
- Add `<buildtool_export_depend>` for `ament_cmake`.
- Use default `dds.transport.UDPv4.builtin.ignore_loopback_interface`.
- Renamed environment variables (`RMW_CONNEXT_USE_DEFAULT_PUBLISH_MODE`, `RMW_CONNEXT_LEGACY_RMW_COMPATIBILITY_MODE`).
- Support a list of initial peers via `RMW_CONNEXT_INITIAL_PEERS`.
- Initial release.
- Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago Paunovic, William Woodall

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/galactic/rmw_connextdds_common/CHANGELOG.rst)

- Correctly detect empty messages ([#33](https://github.com/rticommunity/rmw_connextdds/issues/33))
- Use rmw\_qos\_profile\_unknown when adding entity to graph ([#28](https://github.com/rticommunity/rmw_connextdds/issues/28))
- Resolve issues identified while investigating [#21](https://github.com/rticommunity/rmw_connextdds/issues/21) ([#22](https://github.com/rticommunity/rmw_connextdds/issues/22))
- Use Rolling in README’s Quick Start
- Improved implementation of client::is\_service\_available for Connext Pro
- Only add request header to typecode with Basic req/rep profile
- Remove commented/unused code
- Avoid topic name validation in get\_info functions
- Reduce shutdown period to 10ms
- Pass HistoryQosPolicy to graph cache
- Reset error string after looking up type support
- Remove DDS-based WaitSet implementation
- Merge pull request [#13](https://github.com/rticommunity/rmw_connextdds/issues/13) from Ericsson/unique\_network\_flows
- Remove superfluous header inclusion
- Remove conflicting linkage
- Further remove feature-based exclusion
- Remove feature-based exclusion
- Uncrustify
- Refactor common API
- Include required headers if feature is enabled
- Add conditional compilation support
- Prefer more generic file name
- Restrict unique flow endpoint check to versions beyond Foxy
- Indicate missing support for unique network flows
- Update branch `master` to support Rolling only ([#15](https://github.com/rticommunity/rmw_connextdds/issues/15))
- Add ability to override of endpoint qos settings based on topic name (Pro).
- Optimize QoS for reliable large data (Pro).
- Only trigger data condition if samples were loaned from reader.
- Alternative WaitSet implementation based on C++ std, selectable at compile-time.
- Add `<buildtool_export_depend>` for `ament_cmake`.
- Use default `dds.transport.UDPv4.builtin.ignore_loopback_interface`.
- Don’t log an error on WaitSet::wait() timeout.
- Initial release.
- Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago Paunovic, William Woodall

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/galactic/rmw_connextddsmicro/CHANGELOG.rst)

- Use rmw\_qos\_profile\_unknown when adding entity to graph ([#28](https://github.com/rticommunity/rmw_connextdds/issues/28))
- Resolve issues identified while investigating [#21](https://github.com/rticommunity/rmw_connextdds/issues/21) ([#22](https://github.com/rticommunity/rmw_connextdds/issues/22))
- Use Rolling in README’s Quick Start
- Remove commented/unused code
- Avoid topic name validation in get\_info functions
- Pass HistoryQosPolicy to graph cache
- Reset error string after looking up type support
- Remove DDS-based WaitSet implementation
- Merge pull request [#13](https://github.com/rticommunity/rmw_connextdds/issues/13) from Ericsson/unique\_network\_flows
- Refactor common API
- Update branch `master` to support Rolling only ([#15](https://github.com/rticommunity/rmw_connextdds/issues/15))
- Only trigger data condition if samples were loaned from reader.
- Alternative WaitSet implementation based on C++ std, selectable at compile-time.
- Add `<buildtool_export_depend>` for `ament_cmake`.
- Initial release.
- Contributors: Ananya Muddukrishna, Andrea Sorbini, Ivan Santiago Paunovic, William Woodall

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/galactic/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Fix the history depth for KEEP\_ALL. ([#305](https://github.com/ros2/rmw_cyclonedds/issues/305))
- Use the macros from Cyclone DDS to work with sample payload when using SHM ([#300](https://github.com/ros2/rmw_cyclonedds/issues/300))
- Add loaned sample zero-copy API support ([#297](https://github.com/ros2/rmw_cyclonedds/issues/297))
- Indicate missing support for unique network flows ([#282](https://github.com/ros2/rmw_cyclonedds/issues/282))
- Take and return new RMW\_DURATION\_INFINITE correctly ([#288](https://github.com/ros2/rmw_cyclonedds/issues/288))
- Add RMW function to check QoS compatibility ([#286](https://github.com/ros2/rmw_cyclonedds/issues/286))
- Fix use-after-free in error handling bug
- Drop compatibility with ancient cyclone versions
- Update to use Cyclone’s renamed ddsi\_sertype
- Use init-on-first-use for global state ([#275](https://github.com/ros2/rmw_cyclonedds/issues/275))
- Make sure to reset the error when a typesupport can’t be found.
- Switch to using the generic functions for the typesupport handles.
- Handle typesupport errors on fetch. ([#271](https://github.com/ros2/rmw_cyclonedds/issues/271))
- Handle potential divide by 0 ([#267](https://github.com/ros2/rmw_cyclonedds/issues/267))
- Fix incorrect log message(rmw\_fastrtps\_shared\_cpp -> rmw\_cylonedds\_cpp) ([#260](https://github.com/ros2/rmw_cyclonedds/issues/260))
- Update maintainers ([#254](https://github.com/ros2/rmw_cyclonedds/issues/254))
- Change wrong use of %ld to print std::size\_t to %zu
- Return RMW\_RET\_UNSUPPORTED in rmw\_get\_serialized\_message\_size ([#250](https://github.com/ros2/rmw_cyclonedds/issues/250))
- Update service/client request/response API error returns ([#249](https://github.com/ros2/rmw_cyclonedds/issues/249))
- Updated publisher/subscription allocation and wait set API return codes ([#246](https://github.com/ros2/rmw_cyclonedds/issues/246))
- Fix array `get_function` semantics ([#248](https://github.com/ros2/rmw_cyclonedds/issues/248))
- Update service/client construction/destruction API return codes. ([#247](https://github.com/ros2/rmw_cyclonedds/issues/247))
- Update gid API return codes. ([#244](https://github.com/ros2/rmw_cyclonedds/issues/244))
- Update graph API return codes. ([#243](https://github.com/ros2/rmw_cyclonedds/issues/243))
- Check for message\_info on take where appropriate. ([#245](https://github.com/ros2/rmw_cyclonedds/issues/245)) Fix for regression introduced in [#241](https://github.com/ros2/rmw_cyclonedds/issues/241).
- Updated error returns on rmw\_take\_serialized() and rmw\_take\_with\_message\_info() ([#242](https://github.com/ros2/rmw_cyclonedds/issues/242))
- Updated error returns on rmw\_take() ([#241](https://github.com/ros2/rmw_cyclonedds/issues/241))
- Add quality declaration for Cyclone DDS ([#218](https://github.com/ros2/rmw_cyclonedds/issues/218))
- Fix that not to delete some objects after destroying functions ([#236](https://github.com/ros2/rmw_cyclonedds/issues/236))
- Update rmw\_publish\_serialized\_message() error returns ([#240](https://github.com/ros2/rmw_cyclonedds/issues/240))
- Update rmw\_publish() error returns ([#239](https://github.com/ros2/rmw_cyclonedds/issues/239))
- Remove public declarations ([#230](https://github.com/ros2/rmw_cyclonedds/issues/230))
- Use quotes for non-system includes ([#231](https://github.com/ros2/rmw_cyclonedds/issues/231))
- Use correct functions to resize and get an item, avoiding memory leaks in typesupport code ([#228](https://github.com/ros2/rmw_cyclonedds/issues/228))
- Fix context cleanup. ([#227](https://github.com/ros2/rmw_cyclonedds/issues/227))
- Fix memory leak that type support not deleted. ([#225](https://github.com/ros2/rmw_cyclonedds/issues/225))
- Ensure compliant matched pub/sub count API. ([#223](https://github.com/ros2/rmw_cyclonedds/issues/223))
- Fix memory leak that string not deleted. ([#224](https://github.com/ros2/rmw_cyclonedds/issues/224))
- Change RET\_WRONG\_IMPLID() to return RMW\_RET\_INCORRECT\_IMPLEMENTATION ([#226](https://github.com/ros2/rmw_cyclonedds/issues/226))
- Fix bad conditional in rmw\_serialize(). ([#217](https://github.com/ros2/rmw_cyclonedds/issues/217))
- Ensure compliant subscription API. ([#214](https://github.com/ros2/rmw_cyclonedds/issues/214))
- Ensure compliant publisher API ([#210](https://github.com/ros2/rmw_cyclonedds/issues/210))
- rmw\_destroy\_node must remove node from graph cache ([#213](https://github.com/ros2/rmw_cyclonedds/issues/213))
- Add space between ‘ROS’ and ‘2’ ([#195](https://github.com/ros2/rmw_cyclonedds/issues/195))
- Set context actual domain id ([#208](https://github.com/ros2/rmw_cyclonedds/issues/208))
- Ensure compliant node construction/destruction API ([#206](https://github.com/ros2/rmw_cyclonedds/issues/206))
- Remove domain\_id and localhost\_only from node API ([#205](https://github.com/ros2/rmw_cyclonedds/issues/205))
- Amend rmw\_init() implementation: require enclave. ([#204](https://github.com/ros2/rmw_cyclonedds/issues/204))
- Ensure compliant init/shutdown API implementations. ([#202](https://github.com/ros2/rmw_cyclonedds/issues/202))
- Ensure compliant init options API implementations. ([#200](https://github.com/ros2/rmw_cyclonedds/issues/200))
- Finalize context iff shutdown. ([#196](https://github.com/ros2/rmw_cyclonedds/issues/196))
- Handle RMW\_DEFAULT\_DOMAIN\_ID. ([#194](https://github.com/ros2/rmw_cyclonedds/issues/194))
- Add support to message lost event ([#192](https://github.com/ros2/rmw_cyclonedds/issues/192))
- Mitigate lost service responses discovery issue ([#187](https://github.com/ros2/rmw_cyclonedds/issues/187))
- Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Chen Lihui, Chris Lalancette, Christophe Bedard, Dan Rose, Emerson Knapp, Erik Boasson, Ivan Santiago Paunovic, Jacob Perron, Joe Speed, Jose Tomas Lorente, Lobotuerk, Michel Hidalgo, Scott K Logan, Stephen Brawner, Sumanth Nirmal, Sven Brinkmann, eboasson, pluris

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/galactic/rmw_dds_common/CHANGELOG.rst)

- Fix one more instance of index.ros.org. ([#49](https://github.com/ros2/rmw_dds_common/issues/49))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#46](https://github.com/ros2/rmw_dds_common/issues/46))
- Add function for checking QoS profile compatibility ([#45](https://github.com/ros2/rmw_dds_common/issues/45))
- Shorten some excessively long lines of CMake ([#44](https://github.com/ros2/rmw_dds_common/issues/44))
- Fix test\_graph\_cache ASAN errors ([#41](https://github.com/ros2/rmw_dds_common/issues/41)) ([#42](https://github.com/ros2/rmw_dds_common/issues/42))
- Update QD to QL 1 ([#38](https://github.com/ros2/rmw_dds_common/issues/38))
- Create a utility function to limit rmw\_time\_t to 32-bit values ([#37](https://github.com/ros2/rmw_dds_common/issues/37))
- Update maintainers ([#34](https://github.com/ros2/rmw_dds_common/issues/34))
- Updated performance section QD ([#30](https://github.com/ros2/rmw_dds_common/issues/30))
- Update Quality Declaration to QL2 ([#31](https://github.com/ros2/rmw_dds_common/issues/31))
- Added benchmark test to rmw\_dds\_common ([#29](https://github.com/ros2/rmw_dds_common/issues/29))
- Fix potential memory leak ([#28](https://github.com/ros2/rmw_dds_common/issues/28))
- Add fault injection macro unit tests ([#27](https://github.com/ros2/rmw_dds_common/issues/27))
- Fixed some doxygen warnings ([#26](https://github.com/ros2/rmw_dds_common/issues/26))
- Update Quality Declaration to QL3 ([#24](https://github.com/ros2/rmw_dds_common/issues/24))
- Update QD and documentation ([#23](https://github.com/ros2/rmw_dds_common/issues/23))
- Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Michael Jeronimo, Michel Hidalgo, Scott K Logan, Stephen Brawner, shonigmann, y-okumura-isp

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/galactic/rmw_fastrtps_cpp/CHANGELOG.rst)

- Refactor to use DDS standard API ([#518](https://github.com/ros2/rmw_fastrtps/issues/518))
- Unique network flows ([#502](https://github.com/ros2/rmw_fastrtps/issues/502))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#520](https://github.com/ros2/rmw_fastrtps/issues/520))
- Add RMW function to check QoS compatibility ([#511](https://github.com/ros2/rmw_fastrtps/issues/511))
- Capture cdr exceptions ([#505](https://github.com/ros2/rmw_fastrtps/issues/505))
- Load profiles based on topic names ([#335](https://github.com/ros2/rmw_fastrtps/issues/335))
- Set rmw\_dds\_common::GraphCache callback after init succeeds. ([#496](https://github.com/ros2/rmw_fastrtps/issues/496))
- Handle typesupport errors on fetch. ([#495](https://github.com/ros2/rmw_fastrtps/issues/495))
- Check for correct context shutdown ([#486](https://github.com/ros2/rmw_fastrtps/issues/486))
- New environment variable to change easily the publication mode ([#470](https://github.com/ros2/rmw_fastrtps/issues/470))
- Discriminate when the Client has gone from when the Client has not completely matched ([#467](https://github.com/ros2/rmw_fastrtps/issues/467)) \* Workaround when the client is gone before server sends response \* Change add to the map to listener callback
- Update the package.xml files with the latest Open Robotics maintainers ([#459](https://github.com/ros2/rmw_fastrtps/issues/459))
- Update Quality Declarations and READMEs ([#455](https://github.com/ros2/rmw_fastrtps/issues/455)) \* Add QD links for dependencies to rmw\_fastrtps\_cpp QD \* Provide external dependencies QD links \* Update rmw\_fastrtps README to use Fast DDS \* Update rmw\_fastrtps\_cpp QD: Fast DDS & unit test \* Update README rmw\_fastrtps\_cpp to QL2
- Perform fault injection in all creation/destruction APIs. ([#453](https://github.com/ros2/rmw_fastrtps/issues/453))
- Ensure rmw\_destroy\_node() completes despite run-time errors. ([#458](https://github.com/ros2/rmw_fastrtps/issues/458))
- Update rmw\_fastrtps\_cpp and rmw\_fastrtps\_shared\_cpp QDs to QL2. ([#456](https://github.com/ros2/rmw_fastrtps/issues/456))
- Return RMW\_RET\_UNSUPPORTED in rmw\_get\_serialized\_message\_size ([#452](https://github.com/ros2/rmw_fastrtps/issues/452))
- Updated publisher/subscription allocation and wait set API return codes ([#443](https://github.com/ros2/rmw_fastrtps/issues/443))
- Added rmw\_logging tests ([#442](https://github.com/ros2/rmw_fastrtps/issues/442))
- Make service/client construction/destruction implementation compliant ([#445](https://github.com/ros2/rmw_fastrtps/issues/445))
- Make sure type can be unregistered successfully ([#437](https://github.com/ros2/rmw_fastrtps/issues/437))
- Add tests for native entity getters. ([#439](https://github.com/ros2/rmw_fastrtps/issues/439))
- Avoid deadlock if graph update fails. ([#438](https://github.com/ros2/rmw_fastrtps/issues/438))
- Call Domain::removePublisher while failure occurs in create\_publisher ([#434](https://github.com/ros2/rmw_fastrtps/issues/434))
- Ensure compliant matched pub/sub count API. ([#424](https://github.com/ros2/rmw_fastrtps/issues/424))
- Ensure compliant publisher QoS queries. ([#425](https://github.com/ros2/rmw_fastrtps/issues/425))
- Ensure compliant subscription API. ([#419](https://github.com/ros2/rmw_fastrtps/issues/419))
- Ensure compliant publisher API. ([#414](https://github.com/ros2/rmw_fastrtps/issues/414))
- Set context actual domain id ([#410](https://github.com/ros2/rmw_fastrtps/issues/410))
- Ensure compliant node construction/destruction API. ([#408](https://github.com/ros2/rmw_fastrtps/issues/408))
- Remove domain\_id and localhost\_only from node API ([#407](https://github.com/ros2/rmw_fastrtps/issues/407))
- Amend rmw\_init() implementation: require enclave. ([#406](https://github.com/ros2/rmw_fastrtps/issues/406))
- Update Quality Declarations to QL3. ([#404](https://github.com/ros2/rmw_fastrtps/issues/404))
- Ensure compliant init/shutdown API implementation. ([#401](https://github.com/ros2/rmw_fastrtps/issues/401))
- Update Quality Declaration to QL3. ([#403](https://github.com/ros2/rmw_fastrtps/issues/403))
- Finalize context iff shutdown. ([#396](https://github.com/ros2/rmw_fastrtps/issues/396))
- Make service wait for response reader ([#390](https://github.com/ros2/rmw_fastrtps/issues/390))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Eduardo Ponz Segrelles, Ignacio Montesino Valle, Ivan Santiago Paunovic, JLBuenoLopez-eProsima, Jacob Perron, Jaime Martin Losa, José Luis Bueno López, Michael Jeronimo, Michel Hidalgo, Miguel Company, shonigmann

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/galactic/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Refactor to use DDS standard API ([#518](https://github.com/ros2/rmw_fastrtps/issues/518))
- Unique network flows ([#502](https://github.com/ros2/rmw_fastrtps/issues/502))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#520](https://github.com/ros2/rmw_fastrtps/issues/520))
- Add RMW function to check QoS compatibility ([#511](https://github.com/ros2/rmw_fastrtps/issues/511))
- Capture cdr exceptions ([#505](https://github.com/ros2/rmw_fastrtps/issues/505))
- Load profiles based on topic names in rmw\_fastrtps\_dynamic\_cpp ([#497](https://github.com/ros2/rmw_fastrtps/issues/497))
- Set rmw\_dds\_common::GraphCache callback after init succeeds. ([#496](https://github.com/ros2/rmw_fastrtps/issues/496))
- Handle typesupport errors on fetch. ([#495](https://github.com/ros2/rmw_fastrtps/issues/495))
- Check for correct context shutdown ([#486](https://github.com/ros2/rmw_fastrtps/issues/486))
- New environment variable to change easily the publication mode ([#470](https://github.com/ros2/rmw_fastrtps/issues/470))
- Discriminate when the Client has gone from when the Client has not completely matched ([#467](https://github.com/ros2/rmw_fastrtps/issues/467)) \* Workaround when the client is gone before server sends response \* Change add to the map to listener callback
- Update the package.xml files with the latest Open Robotics maintainers ([#459](https://github.com/ros2/rmw_fastrtps/issues/459))
- Update Quality Declarations and READMEs ([#455](https://github.com/ros2/rmw_fastrtps/issues/455)) \* Add QL of external dependencies to rmw\_fastrtps\_dynamic\_cpp QD \* Add QD links for dependencies to rmw\_fastrtps\_dynamic\_cpp QD \* Provide external dependencies QD links \* Add README to rmw\_fastrtps\_dynamic \* Add QD for rmw\_fastrtps\_dynamic
- Ensure rmw\_destroy\_node() completes despite run-time errors. ([#458](https://github.com/ros2/rmw_fastrtps/issues/458))
- Return RMW\_RET\_UNSUPPORTED in rmw\_get\_serialized\_message\_size ([#452](https://github.com/ros2/rmw_fastrtps/issues/452))
- Updated publisher/subscription allocation and wait set API return codes ([#443](https://github.com/ros2/rmw_fastrtps/issues/443))
- Added rmw\_logging tests ([#442](https://github.com/ros2/rmw_fastrtps/issues/442))
- Fix array `get_function` semantics ([#448](https://github.com/ros2/rmw_fastrtps/issues/448))
- Make service/client construction/destruction implementation compliant ([#445](https://github.com/ros2/rmw_fastrtps/issues/445))
- Make sure type can be unregistered successfully ([#437](https://github.com/ros2/rmw_fastrtps/issues/437))
- Add tests for native entity getters. ([#439](https://github.com/ros2/rmw_fastrtps/issues/439))
- Avoid deadlock if graph update fails. ([#438](https://github.com/ros2/rmw_fastrtps/issues/438))
- Call Domain::removePublisher while failure occurs in create\_publisher ([#434](https://github.com/ros2/rmw_fastrtps/issues/434))
- Avoid memory leaks and undefined behavior in rmw\_fastrtps\_dynamic\_cpp typesupport code ([#429](https://github.com/ros2/rmw_fastrtps/issues/429))
- Ensure compliant matched pub/sub count API. ([#424](https://github.com/ros2/rmw_fastrtps/issues/424))
- Ensure compliant publisher QoS queries. ([#425](https://github.com/ros2/rmw_fastrtps/issues/425))
- Ensure compliant subscription API. ([#419](https://github.com/ros2/rmw_fastrtps/issues/419))
- Ensure compliant publisher API. ([#414](https://github.com/ros2/rmw_fastrtps/issues/414))
- Set context actual domain id ([#410](https://github.com/ros2/rmw_fastrtps/issues/410))
- Ensure compliant node construction/destruction API. ([#408](https://github.com/ros2/rmw_fastrtps/issues/408))
- Remove domain\_id and localhost\_only from node API ([#407](https://github.com/ros2/rmw_fastrtps/issues/407))
- Amend rmw\_init() implementation: require enclave. ([#406](https://github.com/ros2/rmw_fastrtps/issues/406))
- Ensure compliant init/shutdown API implementation. ([#401](https://github.com/ros2/rmw_fastrtps/issues/401))
- Finalize context iff shutdown. ([#396](https://github.com/ros2/rmw_fastrtps/issues/396))
- Make service wait for response reader ([#390](https://github.com/ros2/rmw_fastrtps/issues/390))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Eduardo Ponz Segrelles, Ignacio Montesino Valle, Ivan Santiago Paunovic, JLBuenoLopez-eProsima, Jacob Perron, Jaime Martin Losa, José Luis Bueno López, Michael Jeronimo, Michel Hidalgo, Miguel Company, shonigmann

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/galactic/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Refactor to use DDS standard API ([#518](https://github.com/ros2/rmw_fastrtps/issues/518))
- Unique network flows ([#502](https://github.com/ros2/rmw_fastrtps/issues/502))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#520](https://github.com/ros2/rmw_fastrtps/issues/520))
- Take and return new RMW\_DURATION\_INFINITE correctly ([#515](https://github.com/ros2/rmw_fastrtps/issues/515))
- Add RMW function to check QoS compatibility ([#511](https://github.com/ros2/rmw_fastrtps/issues/511))
- Capture cdr exceptions ([#505](https://github.com/ros2/rmw_fastrtps/issues/505))
- Make sure to lock the mutex protecting client\_endpoints\_. ([#492](https://github.com/ros2/rmw_fastrtps/issues/492))
- Use interface whitelist for localhost only ([#476](https://github.com/ros2/rmw_fastrtps/issues/476))
- Make use of error return value in decrement\_context\_impl\_ref\_count ([#488](https://github.com/ros2/rmw_fastrtps/issues/488))
- Remove unnecessary includes ([#487](https://github.com/ros2/rmw_fastrtps/issues/487))
- Use new time\_utils function to limit rmw\_time\_t values to 32-bits ([#485](https://github.com/ros2/rmw_fastrtps/issues/485))
- New environment variable to change easily the publication mode ([#470](https://github.com/ros2/rmw_fastrtps/issues/470))
- Remove unused headers MessageTypeSupport.hpp and ServiceTypeSupport.hpp ([#481](https://github.com/ros2/rmw_fastrtps/issues/481))
- Discriminate when the Client has gone from when the Client has not completely matched ([#467](https://github.com/ros2/rmw_fastrtps/issues/467)) \* Workaround when the client is gone before server sends response \* Change add to the map to listener callback
- Update the package.xml files with the latest Open Robotics maintainers ([#459](https://github.com/ros2/rmw_fastrtps/issues/459))
- Update Quality Declarations and READMEs ([#455](https://github.com/ros2/rmw_fastrtps/issues/455)) \* Add QD links for dependencies to rmw\_fastrtps\_shared\_cpp QD. \* Provide external dependencies QD links. \* Update rmw\_fastrtps\_shared\_cpp QD: Fast DDS \* Update README rmw\_fastrtps\_shared\_cpp to QL2
- Perform fault injection in all creation/destruction APIs. ([#453](https://github.com/ros2/rmw_fastrtps/issues/453))
- Ensure rmw\_destroy\_node() completes despite run-time errors. ([#458](https://github.com/ros2/rmw_fastrtps/issues/458))
- Handle too large QoS queue depths. ([#457](https://github.com/ros2/rmw_fastrtps/issues/457))
- Update rmw\_fastrtps\_cpp and rmw\_fastrtps\_shared\_cpp QDs to QL2. ([#456](https://github.com/ros2/rmw_fastrtps/issues/456))
- checked client implementation and return RMW\_RET\_INCORRECT\_RMW\_IMPLEMENTATION ([#451](https://github.com/ros2/rmw_fastrtps/issues/451))
- Update service/client request/response API error returns ([#450](https://github.com/ros2/rmw_fastrtps/issues/450))
- Updated publisher/subscription allocation and wait set API return codes ([#443](https://github.com/ros2/rmw_fastrtps/issues/443))
- Added rmw\_logging tests ([#442](https://github.com/ros2/rmw_fastrtps/issues/442))
- Add tests for RMW QoS to DDS attribute conversion. ([#449](https://github.com/ros2/rmw_fastrtps/issues/449))
- Make service/client construction/destruction implementation compliant ([#445](https://github.com/ros2/rmw_fastrtps/issues/445))
- Inject faults on \_\_rmw\_publish() and run\_listener\_thread() call. ([#441](https://github.com/ros2/rmw_fastrtps/issues/441))
- Update gid API return codes. ([#440](https://github.com/ros2/rmw_fastrtps/issues/440))
- Update graph API return codes. ([#436](https://github.com/ros2/rmw_fastrtps/issues/436))
- Update rmw\_take\_serialized() and rmw\_take\_with\_message\_info() error returns ([#435](https://github.com/ros2/rmw_fastrtps/issues/435))
- Update rmw\_take() error returns ([#432](https://github.com/ros2/rmw_fastrtps/issues/432))
- Update rmw\_publish() error returns ([#430](https://github.com/ros2/rmw_fastrtps/issues/430))
- Update rmw\_publish\_serialized\_message() error returns ([#431](https://github.com/ros2/rmw_fastrtps/issues/431))
- Improve \_\_rmw\_create\_wait\_set() implementation. ([#427](https://github.com/ros2/rmw_fastrtps/issues/427))
- Ensure compliant matched pub/sub count API. ([#424](https://github.com/ros2/rmw_fastrtps/issues/424))
- Ensure compliant publisher QoS queries. ([#425](https://github.com/ros2/rmw_fastrtps/issues/425))
- Fix memory leak that wait\_set might be not destoryed in some case. ([#423](https://github.com/ros2/rmw_fastrtps/issues/423))
- Avoid unused identifier variable warnings. ([#422](https://github.com/ros2/rmw_fastrtps/issues/422))
- Fix trying to get topic data that was already removed. ([#417](https://github.com/ros2/rmw_fastrtps/issues/417))
- Ensure compliant subscription API. ([#419](https://github.com/ros2/rmw_fastrtps/issues/419))
- Use package path to TypeSupport.hpp headers in ServiceTypeSupport and MessageTypeSupport ([#415](https://github.com/ros2/rmw_fastrtps/issues/415)) Use package in path to TypeSupport header for ServiceTypeSupport/MessageTypeSupport
- Ensure compliant publisher API. ([#414](https://github.com/ros2/rmw_fastrtps/issues/414))
- Set context actual domain id ([#410](https://github.com/ros2/rmw_fastrtps/issues/410))
- Add missing thread-safety annotation in ServicePubListener ([#409](https://github.com/ros2/rmw_fastrtps/issues/409))
- Ensure compliant node construction/destruction API. ([#408](https://github.com/ros2/rmw_fastrtps/issues/408))
- Update Quality Declarations to QL3. ([#404](https://github.com/ros2/rmw_fastrtps/issues/404))
- Do not use string literals as implementation identifiers in tests. ([#402](https://github.com/ros2/rmw_fastrtps/issues/402))
- Ensure compliant init options API implementations. ([#399](https://github.com/ros2/rmw_fastrtps/issues/399))
- Finalize context iff shutdown. ([#396](https://github.com/ros2/rmw_fastrtps/issues/396))
- Handle RMW\_DEFAULT\_DOMAIN\_ID. ([#394](https://github.com/ros2/rmw_fastrtps/issues/394))
- Make service wait for response reader ([#390](https://github.com/ros2/rmw_fastrtps/issues/390))
- Contributors: Alejandro Hernández Cordero, Chen Lihui, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, JLBuenoLopez-eProsima, Jacob Perron, Jaime Martin Losa, Jose Luis Rivero, Jose Tomas Lorente, José Luis Bueno López, Lobotuerk, Michael Jeronimo, Michel Hidalgo, Miguel Company, Stephen Brawner, shonigmann

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/galactic/rmw_implementation/CHANGELOG.rst)

- Unique network flows ([#170](https://github.com/ros2/rmw_implementation/issues/170))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#185](https://github.com/ros2/rmw_implementation/issues/185))
- Remove rmw\_connext\_cpp. ([#183](https://github.com/ros2/rmw_implementation/issues/183))
- Add support for rmw\_connextdds ([#182](https://github.com/ros2/rmw_implementation/issues/182))
- Add function for checking QoS profile compatibility ([#180](https://github.com/ros2/rmw_implementation/issues/180))
- Shorten some excessively long lines of CMake ([#179](https://github.com/ros2/rmw_implementation/issues/179))
- Add rmw\_fastrtps\_dynamic\_cpp to the explicit group deps ([#177](https://github.com/ros2/rmw_implementation/issues/177))
- Accept any RMW implementation, not just the default ([#172](https://github.com/ros2/rmw_implementation/issues/172))
- Defer path resolution of rmw implementation libraries to dynamic linker. ([#169](https://github.com/ros2/rmw_implementation/issues/169))
- Update QD to QL 1 ([#166](https://github.com/ros2/rmw_implementation/issues/166))
- Fix up C functions to never throw. ([#149](https://github.com/ros2/rmw_implementation/issues/149))
- Restored Dirk as author ([#155](https://github.com/ros2/rmw_implementation/issues/155))
- Update maintainers ([#154](https://github.com/ros2/rmw_implementation/issues/154))
- Updated performance QD section ([#153](https://github.com/ros2/rmw_implementation/issues/153))
- Update Quality Declaration to QL2. ([#151](https://github.com/ros2/rmw_implementation/issues/151))
- Add nominal test for symbol prefetch() and unload. ([#145](https://github.com/ros2/rmw_implementation/issues/145))
- Added benchmark test to rmw\_implementation ([#127](https://github.com/ros2/rmw_implementation/issues/127))
- Test load and lookup functionality. ([#135](https://github.com/ros2/rmw_implementation/issues/135))
- Remove domain\_id and localhost\_only from node API ([#114](https://github.com/ros2/rmw_implementation/issues/114))
- Move the quality declaration into the rmw\_implementation subdirectory. ([#111](https://github.com/ros2/rmw_implementation/issues/111))
- Contributors: Alejandro Hernández Cordero, Ananya Muddukrishna, Andrea Sorbini, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Scott K Logan, Stephen Brawner, shonigmann

<a id="rmw-implementation-cmake"></a>

## [rmw\_implementation\_cmake](https://github.com/ros2/rmw/tree/galactic/rmw_implementation_cmake/CHANGELOG.rst)

- Shorten some excessively long lines of CMake ([#300](https://github.com/ros2/rmw/issues/300))
- Change default RMW vendor to CycloneDDS. ([#293](https://github.com/ros2/rmw/issues/293))
- Update rmw QD to QL 1 ([#289](https://github.com/ros2/rmw/issues/289))
- Update maintainers ([#282](https://github.com/ros2/rmw/issues/282))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Scott K Logan, Stephen Brawner

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/galactic/CHANGELOG.rst)

- Stop rejecting unknown parameters. ([#161](https://github.com/ros/robot_state_publisher/issues/161))
- clean up license to be standard bsd 3 clause ([#130](https://github.com/ros/robot_state_publisher/issues/130))
- Update the maintainers. ([#151](https://github.com/ros/robot_state_publisher/issues/151))
- fix types in range loops to avoid copy due to different type ([#143](https://github.com/ros/robot_state_publisher/issues/143))
- Make sure not to crash on an invalid URDF. ([#141](https://github.com/ros/robot_state_publisher/issues/141))
- Don’t export exe as library ([#25](https://github.com/ros2/robot_state_publisher/issues/25)) ([ros2 #28](https://github.com/ros2/robot_state_publisher/issues/28))
- Contributors: Chris Lalancette, Dirk Thomas, Tully Foote

<a id="ros1-bridge"></a>

## [ros1\_bridge](https://github.com/ros2/ros1_bridge/tree/galactic/CHANGELOG.rst)

- Fix logging for updated rclcpp interface ([#303](https://github.com/ros2/ros1_bridge/issues/303))
- Fix typo in comments ([#297](https://github.com/ros2/ros1_bridge/issues/297))
- Update to use rosidl\_parser and .idl files rather than rosidl\_adapter and .msg files ([#296](https://github.com/ros2/ros1_bridge/issues/296))
- Update maintainers ([#286](https://github.com/ros2/ros1_bridge/issues/286))
- use hardcoded QoS (keep all, transient local) for /tf\_static topic in dynamic\_bridge ([#282](https://github.com/ros2/ros1_bridge/issues/282))
- document explicitly passing the topic type to ‘ros2 topic echo’ ([#279](https://github.com/ros2/ros1_bridge/issues/279))
- Fix multiple definition if message with same name as service exists ([#272](https://github.com/ros2/ros1_bridge/issues/272))
- Contributors: Dirk Thomas, Jacob Perron, Michael Carroll, Vicidel, William Woodall

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/galactic/ros2action/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/galactic/ros2bag/CHANGELOG.rst)

- /clock publisher in Player ([#695](https://github.com/ros2/rosbag2/issues/695))
- Introducing Reindexer CLI ([#699](https://github.com/ros2/rosbag2/issues/699))
- rosbag2\_py pybind wrapper for “record” - remove rosbag2\_transport\_py ([#702](https://github.com/ros2/rosbag2/issues/702))
- Add rosbag2\_py::Player::play to replace rosbag2\_transport\_python version ([#693](https://github.com/ros2/rosbag2/issues/693))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- use rosbag2\_py for ros2 bag info ([#673](https://github.com/ros2/rosbag2/issues/673))
- CLI query rosbag2\_py for available storage implementations ([#659](https://github.com/ros2/rosbag2/issues/659))
- Recorder –regex and –exclude options ([#604](https://github.com/ros2/rosbag2/issues/604))
- Fix the tests on cyclonedds by translating qos duration values ([#606](https://github.com/ros2/rosbag2/issues/606))
- SQLite storage optimized by default ([#568](https://github.com/ros2/rosbag2/issues/568))
- Fix a bug on parsing wrong description in plugin xml file ([#578](https://github.com/ros2/rosbag2/issues/578))
- Compress bag files in separate threads ([#506](https://github.com/ros2/rosbag2/issues/506))
- Sqlite storage double buffering ([#546](https://github.com/ros2/rosbag2/issues/546)) \* Double buffers \* Circular queue and FLUSH option as define \* Minor naming and lexical fixes. \* Removed FLUSH\_BUFFERS define check. \* Sqlite3 storage logging fixes. \* Sqlite3 storage circular buffer with pre allocated memory. \* Sqlite3 storage buffers moved to shared\_ptrs. \* Uncrustify \* Moved double buffers to writer \* Buffer layer reset in seq compression writer in rosbag2 cpp \* Buffer layer for rosbag2 writer refactor \* Changed buffers in BufferLayer to std vectors. \* BufferLayer uncrustify \* Removed non-applicable test for writer cache. \* BufferLayer review fixes \* Rosbag metadata msgs count fixed for BufferLayer \* Condition variable for buffer layer sync. \* Fixed buffer locks \* Buffers in BufferLayer refactored, moved into new class \* Buffer layer split bags fixed. \* Storage options include fix in buffer layer header. \* Mutex around swapping buffers in buffer layer. \* Fixed cache 0 bug in buffer layer. \* Minor buffer layer refactor. \* Counting messages in writer refactored. \* Changed default cache size to 100Mb and updated parameter description \* Applied review remarks: - significant refactoring: separation of cache classes - applied suggested improvements - some renaming - reduce code duplication that would otherwise increase with cache refactor, between compression and plain writers \* Applied review comments - cache consumer now takes a callback and is independent of storage - namespace changes, renaming, cleaning - counting and logging messages by topic \* linter \* Changes after review: fixing flushing, topic counts, and more \* Fix for splitting - flushing state now correctly turns off \* cache classes documentation \* simplified signature \* a couple of tests for cache \* address review: explicit constructor and doxygen styling \* Windows warnings fix \* fixed type mismatch warning on Windows \* added minor comment Co-authored-by: Piotr Jaroszek <[piotr.jaroszek@robotec.ai](mailto:piotr.jaroszek%40robotec.ai)>
- read yaml config file ([#497](https://github.com/ros2/rosbag2/issues/497))
- List all storage plugins in plugin xml file ([#554](https://github.com/ros2/rosbag2/issues/554))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update deprecated qos policy value names ([#548](https://github.com/ros2/rosbag2/issues/548))
- Add record test for ros2bag ([#523](https://github.com/ros2/rosbag2/issues/523))
- Removed duplicated code in record ([#534](https://github.com/ros2/rosbag2/issues/534))
- Change default cache size for sequential\_writer to a non zero value ([#533](https://github.com/ros2/rosbag2/issues/533))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- [ros2bag test\_record] Gets rid of time.sleep and move to using command.wait\_for\_output ([#525](https://github.com/ros2/rosbag2/issues/525))
- Add pytest.ini back to ros2bag. ([#492](https://github.com/ros2/rosbag2/issues/492))
- performance testing packages ([#442](https://github.com/ros2/rosbag2/issues/442))
- Validate QoS profile values are not negative. ([#483](https://github.com/ros2/rosbag2/issues/483))
- catch parent exception ([#472](https://github.com/ros2/rosbag2/issues/472))
- add wait for closed file handles on Windows ([#470](https://github.com/ros2/rosbag2/issues/470))
- introduce ros2 bag list <plugins> ([#468](https://github.com/ros2/rosbag2/issues/468))
- move wait\_for\_shutdown() call out of the context manager ([#466](https://github.com/ros2/rosbag2/issues/466))
- Adding db directory creation to rosbag2\_cpp ([#450](https://github.com/ros2/rosbag2/issues/450))
- use a single temp dir for the test class ([#462](https://github.com/ros2/rosbag2/issues/462))
- Add per-message ZSTD compression ([#418](https://github.com/ros2/rosbag2/issues/418))
- Add split by time to recording ([#409](https://github.com/ros2/rosbag2/issues/409))
- Add pytest.ini so local tests don’t display warning ([#446](https://github.com/ros2/rosbag2/issues/446))
- Contributors: Adam Dąbrowski, Barry Xu, Chris Lalancette, Dirk Thomas, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jaison Titus, Jesse Ikawa, Karsten Knese, Marwan Taher, Michael Jeronimo, P. J. Reed, jhdcs

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/galactic/ros2cli/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Ensure only one daemon can run at a time. ([#622](https://github.com/ros2/ros2cli/issues/622))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add option to support use\_sim\_time. ([#581](https://github.com/ros2/ros2cli/issues/581))
- Bugfix for [#563](https://github.com/ros2/ros2cli/issues/563). ([#570](https://github.com/ros2/ros2cli/issues/570))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Support Python 3.8-provided importlib.metadata. ([#585](https://github.com/ros2/ros2cli/issues/585))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Added dependency to python3-argcomplete to ros2cli. ([#564](https://github.com/ros2/ros2cli/issues/564))
- Remove use of pkg\_resources from ros2cli. ([#537](https://github.com/ros2/ros2cli/pull/537))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Daisuke Sato, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, Tomoya Fujita, Yoan Mollard

<a id="ros2cli-common-extensions"></a>

## [ros2cli\_common\_extensions](https://github.com/ros2/ros2cli_common_extensions/tree/galactic/ros2cli_common_extensions/CHANGELOG.rst)

- remove maintainer ([#5](https://github.com/ros2/ros2cli_common_extensions/issues/5))
- update maintainer ([#4](https://github.com/ros2/ros2cli_common_extensions/issues/4))
- First implementation ([#2](https://github.com/ros2/ros2cli_common_extensions/issues/2))
- Contributors: Bo Sun, Claire Wang

<a id="ros2cli-test-interfaces"></a>

## [ros2cli\_test\_interfaces](https://github.com/ros2/ros2cli/tree/galactic/ros2cli_test_interfaces/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Make ros2cli\_test\_interfaces version equal to other packages.
- Remove ros2interface test dependencies on builtin interface. ([#579](https://github.com/ros2/ros2cli/issues/579))
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Ivan Santiago Paunovic

<a id="ros2component"></a>

## [ros2component](https://github.com/ros2/ros2cli/tree/galactic/ros2component/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Ensure consistent timeout in ros2component list. ([#526](https://github.com/ros2/ros2cli/issues/526))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic, Michel Hidalgo

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/galactic/ros2doctor/CHANGELOG.rst)

- Improve ros2 doctor on Windows. ([#631](https://github.com/ros2/ros2cli/issues/631)) ([#634](https://github.com/ros2/ros2cli/issues/634))
- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Continue to next iteration after exceptions in generate\_reports. ([#623](https://github.com/ros2/ros2cli/issues/623))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Support Python 3.8-provided importlib.metadata. ([#585](https://github.com/ros2/ros2cli/issues/585))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Remove pkg\_resources from ros2doctor. ([#537](https://github.com/ros2/ros2cli/pull/537))
- Make ros2doctor depend on ros\_environment and fix platform.py bug on error. ([#538](https://github.com/ros2/ros2cli/issues/538))
- Refactor ros2doctor hello verb. ([#521](https://github.com/ros2/ros2cli/issues/521))
- Contributors: Alberto Soragna, Audrow Nash, Chris Lalancette, Claire Wang, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, mergify[bot]

<a id="ros2interface"></a>

## [ros2interface](https://github.com/ros2/ros2cli/tree/galactic/ros2interface/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Remove ros2interface test dependencies on builtin interface. ([#579](https://github.com/ros2/ros2cli/issues/579))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Handle inline comments on constants correctly. ([#548](https://github.com/ros2/ros2cli/issues/548))
- Update quoted comments in the test ([#540](https://github.com/ros2/ros2cli/issues/540))
- Add option to include/remove whitespace and comments. ([#527](https://github.com/ros2/ros2cli/issues/527))
- Show “expanded” message definition. ([#524](https://github.com/ros2/ros2cli/issues/524))
- Contributors: Audrow, Audrow Nash, Claire Wang, Ivan Santiago Paunovic, Tully Foote

<a id="ros2launch"></a>

## [ros2launch](https://github.com/ros2/launch_ros/tree/galactic/ros2launch/CHANGELOG.rst)

- Add options extensions to ros2launch and extensibility to the node action ([#216](https://github.com/ros2/launch_ros/issues/216))
- Support non-interactive ros2 launch executions ([#210](https://github.com/ros2/launch_ros/issues/210))
- Merge pull request [#183](https://github.com/ros2/launch_ros/issues/183) from ros2/update-maintainers
- Move previous maintainer to <author>
- Update the package.xml files with the latest Open Robotics maintainers
- Add pytest.ini so local tests don’t display warning ([#152](https://github.com/ros2/launch_ros/issues/152))
- Contributors: Chris Lalancette, Geoffrey Biggs, Michael Jeronimo, Michel Hidalgo

<a id="ros2lifecycle"></a>

## [ros2lifecycle](https://github.com/ros2/ros2cli/tree/galactic/ros2lifecycle/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2lifecycle-test-fixtures"></a>

## [ros2lifecycle\_test\_fixtures](https://github.com/ros2/ros2cli/tree/galactic/ros2lifecycle_test_fixtures/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Depend on rclcpp::rclcpp target. ([#618](https://github.com/ros2/ros2cli/issues/618)) Contributors: Audrow Nash
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2multicast"></a>

## [ros2multicast](https://github.com/ros2/ros2cli/tree/galactic/ros2multicast/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2node"></a>

## [ros2node](https://github.com/ros2/ros2cli/tree/galactic/ros2node/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/galactic/ros2param/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Make the ros2param –filter test more reliable. ([#606](https://github.com/ros2/ros2cli/issues/606))
- Add wildcard loading to ros2 param load. ([#602](https://github.com/ros2/ros2cli/issues/602))
- Ros2 param dump/load should use fully qualified node names. ([#600](https://github.com/ros2/ros2cli/issues/600))
- Add –filter options for ‘ros2 param list’. ([#592](https://github.com/ros2/ros2cli/issues/592))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add rosparam verb load. ([#590](https://github.com/ros2/ros2cli/issues/590))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Add “–param-type” option to ros2param list. ([#572](https://github.com/ros2/ros2cli/issues/572))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic, Victor Lopez, tomoya

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/galactic/ros2pkg/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Use underscores in setup.cfg.em instead of dashes. ([#627](https://github.com/ros2/ros2cli/issues/627))
- Add space for “ROS 2”. ([#617](https://github.com/ros2/ros2cli/issues/617))
- Use target\_compile\_features for c/c++ standards. ([#615](https://github.com/ros2/ros2cli/issues/615))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Declare missing dependency on python3-importlib-resources. ([#584](https://github.com/ros2/ros2cli/issues/584))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Fix incorrect EXPORT for executables. ([#545](https://github.com/ros2/ros2cli/issues/545))
- Switch ros2pkg to using importlib.
- Contributors: Audrow Nash, Chris Lalancette, Claire Wang, Dirk Thomas, Ivan Santiago Paunovic, Scott K Logan, Shane Loretz

<a id="ros2run"></a>

## [ros2run](https://github.com/ros2/ros2cli/tree/galactic/ros2run/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Contributors: Audrow Nash, Claire Wang, Ivan Santiago Paunovic

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/galactic/ros2service/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Check that passed type is actually a service. ([#559](https://github.com/ros2/ros2cli/issues/559))
- Contributors: Audrow Nash, Claire Wang, Dirk Thomas, Ivan Santiago Paunovic

<a id="ros2test"></a>

## [ros2test](https://github.com/ros2/ros_testing/tree/galactic/ros2test/CHANGELOG.rst)

- Add pytest.ini so local tests don’t display warning ([#8](https://github.com/ros2/ros_testing/issues/8))
- Contributors: Chris Lalancette

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/galactic/ros2topic/CHANGELOG.rst)

- Add changelog. ([#636](https://github.com/ros2/ros2cli/issues/636))
- Add verbose info for topic list. ([#351](https://github.com/ros2/ros2cli/issues/351))
- Remove maintainer. ([#597](https://github.com/ros2/ros2cli/issues/597))
- Add option to support use\_sim\_time. ([#581](https://github.com/ros2/ros2cli/issues/581))
- Add Audrow as a maintainer. ([#591](https://github.com/ros2/ros2cli/issues/591))
- Add filter option to ros2topic . ([#575](https://github.com/ros2/ros2cli/issues/575))
- Update deprecated qos policy value names. ([#571](https://github.com/ros2/ros2cli/issues/571))
- Update maintainers. ([#568](https://github.com/ros2/ros2cli/issues/568))
- Fix the test to use the topic name. ([#566](https://github.com/ros2/ros2cli/issues/566))
- Improve the error message for invalid message types. ([#558](https://github.com/ros2/ros2cli/issues/558))
- Use reliable QoS for ros2topic tests. ([#555](https://github.com/ros2/ros2cli/issues/555))
- Add option to echo serialized messages. ([#470](https://github.com/ros2/ros2cli/issues/470))
- Enable –no-daemon flag for some cli tools. ([#514](https://github.com/ros2/ros2cli/issues/514))
- Use transient\_local and longer keep-alive for pub tests. ([#546](https://github.com/ros2/ros2cli/issues/546))
- Add –keep-alive option to ‘topic pub’. ([#544](https://github.com/ros2/ros2cli/issues/544))
- Add option to ros2 topic echo to report lost messages. ([#542](https://github.com/ros2/ros2cli/issues/542))
- Support QoS Depth and History via ros2 topic pub/echo. ([#528](https://github.com/ros2/ros2cli/issues/528))
- Contributors: Audrow Nash, ChenYing Kuo, Chris Lalancette, Claire Wang, Dereck Wonnacott, Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Scott K Logan, Tomoya Fujita, tomoya

<a id="ros-testing"></a>

## [ros\_testing](https://github.com/ros2/ros_testing/tree/galactic/ros_testing/CHANGELOG.rst)

- Use rostest CMake target as output file basename. ([#9](https://github.com/ros2/ros_testing/issues/9))
- Contributors: Michel Hidalgo

<a id="rosbag2"></a>

## [rosbag2](https://github.com/ros2/rosbag2/tree/galactic/rosbag2/CHANGELOG.rst)

- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- RMW-implementation-searcher converter in rosbag2\_cpp ([#670](https://github.com/ros2/rosbag2/issues/670))
- Move zstd compressor to its own package ([#636](https://github.com/ros2/rosbag2/issues/636))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- AMENT\_IGNORE rosbag2\_py for now ([#509](https://github.com/ros2/rosbag2/issues/509))
- rosbag2\_py reader and writer ([#308](https://github.com/ros2/rosbag2/issues/308))
- Contributors: Emerson Knapp, Karsten Knese, Mabel Zhang, Michael Jeronimo

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_compression/CHANGELOG.rst)

- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Reindexer core ([#641](https://github.com/ros2/rosbag2/issues/641)) Add a new C++ Reindexer class for reconstructing metadata from bags that are missing it.
- CLI query rosbag2\_py for available storage implementations ([#659](https://github.com/ros2/rosbag2/issues/659))
- Move zstd compressor to its own package ([#636](https://github.com/ros2/rosbag2/issues/636))
- Remove rosbag2\_compression test dependencies on zstd implementation in prep for moving it into a separate package ([#637](https://github.com/ros2/rosbag2/issues/637))
- Make compressor implementations into a plugin via pluginlib ([#624](https://github.com/ros2/rosbag2/issues/624))
- Use ZSTD’s streaming interface for [de]compressing files ([#543](https://github.com/ros2/rosbag2/issues/543))
- Fix build issues when rosbag2\_storage is binary installed ([#585](https://github.com/ros2/rosbag2/issues/585))
- Fix relative metadata paths in SequentialCompressionWriter ([#613](https://github.com/ros2/rosbag2/issues/613))
- Fix deadlock race condition on compression shutdown ([#616](https://github.com/ros2/rosbag2/issues/616))
- Deduplicate SequentialCompressionReader business logic, add fallback to find bagfiles in incorrectly-written metadata ([#612](https://github.com/ros2/rosbag2/issues/612))
- Compress bag files in separate threads ([#506](https://github.com/ros2/rosbag2/issues/506))
- Sqlite storage double buffering ([#546](https://github.com/ros2/rosbag2/issues/546))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Do not expect empty StorageOptions URI to work in CompressionWriterTest ([#526](https://github.com/ros2/rosbag2/issues/526))
- Remove some code duplication between SequentialWriter and SequentialCompressionWriter ([#527](https://github.com/ros2/rosbag2/issues/527))
- Fix exception thrown given invalid arguments with compression enabled ([#488](https://github.com/ros2/rosbag2/issues/488))
- Adding db directory creation to rosbag2\_cpp ([#450](https://github.com/ros2/rosbag2/issues/450))
- Consolidate ZSTD utility functions ([#459](https://github.com/ros2/rosbag2/issues/459))
- Add per-message ZSTD compression ([#418](https://github.com/ros2/rosbag2/issues/418))
- Contributors: Adam Dąbrowski, Christophe Bedard, Devin Bonnie, Emerson Knapp, Jaison Titus, Karsten Knese, Marwan Taher, Michael Jeronimo, P. J. Reed, jhdcs

<a id="rosbag2-compression-zstd"></a>

## [rosbag2\_compression\_zstd](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_compression_zstd/CHANGELOG.rst)

- Add test\_depend ament\_cmake\_gmock ([#639](https://github.com/ros2/rosbag2/issues/639))
- Move zstd compressor to its own package ([#636](https://github.com/ros2/rosbag2/issues/636))
- Contributors: Emerson Knapp, Shane Loretz

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_cpp/CHANGELOG.rst)

- Add set\_rate to PlayerClock ([#727](https://github.com/ros2/rosbag2/issues/727))
- Enforce non-null now\_fn in TimeControllerClock ([#731](https://github.com/ros2/rosbag2/issues/731))
- Fix pause snapshot behavior and add regression test ([#730](https://github.com/ros2/rosbag2/issues/730))
- Pause/resume PlayerClock ([#704](https://github.com/ros2/rosbag2/issues/704))
- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Enable thread safety analysis for rosbag2\_cpp and add annotations in TimeControllerClock ([#710](https://github.com/ros2/rosbag2/issues/710))
- PlayerClock initial implementation - Player functionally unchanged ([#689](https://github.com/ros2/rosbag2/issues/689))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Reindexer core ([#641](https://github.com/ros2/rosbag2/issues/641)) Add a new C++ Reindexer class for reconstructing metadata from bags that are missing it.
- use rclcpp serialized messages to write data ([#457](https://github.com/ros2/rosbag2/issues/457))
- alternative write api ([#676](https://github.com/ros2/rosbag2/issues/676))
- RMW-implementation-searcher converter in rosbag2\_cpp ([#670](https://github.com/ros2/rosbag2/issues/670))
- CLI query rosbag2\_py for available storage implementations ([#659](https://github.com/ros2/rosbag2/issues/659))
- Fix –topics flag for ros2 bag play being ignored for all bags after the first one. ([#619](https://github.com/ros2/rosbag2/issues/619))
- Fix a crash in test\_message\_cache. ([#635](https://github.com/ros2/rosbag2/issues/635))
- Fix build issues when rosbag2\_storage is binary installed ([#585](https://github.com/ros2/rosbag2/issues/585))
- Deduplicate SequentialCompressionReader business logic, add fallback to find bagfiles in incorrectly-written metadata ([#612](https://github.com/ros2/rosbag2/issues/612))
- include what you use ([#600](https://github.com/ros2/rosbag2/issues/600))
- Only dereference the data pointer if it is valid. ([#581](https://github.com/ros2/rosbag2/issues/581))
- Add back rosbag2\_cpp::StorageOptions as deprecated ([#563](https://github.com/ros2/rosbag2/issues/563))
- Sqlite storage double buffering ([#546](https://github.com/ros2/rosbag2/issues/546))
- correct master build ([#552](https://github.com/ros2/rosbag2/issues/552))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Mutex around writer access in recorder ([#491](https://github.com/ros2/rosbag2/issues/491))
- if cache data exists, it needs to flush the data into the storage before shutdown ([#541](https://github.com/ros2/rosbag2/issues/541))
- Change default cache size for sequential\_writer to a non zero value ([#533](https://github.com/ros2/rosbag2/issues/533))
- SequentialWriter to cache by message size instead of message count ([#530](https://github.com/ros2/rosbag2/issues/530))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Remove some code duplication between SequentialWriter and SequentialCompressionWriter ([#527](https://github.com/ros2/rosbag2/issues/527))
- disable sanitizer by default ([#517](https://github.com/ros2/rosbag2/issues/517))
- Fix typo in error message ([#475](https://github.com/ros2/rosbag2/issues/475))
- introduce defaults for the C++ API ([#452](https://github.com/ros2/rosbag2/issues/452))
- Adding db directory creation to rosbag2\_cpp ([#450](https://github.com/ros2/rosbag2/issues/450))
- comment out unused variable ([#460](https://github.com/ros2/rosbag2/issues/460))
- minimal c++ API test ([#451](https://github.com/ros2/rosbag2/issues/451))
- Add split by time to recording ([#409](https://github.com/ros2/rosbag2/issues/409))
- Contributors: Adam Dąbrowski, Alexander, Chris Lalancette, Dirk Thomas, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jaison Titus, Karsten Knese, Marwan Taher, Michael Jeronimo, P. J. Reed, Patrick Spieler, Tomoya Fujita, jhdcs

<a id="rosbag2-interfaces"></a>

## [rosbag2\_interfaces](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_interfaces/CHANGELOG.rst)

- Add rosbag2\_interfaces package with playback service definitions ([#728](https://github.com/ros2/rosbag2/issues/728))
- Contributors: Emerson Knapp

<a id="rosbag2-performance-benchmarking"></a>

## [rosbag2\_performance\_benchmarking](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst)

- fixed a memory leak in no-transport benchmark ([#674](https://github.com/ros2/rosbag2/issues/674))
- report of performance improvements in rosbag2 (roughly since Foxy) ([#651](https://github.com/ros2/rosbag2/issues/651))
- Performance benchmarking improvements ([#634](https://github.com/ros2/rosbag2/issues/634))
- Performance benchmarking refactor ([#594](https://github.com/ros2/rosbag2/issues/594))
- Sqlite storage double buffering ([#546](https://github.com/ros2/rosbag2/issues/546))
- read yaml config file ([#497](https://github.com/ros2/rosbag2/issues/497))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- performance testing packages ([#442](https://github.com/ros2/rosbag2/issues/442))
- Contributors: Adam Dąbrowski, Karsten Knese, Michael Jeronimo, Piotr Jaroszek

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_py/CHANGELOG.rst)

- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Split Rosbag2Transport into Player and Recorder classes - first pass to enable further progress ([#721](https://github.com/ros2/rosbag2/issues/721))
- /clock publisher in Player ([#695](https://github.com/ros2/rosbag2/issues/695))
- Introducing Reindexer CLI ([#699](https://github.com/ros2/rosbag2/issues/699))
- Fix rosbag2\_py transport test for py capsule ([#707](https://github.com/ros2/rosbag2/issues/707))
- rosbag2\_py pybind wrapper for “record” - remove rosbag2\_transport\_py ([#702](https://github.com/ros2/rosbag2/issues/702))
- Add rosbag2\_py::Player::play to replace rosbag2\_transport\_python version ([#693](https://github.com/ros2/rosbag2/issues/693))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- RMW-implementation-searcher converter in rosbag2\_cpp ([#670](https://github.com/ros2/rosbag2/issues/670))
- use rosbag2\_py for ros2 bag info ([#673](https://github.com/ros2/rosbag2/issues/673))
- CLI query rosbag2\_py for available storage implementations ([#659](https://github.com/ros2/rosbag2/issues/659))
- Fix build issues when rosbag2\_storage is binary installed ([#585](https://github.com/ros2/rosbag2/issues/585))
- Fix the tests on cyclonedds by translating qos duration values ([#606](https://github.com/ros2/rosbag2/issues/606))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Workaround pybind11 bug on Windows when CMAKE\_BUILD\_TYPE=RelWithDebInfo ([#538](https://github.com/ros2/rosbag2/issues/538))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Fix rosbag2\_py on Windows debug and stop ignoring the package ([#531](https://github.com/ros2/rosbag2/issues/531))
- Fix rosbag2\_py bug when using libc++ ([#529](https://github.com/ros2/rosbag2/issues/529))
- AMENT\_IGNORE rosbag2\_py for now ([#509](https://github.com/ros2/rosbag2/issues/509))
- rosbag2\_py reader and writer ([#308](https://github.com/ros2/rosbag2/issues/308))
- Contributors: Emerson Knapp, Ivan Santiago Paunovic, Karsten Knese, Mabel Zhang, Michael Jeronimo, P. J. Reed, jhdcs

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_storage/CHANGELOG.rst)

- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- PlayerClock initial implementation - Player functionally unchanged ([#689](https://github.com/ros2/rosbag2/issues/689))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Reindexer core ([#641](https://github.com/ros2/rosbag2/issues/641)) Add a new C++ Reindexer class for reconstructing metadata from bags that are missing it.
- Remove outdated pluginlib cmake script from rosbag2\_storage ([#661](https://github.com/ros2/rosbag2/issues/661))
- CLI query rosbag2\_py for available storage implementations ([#659](https://github.com/ros2/rosbag2/issues/659))
- Shorten some excessively long lines of CMake ([#648](https://github.com/ros2/rosbag2/issues/648))
- SQLite storage optimized by default ([#568](https://github.com/ros2/rosbag2/issues/568)) \* Use optimized pragmas by default in sqlite storage. Added option to use former behavior
- Use std::filesystem compliant non-member `exists` function for path object ([#593](https://github.com/ros2/rosbag2/issues/593))
- Update codes since rcutils\_calculate\_directory\_size() is changed ([#567](https://github.com/ros2/rosbag2/issues/567))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Add split by time to recording ([#409](https://github.com/ros2/rosbag2/issues/409))
- Contributors: Adam Dąbrowski, Barry Xu, Emerson Knapp, Josh Langsfeld, Karsten Knese, Michael Jeronimo, Scott K Logan, jhdcs

<a id="rosbag2-storage-default-plugins"></a>

## [rosbag2\_storage\_default\_plugins](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_storage_default_plugins/CHANGELOG.rst)

- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Reindexer core ([#641](https://github.com/ros2/rosbag2/issues/641)) Add a new C++ Reindexer class for reconstructing metadata from bags that are missing it.
- Fix build issues when rosbag2\_storage is binary installed ([#585](https://github.com/ros2/rosbag2/issues/585))
- Mutex protection for db writing and stl collections in writer & storage ([#603](https://github.com/ros2/rosbag2/issues/603))
- SQLite storage optimized by default ([#568](https://github.com/ros2/rosbag2/issues/568))
- read yaml config file ([#497](https://github.com/ros2/rosbag2/issues/497))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Contributors: Adam Dąbrowski, Emerson Knapp, Karsten Knese, Michael Jeronimo, P. J. Reed, jhdcs

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_test_common/CHANGELOG.rst)

- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Fix bad\_function\_call by replacing rclcpp::spin\_some with SingleThreadedExecutor ([#705](https://github.com/ros2/rosbag2/issues/705))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Remove temporary directory platform-specific logic from test fixture ([#660](https://github.com/ros2/rosbag2/issues/660))
- Stabilize test\_record by reducing copies of executors and messages ([#576](https://github.com/ros2/rosbag2/issues/576))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Contributors: Emerson Knapp, Michael Jeronimo

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_tests/CHANGELOG.rst)

- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Reindexer core ([#641](https://github.com/ros2/rosbag2/issues/641)) Add a new C++ Reindexer class for reconstructing metadata from bags that are missing it.
- use rclcpp serialized messages to write data ([#457](https://github.com/ros2/rosbag2/issues/457))
- Alternative write api ([#676](https://github.com/ros2/rosbag2/issues/676))
- RMW-implementation-searcher converter in rosbag2\_cpp ([#670](https://github.com/ros2/rosbag2/issues/670))
- Use rosbag2\_py for ros2 bag info ([#673](https://github.com/ros2/rosbag2/issues/673))
- Remove temporary directory platform-specific logic from test fixture ([#660](https://github.com/ros2/rosbag2/issues/660))
- Fix –topics flag for ros2 bag play being ignored for all bags after the first one. ([#619](https://github.com/ros2/rosbag2/issues/619))
- Move zstd compressor to its own package ([#636](https://github.com/ros2/rosbag2/issues/636))
- Fix relative metadata paths in SequentialCompressionWriter ([#613](https://github.com/ros2/rosbag2/issues/613))
- Recorder –regex and –exclude options ([#604](https://github.com/ros2/rosbag2/issues/604))
- Fix the tests on cyclonedds by translating qos duration values ([#606](https://github.com/ros2/rosbag2/issues/606))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Removed duplicated code in record ([#534](https://github.com/ros2/rosbag2/issues/534))
- Change default cache size for sequential\_writer to a non zero value ([#533](https://github.com/ros2/rosbag2/issues/533))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Mark flaky tests as xfail for now ([#520](https://github.com/ros2/rosbag2/issues/520))
- introduce defaults for the C++ API ([#452](https://github.com/ros2/rosbag2/issues/452))
- Adding db directory creation to rosbag2\_cpp ([#450](https://github.com/ros2/rosbag2/issues/450))
- minimal c++ API test ([#451](https://github.com/ros2/rosbag2/issues/451))
- Add split by time to recording ([#409](https://github.com/ros2/rosbag2/issues/409))
- Contributors: Adam Dąbrowski, Alexander, Emerson Knapp, Jaison Titus, Karsten Knese, Marwan Taher, Michael Jeronimo, jhdcs

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/galactic/rosbag2_transport/CHANGELOG.rst)

- cleanup cmakelists ([#726](https://github.com/ros2/rosbag2/issues/726))
- turn recorder into a node ([#724](https://github.com/ros2/rosbag2/issues/724))
- turn player into a node ([#723](https://github.com/ros2/rosbag2/issues/723))
- Remove -Werror from builds, enable it in Action CI ([#722](https://github.com/ros2/rosbag2/issues/722))
- Split Rosbag2Transport into Player and Recorder classes - first pass to enable further progress ([#721](https://github.com/ros2/rosbag2/issues/721))
- /clock publisher in Player ([#695](https://github.com/ros2/rosbag2/issues/695))
- use rclcpp logging macros ([#715](https://github.com/ros2/rosbag2/issues/715))
- use rclcpp::Node for generic pub/sub ([#714](https://github.com/ros2/rosbag2/issues/714))
- PlayerClock initial implementation - Player functionally unchanged ([#689](https://github.com/ros2/rosbag2/issues/689))
- Fix bad\_function\_call by replacing rclcpp::spin\_some with SingleThreadedExecutor ([#705](https://github.com/ros2/rosbag2/issues/705))
- rosbag2\_py pybind wrapper for “record” - remove rosbag2\_transport\_py ([#702](https://github.com/ros2/rosbag2/issues/702))
- Add rosbag2\_py::Player::play to replace rosbag2\_transport\_python version ([#693](https://github.com/ros2/rosbag2/issues/693))
- Fix and clarify logic in test\_play filter test ([#690](https://github.com/ros2/rosbag2/issues/690))
- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Add QoS decoding translation for infinite durations to RMW\_DURATION\_INFINITE ([#684](https://github.com/ros2/rosbag2/issues/684))
- Add support for rmw\_connextdds ([#671](https://github.com/ros2/rosbag2/issues/671))
- Use rosbag2\_py for ros2 bag info ([#673](https://github.com/ros2/rosbag2/issues/673))
- Fix build issues when rosbag2\_storage is binary installed ([#585](https://github.com/ros2/rosbag2/issues/585))
- Regex and exclude fix for rosbag recorder ([#620](https://github.com/ros2/rosbag2/issues/620))
- Recorder –regex and –exclude options ([#604](https://github.com/ros2/rosbag2/issues/604))
- SQLite storage optimized by default ([#568](https://github.com/ros2/rosbag2/issues/568))
- Fixed playing if unknown message types exist ([#592](https://github.com/ros2/rosbag2/issues/592))
- Compress bag files in separate threads ([#506](https://github.com/ros2/rosbag2/issues/506))
- Stabilize test\_record by reducing copies of executors and messages ([#576](https://github.com/ros2/rosbag2/issues/576))
- add storage\_config\_uri ([#493](https://github.com/ros2/rosbag2/issues/493))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- resolve memory leak for serialized message ([#502](https://github.com/ros2/rosbag2/issues/502))
- Use shared logic for importing the rosbag2\_transport\_py library in Python ([#482](https://github.com/ros2/rosbag2/issues/482))
- fix missing target dependencies ([#479](https://github.com/ros2/rosbag2/issues/479))
- reenable cppcheck for rosbag2\_transport ([#461](https://github.com/ros2/rosbag2/issues/461))
- More reliable topic remapping test ([#456](https://github.com/ros2/rosbag2/issues/456))
- Add split by time to recording ([#409](https://github.com/ros2/rosbag2/issues/409))
- export shared\_queues\_vendor ([#434](https://github.com/ros2/rosbag2/issues/434))
- Contributors: Adam Dąbrowski, Andrea Sorbini, Chen Lihui, Dirk Thomas, Emerson Knapp, Karsten Knese, Michael Jeronimo, P. J. Reed, Piotr Jaroszek, jhdcs

<a id="rosgraph-msgs"></a>

## [rosgraph\_msgs](https://github.com/ros2/rcl_interfaces/tree/galactic/rosgraph_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#122](https://github.com/ros2/rcl_interfaces/issues/122))
- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update README.md ([#119](https://github.com/ros2/rcl_interfaces/issues/119))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="rosidl-adapter"></a>

## [rosidl\_adapter](https://github.com/ros2/rosidl/tree/galactic/rosidl_adapter/CHANGELOG.rst)

- Expose .msg/.srv/.action to .idl conversion via rosidl translate CLI ([#576](https://github.com/ros2/rosidl/issues/576))
- Support hex constants in msg files ([#559](https://github.com/ros2/rosidl/issues/559))
- Treat t as whitespace ([#557](https://github.com/ros2/rosidl/issues/557))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Refactor regex for valid package/field names ([#508](https://github.com/ros2/rosidl/issues/508))
- Add pytest.ini so tests succeed locally ([#502](https://github.com/ros2/rosidl/issues/502))
- Contributors: Chris Lalancette, Dereck Wonnacott, Dirk Thomas, Michel Hidalgo

<a id="rosidl-cli"></a>

## [rosidl\_cli](https://github.com/ros2/rosidl/tree/galactic/rosidl_cli/CHANGELOG.rst)

- Align rosidl\_cli package version with the rest of the repo. ([#579](https://github.com/ros2/rosidl/issues/579))
- Expose an API for each rosidl CLI command. ([#577](https://github.com/ros2/rosidl/issues/577))
- Add rosidl translate CLI. ([#575](https://github.com/ros2/rosidl/issues/575))
- Add rosidl generate CLI. ([#567](https://github.com/ros2/rosidl/issues/567))
- Contributors: Michel Hidalgo, Shane Loretz

<a id="rosidl-cmake"></a>

## [rosidl\_cmake](https://github.com/ros2/rosidl/tree/galactic/rosidl_cmake/CHANGELOG.rst)

- Shorten some excessively long lines of CMake ([#571](https://github.com/ros2/rosidl/issues/571))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Modifications to python generator lib to return generated files ([#511](https://github.com/ros2/rosidl/issues/511))
- Contributors: Alex Tyshka, Chris Lalancette, Scott K Logan

<a id="rosidl-default-generators"></a>

## [rosidl\_default\_generators](https://github.com/ros2/rosidl_defaults/tree/galactic/rosidl_default_generators/CHANGELOG.rst)

- Update maintainers ([#13](https://github.com/ros2/rosidl_defaults/issues/13))
- Contributors: Shane Loretz

<a id="rosidl-default-runtime"></a>

## [rosidl\_default\_runtime](https://github.com/ros2/rosidl_defaults/tree/galactic/rosidl_default_runtime/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#18](https://github.com/ros2/rosidl_defaults/issues/18))
- Update QD to QL 1 ([#15](https://github.com/ros2/rosidl_defaults/issues/15))
- Update maintainers ([#13](https://github.com/ros2/rosidl_defaults/issues/13))
- Updated QD to 2 in README.md ([#12](https://github.com/ros2/rosidl_defaults/issues/12))
- Update rosidl\_default\_runtime QD to QL2. ([#11](https://github.com/ros2/rosidl_defaults/issues/11))
- Bump the QUALITY\_DECLARATION to level 3. ([#10](https://github.com/ros2/rosidl_defaults/issues/10))
- Add Security Vulnerability Policy pointing to REP-2006. ([#9](https://github.com/ros2/rosidl_defaults/issues/9))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Shane Loretz, Stephen Brawner, shonigmann

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/galactic/rosidl_generator_c/CHANGELOG.rst)

- Expose C code generation via rosidl generate CLI ([#569](https://github.com/ros2/rosidl/issues/569))
- Strip action service suffixes from C include prefix ([#538](https://github.com/ros2/rosidl/issues/538))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Fix the declared language for a few packages ([#530](https://github.com/ros2/rosidl/issues/530))
- Do not depend on rosidl\_runtime\_c when tests are disabled ([#503](https://github.com/ros2/rosidl/issues/503))
- Contributors: Ben Wolsieffer, Chris Lalancette, Jacob Perron, Michel Hidalgo, Scott K Logan

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/galactic/rosidl_generator_cpp/CHANGELOG.rst)

- Expose C++ code generation via rosidl generate CLI ([#570](https://github.com/ros2/rosidl/issues/570))
- Switch to std::allocator\_traits. ([#564](https://github.com/ros2/rosidl/issues/564))
- Remove unnecessary assert on pointer created with new ([#555](https://github.com/ros2/rosidl/issues/555))
- Use ASSERT\_TRUE to check for nullptr. ([#543](https://github.com/ros2/rosidl/issues/543))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Add to\_yaml() function for C++ messages ([#527](https://github.com/ros2/rosidl/issues/527))
- Add function for getting a types fully qualified name ([#514](https://github.com/ros2/rosidl/issues/514))
- Declaring is\_message in namespace rosidl\_generator\_traits ([#512](https://github.com/ros2/rosidl/issues/512))
- Contributors: Chris Lalancette, Devin Bonnie, Dirk Thomas, Jacob Perron, Michel Hidalgo, Sebastian Höffner, Stephen Brawner

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/galactic/rosidl_generator_dds_idl/CHANGELOG.rst)

- Expose .idl to DDS .idl conversion via rosidl translate CLI. ([#55](https://github.com/ros2/rosidl_dds/issues/55))
- Update maintainers. ([#54](https://github.com/ros2/rosidl_dds/issues/54))
- Contributors: Michel Hidalgo, Shane Loretz

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/galactic/rosidl_generator_py/CHANGELOG.rst)

- Remove dependency from rosidl\_typesupport\_connext\_c ([#127](https://github.com/ros2/rosidl_python/issues/127))
- Expose Python code generation via rosidl generate CLI ([#123](https://github.com/ros2/rosidl_python/issues/123))
- remove maintainer ([#126](https://github.com/ros2/rosidl_python/issues/126))
- Update maintainers ([#119](https://github.com/ros2/rosidl_python/issues/119))
- Fix too early decref of WString when converting from Python to C ([#117](https://github.com/ros2/rosidl_python/issues/117))
- Add pytest.ini so tests succeed locally. ([#116](https://github.com/ros2/rosidl_python/issues/116))
- Contributors: Andrea Sorbini, Chris Lalancette, Claire Wang, Dirk Thomas, Michel Hidalgo

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/galactic/rosidl_parser/CHANGELOG.rst)

- Update and add package.xml descriptions to README ([#553](https://github.com/ros2/rosidl/issues/553))
- Finish support for fixed-point literals.
- Fix parsing of small floats.
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Allow zero length string constants ([#507](https://github.com/ros2/rosidl/issues/507))
- Add pytest.ini so tests succeed locally ([#502](https://github.com/ros2/rosidl/issues/502))
- Contributors: Chris Lalancette, Dirk Thomas, Shane Loretz

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/galactic/rosidl_runtime_c/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#581](https://github.com/ros2/rosidl/issues/581))
- Shorten some excessively long lines of CMake ([#571](https://github.com/ros2/rosidl/issues/571))
- Update and add package.xml descriptions to README ([#553](https://github.com/ros2/rosidl/issues/553))
- Fix item number in QD ([#546](https://github.com/ros2/rosidl/issues/546))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Add rcutils dependency. ([#534](https://github.com/ros2/rosidl/issues/534))
- QD: Add links to hosted API docs ([#533](https://github.com/ros2/rosidl/issues/533))
- Updated Quality Level to 1 ([#532](https://github.com/ros2/rosidl/issues/532))
- Add benchmarks for rosidl\_runtime\_\* packages ([#521](https://github.com/ros2/rosidl/issues/521))
- Fix the declared language for a few packages ([#530](https://github.com/ros2/rosidl/issues/530))
- Add fault injection macros and test ([#509](https://github.com/ros2/rosidl/issues/509))
- Update rosidl\_runtime\_c QD to QL 2 ([#500](https://github.com/ros2/rosidl/issues/500))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Louise Poubel, Scott K Logan, Shane Loretz, Stephen Brawner, brawner, shonigmann

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/galactic/rosidl_runtime_cpp/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#581](https://github.com/ros2/rosidl/issues/581))
- Fix typo of package name in README heading ([#561](https://github.com/ros2/rosidl/issues/561))
- Update and add package.xml descriptions to README ([#553](https://github.com/ros2/rosidl/issues/553))
- Fix item number in QD ([#546](https://github.com/ros2/rosidl/issues/546))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- QD: Add links to hosted API docs ([#533](https://github.com/ros2/rosidl/issues/533))
- Updated Quality Level to 1 ([#532](https://github.com/ros2/rosidl/issues/532))
- Add benchmarks for rosidl\_runtime\_\* packages ([#521](https://github.com/ros2/rosidl/issues/521))
- Add to\_yaml() function for C++ messages ([#527](https://github.com/ros2/rosidl/issues/527))
- Add function for getting a types fully qualified name ([#514](https://github.com/ros2/rosidl/issues/514))
- Fix misuses of input iterators in BoundedVector ([#493](https://github.com/ros2/rosidl/issues/493))
- Update QD to reflect QL 2 statuses ([#499](https://github.com/ros2/rosidl/issues/499))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Devin Bonnie, Dirk Thomas, Jacob Perron, Jonathan Wakely, Louise Poubel, Scott K Logan, Shane Loretz, Stephen Brawner, Tully Foote, shonigmann

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/galactic/CHANGELOG.rst)

- Add pytest.ini so local tests don’t display warning ([#12](https://github.com/ros2/rosidl_runtime_py/issues/12))
- Contributors: Chris Lalancette

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/galactic/rosidl_typesupport_c/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#108](https://github.com/ros2/rosidl_typesupport/issues/108))
- Remove dependencies from Connext type support ([#106](https://github.com/ros2/rosidl_typesupport/issues/106))
- Expose C typesupport generation via rosidl generate CLI ([#105](https://github.com/ros2/rosidl_typesupport/issues/105))
- Typo typesupport\_identidentifier ([#103](https://github.com/ros2/rosidl_typesupport/issues/103))
- Remove type\_support\_dispatch.cpp files. ([#101](https://github.com/ros2/rosidl_typesupport/issues/101))
- Defer path resolution of rosidl typesupport libraries to dynamic linker. ([#98](https://github.com/ros2/rosidl_typesupport/issues/98))
- Ensure typesupport handle functions do not throw. ([#99](https://github.com/ros2/rosidl_typesupport/issues/99))
- Explicitly check lib pointer for null ([#95](https://github.com/ros2/rosidl_typesupport/issues/95))
- Update Quality Declaration to QL 1 ([#96](https://github.com/ros2/rosidl_typesupport/issues/96))
- Add mock for rcutils\_get\_symbol failure ([#93](https://github.com/ros2/rosidl_typesupport/issues/93))
- Update the maintainers ([#89](https://github.com/ros2/rosidl_typesupport/issues/89))
- Catch exception from has\_symbol ([#86](https://github.com/ros2/rosidl_typesupport/issues/86))
- Added benchmark test to rosidl\_typesupport\_c/cpp ([#84](https://github.com/ros2/rosidl_typesupport/issues/84))
- Handle rcpputils::find\_library\_path() failure ([#85](https://github.com/ros2/rosidl_typesupport/issues/85))
- Add fault injection macros and unit tests ([#80](https://github.com/ros2/rosidl_typesupport/issues/80))
- Remove rethrow in extern c code ([#82](https://github.com/ros2/rosidl_typesupport/issues/82))
- Add Security Vulnerability Policy pointing to REP-2006 ([#76](https://github.com/ros2/rosidl_typesupport/issues/76))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris Lalancette, Jose Luis Rivero, Jose Tomas Lorente, Louise Poubel, Michel Hidalgo, Shane Loretz, Stephen Brawner, shonigmann

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/galactic/rosidl_typesupport_cpp/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#108](https://github.com/ros2/rosidl_typesupport/issues/108))
- Remove dependencies from Connext type support ([#106](https://github.com/ros2/rosidl_typesupport/issues/106))
- Expose C++ typesupport generation via rosidl generate CLI ([#104](https://github.com/ros2/rosidl_typesupport/issues/104))
- Remove type\_support\_dispatch.cpp files. ([#101](https://github.com/ros2/rosidl_typesupport/issues/101))
- Defer path resolution of rosidl typesupport libraries to dynamic linker. ([#98](https://github.com/ros2/rosidl_typesupport/issues/98))
- Ensure typesupport handle functions do not throw. ([#99](https://github.com/ros2/rosidl_typesupport/issues/99))
- Explicitly check lib pointer for null ([#95](https://github.com/ros2/rosidl_typesupport/issues/95))
- Update Quality Declaration to QL 1 ([#96](https://github.com/ros2/rosidl_typesupport/issues/96))
- Update the maintainers ([#89](https://github.com/ros2/rosidl_typesupport/issues/89))
- Added benchmark test to rosidl\_typesupport\_c/cpp ([#84](https://github.com/ros2/rosidl_typesupport/issues/84))
- Handle rcpputils::find\_library\_path() failure ([#85](https://github.com/ros2/rosidl_typesupport/issues/85))
- De-duplicate type\_support\_map.h header ([#81](https://github.com/ros2/rosidl_typesupport/issues/81))
- Add fault injection macros and unit tests ([#80](https://github.com/ros2/rosidl_typesupport/issues/80))
- Add Security Vulnerability Policy pointing to REP-2006 ([#76](https://github.com/ros2/rosidl_typesupport/issues/76))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris Lalancette, Jose Luis Rivero, Louise Poubel, Michel Hidalgo, Stephen Brawner, shonigmann

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/galactic/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#69](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/69))
- Expose FastRTPS C typesupport generation via rosidl generate CLI ([#65](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/65))
- Update QDs with up-to-date content ([#64](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/64))
- Fix item number in QD ([#59](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/59))
- Update QL to 2
- Update package maintainers ([#55](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/55))
- Updat QD ([#53](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/53))
- Fix invalid return on deserialize function ([#51](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/51))
- Added benchmark test to rosidl\_typesupport\_fastrtps\_c/cpp ([#52](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/52))
- Update exec dependencies ([#50](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/50))
- Add Security Vulnerability Policy pointing to REP-2006 ([#44](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/44))
- QD Update Version Stability to stable version ([#46](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/46))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge Perez, Louise Poubel, Michel Hidalgo, Stephen Brawner, shonigmann, sung-goo-kim

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/galactic/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#69](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/69))
- Expose FastRTPS C++ typesupport generation via rosidl generate CLI ([#66](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/66))
- Update QDs with up-to-date content ([#64](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/64))
- Fix item number in QD ([#59](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/59))
- Update QL to 2
- Update package maintainers ([#55](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/55))
- Update QD ([#53](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/53))
- Add benchmark test to rosidl\_typesupport\_fastrtps\_c/cpp ([#52](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/52))
- Update exec dependencies ([#50](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/50))
- Add Security Vulnerability Policy pointing to REP-2006 ([#44](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/44))
- QD Update Version Stability to stable version ([#46](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/46))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jorge Perez, Louise Poubel, Michel Hidalgo, Stephen Brawner, shonigmann

<a id="rosidl-typesupport-interface"></a>

## [rosidl\_typesupport\_interface](https://github.com/ros2/rosidl/tree/galactic/rosidl_typesupport_interface/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#581](https://github.com/ros2/rosidl/issues/581))
- Fix item number in QD ([#546](https://github.com/ros2/rosidl/issues/546))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- QD: Add links to hosted API docs ([#533](https://github.com/ros2/rosidl/issues/533))
- Update Quality Declaration to QL 1 for rosidl\_typesupport\_interface ([#519](https://github.com/ros2/rosidl/issues/519))
- Update QD to reflect QL 2 statuses ([#499](https://github.com/ros2/rosidl/issues/499))
- Contributors: Chris Lalancette, Louise Poubel, Stephen Brawner, brawner, shonigmann

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/galactic/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Expose C introspection typesupport generation via rosidl generate CLI ([#572](https://github.com/ros2/rosidl/issues/572))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Fix get\_function and get\_const\_function semantics for arrays ([#531](https://github.com/ros2/rosidl/issues/531))
- Fix the declared language for a few packages ([#530](https://github.com/ros2/rosidl/issues/530))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/galactic/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Expose C++ introspection typesupport generation via rosidl generate CLI ([#573](https://github.com/ros2/rosidl/issues/573))
- Update the maintainers of this repository. ([#536](https://github.com/ros2/rosidl/issues/536))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/galactic/CHANGELOG.rst)

- Create a shared function for importing c libraries ([#4](https://github.com/ros2/rpyutils/issues/4))
- Add pytest.ini so local tests don’t display warning ([#3](https://github.com/ros2/rpyutils/issues/3))
- Contributors: Chris Lalancette, Emerson Knapp

<a id="rqt"></a>

## [rqt](https://github.com/ros-visualization/rqt/tree/crystal-devel/rqt/CHANGELOG.rst)

- 1.0.7 ([#243](https://github.com/ros-visualization/rqt/issues/243))
- Remove Dirk from maintainers in package.xml files per request. ([#236](https://github.com/ros-visualization/rqt/issues/236))
- Update maintainers for the crystal-devel branch ([#234](https://github.com/ros-visualization/rqt/issues/234))
- Contributors: Michael Jeronimo, Scott K Logan

<a id="rqt-action"></a>

## [rqt\_action](https://github.com/ros-visualization/rqt_action/tree/ros2/CHANGELOG.rst)

- Updated Open Robotics maintainer
- Fixed package to run with ros2 run ([#8](https://github.com/ros-visualization/rqt_action/issues/8))
- Contributors: Alejandro Hernández Cordero, Mabel Zhang

<a id="rqt-bag"></a>

## [rqt\_bag](https://github.com/ros-visualization/rqt_bag/tree/ros2/rqt_bag/CHANGELOG.rst)

- Remove an invalid import statement ([#101](https://github.com/ros-visualization/rqt_bag/issues/101))
- Reset timeline zoom after loading a new bag. ([#98](https://github.com/ros-visualization/rqt_bag/issues/98))
- Refactor the Rosbag2 class ([#91](https://github.com/ros-visualization/rqt_bag/issues/91))
- Fix exec\_depend ([#89](https://github.com/ros-visualization/rqt_bag/issues/89))
- Use updated HistoryPolicy values to avoid deprecation warnings ([#88](https://github.com/ros-visualization/rqt_bag/issues/88))
- Enable recording for ROS2 ([#87](https://github.com/ros-visualization/rqt_bag/issues/87))
- Enable the playback functionality for ROS2 ([#85](https://github.com/ros-visualization/rqt_bag/issues/85))
- Port the topic and node selection dialogs to ROS2 ([#86](https://github.com/ros-visualization/rqt_bag/issues/86))
- Save the serialization format and offered\_qos\_profiles when exporting ([#84](https://github.com/ros-visualization/rqt_bag/issues/84))
- Enable the export/save bag functionality for ROS2 ([#82](https://github.com/ros-visualization/rqt_bag/issues/82))
- Update known message types and associated colors ([#81](https://github.com/ros-visualization/rqt_bag/issues/81))
- Open the bag directory instead of a single file ([#80](https://github.com/ros-visualization/rqt_bag/issues/80))
- Port the image\_view plugin to ROS2 ([#78](https://github.com/ros-visualization/rqt_bag/issues/78))
- Clean up widgets in plot\_view layout correctly ([#69](https://github.com/ros-visualization/rqt_bag/issues/69)) ([#77](https://github.com/ros-visualization/rqt_bag/issues/77))
- Fix tuples for bisect calls ([#67](https://github.com/ros-visualization/rqt_bag/issues/67)) ([#76](https://github.com/ros-visualization/rqt_bag/issues/76))
- Fix issue: no vertical scroll bar until window is resized ([#63](https://github.com/ros-visualization/rqt_bag/issues/63)) ([#75](https://github.com/ros-visualization/rqt_bag/issues/75))
- Update the basic plugins for ROS2 ([#72](https://github.com/ros-visualization/rqt_bag/issues/72))
- Update the rosbag2 python module ([#71](https://github.com/ros-visualization/rqt_bag/issues/71))
- Dynamically resize the timeline when recording ([#66](https://github.com/ros-visualization/rqt_bag/issues/66))
- Starting point for resuming the ROS2 port ([#70](https://github.com/ros-visualization/rqt_bag/issues/70))
- Fix a bug with the status line progress bar ([#62](https://github.com/ros-visualization/rqt_bag/issues/62))
- Update a few minor status bar-related items ([#61](https://github.com/ros-visualization/rqt_bag/issues/61))
- Make the tree controls in the Raw View and Plot View consistent ([#57](https://github.com/ros-visualization/rqt_bag/issues/57))
- Update the package.xml files with the latest Open Robotics maintainers ([#58](https://github.com/ros-visualization/rqt_bag/issues/58))
- fix Python 3 issue: long/int ([#52](https://github.com/ros-visualization/rqt_bag/issues/52))
- save last directory opened to load a bag file ([#40](https://github.com/ros-visualization/rqt_bag/issues/40))
- fix shebang line for Python 3 ([#48](https://github.com/ros-visualization/rqt_bag/issues/48))
- bump CMake minimum version to avoid CMP0048 warning
- fix Python 3 exception, wrap filter call in list() ([#46](https://github.com/ros-visualization/rqt_bag/issues/46))
- add Python 3 conditional dependencies ([#44](https://github.com/ros-visualization/rqt_bag/issues/44))
- autopep8 ([#30](https://github.com/ros-visualization/rqt_bag/issues/30))
- add support for opening multiple bag files at once ([#25](https://github.com/ros-visualization/rqt_bag/issues/25))
- fix debug/warning messages for unicode filenames ([#26](https://github.com/ros-visualization/rqt_bag/issues/26))
- fix regression from version 0.4.10 ([#17](https://github.com/ros-visualization/rqt_bag/issues/17))
- fix regression from version 0.4.9 ([#16](https://github.com/ros-visualization/rqt_bag/issues/16))
- handle errors happening while loading a bag ([#14](https://github.com/ros-visualization/rqt_bag/issues/14))
- add rqt\_bag.launch file ([#440](https://github.com/ros-visualization/rqt_common_plugins/pull/440))
- fix Python 2 regression from version 0.4.4 ([#424](https://github.com/ros-visualization/rqt_common_plugins/issues/424))
- use Python 3 compatible syntax ([#421](https://github.com/ros-visualization/rqt_common_plugins/pull/421))
- fix race condition reading bag files ([#412](https://github.com/ros-visualization/rqt_common_plugins/pull/412))
- add “From nodes” button to record mode ([#348](https://github.com/ros-visualization/rqt_common_plugins/issues/348))
- show file size of bag file in the status bar ([#347](https://github.com/ros-visualization/rqt_common_plugins/pull/347))
- fix mouse wheel delta in Qt 5 ([#376](https://github.com/ros-visualization/rqt_common_plugins/issues/376))
- Support Qt 5 (in Kinetic and higher) as well as Qt 4 (in Jade and earlier) ([#359](https://github.com/ros-visualization/rqt_common_plugins/pull/359))
- fix publishing wrong topic after scrolling ([#362](https://github.com/ros-visualization/rqt_common_plugins/pull/362))
- RQT\_BAG: Ensure monotonic clock publishing. Due to parallelism issues, a message can be published with a simulated timestamp in the past. This lead to undesired behaviors when using TF for example.
- Added step-by-step playback capability
- fix viewer plugin relocation issue ([#306](https://github.com/ros-visualization/rqt_common_plugins/issues/306))
- fix topic type retrieval for multiple bag files ([#279](https://github.com/ros-visualization/rqt_common_plugins/issues/279))
- fix region\_changed signal emission when no start/end stamps are set
- improve right-click menu
- improve popup management ([#280](https://github.com/ros-visualization/rqt_common_plugins/issues/280))
- implement recording of topic subsets
- sort the list of topics
- update plugin scripts to use full name to avoid future naming collisions
- fix visibility with dark Qt theme ([#263](https://github.com/ros-visualization/rqt_common_plugins/issues/263))
- fix compatibility with Groovy, use queue\_size for Python publishers only when available ([#243](https://github.com/ros-visualization/rqt_common_plugins/issues/243))
- use thread for loading bag files, emit region changed signal used by plotting plugin ([#239](https://github.com/ros-visualization/rqt_common_plugins/issues/239))
- export architecture\_independent flag in package.xml ([#254](https://github.com/ros-visualization/rqt_common_plugins/issues/254))
- fix closing and reopening topic views
- use queue\_size for Python publishers
- fix raw view not showing fields named ‘msg’ ([#226](https://github.com/ros-visualization/rqt_common_plugins/issues/226))
- add option to publish clock tim from bag ([#204](https://github.com/ros-visualization/rqt_common_plugins/issues/204))
- add groups for rqt plugins, renamed some plugins ([#167](https://github.com/ros-visualization/rqt_common_plugins/issues/167))
- fix high cpu load when idle ([#194](https://github.com/ros-visualization/rqt_common_plugins/issues/194))
- update rqt\_bag plugin interface to work with qt\_gui\_core 0.2.18
- fix rendering of icons on OS X ([ros-visualization/rqt#83](https://github.com/ros-visualization/rqt/issues/83))
- fix shutdown of plugin ([#31](https://github.com/ros-visualization/rqt_common_plugins/issues/31))
- fix saving parts of a bag ([#96](https://github.com/ros-visualization/rqt_common_plugins/issues/96))
- fix long topic names ([#114](https://github.com/ros-visualization/rqt_common_plugins/issues/114))
- fix zoom behavior ([#76](https://github.com/ros-visualization/rqt_common_plugins/issues/76))
- Fix; skips time when resuming playback ([#5](https://github.com/ros-visualization/rqt_common_plugins/issues/5))
- Fix; timestamp printing issue ([#6](https://github.com/ros-visualization/rqt_common_plugins/issues/6))
- expose command line arguments to rqt\_bag script
- added fix to set play/pause button correctly when fastforwarding/rewinding, adjusted time headers to 0m00s instead of 0:00m for ease of reading
- support passing bagfiles on the command line (currently behind –args)
- first release of this package into Groovy
- Contributors: Aaron Blasdel, Chris Lalancette, Michael Grupp, Michael Jeronimo, lsouchet, sambrose

<a id="rqt-bag-plugins"></a>

## [rqt\_bag\_plugins](https://github.com/ros-visualization/rqt_bag/tree/ros2/rqt_bag_plugins/CHANGELOG.rst)

- Refactor the Rosbag2 class ([#91](https://github.com/ros-visualization/rqt_bag/issues/91))
- Port the plot view to ROS2 ([#79](https://github.com/ros-visualization/rqt_bag/issues/79))
- Port the image\_view plugin to ROS2 ([#78](https://github.com/ros-visualization/rqt_bag/issues/78))
- Starting point for resuming the ROS2 port ([#70](https://github.com/ros-visualization/rqt_bag/issues/70))
- Make the tree controls in the Raw View and Plot View consistent ([#57](https://github.com/ros-visualization/rqt_bag/issues/57))
- Update the package.xml files with the latest Open Robotics maintainers ([#58](https://github.com/ros-visualization/rqt_bag/issues/58))
- initialize pil\_mode when image is compressed ([#54](https://github.com/ros-visualization/rqt_bag/issues/54))
- support 16-bit bayer images ([#45](https://github.com/ros-visualization/rqt_bag/issues/45))
- maintain image aspect ratio ([#32](https://github.com/ros-visualization/rqt_bag/issues/32))
- fix Python 3 issue: long/int ([#51](https://github.com/ros-visualization/rqt_bag/issues/51))
- fix Python 3 issue: ensure str is encoded before decoding ([#50](https://github.com/ros-visualization/rqt_bag/issues/50))
- bump CMake minimum version to avoid CMP0048 warning
- add Python 3 conditional dependencies ([#44](https://github.com/ros-visualization/rqt_bag/issues/44))
- add cairocffi as the fallback module ([#43](https://github.com/ros-visualization/rqt_bag/issues/43))
- autopep8 ([#30](https://github.com/ros-visualization/rqt_bag/issues/30))
- fix Python 2 regression from version 0.4.4 ([#426](https://github.com/ros-visualization/rqt_common_plugins/issues/426))
- use Python 3 compatible syntax ([#421](https://github.com/ros-visualization/rqt_common_plugins/pull/421))
- fix crash when toggling thumbnail ([#380](https://github.com/ros-visualization/rqt_common_plugins/issues/380))
- lock bag when reading for plotting ([#382](https://github.com/ros-visualization/rqt_common_plugins/pull/382))
- Support Qt 5 (in Kinetic and higher) as well as Qt 4 (in Jade and earlier) ([#359](https://github.com/ros-visualization/rqt_common_plugins/pull/359))
- add missing dependency on rqt\_plot ([#316](https://github.com/ros-visualization/rqt_common_plugins/pull/316))
- work around Pillow segfault if PyQt5 is installed ([#289](https://github.com/ros-visualization/rqt_common_plugins/pull/289), [#290](https://github.com/ros-visualization/rqt_common_plugins/pull/290))
- add displaying of depth image thumbnails
- add missing dependency on python-cairo ([#269](https://github.com/ros-visualization/rqt_common_plugins/issues/269))
- fix missing installation of resource subfolder
- add plotting plugin ([#239](https://github.com/ros-visualization/rqt_common_plugins/issues/239))
- fix rqt\_bag to plot array members ([#253](https://github.com/ros-visualization/rqt_common_plugins/issues/253))
- export architecture\_independent flag in package.xml ([#254](https://github.com/ros-visualization/rqt_common_plugins/issues/254))
- fix PIL/Pillow error ([#224](https://github.com/ros-visualization/rqt_common_plugins/issues/224))
- first release of this package into Groovy
- Contributors: John Stechschulte, Michael Jeronimo

<a id="rqt-console"></a>

## [rqt\_console](https://github.com/ros-visualization/rqt_console/tree/ros2/CHANGELOG.rst)

- Use underscores in setup.cfg instead of dashes ([#31](https://github.com/ros-visualization/rqt_console/issues/31))
- Fix regression introduced in [#21](https://github.com/ros-visualization/rqt_console/issues/21) ([#28](https://github.com/ros-visualization/rqt_console/issues/28))
- Changed the build type to ament\_python and added setup.cfg ([#21](https://github.com/ros-visualization/rqt_console/issues/21))
- Contributors: Alejandro Hernández Cordero, Michel Hidalgo

<a id="rqt-graph"></a>

## [rqt\_graph](https://github.com/ros-visualization/rqt_graph/tree/galactic-devel/CHANGELOG.rst)

- Make topics that have qos incompatibilities red in the graph, add information to the node tooltip ([#61](https://github.com/ros-visualization/rqt_graph/issues/61))
- Add node name, topic name, and endpoint kind to the qos edge tooltip ([#60](https://github.com/ros-visualization/rqt_graph/issues/60))
- Update maintainers for ROS2 branches ([#55](https://github.com/ros-visualization/rqt_graph/issues/55))
- add edge tooltip with QoS of publishers and subscribers ([#53](https://github.com/ros-visualization/rqt_graph/issues/53))
- install executable rqt\_graph ([#49](https://github.com/ros-visualization/rqt_graph/issues/49))
- add setup.cfg with script install directories ([#42](https://github.com/ros-visualization/rqt_graph/issues/42))
- add pytest.ini so local tests don’t display warning ([#48](https://github.com/ros-visualization/rqt_graph/issues/48))
- Contributors: Ivan Santiago Paunovic, Michael Jeronimo

<a id="rqt-gui"></a>

## [rqt\_gui](https://github.com/ros-visualization/rqt/tree/crystal-devel/rqt_gui/CHANGELOG.rst)

- getiterator() renamed to iter() in Python 3.9 ([#239](https://github.com/ros-visualization/rqt/issues/239))
- Contributors: goekce

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/crystal-devel/rqt_gui_cpp/CHANGELOG.rst)

- use tgt compile features ([#247](https://github.com/ros-visualization/rqt/issues/247))
- Contributors: Audrow Nash

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/crystal-devel/rqt_gui_py/CHANGELOG.rst)

- Fix a crash at shutdown ([#248](https://github.com/ros-visualization/rqt/issues/248))
- Contributors: Michael Jeronimo

<a id="rqt-msg"></a>

## [rqt\_msg](https://github.com/ros-visualization/rqt_msg/tree/foxy-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#8](https://github.com/ros-visualization/rqt_msg/issues/8))
- Use rosidl\_runtype\_py instead of message\_helpers where possible ([#11](https://github.com/ros-visualization/rqt_msg/issues/11))
- Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic

<a id="rqt-plot"></a>

## [rqt\_plot](https://github.com/ros-visualization/rqt_plot/tree/foxy-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#58](https://github.com/ros-visualization/rqt_plot/issues/58))
- Fix plots of array items ([#71](https://github.com/ros-visualization/rqt_plot/issues/71))
- Update maintainers
- Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic, Mabel Zhang

<a id="rqt-publisher"></a>

## [rqt\_publisher](https://github.com/ros-visualization/rqt_publisher/tree/foxy-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#18](https://github.com/ros-visualization/rqt_publisher/issues/18))
- Drop numpy.float128 references ([#26](https://github.com/ros-visualization/rqt_publisher/issues/26))
- Use rosidl\_runtime\_py instead of rqt\_py\_common where possible ([#24](https://github.com/ros-visualization/rqt_publisher/issues/24))
- Add now() to evaluation ([#22](https://github.com/ros-visualization/rqt_publisher/issues/22))
- fix setting expressions on sequence items ([#16](https://github.com/ros-visualization/rqt_publisher/issues/16))
- Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic, Michel Hidalgo, Yossi Ovcharik

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/crystal-devel/rqt_py_common/CHANGELOG.rst)

- Avoid installing test interfaces ([#228](https://github.com/ros-visualization/rqt/issues/228))
- Contributors: Dirk Thomas

<a id="rqt-py-console"></a>

## [rqt\_py\_console](https://github.com/ros-visualization/rqt_py_console/tree/crystal-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#8](https://github.com/ros-visualization/rqt_py_console/issues/8))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-reconfigure"></a>

## [rqt\_reconfigure](https://github.com/ros-visualization/rqt_reconfigure/tree/dashing/CHANGELOG.rst)

- Cleanups to the install scripts. ([#103](https://github.com/ros-visualization/rqt_reconfigure/issues/103))
- Fix a flake8 warning. ([#99](https://github.com/ros-visualization/rqt_reconfigure/issues/99))
- Use timeouts in service calls to avoid hangs ([#98](https://github.com/ros-visualization/rqt_reconfigure/issues/98))
- Add maintainer to package.xml ([#95](https://github.com/ros-visualization/rqt_reconfigure/issues/95))
- Save instance state in rqt settings ([#90](https://github.com/ros-visualization/rqt_reconfigure/issues/90))
- Use safe YAML loader ([#89](https://github.com/ros-visualization/rqt_reconfigure/issues/89))
- Don’t process scroll events unless specifically focused ([#88](https://github.com/ros-visualization/rqt_reconfigure/issues/88))
- Fix node selection from command line ([#87](https://github.com/ros-visualization/rqt_reconfigure/issues/87))
- Add pytest.ini so local tests don’t display warning ([#91](https://github.com/ros-visualization/rqt_reconfigure/issues/91))
- Support PEP 338 invocation of rqt\_reconfigure ([#85](https://github.com/ros-visualization/rqt_reconfigure/issues/85))
- Fixed package to run with ros2 run ([#81](https://github.com/ros-visualization/rqt_reconfigure/issues/81))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael Jeronimo, Scott K Logan

<a id="rqt-service-caller"></a>

## [rqt\_service\_caller](https://github.com/ros-visualization/rqt_service_caller/tree/crystal-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#13](https://github.com/ros-visualization/rqt_service_caller/issues/13))
- ignore services that don’t use the SRV\_MODE (‘srv’) ([#20](https://github.com/ros-visualization/rqt_service_caller/issues/20))
- Contributors: Alejandro Hernández Cordero, William Woodall

<a id="rqt-shell"></a>

## [rqt\_shell](https://github.com/ros-visualization/rqt_shell/tree/crystal-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#11](https://github.com/ros-visualization/rqt_shell/issues/11))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-srv"></a>

## [rqt\_srv](https://github.com/ros-visualization/rqt_srv/tree/crystal-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#4](https://github.com/ros-visualization/rqt_srv/issues/4))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-top"></a>

## [rqt\_top](https://github.com/ros-visualization/rqt_top/tree/crystal-devel/CHANGELOG.rst)

- Changed the build type to ament\_python and fixed package to run with ros2 run ([#8](https://github.com/ros-visualization/rqt_top/issues/8))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-topic"></a>

## [rqt\_topic](https://github.com/ros-visualization/rqt_topic/tree/dashing-devel/CHANGELOG.rst)

- Add pytest.ini to silence warnings when running locally.
- Fix warnings pointed out by flake8.
- Created an entry-point for rqt\_topic in setup.py ([#16](https://github.com/ros-visualization/rqt_topic/issues/16))
- Fix flake8 errors and add linter tests ([#28](https://github.com/ros-visualization/rqt_topic/issues/28))
- Update Open Robotics Maintainer ([#26](https://github.com/ros-visualization/rqt_topic/issues/26))
- Use raw / non-string value for ordering ([#23](https://github.com/ros-visualization/rqt_topic/issues/23))
- Support order fields as defined in message ([#22](https://github.com/ros-visualization/rqt_topic/issues/22))
- Fix the type cell value for sequence items ([#21](https://github.com/ros-visualization/rqt_topic/issues/21))
- Updated version package and license in setup.py ([#17](https://github.com/ros-visualization/rqt_topic/issues/17))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, Scott K Logan

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/galactic/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Pass `-Wl,--no-as-needed` for system dependencies of Connext 5.3.1.
- Set `IMPORTED_NO_SONAME true` for Connext 5.3.1 imported library target.
- Add `<buildtool_export_depend>` for `ament_cmake`.
- Add `<depend>` for `rti-connext-dds-5.3.1`
- Add dependency from rti-connext-dds-5.3.1.
- Initial release.

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/galactic/rttest/CHANGELOG.rst)

- Fix up nonsensical handling of NULL in rttest\_get\_{params,statistics} ([#107](https://github.com/ros2/realtime_support/issues/107))
- Remove “struct” from rttest\_sample\_buffer variable declaration. ([#105](https://github.com/ros2/realtime_support/issues/105))
- Convert the sample buffer to a vector. ([#104](https://github.com/ros2/realtime_support/issues/104))
- Use strdup instead of strlen/strcpy dance. ([#100](https://github.com/ros2/realtime_support/issues/100))
- Enable basic warnings in rttest ([#99](https://github.com/ros2/realtime_support/issues/99))
- Only copy an rttest\_sample\_buffer if it is not nullptr. ([#98](https://github.com/ros2/realtime_support/issues/98))
- Convert timespec to uint64 not long and vice versa ([#94](https://github.com/ros2/realtime_support/issues/94)) ([#96](https://github.com/ros2/realtime_support/issues/96))
- Fix standard deviation overflow([#95](https://github.com/ros2/realtime_support/issues/95)) ([#97](https://github.com/ros2/realtime_support/issues/97))
- Contributors: Audrow Nash, Chris Lalancette, y-okumura-isp

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/galactic/rviz2/CHANGELOG.rst)

- Use “%s” as format string literal in logging macros ([#633](https://github.com/ros2/rviz/issues/633))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Move and update documentation for ROS 2 ([#600](https://github.com/ros2/rviz/issues/600))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="rviz-assimp-vendor"></a>

## [rviz\_assimp\_vendor](https://github.com/ros2/rviz/tree/galactic/rviz_assimp_vendor/CHANGELOG.rst)

- Always preserve source permissions in vendor packages ([#647](https://github.com/ros2/rviz/issues/647))
- Add an override flag to force vendored build ([#642](https://github.com/ros2/rviz/issues/642))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Updated a hack to avoid CMake warning with assimp 5.0.1 and older, applying it cross platforms ([#565](https://github.com/ros2/rviz/issues/565))
- Contributors: Dirk Thomas, Jacob Perron, Scott K Logan

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/galactic/rviz_common/CHANGELOG.rst)

- Add visualization\_frame to the public API ([#660](https://github.com/ros2/rviz/issues/660))
- Add ViewPicker::get3DPatch to the public API ([#657](https://github.com/ros2/rviz/issues/657))
- Fix byte indexing for depth patch pixels ([#661](https://github.com/ros2/rviz/issues/661))
- fix toolbar vanishing when pressing escape ([#656](https://github.com/ros2/rviz/issues/656))
- Expose VisualizationManager and YamlConfigReader to the public API ([#649](https://github.com/ros2/rviz/issues/649))
- Use the stack for the classes in the property test. ([#644](https://github.com/ros2/rviz/issues/644))
- Check that the views\_man\_ and views\_man\_->getCurrent() are not nullptr. ([#634](https://github.com/ros2/rviz/issues/634))
- Fix for mousewheel to zoom in/out ([#623](https://github.com/ros2/rviz/issues/623))
- Ensure rviz\_common::MessageFilterDisplay processes messages in the main thread ([#620](https://github.com/ros2/rviz/issues/620))
- Fix render window disppearing after saving image ([#611](https://github.com/ros2/rviz/issues/611))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- TimePanel port ([#599](https://github.com/ros2/rviz/issues/599))
- Upgrade to tinyxml2 for rviz ([#418](https://github.com/ros2/rviz/issues/418))
- Fix segfault on changing filter size for non-existent topic ([#597](https://github.com/ros2/rviz/issues/597))
- improve color support for themes ([#590](https://github.com/ros2/rviz/issues/590))
- Fix topic IntProperty number ranges ([#596](https://github.com/ros2/rviz/issues/596))
- Switch to nullptr everywhere. ([#592](https://github.com/ros2/rviz/issues/592))
- Expose MessageFilterDisplay’s queue size ([#593](https://github.com/ros2/rviz/issues/593))
- Filter topics in drop down menu ([#591](https://github.com/ros2/rviz/issues/591))
- rviz\_common: Remove variadic macro warning check ([#421](https://github.com/ros2/rviz/issues/421))
- Use retriever.hpp ([#589](https://github.com/ros2/rviz/issues/589))
- Fix the order of destructors ([#572](https://github.com/ros2/rviz/issues/572))
- Changed to not install test header files in rviz\_rendering. ([#564](https://github.com/ros2/rviz/issues/564))
- Fixed alphabetical include order ([#563](https://github.com/ros2/rviz/issues/563))
- Changed to avoid trying to moc generate `env_config.hpp` file. ([#550](https://github.com/ros2/rviz/issues/550))
- Contributors: Audrow Nash, Chen Lihui, Chris Lalancette, Jacob Perron, Jafar Abdi, Joseph Schornak, Karsten Knese, Martin Idel, Michael Ferguson, Michael Jeronimo, Michel Hidalgo, Nico Neumann, Rich Mattes, Shane Loretz, ipa-fez, spiralray

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/galactic/rviz_default_plugins/CHANGELOG.rst)

- Add ViewPicker::get3DPatch to the public API ([#657](https://github.com/ros2/rviz/issues/657))
- Allow to zoom more with orbit controller ([#654](https://github.com/ros2/rviz/issues/654))
- Fix possible nullptr access in robot\_joint.cpp. ([#636](https://github.com/ros2/rviz/issues/636))
- Fix for mousewheel to zoom in/out ([#623](https://github.com/ros2/rviz/issues/623))
- Make the types explicit in quaternion\_helper.hpp. ([#625](https://github.com/ros2/rviz/issues/625))
- Update status message by removing colon or adjust colon position ([#624](https://github.com/ros2/rviz/issues/624))
- Do not use assume every RenderPanel has a ViewController. ([#613](https://github.com/ros2/rviz/issues/613))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- TimePanel port ([#599](https://github.com/ros2/rviz/issues/599))
- Upgrade to tinyxml2 for rviz ([#418](https://github.com/ros2/rviz/issues/418))
- Use retriever.hpp ([#589](https://github.com/ros2/rviz/issues/589))
- Added covariance settings to set pose estimate ([#569](https://github.com/ros2/rviz/issues/569))
- use reference in range loops to avoid copy ([#577](https://github.com/ros2/rviz/issues/577))
- Changed to not install test header files in rviz\_rendering. ([#564](https://github.com/ros2/rviz/issues/564))
- Changed to use a dedicated TransformListener thread. ([#551](https://github.com/ros2/rviz/issues/551))
- Suppressed warnings when building with older Qt versions. ([#562](https://github.com/ros2/rviz/issues/562))
- Restored compatibility with older Qt versions ([#561](https://github.com/ros2/rviz/issues/561))
- Contributors: Chen Lihui, Chris Lalancette, Dirk Thomas, Jacob Perron, Joseph Schornak, Martin Idel, Matthijs den Toom, Michel Hidalgo, Nico Neumann, Shane Loretz, Victor Lamoine, ymd-stella

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/galactic/rviz_ogre_vendor/CHANGELOG.rst)

- Always preserve source permissions in vendor packages ([#647](https://github.com/ros2/rviz/issues/647))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Pass through CMAKE\_{C,CXX}\_FLAGS to OGRE build ([#587](https://github.com/ros2/rviz/issues/587))
- Contributors: Jacob Perron, Scott K Logan

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/galactic/rviz_rendering/CHANGELOG.rst)

- reset current line width when calculating text width ([#655](https://github.com/ros2/rviz/issues/655))
- Silence a dead store warning. ([#643](https://github.com/ros2/rviz/issues/643))
- Fix a memory leak when using the ResourceIOSystem. ([#641](https://github.com/ros2/rviz/issues/641))
- Revert “Support loading meshes other than .mesh and .stl with package URIs ([#610](https://github.com/ros2/rviz/issues/610))” ([#638](https://github.com/ros2/rviz/issues/638))
- Prevent rviz\_rendering::AssimpLoader from loading materials twice. ([#622](https://github.com/ros2/rviz/issues/622))
- Support loading meshes other than .mesh and .stl with package URIs ([#610](https://github.com/ros2/rviz/issues/610))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Switch to nullptr everywhere. ([#592](https://github.com/ros2/rviz/issues/592))
- Use retriever.hpp ([#589](https://github.com/ros2/rviz/issues/589))
- Avoid hidding base class getRenderOperation in PointCloudRenderable ([#586](https://github.com/ros2/rviz/issues/586))
- Changed to not install test header files in rviz\_rendering. ([#564](https://github.com/ros2/rviz/issues/564))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, ipa-fez

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/galactic/rviz_rendering_tests/CHANGELOG.rst)

- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Use retriever.hpp ([#589](https://github.com/ros2/rviz/issues/589))
- Changed to not install test header files in rviz\_rendering. ([#564](https://github.com/ros2/rviz/issues/564))
- Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/galactic/rviz_visual_testing_framework/CHANGELOG.rst)

- Quiet a clang warning about a Qt memory leak. ([#651](https://github.com/ros2/rviz/issues/651))
- use rcutils\_get\_env. ([#609](https://github.com/ros2/rviz/issues/609))
- Add linters and use ament\_lint\_auto ([#608](https://github.com/ros2/rviz/issues/608))
- Update maintainers ([#607](https://github.com/ros2/rviz/issues/607))
- Contributors: Chris Lalancette, Jacob Perron, tomoya

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/sensor_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Fix PointCloud2Iterator namespacing in docs ([#139](https://github.com/ros2/common_interfaces/issues/139))
- Add coverage/performance to qd for sensor\_msgs ([#137](https://github.com/ros2/common_interfaces/issues/137))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Missing cstring header for memcpy in fill\_image.hpp ([#126](https://github.com/ros2/common_interfaces/issues/126))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Andre Nguyen, Chris Lalancette, Jose Luis Rivero, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/galactic/sensor_msgs_py/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg ([#150](https://github.com/ros2/common_interfaces/issues/150))
- Port of point\_cloud2.py from ROS1 to ROS2. As seperate pkg. ([#128](https://github.com/ros2/common_interfaces/issues/128))
- Contributors: Ivan Santiago Paunovic, Sebastian Grans

<a id="shape-msgs"></a>

## [shape\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/shape_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="shared-queues-vendor"></a>

## [shared\_queues\_vendor](https://github.com/ros2/rosbag2/tree/galactic/shared_queues_vendor/CHANGELOG.rst)

- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Contributors: Emerson Knapp, Michael Jeronimo

<a id="spdlog-vendor"></a>

## [spdlog\_vendor](https://github.com/ros2/spdlog_vendor/tree/galactic/CHANGELOG.rst)

- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#24](https://github.com/ros2/spdlog_vendor/issues/24))
- Update to spdlog 1.8.2 ([#23](https://github.com/ros2/spdlog_vendor/issues/23))
- Remove a stale TODO ([#22](https://github.com/ros2/spdlog_vendor/issues/22))
- Always preserve source permissions in vendor packages ([#20](https://github.com/ros2/spdlog_vendor/issues/20))
- Remove unnecessary call to find\_package(PATCH) ([#18](https://github.com/ros2/spdlog_vendor/issues/18))
- Updated QD to 1 ([#16](https://github.com/ros2/spdlog_vendor/issues/16))
- bump spdlog version to 1.6.1 ([#15](https://github.com/ros2/spdlog_vendor/issues/15))
- Bump QD to level 3 and updated QD ([#14](https://github.com/ros2/spdlog_vendor/issues/14))
- Add Security Vulnerability Policy pointing to REP-2006. ([#13](https://github.com/ros2/spdlog_vendor/issues/13))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, Scott K Logan, shonigmann

<a id="sqlite3-vendor"></a>

## [sqlite3\_vendor](https://github.com/ros2/rosbag2/tree/galactic/sqlite3_vendor/CHANGELOG.rst)

- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Always preserve source permissions in vendor packages ([#645](https://github.com/ros2/rosbag2/issues/645))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- use interface\_include\_directories ([#426](https://github.com/ros2/rosbag2/issues/426))
- Contributors: Emerson Knapp, Karsten Knese, Michael Jeronimo, Scott K Logan

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/galactic/sros2/CHANGELOG.rst)

- Skip mypy test on platforms using importlib\_resources ([#258](https://github.com/ros2/sros2/issues/258))
- Enable topic “ros\_discovery\_info” for rmw\_connextdds ([#253](https://github.com/ros2/sros2/issues/253))
- Declare missing dependency on python3-importlib-resources ([#249](https://github.com/ros2/sros2/issues/249)) Co-authored-by: <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Fix namedtuple names. ([#250](https://github.com/ros2/sros2/issues/250))
- parameter\_events topic is now absolute (#233) Signed-off-by: Mikael Arguedas <[mikael.arguedas@gmail.com](mailto:mikael.arguedas%40gmail.com)>
- Expose keystore operations in public API ([#241](https://github.com/ros2/sros2/issues/241))
- add cyclonedds to the list of rmw using graph info topics ([#231](https://github.com/ros2/sros2/issues/231))
- Add scope parameter ([#230](https://github.com/ros2/sros2/issues/230))
- Fix name of argument passed to NodeStrategy ([#227](https://github.com/ros2/sros2/issues/227))
- Remove the use of pkg\_resources. ([#225](https://github.com/ros2/sros2/issues/225))
- Make use of ros\_testing to test policy generation. ([#214](https://github.com/ros2/sros2/issues/214))
- Add pytest.ini so local tests don’t display warning ([#224](https://github.com/ros2/sros2/issues/224))
- Fix list keys verb ([#219](https://github.com/ros2/sros2/issues/219))
- Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron, Jose Luis Rivero, Kyle Fazzari, Michel Hidalgo, Mikael Arguedas, Scott K Logan

<a id="statistics-msgs"></a>

## [statistics\_msgs](https://github.com/ros2/rcl_interfaces/tree/galactic/statistics_msgs/CHANGELOG.rst)

- Updating Quality Declaration ([#120](https://github.com/ros2/rcl_interfaces/issues/120))
- Update quality declaration to QL 1. ([#116](https://github.com/ros2/rcl_interfaces/issues/116))
- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Increase Quality level of packages to 3 ([#108](https://github.com/ros2/rcl_interfaces/issues/108))
- Add Security Vulnerability Policy pointing to REP-2006. ([#106](https://github.com/ros2/rcl_interfaces/issues/106))
- Updating QD to reflect package versions ([#107](https://github.com/ros2/rcl_interfaces/issues/107))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="std-msgs"></a>

## [std\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/std_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145)) Co-authored-by: Simon Honigmann <[shonigmann@blueorigin.com](mailto:shonigmann%40blueorigin.com)>
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="std-srvs"></a>

## [std\_srvs](https://github.com/ros2/common_interfaces/tree/galactic/std_srvs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="stereo-msgs"></a>

## [stereo\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/stereo_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="tango-icons-vendor"></a>

## [tango\_icons\_vendor](https://github.com/ros-visualization/tango_icons_vendor/tree/galactic/CHANGELOG.rst)

- Add exec\_depend on tango-icon-theme system package ([#8](https://github.com/ros-visualization/tango_icons_vendor/issues/8))
- Added common linters ([#7](https://github.com/ros-visualization/tango_icons_vendor/issues/7)) \* Added common linters \* Fixed license in package.xml
- Remaned package qt\_gui\_icons -> tango\_icons\_vendor ([#4](https://github.com/ros-visualization/tango_icons_vendor/issues/4)) \* Remaned package qt\_gui\_icons -> tango\_icons\_vendor \* Updated CMake var to install tango icons: INSTALL\_TANGO\_ICONS \* Added cmake option INSTALL\_TANGO\_ICONS \* Fixed logic \* set INSTALL\_TANGO\_ICONS\_DEFAULT\_VALUE to option \* Make linters happy
- Updated link on the description ([#6](https://github.com/ros-visualization/tango_icons_vendor/issues/6))
- Updated the maintainer ([#5](https://github.com/ros-visualization/tango_icons_vendor/issues/5))
- Version 0.0.0 this package was never released ([#3](https://github.com/ros-visualization/tango_icons_vendor/issues/3))
- Install icons by default on macOS too ([#1](https://github.com/ros-visualization/tango_icons_vendor/issues/1))
- Updating package.xml
- fixup! Install tango icons
- Adding icons
- Install tango icons
- Contributors: Alejandro Hernández Cordero, Scott K Logan, Stephen, Stephen Brawner

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/galactic/test_cli/CHANGELOG.rst)

- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Enable -Wall, -Wextra, and -Wpedantic. ([#447](https://github.com/ros2/system_tests/issues/447))
- Contributors: Audrow Nash, Jacob Perron

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/galactic/test_cli_remapping/CHANGELOG.rst)

- Fix test\_cli\_remapping flaky test. ([#470](https://github.com/ros2/system_tests/issues/470))
- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Enable -Wall, -Wextra, and -Wpedantic. ([#448](https://github.com/ros2/system_tests/issues/448))
- Contributors: Audrow Nash, Jacob Perron, Shane Loretz

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/galactic/test_communication/CHANGELOG.rst)

- Add support for rmw\_connextdds. ([#463](https://github.com/ros2/system_tests/issues/463))
- Kill off the ros2 daemon before running tests. ([#460](https://github.com/ros2/system_tests/pull/460))
- Remove Opensplice from test\_communication. ([#460](https://github.com/ros2/system_tests/pull/460))
- Make TestMessageSerialization robust to missed messages. ([#456](https://github.com/ros2/system_tests/issues/456))
- Add corresponding rclcpp::shutdown. ([#455](https://github.com/ros2/system_tests/issues/455))
- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron, Stephen Brawner

<a id="test-interface-files"></a>

## [test\_interface\_files](https://github.com/ros2/test_interface_files/tree/galactic/CHANGELOG.rst)

- Update maintainer ([#13](https://github.com/ros2/test_interface_files/issues/13))
- Contributors: Jacob Perron

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/galactic/test_launch_ros/CHANGELOG.rst)

- Add a package marker to test\_launch\_ros. ([#226](https://github.com/ros2/launch_ros/issues/226))
- Re-order shutdown vs node destruction ([#213](https://github.com/ros2/launch_ros/issues/213))
- Increase test\_composable\_node\_container timeout ([#195](https://github.com/ros2/launch_ros/issues/195))
- Remove constructors arguments deprecated since Foxy ([#190](https://github.com/ros2/launch_ros/issues/190))
- Merge pull request [#183](https://github.com/ros2/launch_ros/issues/183) from ros2/update-maintainers
- Move previous maintainer to <author>
- Update the package.xml files with the latest Open Robotics maintainers
- Handle any substitution types for SetParameter name argument ([#182](https://github.com/ros2/launch_ros/issues/182))
- Address security bug in yaml loading ([#175](https://github.com/ros2/launch_ros/issues/175))
- Resolve TODO in test ([#172](https://github.com/ros2/launch_ros/issues/172))
- Fix case where list of composable nodes is zero ([#173](https://github.com/ros2/launch_ros/issues/173))
- Do not use event handler for loading composable nodes ([#170](https://github.com/ros2/launch_ros/issues/170))
- Fix race with launch context changes when loading composable nodes ([#166](https://github.com/ros2/launch_ros/issues/166))
- Substitutions in parameter files ([#168](https://github.com/ros2/launch_ros/issues/168))
- Fix problems when parsing a `Command` `Substitution` as a parameter value ([#137](https://github.com/ros2/launch_ros/issues/137))
- Drop double single-quoted params. ([#164](https://github.com/ros2/launch_ros/issues/164))
- Add a way to set remapping rules for all nodes in the same scope ([#163](https://github.com/ros2/launch_ros/issues/163))
- Fix ComposableNode ignoring PushRosNamespace actions ([#162](https://github.com/ros2/launch_ros/issues/162))
- Add a SetParameter action that sets a parameter to all nodes in the same scope ([#158](https://github.com/ros2/launch_ros/issues/158))
- Make namespace parameter mandatory in LifecycleNode constructor ([#157](https://github.com/ros2/launch_ros/issues/157))
- Avoid using a wildcard to specify parameters if possible ([#154](https://github.com/ros2/launch_ros/issues/154))
- Remove the loop parameter from async.sleep. ([#155](https://github.com/ros2/launch_ros/issues/155))
- Fix no specified namespace ([#153](https://github.com/ros2/launch_ros/issues/153))
- Fix test\_node\_frontend ([#146](https://github.com/ros2/launch_ros/issues/146))
- Add pytest.ini so local tests don’t display warning ([#152](https://github.com/ros2/launch_ros/issues/152))
- Contributors: Chris Lalancette, Dan Rose, Ivan Santiago Paunovic, Jacob Perron, Michael Jeronimo, Michel Hidalgo, Scott K Logan, Víctor Mayoral Vilches

<a id="test-launch-testing"></a>

## [test\_launch\_testing](https://github.com/ros2/launch/tree/galactic/test_launch_testing/CHANGELOG.rst)

- Update package maintainers ([#465](https://github.com/ros2/launch/issues/465))
- Add pytest.ini to test\_launch\_testing so tests succeed locally. ([#431](https://github.com/ros2/launch/issues/431))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/galactic/test_msgs/CHANGELOG.rst)

- Update package maintainers. ([#112](https://github.com/ros2/rcl_interfaces/issues/112))
- Contributors: Chris Lalancette

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/galactic/test_quality_of_service/CHANGELOG.rst)

- Add support for rmw\_connextdds. ([#463](https://github.com/ros2/system_tests/issues/463))
- Run QoS tests. ([#441](https://github.com/ros2/system_tests/issues/441))
- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Contributors: Andrea Sorbini, Jacob Perron, Michel Hidalgo

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/galactic/test_rclcpp/CHANGELOG.rst)

- Reenable test that used to be flaky. ([#467](https://github.com/ros2/system_tests/issues/467))
- Get\_parameters\_service\_ should return empty if allow\_undeclared\_ is false. ([#466](https://github.com/ros2/system_tests/issues/466))
- Make test pass after rclcpp#1532. ([#465](https://github.com/ros2/system_tests/issues/465))
- Adapt tests to statically typed parameters. ([#462](https://github.com/ros2/system_tests/issues/462))
- Guard against TOCTTOU with rclcpp::ok and rclcpp:spin\_some. ([#459](https://github.com/ros2/system_tests/issues/459))
- Update parameter client test with timeout. ([#457](https://github.com/ros2/system_tests/issues/457))
- Call rclcpp::init and rclcpp::shutdown in each test for test\_rclcpp. ([#454](https://github.com/ros2/system_tests/issues/454))
- Set cppcheck timeout to 400 seconds. ([#453](https://github.com/ros2/system_tests/issues/453))
- Modify to match Waitable interface adding take\_data. ([#444](https://github.com/ros2/system_tests/issues/444))
- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Fix rclcpp timeout subscriber test. ([#440](https://github.com/ros2/system_tests/issues/440)) \* Use nonzero lower bound for timeout checks. \* Relax time tolerance.
- Show numbers of nanseconds in EXPECT with durations. ([#438](https://github.com/ros2/system_tests/issues/438)) \* Show numbers of nanseconds in expect with durations \* Fix syntax
- Remove ament\_pytest dependency from test\_rclcpp. ([#437](https://github.com/ros2/system_tests/issues/437)) It is not used in test\_rclcpp anywhere.
- Contributors: Audrow Nash, Chris Lalancette, Dirk Thomas, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, Stephen Brawner, Tomoya Fujita, tomoya

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/galactic/test_rmw_implementation/CHANGELOG.rst)

- Implement test for subscription loaned messages ([#186](https://github.com/ros2/rmw_implementation/issues/186))
- Remove rmw\_connext\_cpp. ([#183](https://github.com/ros2/rmw_implementation/issues/183))
- Add support for rmw\_connextdds ([#182](https://github.com/ros2/rmw_implementation/issues/182))
- Add function for checking QoS profile compatibility ([#180](https://github.com/ros2/rmw_implementation/issues/180))
- Make sure to initialize the rmw\_message\_sequence after init. ([#175](https://github.com/ros2/rmw_implementation/issues/175))
- Set the value of is\_available before entering the loop ([#173](https://github.com/ros2/rmw_implementation/issues/173))
- Set the return value of rmw\_ret\_t before entering the loop. ([#171](https://github.com/ros2/rmw_implementation/issues/171))
- Add some additional checking that cleanup happens. ([#168](https://github.com/ros2/rmw_implementation/issues/168))
- Add test to check rmw\_send\_response when the client is gone ([#162](https://github.com/ros2/rmw_implementation/issues/162))
- Update maintainers ([#154](https://github.com/ros2/rmw_implementation/issues/154))
- Add fault injection tests to construction/destroy APIs. ([#144](https://github.com/ros2/rmw_implementation/issues/144))
- Add tests bad type\_support implementation ([#152](https://github.com/ros2/rmw_implementation/issues/152))
- Add tests for localhost-only node creation ([#150](https://github.com/ros2/rmw_implementation/issues/150))
- Added rmw\_service\_server\_is\_available tests ([#140](https://github.com/ros2/rmw_implementation/issues/140))
- Use 10x the intraprocess delay to wait for sent requests. ([#148](https://github.com/ros2/rmw_implementation/issues/148))
- Added rmw\_wait, rmw\_create\_wait\_set, and rmw\_destroy\_wait\_set tests ([#139](https://github.com/ros2/rmw_implementation/issues/139))
- Add tests service/client request/response with bad arguments ([#141](https://github.com/ros2/rmw_implementation/issues/141))
- Added test for rmw\_get\_serialized\_message\_size ([#142](https://github.com/ros2/rmw_implementation/issues/142))
- Add service/client construction/destruction API test coverage. ([#138](https://github.com/ros2/rmw_implementation/issues/138))
- Added rmw\_publisher\_allocation and rmw\_subscription\_allocation related tests ([#137](https://github.com/ros2/rmw_implementation/issues/137))
- Add tests take serialized with info bad arguments ([#130](https://github.com/ros2/rmw_implementation/issues/130))
- Add gid API test coverage. ([#134](https://github.com/ros2/rmw_implementation/issues/134))
- Add tests take bad arguments ([#125](https://github.com/ros2/rmw_implementation/issues/125))
- Bump graph API test coverage. ([#132](https://github.com/ros2/rmw_implementation/issues/132))
- Add tests take sequence serialized with bad arguments ([#129](https://github.com/ros2/rmw_implementation/issues/129))
- Add tests take sequence + take sequence with bad arguments ([#128](https://github.com/ros2/rmw_implementation/issues/128))
- Add tests take with info bad arguments ([#126](https://github.com/ros2/rmw_implementation/issues/126))
- Add tests for non-implemented rmw\_take\_\* functions ([#131](https://github.com/ros2/rmw_implementation/issues/131))
- Add tests publish serialized bad arguments ([#124](https://github.com/ros2/rmw_implementation/issues/124))
- Add tests publish bad arguments ([#123](https://github.com/ros2/rmw_implementation/issues/123))
- Add tests non-implemented functions + loan bad arguments ([#122](https://github.com/ros2/rmw_implementation/issues/122))
- Add missing empty topic name tests. ([#136](https://github.com/ros2/rmw_implementation/issues/136))
- Add rmw\_get\_serialization\_format() smoke test. ([#133](https://github.com/ros2/rmw_implementation/issues/133))
- Complete publisher/subscription QoS query API test coverage. ([#120](https://github.com/ros2/rmw_implementation/issues/120))
- Remove duplicate assertions ([#121](https://github.com/ros2/rmw_implementation/issues/121))
- Add publisher/subscription matched count API test coverage. ([#119](https://github.com/ros2/rmw_implementation/issues/119))
- Add serialize/deserialize API test coverage. ([#118](https://github.com/ros2/rmw_implementation/issues/118))
- Add subscription API test coverage. ([#117](https://github.com/ros2/rmw_implementation/issues/117))
- Extend publisher API test coverage ([#115](https://github.com/ros2/rmw_implementation/issues/115))
- Add node construction/destruction API test coverage. ([#112](https://github.com/ros2/rmw_implementation/issues/112))
- Check that rmw\_init() fails if no enclave is given. ([#113](https://github.com/ros2/rmw_implementation/issues/113))
- Add init options API test coverage. ([#108](https://github.com/ros2/rmw_implementation/issues/108))
- Complete init/shutdown API test coverage. ([#107](https://github.com/ros2/rmw_implementation/issues/107))
- Add dependency on ament\_cmake\_gtest ([#109](https://github.com/ros2/rmw_implementation/issues/109))
- Add test\_rmw\_implementation package. ([#106](https://github.com/ros2/rmw_implementation/issues/106))
- Contributors: Alejandro Hernández Cordero, Andrea Sorbini, Chris Lalancette, Geoffrey Biggs, Ivan Santiago Paunovic, Jacob Perron, Jose Tomas Lorente, José Luis Bueno López, Michel Hidalgo, Miguel Company, Shane Loretz

<a id="test-security"></a>

## [test\_security](https://github.com/ros2/system_tests/tree/galactic/test_security/CHANGELOG.rst)

- Add support for rmw\_connextdds. ([#463](https://github.com/ros2/system_tests/issues/463))
- Update deprecated gtest macros. ([#449](https://github.com/ros2/system_tests/issues/449))
- Update maintainers. ([#450](https://github.com/ros2/system_tests/issues/450))
- Run test\_security on CycloneDDS as well. ([#408](https://github.com/ros2/system_tests/issues/408))
- Remove invalid cert folder to force regeneration of certificates. ([#434](https://github.com/ros2/system_tests/issues/434))
- Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Mikael Arguedas

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/galactic/test_tf2/CHANGELOG.rst)

- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Fix a TOCTTOU race in tf2. ([#307](https://github.com/ros2/geometry2/issues/307))
- Fixed memory leak in Buffer::waitForTransform ([#281](https://github.com/ros2/geometry2/issues/281))
- relax test timings to pass with Connext ([#304](https://github.com/ros2/geometry2/issues/304))
- Explicitly initialize instances of tf2::Duration ([#291](https://github.com/ros2/geometry2/issues/291))
- Generate callbacks after updating message\_ ([#274](https://github.com/ros2/geometry2/issues/274))
- fix test\_static\_publisher in macos ([#284](https://github.com/ros2/geometry2/issues/284))
- Fix up the dependencies in test\_tf2. ([#277](https://github.com/ros2/geometry2/issues/277))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Dirk Thomas, Ivan Santiago Paunovic, Martin Ganeff, Michael Carroll, ymd-stella

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/galactic/tf2/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#394](https://github.com/ros2/geometry2/issues/394))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Active usual compiler warnings in tf2 ([#322](https://github.com/ros2/geometry2/issues/322))
- Cleanups in buffer\_core.cpp. ([#301](https://github.com/ros2/geometry2/issues/301))
- Add PoseWithCovarianceStamped transform support ([#312](https://github.com/ros2/geometry2/issues/312))
- Fix a TOCTTOU race in tf2. ([#307](https://github.com/ros2/geometry2/issues/307))
- Fixed memory leak in Buffer::waitForTransform ([#281](https://github.com/ros2/geometry2/issues/281))
- Add common linters to tf2. ([#258](https://github.com/ros2/geometry2/issues/258))
- Provide more available error messaging for nonexistent and invalid frames in canTransform ([ros2 #187](https://github.com/ros2/geometry2/issues/187))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan Santiago Paunovic, Joshua Whitley, Martin Ganeff

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/galactic/tf2_bullet/CHANGELOG.rst)

- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Suppress compiler warning on Centos ([#290](https://github.com/ros2/geometry2/issues/290))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael Carroll

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/galactic/tf2_eigen/CHANGELOG.rst)

- Fix linter errors ([#385](https://github.com/ros2/geometry2/issues/385))
- Fix up the style in tf2\_eigen. ([#378](https://github.com/ros2/geometry2/issues/378))
- Fix doTransform with Eigen Quaternion ([#369](https://github.com/ros2/geometry2/issues/369))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Contributors: Audrow Nash, Bjar Ne, Chris Lalancette, Ivan Santiago Paunovic

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/galactic/tf2_eigen_kdl/CHANGELOG.rst)

- fix order of find eigen3\_cmake\_module & find eigen3 ([#344](https://github.com/ros2/geometry2/issues/344))
- Update package.xml ([#333](https://github.com/ros2/geometry2/issues/333))
- Port eigen\_kdl.h/cpp to ROS2 ([#311](https://github.com/ros2/geometry2/issues/311))
- Contributors: Ahmed Sobhy, Jafar Abdi

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/galactic/tf2_geometry_msgs/CHANGELOG.rst)

- Fix doTransform with Eigen Quaternion ([#369](https://github.com/ros2/geometry2/issues/369))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Add PoseWithCovarianceStamped transform support ([#312](https://github.com/ros2/geometry2/issues/312))
- Don’t install python tf2\_geometry\_msgs ([#299](https://github.com/ros2/geometry2/issues/299)) It hasn’t been ported yet. Closes <https://github.com/ros2/geometry2/issues/285>
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210)) \* Split tf2\_ros in tf2\_ros and tf2\_ros\_py
- Contributors: Alejandro Hernández Cordero, Bjar Ne, Chris Lalancette, Ivan Santiago Paunovic, Joshua Whitley, Shane Loretz

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/galactic/tf2_kdl/CHANGELOG.rst)

- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan Santiago Paunovic

<a id="tf2-msgs"></a>

## [tf2\_msgs](https://github.com/ros2/geometry2/tree/galactic/tf2_msgs/CHANGELOG.rst)

- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/galactic/tf2_py/CHANGELOG.rst)

- Adapt to Python 3.9 ([#362](https://github.com/ros2/geometry2/issues/362))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Add in pytest.ini so tests succeed locally. ([#280](https://github.com/ros2/geometry2/issues/280))
- Contributors: Chris Lalancette, Homalozoa X

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/galactic/tf2_ros/CHANGELOG.rst)

- Guard against access to null node pointer ([#393](https://github.com/ros2/geometry2/issues/393))
- Allow to reconfigure durability for /tf topic broadcaster/listener ([#383](https://github.com/ros2/geometry2/issues/383))
- Fix the rcl type used in the time jump. ([#391](https://github.com/ros2/geometry2/issues/391))
- Fix linter errors ([#385](https://github.com/ros2/geometry2/issues/385))
- fix accessing freed resources ([#386](https://github.com/ros2/geometry2/issues/386))
- Allow reconfiguring qos of tf and tf\_static topics through parameters ([#381](https://github.com/ros2/geometry2/issues/381))
- Replace ROS\_\* logging macros and use RCLCPP\_\* instead ([#380](https://github.com/ros2/geometry2/issues/380))
- Improve message filters error messages ([#364](https://github.com/ros2/geometry2/issues/364))
- Clarify the role of child\_frame\_id and header.frame\_id in the documentation. ([#345](https://github.com/ros2/geometry2/issues/345))
- Remove usage of deprecated rclcpp::Duration constructor ([#340](https://github.com/ros2/geometry2/issues/340))
- Remove messages\_count member from tf2\_ros::MessageFilter. ([#335](https://github.com/ros2/geometry2/issues/335))
- Style fixup in tf2\_ros. ([#325](https://github.com/ros2/geometry2/issues/325))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Update goal response callback signature ([#323](https://github.com/ros2/geometry2/issues/323))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Fixed memory leak in Buffer::waitForTransform ([#281](https://github.com/ros2/geometry2/issues/281))
- fix time-reset test with Connext ([#306](https://github.com/ros2/geometry2/issues/306))
- reenable FrameGraph server ([#198](https://github.com/ros2/geometry2/issues/198))
- Use the usual style of parameters for static\_transform\_program ([#300](https://github.com/ros2/geometry2/issues/300))
- Make static\_transform\_broadcaster consistent with its command line description ([#294](https://github.com/ros2/geometry2/issues/294))
- Avoid using invalid std::list iterators ([#293](https://github.com/ros2/geometry2/issues/293))
- Generate callbacks after updating message\_ ([#274](https://github.com/ros2/geometry2/issues/274))
- Moved unique\_lock of messages\_mutex\_ to guarantee pointer ([#279](https://github.com/ros2/geometry2/issues/279))
- Fix dependencies in tf2\_ros. ([#269](https://github.com/ros2/geometry2/issues/269))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Dirk Thomas, Hunter L. Allen, Ivan Santiago Paunovic, Jacob Perron, Kazunari Tanaka, Martin Ganeff, Michael Carroll, Vikas Dhiman, ymd-stella

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/galactic/tf2_ros_py/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403)) ([#404](https://github.com/ros2/geometry2/issues/404))
- Use global namespace for TransformListener topics ([#390](https://github.com/ros2/geometry2/issues/390))
- Fix indentation of a comment in buffer.py ([#371](https://github.com/ros2/geometry2/issues/371))
- Update rclpy.Rate TODO with url to issue ([#324](https://github.com/ros2/geometry2/issues/324))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Add deprecation warnings to lookup\_transform to handle the passing of the incorrect Time object. ([#319](https://github.com/ros2/geometry2/issues/319))
- change signature to show true arguments ([#321](https://github.com/ros2/geometry2/issues/321))
- Handle when None passed to qos argument in the constructor of TransformBroadcaster. ([#320](https://github.com/ros2/geometry2/issues/320))
- Add type hints to tf2\_ros\_py code([#275](https://github.com/ros2/geometry2/issues/275)) ([#315](https://github.com/ros2/geometry2/issues/315))
- Clear callbacks\_to\_remove variable after removing ([#303](https://github.com/ros2/geometry2/issues/303))
- Fix cache\_time None check in buffer.py ([#297](https://github.com/ros2/geometry2/issues/297))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Matthijs den Toom, ScottMcMichael, surfertas

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/galactic/tf2_sensor_msgs/CHANGELOG.rst)

- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Activate usual compiler warnings and fix errors ([#270](https://github.com/ros2/geometry2/issues/270))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Ivan Santiago Paunovic

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/galactic/tf2_tools/CHANGELOG.rst)

- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403)) ([#404](https://github.com/ros2/geometry2/issues/404))
- Add wait time option to view\_frames ([#374](https://github.com/ros2/geometry2/issues/374))
- Cleanup tf2\_tools to be more modern. ([#351](https://github.com/ros2/geometry2/issues/351))
- Update maintainers of the ros2/geometry2 fork. ([#328](https://github.com/ros2/geometry2/issues/328))
- Address security bug in yaml loading ([#313](https://github.com/ros2/geometry2/issues/313))
- Split tf2\_ros in tf2\_ros and tf2\_ros\_py ([#210](https://github.com/ros2/geometry2/issues/210))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Víctor Mayoral Vilches

<a id="tlsf"></a>

## [tlsf](https://github.com/ros2/tlsf/tree/galactic/tlsf/CHANGELOG.rst)

- Switch to standard \_\_VA\_ARGS\_\_. ([#9](https://github.com/ros2/tlsf/issues/9))
- Enable basic warnings ([#8](https://github.com/ros2/tlsf/issues/8))
- Contributors: Audrow Nash, Chris Lalancette

<a id="tlsf-cpp"></a>

## [tlsf\_cpp](https://github.com/ros2/realtime_support/tree/galactic/tlsf_cpp/CHANGELOG.rst)

- Add in the Apache license to tlsf\_cpp. ([#108](https://github.com/ros2/realtime_support/issues/108))
- Contributors: Chris Lalancette

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/galactic/topic_monitor/CHANGELOG.rst)

- Use is\_alive for threads. ([#510](https://github.com/ros2/demos/issues/510)) ([#513](https://github.com/ros2/demos/issues/513))
- Use underscores instead of dashes in setup.cfg ([#502](https://github.com/ros2/demos/issues/502))
- Change index.ros.org -> docs.ros.org. ([#496](https://github.com/ros2/demos/issues/496))
- Update deprecated qos policy value names ([#468](https://github.com/ros2/demos/issues/468))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michael Jeronimo

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/galactic/topic_statistics_demo/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#496](https://github.com/ros2/demos/issues/496))
- Update logging macros ([#476](https://github.com/ros2/demos/issues/476))
- Update the package.xml files with the latest Open Robotics maintainers ([#466](https://github.com/ros2/demos/issues/466))
- Create new topic statistics demo package ([#454](https://github.com/ros2/demos/issues/454))
- Contributors: Audrow Nash, Chris Lalancette, Michael Jeronimo, Prajakta Gokhale

<a id="tracetools"></a>

## [tracetools](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/galactic/tracetools/CHANGELOG.rst)

- Update QD to be more specific about public API
- Namespace tracetools C++ functions and macros and deprecate current ones
- Add support for rcl\_publish and rclcpp\_publish tracepoints
- Add instrumentation support for linking a timer to a node
- Bring tracetools up to quality level 1
- Add lifecycle node state transition instrumentation
- Do not export tracetools if empty
- Allow disabling tracetools status app
- Contributors: Christophe Bedard, Ingo Lütkebohle, José Antonio Moral

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/galactic/tracetools_launch/CHANGELOG.rst)

- Allow configuring tracing directory through environment variables
- Contributors: Christophe Bedard

<a id="tracetools-test"></a>

## [tracetools\_test](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/galactic/tracetools_test/CHANGELOG.rst)

- Update after namespacing C++ tracetools functions and macros
- Add tests for rcl\_publish and rclcpp\_publish tracepoints
- Allow asserting order of list of events
- Allow skipping test trace cleanup by setting an environment variable
- Add test for timer-node linking instrumentation
- Increased code coverage > 94% as part of QL1
- Add lifecycle node state transition instrumentation test
- Contributors: Alejandro Hernández Cordero, Christophe Bedard, Ingo Lütkebohle

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/galactic/tracetools_trace/CHANGELOG.rst)

- Add support for rcl\_publish and rclcpp\_publish tracepoints
- Fix flake8 blind except error by using more concrete types
- Allow configuring tracing directory through environment variables
- Cleanly stop ros2trace/tracetools\_trace tracing on SIGINT
- Add instrumentation support for linking a timer to a node
- Add lifecycle node state transition instrumentation
- Contributors: Christophe Bedard, Ingo Lütkebohle

<a id="trajectory-msgs"></a>

## [trajectory\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/trajectory_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Finish up API documentation ([#123](https://github.com/ros2/common_interfaces/issues/123))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/galactic-devel/turtlesim/CHANGELOG.rst)

- Ignore key up events in teleop\_turtle\_key on Windows ([#118](https://github.com/ros/ros_tutorials/issues/118))
- Update maintainers ([#106](https://github.com/ros/ros_tutorials/issues/106))
- Update goal response callback signature ([#100](https://github.com/ros/ros_tutorials/issues/100))
- add holonomic motion for turtlesim ([#98](https://github.com/ros/ros_tutorials/issues/98))
- add step value to turtlesim color parameters ([#91](https://github.com/ros/ros_tutorials/issues/91))
- update Foxy turtle ([#90](https://github.com/ros/ros_tutorials/issues/90))
- Contributors: Jacob Perron, Michel Hidalgo, Shane Loretz

<a id="unique-identifier-msgs"></a>

## [unique\_identifier\_msgs](https://github.com/ros2/unique_identifier_msgs/tree/galactic/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org ([#21](https://github.com/ros2/unique_identifier_msgs/issues/21))
- Update QD to QL 1 ([#17](https://github.com/ros2/unique_identifier_msgs/issues/17))
- Update Quality Declaration to QL2. ([#15](https://github.com/ros2/unique_identifier_msgs/issues/15))
- Update Quality level to level 3 ([#13](https://github.com/ros2/unique_identifier_msgs/issues/13))
- Add Security Vulnerability Policy pointing to REP-2006. ([#11](https://github.com/ros2/unique_identifier_msgs/issues/11))
- Contributors: Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/galactic/urdf/CHANGELOG.rst)

- Work around Windows min/max bug. ([#21](https://github.com/ros2/urdf/issues/21))
- Enable -Wall -Wextra -Wpedantic ([#20](https://github.com/ros2/urdf/issues/20))
- Add dependency on TinyXML2 ([#19](https://github.com/ros2/urdf/issues/19))
- Remove TinyXML dependency from urdf. ([#17](https://github.com/ros2/urdf/issues/17))
- Make urdf plugable and revive urdf\_parser\_plugin ([#13](https://github.com/ros2/urdf/issues/13))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/galactic/urdf_parser_plugin/CHANGELOG.rst)

- Export urdfdom\_headers as urdf\_parser\_plugin dependency. ([#25](https://github.com/ros2/urdf/issues/25))
- Make urdf plugable and revive urdf\_parser\_plugin ([#13](https://github.com/ros2/urdf/issues/13))
- Contributors: Michel Hidalgo, Shane Loretz

<a id="visualization-msgs"></a>

## [visualization\_msgs](https://github.com/ros2/common_interfaces/tree/galactic/visualization_msgs/CHANGELOG.rst)

- Change index.ros.org -> docs.ros.org. ([#149](https://github.com/ros2/common_interfaces/issues/149))
- updating quality declaration links (re: [ros2/docs.ros2.org#52](https://github.com/ros2/docs.ros2.org/issues/52)) ([#145](https://github.com/ros2/common_interfaces/issues/145))
- Update QDs to QL 1 ([#135](https://github.com/ros2/common_interfaces/issues/135))
- Update package maintainers. ([#132](https://github.com/ros2/common_interfaces/issues/132))
- Updated Quality Level to 2 ([#131](https://github.com/ros2/common_interfaces/issues/131))
- Update Quality levels to level 3 ([#124](https://github.com/ros2/common_interfaces/issues/124))
- Add Security Vulnerability Policy pointing to REP-2006. ([#120](https://github.com/ros2/common_interfaces/issues/120))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michel Hidalgo, Stephen Brawner, brawner, shonigmann

<a id="yaml-cpp-vendor"></a>

## [yaml\_cpp\_vendor](https://github.com/ros2/yaml_cpp_vendor/tree/galactic/CHANGELOG.rst)

- Always preserve source permissions in vendor packages ([#22](https://github.com/ros2/yaml_cpp_vendor/issues/22))
- Add an override flag to force vendored build ([#21](https://github.com/ros2/yaml_cpp_vendor/issues/21))
- Reapply “Use system installed yaml-cpp 0.6 if available ([#8](https://github.com/ros2/yaml_cpp_vendor/issues/8))” ([#16](https://github.com/ros2/yaml_cpp_vendor/issues/16))
- Revert “Use system installed yaml-cpp 0.6 if available ([#8](https://github.com/ros2/yaml_cpp_vendor/issues/8))” ([#15](https://github.com/ros2/yaml_cpp_vendor/issues/15))
- Use system installed yaml-cpp 0.6 if available ([#8](https://github.com/ros2/yaml_cpp_vendor/issues/8))
- Contributors: Ivan Santiago Paunovic, Scott K Logan, Sean Yen

<a id="zstd-vendor"></a>

## [zstd\_vendor](https://github.com/ros2/rosbag2/tree/galactic/zstd_vendor/CHANGELOG.rst)

- Explicitly add emersonknapp as maintainer ([#692](https://github.com/ros2/rosbag2/issues/692))
- Always preserve source permissions in vendor packages ([#645](https://github.com/ros2/rosbag2/issues/645))
- Zstd should not install internal headers - some of them try include others that aren’t installed. We don’t use them. Avoid the situation ([#631](https://github.com/ros2/rosbag2/issues/631))
- Patch zstd 1.4.4 to include cmake\_minimum\_version bump to 2.8.12 ([#579](https://github.com/ros2/rosbag2/issues/579))
- Update the package.xml files with the latest Open Robotics maintainers ([#535](https://github.com/ros2/rosbag2/issues/535))
- Contributors: Emerson Knapp, Michael Jeronimo, Scott K Logan
