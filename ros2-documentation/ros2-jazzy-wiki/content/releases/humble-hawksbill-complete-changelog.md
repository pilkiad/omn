---
title: "Humble Hawksbill changelog"
docname: "Releases/Humble-Hawksbill-Complete-Changelog"
source: "Releases/Humble-Hawksbill-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="humble-hawksbill-changelog"></a>

# Humble Hawksbill changelog

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
- [demo\_nodes\_cpp](#demo-nodes-cpp)
- [demo\_nodes\_cpp\_native](#demo-nodes-cpp-native)
- [demo\_nodes\_py](#demo-nodes-py)
- [diagnostic\_msgs](#diagnostic-msgs)
- [domain\_coordinator](#domain-coordinator)
- [dummy\_map\_server](#dummy-map-server)
- [dummy\_robot\_bringup](#dummy-robot-bringup)
- [dummy\_sensors](#dummy-sensors)
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
- [geometry\_msgs](#geometry-msgs)
- [google\_benchmark\_vendor](#google-benchmark-vendor)
- [image\_tools](#image-tools)
- [image\_transport](#image-transport)
- [interactive\_markers](#interactive-markers)
- [intra\_process\_demo](#intra-process-demo)
- [kdl\_parser](#kdl-parser)
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
- [message\_filters](#message-filters)
- [mimick\_vendor](#mimick-vendor)
- [nav\_msgs](#nav-msgs)
- [pendulum\_control](#pendulum-control)
- [pendulum\_msgs](#pendulum-msgs)
- [pluginlib](#pluginlib)
- [pybind11\_vendor](#pybind11-vendor)
- [python\_cmake\_module](#python-cmake-module)
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
- [rmw\_implementation\_cmake](#rmw-implementation-cmake)
- [robot\_state\_publisher](#robot-state-publisher)
- [ros2action](#ros2action)
- [ros2bag](#ros2bag)
- [ros2cli](#ros2cli)
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
- [rosidl\_typesupport\_introspection\_tests](#rosidl-typesupport-introspection-tests)
- [rpyutils](#rpyutils)
- [rqt\_gui](#rqt-gui)
- [rqt\_gui\_cpp](#rqt-gui-cpp)
- [rqt\_gui\_py](#rqt-gui-py)
- [rqt\_py\_common](#rqt-py-common)
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
- [sqlite3\_vendor](#sqlite3-vendor)
- [sros2](#sros2)
- [statistics\_msgs](#statistics-msgs)
- [std\_msgs](#std-msgs)
- [std\_srvs](#std-srvs)
- [stereo\_msgs](#stereo-msgs)
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
- [tracetools\_test](#tracetools-test)
- [tracetools\_trace](#tracetools-trace)
- [trajectory\_msgs](#trajectory-msgs)
- [turtlesim](#turtlesim)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [visualization\_msgs](#visualization-msgs)
- [yaml\_cpp\_vendor](#yaml-cpp-vendor)
- [zstd\_vendor](#zstd-vendor)

<a id="action-msgs"></a>

## [action\_msgs](https://github.com/ros2/rcl_interfaces/tree/humble/action_msgs/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="action-tutorials-interfaces"></a>

## [action\_tutorials\_interfaces](https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_interfaces/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="actionlib-msgs"></a>

## [actionlib\_msgs](https://github.com/ros2/common_interfaces/tree/humble/actionlib_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/humble/ament_clang_format/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/humble/ament_clang_tidy/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- remove google style from clang-tidy default settings, removing need for default config file ([#337](https://github.com/ament/ament_lint/issues/337))
- Improvements to ament\_lint\_clang\_tidy. ([#316](https://github.com/ament/ament_lint/issues/316))
- Contributors: Audrow Nash, Steven! Ragnarök, William Woodall

<a id="ament-cmake"></a>

## [ament\_cmake](https://github.com/ament/ament_cmake/tree/humble/ament_cmake/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Add ament\_cmake\_gen\_version\_h package ([#198](https://github.com/ament/ament_cmake/issues/198))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz, serge-nikulin

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_auto/CHANGELOG.rst)

- Update forthcoming version in changelog
- Fix typo in ament\_auto\_find\_test\_dependencies ([#363](https://github.com/ament/ament_cmake/issues/363))
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Add ament\_auto\_add\_gtest ([#344](https://github.com/ament/ament_cmake/issues/344))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Daisuke Nishimatsu, Joshua Whitley, Shane Loretz

<a id="ament-cmake-clang-format"></a>

## [ament\_cmake\_clang\_format](https://github.com/ament/ament_lint/tree/humble/ament_cmake_clang_format/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-cmake-clang-tidy"></a>

## [ament\_cmake\_clang\_tidy](https://github.com/ament/ament_lint/tree/humble/ament_cmake_clang_tidy/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Improvements to ament\_lint\_clang\_tidy. ([#316](https://github.com/ament/ament_lint/issues/316))
- Contributors: Audrow Nash, Steven! Ragnarök

<a id="ament-cmake-copyright"></a>

## [ament\_cmake\_copyright](https://github.com/ament/ament_lint/tree/humble/ament_cmake_copyright/CHANGELOG.rst)

- Increase the ament\_cmake\_copyright default timeout. ([#355](https://github.com/ament/ament_lint/issues/355))
- Update forthcoming version in changelogs
- [ament\_cmake\_copyright] Add file exclusion support ([#328](https://github.com/ament/ament_lint/issues/328)) \* [ament\_cmake\_copyright] Add file exclusion support In the `ament_copyright` CMake function, the optional list argument `EXCLUDE` can now be used as an exclusion specifier. \* [ament\_cmake\_copyright] Fix function header typo Remove reference to `cppcheck` in the `EXCLUDE` arg description.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_core/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Support commands with executable targets ([#352](https://github.com/ament/ament_cmake/issues/352))
- doc/resource\_index: Indent list subitems correctly ([#342](https://github.com/ament/ament_cmake/issues/342))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Michal Sojka, Scott K Logan, Shane Loretz

<a id="ament-cmake-cppcheck"></a>

## [ament\_cmake\_cppcheck](https://github.com/ament/ament_lint/tree/humble/ament_cmake_cppcheck/CHANGELOG.rst)

- Update forthcoming version in changelogs
- [ament\_cmake\_cppcheck] Fix file exclusion behavior ([#329](https://github.com/ament/ament_lint/issues/329)) The `EXCLUDE` argument of the `ament_cppcheck` CMake function is a list, i.e. a multi-value keyword. As such, it needs to be placed out of the one-value keywords from the `cmake_parse_arguments` function call.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Add cppcheck libraries option ([#323](https://github.com/ament/ament_lint/issues/323)) \* adding ament\_cppcheck libraries option \* pass libraries option via CMake Co-authored-by: William Wedler <[william.wedler@resquared.com](mailto:william.wedler%40resquared.com)>
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Will

<a id="ament-cmake-cpplint"></a>

## [ament\_cmake\_cpplint](https://github.com/ament/ament_lint/tree/humble/ament_cmake_cpplint/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-cmake-export-definitions"></a>

## [ament\_cmake\_export\_definitions](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_definitions/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-export-dependencies"></a>

## [ament\_cmake\_export\_dependencies](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_dependencies/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz

<a id="ament-cmake-export-include-directories"></a>

## [ament\_cmake\_export\_include\_directories](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_include_directories/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-export-interfaces"></a>

## [ament\_cmake\_export\_interfaces](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_interfaces/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-export-libraries"></a>

## [ament\_cmake\_export\_libraries](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_libraries/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Add note regarding interface libraries ([#339](https://github.com/ament/ament_cmake/issues/339))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Bjar Ne, Chris Lalancette, Scott K Logan, Shane Loretz

<a id="ament-cmake-export-link-flags"></a>

## [ament\_cmake\_export\_link\_flags](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_link_flags/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-export-targets"></a>

## [ament\_cmake\_export\_targets](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_targets/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-flake8"></a>

## [ament\_cmake\_flake8](https://github.com/ament/ament_lint/tree/humble/ament_cmake_flake8/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Add custom config file support for flake8 ([#331](https://github.com/ament/ament_lint/issues/331))
- Contributors: Audrow Nash, Kenji Miyake

<a id="ament-cmake-gen-version-h"></a>

## [ament\_cmake\_gen\_version\_h](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gen_version_h/CHANGELOG.rst)

- Add ament\_generate\_version\_header and deprecate ament\_cmake\_gen\_version\_h ([#377](https://github.com/ament/ament_cmake/issues/377))
- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Add ament\_cmake\_gen\_version\_h package ([#198](https://github.com/ament/ament_cmake/issues/198))
- Contributors: Audrow Nash, Shane Loretz, serge-nikulin

<a id="ament-cmake-gmock"></a>

## [ament\_cmake\_gmock](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gmock/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-google-benchmark"></a>

## [ament\_cmake\_google\_benchmark](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_google_benchmark/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gtest/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-include-directories"></a>

## [ament\_cmake\_include\_directories](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_include_directories/CHANGELOG.rst)

- Update forthcoming version in changelog
- Make ament\_include\_directories\_order a function to allow paths with backslashes on windows. ([#371](https://github.com/ament/ament_cmake/issues/371)) \* Repalce backslashes with forward slashes on Windows \* Typo \* Replace slashes in ARGN \* Don’t quote \* Check ARGN has values before trying to string(REPLACE them \* Make ament\_include\_directories\_order a function
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-libraries"></a>

## [ament\_cmake\_libraries](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_libraries/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz

<a id="ament-cmake-lint-cmake"></a>

## [ament\_cmake\_lint\_cmake](https://github.com/ament/ament_lint/tree/humble/ament_cmake_lint_cmake/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-cmake-mypy"></a>

## [ament\_cmake\_mypy](https://github.com/ament/ament_lint/tree/humble/ament_cmake_mypy/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-cmake-nose"></a>

## [ament\_cmake\_nose](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_nose/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Support commands with executable targets ([#352](https://github.com/ament/ament_cmake/issues/352))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-pclint"></a>

## [ament\_cmake\_pclint](https://github.com/ament/ament_lint/tree/humble/ament_cmake_pclint/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-cmake-pep257"></a>

## [ament\_cmake\_pep257](https://github.com/ament/ament_lint/tree/humble/ament_cmake_pep257/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-cmake-pycodestyle"></a>

## [ament\_cmake\_pycodestyle](https://github.com/ament/ament_lint/tree/humble/ament_cmake_pycodestyle/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-cmake-pyflakes"></a>

## [ament\_cmake\_pyflakes](https://github.com/ament/ament_lint/tree/humble/ament_cmake_pyflakes/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-cmake-pytest"></a>

## [ament\_cmake\_pytest](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_pytest/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Fix misleading comment ([#361](https://github.com/ament/ament_cmake/issues/361))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Support commands with executable targets ([#352](https://github.com/ament/ament_cmake/issues/352))
- Mention other platforms in ‘pytest/pytest-cov not found’ warning ([#337](https://github.com/ament/ament_cmake/issues/337))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Christophe Bedard, Shane Loretz

<a id="ament-cmake-python"></a>

## [ament\_cmake\_python](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_python/CHANGELOG.rst)

- Use sysconfig directly to determine python lib dir ([#378](https://github.com/ament/ament_cmake/issues/378))
- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Make ament\_cmake\_python symlink for symlink installs only ([#357](https://github.com/ament/ament_cmake/issues/357))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Make ament\_python\_install\_package() match setuptools’ egg names. ([#338](https://github.com/ament/ament_cmake/issues/338))
- Drop ament\_cmake\_python outdated tests. ([#340](https://github.com/ament/ament_cmake/issues/340))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Make ament\_python\_install\_package() install console\_scripts ([#328](https://github.com/ament/ament_cmake/issues/328))
- Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Scott K Logan, Shane Loretz

<a id="ament-cmake-ros"></a>

## [ament\_cmake\_ros](https://github.com/ros2/ament_cmake_ros/tree/humble/ament_cmake_ros/CHANGELOG.rst)

- Refactor domain\_coordinator API to use a context manager ([#12](https://github.com/ros2/ament_cmake_ros/issues/12))
- Contributors: Timo Röhling

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_target_dependencies/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Fix bug packages with multiple configurations ([#318](https://github.com/ament/ament_cmake/issues/318))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-test"></a>

## [ament\_cmake\_test](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_test/CHANGELOG.rst)

- Update forthcoming version in changelog
- Resolve various ament\_lint linter violations ([#360](https://github.com/ament/ament_cmake/issues/360)) We can’t add ament\_lint linters in ament\_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can’t automatically enforce linting, it’s still a good idea to try to keep conformance where possible.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz

<a id="ament-cmake-uncrustify"></a>

## [ament\_cmake\_uncrustify](https://github.com/ament/ament_lint/tree/humble/ament_cmake_uncrustify/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_cmake\_uncrustify] Add file exclude support ([#330](https://github.com/ament/ament_lint/issues/330)) In the `ament_uncrustify` CMake function, the optional list argument `EXCLUDE` can now be used as an exclusion specifier.
- Contributors: Abrar Rahman Protyasha, Audrow Nash

<a id="ament-cmake-version"></a>

## [ament\_cmake\_version](https://github.com/ament/ament_cmake/tree/humble/ament_cmake_version/CHANGELOG.rst)

- Update forthcoming version in changelog
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362](https://github.com/ament/ament_cmake/issues/362))
- Use FindPython3 instead of FindPythonInterp ([#355](https://github.com/ament/ament_cmake/issues/355))
- Update maintainers ([#336](https://github.com/ament/ament_cmake/issues/336))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="ament-cmake-xmllint"></a>

## [ament\_cmake\_xmllint](https://github.com/ament/ament_lint/tree/humble/ament_cmake_xmllint/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/humble/ament_copyright/CHANGELOG.rst)

- Fix importlib\_metadata warning on Python 3.10. ([#365](https://github.com/ament/ament_lint/issues/365))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_copyright] Fix file exclusion behavior ([#327](https://github.com/ament/ament_lint/issues/327)) \* [ament\_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in <https://github.com/ament/ament_lint/issues/326>. Specifically, the exclusion list is matched against traversed files in the `crawler` module. Changes inspired by <https://github.com/ament/ament_lint/pull/299/>. \* Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. \* Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. \* Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the `ament_copyright.crawler` module.
- Add SPDX identifiers to the licenses. ([#315](https://github.com/ament/ament_lint/issues/315))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/humble/ament_cppcheck/CHANGELOG.rst)

- Disable cppcheck 2.x. ([#345](https://github.com/ament/ament_lint/issues/345))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Add cppcheck libraries option ([#323](https://github.com/ament/ament_lint/issues/323)) \* adding ament\_cppcheck libraries option \* pass libraries option via CMake Co-authored-by: William Wedler <[william.wedler@resquared.com](mailto:william.wedler%40resquared.com)>
- Contributors: Audrow Nash, Chris Lalancette, Will

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/humble/ament_cpplint/CHANGELOG.rst)

- ignore NOLINT comments with categories that come from clang-tidy ([#339](https://github.com/ament/ament_lint/issues/339))
- Update forthcoming version in changelogs
- Reapply patches Reapply parts of 232428752251de61e84ef013bcd643e35eb9038d that are still relevant.
- Update cpplint version Point to the fork <https://github.com/cpplint/cpplint> Contains updates for modern C++ standards (e.g. C++14 and C++17).
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_copyright] Fix file exclusion behavior ([#327](https://github.com/ament/ament_lint/issues/327)) \* [ament\_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in <https://github.com/ament/ament_lint/issues/326>. Specifically, the exclusion list is matched against traversed files in the `crawler` module. Changes inspired by <https://github.com/ament/ament_lint/pull/299/>. \* Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. \* Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. \* Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the `ament_copyright.crawler` module.
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Dirk Thomas, Jacob Perron, William Woodall

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/humble/ament_flake8/CHANGELOG.rst)

- Remove use of distutils.version.LooseVersion. ([#346](https://github.com/ament/ament_lint/issues/346))
- Update forthcoming version in changelogs
- Ignore .\*/\_\* dirs in ament\_flake8 ([#335](https://github.com/ament/ament_lint/issues/335)) Other ament\_\* linters specifically ignore directories starting with a dot or underscore when crawling for files to lint. They also do so implicitly, so this change mimics that same pattern so that the behavior is consistent.
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Ignore flake8-blind-except B902 ([#292](https://github.com/ament/ament_lint/issues/292))
- Contributors: Audrow Nash, Chris Lalancette, Scott K Logan

<a id="ament-index-cpp"></a>

## [ament\_index\_cpp](https://github.com/ament/ament_index/tree/humble/ament_index_cpp/CHANGELOG.rst)

- Install includes to include/ ([#83](https://github.com/ament/ament_index/issues/83))
- Remove ament\_export\_include\_directories and ament\_export\_libraries ([#81](https://github.com/ament/ament_index/issues/81))
- Contributors: Shane Loretz

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/humble/ament_index_python/CHANGELOG.rst)

- Print warning when get\_package\_share\_directory() does not exist (Fix [#74](https://github.com/ament/ament_index/issues/74)) ([#77](https://github.com/ament/ament_index/issues/77))
- Fail lookups on invalid resource names ([#69](https://github.com/ament/ament_index/issues/69))
- Add get\_package\_share\_path method ([#73](https://github.com/ament/ament_index/issues/73))
- Contributors: David V. Lu, rob-clarke

<a id="ament-lint"></a>

## [ament\_lint](https://github.com/ament/ament_lint/tree/humble/ament_lint/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/humble/ament_lint_auto/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/humble/ament_lint_cmake/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_copyright] Fix file exclusion behavior ([#327](https://github.com/ament/ament_lint/issues/327)) \* [ament\_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in <https://github.com/ament/ament_lint/issues/326>. Specifically, the exclusion list is matched against traversed files in the `crawler` module. Changes inspired by <https://github.com/ament/ament_lint/pull/299/>. \* Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. \* Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. \* Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the `ament_copyright.crawler` module.
- Contributors: Abrar Rahman Protyasha, Audrow Nash

<a id="ament-lint-common"></a>

## [ament\_lint\_common](https://github.com/ament/ament_lint/tree/humble/ament_lint_common/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Fix typo in ament\_lint\_common/package.xml ([#336](https://github.com/ament/ament_lint/issues/336))
- Contributors: Audrow Nash, Kenji Miyake

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/humble/ament_mypy/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/humble/CHANGELOG.rst)

- Set forthcoming for previous version
- Add support for appending to environment variables ([#130](https://github.com/ament/ament_package/issues/130)) This works largely the same as ‘prepend-non-duplicate’, but instead puts the candidate value at the end of the target variable.
- Update maintainers to Audrow Nash ([#135](https://github.com/ament/ament_package/issues/135))
- Make python executable variable ament\_package specific ([#134](https://github.com/ament/ament_package/issues/134))
- Contributors: Audrow Nash, Scott K Logan, Shane Loretz

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/humble/ament_pclint/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_copyright] Fix file exclusion behavior ([#327](https://github.com/ament/ament_lint/issues/327)) \* [ament\_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in <https://github.com/ament/ament_lint/issues/326>. Specifically, the exclusion list is matched against traversed files in the `crawler` module. Changes inspired by <https://github.com/ament/ament_lint/pull/299/>. \* Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. \* Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. \* Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the `ament_copyright.crawler` module.
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Bi0T1N

<a id="ament-pep257"></a>

## [ament\_pep257](https://github.com/ament/ament_lint/tree/humble/ament_pep257/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Remove use of distutils.version.LooseVersion. ([#346](https://github.com/ament/ament_lint/issues/346))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N, Chris Lalancette

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/humble/ament_pycodestyle/CHANGELOG.rst)

- Improve documentation by clarifying the purpose of different tools ([#357](https://github.com/ament/ament_lint/issues/357))
- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash, Bi0T1N

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/humble/ament_pyflakes/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/humble/ament_uncrustify/CHANGELOG.rst)

- Update forthcoming version in changelogs
- [ament\_uncrustify] Fix file exclusion behavior ([#334](https://github.com/ament/ament_lint/issues/334)) \* [ament\_uncrustify] Fix file exclusion behavior This PR fixes the file exclusion behavior reported in [#326](https://github.com/ament/ament_lint/issues/326). Specifically, the exclusion list is matched against files/directories as the search path is traversed. Tries to maintain consistency with [#327](https://github.com/ament/ament_lint/issues/327). \* [ament\_uncrustify] Add file exclusion tests \* [ament\_uncrustify] Remove erroneous pytest marker
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- [ament\_uncrustify] Add ament\_lint tests ([#338](https://github.com/ament/ament_lint/issues/338)) \* Add `ament_lint` tests on `ament_uncrustify` \* Address linter warnings in `ament_uncrustify`
- Contributors: Abrar Rahman Protyasha, Audrow Nash

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/humble/ament_xmllint/CHANGELOG.rst)

- Update forthcoming version in changelogs
- Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340](https://github.com/ament/ament_lint/issues/340))
- Contributors: Audrow Nash

<a id="builtin-interfaces"></a>

## [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/humble/builtin_interfaces/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/humble/camera_calibration_parsers/CHANGELOG.rst)

- Tests depend on rcpputils ([#236](https://github.com/ros-perception/image_common/issues/236))
- Remove YAML\_CPP\_DLL define ([#231](https://github.com/ros-perception/image_common/issues/231))
- Export a modern CMake target instead of variables and install includes to include/${PROJECT\_NAME} ([#218](https://github.com/ros-perception/image_common/issues/218))
- Update maintainers ([#173](https://github.com/ros-perception/image_common/issues/173))
- Contributors: Akash, Alejandro Hernández Cordero, Shane Loretz

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/humble/camera_info_manager/CHANGELOG.rst)

- Export a modern CMake target instead of variables and install includes to include/${PROJECT\_NAME} ([#218](https://github.com/ros-perception/image_common/issues/218))
- Update maintainers ([#173](https://github.com/ros-perception/image_common/issues/173))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="class-loader"></a>

## [class\_loader](https://github.com/ros/class_loader/tree/humble/CHANGELOG.rst)

- Install includes to include/ ([#191](https://github.com/ros/class_loader/issues/191))
- Fix include order for cpplint ([#192](https://github.com/ros/class_loader/issues/192))
- Update maintainers to Geoffrey Biggs and Michael Carroll ([#190](https://github.com/ros/class_loader/issues/190))
- Fix spelling mistake ([#184](https://github.com/ros/class_loader/issues/184))
- Contributors: Audrow Nash, David V. Lu!!, Jacob Perron, Shane Loretz

<a id="common-interfaces"></a>

## [common\_interfaces](https://github.com/ros2/common_interfaces/tree/humble/common_interfaces/CHANGELOG.rst)

- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/humble/composition/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette

<a id="composition-interfaces"></a>

## [composition\_interfaces](https://github.com/ros2/rcl_interfaces/tree/humble/composition_interfaces/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/humble/demo_nodes_cpp/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Add how to fix the most vexing parse problem ([#541](https://github.com/ros2/demos/issues/541)) \* use uniform initialization
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Update talker\_loaned\_message.cpp ([#518](https://github.com/ros2/demos/issues/518))
- Revert “Use sizeof(char) in place for sizeof(void) ([#515](https://github.com/ros2/demos/issues/515))” ([#516](https://github.com/ros2/demos/issues/516))
- change how serialized message works with subscription ([#497](https://github.com/ros2/demos/issues/497))
- Use sizeof(char) in place for sizeof(void) ([#515](https://github.com/ros2/demos/issues/515))
- Fix small print issue in allocator tutorial. ([#509](https://github.com/ros2/demos/issues/509))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Michel Hidalgo, Tomoya Fujita, William Woodall, Zongbao Feng

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/humble/demo_nodes_cpp_native/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Fix typo in demo\_nodes\_cpp\_native package description ([#536](https://github.com/ros2/demos/issues/536))
- Contributors: Audrow Nash, Víctor Mayoral Vilches

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/humble/demo_nodes_py/CHANGELOG.rst)

- Cleanups in demo\_nodes\_py. ([#555](https://github.com/ros2/demos/issues/555))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Fixed typo executor -> executors ([#542](https://github.com/ros2/demos/issues/542))
- Update python nodes SIGINT handling ([#539](https://github.com/ros2/demos/issues/539))
- Contributors: Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, ori155

<a id="diagnostic-msgs"></a>

## [diagnostic\_msgs](https://github.com/ros2/common_interfaces/tree/humble/diagnostic_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="domain-coordinator"></a>

## [domain\_coordinator](https://github.com/ros2/ament_cmake_ros/tree/humble/domain_coordinator/CHANGELOG.rst)

- Update maintainers to Michel Hidalgo ([#13](https://github.com/ros2/ament_cmake_ros/issues/13))
- Refactor domain\_coordinator API to use a context manager ([#12](https://github.com/ros2/ament_cmake_ros/issues/12))
- Contributors: Audrow Nash, Timo Röhling

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="example-interfaces"></a>

## [example\_interfaces](https://github.com/ros2/example_interfaces/tree/humble/CHANGELOG.rst)

- Update maintainers to Mabel Zhang ([#15](https://github.com/ros2/example_interfaces/issues/15))
- Add changelog ([#14](https://github.com/ros2/example_interfaces/issues/14))
- Contributors: Audrow Nash, Ivan Santiago Paunovic

<a id="examples-rclcpp-async-client"></a>

## [examples\_rclcpp\_async\_client](https://github.com/ros2/examples/tree/humble/rclcpp/services/async_client/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Add example of how to prune old requests in client API ([#322](https://github.com/ros2/examples/issues/322))
- Contributors: Aditya Pande, Ivan Santiago Paunovic

<a id="examples-rclcpp-cbg-executor"></a>

## [examples\_rclcpp\_cbg\_executor](https://github.com/ros2/examples/tree/humble/rclcpp/executors/cbg_executor/CHANGELOG.rst)

- Improve scheduling configuration of examples\_rclcpp\_cbg\_executor package ([#331](https://github.com/ros2/examples/issues/331))
- Added jitter measurement to examples\_rclcpp\_cbg\_executor. ([#328](https://github.com/ros2/examples/issues/328))
- Fix deprecated subscriber callbacks ([#323](https://github.com/ros2/examples/issues/323))
- Remove use of get\_callback\_groups(). ([#320](https://github.com/ros2/examples/issues/320))
- Contributors: Abrar Rahman Protyasha, Chris Lalancette, Ralph Lange

<a id="examples-rclcpp-minimal-action-client"></a>

## [examples\_rclcpp\_minimal\_action\_client](https://github.com/ros2/examples/tree/humble/rclcpp/actions/minimal_action_client/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande

<a id="examples-rclcpp-minimal-action-server"></a>

## [examples\_rclcpp\_minimal\_action\_server](https://github.com/ros2/examples/tree/humble/rclcpp/actions/minimal_action_server/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande

<a id="examples-rclcpp-minimal-client"></a>

## [examples\_rclcpp\_minimal\_client](https://github.com/ros2/examples/tree/humble/rclcpp/services/minimal_client/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Add example of how to prune old requests in client API ([#322](https://github.com/ros2/examples/issues/322))
- Contributors: Aditya Pande, Ivan Santiago Paunovic

<a id="examples-rclcpp-minimal-composition"></a>

## [examples\_rclcpp\_minimal\_composition](https://github.com/ros2/examples/tree/humble/rclcpp/composition/minimal_composition/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande

<a id="examples-rclcpp-minimal-publisher"></a>

## [examples\_rclcpp\_minimal\_publisher](https://github.com/ros2/examples/tree/humble/rclcpp/topics/minimal_publisher/CHANGELOG.rst)

- Add an example about how to use wait\_for\_all\_acked ([#316](https://github.com/ros2/examples/issues/316))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Add try&catch statement to unique network flow publisher example ([#313](https://github.com/ros2/examples/issues/313))
- Add type adaption example ([#300](https://github.com/ros2/examples/issues/300))
- Contributors: Aditya Pande, Audrow Nash, Barry Xu, Tomoya Fujita

<a id="examples-rclcpp-minimal-service"></a>

## [examples\_rclcpp\_minimal\_service](https://github.com/ros2/examples/tree/humble/rclcpp/services/minimal_service/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/humble/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- Use `const&` signature for read-only sub callbacks ([#337](https://github.com/ros2/examples/issues/337))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Fix deprecated subscriber callbacks ([#323](https://github.com/ros2/examples/issues/323))
- Add wait set examples ([#315](https://github.com/ros2/examples/issues/315))
- Add type adaption example ([#300](https://github.com/ros2/examples/issues/300))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, carlossvg

<a id="examples-rclcpp-minimal-timer"></a>

## [examples\_rclcpp\_minimal\_timer](https://github.com/ros2/examples/tree/humble/rclcpp/timers/minimal_timer/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande

<a id="examples-rclcpp-multithreaded-executor"></a>

## [examples\_rclcpp\_multithreaded\_executor](https://github.com/ros2/examples/tree/humble/rclcpp/executors/multithreaded_executor/CHANGELOG.rst)

- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Fix deprecated subscriber callbacks ([#323](https://github.com/ros2/examples/issues/323))
- Contributors: Abrar Rahman Protyasha, Aditya Pande

<a id="examples-rclcpp-wait-set"></a>

## [examples\_rclcpp\_wait\_set](https://github.com/ros2/examples/tree/humble/rclcpp/wait_set/CHANGELOG.rst)

- Add wait set examples ([#315](https://github.com/ros2/examples/issues/315))
- Contributors: carlossvg

<a id="examples-rclpy-executors"></a>

## [examples\_rclpy\_executors](https://github.com/ros2/examples/tree/humble/rclpy/executors/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Update python nodes sigint/sigterm handling ([#330](https://github.com/ros2/examples/issues/330))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="examples-rclpy-guard-conditions"></a>

## [examples\_rclpy\_guard\_conditions](https://github.com/ros2/examples/tree/humble/rclpy/guard_conditions/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-action-client"></a>

## [examples\_rclpy\_minimal\_action\_client](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_client/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-action-server"></a>

## [examples\_rclpy\_minimal\_action\_server](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_server/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-client"></a>

## [examples\_rclpy\_minimal\_client](https://github.com/ros2/examples/tree/humble/rclpy/services/minimal_client/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329)) \* Updated maintainers \* Removed author
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-publisher"></a>

## [examples\_rclpy\_minimal\_publisher](https://github.com/ros2/examples/tree/humble/rclpy/topics/minimal_publisher/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-service"></a>

## [examples\_rclpy\_minimal\_service](https://github.com/ros2/examples/tree/humble/rclpy/services/minimal_service/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-minimal-subscriber"></a>

## [examples\_rclpy\_minimal\_subscriber](https://github.com/ros2/examples/tree/humble/rclpy/topics/minimal_subscriber/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Contributors: Aditya Pande, Audrow Nash

<a id="examples-rclpy-pointcloud-publisher"></a>

## [examples\_rclpy\_pointcloud\_publisher](https://github.com/ros2/examples/tree/humble/rclpy/topics/pointcloud_publisher/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Contributors: Audrow Nash

<a id="examples-tf2-py"></a>

## [examples\_tf2\_py](https://github.com/ros2/geometry2/tree/humble/examples_tf2_py/CHANGELOG.rst)

- Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481](https://github.com/ros2/geometry2/issues/481))
- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403))
- Contributors: Audrow Nash

<a id="fastrtps-cmake-module"></a>

## [fastrtps\_cmake\_module](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/fastrtps_cmake_module/CHANGELOG.rst)

- Update maintainers to Shane Loretz ([#83](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83))
- Contributors: Audrow Nash

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/humble/geometry_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="google-benchmark-vendor"></a>

## [google\_benchmark\_vendor](https://github.com/ament/google_benchmark_vendor/tree/humble/CHANGELOG.rst)

- Add git buildtool dependency.
- Use git hash for google\_benchmark\_vendor ([#20](https://github.com/ament/google_benchmark_vendor/issues/20))
- Update to google benchmark version 1.6.1 ([#19](https://github.com/ament/google_benchmark_vendor/issues/19))
- Update maintainers to Audrow Nash ([#18](https://github.com/ament/google_benchmark_vendor/issues/18))
- Update google\_benchmark to v1.5.3 ([#16](https://github.com/ament/google_benchmark_vendor/issues/16)) 1. Change google\_benchmark version from v1.5.2 to v1.5.3. Because v1.5.2 can not build with GCC 11 2. Removed shrink-tz-offset-size.patch because of this patch was merged in google-benchmark repo.
- Add changelog ([#15](https://github.com/ament/google_benchmark_vendor/issues/15))
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
- Contributors: Ahmed Sobhy, Audrow Nash, Chris Lalancette, Homalozoa X, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, Shane Loretz, Steven! Ragnarök

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/humble/image_tools/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#548](https://github.com/ros2/demos/issues/548))
- Fix include order and relative paths for cpplint ([#551](https://github.com/ros2/demos/issues/551))
- Reduce the number of OpenCV libraries image\_tools links against. ([#549](https://github.com/ros2/demos/issues/549))
- Adds copy constructor and assignment operator to ROSCvMatContainer ([#546](https://github.com/ros2/demos/issues/546))
- Fixes for uncrustify 0.72 ([#545](https://github.com/ros2/demos/issues/545))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- ambigulity: unknown type name ‘nullptr\_t’ ([#528](https://github.com/ros2/demos/issues/528))
- Add type masquerading demos ([#482](https://github.com/ros2/demos/issues/482))
- Add support for visualizing yuv422 ([#499](https://github.com/ros2/demos/issues/499))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Gonzo, Jacob Perron, Shane Loretz, William Woodall, joshua-qnx, xwnb

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/humble/image_transport/CHANGELOG.rst)

- Image transport publisher crash fixes ([#235](https://github.com/ros-perception/image_common/issues/235))
- Simple IT plugins shutdown ([#225](https://github.com/ros-perception/image_common/issues/225))
- Remove PLUGINLIB\_\_DISABLE\_BOOST\_FUNCTIONS definition. ([#226](https://github.com/ros-perception/image_common/issues/226))
- Fix include order for cpplint ([#221](https://github.com/ros-perception/image_common/issues/221)) Relates to <https://github.com/ament/ament_lint/pull/324>
- Export a modern CMake target instead of variables and install includes to include/${PROJECT\_NAME} ([#218](https://github.com/ros-perception/image_common/issues/218))
- Fix SimpleSubscriberPlugin ([#195](https://github.com/ros-perception/image_common/issues/195))
- Make sure to mark overridden methods as ‘override’. ([#192](https://github.com/ros-perception/image_common/issues/192))
- Expose subscription options ([#186](https://github.com/ros-perception/image_common/issues/186))
- fix mistyping ‘cammera\_publisher.hpp -> camera\_publisher.hpp’ ([#177](https://github.com/ros-perception/image_common/issues/177))
- Update maintainers ([#173](https://github.com/ros-perception/image_common/issues/173))
- make CameraPublisher::getNumSubscribers() work ([#163](https://github.com/ros-perception/image_common/issues/163))
- Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Hye-Jong KIM, Ivan Santiago Paunovic, Jacob Perron, Michael Ferguson, RoboTech Vision, Shane Loretz

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/humble/CHANGELOG.rst)

- Do not publish if context is invalid during shutdown ([#89](https://github.com/ros-visualization/interactive_markers/issues/89))
- Install includes to include/ and misc CMake fixes ([#85](https://github.com/ros-visualization/interactive_markers/issues/85))
- Fix deprecation warning introduced after client API update ([#83](https://github.com/ros-visualization/interactive_markers/issues/83))
- Fix deprecated sub callback warnings ([#84](https://github.com/ros-visualization/interactive_markers/issues/84))
- Include tf2\_geometry\_msgs.hpp instead of the h file. ([#82](https://github.com/ros-visualization/interactive_markers/issues/82))
- Contributors: Abrar Rahman Protyasha, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Shane Loretz

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/humble/intra_process_demo/CHANGELOG.rst)

- Add opencv\_imgproc dependency for cv::putText ([#554](https://github.com/ros2/demos/issues/554))
- Install includes to include/${PROJECT\_NAME} ([#548](https://github.com/ros2/demos/issues/548))
- Fix include order and relative paths for cpplint ([#551](https://github.com/ros2/demos/issues/551))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Revert “Add type masquerading demos ([#482](https://github.com/ros2/demos/issues/482))” ([#520](https://github.com/ros2/demos/issues/520))
- Add type masquerading demos ([#482](https://github.com/ros2/demos/issues/482))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Jacob Perron, Shane Loretz, William Woodall

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/humble/kdl_parser/CHANGELOG.rst)

- Depend on orocos-kdl vendor packages ([#58](https://github.com/ros/kdl_parser/issues/58))
- Install includes to include/ and misc CMake fixes ([#61](https://github.com/ros/kdl_parser/issues/61))
- Update to uncrustify 0.72 ([#60](https://github.com/ros/kdl_parser/issues/60))
- Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/humble/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#86](https://github.com/ros-perception/laser_geometry/issues/86))
- Explicit cast to double to prevent loss of precision
- Fix Duration casting issue leading to no undistortion
- Fix building on running on Windows Debug ([#82](https://github.com/ros-perception/laser_geometry/issues/82))
- Update python code and tests for ros2 ([#80](https://github.com/ros-perception/laser_geometry/issues/80))
- Contributors: Chris Lalancette, Jonathan Binney, Marco Lampacrescia, Shane Loretz

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/humble/launch/CHANGELOG.rst)

- Sandbox environment in tests to fix repeated job failures ([#609](https://github.com/ros2/launch/issues/609))
- Start Python faster in test\_execute\_processs\_shutdown to avoid flakey failures ([#608](https://github.com/ros2/launch/issues/608))
- Fix warnings from importlib\_metdata on Python 3.10. ([#606](https://github.com/ros2/launch/issues/606))
- Add boolean substitutions ([#598](https://github.com/ros2/launch/issues/598))
- Support scoping environment variables ([#601](https://github.com/ros2/launch/issues/601))
- Fix awaiting shutdown in launch context ([#603](https://github.com/ros2/launch/issues/603))
- Fix parse respawn var ([#569](https://github.com/ros2/launch/issues/569))
- Make the logged command pretty in ExecuteLocal ([#594](https://github.com/ros2/launch/issues/594))
- ‘output’ is expanded as a substitution in XML/YAML files ([#577](https://github.com/ros2/launch/issues/577))
- Skip warning test if warning already happend ([#585](https://github.com/ros2/launch/issues/585))
- Use asyncio.wait with timeout rather than sleep ([#576](https://github.com/ros2/launch/issues/576))
- Make test\_parser compatible with Python older than 3.8 ([#575](https://github.com/ros2/launch/issues/575))
- Propagate exceptions of completed actions to launch service main loop ([#566](https://github.com/ros2/launch/issues/566))
- Warn when loading launch extensions fails ([#572](https://github.com/ros2/launch/issues/572))
- Add in two fixes for Jammy ([#571](https://github.com/ros2/launch/issues/571))
- Evaluate math symbols and functions in python expression ([#557](https://github.com/ros2/launch/issues/557))
- Document TimerAction params ([#558](https://github.com/ros2/launch/issues/558))
- Improve launch arguments introspection ([#556](https://github.com/ros2/launch/issues/556))
- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- First prototype of native pytest plugin for launch based tests ([#528](https://github.com/ros2/launch/issues/528))
- Allow for raw path specification in IncludeLaunchDescription ([#544](https://github.com/ros2/launch/issues/544))
- Adding Executable description class ([#454](https://github.com/ros2/launch/issues/454))
- event handlers: Allow to match the target action with a callable and not only with an object instance ([#540](https://github.com/ros2/launch/issues/540))
- Add AppendEnvironmentVariable action ([#543](https://github.com/ros2/launch/issues/543))
- Document EnvironmentVariable substitution resolution context caveat ([#541](https://github.com/ros2/launch/issues/541))
- Feature clear launch configs ([#515](https://github.com/ros2/launch/issues/515))
- Add examples to ExecuteProcess docs ([#525](https://github.com/ros2/launch/issues/525))
- Fix `DeclareLaunchArgument` xml parsing and constructor ([#529](https://github.com/ros2/launch/issues/529))
- Fix pytest run on Windows ([#526](https://github.com/ros2/launch/issues/526))
- Improving docs ([#523](https://github.com/ros2/launch/issues/523))
- Add filtering mechanism for executable prefix application ([#522](https://github.com/ros2/launch/issues/522))
- Make each parser extension provide a set of file extensions ([#516](https://github.com/ros2/launch/issues/516))
- Add missing exec dependency on PyYAML ([#493](https://github.com/ros2/launch/issues/493))
- Refactor TimerAction to allow RosTimer to extend ([#512](https://github.com/ros2/launch/issues/512))
- Improve (Not)Equals condition type hinting ([#510](https://github.com/ros2/launch/issues/510))
- Contributors: Aditya Pande, Audrow Nash, Cameron Miller, Chris Lalancette, Christophe Bedard, David V. Lu!!, Derek Chopp, HMellor, Immanuel Martini, Ivan Santiago Paunovic, Jacob Perron, Kenji Miyake, Khush Jain, Kosuke Takeuchi, Rebecca Butler, Scott K Logan, Shane Loretz, roger-strain, tumtom

<a id="launch-pytest"></a>

## [launch\_pytest](https://github.com/ros2/launch/tree/humble/launch_pytest/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- [launch\_pytest] Modify how wait\_for\_output()/wait\_for\_stderr() work, add assert\_\*() alternatives ([#553](https://github.com/ros2/launch/issues/553))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- - [launch\_pytest] Fix issue when colcon –retest-until-fail flag is used ([#552](https://github.com/ros2/launch/issues/552))
- First prototype of native pytest plugin for launch based tests ([#528](https://github.com/ros2/launch/issues/528))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/humble/launch_ros/CHANGELOG.rst)

- Fix importlib\_metadata warning on Python 3.10. ([#307](https://github.com/ros2/launch_ros/issues/307))
- Use correct namespace when evaluating parameter files for composable nodes ([#303](https://github.com/ros2/launch_ros/issues/303))
- Handle empty strings when evaluating parameters ([#300](https://github.com/ros2/launch_ros/issues/300))
- Add parameter substitution ([#297](https://github.com/ros2/launch_ros/issues/297))
- fix bug in warning when an entry point fails to load ([#243](https://github.com/ros2/launch_ros/issues/243))
- More Helpful Error Messages ([#275](https://github.com/ros2/launch_ros/issues/275))
- Update maintainers in setup.py ([#287](https://github.com/ros2/launch_ros/issues/287))
- Set parameters from file for composable nodes ([#281](https://github.com/ros2/launch_ros/issues/281))
- Update package maintainers ([#284](https://github.com/ros2/launch_ros/issues/284))
- Update node name matcher ([#282](https://github.com/ros2/launch_ros/issues/282))
- Support both parameter file configurations for composable nodes ([#259](https://github.com/ros2/launch_ros/issues/259))
- Handle substitutions in RosTimer ([#264](https://github.com/ros2/launch_ros/issues/264))
- Add SetParametersFromFile action ([#260](https://github.com/ros2/launch_ros/issues/260))
- Properly support ros\_args attribute through launch frontends ([#253](https://github.com/ros2/launch_ros/issues/253))
- Add ‘push\_ros\_namespace’ alias to ‘push-ros-namespace’ ([#250](https://github.com/ros2/launch_ros/issues/250))
- Add ros\_arguments option to Node action ([#249](https://github.com/ros2/launch_ros/issues/249))
- Refactor RosTimer to extend TimerAction ([#248](https://github.com/ros2/launch_ros/issues/248))
- ROS Timer Action ([#244](https://github.com/ros2/launch_ros/issues/244))
- Support container in frontend ([#235](https://github.com/ros2/launch_ros/issues/235))
- Fix a small typo in a comment ([#237](https://github.com/ros2/launch_ros/issues/237))
- Better document parameter handling in Node ([#234](https://github.com/ros2/launch_ros/issues/234))
- Make ‘ros2 launch’ work again. ([launch #201](https://github.com/ros2/launch_ros/issues/201))
- Added LaunchLogger class ([launch #145](https://github.com/ros2/launch/issues/145))
- Changed logger.warn (deprecated) to logger.warning. ([launch #199](https://github.com/ros2/launch/issues/199))
- Added Plumb rclpy.init context to get\_default\_launch\_description. ([launch #193](https://github.com/ros2/launch/issues/193))
- Added normalize\_parameters and evaluate\_paramters. ([launch #192](https://github.com/ros2/launch/issues/192))
- Added normalize\_remap\_rule and types. ([launch #173](https://github.com/ros2/launch/issues/173))
- Renamed transitions to match changes in `lifecycle_msgs` ([launch #153](https://github.com/ros2/launch/issues/153))
- Added support for passing parameters as a dictionary to a Node ([launch #138](https://github.com/ros2/launch/issues/138))
- Made various fixes and added tests for remappings passed to Node actions ([launch #137](https://github.com/ros2/launch/issues/137))
- Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Christophe Bedard, David V. Lu!!, Felix Divo, Jacob Perron, Kenji Miyake, Michel Hidalgo, Rebecca Butler, William Woodall

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/humble/launch_testing/CHANGELOG.rst)

- Removed the deprecated `ready_fn` feature ([#589](https://github.com/ros2/launch/issues/589))
- Added case for instances of ExecuteLocal in resolveProcess function ([#587](https://github.com/ros2/launch/issues/587))
- Add compatitibility with pytest 7 ([#592](https://github.com/ros2/launch/issues/592))
- Renamed three files from example\_processes ([#573](https://github.com/ros2/launch/issues/573))
- Fix launch\_testing README.md proc keyword to process. ([#554](https://github.com/ros2/launch/issues/554)) ([#560](https://github.com/ros2/launch/issues/560))
- Declare frontend group dependency & use explicit dependencies in launch\_testing ([#520](https://github.com/ros2/launch/issues/520))
- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- First prototype of native pytest plugin for launch based tests ([#528](https://github.com/ros2/launch/issues/528))
- Adding Executable description class ([#454](https://github.com/ros2/launch/issues/454))
- Add a “hello world” style example ([#532](https://github.com/ros2/launch/issues/532))
- Contributors: Aditya Pande, Audrow Nash, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Khush Jain, Matt Lanting, Shane Loretz, William Woodall, roger-strain

<a id="launch-testing-ament-cmake"></a>

## [launch\_testing\_ament\_cmake](https://github.com/ros2/launch/tree/humble/launch_testing_ament_cmake/CHANGELOG.rst)

- [launch\_testing\_ament\_cmake] Add test label ([#584](https://github.com/ros2/launch/issues/584))
- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- Contributors: Aditya Pande, Audrow Nash, Keisuke Shima

<a id="launch-testing-examples"></a>

## [launch\_testing\_examples](https://github.com/ros2/examples/tree/humble/launch_testing/launch_testing_examples/CHANGELOG.rst)

- Readded WaitForTopics utility ([#333](https://github.com/ros2/examples/issues/333))
- Final batch of examples ([#327](https://github.com/ros2/examples/issues/327))
- Update maintainers to Aditya Pande and Shane Loretz ([#332](https://github.com/ros2/examples/issues/332))
- Updated maintainers ([#329](https://github.com/ros2/examples/issues/329))
- Reverted WaitForTopics utility usage ([#326](https://github.com/ros2/examples/issues/326))
- Moved examples ([#324](https://github.com/ros2/examples/issues/324))
- Contributors: Aditya Pande, Audrow Nash

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/humble/launch_testing_ros/CHANGELOG.rst)

- Add `hz` param to `talker.py` to fix wait\_for\_topic\_launch\_test ([#309](https://github.com/ros2/launch_ros/issues/309))
- Revert WaitForTopics ([#288](https://github.com/ros2/launch_ros/issues/288))
- Update maintainers in setup.py ([#287](https://github.com/ros2/launch_ros/issues/287))
- Move pytest entrypoints to own module ([#278](https://github.com/ros2/launch_ros/issues/278))
- Update package maintainers ([#284](https://github.com/ros2/launch_ros/issues/284))
- Check that future is done, and always call rclpy.shutdown ([#273](https://github.com/ros2/launch_ros/issues/273))
- Revert “launch testing : Wait for topics to publish ([#274](https://github.com/ros2/launch_ros/issues/274))” ([#276](https://github.com/ros2/launch_ros/issues/276))
- Add WaitForTopics utility for waiting on publishers ([#274](https://github.com/ros2/launch_ros/issues/274))
- Remove unused code, Future.result() already raises ([#270](https://github.com/ros2/launch_ros/issues/270))
- Add timeout to wait for service response in example ([#271](https://github.com/ros2/launch_ros/issues/271))
- Add examples ([#263](https://github.com/ros2/launch_ros/issues/263))
- Contributors: Aditya Pande, Audrow Nash, Jacob Perron, Jorge Perez, Michel Hidalgo, Shane Loretz

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/humble/launch_xml/CHANGELOG.rst)

- Fix sphinx directive to cross-ref Launch method ([#605](https://github.com/ros2/launch/issues/605))
- Add boolean substitutions ([#598](https://github.com/ros2/launch/issues/598))
- Support scoping environment variables ([#601](https://github.com/ros2/launch/issues/601))
- ‘output’ is expanded as a substitution in XML/YAML files ([#577](https://github.com/ros2/launch/issues/577))
- Declare frontend group dependency & use explicit dependencies in launch\_testing ([#520](https://github.com/ros2/launch/issues/520))
- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- Add AppendEnvironmentVariable action ([#543](https://github.com/ros2/launch/issues/543))
- Feature clear launch configs ([#515](https://github.com/ros2/launch/issues/515))
- Fix `DeclareLaunchArgument` xml parsing and constructor ([#529](https://github.com/ros2/launch/issues/529))
- Add ‘launch’ to sets of launch file extensions ([#518](https://github.com/ros2/launch/issues/518))
- Make each parser extension provide a set of file extensions ([#516](https://github.com/ros2/launch/issues/516))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Christophe Bedard, Derek Chopp, Ivan Santiago Paunovic, Jacob Perron, Kenji Miyake, Khush Jain

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/humble/launch_yaml/CHANGELOG.rst)

- Fix sphinx directive to cross-ref Launch method ([#605](https://github.com/ros2/launch/issues/605))
- Add boolean substitutions ([#598](https://github.com/ros2/launch/issues/598))
- Support scoping environment variables ([#601](https://github.com/ros2/launch/issues/601))
- ‘output’ is expanded as a substitution in XML/YAML files ([#577](https://github.com/ros2/launch/issues/577))
- Declare frontend group dependency & use explicit dependencies in launch\_testing ([#520](https://github.com/ros2/launch/issues/520))
- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- Add AppendEnvironmentVariable action ([#543](https://github.com/ros2/launch/issues/543))
- Feature clear launch configs ([#515](https://github.com/ros2/launch/issues/515))
- Add ‘launch’ to sets of launch file extensions ([#518](https://github.com/ros2/launch/issues/518))
- Make each parser extension provide a set of file extensions ([#516](https://github.com/ros2/launch/issues/516))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Christophe Bedard, Derek Chopp, Jacob Perron, Kenji Miyake, Khush Jain

<a id="libcurl-vendor"></a>

## [libcurl\_vendor](https://github.com/ros/resource_retriever/tree/humble/libcurl_vendor/CHANGELOG.rst)

- Update to curl 7.81. ([#74](https://github.com/ros/resource_retriever/issues/74))
- Update maintainers ([#66](https://github.com/ros/resource_retriever/issues/66))
- Contributors: Audrow Nash, Chris Lalancette

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/humble/CHANGELOG.rst)

- Bump pascalgn/automerge-action from 0.14.3 to 0.15.2
- Bump ros-tooling/setup-ros from 0.2.2 to 0.3.0
- Bump actions/upload-artifact from 2.3.1 to 3
- Bump actions/upload-artifact from 2.2.4 to 2.3.1
- Bump actions/checkout from 2 to 3
- Bump ros-tooling/setup-ros from 0.2.1 to 0.2.2 ([#123](https://github.com/ros-tooling/libstatistics_collector/issues/123))
- Install includes to include/${PROJECT\_NAME} ([#122](https://github.com/ros-tooling/libstatistics_collector/issues/122))
- Bump codecov/codecov-action from 2.0.3 to 2.1.0
- Bump pascalgn/automerge-action from 0.14.2 to 0.14.3
- Bump codecov/codecov-action from 2.0.2 to 2.0.3
- Use rosidl\_get\_typesupport\_target() ([#116](https://github.com/ros-tooling/libstatistics_collector/issues/116))
- Bump codecov/codecov-action from 2.0.1 to 2.0.2
- Bump codecov/codecov-action from 1.5.2 to 2.0.1
- Bump actions/upload-artifact from 1 to 2.2.4
- Bump codecov/codecov-action from 1.5.1 to 1.5.2
- Bump codecov/codecov-action from 1.3.1 to 1.5.1
- Bump ros-tooling/setup-ros from 0.2.0 to 0.2.1
- Bump pascalgn/automerge-action from 0.14.1 to 0.14.2
- Bump ros-tooling/setup-ros from 0.1 to 0.2.0
- Bump pascalgn/automerge-action from 0.13.1 to 0.14.1
- Fix autoapprove
- Package.json explicitly owned by emerson to minimize notifications
- Bump hmarr/auto-approve-action from v2.0.0 to v2.1.0
- Bump codecov/codecov-action from v1.2.1 to v1.3.1
- Contributors: Chris Lalancette, Emerson Knapp, Shane Loretz, dependabot[bot]

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/humble/CHANGELOG.rst)

- Add a buildtool dependency on git. ([#48](https://github.com/ros2/libyaml_vendor/issues/48))
- Install headers to include/${PROJECT\_NAME} ([#46](https://github.com/ros2/libyaml_vendor/issues/46))
- Merge pull request [#43](https://github.com/ros2/libyaml_vendor/issues/43) from ros2/update-maintainers
- Update maintainers to Audrow Nash
- Contributors: Audrow Nash, Shane Loretz, Steven! Ragnarök

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/humble/lifecycle/CHANGELOG.rst)

- Make lifecycle demo automatically exit when done ([#558](https://github.com/ros2/demos/issues/558))
- Use default on\_activate()/on\_deactivate() implemenetation of Node ([#552](https://github.com/ros2/demos/issues/552))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Fix use of future in lifecycle demo ([#534](https://github.com/ros2/demos/issues/534))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz

<a id="lifecycle-msgs"></a>

## [lifecycle\_msgs](https://github.com/ros2/rcl_interfaces/tree/humble/lifecycle_msgs/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="lifecycle-py"></a>

## [lifecycle\_py](https://github.com/ros2/demos/tree/humble/lifecycle_py/CHANGELOG.rst)

- Create changelog for lifecycle\_py
- Add rclpy lifecycle demo ([#547](https://github.com/ros2/demos/issues/547))
- Contributors: Audrow Nash, Ivan Santiago Paunovic

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/humble/logging_demo/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Use rosidl\_get\_typesupport\_target() ([#529](https://github.com/ros2/demos/issues/529))
- Contributors: Audrow Nash, Chris Lalancette, Shane Loretz

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/humble/CHANGELOG.rst)

- Use RCL\_ROS\_TIME for message\_traits::TimeStamp ([#72](https://github.com/ros2/message_filters/issues/72))
- Install includes to include/${PROJECT\_NAME} ([#71](https://github.com/ros2/message_filters/issues/71))
- Update maintainers ([#67](https://github.com/ros2/message_filters/issues/67))
- Suppress rclcpp deprecation warnings in unit tests ([#62](https://github.com/ros2/message_filters/issues/62))
- Add missing overrides to subscriber.h ([#60](https://github.com/ros2/message_filters/issues/60))
- Add lifecycle node support ([#59](https://github.com/ros2/message_filters/issues/59))
- Correct package.xml and CMakeLists.txt ([#58](https://github.com/ros2/message_filters/issues/58))
- Expose Subscription Options - V2 ([#56](https://github.com/ros2/message_filters/issues/56))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Hunter L. Allen, Kenji Brameld, Michel Hidalgo, Rebecca Butler, Shane Loretz

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/humble/CHANGELOG.rst)

- support pi zero ([#24](https://github.com/ros2/mimick_vendor/issues/24))
- Update maintainers to Geoffrey Biggs ([#23](https://github.com/ros2/mimick_vendor/issues/23))
- Update to latest commit for Apple M1 support ([#20](https://github.com/ros2/mimick_vendor/issues/20))
- Contributors: Audrow Nash, Brett Downing, Christophe Bedard

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/humble/nav_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/humble/pendulum_control/CHANGELOG.rst)

- Fix include order and relative paths for cpplint ([#551](https://github.com/ros2/demos/issues/551))
- Remove the malloc\_hook from the pendulum\_demo. ([#544](https://github.com/ros2/demos/issues/544))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fix documentation for pendulum\_control. ([#537](https://github.com/ros2/demos/issues/537))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/humble/pendulum_msgs/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Contributors: Audrow Nash

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/humble/pluginlib/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} and remove ament\_target\_dependencies calls ([#226](https://github.com/ros/pluginlib/issues/226))
- Require <memory> ([#225](https://github.com/ros/pluginlib/issues/225))
- Move LibraryLoadExceptions down a level for more accurate error messages ([#221](https://github.com/ros/pluginlib/issues/221))
- Update maintainers to Chris Lalancette ([#223](https://github.com/ros/pluginlib/issues/223))
- extend termination condition to avoid infinite loop if package.xml is not found ([#220](https://github.com/ros/pluginlib/issues/220))
- Remove deprecated headers. ([#217](https://github.com/ros/pluginlib/issues/217))
- Contributors: Alberto Soragna, Audrow Nash, Chris Lalancette, David V. Lu!!, Shane Loretz

<a id="pybind11-vendor"></a>

## [pybind11\_vendor](https://github.com/ros2/pybind11_vendor/tree/humble/CHANGELOG.rst)

- Use sha256 hash instead of tag ([#12](https://github.com/ros2/pybind11_vendor/issues/12))
- Install headers to include/${PROJECT\_NAME} ([#11](https://github.com/ros2/pybind11_vendor/issues/11))
- Update pybind11 to 2.7.1. ([#10](https://github.com/ros2/pybind11_vendor/issues/10)) This is the version that is shipped in Ubuntu 22.04.
- Contributors: Chris Lalancette, Shane Loretz

<a id="python-cmake-module"></a>

## [python\_cmake\_module](https://github.com/ros2/python_cmake_module/tree/humble/CHANGELOG.rst)

- require Python 3.6 as we use format strings in various places ([#10](https://github.com/ros2/python_cmake_module/issues/10))
- Document all variables set by this module ([#5](https://github.com/ros2/python_cmake_module/issues/5))
- Add changelog ([#4](https://github.com/ros2/python_cmake_module/issues/4))
- Contributors: Ivan Santiago Paunovic, Shane Loretz, William Woodall

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/humble-devel/qt_gui_cpp/CHANGELOG.rst)

- Install headers to include${PROJECT\_NAME} ([#259](https://github.com/ros-visualization/qt_gui_core/issues/259))
- Export targets instead of old-style CMake variables ([#257](https://github.com/ros-visualization/qt_gui_core/issues/257))
- FindPython3 explicitly instead of FindPythonInterp implicitly ([#254](https://github.com/ros-visualization/qt_gui_core/issues/254))
- Contributors: Shane Loretz

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#548](https://github.com/ros2/demos/issues/548))
- Fix include order and relative paths for cpplint ([#551](https://github.com/ros2/demos/issues/551))
- Fixes for uncrustify 0.72 ([#545](https://github.com/ros2/demos/issues/545))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Initialize message correctly ([#522](https://github.com/ros2/demos/issues/522))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Shane Loretz

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Update python nodes SIGINT handling ([#539](https://github.com/ros2/demos/issues/539))
- Contributors: Audrow Nash, Ivan Santiago Paunovic

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/humble/rcl/CHANGELOG.rst)

- add content-filtered-topic interfaces ([#894](https://github.com/ros2/rcl/issues/894))
- Add additional null check for timer argument ([#973](https://github.com/ros2/rcl/issues/973))
- Allow forward slashes within a parameter name rule in argument parsing ([#860](https://github.com/ros2/rcl/issues/860))
- Suppress false positive from clang-tidy ([#951](https://github.com/ros2/rcl/issues/951))
- Fix missing terminating 0 in rcl\_context\_impl\_t.argv ([#969](https://github.com/ros2/rcl/issues/969))
- test\_publisher\_wait\_all\_ack depends on rcpputils ([#968](https://github.com/ros2/rcl/issues/968))
- Micro-optimizations in rcl ([#965](https://github.com/ros2/rcl/issues/965))
- If timer canceled, rcl\_timer\_get\_time\_until\_next\_call returns TIMER\_CANCELED ([#963](https://github.com/ros2/rcl/issues/963))
- Add Events Executor ([#839](https://github.com/ros2/rcl/issues/839))
- Remove fastrtps customization on test\_events ([#960](https://github.com/ros2/rcl/issues/960))
- Add client/service QoS getters ([#941](https://github.com/ros2/rcl/issues/941))
- introduce ROS\_DISABLE\_LOAN\_MSG to disable can\_loan\_messages. ([#949](https://github.com/ros2/rcl/issues/949))
- Install includes it include/${PROJECT\_NAME} ([#959](https://github.com/ros2/rcl/issues/959))
- Make rcl\_difference\_times args const ([#955](https://github.com/ros2/rcl/issues/955))
- Update inject\_on\_return test skipping logic ([#953](https://github.com/ros2/rcl/issues/953))
- Fix jump callbacks being called when zero time jump thresholds used ([#948](https://github.com/ros2/rcl/issues/948))
- Only change the default logger level if default\_logger\_level is set ([#943](https://github.com/ros2/rcl/issues/943))
- Add Library for wait\_for\_entity\_helpers to deduplicate compilation ([#942](https://github.com/ros2/rcl/issues/942))
- Increase Windows timeout 15 -> 25 ms ([#940](https://github.com/ros2/rcl/issues/940))
- test should check specified number of entities. ([#935](https://github.com/ros2/rcl/issues/935))
- Fix up documentation build for rcl when using rosdoc2 ([#932](https://github.com/ros2/rcl/issues/932))
- Include rmw\_event\_t instead of forward declaring it ([#933](https://github.com/ros2/rcl/issues/933))
- Add rcl\_publisher\_wait\_for\_all\_acked support. ([#913](https://github.com/ros2/rcl/issues/913))
- Add tracing instrumentation for rcl\_take. ([#930](https://github.com/ros2/rcl/issues/930))
- Fix #include in C++ typesupport example in rcl\_subscription\_init docblock. ([#927](https://github.com/ros2/rcl/issues/927))
- Update includes after rcutils/get\_env.h deprecation. ([#917](https://github.com/ros2/rcl/issues/917))
- Use proper rcl\_logging return value type and compare to constant. ([#916](https://github.com/ros2/rcl/issues/916))
- Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Haowei Wen, Ivan Santiago Paunovic, Jafar Abdi, Michel Hidalgo, Miguel Company, NoyZuberi, Scott K Logan, Shane Loretz, Tomoya Fujita, William Woodall, iRobot ROS, mauropasse

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/humble/rcl_action/CHANGELOG.rst)

- Add Events Executor ([#839](https://github.com/ros2/rcl/issues/839))
- Install includes it include/${PROJECT\_NAME} ([#959](https://github.com/ros2/rcl/issues/959))
- Fix up documentation build for rcl\_action when using rosdoc2 ([#937](https://github.com/ros2/rcl/issues/937))
- Fix expired goals capacity of action server ([#931](https://github.com/ros2/rcl/issues/931))
- Wait for action server in rcl\_action comm tests. ([#919](https://github.com/ros2/rcl/issues/919))
- Contributors: Michel Hidalgo, Shane Loretz, iRobot ROS, spiralray

<a id="rcl-interfaces"></a>

## [rcl\_interfaces](https://github.com/ros2/rcl_interfaces/tree/humble/rcl_interfaces/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/humble/rcl_lifecycle/CHANGELOG.rst)

- Install includes it include/${PROJECT\_NAME} ([#959](https://github.com/ros2/rcl/issues/959))
- [rcl\_lifecycle] Do not share transition event message between nodes ([#956](https://github.com/ros2/rcl/issues/956))
- Update maintainers to Ivan Paunovic and William Woodall ([#952](https://github.com/ros2/rcl/issues/952))
- Fix up documentation build for rcl\_lifecycle when using rosdoc2 ([#938](https://github.com/ros2/rcl/issues/938))
- Rename variable to fix name shadowing warning ([#929](https://github.com/ros2/rcl/issues/929))
- Contributors: Alberto Soragna, Audrow Nash, Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz

<a id="rcl-logging-interface"></a>

## [rcl\_logging\_interface](https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_interface/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#85](https://github.com/ros2/rcl_logging/issues/85))
- Fix include order for cpplint ([#84](https://github.com/ros2/rcl_logging/issues/84)) Relates to <https://github.com/ament/ament_lint/pull/324>
- Update maintainers to Chris Lalancette ([#83](https://github.com/ros2/rcl_logging/issues/83))
- Fix renamed `rcpputils` header ([#81](https://github.com/ros2/rcl_logging/issues/81))
- Add Doxyfile to rcl\_logging\_interface package ([#80](https://github.com/ros2/rcl_logging/issues/80))
- Update includes after rcutils/get\_env.h deprecation ([#75](https://github.com/ros2/rcl_logging/issues/75))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Jacob Perron, Michel Hidalgo, Shane Loretz

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_noop/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#83](https://github.com/ros2/rcl_logging/issues/83))
- Contributors: Audrow Nash

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_spdlog/CHANGELOG.rst)

- Fix include order for cpplint ([#84](https://github.com/ros2/rcl_logging/issues/84)) Relates to <https://github.com/ament/ament_lint/pull/324>
- Update maintainers to Chris Lalancette ([#83](https://github.com/ros2/rcl_logging/issues/83))
- Fix renamed `rcpputils` header ([#81](https://github.com/ros2/rcl_logging/issues/81))
- Update includes after rcutils/get\_env.h deprecation ([#75](https://github.com/ros2/rcl_logging/issues/75))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Jacob Perron

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/humble/rcl_yaml_param_parser/CHANGELOG.rst)

- Install includes it include/${PROJECT\_NAME} ([#959](https://github.com/ros2/rcl/issues/959))
- Update maintainers to Ivan Paunovic and William Woodall ([#952](https://github.com/ros2/rcl/issues/952))
- Tweak rcl\_yaml\_param\_parser documentation ([#939](https://github.com/ros2/rcl/issues/939))
- Contributors: Audrow Nash, Michel Hidalgo, Shane Loretz

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/humble/rclcpp/CHANGELOG.rst)

- remove DEFINE\_CONTENT\_FILTER cmake option ([#1914](https://github.com/ros2/rclcpp/issues/1914))
- remove things that were deprecated during galactic ([#1913](https://github.com/ros2/rclcpp/issues/1913))
- add take\_data\_by\_entity\_id API to waitable ([#1892](https://github.com/ros2/rclcpp/issues/1892))
- add content-filtered-topic interfaces ([#1561](https://github.com/ros2/rclcpp/issues/1561))
- [NodeParameters] Set name in param info pre-check ([#1908](https://github.com/ros2/rclcpp/issues/1908))
- Add test-dep ament\_cmake\_google\_benchmark ([#1904](https://github.com/ros2/rclcpp/issues/1904))
- Add publish by loaned message in GenericPublisher ([#1856](https://github.com/ros2/rclcpp/issues/1856))
- Add missing ament dependency on rcl\_interfaces ([#1903](https://github.com/ros2/rclcpp/issues/1903))
- Update data callback tests to account for all published samples ([#1900](https://github.com/ros2/rclcpp/issues/1900))
- Increase timeout for acknowledgments to account for slower Connext settings ([#1901](https://github.com/ros2/rclcpp/issues/1901))
- clang-tidy: explicit constructors ([#1782](https://github.com/ros2/rclcpp/issues/1782))
- Add client/service QoS getters ([#1784](https://github.com/ros2/rclcpp/issues/1784))
- Fix a bunch more rosdoc2 issues in rclcpp. ([#1897](https://github.com/ros2/rclcpp/issues/1897))
- time\_until\_trigger returns max time if timer is cancelled ([#1893](https://github.com/ros2/rclcpp/issues/1893))
- Micro-optimizations in rclcpp ([#1896](https://github.com/ros2/rclcpp/issues/1896))
- spin\_all with a zero timeout. ([#1878](https://github.com/ros2/rclcpp/issues/1878))
- Add RMW listener APIs ([#1579](https://github.com/ros2/rclcpp/issues/1579))
- Remove fastrtps customization on tests ([#1887](https://github.com/ros2/rclcpp/issues/1887))
- Install headers to include/${PROJECT\_NAME} ([#1888](https://github.com/ros2/rclcpp/issues/1888))
- Use ament\_generate\_version\_header ([#1886](https://github.com/ros2/rclcpp/issues/1886))
- use universal reference to support rvalue. ([#1883](https://github.com/ros2/rclcpp/issues/1883))
- fix one subscription can wait\_for\_message twice ([#1870](https://github.com/ros2/rclcpp/issues/1870))
- Add return value version of get\_parameter\_or ([#1813](https://github.com/ros2/rclcpp/issues/1813))
- Cleanup time source object lifetimes ([#1867](https://github.com/ros2/rclcpp/issues/1867))
- add is\_spinning() method to executor base class
- Cleanup the TypeAdapt tests ([#1858](https://github.com/ros2/rclcpp/issues/1858))
- Cleanup includes ([#1857](https://github.com/ros2/rclcpp/issues/1857))
- Fix include order and relative paths for cpplint ([#1859](https://github.com/ros2/rclcpp/issues/1859))
- Rename stringstream in macros to a more unique name ([#1862](https://github.com/ros2/rclcpp/issues/1862))
- Add non transform capabilities for intra-process ([#1849](https://github.com/ros2/rclcpp/issues/1849))
- Fix rclcpp documentation build ([#1779](https://github.com/ros2/rclcpp/issues/1779))
- Use UninitializedStaticallyTypedParameterException ([#1689](https://github.com/ros2/rclcpp/issues/1689))
- Add wait\_for\_all\_acked support ([#1662](https://github.com/ros2/rclcpp/issues/1662))
- Add tests for function templates of declare\_parameter ([#1747](https://github.com/ros2/rclcpp/issues/1747))
- Fixes for uncrustify 0.72 ([#1844](https://github.com/ros2/rclcpp/issues/1844))
- use private member to keep the all reference underneath. ([#1845](https://github.com/ros2/rclcpp/issues/1845))
- Make node base sharable ([#1832](https://github.com/ros2/rclcpp/issues/1832))
- Add Clock::sleep\_for() ([#1828](https://github.com/ros2/rclcpp/issues/1828))
- Synchronize rcl and std::chrono steady clocks in Clock::sleep\_until ([#1830](https://github.com/ros2/rclcpp/issues/1830))
- Use rclcpp::guard\_condition ([#1612](https://github.com/ros2/rclcpp/issues/1612))
- Call CMake function to generate version header ([#1805](https://github.com/ros2/rclcpp/issues/1805))
- Use parantheses around logging macro parameter ([#1820](https://github.com/ros2/rclcpp/issues/1820))
- Remove author by request ([#1818](https://github.com/ros2/rclcpp/issues/1818))
- Update maintainers ([#1817](https://github.com/ros2/rclcpp/issues/1817))
- min\_forward & min\_backward thresholds must not be disabled ([#1815](https://github.com/ros2/rclcpp/issues/1815))
- Re-add Clock::sleep\_until ([#1814](https://github.com/ros2/rclcpp/issues/1814))
- Fix lifetime of context so it remains alive while its dependent node handles are still in use ([#1754](https://github.com/ros2/rclcpp/issues/1754))
- Add the interface for pre-shutdown callback ([#1714](https://github.com/ros2/rclcpp/issues/1714))
- Take message ownership from moved LoanedMessage ([#1808](https://github.com/ros2/rclcpp/issues/1808))
- Suppress clang dead-store warnings in the benchmarks. ([#1802](https://github.com/ros2/rclcpp/issues/1802))
- Wait for publisher and subscription to match ([#1777](https://github.com/ros2/rclcpp/issues/1777))
- Fix unused QoS profile for clock subscription and make ClockQoS the default ([#1801](https://github.com/ros2/rclcpp/issues/1801))
- Fix dangerous std::bind capture in TimeSource implementation. ([#1768](https://github.com/ros2/rclcpp/issues/1768))
- Fix dangerous std::bind capture in ParameterEventHandler implementation. ([#1770](https://github.com/ros2/rclcpp/issues/1770))
- Handle sigterm, in the same way sigint is being handled. ([#1771](https://github.com/ros2/rclcpp/issues/1771))
- rclcpp::Node copy constructor: make copy of node\_waitables\_ member. ([#1799](https://github.com/ros2/rclcpp/issues/1799))
- Extend NodeGraph to match what rcl provides. ([#1484](https://github.com/ros2/rclcpp/issues/1484))
- Context::sleep\_for(): replace recursion with do-while to avoid potential stack-overflow. ([#1765](https://github.com/ros2/rclcpp/issues/1765))
- extend\_sub\_namespace(): Verify string::empty() before calling string::front(). ([#1764](https://github.com/ros2/rclcpp/issues/1764))
- Deprecate the `void shared_ptr<MessageT>` subscription callback signatures. ([#1713](https://github.com/ros2/rclcpp/issues/1713))
- Remove can\_be\_nullptr assignment check for QNX case. ([#1752](https://github.com/ros2/rclcpp/issues/1752))
- Update client API to be able to remove pending requests. ([#1734](https://github.com/ros2/rclcpp/issues/1734))
- Fix: Allow to add a node while spinning in the StaticSingleThreadedExecutor. ([#1690](https://github.com/ros2/rclcpp/issues/1690))
- Add tracing instrumentation for executor and message taking. ([#1738](https://github.com/ros2/rclcpp/issues/1738))
- Fix: Reset timer trigger time before execute in StaticSingleThreadedExecutor. ([#1739](https://github.com/ros2/rclcpp/issues/1739))
- Use FindPython3 and make python3 dependency explicit. ([#1745](https://github.com/ros2/rclcpp/issues/1745))
- Use rosidl\_get\_typesupport\_target(). ([#1729](https://github.com/ros2/rclcpp/issues/1729))
- Fix returning invalid namespace if sub\_namespace is empty. ([#1658](https://github.com/ros2/rclcpp/issues/1658))
- Add free function to wait for a subscription message. ([#1705](https://github.com/ros2/rclcpp/issues/1705))
- Use rcpputils/scope\_exit.hpp and remove rclcpp/scope\_exit.hpp. ([#1727](https://github.com/ros2/rclcpp/issues/1727))
- Remove unsafe get\_callback\_groups API. Callers should change to using for\_each\_callback\_group(), or store the callback groups they need internally.
- Add in callback\_groups\_for\_each. The main reason to add this method in is to make accesses to the callback\_groups\_ vector thread-safe. By having a callback\_groups\_for\_each that accepts a std::function, we can just have the callers give us the callback they are interested in, and we can take care of the locking. The rest of this fairly large PR is cleaning up all of the places that use get\_callback\_groups() to instead use callback\_groups\_for\_each().
- Use a different mechanism to avoid timers being scheduled multiple times by the MultiThreadedExecutor ([#1692](https://github.com/ros2/rclcpp/issues/1692))
- Fix windows CI ([#1726](https://github.com/ros2/rclcpp/issues/1726)) Fix bug in AnyServiceCallback introduced in [#1709](https://github.com/ros2/rclcpp/issues/1709).
- Support to defer to send a response in services. ([#1709](https://github.com/ros2/rclcpp/issues/1709)) Signed-off-by: Ivan Santiago Paunovic <[ivanpauno@ekumenlabs.com](mailto:ivanpauno%40ekumenlabs.com)>
- Fix documentation bug. ([#1719](https://github.com/ros2/rclcpp/issues/1719)) Signed-off-by: William Woodall <[william@osrfoundation.org](mailto:william%40osrfoundation.org)>
- Removed left over `is_initialized()` implementation ([#1711](https://github.com/ros2/rclcpp/issues/1711)) Leftover from <https://github.com/ros2/rclcpp/pull/1622>
- Fixed declare parameter methods for int and float vectors ([#1696](https://github.com/ros2/rclcpp/issues/1696))
- Cleaned up implementation of the intra-process manager ([#1695](https://github.com/ros2/rclcpp/issues/1695))
- Added the node name to an executor `runtime_error` ([#1686](https://github.com/ros2/rclcpp/issues/1686))
- Fixed a typo “Attack” -> “Attach” ([#1687](https://github.com/ros2/rclcpp/issues/1687))
- Removed use of std::allocator<>::rebind ([#1678](https://github.com/ros2/rclcpp/issues/1678)) rebind is deprecated in c++17 and removed in c++20
- Allow declare uninitialized parameters ([#1673](https://github.com/ros2/rclcpp/issues/1673))
- Fix syntax issue with gcc ([#1674](https://github.com/ros2/rclcpp/issues/1674))
- [service] Don’t use a weak\_ptr to avoid leaking ([#1668](https://github.com/ros2/rclcpp/issues/1668))
- Fix doc typo ([#1663](https://github.com/ros2/rclcpp/issues/1663))
- [rclcpp] Type Adaptation feature ([#1557](https://github.com/ros2/rclcpp/issues/1557))
- Do not attempt to use void allocators for memory allocation. ([#1657](https://github.com/ros2/rclcpp/issues/1657))
- Keep custom allocator in publisher and subscription options alive. ([#1647](https://github.com/ros2/rclcpp/issues/1647))
- Fix get\_publishers\_subscriptions\_info\_by\_topic test in test\_node.cpp ([#1648](https://github.com/ros2/rclcpp/issues/1648))
- Use OnShutdown callback handle instead of OnShutdown callback ([#1639](https://github.com/ros2/rclcpp/issues/1639))
- use dynamic\_pointer\_cast to detect allocator mismatch in intra process manager ([#1643](https://github.com/ros2/rclcpp/issues/1643))
- Contributors: Abrar Rahman Protyasha, Ahmed Sobhy, Alberto Soragna, Andrea Sorbini, Audrow Nash, Barry Xu, Bi0T1N, Chen Lihui, Chris Lalancette, Christophe Bedard, Doug Smith, Emerson Knapp, Gaël Écorchard, Geoffrey Biggs, Gonzo, Grey, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Karsten Knese, Kenji Miyake, M. Hofstätter, M. Mostafa Farzan, Mauro Passerino, Michel Hidalgo, Miguel Company, Nikolai Morin, Petter Nilsson, Scott K Logan, Shane Loretz, Steve Macenski, Tomoya Fujita, William Woodall, Yong-Hao Zou, iRobot ROS, livanov93, mauropasse

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/humble/rclcpp_action/CHANGELOG.rst)

- remove things that were deprecated during galactic ([#1913](https://github.com/ros2/rclcpp/issues/1913))
- add take\_data\_by\_entity\_id API to waitable ([#1892](https://github.com/ros2/rclcpp/issues/1892))
- Fix rosdoc2 issues ([#1897](https://github.com/ros2/rclcpp/issues/1897))
- Add RMW listener APIs ([#1579](https://github.com/ros2/rclcpp/issues/1579))
- Install headers to include/${PROJECT\_NAME} ([#1888](https://github.com/ros2/rclcpp/issues/1888))
- Fix include order and relative paths for cpplint ([#1859](https://github.com/ros2/rclcpp/issues/1859))
- Fixes for uncrustify 0.72 ([#1844](https://github.com/ros2/rclcpp/issues/1844))
- Use rclcpp::guard\_condition ([#1612](https://github.com/ros2/rclcpp/issues/1612))
- Remove author by request ([#1818](https://github.com/ros2/rclcpp/issues/1818))
- Update maintainers ([#1817](https://github.com/ros2/rclcpp/issues/1817))
- Suppress clang dead-store warnings in the benchmarks. ([#1802](https://github.com/ros2/rclcpp/issues/1802))
- Deprecate the `void shared_ptr<MessageT>` subscription callback signatures ([#1713](https://github.com/ros2/rclcpp/issues/1713))
- Use rcpputils/scope\_exit.hpp and remove rclcpp/scope\_exit.hpp. ([#1727](https://github.com/ros2/rclcpp/issues/1727))
- Fixed occasionally missing goal result caused by race condition ([#1677](https://github.com/ros2/rclcpp/issues/1677))
- Bump the benchmark timeout for benchmark\_action\_client ([#1671](https://github.com/ros2/rclcpp/issues/1671))
- Returns CancelResponse::REJECT while goal handle failed to transit to CANCELING state ([#1641](https://github.com/ros2/rclcpp/issues/1641))
- Fix action server deadlock issue that caused by other mutexes locked in CancelCallback ([#1635](https://github.com/ros2/rclcpp/issues/1635))
- Contributors: Abrar Rahman Protyasha, Alberto Soragna, Chris Lalancette, Christophe Bedard, Jacob Perron, Kaven Yau, Shane Loretz, Tomoya Fujita, William Woodall, iRobot ROS, mauropasse

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/humble/rclcpp_components/CHANGELOG.rst)

- Select executor in node registration ([#1898](https://github.com/ros2/rclcpp/issues/1898))
- Fix rosdoc2 issues in rclcpp ([#1897](https://github.com/ros2/rclcpp/issues/1897))
- Fix bugprone-exception-escape in node\_main.cpp.in ([#1895](https://github.com/ros2/rclcpp/issues/1895))
- small improvements to node\_main.cpp.in
- Install headers to include/${PROJECT\_NAME} ([#1888](https://github.com/ros2/rclcpp/issues/1888))
- Use spin() in component\_manager\_isolated.hpp ([#1881](https://github.com/ros2/rclcpp/issues/1881))
- add use\_global\_arguments for node options of component nodes ([#1776](https://github.com/ros2/rclcpp/issues/1776))
- Add rclcpp\_components::component ([#1855](https://github.com/ros2/rclcpp/issues/1855))
- Add parameter to configure number of thread ([#1708](https://github.com/ros2/rclcpp/issues/1708))
- remove RCLCPP\_COMPONENTS\_PUBLIC in class ComponentManagerIsolated ([#1843](https://github.com/ros2/rclcpp/issues/1843))
- create component\_container\_isolated ([#1781](https://github.com/ros2/rclcpp/issues/1781))
- Remove author by request ([#1818](https://github.com/ros2/rclcpp/issues/1818))
- Update maintainers ([#1817](https://github.com/ros2/rclcpp/issues/1817))
- Suppress clang dead-store warnings in the benchmarks. ([#1802](https://github.com/ros2/rclcpp/issues/1802))
- Update client API to be able to remove pending requests. ([#1734](https://github.com/ros2/rclcpp/issues/1734))
- Deprecate method names that use CamelCase in rclcpp\_components. ([#1716](https://github.com/ros2/rclcpp/issues/1716))
- Added a hook to generate node options in ComponentManager ([#1702](https://github.com/ros2/rclcpp/issues/1702))
- Contributors: Alberto Soragna, Chris Lalancette, Daisuke Nishimatsu, Hirokazu Ishida, Ivan Santiago Paunovic, Jacob Perron, Rebecca Butler, Shane Loretz, gezp

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/humble/rclcpp_lifecycle/CHANGELOG.rst)

- remove things that were deprecated during galactic ([#1913](https://github.com/ros2/rclcpp/issues/1913))
- Fix rosdoc2 issues ([#1897](https://github.com/ros2/rclcpp/issues/1897))
- Install headers to include/${PROJECT\_NAME} ([#1888](https://github.com/ros2/rclcpp/issues/1888))
- LifecycleNode::on\_deactivate deactivate all managed entities. ([#1885](https://github.com/ros2/rclcpp/issues/1885))
- Automatically transition lifecycle entities when node transitions ([#1863](https://github.com/ros2/rclcpp/issues/1863))
- Remove author by request ([#1818](https://github.com/ros2/rclcpp/issues/1818))
- Update maintainers ([#1817](https://github.com/ros2/rclcpp/issues/1817))
- Suppress clang dead-store warnings in the benchmarks. ([#1802](https://github.com/ros2/rclcpp/issues/1802))
- Update forward declarations of `rcl_lifecycle` types ([#1788](https://github.com/ros2/rclcpp/issues/1788))
- Deprecate the `void shared_ptr<MessageT>` subscription callback signatures ([#1713](https://github.com/ros2/rclcpp/issues/1713))
- Update client API to be able to remove pending requests. ([#1734](https://github.com/ros2/rclcpp/issues/1734))
- Change log level for lifecycle\_publisher. ([#1715](https://github.com/ros2/rclcpp/issues/1715))
- Fix: RCLCPP\_PUBLIC -> RCLCPP\_LIFECYCLE\_PUBLIC ([#1732](https://github.com/ros2/rclcpp/issues/1732))
- Use rcpputils/scope\_exit.hpp and remove rclcpp/scope\_exit.hpp ([#1727](https://github.com/ros2/rclcpp/issues/1727))
- Remove unsafe get\_callback\_groups API. Callers should change to using for\_each\_callback\_group(), or store the callback groups they need internally.
- Add in callback\_groups\_for\_each. The main reason to add this method in is to make accesses to the callback\_groups\_ vector thread-safe. By having a callback\_groups\_for\_each that accepts a std::function, we can just have the callers give us the callback they are interested in, and we can take care of the locking. The rest of this fairly large PR is cleaning up all of the places that use get\_callback\_groups() to instead use callback\_groups\_for\_each().
- Fix destruction order in lifecycle benchmark ([#1675](https://github.com/ros2/rclcpp/issues/1675))
- [rclcpp] Type Adaptation feature ([#1557](https://github.com/ros2/rclcpp/issues/1557))
- Contributors: Abrar Rahman Protyasha, Alberto Soragna, Audrow Nash, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, Tomoya Fujita, William Woodall

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/humble/rclpy/CHANGELOG.rst)

- Make rclpy dependencies explicit ([#906](https://github.com/ros2/rclpy/issues/906))
- Avoid exception in Node constructor when use override for ‘use\_sim\_time’ ([#896](https://github.com/ros2/rclpy/issues/896))
- time\_until\_next\_call returns max if timer is canceled. ([#910](https://github.com/ros2/rclpy/issues/910))
- Properly implement action server/client handle cleanup. ([#905](https://github.com/ros2/rclpy/issues/905))
- Make sure to take out contexts on Action{Client,Server}. ([#904](https://github.com/ros2/rclpy/issues/904))
- Make sure to free the goal\_status\_array when done using it. ([#902](https://github.com/ros2/rclpy/issues/902))
- Bugfix to Node.destroy\_rate() result ([#901](https://github.com/ros2/rclpy/issues/901))
- Remove fastrtps customization on tests ([#895](https://github.com/ros2/rclpy/issues/895))
- fix typo ([#890](https://github.com/ros2/rclpy/issues/890))
- Document that Future.result() may return None ([#884](https://github.com/ros2/rclpy/issues/884))
- update doc release number ([#885](https://github.com/ros2/rclpy/issues/885))
- Fix multi-threaded race condition in client.call\_async ([#871](https://github.com/ros2/rclpy/issues/871))
- Fix include order for cpplint ([#877](https://github.com/ros2/rclpy/issues/877))
- Bugfix/duration to msg precision ([#876](https://github.com/ros2/rclpy/issues/876))
- Update to pybind11 2.7.1 ([#874](https://github.com/ros2/rclpy/issues/874))
- QoS history depth is only available with KEEP\_LAST ([#869](https://github.com/ros2/rclpy/issues/869))
- Implement managed nodes. ([#865](https://github.com/ros2/rclpy/issues/865))
- Make rclpy.try\_shutdown() behavior to follow rclpy.shutdown() more closely. ([#868](https://github.com/ros2/rclpy/issues/868))
- Update TopicEndpointTypeEnum.\_\_str\_\_() method to include history kind and history depth. ([#849](https://github.com/ros2/rclpy/issues/849))
- Add Clock.sleep\_for() using Clock.sleep\_until(). ([#864](https://github.com/ros2/rclpy/issues/864))
- Add Clock.sleep\_until() ([#858](https://github.com/ros2/rclpy/issues/858))
- Add \_\_enter\_\_ and \_\_exit\_\_ to JumpHandle. ([#862](https://github.com/ros2/rclpy/issues/862))
- Don’t override rclpy.\_rclpy\_pybind11 docs. ([#863](https://github.com/ros2/rclpy/issues/863))
- Improve JumpThreshold documentation and forbid zero durations. ([#861](https://github.com/ros2/rclpy/issues/861))
- Fix time.py and clock.py circular import. ([#860](https://github.com/ros2/rclpy/issues/860))
- Make context.on\_shutdown() allow free functions. ([#859](https://github.com/ros2/rclpy/issues/859))
- Fix automatically declared parameters descriptor type. ([#853](https://github.com/ros2/rclpy/issues/853))
- Shutdown asynchronously when sigint is received. ([#844](https://github.com/ros2/rclpy/issues/844))
- Update maintainers. ([#845](https://github.com/ros2/rclpy/issues/845))
- Add entities to callback group before making them available to the executor to avoid a race condition. ([#839](https://github.com/ros2/rclpy/issues/839))
- Avoid race condition in client.call(). ([#838](https://github.com/ros2/rclpy/issues/838))
- Handle sigterm. ([#830](https://github.com/ros2/rclpy/issues/830))
- Use pybind11 for signal handling, and delete now unused rclpy\_common, pycapsule, and handle code. ([#814](https://github.com/ros2/rclpy/issues/814))
- Fix memory leak in Service::take\_request() and Client::take\_response(). ([#828](https://github.com/ros2/rclpy/issues/828))
- Add Publisher.wait\_for\_all\_acked(). ([#793](https://github.com/ros2/rclpy/issues/793))
- Only add one done callback to a future in Executor. ([#816](https://github.com/ros2/rclpy/issues/816))
- Add convert function from ParameterValue to Python builtin. ([#819](https://github.com/ros2/rclpy/issues/819))
- Call Context.\_logging\_fini() in Context.try\_shutdown(). ([#800](https://github.com/ros2/rclpy/issues/800))
- Lift LoggingSeverity enum as common dependency to logging and rcutils\_logger modules ([#785](https://github.com/ros2/rclpy/issues/785))
- Set Context.\_\_context to None in \_\_init\_\_(). ([#812](https://github.com/ros2/rclpy/issues/812))
- Remove unused function make\_mock\_subscription. ([#809](https://github.com/ros2/rclpy/issues/809))
- Removed common.c/h ([#789](https://github.com/ros2/rclpy/issues/789))
- Allow declaring uninitialized parameters ([#798](https://github.com/ros2/rclpy/issues/798))
- Reject cancel request if failed to transit to CANCEL\_GOAL state ([#791](https://github.com/ros2/rclpy/issues/791))
- Deleted handle as it should no longer be used ([#786](https://github.com/ros2/rclpy/issues/786))
- Removed some functions in common.c and replaced them in utils.cpp ([#787](https://github.com/ros2/rclpy/issues/787))
- Moved exception.cpp/hpp to the \_rclpy\_pybind11 module ([#788](https://github.com/ros2/rclpy/issues/788))
- Print ‘Infinite’ for infinite durations in topic endpoint info ([#722](https://github.com/ros2/rclpy/issues/722))
- Break log function execution ASAP if configured severity is too high ([#776](https://github.com/ros2/rclpy/issues/776))
- Convert Node and Context to use C++ Classes ([#771](https://github.com/ros2/rclpy/issues/771))
- Misc action server improvements ([#774](https://github.com/ros2/rclpy/issues/774))
- Misc action goal handle improvements ([#767](https://github.com/ros2/rclpy/issues/767))
- Convert Guardcondition to use C++ classes ([#772](https://github.com/ros2/rclpy/issues/772))
- Removed unused structs `rclpy_client_t` and `rclpy_service_t` ([#770](https://github.com/ros2/rclpy/issues/770))
- Convert WaitSet to use C++ Classes ([#769](https://github.com/ros2/rclpy/issues/769))
- Convert ActionServer to use C++ Classes ([#766](https://github.com/ros2/rclpy/issues/766))
- Convert ActionClient to use C++ classes ([#759](https://github.com/ros2/rclpy/issues/759))
- Use py::class\_ for rcl\_action\_goal\_handle\_t ([#751](https://github.com/ros2/rclpy/issues/751))
- Convert Publisher and Subscription to use C++ Classes ([#756](https://github.com/ros2/rclpy/issues/756))
- Rename QoS\*Policy enum’s to \*Policy ([#379](https://github.com/ros2/rclpy/issues/379))
- Use params from node ‘/\*\*’ from parameter YAML file ([#370](https://github.com/ros2/rclpy/issues/370))
- Updated to use params from node ‘/\*\*’ from parameter YAML file. ([#399](https://github.com/ros2/rclpy/issues/399))
- Contributors: Alejandro Hernández Cordero, Anthony, Artem Shumov, Auguste Lalande, Barry Xu, Chris Lalancette, Emerson Knapp, Erki Suurjaak, Greg Balke, Ivan Santiago Paunovic, Jacob Perron, Lei Liu, Louise Poubel, Miguel Company, Shane Loretz, Tomoya Fujita, ksuszka

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/humble/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#160](https://github.com/ros2/rcpputils/issues/160))
- Fix include order for cpplint ([#158](https://github.com/ros2/rcpputils/issues/158))
- [path] Declare the default assignment operator ([#156](https://github.com/ros2/rcpputils/issues/156))
- Fixes for uncrustify 0.72 ([#154](https://github.com/ros2/rcpputils/issues/154))
- Fix the BSD license headers to use the standard one. ([#153](https://github.com/ros2/rcpputils/issues/153))
- Update maintainers to Chris Lalancette ([#152](https://github.com/ros2/rcpputils/issues/152))
- Add checked convert\_to\_nanoseconds() function ([#145](https://github.com/ros2/rcpputils/issues/145))
- Add missing sections in docs/FEATURES.md TOC ([#151](https://github.com/ros2/rcpputils/issues/151))
- [env] Add `set_env_var` function ([#150](https://github.com/ros2/rcpputils/issues/150))
- Add missing cstddef include ([#147](https://github.com/ros2/rcpputils/issues/147))
- Add accumulator test to CMakeLists.txt ([#144](https://github.com/ros2/rcpputils/issues/144))
- `rcpputils::fs`: Fix doxygen parameter identifier ([#142](https://github.com/ros2/rcpputils/issues/142))
- Make thread safety macro C++ standards compliant ([#141](https://github.com/ros2/rcpputils/issues/141))
- Fix API documentation for clean `rosdoc2` build ([#139](https://github.com/ros2/rcpputils/issues/139))
- Improve `rcppmath` Doxygen documentation ([#138](https://github.com/ros2/rcpputils/issues/138))
- Improve documentation of utilities in docs/FEATURES.md ([#137](https://github.com/ros2/rcpputils/issues/137))
- Include `rcppmath` utilities in docs/FEATURES.md ([#136](https://github.com/ros2/rcpputils/issues/136))
- Fix `IllegalStateException` reference in FEATURES ([#135](https://github.com/ros2/rcpputils/issues/135))
- migrate rolling mean from ros2\_controllers to rcppmath ([#133](https://github.com/ros2/rcpputils/issues/133))
- Update includes after rcutils/get\_env.h deprecation ([#132](https://github.com/ros2/rcpputils/issues/132))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chris Lalancette, Christophe Bedard, Jacob Perron, Karsten Knese, Octogonapus, Shane Loretz

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/humble/CHANGELOG.rst)

- Update launch test for change related to enviroment variables in launch ([#354](https://github.com/ros2/rcutils/issues/354))
- Remove dst\_size from strlen usage ([#353](https://github.com/ros2/rcutils/issues/353))
- Install headers to include${PROJECT\_NAME} ([#351](https://github.com/ros2/rcutils/issues/351))
- Use static\_cast instead of C-style cast ([#349](https://github.com/ros2/rcutils/issues/349))
- Fixing up documentation build when using rosdoc2 ([#344](https://github.com/ros2/rcutils/issues/344))
- Stop double-defining structs. ([#333](https://github.com/ros2/rcutils/issues/333))
- Use FindPython3 explicitly instead of FindPythonInterp implicitly ([#345](https://github.com/ros2/rcutils/issues/345))
- Fix build on Android ([#342](https://github.com/ros2/rcutils/issues/342))
- Deprecate get\_env.h and move content to env.{h,c} ([#340](https://github.com/ros2/rcutils/issues/340))
- Contributors: Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Shane Loretz, William Woodall

<a id="resource-retriever"></a>

## [resource\_retriever](https://github.com/ros/resource_retriever/tree/humble/resource_retriever/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#72](https://github.com/ros/resource_retriever/issues/72))
- Fix include order for cpplint ([#69](https://github.com/ros/resource_retriever/issues/69))
- Update maintainers ([#66](https://github.com/ros/resource_retriever/issues/66))
- Remove the deprecated retriever.h header ([#63](https://github.com/ros/resource_retriever/issues/63))
- Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/humble/rmw/CHANGELOG.rst)

- Add content filtered topics support. ([#302](https://github.com/ros2/rmw/issues/302))
- Add sequence numbers to rmw\_message\_info\_t. ([#318](https://github.com/ros2/rmw/issues/318))
- Add rmw\_feature\_supported(). ([#318](https://github.com/ros2/rmw/issues/318))
- Add EventsExecutor ([#286](https://github.com/ros2/rmw/issues/286))
- Document that rmw\_wait() SHOULD use a monotonic clock ([#316](https://github.com/ros2/rmw/issues/316))
- Install headers to include/${PROJECT\_NAME} ([#317](https://github.com/ros2/rmw/issues/317))
- Update rmw\_server\_is\_available() API documentation. ([#277](https://github.com/ros2/rmw/issues/277))
- Add client/service QoS getters. ([#314](https://github.com/ros2/rmw/issues/314))
- Fix up documentation build for rmw when using rosdoc2 ([#313](https://github.com/ros2/rmw/issues/313))
- Fix up errors in doxygen documentation ([#311](https://github.com/ros2/rmw/issues/311))
- Fix copy-paste error in API doc for rmw\_get\_gid\_for\_publisher ([#310](https://github.com/ros2/rmw/issues/310))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#296](https://github.com/ros2/rmw/issues/296))
- Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz, iRobot ROS, mauropasse

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds/CHANGELOG.rst)

- Exclude missing sample info fields when building rmw\_connextddsmicro ([#79](https://github.com/ros2/rmw_connextdds/issues/79))
- Update launch\_testing\_ros output filter prefixes for Connext6 ([#80](https://github.com/ros2/rmw_connextdds/issues/80))
- Add support for user-specified content filters ([#68](https://github.com/ros2/rmw_connextdds/issues/68))
- add stub for content filtered topic ([#77](https://github.com/ros2/rmw_connextdds/issues/77))
- Add rmw listener apis ([#44](https://github.com/rticommunity/rmw_connextdds/issues/44))
- Add client/service QoS getters. ([#67](https://github.com/rticommunity/rmw_connextdds/issues/67))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#20](https://github.com/rticommunity/rmw_connextdds/issues/20))
- Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago Paunovic, iRobot ROS, mauropasse

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds_common/CHANGELOG.rst)

- Exclude missing sample info fields when building rmw\_connextddsmicro ([#79](https://github.com/ros2/rmw_connextdds/issues/79))
- Properly initialize CDR stream before using it for filtering ([#81](https://github.com/ros2/rmw_connextdds/issues/81))
- Add support for user-specified content filters ([#68](https://github.com/ros2/rmw_connextdds/issues/68))
- add stub for content filtered topic ([#77](https://github.com/ros2/rmw_connextdds/issues/77))
- Add sequence numbers to message info structure ([#74](https://github.com/ros2/rmw_connextdds/issues/74))
- Add rmw listener apis ([#44](https://github.com/rticommunity/rmw_connextdds/issues/44))
- Fix cpplint errors ([#69](https://github.com/ros2/rmw_connextdds/issues/69))
- Add client/service QoS getters. ([#67](https://github.com/rticommunity/rmw_connextdds/issues/67))
- Update rmw\_context\_impl\_t definition ([#65](https://github.com/ros2/rmw_connextdds/issues/65))
- Use the new rmw\_dds\_common::get\_security\_files API ([#61](https://github.com/ros2/rmw_connextdds/issues/61))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#20](https://github.com/rticommunity/rmw_connextdds/issues/20))
- Support extended signature for `message_type_support_callbacks_t::max_serialized_size()` from `rosidl_typesupport_fastrtps_cpp`. ([#14](https://github.com/rticommunity/rmw_connextdds/issues/14))
- Update includes after rcutils/get\_env.h deprecation. ([#55](https://github.com/rticommunity/rmw_connextdds/issues/55))
- Always modify UserObjectQosPolicy regardless of override policy. ([#53](https://github.com/rticommunity/rmw_connextdds/issues/53))
- Improved conversion of time values between ROS and DDS formats. ([#43](https://github.com/rticommunity/rmw_connextdds/issues/43))
- Allow sharing DomainParticipant with C++ applications. ([#25](https://github.com/rticommunity/rmw_connextdds/issues/25))
- Add environment variable to control override of DomainParticipantQos. ([#41](https://github.com/rticommunity/rmw_connextdds/issues/41))
- Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Miguel Company, iRobot ROS, mauropasse

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextddsmicro/CHANGELOG.rst)

- Exclude missing sample info fields when building rmw\_connextddsmicro ([#79](https://github.com/ros2/rmw_connextdds/issues/79))
- Add support for user-specified content filters ([#68](https://github.com/ros2/rmw_connextdds/issues/68))
- add stub for content filtered topic ([#77](https://github.com/ros2/rmw_connextdds/issues/77))
- Add sequence numbers to message info structure ([#74](https://github.com/ros2/rmw_connextdds/issues/74))
- Add rmw listener apis ([#44](https://github.com/rticommunity/rmw_connextdds/issues/44))
- Add client/service QoS getters. ([#67](https://github.com/rticommunity/rmw_connextdds/issues/67))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#20](https://github.com/rticommunity/rmw_connextdds/issues/20))
- Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago Paunovic, iRobot ROS, mauropasse

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/humble/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Fix get\_topic\_name and handling long service names
- Add serialization for SDK\_DATA
- Additional checks for loan API
- Depend on just rmw\_dds\_common::rmw\_dds\_common\_library ([#385](https://github.com/ros2/rmw_cyclonedds/issues/385))
- Fix error message in rmw\_init\_options\_copy(). ([#380](https://github.com/ros2/rmw_cyclonedds/issues/380))
- Add content filter topic feature empty stub. ([#289](https://github.com/ros2/rmw_cyclonedds/issues/289))
- Update to work with Cyclone 0.9.0 and Iceoryx 2.0 ([#379](https://github.com/ros2/rmw_cyclonedds/issues/379))
- Fill message info sequence numbers as unsupported, add rmw\_feature\_supported() implementation. ([#381](https://github.com/ros2/rmw_cyclonedds/issues/381))
- Fix a warning by making a pointer nullptr. ([#375](https://github.com/ros2/rmw_cyclonedds/issues/375))
- Bump QDs to QL2 ([#371](https://github.com/ros2/rmw_cyclonedds/issues/371))
- Add EventsExecutor ([#256](https://github.com/ros2/rmw_cyclonedds/issues/256))
- Call dissociate\_reader in rmw\_destroy\_subscription
- Wrap creation of new serdata\_rmw within a try-catch block
- Fix memory leak in error scenario on the publish side with SHM
- Fix memory leaks on the take side with SHM
- rename \_cyclonedds\_has\_shm to follow the convention
- Add iceoryx\_binding\_c as dependency to rmw\_cyclonedds\_cpp
- Release iox\_chunk to iceoryx in serdata\_free if the iox\_chunk is still available
- Update iceoryx\_subscriber also when constructing the serdata from the iox chunk
- Fix cpplint errors ([#363](https://github.com/ros2/rmw_cyclonedds/issues/363))
- Updates for uncrustify 0.72 ([#358](https://github.com/ros2/rmw_cyclonedds/issues/358))
- Export only rmw::rmw to downstream targets ([#360](https://github.com/ros2/rmw_cyclonedds/issues/360))
- Export modern CMake targets ([#357](https://github.com/ros2/rmw_cyclonedds/issues/357))
- Free with the same allocator in rmw\_destroy\_node ([#355](https://github.com/ros2/rmw_cyclonedds/issues/355))
- Add client/service QoS getters. ([#343](https://github.com/ros2/rmw_cyclonedds/issues/343))
- Updated version number and quality level. ([#349](https://github.com/ros2/rmw_cyclonedds/issues/349))
- Update package maintainers. ([#351](https://github.com/ros2/rmw_cyclonedds/issues/351))
- Fix undesired memory initialization in zero-copy data path. ([#348](https://github.com/ros2/rmw_cyclonedds/issues/348))
- Fix QoS depth settings for clients/service being ignored. ([#340](https://github.com/ros2/rmw_cyclonedds/issues/340))
- Link to Cyclone DDS in Quality Declaration. ([#342](https://github.com/ros2/rmw_cyclonedds/issues/342))
- Update rmw\_context\_impl\_t definition ([#337](https://github.com/ros2/rmw_cyclonedds/issues/337))
- Add quality declaration for rmw\_cyclonedds\_cpp ([#335](https://github.com/ros2/rmw_cyclonedds/issues/335))
- Fix use of deprecated is\_loan\_available ([#336](https://github.com/ros2/rmw_cyclonedds/issues/336))
- Add -latomic for RISC-V ([#332](https://github.com/ros2/rmw_cyclonedds/issues/332))
- Add pub/sub init, publish and take instrumentation using tracetools ([#329](https://github.com/ros2/rmw_cyclonedds/issues/329))
- Pass the CRL down to CycloneDDS if it exists ([#325](https://github.com/ros2/rmw_cyclonedds/issues/325))
- Use the new rmw\_dds\_common::get\_security\_files API ([#323](https://github.com/ros2/rmw_cyclonedds/issues/323))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#294](https://github.com/ros2/rmw_cyclonedds/issues/294))
- Fix zero copy issues. ([#309](https://github.com/ros2/rmw_cyclonedds/issues/309))
- Handle allocation errors during message deserialization. ([#313](https://github.com/ros2/rmw_cyclonedds/issues/313))
- Update includes after rcutils/get\_env.h deprecation. ([#312](https://github.com/ros2/rmw_cyclonedds/issues/312))
- Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Dietrich Krönke, Erik Boasson, Haowei Wen, Ivan Santiago Paunovic, Jacob Perron, Joe Speed, Michel Hidalgo, Shane Loretz, Sumanth Nirmal, eboasson, guillaume-pais-siemens, iRobot ROS, mauropasse

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/humble/rmw_dds_common/CHANGELOG.rst)

- Depend on target generated by rosidl\_typesupport\_cpp ([#58](https://github.com/ros2/rmw_dds_common/issues/58))
- Use rosidl\_get\_typesupport\_target() and target\_link\_libraries(). ([#57](https://github.com/ros2/rmw_dds_common/issues/57))
- Install headers to include/${PROJECT\_NAME} ([#56](https://github.com/ros2/rmw_dds_common/issues/56))
- Fix include order for cpplint ([#55](https://github.com/ros2/rmw_dds_common/issues/55))
- Fix up rmw\_dds\_common documentation when using rosdoc2 ([#54](https://github.com/ros2/rmw_dds_common/issues/54))
- Add support for Certificate Revocation List files ([#52](https://github.com/ros2/rmw_dds_common/issues/52))
- Silence clang warning (`range-loop-construct`) ([#53](https://github.com/ros2/rmw_dds_common/issues/53))
- Add a common function for security files. ([#51](https://github.com/ros2/rmw_dds_common/issues/51))
- Normalize rmw\_time\_t according to DDS spec ([#48](https://github.com/ros2/rmw_dds_common/issues/48))
- Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron, Karsten Knese, Michel Hidalgo, Shane Loretz

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_cpp/CHANGELOG.rst)

- Add pub/sub init, publish and take instrumentation using tracetools ([#591](https://github.com/ros2/rmw_fastrtps/issues/591))
- Add content filter topic feature ([#513](https://github.com/ros2/rmw_fastrtps/issues/513))
- Add sequence numbers to message info structure ([#587](https://github.com/ros2/rmw_fastrtps/issues/587))
- Removed some heap interactions in rmw\_serialize.cpp ([#590](https://github.com/ros2/rmw_fastrtps/issues/590))
- Add EventsExecutor ([#468](https://github.com/ros2/rmw_fastrtps/issues/468))
- Install headers to include/${PROJECT\_NAME} ([#578](https://github.com/ros2/rmw_fastrtps/issues/578))
- Add client/service QoS getters. ([#560](https://github.com/ros2/rmw_fastrtps/issues/560))
- Correctly recalculate serialized size on bounded sequences. ([#540](https://github.com/ros2/rmw_fastrtps/issues/540))
- Fix type size alignment. ([#550](https://github.com/ros2/rmw_fastrtps/issues/550))
- Change links from index.ros.org -> docs.ros.org ([#539](https://github.com/ros2/rmw_fastrtps/issues/539))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#519](https://github.com/ros2/rmw_fastrtps/issues/519))
- Loan messages implementation ([#523](https://github.com/ros2/rmw_fastrtps/issues/523)) \* Added is\_plain\_ attribute to base TypeSupport. \* Added new methods to base TypeSupport. \* Implementation of rmw\_borrow\_loaned\_message. \* Implementation of rmw\_return\_loaned\_message\_from\_publisher. \* Enable loan messages on publishers of plain types. \* Implementation for taking loaned messages. \* Enable loan messages on subscriptions of plain types.
- Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Miguel Company, Shane Loretz, WideAwakeTN, iRobot ROS, mauropasse

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Add content filter topic feature ([#513](https://github.com/ros2/rmw_fastrtps/issues/513))
- Add sequence numbers to message info structure ([#587](https://github.com/ros2/rmw_fastrtps/issues/587))
- Add EventsExecutor ([#468](https://github.com/ros2/rmw_fastrtps/issues/468))
- Install headers to include/${PROJECT\_NAME} ([#578](https://github.com/ros2/rmw_fastrtps/issues/578))
- Add client/service QoS getters. ([#560](https://github.com/ros2/rmw_fastrtps/issues/560))
- Correctly recalculate serialized size on bounded sequences. ([#540](https://github.com/ros2/rmw_fastrtps/issues/540))
- Fix type size alignment. ([#550](https://github.com/ros2/rmw_fastrtps/issues/550))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#519](https://github.com/ros2/rmw_fastrtps/issues/519))
- Loan messages implementation ([#523](https://github.com/ros2/rmw_fastrtps/issues/523)) \* Added is\_plain\_ attribute to base TypeSupport. \* Added new methods to base TypeSupport. \* Implementation of rmw\_borrow\_loaned\_message. \* Implementation of rmw\_return\_loaned\_message\_from\_publisher. \* Enable loan messages on publishers of plain types. \* Implementation for taking loaned messages. \* Enable loan messages on subscriptions of plain types.
- Contributors: Barry Xu, Chen Lihui, Ivan Santiago Paunovic, Miguel Company, Shane Loretz, iRobot ROS, mauropasse

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Address linter waning for windows. ([#592](https://github.com/ros2/rmw_fastrtps/issues/592))
- Add pub/sub init, publish and take instrumentation using tracetools ([#591](https://github.com/ros2/rmw_fastrtps/issues/591))
- Add content filter topic feature ([#513](https://github.com/ros2/rmw_fastrtps/issues/513))
- Add sequence numbers to message info structure ([#587](https://github.com/ros2/rmw_fastrtps/issues/587))
- Add EventsExecutor ([#468](https://github.com/ros2/rmw_fastrtps/issues/468))
- Complete events support ([#583](https://github.com/ros2/rmw_fastrtps/issues/583))
- Install headers to include/${PROJECT\_NAME} ([#578](https://github.com/ros2/rmw_fastrtps/issues/578))
- Change default to synchronous ([#571](https://github.com/ros2/rmw_fastrtps/issues/571))
- Fix cpplint error ([#574](https://github.com/ros2/rmw_fastrtps/issues/574))
- Fixes for uncrustify 0.72 ([#572](https://github.com/ros2/rmw_fastrtps/issues/572))
- Add client/service QoS getters. ([#560](https://github.com/ros2/rmw_fastrtps/issues/560))
- Fix QoS depth settings for clients/service being ignored. ([#564](https://github.com/ros2/rmw_fastrtps/issues/564))
- Update rmw\_context\_impl\_t definition. ([#558](https://github.com/ros2/rmw_fastrtps/issues/558))
- Update the LoanManager to do internal locking. ([#552](https://github.com/ros2/rmw_fastrtps/issues/552))
- Pass the CRL down to Fast-DDS if available. ([#546](https://github.com/ros2/rmw_fastrtps/issues/546))
- Use the new rmw\_dds\_common::get\_security\_files ([#544](https://github.com/ros2/rmw_fastrtps/issues/544))
- Support for SubscriptionOptions::ignore\_local\_publications ([#536](https://github.com/ros2/rmw_fastrtps/issues/536))
- Change links from index.ros.org -> docs.ros.org ([#539](https://github.com/ros2/rmw_fastrtps/issues/539))
- Add rmw\_publisher\_wait\_for\_all\_acked support. ([#519](https://github.com/ros2/rmw_fastrtps/issues/519))
- Loan messages implementation ([#523](https://github.com/ros2/rmw_fastrtps/issues/523)) \* Added is\_plain\_ attribute to base TypeSupport. \* Added new methods to base TypeSupport. \* Implementation of rmw\_borrow\_loaned\_message. \* Implementation of rmw\_return\_loaned\_message\_from\_publisher. \* Enable loan messages on publishers of plain types. \* Implementation for taking loaned messages. \* Enable loan messages on subscriptions of plain types.
- Export rmw\_dds\_common as an rmw\_fastrtps\_shared\_cpp dependency ([#530](https://github.com/ros2/rmw_fastrtps/issues/530))
- Update includes after rcutils/get\_env.h deprecation ([#529](https://github.com/ros2/rmw_fastrtps/issues/529))
- Contributors: Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Jose Antonio Moral, Michel Hidalgo, Miguel Company, Shane Loretz, Tomoya Fujita, iRobot ROS, mauropasse

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/humble/rmw_implementation/CHANGELOG.rst)

- add content-filtered-topic interfaces ([#181](https://github.com/ros2/rmw_implementation/issues/181))
- Add rmw\_feature\_supported() ([#204](https://github.com/ros2/rmw_implementation/issues/204))
- Add EventsExecutor ([#161](https://github.com/ros2/rmw_implementation/issues/161))
- Fix relative path include syntax for cpplint ([#203](https://github.com/ros2/rmw_implementation/issues/203))
- Support and prefer exported targets from rmw implementations ([#201](https://github.com/ros2/rmw_implementation/issues/201))
- Add client/service QoS getters. ([#196](https://github.com/ros2/rmw_implementation/issues/196))
- Update maintainers to Audrow Nash and Michael Carroll. ([#199](https://github.com/ros2/rmw_implementation/issues/199))
- Fix renamed `rcpputils` header ([#198](https://github.com/ros2/rmw_implementation/issues/198))
- Fix rmw\_implementation generated documentation ([#197](https://github.com/ros2/rmw_implementation/issues/197))
- Add rmw\_publisher\_wait\_for\_all\_acked. ([#188](https://github.com/ros2/rmw_implementation/issues/188))
- Attempt to load any available RMW implementation. ([#189](https://github.com/ros2/rmw_implementation/issues/189))
- Update includes after rcutils/get\_env.h deprecation ([#190](https://github.com/ros2/rmw_implementation/issues/190))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, iRobot ROS, mauropasse

<a id="rmw-implementation-cmake"></a>

## [rmw\_implementation\_cmake](https://github.com/ros2/rmw/tree/humble/rmw_implementation_cmake/CHANGELOG.rst)

- Use FastDDS as default DDS ([#315](https://github.com/ros2/rmw/issues/315))
- Contributors: Audrow Nash

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/humble/CHANGELOG.rst)

- Depend on orocos\_kdl\_vendor ([#191](https://github.com/ros/robot_state_publisher/issues/191))
- export dependencies, to use robot\_state\_publisher as a component ([#193](https://github.com/ros/robot_state_publisher/issues/193))
- Fix include order for cpplint ([#186](https://github.com/ros/robot_state_publisher/issues/186))
- Change how parameter updates are handled ([#180](https://github.com/ros/robot_state_publisher/issues/180))
- Install includes to instal/${PROJECT\_NAME} ([#184](https://github.com/ros/robot_state_publisher/issues/184))
- Make the change\_fixed\_joint test more robust ([#183](https://github.com/ros/robot_state_publisher/issues/183))
- Add in a test to make sure fixed transforms change on update
- Small C++ nice-isms in the tests
- Switch to using target\_include\_directories for tests
- Publish new fixed transforms when URDF is updated
- Make joint\_states subscription QoS configurable; default to SensorDataQoS ([#179](https://github.com/ros/robot_state_publisher/issues/179))
- Remove dependency on urdfdom\_headers ([#168](https://github.com/ros/robot_state_publisher/issues/168))
- Fix deprecated subscriber callbacks ([#173](https://github.com/ros/robot_state_publisher/issues/173))
- Cleanup the documentation in the RobotStatePublisher class. ([#172](https://github.com/ros/robot_state_publisher/issues/172))
- Always publish fixed frames to /tf\_static ([#158](https://github.com/ros/robot_state_publisher/issues/158))
- corrected publish\_frequency default in README ([#166](https://github.com/ros/robot_state_publisher/issues/166))
- Add tf frame\_prefix parameter ([#159](https://github.com/ros/robot_state_publisher/issues/159))
- Contributors: Abrar Rahman Protyasha, Anthony Deschamps, Chris Lalancette, Jacob Perron, Kenji Brameld, Nils Schulte, Russell Joyce, Shane Loretz, Steve Nogar

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/humble/ros2action/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/humble/ros2bag/CHANGELOG.rst)

- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Bump version number to avoid conflict
- Make sure published messages are acknowledged for play mode ([#951](https://github.com/ros2/rosbag2/issues/951))
- TopicFilter use regex\_search instead of regex\_match ([#932](https://github.com/ros2/rosbag2/issues/932))
- Add start-offset play option ([#931](https://github.com/ros2/rosbag2/issues/931))
- Expose bag\_rewrite as `ros2 bag convert` ([#921](https://github.com/ros2/rosbag2/issues/921))
- Add “ignore leaf topics” option to recorder ([#925](https://github.com/ros2/rosbag2/issues/925))
- Auto-detect storage\_id for Reader (if possible) ([#918](https://github.com/ros2/rosbag2/issues/918))
- Add pause/resume options to the bag recorder ([#905](https://github.com/ros2/rosbag2/issues/905))
- Add –start-paused option to `ros2 bag play` ([#904](https://github.com/ros2/rosbag2/issues/904))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Fix converter plugin choices for record ([#897](https://github.com/ros2/rosbag2/issues/897))
- Add missing spaces to error message ([#875](https://github.com/ros2/rosbag2/issues/875))
- keyboard controls for pause/resume toggle and play-next: ([#847](https://github.com/ros2/rosbag2/issues/847))
- Add –snapshot-mode argument to the “record” verb ([#851](https://github.com/ros2/rosbag2/issues/851))
- Refactor plugin query mechanism and standardize trait management ([#833](https://github.com/ros2/rosbag2/issues/833))
- Update `PlayOptions::delay` to `rclcpp::Duration` to get nanosecond resolution ([#843](https://github.com/ros2/rosbag2/issues/843))
- Load compression and serialization choices via plugin query ([#827](https://github.com/ros2/rosbag2/issues/827))
- Add delay option ([#789](https://github.com/ros2/rosbag2/issues/789))
- Avoid passing exception KeyboardInterrupt to the upper layer ([#788](https://github.com/ros2/rosbag2/issues/788))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Kosuke Takeuchi, Michel Hidalgo, Sonia Jin, Tony Peng

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/humble/ros2cli/CHANGELOG.rst)

- Fix importlib\_metadata warning on Python 3.10. ([#706](https://github.com/ros2/ros2cli/issues/706))
- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Use try\_shutdown() instead of shutdown() in DirectNode.\_\_exit\_\_() ([#683](https://github.com/ros2/ros2cli/issues/683))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Reapply [#659](https://github.com/ros2/ros2cli/issues/659) ([#661](https://github.com/ros2/ros2cli/issues/661))
- Revert “Make the ros2cli output always line buffered ([#659](https://github.com/ros2/ros2cli/issues/659))” ([#660](https://github.com/ros2/ros2cli/issues/660))
- Make the ros2cli output always line buffered ([#659](https://github.com/ros2/ros2cli/issues/659))
- add uuid to ros2 daemon node name. ([#658](https://github.com/ros2/ros2cli/issues/658))
- Transfer daemon socket ownership on spawn. ([#652](https://github.com/ros2/ros2cli/issues/652))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Tomoya Fujita

<a id="ros2cli-test-interfaces"></a>

## [ros2cli\_test\_interfaces](https://github.com/ros2/ros2cli/tree/humble/ros2cli_test_interfaces/CHANGELOG.rst)

- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="ros2component"></a>

## [ros2component](https://github.com/ros2/ros2cli/tree/humble/ros2component/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Drop deprecated get\_container\_components\_info() API. ([#647](https://github.com/ros2/ros2cli/issues/647))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Michel Hidalgo

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/humble/ros2doctor/CHANGELOG.rst)

- Fix importlib\_metadata warning on Python 3.10. ([#706](https://github.com/ros2/ros2cli/issues/706))
- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Switch ros2 doctor to using psutil for network checks. ([#687](https://github.com/ros2/ros2cli/issues/687))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Improve ros2 doctor on Windows. ([#631](https://github.com/ros2/ros2cli/issues/631))
- Add QoS compatibility check and report. ([#621](https://github.com/ros2/ros2cli/issues/621))
- Contributors: Aditya Pande, Alberto Soragna, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz

<a id="ros2interface"></a>

## [ros2interface](https://github.com/ros2/ros2cli/tree/humble/ros2interface/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

<a id="ros2launch"></a>

## [ros2launch](https://github.com/ros2/launch_ros/tree/humble/ros2launch/CHANGELOG.rst)

- Update maintainers in setup.py ([#287](https://github.com/ros2/launch_ros/issues/287))
- Use frontend group dependency & explicit dependencies in ros2launch ([#256](https://github.com/ros2/launch_ros/issues/256))
- Update package maintainers ([#284](https://github.com/ros2/launch_ros/issues/284))
- Add regex filter for selective launch-prefix application ([#261](https://github.com/ros2/launch_ros/issues/261))
- Resolves [#37](https://github.com/ros2/launch_ros/issues/37) - Added –launch-prefix argument for ‘ros2 launch’ command ([#254](https://github.com/ros2/launch_ros/issues/254))
- Use sets of file extensions provided by parser extensions ([#252](https://github.com/ros2/launch_ros/issues/252))
- Simplify logic to fix absolute paths ([#230](https://github.com/ros2/launch_ros/issues/230))
- add way to include other Python launch files ([launch #122](https://github.com/ros2/launch/issues/122))
- Contributors: Audrow Nash, Cameron Miller, Christophe Bedard, Michel Hidalgo, rob-clarke

<a id="ros2lifecycle"></a>

## [ros2lifecycle](https://github.com/ros2/ros2cli/tree/humble/ros2lifecycle/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

<a id="ros2lifecycle-test-fixtures"></a>

## [ros2lifecycle\_test\_fixtures](https://github.com/ros2/ros2cli/tree/humble/ros2lifecycle_test_fixtures/CHANGELOG.rst)

- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="ros2multicast"></a>

## [ros2multicast](https://github.com/ros2/ros2cli/tree/humble/ros2multicast/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="ros2node"></a>

## [ros2node](https://github.com/ros2/ros2cli/tree/humble/ros2node/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/humble/ros2param/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Fix how ros2 param interprets command-line arguments. ([#684](https://github.com/ros2/ros2cli/issues/684))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Removed redundant code ([#666](https://github.com/ros2/ros2cli/issues/666))
- Reapply [#659](https://github.com/ros2/ros2cli/issues/659) ([#661](https://github.com/ros2/ros2cli/issues/661))
- Fix flaky ros2 param list ([#656](https://github.com/ros2/ros2cli/issues/656))
- Skip None Result ([#646](https://github.com/ros2/ros2cli/issues/646))
- add ‘–write’ option to avoid an unintentional data loss. ([#638](https://github.com/ros2/ros2cli/issues/638))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Jay Wang, Tomoya Fujita

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/humble/ros2pkg/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Use local git config instead of global ([#693](https://github.com/ros2/ros2cli/issues/693))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- [ros2pkg] Skip copyright tests in template packages ([#676](https://github.com/ros2/ros2cli/issues/676))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Generate LICENSE files on ros2 pkg create. ([#650](https://github.com/ros2/ros2cli/issues/650))
- Handle ValueError ([#643](https://github.com/ros2/ros2cli/issues/643))
- Pass package exports to template in pkg create api ([#619](https://github.com/ros2/ros2cli/issues/619)) ([#628](https://github.com/ros2/ros2cli/issues/628))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Amro Al-Baali, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz, rob-clarke, tim-fan

<a id="ros2run"></a>

## [ros2run](https://github.com/ros2/ros2cli/tree/humble/ros2run/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- check subprocess.returncode to print error message. ([#639](https://github.com/ros2/ros2cli/issues/639))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Tomoya Fujita

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/humble/ros2service/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Also provide –include-hidden-services for `ros2 service list` verb ([#551](https://github.com/ros2/ros2cli/issues/551))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Karsten Knese, Shane Loretz

<a id="ros2test"></a>

## [ros2test](https://github.com/ros2/ros_testing/tree/humble/ros2test/CHANGELOG.rst)

- Use new domain\_coordinator API ([#10](https://github.com/ros2/ros_testing/issues/10))
- Contributors: Timo Röhling

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/humble/ros2topic/CHANGELOG.rst)

- Add timeout to kill hanging tests ([#701](https://github.com/ros2/ros2cli/issues/701))
- Add yaml dump flow style. ([#698](https://github.com/ros2/ros2cli/issues/698))
- support ros2topic echo once option. ([#695](https://github.com/ros2/ros2cli/issues/695))
- Fix special case for fastrtps incompatible QoS. ([#694](https://github.com/ros2/ros2cli/issues/694))
- Depend on launch packages instead of ros\_testing to avoid circular dependency ([#685](https://github.com/ros2/ros2cli/issues/685))
- Add QoS history and depth information if available. ([#678](https://github.com/ros2/ros2cli/issues/678))
- Cleanup mislabeled BSD license ([#447](https://github.com/ros2/ros2cli/issues/447))
- Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673](https://github.com/ros2/ros2cli/issues/673))
- Updated maintainers ([#670](https://github.com/ros2/ros2cli/issues/670))
- Update lost messages test case ([#669](https://github.com/ros2/ros2cli/issues/669))
- Implementation of message filtering for ros2 ([#654](https://github.com/ros2/ros2cli/issues/654))
- Change default QoSProfile for pub ([#653](https://github.com/ros2/ros2cli/issues/653))
- Add option in ros2 topic pub to wait for N matching subscriptions, use N=1 by default when combined with –times ([#642](https://github.com/ros2/ros2cli/issues/642))
- `ros2 topic pub` starts publishing right away. ([#626](https://github.com/ros2/ros2cli/issues/626))
- Fix Topic Info Test with “Infinite” printing ([#616](https://github.com/ros2/ros2cli/issues/616))
- Add changelogs ([#635](https://github.com/ros2/ros2cli/issues/635))
- QoS autodetection ([#613](https://github.com/ros2/ros2cli/issues/613))
- Make Lost Messages option ON by default ([#633](https://github.com/ros2/ros2cli/issues/633))
- Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Emerson Knapp, Gonzo, Ivan Santiago Paunovic, Jorge Perez, Shane Loretz, Tomoya Fujita, Tully Foote, matthews-jca

<a id="ros2trace"></a>

## [ros2trace](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/ros2trace/CHANGELOG.rst)

- Fix ‘ros2 trace’ fini() error
- Don’t require kernel tracer and detect when it’s not installed
- Deprecate ‘context\_names’ param and replace with ‘context\_fields’
- Contributors: Christophe Bedard

<a id="rosbag2"></a>

## [rosbag2](https://github.com/ros2/rosbag2/tree/humble/rosbag2/CHANGELOG.rst)

- Bump version number to avoid conflict
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression/CHANGELOG.rst)

- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Remove unnecessary public definition. ([#950](https://github.com/ros2/rosbag2/issues/950))
- Changes for uncrustify 0.72 ([#937](https://github.com/ros2/rosbag2/issues/937))
- Bugfix for broken bag split when using cache ([#936](https://github.com/ros2/rosbag2/issues/936))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Don’t preprocess a storage file more than once ([#895](https://github.com/ros2/rosbag2/issues/895))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Refactor plugin query mechanism and standardize trait management ([#833](https://github.com/ros2/rosbag2/issues/833))
- fix sequential reader rollover-to-next-file strategy: ([#839](https://github.com/ros2/rosbag2/issues/839))
- Load compression and serialization choices via plugin query ([#827](https://github.com/ros2/rosbag2/issues/827))
- Contributors: Cameron Miller, Chris Lalancette, Michael Orlov, Michel Hidalgo, Shane Loretz, sonia

<a id="rosbag2-compression-zstd"></a>

## [rosbag2\_compression\_zstd](https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression_zstd/CHANGELOG.rst)

- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/humble/rosbag2_cpp/CHANGELOG.rst)

- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Remove unnecessary public definition. ([#950](https://github.com/ros2/rosbag2/issues/950))
- Fix relative path syntax for cpplint ([#947](https://github.com/ros2/rosbag2/issues/947))
- Mark up the message\_cache with TSA annotations ([#946](https://github.com/ros2/rosbag2/issues/946))
- Changes for uncrustify 0.72 ([#937](https://github.com/ros2/rosbag2/issues/937))
- Redesign in cache consumer and circular message cache to get rid from busy loop ([#941](https://github.com/ros2/rosbag2/issues/941))
- Bugfix for broken bag split when using cache ([#936](https://github.com/ros2/rosbag2/issues/936))
- Remove JumpHandler copy-implementation from PlayerClock/TimeControllerClock ([#935](https://github.com/ros2/rosbag2/issues/935))
- Auto-detect storage\_id for Reader (if possible) ([#918](https://github.com/ros2/rosbag2/issues/918))
- Add –start-paused option to `ros2 bag play` ([#904](https://github.com/ros2/rosbag2/issues/904))
- Use the message\_introspection header to get MessageMember. ([#903](https://github.com/ros2/rosbag2/issues/903))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Fix converter plugin choices for record ([#897](https://github.com/ros2/rosbag2/issues/897))
- Enable sanitizers only if code actually can run ([#572](https://github.com/ros2/rosbag2/issues/572))
- Need to pass introspection TS to converter plugin for it to be useful ([#896](https://github.com/ros2/rosbag2/issues/896))
- Don’t preprocess a storage file more than once ([#895](https://github.com/ros2/rosbag2/issues/895))
- Fix a bug on invalid pointer address when using “MESSAGE” compressio… ([#866](https://github.com/ros2/rosbag2/issues/866))
- Metadata per file info ([#870](https://github.com/ros2/rosbag2/issues/870))
- Fix TSA warnings when building with clang thread analysis. ([#877](https://github.com/ros2/rosbag2/issues/877))
- Implement snapshot mechanism and corresponding ROS Service ([#850](https://github.com/ros2/rosbag2/issues/850))
- Circular Message Cache implementation for snapshot feature ([#844](https://github.com/ros2/rosbag2/issues/844))
- Fix discovery silently stops after unknown msg type is found. ([#848](https://github.com/ros2/rosbag2/issues/848))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Refactor plugin query mechanism and standardize trait management ([#833](https://github.com/ros2/rosbag2/issues/833))
- fix sequential reader rollover-to-next-file strategy: ([#839](https://github.com/ros2/rosbag2/issues/839))
- Load compression and serialization choices via plugin query ([#827](https://github.com/ros2/rosbag2/issues/827))
- Workaround for false positive findings by clang thread safety analysis in time controller jump callbacks API. ([#799](https://github.com/ros2/rosbag2/issues/799))
- Add callbacks for PlayerClock::jump(time\_point) API with CI fix ([#779](https://github.com/ros2/rosbag2/issues/779))
- Revert “Add callbacks for PlayerClock::jump(time\_point) API ([#775](https://github.com/ros2/rosbag2/issues/775))” ([#778](https://github.com/ros2/rosbag2/issues/778))
- Add callbacks for PlayerClock::jump(time\_point) API ([#775](https://github.com/ros2/rosbag2/issues/775))
- Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Lei Liu, Michael Orlov, Michel Hidalgo, Shane Loretz, Tony Peng, Wojciech Jaworski, sonia

<a id="rosbag2-interfaces"></a>

## [rosbag2\_interfaces](https://github.com/ros2/rosbag2/tree/humble/rosbag2_interfaces/CHANGELOG.rst)

- Bump version number to avoid conflict
- Add burst-mode to Player ([#977](https://github.com/ros2/rosbag2/issues/977))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Implement snapshot mechanism and corresponding ROS Service ([#850](https://github.com/ros2/rosbag2/issues/850)) \* Add snapshot service to recorder node \* Simplify and clarify double buffering patterns
- Contributors: Cameron Miller, Chris Lalancette, Geoffrey Biggs, Michel Hidalgo

<a id="rosbag2-performance-benchmarking"></a>

## [rosbag2\_performance\_benchmarking](https://github.com/ros2/rosbag2/tree/humble/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst)

- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916](https://github.com/ros2/rosbag2/issues/916)) \* Enable YAML encoding/decoding for RecordOptions and StorageOptions
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Updated node declare\_parameter to new syntax ([#882](https://github.com/ros2/rosbag2/issues/882))
- Updated benchmark package to use writer close() instead of old reset() ([#881](https://github.com/ros2/rosbag2/issues/881))
- Contributors: Adam Dąbrowski, Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/humble/rosbag2_py/CHANGELOG.rst)

- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Bump version number to avoid conflict
- Make sure published messages are acknowledged for play mode ([#951](https://github.com/ros2/rosbag2/issues/951))
- Fix relative path syntax for cpplint ([#947](https://github.com/ros2/rosbag2/issues/947))
- Update to pybind11 2.7.1 ([#945](https://github.com/ros2/rosbag2/issues/945))
- Add start-offset play option ([#931](https://github.com/ros2/rosbag2/issues/931))
- Expose bag\_rewrite as `ros2 bag convert` ([#921](https://github.com/ros2/rosbag2/issues/921))
- Add “ignore leaf topics” option to recorder ([#925](https://github.com/ros2/rosbag2/issues/925))
- Add a ReaderWriterFactory utility to share logic for reuse ([#923](https://github.com/ros2/rosbag2/issues/923))
- Add pause/resume options to the bag recorder ([#905](https://github.com/ros2/rosbag2/issues/905))
- Add –start-paused option to `ros2 bag play` ([#904](https://github.com/ros2/rosbag2/issues/904))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Fix converter plugin choices for record ([#897](https://github.com/ros2/rosbag2/issues/897))
- Metadata per file info ([#870](https://github.com/ros2/rosbag2/issues/870))
- keyboard controls for pause/resume toggle and play-next: ([#847](https://github.com/ros2/rosbag2/issues/847))
- Add –snapshot-mode argument to the “record” verb ([#851](https://github.com/ros2/rosbag2/issues/851))
- Add stopRecording into rosbag2\_py ([#854](https://github.com/ros2/rosbag2/issues/854))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Refactor plugin query mechanism and standardize trait management ([#833](https://github.com/ros2/rosbag2/issues/833))
- Update `PlayOptions::delay` to `rclcpp::Duration` to get nanosecond resolution ([#843](https://github.com/ros2/rosbag2/issues/843))
- Load compression and serialization choices via plugin query ([#827](https://github.com/ros2/rosbag2/issues/827))
- Add delay option ([#789](https://github.com/ros2/rosbag2/issues/789))
- Handle SIGTERM gracefully in recording ([#792](https://github.com/ros2/rosbag2/issues/792))
- Contributors: Abrar Rahman Protyasha, Afonso da Fonseca Braga, Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Kosuke Takeuchi, Michel Hidalgo, Tony Peng, Wojciech Jaworski, sonia

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage/CHANGELOG.rst)

- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Remove unnecessary public definition. ([#950](https://github.com/ros2/rosbag2/issues/950))
- Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916](https://github.com/ros2/rosbag2/issues/916))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Provide MetadataIO interface to convert metadata to a string in memory, alongside file IO versions ([#894](https://github.com/ros2/rosbag2/issues/894))
- Metadata per file info ([#870](https://github.com/ros2/rosbag2/issues/870))
- Implement snapshot mechanism and corresponding ROS Service ([#850](https://github.com/ros2/rosbag2/issues/850))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Refactor plugin query mechanism and standardize trait management ([#833](https://github.com/ros2/rosbag2/issues/833))
- Contributors: Audrow Nash, Cameron Miller, Chris Lalancette, Emerson Knapp, Jorge Perez, Michel Hidalgo, Shane Loretz, Tony Peng, Wojciech Jaworski, sonia

<a id="rosbag2-storage-default-plugins"></a>

## [rosbag2\_storage\_default\_plugins](https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage_default_plugins/CHANGELOG.rst)

- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Emit a warning rather than crash when a message is too big for sqlite ([#919](https://github.com/ros2/rosbag2/issues/919))
- Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916](https://github.com/ros2/rosbag2/issues/916))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Contributors: Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz, William Woodall, sonia

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/humble/rosbag2_test_common/CHANGELOG.rst)

- Bump version number to avoid conflict
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Make sure the subscription exists before publishing messages ([#804](https://github.com/ros2/rosbag2/issues/804))
- Handle SIGTERM gracefully in recording ([#792](https://github.com/ros2/rosbag2/issues/792))
- Add spin\_and\_wait\_for\_matched to PublicationManager and update test c… ([#797](https://github.com/ros2/rosbag2/issues/797))
- Avoid passing exception KeyboardInterrupt to the upper layer ([#788](https://github.com/ros2/rosbag2/issues/788))
- Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/humble/rosbag2_tests/CHANGELOG.rst)

- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Revert “Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))” ([#984](https://github.com/ros2/rosbag2/issues/984))
- Add the ability to record any key/value pair in the ‘custom’ field in metadata.yaml ([#976](https://github.com/ros2/rosbag2/issues/976))
- Bump version number to avoid conflict
- Add pause/resume options to the bag recorder ([#905](https://github.com/ros2/rosbag2/issues/905))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Fix a bug on invalid pointer address when using “MESSAGE” compressio… ([#866](https://github.com/ros2/rosbag2/issues/866))
- Metadata per file info ([#870](https://github.com/ros2/rosbag2/issues/870))
- Fix record test to reflect plugin query changes ([#838](https://github.com/ros2/rosbag2/issues/838))
- Make sure the subscription exists before publishing messages ([#804](https://github.com/ros2/rosbag2/issues/804))
- Handle SIGTERM gracefully in recording ([#792](https://github.com/ros2/rosbag2/issues/792))
- Add spin\_and\_wait\_for\_matched to PublicationManager and update test c… ([#797](https://github.com/ros2/rosbag2/issues/797))
- Remove rmw\_fastrtps\_cpp find\_package in rosbag2\_tests ([#774](https://github.com/ros2/rosbag2/issues/774))
- Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jorge Perez, Michel Hidalgo, Tony Peng, Wojciech Jaworski

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/humble/rosbag2_transport/CHANGELOG.rst)

- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- support to publish as loaned message ([#981](https://github.com/ros2/rosbag2/issues/981))
- Bump version number to avoid conflict
- Add burst-mode to Player ([#977](https://github.com/ros2/rosbag2/issues/977))
- Install headers to include/${PROJECT\_NAME} ([#958](https://github.com/ros2/rosbag2/issues/958))
- Make sure published messages are acknowledged for play mode ([#951](https://github.com/ros2/rosbag2/issues/951))
- Changes for uncrustify 0.72 ([#937](https://github.com/ros2/rosbag2/issues/937))
- TopicFilter use regex\_search instead of regex\_match ([#932](https://github.com/ros2/rosbag2/issues/932))
- Add start-offset play option ([#931](https://github.com/ros2/rosbag2/issues/931))
- Add parentheses suggested by Clang on OSX to fix build warning ([#930](https://github.com/ros2/rosbag2/issues/930))
- Bag rewriter (C++) ([#920](https://github.com/ros2/rosbag2/issues/920))
- Add “ignore leaf topics” option to recorder ([#925](https://github.com/ros2/rosbag2/issues/925))
- Rewrite TopicFilter for single-call reusability ([#924](https://github.com/ros2/rosbag2/issues/924))
- Add a ReaderWriterFactory utility to share logic for reuse ([#923](https://github.com/ros2/rosbag2/issues/923))
- Add pause/resume options to the bag recorder ([#905](https://github.com/ros2/rosbag2/issues/905))
- Add logging macros for rosbag2\_transport ([#917](https://github.com/ros2/rosbag2/issues/917))
- Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916](https://github.com/ros2/rosbag2/issues/916))
- Expose the QoS object wrapper ([#910](https://github.com/ros2/rosbag2/issues/910))
- Add –start-paused option to `ros2 bag play` ([#904](https://github.com/ros2/rosbag2/issues/904))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Add a Seek service ([#874](https://github.com/ros2/rosbag2/issues/874))
- Add simple keyboard control for playback rate ([#893](https://github.com/ros2/rosbag2/issues/893))
- Fix a bug on invalid pointer address when using “MESSAGE” compressio… ([#866](https://github.com/ros2/rosbag2/issues/866))
- Fix typo ([#880](https://github.com/ros2/rosbag2/issues/880))
- Use Reader’s seek() method for seeking/jumping in Player ([#873](https://github.com/ros2/rosbag2/issues/873))
- keyboard controls for pause/resume toggle and play-next: ([#847](https://github.com/ros2/rosbag2/issues/847))
- Implement snapshot mechanism and corresponding ROS Service ([#850](https://github.com/ros2/rosbag2/issues/850))
- Circular Message Cache implementation for snapshot feature ([#844](https://github.com/ros2/rosbag2/issues/844))
- Add jump/seek API for Player class ([#826](https://github.com/ros2/rosbag2/issues/826))
- Restructure test\_play\_timing to one test per case, to see which times out ([#863](https://github.com/ros2/rosbag2/issues/863))
- Fix discovery silently stops after unknown msg type is found. ([#848](https://github.com/ros2/rosbag2/issues/848))
- Fixing deprecated subscriber callback warnings ([#852](https://github.com/ros2/rosbag2/issues/852))
- Bugfix for race condition in Player::peek\_next\_message\_from\_queue() ([#849](https://github.com/ros2/rosbag2/issues/849))
- added seek interface ([#836](https://github.com/ros2/rosbag2/issues/836))
- Update `PlayOptions::delay` to `rclcpp::Duration` to get nanosecond resolution ([#843](https://github.com/ros2/rosbag2/issues/843))
- Move notification about ready for playback inside play\_messages\_from\_queue() ([#832](https://github.com/ros2/rosbag2/issues/832))
- Add wait for player to be ready for playback in Player::play\_next() method ([#814](https://github.com/ros2/rosbag2/issues/814))
- Make sure the subscription exists before publishing messages ([#804](https://github.com/ros2/rosbag2/issues/804))
- Add delay option ([#789](https://github.com/ros2/rosbag2/issues/789))
- Copy recorder QoS profile to local variable so that temporary value isn’t cleared ([#803](https://github.com/ros2/rosbag2/issues/803))
- test\_play\_services: fail gracefully on future error ([#798](https://github.com/ros2/rosbag2/issues/798))
- Recording with –all and –exclude fix ([#765](https://github.com/ros2/rosbag2/issues/765))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Bastian Jäger, Cameron Miller, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Ivan Santiago Paunovic, Kosuke Takeuchi, Lei Liu, Louise Poubel, Michael Orlov, Michel Hidalgo, Piotr Jaroszek, Shane Loretz, sonia

<a id="rosgraph-msgs"></a>

## [rosgraph\_msgs](https://github.com/ros2/rcl_interfaces/tree/humble/rosgraph_msgs/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="rosidl-adapter"></a>

## [rosidl\_adapter](https://github.com/ros2/rosidl/tree/humble/rosidl_adapter/CHANGELOG.rst)

- rename nested loop index ([#643](https://github.com/ros2/rosidl/issues/643))
- Fix how comments in action interfaces are processed ([#632](https://github.com/ros2/rosidl/issues/632))
- Pass comments in ros interface constants to the .idl generated files ([#630](https://github.com/ros2/rosidl/issues/630))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612](https://github.com/ros2/rosidl/issues/612))
- Fix escaping in string literals ([#595](https://github.com/ros2/rosidl/issues/595))
- Ignore multiple `#` characters and dedent comments ([#594](https://github.com/ros2/rosidl/issues/594))
- Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz, ibnHatab

<a id="rosidl-cli"></a>

## [rosidl\_cli](https://github.com/ros2/rosidl/tree/humble/rosidl_cli/CHANGELOG.rst)

- Fix importlib\_metdata warning with Python 3.10. ([#674](https://github.com/ros2/rosidl/issues/674))
- Update maintainers to Michel Hidalgo and Shane Loretz ([#633](https://github.com/ros2/rosidl/issues/633))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Support passing keyword arguments to rosidl CLI extensions ([#597](https://github.com/ros2/rosidl/issues/597))
- Add missing f for format string ([#600](https://github.com/ros2/rosidl/issues/600))
- Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Shane Loretz

<a id="rosidl-cmake"></a>

## [rosidl\_cmake](https://github.com/ros2/rosidl/tree/humble/rosidl_cmake/CHANGELOG.rst)

- Make rosidl\_get\_typesupport\_target return -NOTFOUND instead of FATAL\_ERROR ([#672](https://github.com/ros2/rosidl/issues/672))
- Add introspection typesupport tests for C/C++ messages ([#651](https://github.com/ros2/rosidl/issues/651))
- Use target output name for exporting typesupport library ([#625](https://github.com/ros2/rosidl/issues/625))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#611](https://github.com/ros2/rosidl/issues/611))
- Add rosidl\_get\_typesupport\_target and deprecate rosidl\_target\_interfaces ([#606](https://github.com/ros2/rosidl/issues/606))
- Bundle and ensure the exportation of rosidl generated targets ([#601](https://github.com/ros2/rosidl/issues/601))
- Contributors: Jonathan Selling, Michel Hidalgo, Shane Loretz

<a id="rosidl-default-generators"></a>

## [rosidl\_default\_generators](https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_generators/CHANGELOG.rst)

- Unroll group dependencies ([#20](https://github.com/ros2/rosidl_defaults/issues/20))
- Contributors: Shane Loretz

<a id="rosidl-default-runtime"></a>

## [rosidl\_default\_runtime](https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_runtime/CHANGELOG.rst)

- Unroll group dependencies ([#20](https://github.com/ros2/rosidl_defaults/issues/20))
- Contributors: Shane Loretz

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/humble/rosidl_generator_c/CHANGELOG.rst)

- Fix error handling when copying C sequence messages ([#671](https://github.com/ros2/rosidl/issues/671))
- Install generated headers to include/${PROJECT\_NAME} ([#670](https://github.com/ros2/rosidl/issues/670))
- Misc cleanup in the rosidl generator extensions ([#662](https://github.com/ros2/rosidl/issues/662))
- Set the output size unconditionally when copying sequences ([#669](https://github.com/ros2/rosidl/issues/669))
- Implement copy function for C messages ([#650](https://github.com/ros2/rosidl/issues/650))
- Implement equality operator function for C messages. ([#648](https://github.com/ros2/rosidl/issues/648))
- Generate documentation in generated C header files based on ROS interfaces comments ([#593](https://github.com/ros2/rosidl/issues/593))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612](https://github.com/ros2/rosidl/issues/612))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#611](https://github.com/ros2/rosidl/issues/611))
- Bundle and ensure the exportation of rosidl generated targets ([#601](https://github.com/ros2/rosidl/issues/601))
- Fix a cpplint allocator regression. ([#590](https://github.com/ros2/rosidl/issues/590))
- Use RCUtils allocators in rosidl\_generator\_c ([#584](https://github.com/ros2/rosidl/issues/584))
- Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Nikolai Morin, Pablo Garrido, Shane Loretz

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/humble/rosidl_generator_cpp/CHANGELOG.rst)

- Install generated headers to include/${PROJECT\_NAME} ([#670](https://github.com/ros2/rosidl/issues/670))
- Misc cleanup in the rosidl generator extensions ([#662](https://github.com/ros2/rosidl/issues/662))
- Add missing build\_export\_depend dependency ([#665](https://github.com/ros2/rosidl/issues/665))
- Fix bug where rosidl\_runtime\_cpp wasn’t depended upon ([#660](https://github.com/ros2/rosidl/issues/660))
- Fix include order for cpplint ([#644](https://github.com/ros2/rosidl/issues/644))
- Set CXX standard to 17 ([#635](https://github.com/ros2/rosidl/issues/635))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612](https://github.com/ros2/rosidl/issues/612))
- Support flow style YAML printing ([#613](https://github.com/ros2/rosidl/issues/613))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#611](https://github.com/ros2/rosidl/issues/611))
- Relocate to\_yaml() under message namespace ([#609](https://github.com/ros2/rosidl/issues/609))
- Bundle and ensure the exportation of rosidl generated targets ([#601](https://github.com/ros2/rosidl/issues/601))
- Contributors: Jacob Perron, Jorge Perez, Michel Hidalgo, Shane Loretz, Øystein Sture

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/humble/rosidl_generator_dds_idl/CHANGELOG.rst)

- Add changelog ([#56](https://github.com/ros2/rosidl_dds/issues/56))
- Contributors: Ivan Santiago Paunovic

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/humble/rosidl_generator_py/CHANGELOG.rst)

- Removes erroneous unmatched closing parenthesis ([#125](https://github.com/ros2/rosidl_python/issues/125))
- require Python 3.6 as we use format strings in various places ([#152](https://github.com/ros2/rosidl_python/issues/152))
- Fix rosidl\_generator\_py assuming incorect library names ([#149](https://github.com/ros2/rosidl_python/issues/149))
- Fix for msg file containing a property field that is not at the end ([#151](https://github.com/ros2/rosidl_python/issues/151))
- Update package maintainers ([#147](https://github.com/ros2/rosidl_python/issues/147))
- Use rosidl\_get\_typesupport\_target() ([#139](https://github.com/ros2/rosidl_python/issues/139))
- Support available typesupport specification in CLI extension ([#133](https://github.com/ros2/rosidl_python/issues/133))
- Use python\_d for test\_cli\_extension in Debug mode ([#136](https://github.com/ros2/rosidl_python/issues/136))
- Add missing float/double bounds check ([#128](https://github.com/ros2/rosidl_python/issues/128))
- Added optimization for copying arrays using buffer protocol ([#129](https://github.com/ros2/rosidl_python/issues/129))
- Add smoke test for CLI extension ([#132](https://github.com/ros2/rosidl_python/issues/132))
- Install generated Python interfaces in a Python package ([#131](https://github.com/ros2/rosidl_python/issues/131))
- Contributors: Charles Cross, Chen Lihui, Michel Hidalgo, Seulbae Kim, Shane Loretz, William Woodall, ksuszka

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/humble/rosidl_parser/CHANGELOG.rst)

- Set maybe\_placeholders to False for lark 1.+ compatibility ([#664](https://github.com/ros2/rosidl/issues/664))
- Generate documentation in generated C header files based on ROS interfaces comments ([#593](https://github.com/ros2/rosidl/issues/593))
- Pass comments in ros interface constants to the .idl generated files ([#630](https://github.com/ros2/rosidl/issues/630))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Fix escaping in string literals ([#595](https://github.com/ros2/rosidl/issues/595))
- Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_c/CHANGELOG.rst)

- Fix error handling when copying C sequence messages ([#671](https://github.com/ros2/rosidl/issues/671))
- Set the output size unconditionally when copying sequences ([#669](https://github.com/ros2/rosidl/issues/669))
- De-duplicate Quality Level from README and QUALITY\_DECLARATION ([#661](https://github.com/ros2/rosidl/issues/661))
- Install headers to include/${PROJECT\_NAME} ([#658](https://github.com/ros2/rosidl/issues/658))
- Implement copy function for C messages ([#650](https://github.com/ros2/rosidl/issues/650))
- Implement equality operator function for C messages. ([#648](https://github.com/ros2/rosidl/issues/648))
- Set CXX standard to 17 ([#635](https://github.com/ros2/rosidl/issues/635))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Use RCUtils allocators in rosidl\_generator\_c ([#584](https://github.com/ros2/rosidl/issues/584))
- Contributors: Jose Luis Rivero, Michel Hidalgo, Nikolai Morin, Pablo Garrido, Shane Loretz, Øystein Sture

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_cpp/CHANGELOG.rst)

- Add missing dependency on rosidl\_runtime\_c ([#666](https://github.com/ros2/rosidl/issues/666))
- De-duplicate Quality Level from README and QUALITY\_DECLARATION ([#661](https://github.com/ros2/rosidl/issues/661))
- Install headers to include/${PROJECT\_NAME} ([#658](https://github.com/ros2/rosidl/issues/658))
- Set CXX standard to 17 ([#635](https://github.com/ros2/rosidl/issues/635))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz, Øystein Sture

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/humble/CHANGELOG.rst)

- add yaml dump flow style. ([#16](https://github.com/ros2/rosidl_runtime_py/issues/16))
- Update maintainers ([#15](https://github.com/ros2/rosidl_runtime_py/issues/15)) \* Update maintainers to Shane Loretz \* Update Shane’s email Co-authored-by: Shane Loretz <[sloretz@openrobotics.org](mailto:sloretz%40openrobotics.org)>
- Contributors: Audrow Nash, Tomoya Fujita

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_c/CHANGELOG.rst)

- Use target\_link\_libraries(… PRIVATE …) in single typesupport case ([#124](https://github.com/ros2/rosidl_typesupport/issues/124))
- rosidl CMake cleanup in rosidl\_typesupport\_c ([#123](https://github.com/ros2/rosidl_typesupport/issues/123))
- Install headers to include/${PROJECT\_NAME} ([#121](https://github.com/ros2/rosidl_typesupport/issues/121))
- Use FindPython3 ([#118](https://github.com/ros2/rosidl_typesupport/issues/118))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#116](https://github.com/ros2/rosidl_typesupport/issues/116))
- Support available typesupport specification in CLI extensions ([#112](https://github.com/ros2/rosidl_typesupport/issues/112))
- Bundle and ensure the exportation of rosidl generated targets ([#113](https://github.com/ros2/rosidl_typesupport/issues/113))
- Fix C and C++ typesupports CLI extensions ([#111](https://github.com/ros2/rosidl_typesupport/issues/111))
- Contributors: Michel Hidalgo, Shane Loretz

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_cpp/CHANGELOG.rst)

- Use target\_link\_libraries(… PRIVATE …) in single typesupport case ([#124](https://github.com/ros2/rosidl_typesupport/issues/124))
- rosidl CMake cleanup in rosidl\_typesupport\_cpp ([#123](https://github.com/ros2/rosidl_typesupport/issues/123))
- Install headers to include/${PROJECT\_NAME} ([#121](https://github.com/ros2/rosidl_typesupport/issues/121))
- Make sure to check typesupport handles against nullptr properly ([#119](https://github.com/ros2/rosidl_typesupport/issues/119))
- Use FindPython3 ([#118](https://github.com/ros2/rosidl_typesupport/issues/118))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#116](https://github.com/ros2/rosidl_typesupport/issues/116))
- Support available typesupport specification in CLI extensions ([#112](https://github.com/ros2/rosidl_typesupport/issues/112))
- Bundle and ensure the exportation of rosidl generated targets ([#113](https://github.com/ros2/rosidl_typesupport/issues/113))
- Fix C and C++ typesupports CLI extensions ([#111](https://github.com/ros2/rosidl_typesupport/issues/111))
- Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- Install generated headers to include/${PROJECT\_NAME} ([#88](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88))
- Misc fastrtps typesupport generator cleanup ([#87](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87))
- Install headers to include/${PROJECT\_NAME} ([#86](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86))
- Fix include order for cpplint ([#84](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84))
- Update maintainers to Shane Loretz ([#83](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83))
- Use FindPython3 explicitly instead of PythonInterp implicitly ([#78](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78))
- Revert rosidl targets and dependencies exportation ([#76](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76)) \* Revert “Export rosidl\_typesupport\_fastrtps\_c\* dependencies ([#75](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75))” \* Revert “Bundle and ensure the exportation of rosidl generated targets ([#73](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73))”
- Correctly inform that a BoundedSequence is bounded ([#71](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71))
- Export rosidl\_typesupport\_fastrtps\_c\* dependencies ([#75](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75))
- Bundle and ensure the exportation of rosidl generated targets ([#73](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73))
- Fix Fast-RTPS C++ typesupport CLI extension ([#72](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72))
- Fastdds type support extensions ([#67](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67))
- Remove fastrtps dependency ([#68](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68))
- Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Michel Hidalgo, Miguel Company, Shane Loretz

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- Install generated headers to include/${PROJECT\_NAME} ([#88](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88))
- Misc fastrtps typesupport generator cleanup ([#87](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87))
- Install headers to include/${PROJECT\_NAME} ([#86](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86))
- Fix include order for cpplint ([#84](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84)) \* Fix include order for cpplint Relates to <https://github.com/ament/ament_lint/pull/324> \* Use double-quotes for other includes This is backwards compatible with older versions of cpplint.
- Update maintainers to Shane Loretz ([#83](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83))
- Re-introduce improvements to serialization of primitive bounded sequences for C++ type support ([#81](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/81))
- Revert “Improve serialization of … ([#79](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79))” ([#80](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/80))
- Improve serialization of primitive bounded sequences in C++ type support ([#79](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79))
- Use FindPython3 explicitly instead of PythonInterp implicitly ([#78](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78))
- Revert rosidl targets and dependencies exportation ([#76](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76)) \* Revert “Export rosidl\_typesupport\_fastrtps\_c\* dependencies ([#75](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75))” \* Revert “Bundle and ensure the exportation of rosidl generated targets ([#73](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73))”
- Correctly inform that a BoundedSequence is bounded ([#71](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71))
- Export rosidl\_typesupport\_fastrtps\_c\* dependencies ([#75](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75))
- Bundle and ensure the exportation of rosidl generated targets ([#73](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73))
- Fix Fast-RTPS C++ typesupport CLI extension ([#72](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72))
- Fastdds type support extensions ([#67](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67))
- Remove fastrtps dependency ([#68](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68))
- Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Jorge Perez, Michel Hidalgo, Miguel Company, Shane Loretz

<a id="rosidl-typesupport-interface"></a>

## [rosidl\_typesupport\_interface](https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_interface/CHANGELOG.rst)

- De-duplicate Quality Level from README and QUALITY\_DECLARATION ([#661](https://github.com/ros2/rosidl/issues/661))
- Install headers to include/${PROJECT\_NAME} ([#658](https://github.com/ros2/rosidl/issues/658))
- Add ROSIDL\_TYPESUPPORT\_INTERFACE\_\_LIBRARY\_NAME() macro ([#649](https://github.com/ros2/rosidl/issues/649))
- Set CXX standard to 17 ([#635](https://github.com/ros2/rosidl/issues/635))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz, Øystein Sture

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Install generated headers to include/${PROJECT\_NAME} ([#670](https://github.com/ros2/rosidl/issues/670))
- Misc cleanup in the rosidl generator extensions ([#662](https://github.com/ros2/rosidl/issues/662))
- De-duplicate Quality Level from README and QUALITY\_DECLARATION ([#661](https://github.com/ros2/rosidl/issues/661))
- Update Quality declaration to level 1 in README for instrospection pkgs ([#659](https://github.com/ros2/rosidl/issues/659))
- Install headers to include/${PROJECT\_NAME} ([#658](https://github.com/ros2/rosidl/issues/658))
- Move rosidl\_typesupport\_introspection\_cpp quality declaration to Q1 ([#657](https://github.com/ros2/rosidl/issues/657))
- Move rosidl\_typesupport\_introspection\_c quality declaration to Q1 ([#656](https://github.com/ros2/rosidl/issues/656))
- add documentation for generators and API ([#646](https://github.com/ros2/rosidl/issues/646))
- Rework nested types’ items introspection in C and C++ ([#652](https://github.com/ros2/rosidl/issues/652))
- Fix up the documentation for rosidl\_typesupport\_introspection\_c ([#628](https://github.com/ros2/rosidl/issues/628))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Quality Declaration for typesupport\_introspection ([#621](https://github.com/ros2/rosidl/issues/621))
- Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612](https://github.com/ros2/rosidl/issues/612))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#611](https://github.com/ros2/rosidl/issues/611))
- Bundle and ensure the exportation of rosidl generated targets ([#601](https://github.com/ros2/rosidl/issues/601))
- Update function prefix ([#596](https://github.com/ros2/rosidl/issues/596))
- Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo, Pablo Garrido, Shane Loretz, eboasson

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Install generated headers to include/${PROJECT\_NAME} ([#670](https://github.com/ros2/rosidl/issues/670))
- Misc cleanup in the rosidl generator extensions ([#662](https://github.com/ros2/rosidl/issues/662))
- De-duplicate Quality Level from README and QUALITY\_DECLARATION ([#661](https://github.com/ros2/rosidl/issues/661))
- Update Quality declaration to level 1 in README for instrospection pkgs ([#659](https://github.com/ros2/rosidl/issues/659))
- Install headers to include/${PROJECT\_NAME} ([#658](https://github.com/ros2/rosidl/issues/658))
- Move rosidl\_typesupport\_introspection\_cpp quality declaration to Q1 ([#657](https://github.com/ros2/rosidl/issues/657))
- add documentation for generators and API ([#646](https://github.com/ros2/rosidl/issues/646))
- Rework nested types’ items introspection in C and C++ ([#652](https://github.com/ros2/rosidl/issues/652))
- Set CXX standard to 17 ([#635](https://github.com/ros2/rosidl/issues/635))
- Fix up the documentation for rosidl\_typesupport\_introspection\_cpp ([#627](https://github.com/ros2/rosidl/issues/627))
- Update package maintainers ([#624](https://github.com/ros2/rosidl/issues/624))
- Quality Declaration for typesupport\_introspection ([#621](https://github.com/ros2/rosidl/issues/621))
- Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612](https://github.com/ros2/rosidl/issues/612))
- Revert “Bundle and ensure the exportation of rosidl generated targets” ([#611](https://github.com/ros2/rosidl/issues/611))
- Bundle and ensure the exportation of rosidl generated targets ([#601](https://github.com/ros2/rosidl/issues/601))
- Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo, Shane Loretz, eboasson, Øystein Sture

<a id="rosidl-typesupport-introspection-tests"></a>

## [rosidl\_typesupport\_introspection\_tests](https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_tests/CHANGELOG.rst)

- Bump `rosidl_typesupport_introspection_tests` coverage ([#655](https://github.com/ros2/rosidl/issues/655))
- Add introspection typesupport tests for C/C++ services ([#653](https://github.com/ros2/rosidl/issues/653))
- Add introspection typesupport tests for C/C++ messages ([#651](https://github.com/ros2/rosidl/issues/651))
- Contributors: Michel Hidalgo

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/humble/CHANGELOG.rst)

- Make sure to call abspath when adding Windows DLL directories. ([#8](https://github.com/ros2/rpyutils/issues/8))
- Update troubleshooting links to docs.ros.org ([#6](https://github.com/ros2/rpyutils/issues/6))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="rqt-gui"></a>

## [rqt\_gui](https://github.com/ros-visualization/rqt/tree/humble/rqt_gui/CHANGELOG.rst)

- Changed getiter to iter ([#1](https://github.com/ros-visualization/rqt/issues/1)) ([#241](https://github.com/ros-visualization/rqt/issues/241))
- Update maintainers ([#233](https://github.com/ros-visualization/rqt/issues/233)) ([#237](https://github.com/ros-visualization/rqt/issues/237))
- add missing dependencies: rospkg-modules, python\_qt\_binding, rospy ([#227](https://github.com/ros-visualization/rqt/issues/227))
- bump CMake minimum version to avoid CMP0048 warning ([#219](https://github.com/ros-visualization/rqt/issues/219))
- use catkin\_install\_python for Python script ([#206](https://github.com/ros-visualization/rqt/issues/206))
- Contributors: Michael Jeronimo, sven-herrmann

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/humble/rqt_gui_cpp/CHANGELOG.rst)

- Update maintainers ([#233](https://github.com/ros-visualization/rqt/issues/233)) ([#237](https://github.com/ros-visualization/rqt/issues/237))
- bump CMake minimum version to avoid CMP0048 warning ([#219](https://github.com/ros-visualization/rqt/issues/219))
- [Windows] fix rqt\_gui\_cpp install path ([#190](https://github.com/ros-visualization/rqt/issues/190))
- [Windows] fix building ([#189](https://github.com/ros-visualization/rqt/issues/189))
- Contributors: Michael Jeronimo

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/humble/rqt_gui_py/CHANGELOG.rst)

- Update maintainers ([#233](https://github.com/ros-visualization/rqt/issues/233)) ([#237](https://github.com/ros-visualization/rqt/issues/237))
- bump CMake minimum version to avoid CMP0048 warning ([#219](https://github.com/ros-visualization/rqt/issues/219))

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/humble/rqt_py_common/CHANGELOG.rst)

- Update maintainers ([#233](https://github.com/ros-visualization/rqt/issues/233)) ([#237](https://github.com/ros-visualization/rqt/issues/237))
- bump CMake minimum version to avoid CMP0048 warning ([#219](https://github.com/ros-visualization/rqt/issues/219))
- fix missing import bugs ([#139](https://github.com/ros-visualization/rqt/issues/139))
- Contributors: Michael Jeronimo

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/humble/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Update rti-connext-dds dependency to 6.0.1. ([#71](https://github.com/ros2/rmw_connextdds/issues/71))
- Contributors: Steven! Ragnarök

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/humble/rttest/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#114](https://github.com/ros2/realtime_support/issues/114))
- Fix include order for cpplint ([#113](https://github.com/ros2/realtime_support/issues/113))
- Fixes for uncrustify 0.72 ([#111](https://github.com/ros2/realtime_support/issues/111))
- Mark dependent targets as PRIVATE ([#112](https://github.com/ros2/realtime_support/issues/112))
- Export modern CMake targets ([#110](https://github.com/ros2/realtime_support/issues/110))
- Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/humble/rviz2/CHANGELOG.rst)

- Change links index.ros.org -> docs.ros.org. ([#698](https://github.com/ros2/rviz/issues/698))
- Contributors: Chris Lalancette

<a id="rviz-assimp-vendor"></a>

## [rviz\_assimp\_vendor](https://github.com/ros2/rviz/tree/humble/rviz_assimp_vendor/CHANGELOG.rst)

- Make sure to pass compiler and flags down to assimp ([#844](https://github.com/ros2/rviz/issues/844))
- Fix support for assimp 5.1.0 ([#817](https://github.com/ros2/rviz/issues/817))
- Contributors: Chris Lalancette, Silvio Traversaro

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/humble/rviz_common/CHANGELOG.rst)

- Add implementation for cancel interface ([#809](https://github.com/ros2/rviz/issues/809))
- Install headers to include/${PROJECT\_NAME} ([#829](https://github.com/ros2/rviz/issues/829))
- Remove definition of PLUGINLIB\_DISABLE\_BOOST. ([#821](https://github.com/ros2/rviz/issues/821))
- Fix support for assimp 5.1.0 ([#817](https://github.com/ros2/rviz/issues/817))
- Fix cpplint errors ([#818](https://github.com/ros2/rviz/issues/818))
- Set message type for ros topic display ([#800](https://github.com/ros2/rviz/issues/800))
- Fixes for uncrustify 0.72 ([#807](https://github.com/ros2/rviz/issues/807))
- Do not block visualization manager updates when opening the display panel dialog ([#795](https://github.com/ros2/rviz/issues/795))
- Switch to using Qt::MiddleButton for RViz. ([#802](https://github.com/ros2/rviz/issues/802))
- Removed traces in renderPanel ([#777](https://github.com/ros2/rviz/issues/777))
- move yaml\_config\_writer.hpp to public includes ([#764](https://github.com/ros2/rviz/issues/764))
- Update displays\_panel.cpp ([#745](https://github.com/ros2/rviz/issues/745))
- Robot: Report mesh loading issues ([#744](https://github.com/ros2/rviz/issues/744))
- Exposed tool\_manager header file. ([#767](https://github.com/ros2/rviz/issues/767))
- refactor: make const getter methods const ([#756](https://github.com/ros2/rviz/issues/756))
- Efficiently handle 3-bytes pixel formats ([#743](https://github.com/ros2/rviz/issues/743))
- Report sample lost events ([#686](https://github.com/ros2/rviz/issues/686))
- Update window close icon ([#734](https://github.com/ros2/rviz/issues/734))
- Fix missing “X” icon in panel close button ([#731](https://github.com/ros2/rviz/issues/731))
- Add rviz\_rendering dependency to rviz\_common ([#727](https://github.com/ros2/rviz/issues/727))
- Remove the word “Alpha” from the splash screen. ([#696](https://github.com/ros2/rviz/issues/696))
- Removed some memory leaks in rviz\_rendering and rviz\_rendering\_tests ([#710](https://github.com/ros2/rviz/issues/710))
- Contributors: ANDOU Tetsuo, Alejandro Hernández Cordero, Chen Lihui, Chris Lalancette, Daisuke Nishimatsu, Gonzo, Ivan Santiago Paunovic, Jacob Perron, Joseph Schornak, Rebecca Butler, Shane Loretz, Silvio Traversaro, davidorchansky

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/humble/rviz_default_plugins/CHANGELOG.rst)

- Add far plane distance property to camera ([#849](https://github.com/ros2/rviz/issues/849))
- Drop ignition-math6 from rviz\_default\_plugins link interface ([#833](https://github.com/ros2/rviz/issues/833))
- add implementation for cancel interface ([#809](https://github.com/ros2/rviz/issues/809))
- Install headers to include/${PROJECT\_NAME} ([#829](https://github.com/ros2/rviz/issues/829))
- Remove definition of PLUGINLIB\_DISABLE\_BOOST. ([#821](https://github.com/ros2/rviz/issues/821))
- Remove TF filter from ImageTransportDisplay ([#788](https://github.com/ros2/rviz/issues/788))
- Add underscores to material names ([#811](https://github.com/ros2/rviz/issues/811))
- Export image\_transport dependency ([#813](https://github.com/ros2/rviz/issues/813))
- Fixes for uncrustify 0.72 ([#807](https://github.com/ros2/rviz/issues/807))
- Switch to using Qt::MiddleButton for RViz. ([#802](https://github.com/ros2/rviz/issues/802))
- Add a tf\_buffer\_cache\_time\_ns to tf\_wrapper ([#792](https://github.com/ros2/rviz/issues/792))
- Make libraries to avoid compiling files multiple times ([#774](https://github.com/ros2/rviz/issues/774))
- Computed inertia with ignition-math ([#751](https://github.com/ros2/rviz/issues/751))
- Fixed crash when changing rendering parameters for pointcloud2 while ‘Selectable’ box is unchecked ([#768](https://github.com/ros2/rviz/issues/768))
- Robot: Report mesh loading issues ([#744](https://github.com/ros2/rviz/issues/744))
- Handle NaN values for Wrench msgs ([#746](https://github.com/ros2/rviz/issues/746))
- Triangle lists support textures ([#719](https://github.com/ros2/rviz/issues/719))
- Report sample lost events ([#686](https://github.com/ros2/rviz/issues/686))
- Fix path message orientation error ([#736](https://github.com/ros2/rviz/issues/736))
- Set topic namespace in interactive markers display ([#725](https://github.com/ros2/rviz/issues/725))
- mass property visualization ([#714](https://github.com/ros2/rviz/issues/714))
- Export InteractiveMarker ([#718](https://github.com/ros2/rviz/issues/718))
- Yuv to rgb changes ([#701](https://github.com/ros2/rviz/issues/701))
- Extract message type in ImageTransportDisplay ([#711](https://github.com/ros2/rviz/issues/711))
- Duplicated code RobotJoint ([#702](https://github.com/ros2/rviz/issues/702))
- Don’t attempt to moc generate files that don’t have QOBJECT. ([#690](https://github.com/ros2/rviz/issues/690))
- Switch to including tf2\_geometry\_msgs.hpp ([#689](https://github.com/ros2/rviz/issues/689))
- Export Qt5 dependencies properly ([#687](https://github.com/ros2/rviz/issues/687))
- Add support for namespace-scoped DELETEALL action in Marker displays ([#685](https://github.com/ros2/rviz/issues/685))
- Use image\_transport to subscribe to image messages ([#523](https://github.com/ros2/rviz/issues/523))
- Contributors: Akash, Alejandro Hernández Cordero, Audrow Nash, Chen Lihui, Chris Lalancette, Cory Crean, Gonzo, Greg Balke, Ivan Santiago Paunovic, Jacob Perron, Martin Idel, Michel Hidalgo, Paul, Rebecca Butler, Scott K Logan, Shane Loretz, bailaC, brian soe, cturcotte-qnx, ketatam

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/humble/rviz_ogre_vendor/CHANGELOG.rst)

- Fix interface link libraries in ogre vendor ([#761](https://github.com/ros2/rviz/issues/761))
- Fix the build for Ubuntu Jammy arm64. ([#828](https://github.com/ros2/rviz/issues/828))
- Strip RPATH from installed Ogre binaries ([#688](https://github.com/ros2/rviz/issues/688))
- Contributors: Chris Lalancette, Laszlo Turanyi, Michel Hidalgo

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/humble/rviz_rendering/CHANGELOG.rst)

- Make getVerticesPerPoint method public and improve tests ([#843](https://github.com/ros2/rviz/issues/843))
- Disable class-memaccess warnings for Eigen ([#838](https://github.com/ros2/rviz/issues/838))
- Disable a warning when including Eigen. ([#835](https://github.com/ros2/rviz/issues/835))
- Install headers to include/${PROJECT\_NAME} ([#829](https://github.com/ros2/rviz/issues/829))
- Fix support for assimp 5.1.0 ([#817](https://github.com/ros2/rviz/issues/817))
- Fix cpplint errors ([#818](https://github.com/ros2/rviz/issues/818))
- Fixes for uncrustify 0.72 ([#807](https://github.com/ros2/rviz/issues/807))
- Suppress assimp warnings in rviz\_rendering build ([#775](https://github.com/ros2/rviz/issues/775))
- Fix for ogre failing when material already exists ([#729](https://github.com/ros2/rviz/issues/729))
- Removed some memory leaks in rviz\_rendering and rviz\_rendering\_tests ([#710](https://github.com/ros2/rviz/issues/710))
- Export Qt5 dependencies properly ([#687](https://github.com/ros2/rviz/issues/687))
- Putting glsl 1.50 resources back in RenderSystem ([#668](https://github.com/ros2/rviz/issues/668))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Jorge Perez, Michel Hidalgo, Piotr Jaroszek, Scott K Logan, Shane Loretz, Silvio Traversaro, Wolf Vollprecht

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/humble/rviz_rendering_tests/CHANGELOG.rst)

- Removed some memory leaks in rviz\_rendering and rviz\_rendering\_tests ([#710](https://github.com/ros2/rviz/issues/710))
- Contributors: Alejandro Hernández Cordero

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/humble/rviz_visual_testing_framework/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#829](https://github.com/ros2/rviz/issues/829))
- Fixes for uncrustify 0.72 ([#807](https://github.com/ros2/rviz/issues/807))
- Update includes after rcutils/get\_env.h deprecation ([#677](https://github.com/ros2/rviz/issues/677))
- Contributors: Chris Lalancette, Christophe Bedard, Shane Loretz

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/humble/sensor_msgs/CHANGELOG.rst)

- Move the find\_package statements for BUILD\_TESTING ([#186](https://github.com/ros2/common_interfaces/issues/186))
- Feedback on conditional sensor\_msgs\_library target ([#1](https://github.com/ros2/common_interfaces/issues/1)) ([#183](https://github.com/ros2/common_interfaces/issues/183))
- [Fix] Fix image\_encodings.hpp’s URL in README ([#184](https://github.com/ros2/common_interfaces/issues/184))
- [Fix] Fix fill\_image.hpp’s URL in README ([#182](https://github.com/ros2/common_interfaces/issues/182))
- Add sensor\_msgs\_library target and install headers to include/${PROJECT\_NAME} ([#178](https://github.com/ros2/common_interfaces/issues/178))
- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Add YUV420 and YUV444 to image encodings ([#172](https://github.com/ros2/common_interfaces/issues/172))
- Cleanup mislabeled BSD license ([#83](https://github.com/ros2/common_interfaces/issues/83))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Fix rosdoc2 warnings in sensor\_msgs. ([#162](https://github.com/ros2/common_interfaces/issues/162))
- Add equidistant distortion model ([#160](https://github.com/ros2/common_interfaces/issues/160))
- Use rosidl\_get\_typesupport\_target() ([#156](https://github.com/ros2/common_interfaces/issues/156))
- Update CompressedImage documentation: add ‘tiff’ as a supported format ([#154](https://github.com/ros2/common_interfaces/issues/154))
- Contributors: Audrow Nash, Chris Lalancette, Grey, Hemal Shah, Homalozoa X, Ivan Santiago Paunovic, Martin Günther, Michael Jeronimo, Pablo Garrido, Shane Loretz, Tully Foote

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/humble/sensor_msgs_py/CHANGELOG.rst)

- Add in a compatibility layer for older versions of numpy. ([#185](https://github.com/ros2/common_interfaces/issues/185))
- Port pointcloud creation to numpy. ([#175](https://github.com/ros2/common_interfaces/issues/175))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Chris Lalancette, Florian Vahl

<a id="shape-msgs"></a>

## [shape\_msgs](https://github.com/ros2/common_interfaces/tree/humble/shape_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Add prism type to the SolidPrimitive.msg ([#166](https://github.com/ros2/common_interfaces/issues/166)) ([#167](https://github.com/ros2/common_interfaces/issues/167))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey, M. Fatih Cırıt

<a id="shared-queues-vendor"></a>

## [shared\_queues\_vendor](https://github.com/ros2/rosbag2/tree/humble/shared_queues_vendor/CHANGELOG.rst)

- Bump version number to avoid conflict
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="sqlite3-vendor"></a>

## [sqlite3\_vendor](https://github.com/ros2/rosbag2/tree/humble/sqlite3_vendor/CHANGELOG.rst)

- Bump version number to avoid conflict
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Contributors: Chris Lalancette, Michel Hidalgo

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/humble/sros2/CHANGELOG.rst)

- Increase the shutdown timeout for test\_generate\_policy\_no\_nodes. ([#278](https://github.com/ros2/sros2/issues/278))
- Contributors: Chris Lalancette

<a id="statistics-msgs"></a>

## [statistics\_msgs](https://github.com/ros2/rcl_interfaces/tree/humble/statistics_msgs/CHANGELOG.rst)

- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Contributors: Audrow Nash

<a id="std-msgs"></a>

## [std\_msgs](https://github.com/ros2/common_interfaces/tree/humble/std_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="std-srvs"></a>

## [std\_srvs](https://github.com/ros2/common_interfaces/tree/humble/std_srvs/CHANGELOG.rst)

- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash

<a id="stereo-msgs"></a>

## [stereo\_msgs](https://github.com/ros2/common_interfaces/tree/humble/stereo_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/humble/test_cli/CHANGELOG.rst)

- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Merge pull request [#356](https://github.com/ros2/system_tests/issues/356) from ros2/issue/321\_enhance\_parameter\_api
- Contributors: Aditya Pande, Ivan Santiago Paunovic

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/humble/test_cli_remapping/CHANGELOG.rst)

- Update python nodes SIGINT handling ([#490](https://github.com/ros2/system_tests/issues/490))
- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Contributors: Aditya Pande, Ivan Santiago Paunovic

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/humble/test_communication/CHANGELOG.rst)

- Split test\_subscriber into multiple compilation units. ([#500](https://github.com/ros2/system_tests/issues/500))
- Add test\_msgs dependency ([#497](https://github.com/ros2/system_tests/issues/497))
- Update python nodes SIGINT handling ([#490](https://github.com/ros2/system_tests/issues/490))
- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Fix deprecated subscriber callback warnings ([#483](https://github.com/ros2/system_tests/issues/483))
- Add tests for BoundedPlainSequences ([#481](https://github.com/ros2/system_tests/issues/481))
- Use rosidl\_get\_typesupport\_target() ([#480](https://github.com/ros2/system_tests/issues/480))
- Use rcpputils/scope\_exit.hpp instead of rclcpp/scope\_exit.hpp ([#479](https://github.com/ros2/system_tests/issues/479))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz

<a id="test-interface-files"></a>

## [test\_interface\_files](https://github.com/ros2/test_interface_files/tree/humble/CHANGELOG.rst)

- Revert “Update package.xml ([#18](https://github.com/ros2/test_interface_files/issues/18))” ([#19](https://github.com/ros2/test_interface_files/issues/19))
- Update package.xml ([#18](https://github.com/ros2/test_interface_files/issues/18))
- Update maintainers to Audrow Nash ([#17](https://github.com/ros2/test_interface_files/issues/17))
- Added BoundedPlainSequences messages ([#14](https://github.com/ros2/test_interface_files/issues/14))
- Contributors: Audrow Nash, Chris Lalancette, Miguel Company, Nikolai Morin

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/humble/test_launch_ros/CHANGELOG.rst)

- Increase test time tolerance ([#305](https://github.com/ros2/launch_ros/issues/305))
- Use correct namespace when evaluating parameter files for composable nodes ([#303](https://github.com/ros2/launch_ros/issues/303))
- Handle empty strings when evaluating parameters ([#300](https://github.com/ros2/launch_ros/issues/300))
- Add parameter substitution ([#297](https://github.com/ros2/launch_ros/issues/297))
- More Helpful Error Messages ([#275](https://github.com/ros2/launch_ros/issues/275))
- Update maintainers in setup.py ([#287](https://github.com/ros2/launch_ros/issues/287))
- Set parameters from file for composable nodes ([#281](https://github.com/ros2/launch_ros/issues/281))
- Update package maintainers ([#284](https://github.com/ros2/launch_ros/issues/284))
- Update node name matcher ([#282](https://github.com/ros2/launch_ros/issues/282))
- Support both parameter file configurations for composable nodes ([#259](https://github.com/ros2/launch_ros/issues/259))
- Shutdown context after test ([#267](https://github.com/ros2/launch_ros/issues/267))
- Handle substitutions in RosTimer ([#264](https://github.com/ros2/launch_ros/issues/264))
- Add SetParametersFromFile action ([#260](https://github.com/ros2/launch_ros/issues/260))
- Properly support ros\_args attribute through launch frontends ([#253](https://github.com/ros2/launch_ros/issues/253))
- Add ‘push\_ros\_namespace’ alias to ‘push-ros-namespace’ ([#250](https://github.com/ros2/launch_ros/issues/250))
- Add ros\_arguments option to Node action ([#249](https://github.com/ros2/launch_ros/issues/249))
- ROS Timer Action ([#244](https://github.com/ros2/launch_ros/issues/244))
- Support container in frontend ([#235](https://github.com/ros2/launch_ros/issues/235))
- Added normalize\_remap\_rule and types. ([launch #173](https://github.com/ros2/launch/issues/173))
- Fixed setup.py versions ([launch #155](https://github.com/ros2/launch/issues/155))
- Fixed a bug to ensure that shutdown event is handled correctly ([launch #154](https://github.com/ros2/launch/issues/154))
- Made various fixes and added tests for remappings passed to Node actions ([launch #137](https://github.com/ros2/launch/issues/137))
- Contributors: Aditya Pande, Audrow Nash, Christophe Bedard, David V. Lu!!, Jacob Perron, Jorge Perez, Kenji Miyake, Michel Hidalgo, Rebecca Butler

<a id="test-launch-testing"></a>

## [test\_launch\_testing](https://github.com/ros2/launch/tree/humble/test_launch_testing/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Michel Hidalgo ([#559](https://github.com/ros2/launch/issues/559))
- Updated maintainers ([#555](https://github.com/ros2/launch/issues/555))
- Contributors: Aditya Pande, Audrow Nash

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/humble/test_msgs/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} and Depend on rosidl\_typesupport\_\* targets directly ([#133](https://github.com/ros2/rcl_interfaces/issues/133))
- Update maintainers to Chris Lalancette ([#130](https://github.com/ros2/rcl_interfaces/issues/130))
- Add test fixures for BoundedPlainSequences ([#125](https://github.com/ros2/rcl_interfaces/issues/125))
- Added BoundedPlainSequences to test\_msgs ([#123](https://github.com/ros2/rcl_interfaces/issues/123))
- Contributors: Audrow Nash, Miguel Company, Shane Loretz

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/humble/test_quality_of_service/CHANGELOG.rst)

- Update maintainers to Aditya Pande and Shane Loretz ([#491](https://github.com/ros2/system_tests/issues/491))
- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Fix deprecated subscriber callback warnings ([#483](https://github.com/ros2/system_tests/issues/483))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Ivan Santiago Paunovic

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/humble/test_rclcpp/CHANGELOG.rst)

- Fix include order for cpplint ([#493](https://github.com/ros2/system_tests/issues/493))
- Fix test ([#488](https://github.com/ros2/system_tests/issues/488))
- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Add tests for rclcpp sigterm handler ([#485](https://github.com/ros2/system_tests/issues/485))
- Fix deprecated subscriber callback warnings ([#483](https://github.com/ros2/system_tests/issues/483))
- Fix deprecation warnings and failures after client API update ([#482](https://github.com/ros2/system_tests/issues/482))
- Use rosidl\_get\_typesupport\_target() ([#480](https://github.com/ros2/system_tests/issues/480))
- Use rcpputils/scope\_exit.hpp instead of rclcpp/scope\_exit.hpp ([#479](https://github.com/ros2/system_tests/issues/479))
- Add test for defered service callback signature ([#478](https://github.com/ros2/system_tests/issues/478))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Merge pull request [#357](https://github.com/ros2/system_tests/issues/357) from ros2/ros2\_658\_leftovers
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Mauro Passerino, Shane Loretz

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/humble/test_rmw_implementation/CHANGELOG.rst)

- add content-filtered-topic interfaces ([#181](https://github.com/ros2/rmw_implementation/issues/181))
- Fix linter issues ([#200](https://github.com/ros2/rmw_implementation/issues/200))
- Add client/service QoS getters. ([#196](https://github.com/ros2/rmw_implementation/issues/196))
- Added tests for bounded sequences serialization ([#193](https://github.com/ros2/rmw_implementation/issues/193))
- Add RMW\_DURATION\_INFINITE basic compliance test. ([#194](https://github.com/ros2/rmw_implementation/issues/194))
- Test SubscriptionOptions::ignore\_local\_publications. ([#192](https://github.com/ros2/rmw_implementation/issues/192))
- Add rmw\_publisher\_wait\_for\_all\_acked. ([#188](https://github.com/ros2/rmw_implementation/issues/188))
- Wait for server in test\_rmw\_implementation service tests. ([#191](https://github.com/ros2/rmw_implementation/issues/191))
- Contributors: Barry Xu, Chen Lihui, Emerson Knapp, Jorge Perez, Jose Antonio Moral, Michel Hidalgo, Miguel Company, mauropasse

<a id="test-security"></a>

## [test\_security](https://github.com/ros2/system_tests/tree/humble/test_security/CHANGELOG.rst)

- Updated maintainers ([#489](https://github.com/ros2/system_tests/issues/489))
- Fix deprecated subscriber callback warnings ([#483](https://github.com/ros2/system_tests/issues/483))
- Add changelogs ([#473](https://github.com/ros2/system_tests/issues/473))
- Simplify the test\_secure\_subscriber code. ([#471](https://github.com/ros2/system_tests/issues/471))
- Update includes after rcutils/get\_env.h deprecation ([#472](https://github.com/ros2/system_tests/issues/472))
- Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/humble/test_tf2/CHANGELOG.rst)

- Fix more instances of Eigen problems on RHEL. ([#515](https://github.com/ros2/geometry2/issues/515))
- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- Fix precision loss from using rclcpp::Time::seconds() ([#511](https://github.com/ros2/geometry2/issues/511))
- More Intuitive CLI for Static Transform Publisher ([#392](https://github.com/ros2/geometry2/issues/392))
- Conversion tests for toMsg() ([#423](https://github.com/ros2/geometry2/issues/423))
- Deprecate tf2\_geometry\_msgs.h ([#418](https://github.com/ros2/geometry2/issues/418))
- Deprecate tf2\_kdl.h ([#414](https://github.com/ros2/geometry2/issues/414))
- Deprecate tf2\_bullet.h ([#412](https://github.com/ros2/geometry2/issues/412))
- Contributors: Bjar Ne, Chris Lalancette, Hunter L. Allen, Kenji Brameld, Shane Loretz

<a id="test-tracetools"></a>

## [test\_tracetools](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools/CHANGELOG.rst)

- Introduce constants for tracepoint names
- Move actual tests out of tracetools\_test to new test\_tracetools package
- Contributors: Christophe Bedard

<a id="test-tracetools-launch"></a>

## [test\_tracetools\_launch](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools_launch/CHANGELOG.rst)

- Add support for preloading pthread and dl instrumentation shared libs
- Remove profile\_fast option and consider LD\_PRELOADing both libs
- Fix multiple LdPreload actions not working and add test
- Deprecate ‘context\_names’ param and replace with ‘context\_fields’
- Move some tests from tracetools\_launch to test\_tracetools\_launch
- Contributors: Christophe Bedard, Ingo Lütkebohle

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/humble/tf2/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- forward declare fromMsg to avoid missing symbols in downstream libraries ([#485](https://github.com/ros2/geometry2/issues/485))
- tf2: Enable common linter tests ([#469](https://github.com/ros2/geometry2/issues/469))
- Move time functions into time.cpp.
- Change a for loop to a while loop.
- Switch to C++-style casts.
- Remove totally unused (and unreachable) code.
- Replace NULL with nullptr.
- Fix up some comments.
- Use std::make\_shared where we can.
- Replace two comparisons with empty string to empty().
- Make sure to include-what-you-use.
- Remove unnecessary internal method.
- Remove long-deprecated walkToTopParent overload.
- Remove unnecessary test dependencies.
- Remove some references to the ROS 1 wiki.
- Add rosidl\_runtime\_cpp as build\_depend and build\_export\_depend.
- Minor cleanups in CMakeLists.txt.
- Remove include directory that doesn’t exist.
- Remove completely unnecessary target\_link\_libraries.
- Remove unused speed\_test from tf2.
- Suppress clang warnings about enumerator attributes. ([#463](https://github.com/ros2/geometry2/issues/463))
- Change TF2Error names to be a bit more descriptive. ([#349](https://github.com/ros2/geometry2/issues/349))
- Fixed errors due to missing header link. ([#432](https://github.com/ros2/geometry2/issues/432))
- Deprecate tf2\_geometry\_msgs.h ([#418](https://github.com/ros2/geometry2/issues/418))
- Speedup covariance unwrapping ([#399](https://github.com/ros2/geometry2/issues/399))
- Contributors: Abrar Rahman Protyasha, Chris Lalancette, Dima Dorezyuk, João C. Monteiro, Shane Loretz, Shivam Pandey

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/humble/tf2_bullet/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- Export a tf2\_bullet::tf2\_bullet target ([#495](https://github.com/ros2/geometry2/issues/495))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Remove some references to the ROS 1 wiki.
- Fix tf2\_bullet dependency export ([#428](https://github.com/ros2/geometry2/issues/428))
- Deprecate tf2\_bullet.h ([#412](https://github.com/ros2/geometry2/issues/412))
- Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/humble/tf2_eigen/CHANGELOG.rst)

- Workaround broken RHEL FindEigen3.cmake ([#513](https://github.com/ros2/geometry2/issues/513))
- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- Disable mem-access warnings on aarch64. ([#506](https://github.com/ros2/geometry2/issues/506))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Remove some references to the ROS 1 wiki.
- Add doTransform function for twists or wrenches ([#406](https://github.com/ros2/geometry2/issues/406))
- Reenable stamped eigen tests ([#429](https://github.com/ros2/geometry2/issues/429))
- Deprecate tf2\_eigen.h ([#413](https://github.com/ros2/geometry2/issues/413))
- Contributors: AndyZe, Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/humble/tf2_eigen_kdl/CHANGELOG.rst)

- Fix more instances of Eigen problems on RHEL. ([#515](https://github.com/ros2/geometry2/issues/515))
- Depend on orocos\_kdl\_vendor ([#473](https://github.com/ros2/geometry2/issues/473))
- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/humble/tf2_geometry_msgs/CHANGELOG.rst)

- Make sure to find the right Python executable. ([#514](https://github.com/ros2/geometry2/issues/514))
- Depend on orocos\_kdl\_vendor ([#473](https://github.com/ros2/geometry2/issues/473))
- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- Drop PyKDL dependency in tf2\_geometry\_msgs ([#509](https://github.com/ros2/geometry2/issues/509))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Export a tf2\_geometry\_msgs::tf2\_geometry\_msgs target ([#496](https://github.com/ros2/geometry2/issues/496))
- Feature: Add doTransform for Wrench messages ([#476](https://github.com/ros2/geometry2/issues/476))
- Remove some references to the ROS 1 wiki.
- Style fixes in tf2\_geometry\_msgs. ([#464](https://github.com/ros2/geometry2/issues/464))
- Fix for issue [#431](https://github.com/ros2/geometry2/issues/431) - Covariance is not transformed in do\_transform\_pose\_with\_covariance\_stamped ([#453](https://github.com/ros2/geometry2/issues/453))
- doTransform non stamped msgs ([#452](https://github.com/ros2/geometry2/issues/452))
- `tf2_geometry_msgs`: Fixing covariance transformation in `doTransform<PoseWithCovarianceStamped, TransformStamped>` ([#430](https://github.com/ros2/geometry2/issues/430))
- Geometry nitpicks ([#426](https://github.com/ros2/geometry2/issues/426))
- Conversion tests for toMsg() ([#423](https://github.com/ros2/geometry2/issues/423))
- Deprecate tf2\_geometry\_msgs.h ([#418](https://github.com/ros2/geometry2/issues/418))
- Contributors: Abrar Rahman Protyasha, Bjar Ne, Chris Lalancette, Denis Štogl, Florian Vahl, Jacob Perron, Khasreto, Shane Loretz, vineet131

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/humble/tf2_kdl/CHANGELOG.rst)

- Depend on orocos\_kdl\_vendor ([#473](https://github.com/ros2/geometry2/issues/473))
- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- KDL python formatting and licenses ([#425](https://github.com/ros2/geometry2/issues/425))
- Deprecate tf2\_kdl.h ([#414](https://github.com/ros2/geometry2/issues/414))
- Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz

<a id="tf2-msgs"></a>

## [tf2\_msgs](https://github.com/ros2/geometry2/tree/humble/tf2_msgs/CHANGELOG.rst)

- Remove dead file from tf2\_msgs ([#415](https://github.com/ros2/geometry2/issues/415))
- Contributors: Chris Lalancette

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/humble/tf2_py/CHANGELOG.rst)

- Make sure to finalize tf2\_py BufferCore. ([#505](https://github.com/ros2/geometry2/issues/505))
- Make tf2\_py Use FindPython3 ([#494](https://github.com/ros2/geometry2/issues/494))
- Change TF2Error names to be a bit more descriptive. ([#349](https://github.com/ros2/geometry2/issues/349))
- Remove python\_compat.h ([#417](https://github.com/ros2/geometry2/issues/417))
- Contributors: Chris Lalancette, Shane Loretz

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/humble/tf2_ros/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} and use modern CMake ([#493](https://github.com/ros2/geometry2/issues/493))
- use dedicated callback group and executor to isolate timer ([#447](https://github.com/ros2/geometry2/issues/447))
- Adding shared pointer definition to tf2 buffer ([#508](https://github.com/ros2/geometry2/issues/508))
- fix for a basic logic ([#510](https://github.com/ros2/geometry2/issues/510))
- Fix precision loss from using rclcpp::Time::seconds() ([#511](https://github.com/ros2/geometry2/issues/511))
- clear relative callback of Buffer if MessageFilter is destroyed ([#490](https://github.com/ros2/geometry2/issues/490))
- More info in tf2\_echo output ([#468](https://github.com/ros2/geometry2/issues/468))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Fixes for uncrustify 0.72 ([#486](https://github.com/ros2/geometry2/issues/486))
- More Intuitive CLI for Static Transform Publisher ([#392](https://github.com/ros2/geometry2/issues/392))
- Reduce transform listener nodes ([#442](https://github.com/ros2/geometry2/issues/442))
- `tf2_ros`: Fix deprecated subscriber callbacks ([#448](https://github.com/ros2/geometry2/issues/448))
- Fix tf2\_echo does not work with ros-args ([#407](https://github.com/ros2/geometry2/issues/407)) ([#408](https://github.com/ros2/geometry2/issues/408))
- Contributors: Abrar Rahman Protyasha, Chen Lihui, Chris Lalancette, Hunter L. Allen, Jacob Perron, Kenji Brameld, PGotzmann, Shane Loretz, Steve Macenski, Zhenpeng Ge, gezp, simulacrus

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/humble/tf2_ros_py/CHANGELOG.rst)

- Drop PyKDL dependency in tf2\_geometry\_msgs ([#509](https://github.com/ros2/geometry2/issues/509))
- Add in one more destroy call that was missed in testing. ([#504](https://github.com/ros2/geometry2/issues/504))
- Be much more careful about cleanup in the tf2\_ros\_py tests. ([#499](https://github.com/ros2/geometry2/issues/499))
- Use the correct type for BufferClient timeout\_padding. ([#498](https://github.com/ros2/geometry2/issues/498)) It should be a duration, not a float.
- Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481](https://github.com/ros2/geometry2/issues/481))
- Fix buffer\_client.py using default timeout\_padding ([#437](https://github.com/ros2/geometry2/issues/437))
- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403))
- Contributors: Audrow Nash, Carlos Andrés Álvarez Restrepo, Chris Lalancette, Florian Vahl

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/humble/tf2_sensor_msgs/CHANGELOG.rst)

- Disable mem-access warnings on aarch64. ([#506](https://github.com/ros2/geometry2/issues/506))
- Fix cpplint errors ([#497](https://github.com/ros2/geometry2/issues/497))
- Reenable sensor\_msgs test ([#422](https://github.com/ros2/geometry2/issues/422))
- Deprecate tf2\_sensor\_msgs.h ([#416](https://github.com/ros2/geometry2/issues/416))
- Contributors: Bjar Ne, Chris Lalancette, Jacob Perron

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/humble/tf2_tools/CHANGELOG.rst)

- Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481](https://github.com/ros2/geometry2/issues/481))
- Remove unused import ([#465](https://github.com/ros2/geometry2/issues/465))
- Adding date-time to frames filename ([#454](https://github.com/ros2/geometry2/issues/454))
- Use underscores instead of dashes in setup.cfg. ([#403](https://github.com/ros2/geometry2/issues/403))
- Contributors: Audrow Nash, Hannu Henttinen, Nisala Kalupahana

<a id="tlsf"></a>

## [tlsf](https://github.com/ros2/tlsf/tree/humble/tlsf/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#11](https://github.com/ros2/tlsf/issues/11))
- Export a modern CMake target instead of old-style variables ([#10](https://github.com/ros2/tlsf/issues/10))
- Contributors: Shane Loretz

<a id="tlsf-cpp"></a>

## [tlsf\_cpp](https://github.com/ros2/realtime_support/tree/humble/tlsf_cpp/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#114](https://github.com/ros2/realtime_support/issues/114))
- Export modern CMake targets ([#110](https://github.com/ros2/realtime_support/issues/110))
- Remove the use of malloc hooks from the tlsf\_cpp tests. ([#109](https://github.com/ros2/realtime_support/issues/109))
- Contributors: Chris Lalancette, Shane Loretz

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/humble/topic_monitor/CHANGELOG.rst)

- Update maintainers to Audrow Nash and Michael Jeronimo ([#543](https://github.com/ros2/demos/issues/543))
- Small cleanups to the topic monitor. ([#517](https://github.com/ros2/demos/issues/517))
- Fix topic\_monitor for high publication rate ([#461](https://github.com/ros2/demos/issues/461))
- Use is\_alive for threads. ([#510](https://github.com/ros2/demos/issues/510))
- Contributors: Audrow Nash, Chris Lalancette, Elias De Coninck

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/humble/topic_statistics_demo/CHANGELOG.rst)

- Install includes to include/${PROJECT\_NAME} ([#548](https://github.com/ros2/demos/issues/548))
- Additional fixes for documentation in demos. ([#538](https://github.com/ros2/demos/issues/538))
- Fixing deprecated subscriber callback warnings ([#532](https://github.com/ros2/demos/issues/532))
- Contributors: Abrar Rahman Protyasha, Chris Lalancette, Shane Loretz

<a id="tracetools"></a>

## [tracetools](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME}
- Merge branch ‘update-mentions-of-tracetools-test’ into ‘master’ Update applicable mentions of tracetools\_test to test\_tracetools See merge request [ros-tracing/ros2\_tracing!259](https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/259)
- Update applicable mentions of tracetools\_test to test\_tracetools
- Merge branch ‘version-3-1-0’ into ‘master’ Version 3.1.0 See merge request [ros-tracing/ros2\_tracing!256](https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/256)
- Correctly handle calls to TRACEPOINT() macro with no tracepoint args
- Move publisher handle tracepoint argument from rclcpp\_publish to rcl\_publish
- Add support for rmw init/pub, take, and executor instrumentation
- Export target on Windows and export an interface if TRACETOOLS\_DISABLED
- Remove deprecated utility functions
- Contributors: Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_launch/CHANGELOG.rst)

- Disable kernel tracing by default
- Don’t require kernel tracer and detect when it’s not installed
- Add support for preloading pthread and dl instrumentation shared libs
- Remove profile\_fast option and consider LD\_PRELOADing both libs
- Improve event matching for shared lib preloading
- Improve LdPreload action’s lib-finding function and add proper tests
- Fix multiple LdPreload actions not working and add test
- Deprecate ‘context\_names’ param and replace with ‘context\_fields’
- Support per-domain context fields for the Trace action
- Improve LdPreload.get\_shared\_lib\_path() for when a static lib may exist
- Move some tests from tracetools\_launch to test\_tracetools\_launch
- Expose Trace action as frontend action and support substitutions
- Contributors: Christophe Bedard, Ingo Lütkebohle

<a id="tracetools-test"></a>

## [tracetools\_test](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_test/CHANGELOG.rst)

- Allow providing additional actions for TraceTestCase
- Remove default value for ‘package’ kwarg for TraceTestCase
- Move actual tests out of tracetools\_test to new test\_tracetools package
- Add tests for rmw init/pub, take, and executor instrumentation
- Add field type assertion utilities to TraceTestCase
- Fixing deprecated subscriber callback warnings
- Contributors: Abrar Rahman Protyasha, Christophe Bedard

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_trace/CHANGELOG.rst)

- Disable kernel tracing by default
- Don’t require kernel tracer and detect when it’s not installed
- Introduce constants for tracepoint names
- Optimize default tracing session channel config values
- Deprecate ‘context\_names’ param and replace with ‘context\_fields’
- Support per-domain context fields for the Trace action
- Add support for rmw init/pub, take, and executor tracepoints
- Contributors: Christophe Bedard

<a id="trajectory-msgs"></a>

## [trajectory\_msgs](https://github.com/ros2/common_interfaces/tree/humble/trajectory_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Contributors: Audrow Nash, Grey

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/humble-devel/turtlesim/CHANGELOG.rst)

- Use `double` when handling `qreal orient\_` ([#114](https://github.com/ros/ros_tutorials/issues/114))
- Add Rolling Icon ([#133](https://github.com/ros/ros_tutorials/issues/133))
- Update maintainers to Audrow Nash and Michael Jeronimo ([#137](https://github.com/ros/ros_tutorials/issues/137))
- Fixing deprecated subscriber callback warnings ([#134](https://github.com/ros/ros_tutorials/issues/134))
- Use rosidl\_get\_typesupport\_target() ([#132](https://github.com/ros/ros_tutorials/issues/132))
- Print out the correct node name on startup. ([#122](https://github.com/ros/ros_tutorials/issues/122))
- Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Katherine Scott, Seulbae Kim, Shane Loretz

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/humble/urdf/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#31](https://github.com/ros2/urdf/issues/31))
- Add linter tests and fix errors ([#30](https://github.com/ros2/urdf/issues/30))
- Add in a Doxyfile to predefine macros. ([#28](https://github.com/ros2/urdf/issues/28))
- Contributors: Chris Lalancette, Jacob Perron, Shane Loretz

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/humble/urdf_parser_plugin/CHANGELOG.rst)

- Install headers to include/${PROJECT\_NAME} ([#31](https://github.com/ros2/urdf/issues/31))
- Add linter tests and fix errors ([#30](https://github.com/ros2/urdf/issues/30))
- Contributors: Jacob Perron, Shane Loretz

<a id="visualization-msgs"></a>

## [visualization\_msgs](https://github.com/ros2/common_interfaces/tree/humble/visualization_msgs/CHANGELOG.rst)

- Interface packages should fully <depend> on the interface packages that they depend on ([#173](https://github.com/ros2/common_interfaces/issues/173))
- Update maintainers to Geoffrey Biggs and Tully Foote ([#163](https://github.com/ros2/common_interfaces/issues/163))
- Marker Textures ([#153](https://github.com/ros2/common_interfaces/issues/153))
- Document namespace scoped marker deletion. ([#151](https://github.com/ros2/common_interfaces/issues/151))
- Contributors: Audrow Nash, Greg Balke, Grey, Michel Hidalgo

<a id="yaml-cpp-vendor"></a>

## [yaml\_cpp\_vendor](https://github.com/ros2/yaml_cpp_vendor/tree/humble/CHANGELOG.rst)

- Add missing dependency on yaml-cpp ([#32](https://github.com/ros2/yaml_cpp_vendor/issues/32))
- Upgrade to yaml-cpp 0.7.0 ([#25](https://github.com/ros2/yaml_cpp_vendor/issues/25))
- Contributors: Chris Lalancette, Scott K Logan

<a id="zstd-vendor"></a>

## [zstd\_vendor](https://github.com/ros2/rosbag2/tree/humble/zstd_vendor/CHANGELOG.rst)

- Bump version number to avoid conflict
- Use git hash for zstd vendor ([#969](https://github.com/ros2/rosbag2/issues/969))
- Update package maintainers ([#899](https://github.com/ros2/rosbag2/issues/899))
- Declare missing dependency on ‘git’ in zstd\_vendor ([#890](https://github.com/ros2/rosbag2/issues/890))
- Switch to using ‘git apply’ for zstd\_vendor patches ([#846](https://github.com/ros2/rosbag2/issues/846))
- Contributors: Chris Lalancette, Christophe Bedard, Michel Hidalgo, Scott K Logan, Shane Loretz
