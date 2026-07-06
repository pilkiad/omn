---
title: "ROS 2 Lyrical Luth Complete Changelog"
docname: "Releases/Lyrical-Luth-Complete-Changelog"
source: "Releases/Lyrical-Luth-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="ros-2-lyrical-luth-complete-changelog"></a>

# ROS 2 Lyrical Luth Complete Changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

Table of Contents

- [action\_msgs](#action-msgs)
- [action\_tutorials\_cpp](#action-tutorials-cpp)
- [action\_tutorials\_py](#action-tutorials-py)
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
- [ament\_cmake\_export\_targets](#ament-cmake-export-targets)
- [ament\_cmake\_flake8](#ament-cmake-flake8)
- [ament\_cmake\_gen\_version\_h](#ament-cmake-gen-version-h)
- [ament\_cmake\_gmock](#ament-cmake-gmock)
- [ament\_cmake\_gtest](#ament-cmake-gtest)
- [ament\_cmake\_libraries](#ament-cmake-libraries)
- [ament\_cmake\_lint\_cmake](#ament-cmake-lint-cmake)
- [ament\_cmake\_mypy](#ament-cmake-mypy)
- [ament\_cmake\_pclint](#ament-cmake-pclint)
- [ament\_cmake\_pep257](#ament-cmake-pep257)
- [ament\_cmake\_pycodestyle](#ament-cmake-pycodestyle)
- [ament\_cmake\_pyflakes](#ament-cmake-pyflakes)
- [ament\_cmake\_python](#ament-cmake-python)
- [ament\_cmake\_python\_test](#ament-cmake-python-test)
- [ament\_cmake\_ros](#ament-cmake-ros)
- [ament\_cmake\_ros\_core](#ament-cmake-ros-core)
- [ament\_cmake\_target\_dependencies](#ament-cmake-target-dependencies)
- [ament\_cmake\_uncrustify](#ament-cmake-uncrustify)
- [ament\_cmake\_vendor\_package](#ament-cmake-vendor-package)
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
- [camera\_info\_manager\_py](#camera-info-manager-py)
- [class\_loader](#class-loader)
- [common\_interfaces](#common-interfaces)
- [composition](#composition)
- [composition\_interfaces](#composition-interfaces)
- [console\_bridge\_vendor](#console-bridge-vendor)
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
- [foonathan\_memory\_vendor](#foonathan-memory-vendor)
- [geometry2](#geometry2)
- [geometry\_msgs](#geometry-msgs)
- [gmock\_vendor](#gmock-vendor)
- [gtest\_vendor](#gtest-vendor)
- [gz\_cmake\_vendor](#gz-cmake-vendor)
- [gz\_math\_vendor](#gz-math-vendor)
- [gz\_utils\_vendor](#gz-utils-vendor)
- [image\_common](#image-common)
- [image\_tools](#image-tools)
- [image\_transport](#image-transport)
- [image\_transport\_py](#image-transport-py)
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
- [libstatistics\_collector](#libstatistics-collector)
- [libyaml\_vendor](#libyaml-vendor)
- [lifecycle](#lifecycle)
- [lifecycle\_msgs](#lifecycle-msgs)
- [lifecycle\_py](#lifecycle-py)
- [logging\_demo](#logging-demo)
- [lttngpy](#lttngpy)
- [map\_msgs](#map-msgs)
- [mcap\_vendor](#mcap-vendor)
- [message\_filters](#message-filters)
- [mimick\_vendor](#mimick-vendor)
- [nav\_msgs](#nav-msgs)
- [osrf\_testing\_tools\_cpp](#osrf-testing-tools-cpp)
- [pendulum\_control](#pendulum-control)
- [pendulum\_msgs](#pendulum-msgs)
- [performance\_test\_fixture](#performance-test-fixture)
- [pluginlib](#pluginlib)
- [point\_cloud\_transport](#point-cloud-transport)
- [point\_cloud\_transport\_py](#point-cloud-transport-py)
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
- [rcl\_logging\_implementation](#rcl-logging-implementation)
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
- [resource\_retriever\_interfaces](#resource-retriever-interfaces)
- [resource\_retriever\_service](#resource-retriever-service)
- [resource\_retriever\_service\_plugin](#resource-retriever-service-plugin)
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
- [rmw\_test\_fixture](#rmw-test-fixture)
- [rmw\_test\_fixture\_implementation](#rmw-test-fixture-implementation)
- [rmw\_zenoh\_cpp](#rmw-zenoh-cpp)
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
- [ros2plugin](#ros2plugin)
- [ros2run](#ros2run)
- [ros2service](#ros2service)
- [ros2test](#ros2test)
- [ros2topic](#ros2topic)
- [ros2trace](#ros2trace)
- [ros\_environment](#ros-environment)
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
- [rosidl\_buffer](#rosidl-buffer)
- [rosidl\_buffer\_backend](#rosidl-buffer-backend)
- [rosidl\_buffer\_backend\_registry](#rosidl-buffer-backend-registry)
- [rosidl\_buffer\_py](#rosidl-buffer-py)
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
- [rosidl\_generator\_rs](#rosidl-generator-rs)
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
- [spdlog\_vendor](#spdlog-vendor)
- [sros2](#sros2)
- [sros2\_cmake](#sros2-cmake)
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
- [tracetools\_read](#tracetools-read)
- [tracetools\_test](#tracetools-test)
- [tracetools\_trace](#tracetools-trace)
- [trajectory\_msgs](#trajectory-msgs)
- [turtlesim](#turtlesim)
- [turtlesim\_msgs](#turtlesim-msgs)
- [type\_description\_interfaces](#type-description-interfaces)
- [uncrustify\_vendor](#uncrustify-vendor)
- [unique\_identifier\_msgs](#unique-identifier-msgs)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [urdfdom](#urdfdom)
- [urdfdom\_headers](#urdfdom-headers)
- [visualization\_msgs](#visualization-msgs)
- [yaml\_cpp\_vendor](#yaml-cpp-vendor)
- [zenoh\_cpp\_vendor](#zenoh-cpp-vendor)
- [zenoh\_security\_tools](#zenoh-security-tools)

<a id="action-msgs"></a>

## [action\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/action_msgs/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/lyrical/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Update action cpp demos to support setting introspection ([#709](https://github.com/ros2/demos/issues/709)) \* Update action cpp demos to support setting introspection \* Add the missing header file declaration ———
- Contributors: Barry Xu, Emerson Knapp, mosfet80

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/lyrical/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- action\_tutorials\_py: add ament\_mypy support ([#775](https://github.com/ros2/demos//issues/775))
- fix setuptools deprecations ([#733](https://github.com/ros2/demos/issues/733))
- support cancel handler in action\_tutorials\_py action server. ([#727](https://github.com/ros2/demos/issues/727))
- Update action python demos to support setting introspection ([#708](https://github.com/ros2/demos/issues/708)) \* Update action python demos to support setting introspection \* Correct the errors in the document ———
- Contributors: Barry Xu, Tomoya Fujita, mohit, mosfet80

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/lyrical/ament_clang_format/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/lyrical/ament_clang_tidy/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-cmake"></a>

## [ament\_cmake](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake/CHANGELOG.rst)

- Removed deprecated ament\_cmake\_export\_interfaces package ([#581](https://github.com/ament/ament_cmake/issues/581))
- Contributors: Alejandro Hernández Cordero

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_auto/CHANGELOG.rst)

- Do not error on USE\_SCOPED\_HEADER\_INSTALL\_DIR ([#596](https://github.com/ament/ament_cmake/issues/596))
- Contributors: Tim Clephas

<a id="ament-cmake-clang-format"></a>

## [ament\_cmake\_clang\_format](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_clang_format/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Allow overriding clang-format version via CMake ([#536](https://github.com/ament/ament_lint/issues/536))
- Contributors: Nathan Wiebe Neufeldt, mosfet80

<a id="ament-cmake-clang-tidy"></a>

## [ament\_cmake\_clang\_tidy](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_clang_tidy/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-copyright"></a>

## [ament\_cmake\_copyright](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_copyright/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_core/CHANGELOG.rst)

- Remove unused AMENT\_CMAKE\_ENVIRONMENT\_GENERATION option ([#354](https://github.com/ament/ament_cmake/issues/354))
- Address ament\_lint\_cmake regressions ([#604](https://github.com/ament/ament_cmake/issues/604))
- Respect find\_package(QUIET) in chains from ament\_cmake\_core ([#603](https://github.com/ament/ament_cmake/issues/603))
- perf: faster normalize\_path implementation using cmake\_path ([#586](https://github.com/ament/ament_cmake/issues/586))
- Contributors: Nathan Boisard, Scott K Logan, Shane Loretz

<a id="ament-cmake-cppcheck"></a>

## [ament\_cmake\_cppcheck](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_cppcheck/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-cpplint"></a>

## [ament\_cmake\_cpplint](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_cpplint/CHANGELOG.rst)

- Fixing EXCLUDE consistency ([#481](https://github.com/ament/ament_lint/issues/481))
- cpplint: update link to upstream cpplint repo ([#538](https://github.com/ament/ament_lint/issues/538))
- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: Romain Reignier, Tom Moore, mosfet80

<a id="ament-cmake-export-targets"></a>

## [ament\_cmake\_export\_targets](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_export_targets/CHANGELOG.rst)

- Address ament\_lint\_cmake regressions ([#604](https://github.com/ament/ament_cmake/issues/604))
- Contributors: Scott K Logan

<a id="ament-cmake-flake8"></a>

## [ament\_cmake\_flake8](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_flake8/CHANGELOG.rst)

- Fixing EXCLUDE consistency ([#481](https://github.com/ament/ament_lint/issues/481))
- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: Tom Moore, mosfet80

<a id="ament-cmake-gen-version-h"></a>

## [ament\_cmake\_gen\_version\_h](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gen_version_h/CHANGELOG.rst)

- Address ament\_lint\_cmake regressions ([#604](https://github.com/ament/ament_cmake/issues/604))
- Update CMake requirement ([#589](https://github.com/ament/ament_cmake/issues/589))
- Removed deprecated function ament\_cmake\_gen\_version\_h ([#582](https://github.com/ament/ament_cmake/issues/582))
- Contributors: Alejandro Hernández Cordero, Scott K Logan, mosfet80

<a id="ament-cmake-gmock"></a>

## [ament\_cmake\_gmock](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gmock/CHANGELOG.rst)

- Use libgtest-dev and libgmock-dev ([#622](https://github.com/ament/ament_cmake//issues/622))
- Contributors: Shane Loretz

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gtest/CHANGELOG.rst)

- Use libgtest-dev and libgmock-dev ([#622](https://github.com/ament/ament_cmake//issues/622))
- Contributors: Shane Loretz

<a id="ament-cmake-libraries"></a>

## [ament\_cmake\_libraries](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_libraries/CHANGELOG.rst)

- Address ament\_lint\_cmake regressions ([#604](https://github.com/ament/ament_cmake/issues/604))
- Contributors: Scott K Logan

<a id="ament-cmake-lint-cmake"></a>

## [ament\_cmake\_lint\_cmake](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_lint_cmake/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-mypy"></a>

## [ament\_cmake\_mypy](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_mypy/CHANGELOG.rst)

- [ament\_mypy] Add `--ament-strict` flag for more strict type checking. ([#573](https://github.com/ament/ament_lint/issues/573))
- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: Michael Carlstrom, mosfet80

<a id="ament-cmake-pclint"></a>

## [ament\_cmake\_pclint](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pclint/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-pep257"></a>

## [ament\_cmake\_pep257](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pep257/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-pycodestyle"></a>

## [ament\_cmake\_pycodestyle](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pycodestyle/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-pyflakes"></a>

## [ament\_cmake\_pyflakes](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pyflakes/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-cmake-python"></a>

## [ament\_cmake\_python](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_python/CHANGELOG.rst)

- feature: allow extending a python package in `ament_python_install_package` ([#587](https://github.com/ament/ament_cmake//issues/587))
- Add missing dependency ([#617](https://github.com/ament/ament_cmake/issues/617))
- Contributors: Nadav Elkabets, Robert Haschke

<a id="ament-cmake-python-test"></a>

## [ament\_cmake\_python\_test](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_python_test/CHANGELOG.rst)

- feature: allow extending a python package in `ament_python_install_package` ([#587](https://github.com/ament/ament_cmake//issues/587))
- Contributors: Nadav Elkabets

<a id="ament-cmake-ros"></a>

## [ament\_cmake\_ros](https://github.com/ros2/ament_cmake_ros/tree/lyrical/ament_cmake_ros/CHANGELOG.rst)

- fix cmake deprecation ([#47](https://github.com/ros2/ament_cmake_ros/issues/47))
- Contributors: mosfet80

<a id="ament-cmake-ros-core"></a>

## [ament\_cmake\_ros\_core](https://github.com/ros2/ament_cmake_ros/tree/lyrical/ament_cmake_ros_core/CHANGELOG.rst)

- Add `ament_ros_defaults` target ([#62](https://github.com/ros2/ament_cmake_ros/issues/62))
- fix cmake deprecation ([#47](https://github.com/ros2/ament_cmake_ros/issues/47))
- Contributors: Michael Carlstrom, mosfet80

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_target_dependencies/CHANGELOG.rst)

- Revert “Revert “Removed deprecated function ament\_cmake\_target\_dependencies (…” ([#614](https://github.com/ament/ament_cmake/issues/614))
- Revert “Removed deprecated function ament\_cmake\_target\_dependencies” ([#585](https://github.com/ament/ament_cmake/issues/585))
- Removed deprecated function ament\_cmake\_target\_dependencies ([#583](https://github.com/ament/ament_cmake/issues/583))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="ament-cmake-uncrustify"></a>

## [ament\_cmake\_uncrustify](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_uncrustify/CHANGELOG.rst)

- [ament\_cmake\_uncrustify] Add ament\_cmake\_uncrustify\_LANGUAGE variable ([#384](https://github.com/ament/ament_lint/issues/384))
- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: Abrar Rahman Protyasha, mosfet80

<a id="ament-cmake-vendor-package"></a>

## [ament\_cmake\_vendor\_package](https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_vendor_package/CHANGELOG.rst)

- ament\_vendor: Propagate additional variables to ExternalProject ([#593](https://github.com/ament/ament_cmake/issues/593))
- Contributors: Silvio Traversaro

<a id="ament-cmake-xmllint"></a>

## [ament\_cmake\_xmllint](https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_xmllint/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/lyrical/ament_copyright/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Remove `importlib_metadata` ([#564](https://github.com/ament/ament_lint/issues/564))
- Remove invalid license template. ([#209](https://github.com/ament/ament_lint/issues/209))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, Tully Foote, mosfet80

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/lyrical/ament_cppcheck/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/lyrical/ament_cpplint/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- cpplint: update link to upstream cpplint repo ([#538](https://github.com/ament/ament_lint/issues/538))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, Romain Reignier, mosfet80

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/lyrical/ament_flake8/CHANGELOG.rst)

- [ament\_mypy] Add `--ament-strict` flag for more strict type checking. ([#573](https://github.com/ament/ament_lint/issues/573))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Drop dependency on python3-flake8-docstrings ([#513](https://github.com/ament/ament_lint/issues/513))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan, mosfet80

<a id="ament-index-cpp"></a>

## [ament\_index\_cpp](https://github.com/ament/ament_index/tree/lyrical/ament_index_cpp/CHANGELOG.rst)

- Cleanups ([#114](https://github.com/ament/ament_index/issues/114))
- Use get\_package\_share\_path just as python ([#112](https://github.com/ament/ament_index//issues/112))
- Add autogenerated version header ([#105](https://github.com/ament/ament_index/issues/105))
- Extend API to use std::filesystem ([#104](https://github.com/ament/ament_index/issues/104))
- Fix CMake deprecation ([#102](https://github.com/ament/ament_index/issues/102))
- Contributors: Alejandro Hernández Cordero, Eric Lujan, Tim Clephas, mosfet80

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/lyrical/ament_index_python/CHANGELOG.rst)

- Cleanups ament\_index\_python ([#115](https://github.com/ament/ament_index/issues/115))
- fix setuptools deprecations ([#101](https://github.com/ament/ament_index/issues/101))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="ament-lint"></a>

## [ament\_lint](https://github.com/ament/ament_lint/tree/lyrical/ament_lint/CHANGELOG.rst)

- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/lyrical/ament_lint_auto/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/lyrical/ament_lint_cmake/CHANGELOG.rst)

- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-lint-common"></a>

## [ament\_lint\_common](https://github.com/ament/ament_lint/tree/lyrical/ament_lint_common/CHANGELOG.rst)

- Fix cmake deprecation ([#539](https://github.com/ament/ament_lint/issues/539))
- Contributors: mosfet80

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/lyrical/ament_mypy/CHANGELOG.rst)

- Allow unused ignores ([#575](https://github.com/ament/ament_lint/issues/575))
- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- [ament\_mypy] Add `--ament-strict` flag for more strict type checking. ([#573](https://github.com/ament/ament_lint/issues/573))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/lyrical/CHANGELOG.rst)

- feat: add support for fish ([#164](https://github.com/ament/ament_package/issues/164))
- Fix flake8 ([#163](https://github.com/ament/ament_package/issues/163))
- Remove unneeded deps ([#161](https://github.com/ament/ament_package/issues/161))
- fix setuptools deprecations ([#156](https://github.com/ament/ament_package/issues/156))
- Contributors: Michael Carlstrom, SPeak, mosfet80

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/lyrical/ament_pclint/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- clean setup.py ([#552](https://github.com/ament/ament_lint/issues/552))
- fix setuptools deprecation ([#551](https://github.com/ament/ament_lint/issues/551))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-pep257"></a>

## [ament\_pep257](https://github.com/ament/ament_lint/tree/lyrical/ament_pep257/CHANGELOG.rst)

- Skip pydocstyle tests if it can’t be imported ([#579](https://github.com/ament/ament_lint/issues/579))
- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan, mosfet80

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/lyrical/ament_pycodestyle/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/lyrical/ament_pyflakes/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/lyrical/ament_uncrustify/CHANGELOG.rst)

- [ament\_mypy] Fix config for ament\_cmake packages and type entrypoints ([#574](https://github.com/ament/ament_lint/issues/574))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Revert “Removed uncrustify\_vendor ([#556](https://github.com/ament/ament_lint/issues/556))” ([#561](https://github.com/ament/ament_lint/issues/561))
- Removed uncrustify\_vendor ([#556](https://github.com/ament/ament_lint/issues/556))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Alejandro Hernández Cordero, Jochen Sprickerhof, Michael Carlstrom, Michael Orlov, mosfet80

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/lyrical/ament_xmllint/CHANGELOG.rst)

- [ament\_mypy] Add `--ament-strict` flag for more strict type checking. ([#573](https://github.com/ament/ament_lint/issues/573))
- xmllint: fetch external schemas via Python ([#570](https://github.com/ament/ament_lint/issues/570))
- Drop setuptools from install\_requires ([#566](https://github.com/ament/ament_lint/issues/566))
- Export typing information for ament linters ([#553](https://github.com/ament/ament_lint/issues/553))
- fix setuptools deprecations ([#547](https://github.com/ament/ament_lint/issues/547))
- Contributors: Jochen Sprickerhof, Michael Carlstrom, Michael Carroll, mosfet80

<a id="builtin-interfaces"></a>

## [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/lyrical/builtin_interfaces/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Add info to duration message and time message comments ([#176](https://github.com/ros2/rcl_interfaces/issues/176))
- Contributors: Jimmy McElwain, mosfet80

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/lyrical/camera_calibration_parsers/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#396](https://github.com/ros-perception/image_common/issues/396))
- Delete camera\_calibration\_parsers/setup.py ([#393](https://github.com/ros-perception/image_common/issues/393))
- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Fix cmake deprecation ([#367](https://github.com/ros-perception/image_common/issues/367))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#345](https://github.com/ros-perception/image_common/issues/345))
- Contributors: Emerson Knapp, Garrett Brown, Michael Carlstrom, Shane Loretz, mosfet80

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/lyrical/camera_info_manager/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#396](https://github.com/ros-perception/image_common/issues/396))
- Added camera info manager unit test ([#358](https://github.com/ros-perception/image_common/issues/358))
- Use get\_package\_share\_path ([#391](https://github.com/ros-perception/image_common/issues/391))
- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Updated deprecated ament\_index\_cpp API ([#388](https://github.com/ros-perception/image_common/issues/388))
- Fix compilation error with clang ([#372](https://github.com/ros-perception/image_common/issues/372))
- Support lifecycle node - NodeInterfaces ([#352](https://github.com/ros-perception/image_common/issues/352))
- Deprecated rmw\_qos\_profile\_t in favour of rclcpp::QoS ([#364](https://github.com/ros-perception/image_common/issues/364))
- Fix cmake deprecation ([#367](https://github.com/ros-perception/image_common/issues/367))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett Brown, mosfet80

<a id="camera-info-manager-py"></a>

## [camera\_info\_manager\_py](https://github.com/ros-perception/image_common/tree/lyrical/camera_info_manager_py/CHANGELOG.rst)

- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Cleanup mislabeled BSD license ([#382](https://github.com/ros-perception/image_common/issues/382))
- fix setuptools deprecation ([#366](https://github.com/ros-perception/image_common/issues/366))
- Fix CameraInfo distortion coefficients and logger ([#360](https://github.com/ros-perception/image_common/issues/360))
- Contributors: Alejandro Hernández Cordero, Garrett Brown, Rick-v-E, mosfet80

<a id="class-loader"></a>

## [class\_loader](https://github.com/ros/class_loader/tree/lyrical/CHANGELOG.rst)

- Fix compiler error with clang ([#227](https://github.com/ros/class_loader/issues/227))
- Remove ament\_cmake\_ros dependency ([#226](https://github.com/ros/class_loader/issues/226)) The dependent ament\_cmake\_ros package transitively pulls in RMW-layer packages which is unnecessarily heavy to class\_loader that is supposed to be an independent plugin loading library. This commit removes the ament\_cmake\_ros dependency and replaces with a plain ament\_cmake with an explicit SHARED library type to keep the dependency minimal.
- Improvements ([#225](https://github.com/ros/class_loader/issues/225))
- Clean up tests ([#224](https://github.com/ros/class_loader/issues/224))
- Add support for passing arguments to constructors ([#223](https://github.com/ros/class_loader//issues/223))
- Thread and Address Sanitizer CI ([#198](https://github.com/ros/class_loader/issues/198))
- Update cmake requirement
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#215](https://github.com/ros/class_loader/issues/215))
- Contributors: Alejandro Hernández Cordero, CY Chen, Tyler Weaver, mosfet80, pum1k

<a id="common-interfaces"></a>

## [common\_interfaces](https://github.com/ros2/common_interfaces/tree/lyrical/common_interfaces/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Removed deprecated actionlib\_msgs ([#280](https://github.com/ros2/common_interfaces/issues/280))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/lyrical/composition/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Add tests isolation in test\_dlopen\_composition.py.in and test\_linktime\_composition.py.in ([#764](https://github.com/ros2/demos//issues/764))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Log message for linktime composition on Windows ([#640](https://github.com/ros2/demos/issues/640))
- correct name of shared libraries and their location ([#722](https://github.com/ros2/demos/issues/722)) ([#726](https://github.com/ros2/demos/issues/726))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien Enoch, Lucas Wendland, Scott K Logan, Shane Loretz, mergify[bot], mosfet80, yadunund

<a id="composition-interfaces"></a>

## [composition\_interfaces](https://github.com/ros2/rcl_interfaces/tree/lyrical/composition_interfaces/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="console-bridge-vendor"></a>

## [console\_bridge\_vendor](https://github.com/ros2/console_bridge_vendor/tree/lyrical/CHANGELOG.rst)

- Update CMake version here and console\_bridge ([#44](https://github.com/ros2/console_bridge_vendor/issues/44))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#42](https://github.com/ros2/console_bridge_vendor/issues/42))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/lyrical/demo_nodes_cpp/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- add child logger under parent node, with different log levels. ([#772](https://github.com/ros2/demos//issues/772))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Update subscription callback signatures ([#754](https://github.com/ros2/demos/issues/754))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- fix typo in docs demo\_nodes\_cpp ([#715](https://github.com/ros2/demos/issues/715))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Khaled Gabr, Lucas Wendland, Scott K Logan, Tomoya Fujita, mini-1235, mosfet80

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/lyrical/demo_nodes_cpp_native/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Removed outdated TODO ([#723](https://github.com/ros2/demos/issues/723))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Shane Loretz, mosfet80

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/lyrical/demo_nodes_py/CHANGELOG.rst)

- add child logger under parent node, with different log levels. ([#772](https://github.com/ros2/demos//issues/772))
- Fix deprecated RcutilsLogger::warn() usage in LoggerServiceNode ([#773](https://github.com/ros2/demos//issues/773))
- Ignore A005 ([#771](https://github.com/ros2/demos//issues/771))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- fix setuptools deprecations ([#733](https://github.com/ros2/demos/issues/733))
- Revert “Revert “fix loading parameter behavior from yaml file. ([#656](https://github.com/ros2/demos/issues/656))” ([#660](https://github.com/ros2/demos/issues/660))” ([#661](https://github.com/ros2/demos/issues/661))
- Contributors: Barry Xu, Lucas Wendland, Michael Carlstrom, Tomoya Fujita, mosfet80

<a id="diagnostic-msgs"></a>

## [diagnostic\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/diagnostic_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="domain-coordinator"></a>

## [domain\_coordinator](https://github.com/ros2/ament_cmake_ros/tree/lyrical/domain_coordinator/CHANGELOG.rst)

- fix setuptools deprecations ([#49](https://github.com/ros2/ament_cmake_ros/issues/49))
- Contributors: mosfet80

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- get rid of deprecated rclcpp::spin\_some(). ([#734](https://github.com/ros2/demos/issues/734))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- Fixed launch file ([#759](https://github.com/ros2/demos/issues/759))
- Added README.md for dummy\_robot\_bringup. ([#574](https://github.com/ros2/demos/issues/574))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Contributors: Alejandro Hernández Cordero, Gary Bey, mosfet80

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- get rid of deprecated rclcpp::spin\_some(). ([#734](https://github.com/ros2/demos/issues/734))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

<a id="eigen3-cmake-module"></a>

## [eigen3\_cmake\_module](https://github.com/ros2/eigen3_cmake_module/tree/lyrical/CHANGELOG.rst)

- fix cmake deprecation ([#10](https://github.com/ros2/eigen3_cmake_module/issues/10))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#8](https://github.com/ros2/eigen3_cmake_module/issues/8))
- Contributors: Chris Lalancette, mosfet80

<a id="example-interfaces"></a>

## [example\_interfaces](https://github.com/ros2/example_interfaces/tree/lyrical/CHANGELOG.rst)

- fix cmake deprecation ([#23](https://github.com/ros2/example_interfaces/issues/23))
- Remove .github/ISSUE\_TEMPLATE.md (old version of templates) ([#21](https://github.com/ros2/example_interfaces/issues/21))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#19](https://github.com/ros2/example_interfaces/issues/19))
- Contributors: Chris Lalancette, Tomoya Fujita, mosfet80

<a id="examples-rclcpp-async-client"></a>

## [examples\_rclcpp\_async\_client](https://github.com/ros2/examples/tree/lyrical/rclcpp/services/async_client/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-cbg-executor"></a>

## [examples\_rclcpp\_cbg\_executor](https://github.com/ros2/examples/tree/lyrical/rclcpp/executors/cbg_executor/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-minimal-action-client"></a>

## [examples\_rclcpp\_minimal\_action\_client](https://github.com/ros2/examples/tree/lyrical/rclcpp/actions/minimal_action_client/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- get rid of deprecated rclcpp::spin\_some(). ([#422](https://github.com/ros2/examples//issues/422))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80

<a id="examples-rclcpp-minimal-action-server"></a>

## [examples\_rclcpp\_minimal\_action\_server](https://github.com/ros2/examples/tree/lyrical/rclcpp/actions/minimal_action_server/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Add rclcpp single goal action server example ([#429](https://github.com/ros2/examples/issues/429))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, Taiga Arai, mosfet80

<a id="examples-rclcpp-minimal-client"></a>

## [examples\_rclcpp\_minimal\_client](https://github.com/ros2/examples/tree/lyrical/rclcpp/services/minimal_client/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-minimal-composition"></a>

## [examples\_rclcpp\_minimal\_composition](https://github.com/ros2/examples/tree/lyrical/rclcpp/composition/minimal_composition/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-minimal-publisher"></a>

## [examples\_rclcpp\_minimal\_publisher](https://github.com/ros2/examples/tree/lyrical/rclcpp/topics/minimal_publisher/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Improve minimal\_publisher README with clearer structure and usage guidance ([#434](https://github.com/ros2/examples/issues/434))
- get rid of deprecated rclcpp::spin\_some(). ([#422](https://github.com/ros2/examples//issues/422))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- wait 5 secs until all subscriptions acknowledge the messages. ([#414](https://github.com/ros2/examples/issues/414))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, Yadnyeshwar Amol Sakhare, mosfet80

<a id="examples-rclcpp-minimal-service"></a>

## [examples\_rclcpp\_minimal\_service](https://github.com/ros2/examples/tree/lyrical/rclcpp/services/minimal_service/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/lyrical/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclcpp-minimal-timer"></a>

## [examples\_rclcpp\_minimal\_timer](https://github.com/ros2/examples/tree/lyrical/rclcpp/timers/minimal_timer/CHANGELOG.rst)

- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz, mosfet80

<a id="examples-rclcpp-multithreaded-executor"></a>

## [examples\_rclcpp\_multithreaded\_executor](https://github.com/ros2/examples/tree/lyrical/rclcpp/executors/multithreaded_executor/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Improve readibility of reported thread ids in the multithreaded executor example ([#415](https://github.com/ros2/examples/issues/415))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, José Faria, Shane Loretz, mosfet80

<a id="examples-rclcpp-wait-set"></a>

## [examples\_rclcpp\_wait\_set](https://github.com/ros2/examples/tree/lyrical/rclcpp/wait_set/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#444](https://github.com/ros2/examples/issues/444))
- Fix CMAKE deprecation ([#419](https://github.com/ros2/examples/issues/419))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Emerson Knapp, Shane Loretz, mosfet80

<a id="examples-rclpy-executors"></a>

## [examples\_rclpy\_executors](https://github.com/ros2/examples/tree/lyrical/rclpy/executors/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: mosfet80

<a id="examples-rclpy-guard-conditions"></a>

## [examples\_rclpy\_guard\_conditions](https://github.com/ros2/examples/tree/lyrical/rclpy/guard_conditions/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: mosfet80

<a id="examples-rclpy-minimal-action-client"></a>

## [examples\_rclpy\_minimal\_action\_client](https://github.com/ros2/examples/tree/lyrical/rclpy/actions/minimal_action_client/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: mosfet80

<a id="examples-rclpy-minimal-action-server"></a>

## [examples\_rclpy\_minimal\_action\_server](https://github.com/ros2/examples/tree/lyrical/rclpy/actions/minimal_action_server/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: mosfet80

<a id="examples-rclpy-minimal-client"></a>

## [examples\_rclpy\_minimal\_client](https://github.com/ros2/examples/tree/lyrical/rclpy/services/minimal_client/CHANGELOG.rst)

- flake8 fixes ([#445](https://github.com/ros2/examples/issues/445))
- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: Michael Carlstrom, mosfet80

<a id="examples-rclpy-minimal-publisher"></a>

## [examples\_rclpy\_minimal\_publisher](https://github.com/ros2/examples/tree/lyrical/rclpy/topics/minimal_publisher/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Address flake8 errors for examples\_rclpy\_minimal\_publisher ([#410](https://github.com/ros2/examples/issues/410))
- Add publisher\_member\_function\_with\_wait\_for\_all\_acked.py ([#407](https://github.com/ros2/examples/issues/407))
- Contributors: Tomoya Fujita, mosfet80

<a id="examples-rclpy-minimal-service"></a>

## [examples\_rclpy\_minimal\_service](https://github.com/ros2/examples/tree/lyrical/rclpy/services/minimal_service/CHANGELOG.rst)

- flake8 fixes ([#445](https://github.com/ros2/examples/issues/445))
- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: Michael Carlstrom, mosfet80

<a id="examples-rclpy-minimal-subscriber"></a>

## [examples\_rclpy\_minimal\_subscriber](https://github.com/ros2/examples/tree/lyrical/rclpy/topics/minimal_subscriber/CHANGELOG.rst)

- flake8 fixes ([#445](https://github.com/ros2/examples/issues/445))
- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: Michael Carlstrom, mosfet80

<a id="examples-rclpy-pointcloud-publisher"></a>

## [examples\_rclpy\_pointcloud\_publisher](https://github.com/ros2/examples/tree/lyrical/rclpy/topics/pointcloud_publisher/CHANGELOG.rst)

- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: mosfet80

<a id="examples-tf2-py"></a>

## [examples\_tf2\_py](https://github.com/ros2/geometry2/tree/lyrical/examples_tf2_py/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Fix Setuptools deprecations ([#809](https://github.com/ros2/geometry2/issues/809))
- Contributors: Auguste Lalande, R Kent James, mosfet80

<a id="foonathan-memory-vendor"></a>

## [foonathan\_memory\_vendor](https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst)

- Change upstream to fix build with clang (#80)
- Change upstream to eProsima fork to avoid patch command (#80)
- Update upstream to release 0.7-4 (#75)
- Remove installer CMake patches (#75)
- Improve mechanism to find an installation of foonathan\_memory (#67)
- Fix ament\_lint\_cmake errors (#68)
- Add FORCE\_BUILD option to cmake (#69)
- Shorten new option description (#70)

<a id="geometry2"></a>

## [geometry2](https://github.com/ros2/geometry2/tree/lyrical/geometry2/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: mosfet80

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/geometry_msgs/CHANGELOG.rst)

- Clarify `Inertia.msg` expresses inertia about the center of mass ([#313](https://github.com/ros2/common_interfaces/issues/313))
- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Removed deprecated geometry\_msgs/Pose2d ([#283](https://github.com/ros2/common_interfaces/issues/283))
- Contributors: Alejandro Hernández Cordero, Andrew Symington, mosfet80

<a id="gmock-vendor"></a>

## [gmock\_vendor](https://github.com/ament/googletest/tree/lyrical/googlemock/CHANGELOG.rst)

- Deprecate gtest\_vendor and gmock\_vendor ([#41](https://github.com/ament/googletest/issues/41))
- Contributors: Shane Loretz

<a id="gtest-vendor"></a>

## [gtest\_vendor](https://github.com/ament/googletest/tree/lyrical/googletest/CHANGELOG.rst)

- Deprecate gtest\_vendor and gmock\_vendor ([#41](https://github.com/ament/googletest/issues/41))
- Contributors: Shane Loretz

<a id="gz-cmake-vendor"></a>

## [gz\_cmake\_vendor](https://github.com/gazebo-release/gz_cmake_vendor/tree/lyrical/CHANGELOG.rst)

- Bump version to 5.1.0 ([#24](https://github.com/gazebo-release/gz_cmake_vendor/issues/24))
- Merge pull request [#23](https://github.com/gazebo-release/gz_cmake_vendor/issues/23) Bump version to 5.0.2 ———
- Bump version to 5.0.1 ([#20](https://github.com/gazebo-release/gz_cmake_vendor/issues/20))
- Bump version to 5.0.0 ([#19](https://github.com/gazebo-release/gz_cmake_vendor/issues/19))
- Jetty support: bump to 5.0.0, fix package names ([#16](https://github.com/gazebo-release/gz_cmake_vendor/issues/16)) \* Jetty support: bump to 5.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. \* Add option VENDOR\_FROM\_LIB\_VCS\_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB\_VCS\_REF variable. If LIB\_VCS\_REF is unspecified, vendoring will use main. \* remove unused cmake config template \* use lowercase to fix linter complaint \* 5.0.0~pre1 ———
- Bump version to 4.2.0 ([#15](https://github.com/gazebo-release/gz_cmake_vendor/issues/15))
- Contributors: Addisu Z. Taddese, Jose Luis Rivero, Steve Peters

<a id="gz-math-vendor"></a>

## [gz\_math\_vendor](https://github.com/gazebo-release/gz_math_vendor/tree/lyrical/CHANGELOG.rst)

- Bump version to 9.1.0 ([#20](https://github.com/gazebo-release/gz_math_vendor/issues/20))
- Bump version to 9.0.0 ([#17](https://github.com/gazebo-release/gz_math_vendor/issues/17))
- Set PYTHONPATH for Jetty packages ([#14](https://github.com/gazebo-release/gz_math_vendor/issues/14)) \* Set PYTHONPATH for unversioned packages \* Bump to 9.0.0-pre2 \* Set PYTHONPATH in separate dsv file ———
- Bump to 9.0.0-pre2 ([#16](https://github.com/gazebo-release/gz_math_vendor/issues/16))
- Jetty support: bump to 9.0.0, fix package names ([#12](https://github.com/gazebo-release/gz_math_vendor/issues/12)) \* Jetty support: bump to 9.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. \* Add option VENDOR\_FROM\_LIB\_VCS\_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB\_VCS\_REF variable. If LIB\_VCS\_REF is unspecified, vendoring will use main. \* remove unused cmake config file \* use lowercase to fix linter complaint \* build python bindings \* 9.0.0~pre1 ———
- Bump version to 8.2.0 ([#11](https://github.com/gazebo-release/gz_math_vendor/issues/11))
- Contributors: Addisu Z. Taddese, Ian Chen, Jose Luis Rivero, Steve Peters

<a id="gz-utils-vendor"></a>

## [gz\_utils\_vendor](https://github.com/gazebo-release/gz_utils_vendor/tree/lyrical/CHANGELOG.rst)

- Bump version to 4.0.0 ([#12](https://github.com/gazebo-release/gz_utils_vendor/issues/12))
- Add dsv for PYTHONPATH for Jetty packages ([#13](https://github.com/gazebo-release/gz_utils_vendor/issues/13))
- Jetty support: bump to 4.0.0, fix package names ([#11](https://github.com/gazebo-release/gz_utils_vendor/issues/11)) \* Jetty support: bump to 4.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. \* Add option VENDOR\_FROM\_LIB\_VCS\_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB\_VCS\_REF variable. If LIB\_VCS\_REF is unspecified, vendoring will use main. \* remove unused cmake config file \* use lowercase to fix linter complaint \* Add dependency on cli11 \* 4.0.0~pre1 \* Use vendored version of CLI11 ——— Co-authored-by: Addisu Z. Taddese <[addisu@openrobotics.org](mailto:addisu%40openrobotics.org)>
- Contributors: Addisu Z. Taddese, Steve Peters

<a id="image-common"></a>

## [image\_common](https://github.com/ros-perception/image_common/tree/lyrical/image_common/CHANGELOG.rst)

- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Fix cmake deprecation ([#367](https://github.com/ros-perception/image_common/issues/367))
- Contributors: Garrett Brown, mosfet80

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/lyrical/image_tools/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Don’t use `libopencv-dev` for exec ([#760](https://github.com/ros2/demos//issues/760))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Lint image\_tools/CMakeLists.txt ([#712](https://github.com/ros2/demos/issues/712))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Michael Carlstrom, Scott K Logan, mosfet80, yadunund

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/lyrical/image_transport/CHANGELOG.rst)

- Removed clang warning ([#399](https://github.com/ros-perception/image_common/issues/399))
- Include message type ([#394](https://github.com/ros-perception/image_common/issues/394))
- Use new ROSIDL aggregate CMake target ([#396](https://github.com/ros-perception/image_common/issues/396))
- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- properly shut down rclcpp after all tests complete. ([#384](https://github.com/ros-perception/image_common/issues/384))
- Fix QoS override tests ([#376](https://github.com/ros-perception/image_common/issues/376))
- Fix rclcpp\_lifecycle dependency ([#373](https://github.com/ros-perception/image_common/issues/373))
- Fix compilation error with clang ([#372](https://github.com/ros-perception/image_common/issues/372))
- Support lifecycle node - NodeInterfaces ([#352](https://github.com/ros-perception/image_common/issues/352))
- Fixed clang build ([#371](https://github.com/ros-perception/image_common/issues/371))
- fixed build ([#369](https://github.com/ros-perception/image_common/issues/369))
- Deprecated rmw\_qos\_profile\_t in favour of rclcpp::QoS ([#364](https://github.com/ros-perception/image_common/issues/364))
- Removed deprecated code ([#356](https://github.com/ros-perception/image_common/issues/356))
- Fix cmake deprecation ([#367](https://github.com/ros-perception/image_common/issues/367))
- Fix topic resolution for plugins ([#365](https://github.com/ros-perception/image_common/issues/365))
- Remove windows warnings ([#350](https://github.com/ros-perception/image_common/issues/350))
- Add `rclcpp::shutdown` ([#347](https://github.com/ros-perception/image_common/issues/347))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#345](https://github.com/ros-perception/image_common/issues/345))
- Contributors: Alejandro Hernández Cordero, Alex Tyshka, Emerson Knapp, Garrett Brown, Shane Loretz, Tomoya Fujita, Yuyuan Yuan, mosfet80

<a id="image-transport-py"></a>

## [image\_transport\_py](https://github.com/ros-perception/image_common/tree/lyrical/image_transport_py/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#396](https://github.com/ros-perception/image_common/issues/396))
- Update BSD licenses to SPDX identifier ([#389](https://github.com/ros-perception/image_common/issues/389)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Use pybind11 from deb or pixi ([#374](https://github.com/ros-perception/image_common/issues/374))
- Support lifecycle node - NodeInterfaces ([#352](https://github.com/ros-perception/image_common/issues/352))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett Brown

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/lyrical/CHANGELOG.rst)

- fix: Fix compilation on MSVC 2022 ([#120](https://github.com/ros-visualization/interactive_markers/issues/120))
- Use new ROSIDL aggregate CMake target ([#119](https://github.com/ros-visualization/interactive_markers/issues/119))
- Cleanup mislabeled BSD license ([#118](https://github.com/ros-visualization/interactive_markers/issues/118))
- Explicit Time comparissons ([#105](https://github.com/ros-visualization/interactive_markers/issues/105))
- fix cmake deprecation ([#113](https://github.com/ros-visualization/interactive_markers/issues/113))
- Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson Knapp, Janosch Machowinski, mosfet80

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/lyrical/intra_process_demo/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Don’t use `libopencv-dev` for exec ([#760](https://github.com/ros2/demos//issues/760))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- fixup image\_pipeline\_demo ([#755](https://github.com/ros2/demos/issues/755))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Michael Carlstrom, Scott K Logan, William Woodall, mosfet80

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/lyrical/CHANGELOG.rst)

- Removed kdl vendor dependency ([#90](https://github.com/ros/kdl_parser//issues/90))
- Cmake requirement ([#88](https://github.com/ros/kdl_parser/issues/88))
- Remove kdl\_parser\_py. ([#89](https://github.com/ros/kdl_parser/issues/89))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, mosfet80

<a id="keyboard-handler"></a>

## [keyboard\_handler](https://github.com/ros-tooling/keyboard_handler/tree/lyrical/keyboard_handler/CHANGELOG.rst)

- fix cmake deprecation ([#55](https://github.com/ros-tooling/keyboard_handler/issues/55))
- Contributors: mosfet80

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/lyrical/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#115](https://github.com/ros-perception/laser_geometry/issues/115))
- Use seconds in sensor\_msgs::msg::LaserScan msg inside the test ([#107](https://github.com/ros-perception/laser_geometry/issues/107))
- Use constructor of rclcpp::Time instead of conversion. ([#91](https://github.com/ros-perception/laser_geometry/issues/91))
- fix cmake deprecation ([#105](https://github.com/ros-perception/laser_geometry/issues/105))
- Remove hard-coded eigen3 header path for linux hosts ([#95](https://github.com/ros-perception/laser_geometry/issues/95)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson Knapp, Lukas Schäper, mosfet80

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/lyrical/launch/CHANGELOG.rst)

- Correct typos ([#961](https://github.com/ros2/launch/issues/961))
- hotfix ([#950](https://github.com/ros2/launch/issues/950))
- Declare Boolean Launch Argument ([#944](https://github.com/ros2/launch/issues/944))
- Support frontends for PathJoinSubstitution ([#943](https://github.com/ros2/launch/issues/943))
- test python substitution with submodules ([#688](https://github.com/ros2/launch/issues/688))
- Scope launch file dir/path locals to included launch file ([#862](https://github.com/ros2/launch/issues/862))
- Capture the environment variables in TimerAction ([#728](https://github.com/ros2/launch/issues/728))
- Remove importlib metadata ([#932](https://github.com/ros2/launch/issues/932))
- Fix intersphinx\_mapping format ([#921](https://github.com/ros2/launch/issues/921))
- Make the directory-finding substitutions into a PathSubstitution for / operator ([#914](https://github.com/ros2/launch//issues/914))
- Expose StringJoinSubstitution to frontend ([#857](https://github.com/ros2/launch//issues/857))
- Shared logic for substitutions ([#769](https://github.com/ros2/launch/issues/769))
- Use yaml types ([#781](https://github.com/ros2/launch/issues/781))
- Switch osrf\_pycommon dependency to system package ([#817](https://github.com/ros2/launch/issues/817))
- Fix all/any in xml and yaml launch files ([#906](https://github.com/ros2/launch/issues/906))
- Allow providing launch args to include using let in frontends ([#848](https://github.com/ros2/launch//issues/848))
- Fix Setuptoolsdeprecations ([#898](https://github.com/ros2/launch/issues/898))
- Remove LaunchDescriptionArgument ([#891](https://github.com/ros2/launch/issues/891))
- Make sure to install py.typed files ([#886](https://github.com/ros2/launch/issues/886))
- use custom log\_file name as per the user setting ([#861](https://github.com/ros2/launch/issues/861))
- Using `TimerAction` with `SetParameter` from launch\_ros causes crash ([#879](https://github.com/ros2/launch/issues/879))
- Fix `log\_*` warnings ([#883](https://github.com/ros2/launch/issues/883))
- Updated `launch` typings ([#831](https://github.com/ros2/launch/issues/831))
- Allow Path in substitutions, instead of requiring cast to str ([#873](https://github.com/ros2/launch/issues/873))
- Add a `/` path join operator for `PathJoinSubstitution` ([#868](https://github.com/ros2/launch/issues/868))
- Other Logging Implementations with `getLevelNamesMapping` fix ([#866](https://github.com/ros2/launch/issues/866))
- Revert “Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))” ([#865](https://github.com/ros2/launch/issues/865)) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
- Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))
- Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, David V. Lu!!, Emerson Knapp, Harrison Chen, Jonas Otto, Kenji Brameld (TRACLabs), Matthijs van der Burgh, Michael Carlstrom, Scott K Logan, Sebastian Javier D’Alessandro Szymanowski, Tanishq Chaudhary, Will, mosfet80

<a id="launch-pytest"></a>

## [launch\_pytest](https://github.com/ros2/launch/tree/lyrical/launch_pytest/CHANGELOG.rst)

- fix regressions ([#959](https://github.com/ros2/launch/issues/959))
- fix: add get\_launch\_test\_fixture\_scope for pytest compatibility ([#949](https://github.com/ros2/launch/issues/949))
- Switch osrf\_pycommon dependency to system package ([#817](https://github.com/ros2/launch/issues/817))
- Fix Setuptoolsdeprecations ([#898](https://github.com/ros2/launch/issues/898))
- Make sure to install py.typed files ([#886](https://github.com/ros2/launch/issues/886))
- Add remaining `py.typed` ([#884](https://github.com/ros2/launch/issues/884))
- Allow Path in substitutions, instead of requiring cast to str ([#873](https://github.com/ros2/launch/issues/873))
- fix(launch\_pytest): prevent re-wrapping test funtions on re-run ([#855](https://github.com/ros2/launch/issues/855))
- Contributors: Christophe Bedard, Daisuke Nishimatsu, David Revay, Emerson Knapp, Michael Carlstrom, Scott K Logan, mosfet80

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/lyrical/launch_ros/CHANGELOG.rst)

- Fix flake8 ([#529](https://github.com/ros2/launch_ros//issues/529))
- correct typos ([#524](https://github.com/ros2/launch_ros//issues/524))
- Fix regression ([#521](https://github.com/ros2/launch_ros//issues/521))
- Fix rhel10 flake8 error ([#515](https://github.com/ros2/launch_ros//issues/515))
- Compatiblity with ‘Populate Transitions’ [ros2/rcl#1269](https://github.com/ros2/rcl/issues/1269) ([#495](https://github.com/ros2/launch_ros/issues/495))
- remove importlib ([#508](https://github.com/ros2/launch_ros/issues/508))
- Make FindPackage substitutions a Path to get operator / ([#494](https://github.com/ros2/launch_ros/issues/494))
- Expose lifecycle\_node ([#327](https://github.com/ros2/launch_ros/issues/327)) (with test) ([#482](https://github.com/ros2/launch_ros/issues/482))
- Expose composable\_lifecycle\_node in front-end ([#480](https://github.com/ros2/launch_ros/issues/480))
- Switch osrf\_pycommon dependency to system package ([#431](https://github.com/ros2/launch_ros/issues/431))
- Fix SetUseSimTime for launch frontends ([#488](https://github.com/ros2/launch_ros/issues/488))
- fix setuptools deprecations ([#475](https://github.com/ros2/launch_ros/issues/475))
- improve type readability in errors ([#469](https://github.com/ros2/launch_ros/issues/469))
- Fix: LoadComposableNodes fails to parse wildcard param files correctly ([#460](https://github.com/ros2/launch_ros/issues/460)) ([#465](https://github.com/ros2/launch_ros/issues/465))
- Contributors: Auguste Lalande, Christophe Bedard, Emerson Knapp, Emre Kuru, Jasper van Brakel, Kenji Brameld, Michael Carlstrom, Scott K Logan, mosfet80

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/lyrical/launch_testing/CHANGELOG.rst)

- Correct typos ([#961](https://github.com/ros2/launch/issues/961))
- Fix test\_io\_tests for Ubuntu26 ([#960](https://github.com/ros2/launch/issues/960))
- Fix flake8 ([#952](https://github.com/ros2/launch/issues/952))
- Switch osrf\_pycommon dependency to system package ([#817](https://github.com/ros2/launch/issues/817))
- Fix Setuptoolsdeprecations ([#898](https://github.com/ros2/launch/issues/898))
- Make sure to install py.typed files ([#886](https://github.com/ros2/launch/issues/886))
- Add remaining `py.typed` ([#884](https://github.com/ros2/launch/issues/884))
- Updated `launch` typings ([#831](https://github.com/ros2/launch/issues/831))
- Contributors: Auguste Lalande, Christophe Bedard, Michael Carlstrom, Scott K Logan, mosfet80

<a id="launch-testing-ament-cmake"></a>

## [launch\_testing\_ament\_cmake](https://github.com/ros2/launch/tree/lyrical/launch_testing_ament_cmake/CHANGELOG.rst)

- Fix CMake deprecation ([#899](https://github.com/ros2/launch/issues/899))
- Contributors: mosfet80

<a id="launch-testing-examples"></a>

## [launch\_testing\_examples](https://github.com/ros2/examples/tree/lyrical/launch_testing/launch_testing_examples/CHANGELOG.rst)

- improve test integrity with rmw\_cyclonedds\_cpp. ([#440](https://github.com/ros2/examples/issues/440))
- Fix setuptools deprecations ([#421](https://github.com/ros2/examples/issues/421))
- Contributors: Tomoya Fujita, mosfet80

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/lyrical/launch_testing_ros/CHANGELOG.rst)

- Add tests isolation in launch\_testing\_ros ([#528](https://github.com/ros2/launch_ros//issues/528))
- Surpressing multi-threaded process warning from flake8. ([#520](https://github.com/ros2/launch_ros//issues/520))
- correct typos ([#524](https://github.com/ros2/launch_ros//issues/524))
- Fix launch\_ros\_testing shutdown race in WaitForTopics ([#511](https://github.com/ros2/launch_ros/issues/511))
- Give the option to inject a quality of service profile ([#493](https://github.com/ros2/launch_ros/issues/493))
- fix setuptools deprecations ([#475](https://github.com/ros2/launch_ros/issues/475))
- `WaitForTopics`: wait for publisher-subscriber connection to be established ([#474](https://github.com/ros2/launch_ros/issues/474))
- Contributors: Auguste Lalande, Giorgio Pintaudi, Julien Enoch, Michael Carroll, Tomoya Fujita, mosfet80

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/lyrical/launch_xml/CHANGELOG.rst)

- Correct typos ([#961](https://github.com/ros2/launch/issues/961))
- Support frontends for PathJoinSubstitution ([#943](https://github.com/ros2/launch/issues/943))
- Capture the environment variables in TimerAction ([#728](https://github.com/ros2/launch/issues/728))
- Expose StringJoinSubstitution to frontend ([#857](https://github.com/ros2/launch//issues/857))
- Fix all/any in xml and yaml launch files ([#906](https://github.com/ros2/launch/issues/906))
- Allow providing launch args to include using let in frontends ([#848](https://github.com/ros2/launch//issues/848))
- Fix Setuptoolsdeprecations ([#898](https://github.com/ros2/launch/issues/898))
- Make sure to install py.typed files ([#886](https://github.com/ros2/launch/issues/886))
- Add remaining `py.typed` ([#884](https://github.com/ros2/launch/issues/884))
- Fix `log\_*` warnings ([#883](https://github.com/ros2/launch/issues/883))
- Allow Path in substitutions, instead of requiring cast to str ([#873](https://github.com/ros2/launch/issues/873))
- Other Logging Implementations with `getLevelNamesMapping` fix ([#866](https://github.com/ros2/launch/issues/866))
- Revert “Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))” ([#865](https://github.com/ros2/launch/issues/865)) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
- Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))
- Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, Emerson Knapp, Matthijs van der Burgh, Michael Carlstrom, Sebastian Javier D’Alessandro Szymanowski, mosfet80

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/lyrical/launch_yaml/CHANGELOG.rst)

- Correct typos ([#961](https://github.com/ros2/launch/issues/961))
- Support frontends for PathJoinSubstitution ([#943](https://github.com/ros2/launch/issues/943))
- Capture the environment variables in TimerAction ([#728](https://github.com/ros2/launch/issues/728))
- Expose StringJoinSubstitution to frontend ([#857](https://github.com/ros2/launch//issues/857))
- Fix all/any in xml and yaml launch files ([#906](https://github.com/ros2/launch/issues/906))
- Allow providing launch args to include using let in frontends ([#848](https://github.com/ros2/launch//issues/848))
- Fix Setuptoolsdeprecations ([#898](https://github.com/ros2/launch/issues/898))
- Make sure to install py.typed files ([#886](https://github.com/ros2/launch/issues/886))
- Add remaining `py.typed` ([#884](https://github.com/ros2/launch/issues/884))
- Fix `log\_*` warnings ([#883](https://github.com/ros2/launch/issues/883))
- Other Logging Implementations with `getLevelNamesMapping` fix ([#866](https://github.com/ros2/launch/issues/866))
- Revert “Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))” ([#865](https://github.com/ros2/launch/issues/865)) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
- Add Other Logging Implementations ([#858](https://github.com/ros2/launch/issues/858))
- Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, Matthijs van der Burgh, Michael Carlstrom, Sebastian Javier D’Alessandro Szymanowski, mosfet80

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/lyrical/CHANGELOG.rst)

- Use new aggregate rosidl target instead of \_TARGETS ([#222](https://github.com/ros-tooling/libstatistics_collector/issues/222))
- fix cmake deprecation ([#214](https://github.com/ros-tooling/libstatistics_collector/issues/214))
- Bump ros-tooling/action-ros-ci from 0.3 to 0.4
- Bump codecov/codecov-action from 5.3.1 to 5.4.0
- Bump codecov/codecov-action from 5.1.2 to 5.3.1
- Bump codecov/codecov-action from 5.0.7 to 5.1.2
- Bump codecov/codecov-action from 4.6.0 to 5.0.7
- Contributors: Alexis Tsogias, dependabot[bot], mosfet80

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/lyrical/CHANGELOG.rst)

- Replace ament\_vendor with cmake module ([#67](https://github.com/ros2/libyaml_vendor/issues/67))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#65](https://github.com/ros2/libyaml_vendor/issues/65))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/lyrical/lifecycle/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- r-simonelli/demos-lifecycle ([#750](https://github.com/ros2/demos/issues/750))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Emerson Knapp, Lucas Wendland, Shane Loretz, mosfet80, r-simonelli

<a id="lifecycle-msgs"></a>

## [lifecycle\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/lifecycle_msgs/CHANGELOG.rst)

- Use builtin\_interfaces/Time for TransitionEvent stamp ([#185](https://github.com/ros2/rcl_interfaces/issues/185))
- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: Jasper van Brakel, mosfet80

<a id="lifecycle-py"></a>

## [lifecycle\_py](https://github.com/ros2/demos/tree/lyrical/lifecycle_py/CHANGELOG.rst)

- Add `ament_mypy` support and type hints to `lifecycle_py` ([#778](https://github.com/ros2/demos/issues/778))
- Revert lifecycle\_py accidental merge - ament\_mypy ([#777](https://github.com/ros2/demos//issues/777))
- action\_tutorials\_py: add ament\_mypy support ([#775](https://github.com/ros2/demos//issues/775))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- fix setuptools deprecations ([#733](https://github.com/ros2/demos/issues/733))
- Contributors: Lucas Wendland, Mohit Kumaresan, mohit, mosfet80

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/lyrical/logging_demo/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Scott K Logan, Shane Loretz, mosfet80

<a id="lttngpy"></a>

## [lttngpy](https://github.com/ros2/ros2_tracing/tree/lyrical/lttngpy/CHANGELOG.rst)

- Use <lttng/lttng.h> in lttngpy and clean up includes ([#222](https://github.com/ros2/ros2_tracing/issues/222))
- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- [Fix] compile fail ([#194](https://github.com/ros2/ros2_tracing/issues/194))
- Use pybind11 from deb or pixi ([#197](https://github.com/ros2/ros2_tracing/issues/197))
- Add support for starting tracing at runtime ([#191](https://github.com/ros2/ros2_tracing/issues/191))
- Contributors: Alejandro Hernández Cordero, RHolland, Shravan Deva, mosfet80

<a id="map-msgs"></a>

## [map\_msgs](https://github.com/ros-planning/navigation_msgs/tree/lyrical/map_msgs/CHANGELOG.rst)

- Change email address associated with maintainer
- fix cmake deprecation
- Contributors: David V. Lu, Steve Macenski, mosfet80

<a id="mcap-vendor"></a>

## [mcap\_vendor](https://github.com/ros2/rosbag2/tree/lyrical/mcap_vendor/CHANGELOG.rst)

- Update mcap dependency to version 2.1.3 ([#2355](https://github.com/ros2/rosbag2/issues/2355))
- Remove lz4 vendor package ([#2165](https://github.com/ros2/rosbag2/issues/2165))
- Replace `zstd_vendor` with `zstd_cmake_module` ([#2166](https://github.com/ros2/rosbag2/issues/2166))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Backport missing `cstdint` include ([#2008](https://github.com/ros2/rosbag2/issues/2008))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, David Anthony, mosfet80

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/lyrical/CHANGELOG.rst)

- Avoid vector assignment in message\_filters signal callback ([#292](https://github.com/ros2/message_filters/issues/292)) ([#293](https://github.com/ros2/message_filters/issues/293))
- Cleanup headers and removed deadcode ([#284](https://github.com/ros2/message_filters/issues/284)) ([#291](https://github.com/ros2/message_filters/issues/291))
- feat(python): add python implementation of InputAligner (backport [#283](https://github.com/ros2/message_filters/issues/283)) ([#286](https://github.com/ros2/message_filters/issues/286))
- C++20 style ([#272](https://github.com/ros2/message_filters/issues/272))
- ([#221](https://github.com/ros2/message_filters/issues/221)) Tutorials: Add DeltaFilter Python tutorial ([#277](https://github.com/ros2/message_filters/issues/277))
- DeltaFilter(C++): Add DeltaFilter class. Add tests ([#273](https://github.com/ros2/message_filters/issues/273)) ([#273](https://github.com/ros2/message_filters/issues/273))
- Removed dead code
- Improvements and more test coverage
- Use new ROSIDL aggregate CMake target
- Tutorials minor fixers: Replace the TODOs with the actual links to other tutorials as required. Rename Approximate-Tyme tutorial to Approximate-Time ([#266](https://github.com/ros2/message_filters/issues/266))
- Tutorials: Add LatestTime synchronization policy tutorial ([#266](https://github.com/ros2/message_filters/issues/266))
- Tutorials: Approximate-Synchronizer: Label CMake code blocks with the right language markings
- Tutorials: Add C++ tutorial for Approximate Epsilon Time Sync policy
- DeltaFilter(Python): Add DeltaFilter for Python. Add tests. Add docstring to filters and comparison handlers ([#252](https://github.com/ros2/message_filters/issues/252))
- remove setup.py ([#257](https://github.com/ros2/message_filters/issues/257))
- ([#246](https://github.com/ros2/message_filters/issues/246), [#186](https://github.com/ros2/message_filters/issues/186)) Subscriber(Python): Add callback\_group, event\_callbacks, qos\_overriding\_options, raw and content\_filter\_options arguments to \_\_init\_\_. ([#251](https://github.com/ros2/message_filters/issues/251))
- Add kwargs passing from Subscriber to node.create\_subscription ([#247](https://github.com/ros2/message_filters/issues/247)) Fixes callers that use callback\_group
- Get topic name from base class to propagate remaps ([#68](https://github.com/ros2/message_filters/issues/68))
- [#130](https://github.com/ros2/message_filters/issues/130) add simple filter tutorial for cpp ([#239](https://github.com/ros2/message_filters/issues/239))
- [#200](https://github.com/ros2/message_filters/issues/200) fix inconsistensy between cpp and python exact time synchronizer impl ([#238](https://github.com/ros2/message_filters/issues/238))
- Add simple filter tutorials ([#226](https://github.com/ros2/message_filters/issues/226))
- Update subscription callback signatures ([#222](https://github.com/ros2/message_filters/issues/222))
- Add chain tutorial python ([#219](https://github.com/ros2/message_filters/issues/219))
- Change function signature for Python Subscriber class ([#220](https://github.com/ros2/message_filters/issues/220))
- Add Python implementation for a Chain filter ([#213](https://github.com/ros2/message_filters/issues/213))
- Fix comparison of different time sources in C++ TimeSequencer ([#202](https://github.com/ros2/message_filters/issues/202))
- Some fixes to documentation ([#208](https://github.com/ros2/message_filters/issues/208))
- Create a Chain class tutorial for C++ ([#203](https://github.com/ros2/message_filters/issues/203))
- get rid of deprecated rclcpp::spin\_some(). ([#201](https://github.com/ros2/message_filters/issues/201))
- Add ‘Cache (C++)’ tutorial ([#196](https://github.com/ros2/message_filters/issues/196))
- cache.hpp: Add allow\_headerless ([#195](https://github.com/ros2/message_filters/issues/195))
- Simplify method call ([#194](https://github.com/ros2/message_filters/issues/194))
- Fix cache tutorial: added tab extension ([#190](https://github.com/ros2/message_filters/issues/190))
- Add tutorial for Cache filter for Python ([#185](https://github.com/ros2/message_filters/issues/185))
- fix cmake deprecation ([#182](https://github.com/ros2/message_filters/issues/182))
- update documentation ([#180](https://github.com/ros2/message_filters/issues/180))
- Removed missing pragma ([#179](https://github.com/ros2/message_filters/issues/179))
- Removed Subscriber deprecation ([#177](https://github.com/ros2/message_filters/issues/177))
- Removed deprecated headers ([#176](https://github.com/ros2/message_filters/issues/176))
- Use warning instead of warn ([#178](https://github.com/ros2/message_filters/issues/178))
- Docs - Remove C++ implementation limit of 9 channels ([#174](https://github.com/ros2/message_filters/issues/174))
- Contributors: Alejandro Hernandez Cordero, Alejandro Hernández Cordero, Alex Spitzer, Emerson Knapp, Erwin L., EsipovPA, Johannes Böhm, Michael Carlstrom, Patrick Roncagliolo, Pavel Esipov, Samuel Foo Enze, Tomoya Fujita, mergify[bot], mini-1235, mosfet80

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/lyrical/CHANGELOG.rst)

- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#40](https://github.com/ros2/mimick_vendor/issues/40))
- Contributors: Chris Lalancette

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/nav_msgs/CHANGELOG.rst)

- Adding the Trajectory and trajectoryPoint messages ([#296](https://github.com/ros2/common_interfaces/issues/296))
- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: Steve Macenski, mosfet80

<a id="osrf-testing-tools-cpp"></a>

## [osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/lyrical/osrf_testing_tools_cpp/CHANGELOG.rst)

- fix cmake min version ([#96](https://github.com/osrf/osrf_testing_tools_cpp/issues/96))
- fix cmake deprecation ([#94](https://github.com/osrf/osrf_testing_tools_cpp/issues/94))
- Contributors: mosfet80

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/lyrical/pendulum_control/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Update subscription callback signatures ([#754](https://github.com/ros2/demos/issues/754))
- get rid of deprecated rclcpp::spin\_some(). ([#734](https://github.com/ros2/demos/issues/734))
- Use EnableRmwIsolation in launch tests ([#724](https://github.com/ros2/demos/issues/724))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/lyrical/pendulum_msgs/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Contributors: mosfet80

<a id="performance-test-fixture"></a>

## [performance\_test\_fixture](https://github.com/ros2/performance_test_fixture/tree/lyrical/CHANGELOG.rst)

- fix cmake deprecation ([#31](https://github.com/ros2/performance_test_fixture/issues/31))
- Remove CODEOWNERS and mirror-rolling-to-main workflow. ([#28](https://github.com/ros2/performance_test_fixture/issues/28))
- Contributors: Chris Lalancette, mosfet80

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/lyrical/pluginlib/CHANGELOG.rst)

- Fix some minor issues ([#292](https://github.com/ros/pluginlib/issues/292))
- Add support for passing arguments to constructors ([#291](https://github.com/ros/pluginlib/issues/291))
- Export includes ([#290](https://github.com/ros/pluginlib/issues/290))
- Updated deprecated ament\_index\_cpp API ([#289](https://github.com/ros/pluginlib/issues/289))
- refactor: replace regex with find\_last\_of to split plugin name ([#271](https://github.com/ros/pluginlib/issues/271))
- Removed tinyxml2\_vendor dependency ([#274](https://github.com/ros/pluginlib/issues/274))
- Add ros2plugin ([#165](https://github.com/ros/pluginlib/issues/165))
- Contributors: Alejandro Hernández Cordero, Jeremie Deray, ipa-fez, pum1k

<a id="point-cloud-transport"></a>

## [point\_cloud\_transport](https://github.com/ros-perception/point_cloud_transport/tree/lyrical/point_cloud_transport/CHANGELOG.rst)

- Fix exit crash on aarch64 by using leaky singleton for global loader ([#157](https://github.com/ros-perception/point_cloud_transport/issues/157))
- Include message type ([#152](https://github.com/ros-perception/point_cloud_transport/issues/152))
- Use new aggregate rosidl target instead of \_TARGETS ([#153](https://github.com/ros-perception/point_cloud_transport/issues/153)) Co-authored-by: Alexis Tsogias <[a.tsogias@cellumation.com](mailto:a.tsogias%40cellumation.com)>
- Improvements ([#150](https://github.com/ros-perception/point_cloud_transport/issues/150))
- Expose original ROS Publishers and Subscription ([#146](https://github.com/ros-perception/point_cloud_transport/issues/146)) ([#148](https://github.com/ros-perception/point_cloud_transport/issues/148))
- Fix duplicate component registration for Republisher ([#142](https://github.com/ros-perception/point_cloud_transport/issues/142))
- Removed outdated comment ([#138](https://github.com/ros-perception/point_cloud_transport/issues/138))
- Use standard unsigned int in place of uint for Windows compatibility ([#134](https://github.com/ros-perception/point_cloud_transport/issues/134))
- Update subscriber filter ([#126](https://github.com/ros-perception/point_cloud_transport/issues/126))
- Simplify NodeInterface API mehotd call ([#129](https://github.com/ros-perception/point_cloud_transport/issues/129))
- Fixed QOS override tests ([#128](https://github.com/ros-perception/point_cloud_transport/issues/128))
- Deprecated rmw\_qos\_profile\_t ([#125](https://github.com/ros-perception/point_cloud_transport/issues/125))
- Feat/Add LifecycleNode Support ([#109](https://github.com/ros-perception/point_cloud_transport/issues/109))
- Add `rclcpp::shutdown` ([#110](https://github.com/ros-perception/point_cloud_transport/issues/110))
- Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed ElSheikh, Michael Carroll, Silvio Traversaro, Yuyuan Yuan, mergify[bot], mini-1235

<a id="point-cloud-transport-py"></a>

## [point\_cloud\_transport\_py](https://github.com/ros-perception/point_cloud_transport/tree/lyrical/point_cloud_transport_py/CHANGELOG.rst)

- Use new aggregate rosidl target instead of \_TARGETS ([#153](https://github.com/ros-perception/point_cloud_transport/issues/153))
- Python improvements ([#151](https://github.com/ros-perception/point_cloud_transport/issues/151))
- Use pybind11 from deb or pixi ([#131](https://github.com/ros-perception/point_cloud_transport/issues/131))
- Simplify NodeInterface API mehotd call ([#129](https://github.com/ros-perception/point_cloud_transport/issues/129))
- Feat/Add LifecycleNode Support ([#109](https://github.com/ros-perception/point_cloud_transport/issues/109))
- Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed ElSheikh

<a id="python-qt-binding"></a>

## [python\_qt\_binding](https://github.com/ros-visualization/python_qt_binding/tree/lyrical/CHANGELOG.rst)

- Pick Qt version at build time, not install time ([#161](https://github.com/ros-visualization/python_qt_binding/issues/161))
- Re-add exec depend on python3 qt bindings rosdep key ([#160](https://github.com/ros-visualization/python_qt_binding/issues/160))
- Remove qt6-base-dev from package.xml ([#159](https://github.com/ros-visualization/python_qt_binding/issues/159))
- Depend on python3-dev ([#158](https://github.com/ros-visualization/python_qt_binding/issues/158))
- Use sip-build and python3\_add\_library for Qt5/Qt6 ([#157](https://github.com/ros-visualization/python_qt_binding/issues/157))
- fix setuptools deprecation ([#151](https://github.com/ros-visualization/python_qt_binding/issues/151))
- fix cmake deprecation ([#150](https://github.com/ros-visualization/python_qt_binding/issues/150))
- Remove the mirror-rolling-to-main workflow ([#145](https://github.com/ros-visualization/python_qt_binding/issues/145))
- Remove CODEOWNERS ([#144](https://github.com/ros-visualization/python_qt_binding/issues/144))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane Loretz, mosfet80

<a id="qt-dotgraph"></a>

## [qt\_dotgraph](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_dotgraph/CHANGELOG.rst)

- More qt6 fixes ([#334](https://github.com/ros-visualization/qt_gui_core/issues/334)) ([#335](https://github.com/ros-visualization/qt_gui_core/issues/335)) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Support qt6 ([#293](https://github.com/ros-visualization/qt_gui_core/issues/293))
- Ignore case when asserting snippet presence in tests ([#314](https://github.com/ros-visualization/qt_gui_core/issues/314))
- Fix setupTools deprecations ([#308](https://github.com/ros-visualization/qt_gui_core/issues/308))
- Contributors: Alejandro Hernández Cordero, Scott K Logan, mergify[bot], mosfet80

<a id="qt-gui"></a>

## [qt\_gui](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui/CHANGELOG.rst)

- More qt6 fixes ([#334](https://github.com/ros-visualization/qt_gui_core/issues/334)) ([#335](https://github.com/ros-visualization/qt_gui_core/issues/335)) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Support qt6 ([#293](https://github.com/ros-visualization/qt_gui_core/issues/293))
- fix(qt\_gui): \_\_builtin\_\_ -> builtins ([#315](https://github.com/ros-visualization/qt_gui_core/issues/315))
- Fix cmake deprecations ([#307](https://github.com/ros-visualization/qt_gui_core/issues/307))
- Contributors: Alejandro Hernández Cordero, Matthijs van der Burgh, mergify[bot], mosfet80

<a id="qt-gui-app"></a>

## [qt\_gui\_app](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_app/CHANGELOG.rst)

- Fix cmake deprecations ([#307](https://github.com/ros-visualization/qt_gui_core/issues/307))
- Contributors: mosfet80

<a id="qt-gui-core"></a>

## [qt\_gui\_core](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_core/CHANGELOG.rst)

- Update qt\_gui\_core to package.xml version 2. ([#319](https://github.com/ros-visualization/qt_gui_core/issues/319))
- Fix cmake deprecations ([#307](https://github.com/ros-visualization/qt_gui_core/issues/307))
- Contributors: Chris Lalancette, mosfet80

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_cpp/CHANGELOG.rst)

- More qt6 fixes ([#334](https://github.com/ros-visualization/qt_gui_core/issues/334)) ([#335](https://github.com/ros-visualization/qt_gui_core/issues/335)) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- find\_package(Qt…) in downstream packages ([#332](https://github.com/ros-visualization/qt_gui_core/issues/332))
- Export qt dependencies in package.xml ([#331](https://github.com/ros-visualization/qt_gui_core/issues/331))
- Use qt-base-dev / libqtwidgets ([#330](https://github.com/ros-visualization/qt_gui_core/issues/330))
- Support qt6 ([#293](https://github.com/ros-visualization/qt_gui_core/issues/293))
- Use new aggregate rosidl target instead of \_TARGETS ([#325](https://github.com/ros-visualization/qt_gui_core/issues/325))
- remove unsued setup.py ([#323](https://github.com/ros-visualization/qt_gui_core/issues/323))
- Removed tinyxml2\_vendor dependency ([#309](https://github.com/ros-visualization/qt_gui_core/issues/309))
- Fix cmake deprecations ([#307](https://github.com/ros-visualization/qt_gui_core/issues/307))
- Removed deprecated headers ([#305](https://github.com/ros-visualization/qt_gui_core/issues/305))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#302](https://github.com/ros-visualization/qt_gui_core/issues/302))
- Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Michael Carlstrom, Shane Loretz, mergify[bot], mosfet80

<a id="qt-gui-py-common"></a>

## [qt\_gui\_py\_common](https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_py_common/CHANGELOG.rst)

- More qt6 fixes ([#334](https://github.com/ros-visualization/qt_gui_core/issues/334)) ([#335](https://github.com/ros-visualization/qt_gui_core/issues/335))
- Support qt6 ([#293](https://github.com/ros-visualization/qt_gui_core/issues/293))
- remove unsued setup.py ([#323](https://github.com/ros-visualization/qt_gui_core/issues/323))
- Fix cmake deprecations ([#307](https://github.com/ros-visualization/qt_gui_core/issues/307))
- Contributors: Alejandro Hernández Cordero, Michael Carlstrom, mergify[bot], mosfet80

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/lyrical/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Contributors: Emerson Knapp, Lucas Wendland, mosfet80

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/lyrical/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- fix setuptools deprecations ([#731](https://github.com/ros2/demos/issues/731))
- Contributors: Lucas Wendland, mosfet80

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/lyrical/rcl/CHANGELOG.rst)

- feat: Added check for double usage of entities in rcl\_waitset ([#1206](https://github.com/ros2/rcl/issues/1206))
- Preserve `rmw_create_node` error state in `rcl_node_init` by using `RCL_EXPECT_ERROR_IS_SET` ([#1313](https://github.com/ros2/rcl/issues/1313))
- Remove clang warnings ([#1315](https://github.com/ros2/rcl/issues/1315))
- Add RCL\_EXPECT\_ERROR\_IS\_SET macro ([#1312](https://github.com/ros2/rcl/issues/1312))
- Improved documentation of rcl\_XYZ\_set\_on\_new\_XYZ\_callback ([#1289](https://github.com/ros2/rcl/issues/1289))
- Add rcl\_subscription\_options\_set\_acceptable\_buffer\_backends with proper lifetime management ([#1308](https://github.com/ros2/rcl/issues/1308))
- Added tracepoint to rcl\_take\_loaned\_message ([#1300](https://github.com/ros2/rcl/issues/1300))
- Apply change from “Use new aggregate rosidl target instead of \_TARGETS ([#1302](https://github.com/ros2/rcl/issues/1302))” on some leftovers ([#1309](https://github.com/ros2/rcl/issues/1309))
- Remove the check for content filter support at the RCL layer ([#1304](https://github.com/ros2/rcl/issues/1304))
- Use new aggregate rosidl target instead of \_TARGETS ([#1302](https://github.com/ros2/rcl/issues/1302))
- Add API for client libraries to set action server goal expiration callbacks ([#1295](https://github.com/ros2/rcl/issues/1295))
- Fujitatomoya/improve rcl test graph ([#1296](https://github.com/ros2/rcl/issues/1296))
- Add content filtering support check for subscriptions ([#1293](https://github.com/ros2/rcl/issues/1293))
- rcl\_logging\_implementation package support. ([#1276](https://github.com/ros2/rcl/issues/1276))
- Remove default from switch with enum, so that compiler warns. ([#1278](https://github.com/ros2/rcl/issues/1278))
- Add clients servers info ([#1161](https://github.com/ros2/rcl/issues/1161))
- Fix REP url locations ([#1271](https://github.com/ros2/rcl/issues/1271))
- rcl\_logging\_allocator\_initialize() support. ([#1049](https://github.com/ros2/rcl/issues/1049))
- Fix typos: occurrs->occurs, successfull->successful ([#1259](https://github.com/ros2/rcl/issues/1259))
- Refer to ‘the middleware’ and not ‘the DDS implementation’ in doc ([#1260](https://github.com/ros2/rcl/issues/1260))
- Switch to isolated testing via rmw\_test\_fixture ([#1251](https://github.com/ros2/rcl/issues/1251))
- Fix Cmake deprecation ([#1249](https://github.com/ros2/rcl/issues/1249))
- Assert HistoryQoS in test\_info\_by\_topic ([#1242](https://github.com/ros2/rcl//issues/1242))
- Add a test for the subscription option ‘ignore\_local\_publications’ ([#1239](https://github.com/ros2/rcl//issues/1239))
- remove unnecessary test\_with\_localhost\_only. ([#1238](https://github.com/ros2/rcl/issues/1238))
- Address memory leaks in rcl test\_timer\_init\_state ([#1236](https://github.com/ros2/rcl/issues/1236))
- Removed unused nondefault\_qos\_profile ([#1233](https://github.com/ros2/rcl/issues/1233))
- Removed unused functions ([#1230](https://github.com/ros2/rcl/issues/1230))
- remove rcl\_qos\_profile\_rosout\_default. ([#1225](https://github.com/ros2/rcl/issues/1225))
- remove rmw\_connext from test. ([#1226](https://github.com/ros2/rcl/issues/1226))
- Fix a dangling pointer discovered by a fresh Clang ([#1222](https://github.com/ros2/rcl/issues/1222))
- Contributors: Akihiko Komada, Alejandro Hernández Cordero, Alexander Kornienko, Alexis Tsogias, Barry Xu, CY Chen, Christophe Bedard, Emerson Knapp, Janosch Machowinski, Lee, Mario Domínguez López, Michael Orlov, Minju, Oren Bell PhD, Rushhaank Sahay, Sai Kishor Kothakota, Shane Loretz, Skyler Medeiros, Tim Clephas, Tomoya Fujita, mosfet80, yadunund

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/lyrical/rcl_action/CHANGELOG.rst)

- fix(rcl\_action): use RMW isolation for cross-node tests ([#1311](https://github.com/ros2/rcl/issues/1311))
- Add 2 interfaces for configuring action client feedback subscription contents filter ([#1287](https://github.com/ros2/rcl/issues/1287))
- Apply change from “Use new aggregate rosidl target instead of \_TARGETS ([#1302](https://github.com/ros2/rcl/issues/1302))” on some leftovers ([#1309](https://github.com/ros2/rcl/issues/1309))
- simplify error logging for timer cancellation ([#1307](https://github.com/ros2/rcl/issues/1307))
- fix: Prevent short time endless loop in expire\_timer ([#1303](https://github.com/ros2/rcl/issues/1303))
- Add API for client libraries to set action server goal expiration callbacks ([#1295](https://github.com/ros2/rcl/issues/1295))
- support rcl\_action\_count\_clients and rcl\_action\_count\_servers. ([#1294](https://github.com/ros2/rcl/issues/1294))
- Fix REP url locations ([#1271](https://github.com/ros2/rcl/issues/1271))
- add rcl\_action\_goal\_handle\_is\_abortable(). ([#1257](https://github.com/ros2/rcl/issues/1257))
- Fix Cmake deprecation ([#1249](https://github.com/ros2/rcl/issues/1249))
- Contributors: Alexis Tsogias, Barry Xu, Janosch Machowinski, Skyler Medeiros, Tim Clephas, Tomoya Fujita, William Woodall, Yuyuan Yuan, mosfet80

<a id="rcl-interfaces"></a>

## [rcl\_interfaces](https://github.com/ros2/rcl_interfaces/tree/lyrical/rcl_interfaces/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/lyrical/rcl_lifecycle/CHANGELOG.rst)

- Apply change from “Use new aggregate rosidl target instead of \_TARGETS ([#1302](https://github.com/ros2/rcl/issues/1302))” on some leftovers ([#1309](https://github.com/ros2/rcl/issues/1309))
- Populate Transitions in Transition Events (continuation) ([#1269](https://github.com/ros2/rcl/issues/1269))
- Fix REP url locations ([#1271](https://github.com/ros2/rcl/issues/1271))
- Fix Cmake deprecation ([#1249](https://github.com/ros2/rcl/issues/1249))
- introduce rcl\_lifecycle\_get\_transition\_label\_by\_id(). ([#1229](https://github.com/ros2/rcl/issues/1229))
- Contributors: Alexis Tsogias, Jasper van Brakel, Tim Clephas, Tomoya Fujita, mosfet80

<a id="rcl-logging-implementation"></a>

## [rcl\_logging\_implementation](https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_implementation/CHANGELOG.rst)

- update rcl\_logging\_implementation architecture diagram. ([#137](https://github.com/ros2/rcl_logging/issues/137))
- rcl logging implementation ([#135](https://github.com/ros2/rcl_logging/issues/135)) \* 1st draft bring-up for rcl\_logging\_implementation package. \* add test\_logging\_implementation to check dynamic loading. \* address Copilot review comments. \* fix: correct visibility macro for DLL export in CMakeLists.txt \* add visibility control with RCL\_LOGGING\_IMPLEMENTATION\_DEFAULT\_VISIBILITY. \* load the all symbols at the initialization. \* Use goto pattern to eliminate the cleanup duplication. \* Add basic design doc of rmw\_logging\_implementation. \* use RCPPUTILS\_SCOPE\_EXIT instead of goto statement. \* logging visibility macro was incorrect. \* logging symbols stay until the peocess actually exits. ——— Co-authored-by: Barry Xu <[barry.xu@sony.com](mailto:barry.xu%40sony.com)>
- Contributors: Tomoya Fujita

<a id="rcl-logging-interface"></a>

## [rcl\_logging\_interface](https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_interface/CHANGELOG.rst)

- Fix cmake deprecation ([#133](https://github.com/ros2/rcl_logging/issues/133))
- Contributors: mosfet80

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_noop/CHANGELOG.rst)

- Fix cmake deprecation ([#133](https://github.com/ros2/rcl_logging/issues/133))
- Cleanup rcl\_logging\_noop dependencies. ([#132](https://github.com/ros2/rcl_logging/issues/132)) It shouldn’t build\_export\_depend anything (as nothing downstream should link against it), and all of its dependencies can be private.
- Contributors: Chris Lalancette, mosfet80

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_spdlog/CHANGELOG.rst)

- feat: add env variable to configure flushing interval ([#139](https://github.com/ros2/rcl_logging/issues/139))
- Fix cmake deprecation ([#133](https://github.com/ros2/rcl_logging/issues/133))
- Cleanup overwritten warning messages on error. ([#128](https://github.com/ros2/rcl_logging/issues/128))
- Contributors: Achille Verheye, Chris Lalancette, mosfet80

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/lyrical/rcl_yaml_param_parser/CHANGELOG.rst)

- Remove clang warnings ([#1315](https://github.com/ros2/rcl/issues/1315))
- fix ([#1310](https://github.com/ros2/rcl/issues/1310))
- Use the POSIX locale to parse YAML double ([#1292](https://github.com/ros2/rcl/issues/1292))
- rcl\_yaml\_node\_struct\_print print loop interation fix. ([#1290](https://github.com/ros2/rcl//issues/1290))
- rcl\_yaml\_param\_parser: add support for binary tag to load byte arrays parameters ([#1256](https://github.com/ros2/rcl//issues/1256))
- Validate name input in add\_name\_to\_ns function ([#1281](https://github.com/ros2/rcl/issues/1281))
- parse\_key() should use yaml\_map\_lvl\_t instead of uint\_32. ([#1279](https://github.com/ros2/rcl/issues/1279))
- Remove default from switch with enum, so that compiler warns. ([#1278](https://github.com/ros2/rcl/issues/1278))
- Add yaml tags support ([#1275](https://github.com/ros2/rcl/issues/1275)) Co-authored-by: Lei Liu <[Lei.Liu.AP@sony.com](mailto:Lei.Liu.AP%40sony.com)>
- Fix REP url locations ([#1271](https://github.com/ros2/rcl/issues/1271))
- Fix param file parsing failure with wildcards due to ordering ([#1253](https://github.com/ros2/rcl/issues/1253))
- Fix Cmake deprecation ([#1249](https://github.com/ros2/rcl/issues/1249))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Hugal31, Michael Carlstrom, Romain Reignier, Tim Clephas, Tomoya Fujita, mosfet80

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/lyrical/rclcpp/CHANGELOG.rst)

- Include EventsCBGExecutor ([#3137](https://github.com/ros2/rclcpp/issues/3137))
- Fix topic statistics for IPC subscriptions ([#3130](https://github.com/ros2/rclcpp/issues/3130))
- fix: Fixed MSVC compile errors ([#3135](https://github.com/ros2/rclcpp/issues/3135))
- feat: Added callback group events executor ([#3097](https://github.com/ros2/rclcpp/issues/3097))
- Fix wrong dependency ([#3133](https://github.com/ros2/rclcpp/issues/3133))
- feat: Switch to c++20 and remove resulting compile warnings ([#3124](https://github.com/ros2/rclcpp/issues/3124))
- fix: Compile fix for MSVC 2022 ([#3131](https://github.com/ros2/rclcpp/issues/3131))
- Remove warnings on tests ([#3125](https://github.com/ros2/rclcpp/issues/3125))
- feat: Add per-node log level support via NodeOptions ([#3092](https://github.com/ros2/rclcpp/issues/3092))
- Improve error message when parameter value is missing ([#3093](https://github.com/ros2/rclcpp/issues/3093))
- Fix incorrect internal clear inside `RingBufferImplementation` ([#3116](https://github.com/ros2/rclcpp/issues/3116))
- Add acceptable\_buffer\_backends field in SubscriptionOptionsBase ([#3098](https://github.com/ros2/rclcpp/issues/3098))
- Remove comment about removed StaticSingleThreadedExecutor ([#3121](https://github.com/ros2/rclcpp/issues/3121))
- Added tracepoint ([#3103](https://github.com/ros2/rclcpp/issues/3103))
- Add ConstRefCallback in take\_shared\_method ([#3066](https://github.com/ros2/rclcpp/issues/3066))
- Replace mispelled “${rcl\_interfaces\_TARGES}” by rcl\_interfaces::rcl\_interfaces ([#3112](https://github.com/ros2/rclcpp/issues/3112))
- Use new ROSIDL aggregate CMake target ([#3105](https://github.com/ros2/rclcpp/issues/3105))
- remove duplicate test cases in TestAnySubscriptionCallback::is\_serialized\_message\_callback ([#3104](https://github.com/ros2/rclcpp/issues/3104))
- keep the event alive throught the assertion, preveiting the race. ([#3099](https://github.com/ros2/rclcpp/issues/3099))
- Add support check for content filter feature in subscription ([#3089](https://github.com/ros2/rclcpp/issues/3089))
- Expose ServiceType in Service public API ([#3088](https://github.com/ros2/rclcpp/issues/3088))
- perf: Optimized out shared\_ptr copies ([#3079](https://github.com/ros2/rclcpp/issues/3079))
- avoid stale parameter events in content filter tests. ([#3085](https://github.com/ros2/rclcpp/issues/3085))
- improve lookup time for matches\_any\_publishers() ([#3084](https://github.com/ros2/rclcpp/issues/3084))
- Add tests isolation ([#3081](https://github.com/ros2/rclcpp/issues/3081))
- Revert “improve lookup time for matches\_any\_publishers(). ([#3068](https://github.com/ros2/rclcpp/issues/3068))” ([#3077](https://github.com/ros2/rclcpp/issues/3077))
- improve lookup time for matches\_any\_publishers(). ([#3068](https://github.com/ros2/rclcpp/issues/3068))
- fix: Use default rcl allocator if allocator is std::allocator ([#3058](https://github.com/ros2/rclcpp/issues/3058))
- fix: Various data races in test cases ([#3057](https://github.com/ros2/rclcpp/issues/3057))
- fix: Fix data race in CallbackGroup::size() ([#3056](https://github.com/ros2/rclcpp/issues/3056))
- remove default: so that compiler can detect the missing case. ([#3048](https://github.com/ros2/rclcpp/issues/3048))
- use weak\_ptr for rcl entities in the memory strategy. ([#2988](https://github.com/ros2/rclcpp/issues/2988))
- remove test\_static\_executor\_entities\_collector.cpp ([#3041](https://github.com/ros2/rclcpp/issues/3041))
- include the 1st spin that might throw the exception. ([#3042](https://github.com/ros2/rclcpp/issues/3042))
- print warning message on owner node if the parameter operation fails. ([#3037](https://github.com/ros2/rclcpp/issues/3037))
- fix context in wait for message wait set ([#3030](https://github.com/ros2/rclcpp/issues/3030))
- Revert “construct wait set with passed in context ([#3021](https://github.com/ros2/rclcpp/issues/3021))” ([#3028](https://github.com/ros2/rclcpp/issues/3028))
- construct wait set with passed in context ([#3021](https://github.com/ros2/rclcpp/issues/3021))
- Improve the robustness of the TopicEndpointInfo constructor ([#3013](https://github.com/ros2/rclcpp/issues/3013))
- Deprecate the shared\_ptr<MessageT> subscription callback signatures ([#2975](https://github.com/ros2/rclcpp/issues/2975))
- Updated deprecated ament\_index\_cpp API ([#3011](https://github.com/ros2/rclcpp/issues/3011))
- Unified Node Interfaces: Add const version of get\_node\_x\_interface() ([#3006](https://github.com/ros2/rclcpp/issues/3006))
- Parameter Descriptor Simplification ([#2179](https://github.com/ros2/rclcpp/issues/2179))
- ParameterEventHandler support ContentFiltering ([#2971](https://github.com/ros2/rclcpp/issues/2971))
- update policy\_name\_from\_kind && test\_qos ([#2156](https://github.com/ros2/rclcpp/issues/2156))
- Add ability to disable and enable subscription’s callbacks ([#2985](https://github.com/ros2/rclcpp/issues/2985))
- Switch to isolated testing via rmw\_test\_fixture ([#2929](https://github.com/ros2/rclcpp/issues/2929))
- remove I/O from signal handler. ([#2986](https://github.com/ros2/rclcpp/issues/2986))
- correct test function descriptions ([#2970](https://github.com/ros2/rclcpp/issues/2970))
- add : get clients, servers info ([#2569](https://github.com/ros2/rclcpp/issues/2569))
- Fix REP url locations ([#2987](https://github.com/ros2/rclcpp/issues/2987))
- clear handles before node destruction in test\_memory\_strategy. ([#2969](https://github.com/ros2/rclcpp/issues/2969))
- Added static assert asserting custom types have no overloaded operator new ([#2954](https://github.com/ros2/rclcpp/issues/2954))
- Store graph listener inside the context instead of the node graph ([#2952](https://github.com/ros2/rclcpp/issues/2952))
- Reapply “Catch the exception from rate.sleep() if the context is invalid. ([#2956](https://github.com/ros2/rclcpp/issues/2956))” ([#2963](https://github.com/ros2/rclcpp/issues/2963)) ([#2964](https://github.com/ros2/rclcpp/issues/2964))
- Revert “Catch the exception from rate.sleep() if the context is invalid. ([#2956](https://github.com/ros2/rclcpp/issues/2956))” ([#2963](https://github.com/ros2/rclcpp/issues/2963))
- Catch the exception from rate.sleep() if the context is invalid. ([#2956](https://github.com/ros2/rclcpp/issues/2956))
- update Time documentation ([#2955](https://github.com/ros2/rclcpp/issues/2955))
- Removed warning ([#2949](https://github.com/ros2/rclcpp/issues/2949))
- add note about problems with spin\_until\_future\_complete ([#2849](https://github.com/ros2/rclcpp/issues/2849))
- deprecate rclcpp::spin\_some and rclcpp::spin\_all ([#2848](https://github.com/ros2/rclcpp/issues/2848))
- Improve the function extract\_type\_identifier ([#2923](https://github.com/ros2/rclcpp/issues/2923))
- Allow for implicitly convertable loggers as well ([#2922](https://github.com/ros2/rclcpp/issues/2922))
- Fix: improve exception context for parameter\_value\_from ([#2917](https://github.com/ros2/rclcpp/issues/2917))
- Fix `start_type_description_service` param handling ([#2897](https://github.com/ros2/rclcpp/issues/2897))
- Add qos parameter for wait\_for\_message function ([#2903](https://github.com/ros2/rclcpp/issues/2903))
- Fujitatomoya/test append parameter override ([#2896](https://github.com/ros2/rclcpp/issues/2896))
- Expose `typesupport_helpers` API needed for the Rosbag2 ([#2858](https://github.com/ros2/rclcpp/issues/2858))
- Remove comment about now-removed StaticSingleThreadedExecutor ([#2893](https://github.com/ros2/rclcpp/issues/2893))
- Add overload of `append_parameter_override` ([#2891](https://github.com/ros2/rclcpp/issues/2891))
- fix: Don’t deadlock if removing shutdown callbacks in a shutdown callback ([#2886](https://github.com/ros2/rclcpp/issues/2886))
- Hand-code logging.hpp ([#2870](https://github.com/ros2/rclcpp/issues/2870))
- Adressed TODO in node\_graph ([#2877](https://github.com/ros2/rclcpp/issues/2877))
- fix test\_publisher\_with\_system\_default\_qos. ([#2881](https://github.com/ros2/rclcpp/issues/2881))
- Fix for memory leaks in rclcpp::SerializedMessage ([#2861](https://github.com/ros2/rclcpp/issues/2861))
- Removed warning test\_qos ([#2859](https://github.com/ros2/rclcpp/issues/2859))
- Added missing chrono includes ([#2854](https://github.com/ros2/rclcpp/issues/2854))
- get\_all\_data\_impl() does not handle null pointers properly, causing segmentation fault ([#2840](https://github.com/ros2/rclcpp/issues/2840))
- QoSInitialization::from\_rmw does not validate invalid history policy values, leading to silent failures ([#2841](https://github.com/ros2/rclcpp/issues/2841))
- remove get\_notify\_guard\_condition from NodeBaseInterface. ([#2839](https://github.com/ros2/rclcpp/issues/2839))
- Removed deprecated StaticSingleThreadedExecutor ([#2835](https://github.com/ros2/rclcpp/issues/2835))
- Removed deprecated rcpputils Path ([#2834](https://github.com/ros2/rclcpp/issues/2834))
- Add range constraints for applicable array parameters ([#2828](https://github.com/ros2/rclcpp/issues/2828))
- Update RingBufferImplementation to clear internal data. ([#2837](https://github.com/ros2/rclcpp/issues/2837))
- Removed deprecated cancel\_sleep\_or\_wait ([#2836](https://github.com/ros2/rclcpp/issues/2836))
- Add missing ‘s’ to ‘NodeParametersInterface’ in doc/comment ([#2831](https://github.com/ros2/rclcpp/issues/2831))
- subordinate node consistent behavior and update docstring. ([#2822](https://github.com/ros2/rclcpp/issues/2822))
- throws std::invalid\_argument if ParameterEvent is NULL. ([#2814](https://github.com/ros2/rclcpp/issues/2814))
- Removed clang warnings ([#2823](https://github.com/ros2/rclcpp/issues/2823))
- Contributors: Alberto Soragna, Alejandro Hernández Cordero, Alex Youngs, Alexis Tsogias, Andrianov Roman, Barry Xu, CY Chen, Chris Lalancette, Christophe Bedard, Danil, Emerson Knapp, Ilario A. Azzollini, Ivo Ivanov, Janosch Machowinski, Julien Enoch, Lee, Lucas Wendland, Maurice Alexander Purnawan, Michael Carlstrom, Michael Carroll, Michael Orlov, Michiel Leegwater, Minju, Oren Bell, Patrick Roncagliolo, Peng Wang, Rahat Dhande, Skyler Medeiros, Sriharsha Ghanta, Tim Clephas, Tomoya Fujita, Yadnyeshwar Amol Sakhare, Yuchen966, fabianhirmann, jay, yadunund

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_action/CHANGELOG.rst)

- publish\_feedback should effect only on executing state. ([#3118](https://github.com/ros2/rclcpp/issues/3118))
- Support to configure feedback subscription content filter for action client ([#3034](https://github.com/ros2/rclcpp/issues/3034))
- Use new ROSIDL aggregate CMake target ([#3105](https://github.com/ros2/rclcpp/issues/3105))
- Fix expiration of action goals when EventsExecutors are used ([#3018](https://github.com/ros2/rclcpp/issues/3018))
- perf: Optimized out shared\_ptr copies ([#3079](https://github.com/ros2/rclcpp/issues/3079))
- remove default: so that compiler can detect the missing case. ([#3048](https://github.com/ros2/rclcpp/issues/3048))
- Update exception documentation for goal cancellation in ServerGoalHandle ([#3019](https://github.com/ros2/rclcpp/issues/3019))
- Fix REP url locations ([#2987](https://github.com/ros2/rclcpp/issues/2987))
- it misses the iterator second to lock the weakptr. ([#2958](https://github.com/ros2/rclcpp/issues/2958))
- try aborting before canceling 1st on dtor of ServerGoalHandle. ([#2953](https://github.com/ros2/rclcpp/issues/2953))
- deprecate rclcpp::spin\_some and rclcpp::spin\_all ([#2848](https://github.com/ros2/rclcpp/issues/2848))
- fix cmake deprecation ([#2914](https://github.com/ros2/rclcpp/issues/2914))
- Replace std::default\_random\_engine with std::mt19937 (rolling) ([#2843](https://github.com/ros2/rclcpp/issues/2843))
- Added missing chrono includes ([#2854](https://github.com/ros2/rclcpp/issues/2854))
- Contributors: Alberto Soragna, Alejandro Hernández Cordero, Andrei Costinescu, Barry Xu, Emerson Knapp, Janosch Machowinski, Skyler Medeiros, Tim Clephas, Tomoya Fujita, keeponoiro, mosfet80

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_components/CHANGELOG.rst)

- Refactor component containers + Add option for CBG Executor ([#3134](https://github.com/ros2/rclcpp/issues/3134))
- feat: Add per-node log level support via NodeOptions ([#3092](https://github.com/ros2/rclcpp/issues/3092))
- Use new ROSIDL aggregate CMake target ([#3105](https://github.com/ros2/rclcpp/issues/3105))
- Avoid unecessary creation of MultiThreadedExecutor ([#3090](https://github.com/ros2/rclcpp/issues/3090))
- Fix component registering in subdirectories ([#3064](https://github.com/ros2/rclcpp/issues/3064))
- Add library dependency to node executable in rclcpp\_components\_register\_node ([#3047](https://github.com/ros2/rclcpp/issues/3047))
- Updated deprecated ament\_index\_cpp API ([#3011](https://github.com/ros2/rclcpp/issues/3011))
- Fix REP url locations ([#2987](https://github.com/ros2/rclcpp/issues/2987))
- Cleanup the dependencies in rclcpp\_components. ([#2918](https://github.com/ros2/rclcpp/issues/2918))
- fix cmake deprecation ([#2914](https://github.com/ros2/rclcpp/issues/2914))
- NEW PR: Add component\_container for EventsExecutor ([#2885](https://github.com/ros2/rclcpp/issues/2885))
- make sure that plugin arg includes the double colon. ([#2878](https://github.com/ros2/rclcpp/issues/2878))
- set thread names by node in component container isolated ([#2871](https://github.com/ros2/rclcpp/issues/2871))
- Added missing chrono includes ([#2854](https://github.com/ros2/rclcpp/issues/2854))
- Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris Lalancette, Emerson Knapp, Mihir Rao, Peng Wang, Skyler Medeiros, Tim Clephas, Tomoya Fujita, YuJin Hong, mosfet80, pum1k, solo

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_lifecycle/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#3105](https://github.com/ros2/rclcpp/issues/3105))
- Compatiblity with ‘Populate Transitions’ [ros2/rcl#1269](https://github.com/ros2/rcl/issues/1269) ([#2967](https://github.com/ros2/rclcpp/issues/2967))
- add : get clients, servers info ([#2569](https://github.com/ros2/rclcpp/issues/2569))
- Fix REP url locations ([#2987](https://github.com/ros2/rclcpp/issues/2987))
- Add get\_parameter\_or overload returning value or alternative ([#2973](https://github.com/ros2/rclcpp/issues/2973))
- deprecate rclcpp::spin\_some and rclcpp::spin\_all ([#2848](https://github.com/ros2/rclcpp/issues/2848))
- Clearer warning message, the old one lacked information and was perhaps misleading ([#2927](https://github.com/ros2/rclcpp/issues/2927))
- fix cmake deprecation ([#2914](https://github.com/ros2/rclcpp/issues/2914)) cmake version < then 3.10 is deprecated
- Added missing chrono includes ([#2854](https://github.com/ros2/rclcpp/issues/2854))
- introduce rcl\_lifecycle\_get\_transition\_label\_by\_id(). ([#2827](https://github.com/ros2/rclcpp/issues/2827))
- Contributors: Alberto Soragna, Alejandro Hernández Cordero, Emerson Knapp, Jasper van Brakel, Lee, Minju, Peter Mitrano (AR), Tim Clephas, Tomoya Fujita, Zheng Qu, mosfet80

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/lyrical/rclpy/CHANGELOG.rst)

- Feature: async node ([#1620](https://github.com/ros2/rclpy/issues/1620))
- Refactor: moved TypeDescriptionService, LoggingService, ParameterService to BaseNode ([#1645](https://github.com/ros2/rclpy/issues/1645))
- Refactor: base node ([#1637](https://github.com/ros2/rclpy/issues/1637))
- Bugfix: executor doesn’t propagate exception from task that awaited a future ([#1643](https://github.com/ros2/rclpy/issues/1643))
- Fix: disable flaky executor test ([#1648](https://github.com/ros2/rclpy/issues/1648)) ([#1649](https://github.com/ros2/rclpy/issues/1649))
- Streamline entity destroy ([#1629](https://github.com/ros2/rclpy/issues/1629))
- Add acceptable\_buffer\_backends as subscription option in rclpy ([#1628](https://github.com/ros2/rclpy/issues/1628))
- publish\_feedback should effect only on executing state. ([#1639](https://github.com/ros2/rclpy/issues/1639))
- Support to configure feedback subscription content filter for action client ([#1633](https://github.com/ros2/rclpy/issues/1633))
- fix flaky test\_multi\_threaded\_executor\_closes\_threads. ([#1636](https://github.com/ros2/rclpy/issues/1636))
- Fix violation ([#1635](https://github.com/ros2/rclpy/issues/1635))
- Fix test\_executor types ([#1632](https://github.com/ros2/rclpy/issues/1632))
- Refactor: base clock ([#1627](https://github.com/ros2/rclpy/issues/1627))
- Fix future flake8 ([#1634](https://github.com/ros2/rclpy/issues/1634))
- Use new ROSIDL aggregate CMake target ([#1630](https://github.com/ros2/rclpy/issues/1630))
- Update type hints for parameters ([#1631](https://github.com/ros2/rclpy/issues/1631))
- Add support check for content filter feature in subscription ([#1618](https://github.com/ros2/rclpy/issues/1618))
- Refactor: base entity classes ([#1624](https://github.com/ros2/rclpy/issues/1624))
- Fix more test typings and remove unused type aliases ([#1626](https://github.com/ros2/rclpy/issues/1626))
- Add types to test\_waitable ([#1625](https://github.com/ros2/rclpy/issues/1625))
- Correct typos ([#1619](https://github.com/ros2/rclpy/issues/1619))
- Fix incorrect action client/server callback type hints ([#1616](https://github.com/ros2/rclpy/issues/1616))
- avoid stale parameter events in content filter tests. ([#1615](https://github.com/ros2/rclpy/issues/1615))
- fix violations ([#1614](https://github.com/ros2/rclpy/issues/1614))
- Typing Regression Fixes ([#1612](https://github.com/ros2/rclpy/issues/1612))
- CFT is only supported rmw\_fastrtps and rmw\_connextdds. ([#1611](https://github.com/ros2/rclpy/issues/1611))
- Prevents the Future result from being set twice. ([#1599](https://github.com/ros2/rclpy/issues/1599))
- Wrap up ActionClient construction before spining ([#1591](https://github.com/ros2/rclpy/issues/1591))
- Compatiblity with ‘Populate Transitions’ [ros2/rcl#1269](https://github.com/ros2/rcl/issues/1269) ([#1528](https://github.com/ros2/rclpy/issues/1528))
- Drop invalid waitables from wait set ([#1590](https://github.com/ros2/rclpy/issues/1590))
- give some time for the discovery for test\_on\_new\_message\_callback. ([#1585](https://github.com/ros2/rclpy/issues/1585))
- print warning message on owner node if the parameter operation fails. ([#1584](https://github.com/ros2/rclpy/issues/1584))
- Update release version to 10.0.4 ([#1583](https://github.com/ros2/rclpy/issues/1583))
- Update `type_support.py` to use new message abstract base classes ([#1509](https://github.com/ros2/rclpy/issues/1509))
- Fix performance bug in MultiThreadedExecutor (hopefully) ([#1547](https://github.com/ros2/rclpy/issues/1547))
- Expose action graph functions as Node class methods. ([#1574](https://github.com/ros2/rclpy/issues/1574))
- Improve wildcard parsing and optimize the logic for parsing YAML para… ([#1571](https://github.com/ros2/rclpy/issues/1571))
- Improve the compatibility of processing YAML parameter files ([#1548](https://github.com/ros2/rclpy/issues/1548))
- Fix parameter parsing for unspecified target nodes ([#1552](https://github.com/ros2/rclpy/issues/1552))
- Remove default from switch with enum, so that compiler warns. ([#1566](https://github.com/ros2/rclpy/issues/1566))
- Use unconditional wait when possible. ([#1563](https://github.com/ros2/rclpy/issues/1563))
- Increase clock accuracy ([#1564](https://github.com/ros2/rclpy/issues/1564))
- Fix issues with resuming async tasks awaiting a future ([#1469](https://github.com/ros2/rclpy/issues/1469))
- ParameterEventHandler support ContentFiltering ([#1531](https://github.com/ros2/rclpy/issues/1531))
- add : get clients, servers info ([#1307](https://github.com/ros2/rclpy/issues/1307))
- Allow action servers without execute callback ([#1219](https://github.com/ros2/rclpy/issues/1219))
- Remove accidental tuple ([#1542](https://github.com/ros2/rclpy/issues/1542))
- fix(test\_events\_executor): destroy all nodes before shutdown ([#1538](https://github.com/ros2/rclpy/issues/1538))
- Remove duplicate future handling from send\_goal\_async ([#1532](https://github.com/ros2/rclpy/issues/1532))
- remove unused ‘param\_type’ ([#1524](https://github.com/ros2/rclpy/issues/1524))
- Fixes Action.\*\_async futures never complete ([#1308](https://github.com/ros2/rclpy/issues/1308))
- add spinning state for the Executor classes. ([#1510](https://github.com/ros2/rclpy/issues/1510))
- EventsExecutor: Handle async callbacks for services and subscriptions ([#1478](https://github.com/ros2/rclpy/issues/1478))
- Added lock to protect futures for multithreaded executor ([#1477](https://github.com/ros2/rclpy/issues/1477))
- Add content-filtered-topic interfaces ([#1506](https://github.com/ros2/rclpy/issues/1506))
- Fix warnings from gcc. ([#1501](https://github.com/ros2/rclpy/issues/1501))
- Feature: expose event callback setter in subscription, service, client and timer ([#1496](https://github.com/ros2/rclpy/issues/1496))
- Feature: add executor.create\_future() ([#1495](https://github.com/ros2/rclpy/issues/1495))
- Add More Test Typings ([#1472](https://github.com/ros2/rclpy/issues/1472))
- Use pybind11 from deb or pixi ([#1497](https://github.com/ros2/rclpy/issues/1497))
- Do not execute the timer if call\_timer\_with\_info() fails ([#1488](https://github.com/ros2/rclpy/issues/1488))
- Fix msbuild warnings on `operator==` deprecation for pybind11 >=2.2 ([#1483](https://github.com/ros2/rclpy/issues/1483))
- Cleanup the rclpy dependencies. ([#1482](https://github.com/ros2/rclpy/issues/1482))
- Feature: add logger\_name property to subscription, publisher, service and client ([#1471](https://github.com/ros2/rclpy/issues/1471))
- Update `test_node` Types ([#1464](https://github.com/ros2/rclpy/issues/1464))
- Add method that get datetime.datetime from Time ([#1443](https://github.com/ros2/rclpy/issues/1443))
- add `MessageInfo.publisher_gid` ([#1466](https://github.com/ros2/rclpy/issues/1466))
- Add types to `test_action\_\*.py` ([#1444](https://github.com/ros2/rclpy/issues/1444))
- Revert “Fix Duration, Clock, and QoS Docs ([#1428](https://github.com/ros2/rclpy/issues/1428))” ([#1447](https://github.com/ros2/rclpy/issues/1447))
- remove all deprecated classes and methods ([#1456](https://github.com/ros2/rclpy/issues/1456))
- [rclpy] Fix spin() incorrectly removing node from executor if already attached ([#1446](https://github.com/ros2/rclpy/issues/1446))
- Contributors: Alejandro Hernández Cordero, Alon Borenshtein, Auguste Lalande, Barry Xu, Brad Martin, Brennan Miller-Klugman, Błażej Sowa, CY Chen, Chris Lalancette, Christian Rauch, Clara Berendsen, Emerson Knapp, Florian Vahl, Jasper van Brakel, Jean Paul, Jonathan, Lee, Michael Carlstrom, Michael Tandy, Minju, Nadav Elkabets, Nathan Wiebe Neufeldt, Tim Clephas, Tomoya Fujita, Yuyuan Yuan, mhidalgo-rai

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/lyrical/CHANGELOG.rst)

- Updated note related with tl\_expected ([#229](https://github.com/ros2/rcpputils/issues/229))
- Increase test coverage ([#222](https://github.com/ros2/rcpputils/issues/222))
- Append copies of BSD and CC0 licenses from the works ([#223](https://github.com/ros2/rcpputils/issues/223))
- Use std::filesystem in find\_library and add more test ([#221](https://github.com/ros2/rcpputils/issues/221))
- Remove -Werror from Clang compile options ([#220](https://github.com/ros2/rcpputils/issues/220))
- Remove unnecessary dependencies from rcpputils. ([#216](https://github.com/ros2/rcpputils/issues/216)) It doesn’t need to have dependencies on python tests.
- fix cmake deprecation ([#214](https://github.com/ros2/rcpputils/issues/214))
- add thread naming utilities ([#213](https://github.com/ros2/rcpputils/issues/213))
- Removed deprecated path ([#212](https://github.com/ros2/rcpputils/issues/212))
- Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris Lalancette, Tully Foote, William Woodall, mosfet80

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/lyrical/CHANGELOG.rst)

- Add buildtool\_export\_depend on ament\_cmake\_ros\_core ([#558](https://github.com/ros2/rcutils/issues/558))
- fix: typo in parameter documentation for overwrite ([#557](https://github.com/ros2/rcutils/issues/557))
- Remove ATOMIC\_VAR\_INIT ([#556](https://github.com/ros2/rcutils/issues/556))
- Use `ament_set_default_language_standards` from `ament_cmake_core` ([#548](https://github.com/ros2/rcutils/issues/548))
- Use uncommon variable name in macro to avoid being overwritten ([#551](https://github.com/ros2/rcutils/issues/551))
- Remove `ament_export_link_flags()` for atomic operations ([#528](https://github.com/ros2/rcutils/issues/528))
- Use less common variable name in macro ([#550](https://github.com/ros2/rcutils/issues/550))
- Fix missing include for std::get\_time ([#549](https://github.com/ros2/rcutils/issues/549))
- Fix gcc 15.2.1 warning for discarding ‘const’ qualifier ([#547](https://github.com/ros2/rcutils/issues/547))
- Disable warning C5105 for older Windows SDKs in base64.c ([#544](https://github.com/ros2/rcutils/issues/544))
- Add {short\_file\_name} as log format option ([#541](https://github.com/ros2/rcutils/issues/541))
- Add base64 encoding and decoding functions with tests ([#533](https://github.com/ros2/rcutils/issues/533))
- remove default: so that compiler can detect the missing case. ([#534](https://github.com/ros2/rcutils/issues/534))
- Check SIZE\_MAX for array initialization. ([#527](https://github.com/ros2/rcutils/issues/527))
- Do not export dl in rcutils\_LIBRARIES ([#522](https://github.com/ros2/rcutils/issues/522))
- rcutils\_logging\_allocator\_initialize() support. ([#419](https://github.com/ros2/rcutils/issues/419))
- Export -latomic even if BUILD\_TESTING is disabled. ([#516](https://github.com/ros2/rcutils/issues/516))
- Add rcutils\_raw\_steady\_time\_now method for slew-free clock ([#507](https://github.com/ros2/rcutils/issues/507))
- Revert “use getenv\_s instead of getenv for Windows. ([#499](https://github.com/ros2/rcutils/issues/499))” ([#504](https://github.com/ros2/rcutils/issues/504)) This reverts commit 46ab4d4eeb555a2e9e880157b97f0a867d3a256c.
- Hand-code logging\_macros.h ([#502](https://github.com/ros2/rcutils/issues/502))
- Implement rcutils\_strnlen. ([#430](https://github.com/ros2/rcutils/issues/430))
- use getenv\_s instead of getenv for Windows. ([#499](https://github.com/ros2/rcutils/issues/499))
- Make linters happy
- Clean memory in test\_process.cpp ([#495](https://github.com/ros2/rcutils/issues/495))
- Contributors: Alejandro Hernández Cordero, Andrei Kholodnyi, Barry Xu, Chris Lalancette, EddyGharib, Miguel Company, Sai Kishor Kothakota, Shane Loretz, Tomoya Fujita, Tony Najjar

<a id="resource-retriever"></a>

## [resource\_retriever](https://github.com/ros/resource_retriever/tree/lyrical/resource_retriever/CHANGELOG.rst)

- Removed python2 code ([#121](https://github.com/ros/resource_retriever/issues/121))
- Delete resource\_retriever/setup.py ([#120](https://github.com/ros/resource_retriever/issues/120))
- Use get\_package\_share\_path ([#119](https://github.com/ros/resource_retriever/issues/119))
- Updated deprecated ament\_index\_cpp API ([#118](https://github.com/ros/resource_retriever/issues/118))
- removed libcurl\_vendor package ([#116](https://github.com/ros/resource_retriever/issues/116))
- Removed deprecated code ([#113](https://github.com/ros/resource_retriever/issues/113))
- Fixed clang compile error ([#112](https://github.com/ros/resource_retriever/issues/112))
- Removed windows warnings ([#111](https://github.com/ros/resource_retriever/issues/111))
- Add a plugin mechanism to resource\_retriever ([#103](https://github.com/ros/resource_retriever/issues/103))
- uniform MinCMakeVersion ([#108](https://github.com/ros/resource_retriever/issues/108))
- Contributors: Alejandro Hernández Cordero, Michael Carlstrom, Michael Carroll, mosfet80

<a id="resource-retriever-interfaces"></a>

## [resource\_retriever\_interfaces](https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_interfaces/CHANGELOG.rst)

- Update the plugin license ([#17](https://github.com/ros2/resource_retriever_service/issues/17))
- Contributors: Stoyan Gaydarov

<a id="resource-retriever-service"></a>

## [resource\_retriever\_service](https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_service/CHANGELOG.rst)

- Update the plugin license ([#17](https://github.com/ros2/resource_retriever_service/issues/17))
- Contributors: Stoyan Gaydarov

<a id="resource-retriever-service-plugin"></a>

## [resource\_retriever\_service\_plugin](https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_service_plugin/CHANGELOG.rst)

- Update the plugin license ([#17](https://github.com/ros2/resource_retriever_service/issues/17))
- Contributors: Stoyan Gaydarov

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/lyrical/rmw/CHANGELOG.rst)

- find\_package ament\_cmake\_gtest ([#417](https://github.com/ros2/rmw/issues/417))
- Add acceptable\_buffer\_backends field in rmw\_subscription\_options\_s ([#416](https://github.com/ros2/rmw/issues/416))
- Add is\_cft\_supported field to rmw\_subscription\_t for content filtering support ([#415](https://github.com/ros2/rmw/issues/415))
- Remove default from switch with enum, so that compiler warns. ([#414](https://github.com/ros2/rmw/issues/414))
- add: get clients, servers info ([#371](https://github.com/ros2/rmw//issues/371))
- Fix REP url locations ([#406](https://github.com/ros2/rmw//issues/406))
- Update link to rmw API docs ([#405](https://github.com/ros2/rmw//issues/405))
- Don’t assume a DDS-based implementation in function docs ([#402](https://github.com/ros2/rmw//issues/402))
- Contributors: Barry Xu, CY Chen, Christophe Bedard, Lee, Minju, Shane Loretz, Tim Clephas, Tomoya Fujita

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextdds/CHANGELOG.rst)

- fix: Fixed compilation on MSVC 2022 ([#225](https://github.com/ros2/rmw_connextdds/issues/225))
- Remove default from switch with enum to enable compiler warnings ([#216](https://github.com/ros2/rmw_connextdds/issues/216))
- add : get clients,servers info ([#154](https://github.com/ros2/rmw_connextdds/issues/154))
- fix: remove superflous `buildtool_export_depend` ([#206](https://github.com/ros2/rmw_connextdds/issues/206))
- Fix cmake deprecation ([#198](https://github.com/ros2/rmw_connextdds/issues/198))
- Contributors: Bas Zalmstra, Janosch Machowinski, Lee, Minju, Tomoya Fujita, mosfet80

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextdds_common/CHANGELOG.rst)

- Fix content filtering on Windows with modern Connext DDS ([#226](https://github.com/ros2/rmw_connextdds/issues/226)) ([#230](https://github.com/ros2/rmw_connextdds/issues/230))
- fix: Fixed compilation on MSVC 2022 ([#225](https://github.com/ros2/rmw_connextdds/issues/225))
- Add variable `RMW_CONNEXT_USER_TOPICS_PUBLISH_MODE` and deprecate `RMW_CONNEXT_USE_DEFAULT_PUBLISH_MODE` ([#224](https://github.com/ros2/rmw_connextdds/issues/224))
- Update Connext from 7.3.0 to 7.7.0, disable monitoring library by default, and use synchronous publishing mode ([#219](https://github.com/ros2/rmw_connextdds/issues/219))
- Enable property `dds.ros.demangle_topic_and_type_names` to announce demangled topic name as topic alias ([#221](https://github.com/ros2/rmw_connextdds/issues/221))
- Enable content filtering flag ([#223](https://github.com/ros2/rmw_connextdds/issues/223))
- Remove deprecated security properties and use new ones ([#217](https://github.com/ros2/rmw_connextdds/issues/217))
- Remove default from switch with enum to enable compiler warnings ([#216](https://github.com/ros2/rmw_connextdds/issues/216))
- Replace `DDS_ContentFilter_register_filter` with `DDS_DomainParticipant_register_contentfilterI` ([#215](https://github.com/ros2/rmw_connextdds/issues/215))
- Remove superfluous `buildtool_export_depend` ([#210](https://github.com/ros2/rmw_connextdds/issues/210))
- add : get clients,servers info ([#154](https://github.com/ros2/rmw_connextdds/issues/154))
- [rmw\_connextdds\_common]: Remove <member\_of\_group>rosidl\_interface\_packages ([#202](https://github.com/ros2/rmw_connextdds/issues/202))
- Correctly calculate the size of a serialized key ([#200](https://github.com/ros2/rmw_connextdds/issues/200))
- Fix cmake deprecation ([#198](https://github.com/ros2/rmw_connextdds/issues/198))
- Fixed serialized minimum sample size callback ([#196](https://github.com/ros2/rmw_connextdds/issues/196))
- Removed warning ([#187](https://github.com/ros2/rmw_connextdds/issues/187))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Francisco Gallego Salido, Janosch Machowinski, Lee, Minju, Tomoya Fujita, mergify[bot], mosfet80

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextddsmicro/CHANGELOG.rst)

- fix: Fixed compilation on MSVC 2022 ([#225](https://github.com/ros2/rmw_connextdds/issues/225))
- Remove default from switch with enum to enable compiler warnings ([#216](https://github.com/ros2/rmw_connextdds/issues/216))
- Remove superfluous `buildtool_export_depend` ([#210](https://github.com/ros2/rmw_connextdds/issues/210))
- add : get clients,servers info ([#154](https://github.com/ros2/rmw_connextdds/issues/154))
- Fix cmake deprecation ([#198](https://github.com/ros2/rmw_connextdds/issues/198))
- Contributors: Janosch Machowinski, Lee, Minju, Tomoya Fujita, mosfet80

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/lyrical/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Silence unused variable warning in Release builds ([#580](https://github.com/ros2/rmw_cyclonedds/issues/580))
- Add key support and update Cyclone DDS compatibility ([#575](https://github.com/ros2/rmw_cyclonedds/issues/575))
- Explicitly disable content filtering support ([#574](https://github.com/ros2/rmw_cyclonedds/issues/574))
- Add tracepoint to `rmw_take_loan_int` ([#566](https://github.com/ros2/rmw_cyclonedds/issues/566))
- Fix warnings about `may be used uninitialized` ([#573](https://github.com/ros2/rmw_cyclonedds/issues/573))
- Improve MessageTypeSupport performance ([#562](https://github.com/ros2/rmw_cyclonedds/issues/562))
- Improve serialization performance by optimizing `dynamic_cast` usage and replacing virtual functions with templates ([#553](https://github.com/ros2/rmw_cyclonedds/issues/553))
- Remove defaults to trigger proper warnings ([#549](https://github.com/ros2/rmw_cyclonedds/issues/549))
- add : get clients, servers info ([#499](https://github.com/ros2/rmw_cyclonedds/issues/499))
- Do not include rosidl\_typesupport\_{c,cpp} in rmw impl typesupport list ([#544](https://github.com/ros2/rmw_cyclonedds/issues/544))
- Update CMake requirement ([#539](https://github.com/ros2/rmw_cyclonedds/issues/539))
- Contributors: Brandon Simoncic, Christophe Bedard, Janosch Machowinski, Lee, Minju, Oren Bell PhD, Shane Loretz, Tomoya Fujita, eboasson, mosfet80

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/lyrical/rmw_dds_common/CHANGELOG.rst)

- If no publishers discovered, make the best available QoS for subscription. ([#84](https://github.com/ros2/rmw_dds_common/issues/84))
- Add get\_clients\_info\_by\_service and get\_servers\_info\_by\_service; introduce ServiceEntityInfo to handle service type hash in graph cache ([#82](https://github.com/ros2/rmw_dds_common/issues/82))
- Remove deprecated GraphCache methods without type hash ([#83](https://github.com/ros2/rmw_dds_common/issues/83))
- Update cmake requirements ([#80](https://github.com/ros2/rmw_dds_common/issues/80))
- Remove deprecated security utilities ([#79](https://github.com/ros2/rmw_dds_common/issues/79))
- Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee, Minju, Tomoya Fujita, mosfet80

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_cpp/CHANGELOG.rst)

- Clean up logs for the rosidl::Buffer path ([#886](https://github.com/ros2/rmw_fastrtps//issues/886)) ([#887](https://github.com/ros2/rmw_fastrtps//issues/887))
- Change the buffer-aware BUFBE: -> bufbe. (backport [#880](https://github.com/ros2/rmw_fastrtps//issues/880)) ([#884](https://github.com/ros2/rmw_fastrtps//issues/884))
- Fix UB in accessing the keys ([#879](https://github.com/ros2/rmw_fastrtps//issues/879)) ([#882](https://github.com/ros2/rmw_fastrtps//issues/882))
- Remove warning when compiling with `lcang` ([#876](https://github.com/ros2/rmw_fastrtps/issues/876))
- Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867](https://github.com/ros2/rmw_fastrtps/issues/867))
- Use new aggregate rosidl target instead of \_TARGETS ([#870](https://github.com/ros2/rmw_fastrtps/issues/870))
- Enable content filtering flag ([#869](https://github.com/ros2/rmw_fastrtps/issues/869))
- fix: remove superflous buildtool\_export\_depend. ([#852](https://github.com/ros2/rmw_fastrtps/issues/852))
- add : get clients, servers info ([#771](https://github.com/ros2/rmw_fastrtps/issues/771))
- Do not include rosidl\_typesupport\_{c,cpp} in rmw impl typesupport list ([#843](https://github.com/ros2/rmw_fastrtps/issues/843))
- fix cmake deprecation ([#831](https://github.com/ros2/rmw_fastrtps/issues/831))
- Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Barry Xu, CY Chen, Christophe Bedard, Lee, Minju, Tomoya Fujita, mergify[bot], mosfet80

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Fix UB in accessing the keys ([#879](https://github.com/ros2/rmw_fastrtps//issues/879)) ([#882](https://github.com/ros2/rmw_fastrtps//issues/882))
- Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867](https://github.com/ros2/rmw_fastrtps/issues/867))
- Use new aggregate rosidl target instead of \_TARGETS ([#870](https://github.com/ros2/rmw_fastrtps/issues/870))
- fix: remove superflous buildtool\_export\_depend. ([#852](https://github.com/ros2/rmw_fastrtps/issues/852))
- add : get clients, servers info ([#771](https://github.com/ros2/rmw_fastrtps/issues/771))
- Do not include rosidl\_typesupport\_{c,cpp} in rmw impl typesupport list ([#843](https://github.com/ros2/rmw_fastrtps/issues/843))
- Check remaining size before resizing sequences ([#827](https://github.com/ros2/rmw_fastrtps/issues/827))
- fix cmake deprecation ([#831](https://github.com/ros2/rmw_fastrtps/issues/831))
- Contributors: Alexis Tsogias, CY Chen, Christophe Bedard, Lee, Miguel Company, Minju, Tomoya Fujita, mergify[bot], mosfet80

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Change the buffer-aware BUFBE: -> bufbe. (backport [#880](https://github.com/ros2/rmw_fastrtps//issues/880)) ([#884](https://github.com/ros2/rmw_fastrtps//issues/884))
- feat: set collection header element\_flags TryConstructFailAction::DISCARD instead of 0 ([#875](https://github.com/ros2/rmw_fastrtps/issues/875))
- Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867](https://github.com/ros2/rmw_fastrtps/issues/867))
- Added rmw\_take tracepoint, because it wasn’t being triggered for successful takes ([#871](https://github.com/ros2/rmw_fastrtps/issues/871))
- Added tracepoint to loaned take ([#868](https://github.com/ros2/rmw_fastrtps/issues/868))
- fix: remove superflous buildtool\_export\_depend. ([#852](https://github.com/ros2/rmw_fastrtps/issues/852))
- add : get clients, servers info ([#771](https://github.com/ros2/rmw_fastrtps/issues/771))
- Refs [#23861](https://github.com/ros2/rmw_fastrtps/issues/23861). Use key annotation in TypeObject build ([#849](https://github.com/ros2/rmw_fastrtps/issues/849))
- fix cmake deprecation ([#831](https://github.com/ros2/rmw_fastrtps/issues/831))
- Retrieve `HistoryQoS` in discovery when available ([#829](https://github.com/ros2/rmw_fastrtps/issues/829))
- check a local publication to ignore with serialized message. ([#823](https://github.com/ros2/rmw_fastrtps/issues/823))
- Contributors: CY Chen, Daisuke Nishimatsu, Lee, Mario Domínguez López, Miguel Company, Minju, Oren Bell, Oren Bell PhD, Tomoya Fujita, mergify[bot], mosfet80

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/lyrical/rmw_implementation/CHANGELOG.rst)

- Add rmw\_zenoh\_cpp as a build dependency ([#273](https://github.com/ros2/rmw_implementation/issues/273))
- Updated deprecated ament\_index\_cpp API ([#272](https://github.com/ros2/rmw_implementation/issues/272))
- Add rmw\_get\_clients\_info\_by\_service , rmw\_servers\_clients\_info\_by\_service ([#238](https://github.com/ros2/rmw_implementation/issues/238))
- fix cmake deprecation ([#267](https://github.com/ros2/rmw_implementation/issues/267))
- Explain rosidl\_typesupport\_{c,cpp} in rmw impl typesupport list ([#265](https://github.com/ros2/rmw_implementation/issues/265))
- Fixed windows warning ([#254](https://github.com/ros2/rmw_implementation/issues/254))
- Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee, Minju, Tony Najjar, mosfet80

<a id="rmw-test-fixture"></a>

## [rmw\_test\_fixture](https://github.com/ros2/ament_cmake_ros/tree/lyrical/rmw_test_fixture/CHANGELOG.rst)

- Add missing dependency from rmw\_test\_fixture to rmw ([#53](https://github.com/ros2/ament_cmake_ros/issues/53))
- add find\_package call ([#50](https://github.com/ros2/ament_cmake_ros/issues/50))
- fix cmake deprecation ([#47](https://github.com/ros2/ament_cmake_ros/issues/47))
- Contributors: Matt Condino, Scott K Logan, mosfet80

<a id="rmw-test-fixture-implementation"></a>

## [rmw\_test\_fixture\_implementation](https://github.com/ros2/ament_cmake_ros/tree/lyrical/rmw_test_fixture_implementation/CHANGELOG.rst)

- Block signals during Python environment reload in rmw\_test\_fixture\_implementation ([#64](https://github.com/ros2/ament_cmake_ros/issues/64))
- Add `ament_ros_defaults` target ([#62](https://github.com/ros2/ament_cmake_ros/issues/62))
- Drop dependency group dependency on test fixtures ([#60](https://github.com/ros2/ament_cmake_ros/issues/60))
- Restore ROS\_DOMAIN\_ID after isolation is finished ([#58](https://github.com/ros2/ament_cmake_ros/issues/58))
- default to c++17 due to use of newer methods on std::map ([#55](https://github.com/ros2/ament_cmake_ros/issues/55))
- fix cmake deprecation ([#47](https://github.com/ros2/ament_cmake_ros/issues/47))
- On start-after-stop, re-check RMW\_IMPLEMENTATION for changes ([#46](https://github.com/ros2/ament_cmake_ros/issues/46))
- Choose random domain IDs during default RMW isolation ([#39](https://github.com/ros2/ament_cmake_ros/issues/39))
- Ignore SIGINT *after* child process has been spawned ([#45](https://github.com/ros2/ament_cmake_ros/issues/45))
- Add some smoke tests for rmw\_test\_fixture\_implementation ([#42](https://github.com/ros2/ament_cmake_ros/issues/42))
- Copy all environment variables explicitly ([#43](https://github.com/ros2/ament_cmake_ros/issues/43))
- Split the generator expression for each library ([#36](https://github.com/ros2/ament_cmake_ros/issues/36))
- Removed clang warnings ([#34](https://github.com/ros2/ament_cmake_ros/issues/34))
- Contributors: Alejandro Hernández Cordero, Michael Carlstrom, Michael Carroll, Scott K Logan, Tanishq Chaudhary, William Woodall, mosfet80

<a id="rmw-zenoh-cpp"></a>

## [rmw\_zenoh\_cpp](https://github.com/ros2/rmw_zenoh/tree/lyrical/rmw_zenoh_cpp/CHANGELOG.rst)

- Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve synchronization with `undeclare` ([#964](https://github.com/ros2/rmw_zenoh/issues/964))
- Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0 ([#960](https://github.com/ros2/rmw_zenoh/issues/960))
- Prevent deadlock by not holding both locks when processing event data ([#937](https://github.com/ros2/rmw_zenoh/issues/937))
- Bump zenoh to 1.8.0 ([#935](https://github.com/ros2/rmw_zenoh/issues/935))
- Explicitly set `false` for the content filtering feature ([#938](https://github.com/ros2/rmw_zenoh/issues/938))
- Add deadline/liveliness QoS events to `rmw_zenoh_cpp` ([#934](https://github.com/ros2/rmw_zenoh/issues/934))
- Catch `PackageNotFoundError` during default config URI loading to prevent crash ([#915](https://github.com/ros2/rmw_zenoh/issues/915))
- Populate `reception_sequence_number` and `advertise_sequence_number` features ([#920](https://github.com/ros2/rmw_zenoh/issues/920))
- Use `get_package_share_path` ([#913](https://github.com/ros2/rmw_zenoh/issues/913))
- Address outstanding TODO items ([#896](https://github.com/ros2/rmw_zenoh/issues/896))
- Expose zenoh session ([#865](https://github.com/ros2/rmw_zenoh/issues/865))
- Fix config loading with incorrect path variable ([#898](https://github.com/ros2/rmw_zenoh/issues/898))
- Fix build binary workflow ([#895](https://github.com/ros2/rmw_zenoh/issues/895))
- Fix line ending in session open error message ([#888](https://github.com/ros2/rmw_zenoh/issues/888))
- Update deprecated `ament_index_cpp` API ([#879](https://github.com/ros2/rmw_zenoh/issues/879))
- Remove `default` from switch with enum to enable compiler warnings ([#871](https://github.com/ros2/rmw_zenoh/issues/871))
- Use shared SHM transport provider instead of creating a new instance ([#857](https://github.com/ros2/rmw_zenoh/issues/857))
- Bump `zenoh` to 1.7.1 ([#870](https://github.com/ros2/rmw_zenoh/issues/870))
- Add rmw\_get\_clients\_info\_by\_service and rmw\_get\_servers\_info\_by\_service ([#679](https://github.com/ros2/rmw_zenoh/issues/679))
- Fix REP url locations ([#858](https://github.com/ros2/rmw_zenoh/issues/858))
- Restore ZENOH\_CONFIG\_OVERRIDE after isolation is finished ([#855](https://github.com/ros2/rmw_zenoh/issues/855))
- Fix typo in ‘triggered’ ([#844](https://github.com/ros2/rmw_zenoh/issues/844))
- Log details at SHM creation (alloc and threashold sizes) ([#835](https://github.com/ros2/rmw_zenoh/issues/835))
- Change default value of ZENOH\_SHM\_ALLOC\_SIZE to 48 MiB ([#830](https://github.com/ros2/rmw_zenoh/issues/830))
- config: increase queries\_default\_timeout to 10min ([#820](https://github.com/ros2/rmw_zenoh/issues/820))
- Fix compile with clang ([#819](https://github.com/ros2/rmw_zenoh/issues/819))
- feat(logging): add contextual information to log messages ([#809](https://github.com/ros2/rmw_zenoh/issues/809))
- Align the config with upstream Zenoh. ([#785](https://github.com/ros2/rmw_zenoh/issues/785))
- fix: resolve memory leak when publishing with the default allocator ([#797](https://github.com/ros2/rmw_zenoh/issues/797))
- Recycle serialization buffers on transmission ([#342](https://github.com/ros2/rmw_zenoh/issues/342))
- refactor: avoid redundant key expression creation when replying ([#732](https://github.com/ros2/rmw_zenoh/issues/732))
- Do not include rosidl\_typesupport\_{c,cpp} in rmw impl typesupport list ([#748](https://github.com/ros2/rmw_zenoh/issues/748))
- fixing typo flow to flows in config files ([#740](https://github.com/ros2/rmw_zenoh/issues/740))
- Shared Memory on C++ API ([#363](https://github.com/ros2/rmw_zenoh/issues/363))
- Bump Zenoh to v1.5.0 ([#728](https://github.com/ros2/rmw_zenoh/issues/728))
- rmw\_zenoh\_cpp: Include algorithm for std::find\_if ([#723](https://github.com/ros2/rmw_zenoh/issues/723))
- Use rfind to avoid issues with service types ending in Request or Response ([#719](https://github.com/ros2/rmw_zenoh/issues/719))
- Remove the extra copy on the publisher side ([#711](https://github.com/ros2/rmw_zenoh/issues/711))
- Avoid ambiguity with variable shadowing ([#706](https://github.com/ros2/rmw_zenoh/issues/706))
- Only configure the timeout of the action-related service `get_result` to maximum value. ([#685](https://github.com/ros2/rmw_zenoh/issues/685))
- Use Zenoh Querier to replace Session.get ([#694](https://github.com/ros2/rmw_zenoh/issues/694))
- Use data() to avoid potentially dereferencing an empty vector ([#667](https://github.com/ros2/rmw_zenoh/issues/667))
- Bump Zenoh to 1.4.0 ([#652](https://github.com/ros2/rmw_zenoh/issues/652))
- fix(comment): correct the QoS incompatibilities ([#644](https://github.com/ros2/rmw_zenoh/issues/644))
- fix rmw\_take\_serialized\_message. ([#638](https://github.com/ros2/rmw_zenoh/issues/638))
- Update CMakeLists.txt ([#617](https://github.com/ros2/rmw_zenoh/issues/617))
- Contributors: Alejandro Hernandez Cordero, Alejandro Hernández Cordero, ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard, Faseel Chemmadan, Filip, Hervé Audren, Jan Vermaete, Julien Enoch, Lee, Mahmoud Mazouz, Minju, Nikola Banović, Scott K Logan, Shane Loretz, Skyler Medeiros, Steven Palma, Tim Clephas, Tomoya Fujita, Yadunund, Yuyuan Yuan, jordanburklund, milidam, mosfet80, yadunund, yellowhatter, Øystein Sture

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/lyrical/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#246](https://github.com/ros/robot_state_publisher/issues/246))
- Improvements ([#245](https://github.com/ros/robot_state_publisher/issues/245))
- Update subscription callback signatures ([#241](https://github.com/ros/robot_state_publisher/issues/241))
- Add functionality to read description from a topic instead of a parameter ([#234](https://github.com/ros/robot_state_publisher/issues/234))
- Removed tf2\_ros warning ([#239](https://github.com/ros/robot_state_publisher/issues/239))
- fix cmake deprecation ([#232](https://github.com/ros/robot_state_publisher/issues/232))
- Removed tf2\_ros warning ([#238](https://github.com/ros/robot_state_publisher/issues/238))
- Removed orocos kdl vendor dependency ([#237](https://github.com/ros/robot_state_publisher/issues/237))
- Removed warnings in geometry2 ([#236](https://github.com/ros/robot_state_publisher/issues/236))
- Replace deprecated tf2\_ros headers ([#235](https://github.com/ros/robot_state_publisher/issues/235))
- Removed deprecated command-line argument ([#233](https://github.com/ros/robot_state_publisher/issues/233))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Kenji Brameld (TRACLabs), Maurice Alexander Purnawan, mosfet80

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/lyrical/ros2action/CHANGELOG.rst)

- Fix `flake8` ([#1215](https://github.com/ros2/ros2cli/issues/1215))
- Add timeout arguments to `ros2 service call`, `ros2 action send_goal`, `ros2 component`, `ros2 lifecycle`, and `ros2 param` ([#1185](https://github.com/ros2/ros2cli/issues/1185))
- add osrf\_pycommon depend for test\_exec. ([#1120](https://github.com/ros2/ros2cli/issues/1120))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- fix ros2action send\_goal signal handling. ([#1072](https://github.com/ros2/ros2cli/issues/1072))
- Fujitatomoya/ros2 action send goal timeout ([#1067](https://github.com/ros2/ros2cli/issues/1067))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Relax the check from exact to partial match. ([#1055](https://github.com/ros2/ros2cli/issues/1055))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- move QoS methods from ros2topic.api to ros2cli.qos. ([#1053](https://github.com/ros2/ros2cli/issues/1053))
- remove unnecessary ‘/’ from ros2 action info. ([#1049](https://github.com/ros2/ros2cli/issues/1049))
- add QoS option to ros2service/ros2action echo commands. ([#1036](https://github.com/ros2/ros2cli/issues/1036))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Support ‘ros2 action echo’ ([#978](https://github.com/ros2/ros2cli/issues/978))
- Correct the license content ([#979](https://github.com/ros2/ros2cli/issues/979))
- Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mosfet80

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/lyrical/ros2bag/CHANGELOG.rst)

- Add `--repeat-all-transient-local` flag for automatic transient-local topic detection ([#2391](https://github.com/ros2/rosbag2/issues/2391))
- Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387](https://github.com/ros2/rosbag2/issues/2387))
- Suppress multi-threaded process warning from rosbag2 flake8 ([#2329](https://github.com/ros2/rosbag2/issues/2329))
- Remove deprecated arguments and options from `ros2bag` ([#2328](https://github.com/ros2/rosbag2/issues/2328))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Improve `ros2 bag convert` performance for fragment cutting and add `--input-options` ([#2325](https://github.com/ros2/rosbag2/issues/2325))
- Add static topics feature for recorder ([#2319](https://github.com/ros2/rosbag2/issues/2319))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Add `rosbag2_storage_default_plugins` to `exec_depend` of `ros2bag` ([#2227](https://github.com/ros2/rosbag2/issues/2227))
- Add `input_serialization_format` and `output_serialization_format` to `RecordOptions`, deprecating `rmw_serialization_format` ([#2215](https://github.com/ros2/rosbag2/issues/2215))
- Publish messages lost statistics to ‘events/messages\_lost’ topic ([#2150](https://github.com/ros2/rosbag2/issues/2150))
- Expose more of the player and recorder API to Python, and improve signal handling ([#2062](https://github.com/ros2/rosbag2/issues/2062))
- Fix setuptools deprecations ([#2087](https://github.com/ros2/rosbag2/issues/2087))
- Refactor Python player and recorder APIs into classes ([#2047](https://github.com/ros2/rosbag2/issues/2047))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Contributors: Christophe Bedard, Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, mosfet80

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/lyrical/ros2cli/CHANGELOG.rst)

- Add RMW isolation fixture to enable discovery for `rmw_zenoh_cpp` tests ([#1216](https://github.com/ros2/ros2cli/issues/1216))
- Add support for fish ([#1211](https://github.com/ros2/ros2cli/issues/1211))
- Fix `flake8` ([#1215](https://github.com/ros2/ros2cli/issues/1215))
- Fix future flake8 regressions ([#1196](https://github.com/ros2/ros2cli//issues/1196))
- fix deprecated warning for action graph APIs. ([#1188](https://github.com/ros2/ros2cli//issues/1188))
- Enable always complete ([#1190](https://github.com/ros2/ros2cli//issues/1190))
- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- check for invalid ROS discovery configuration and print warning if ne… ([#1178](https://github.com/ros2/ros2cli//issues/1178))
- skip history and depth check for rmw\_connextdds. ([#1064](https://github.com/ros2/ros2cli/issues/1064))
- Remove importlib packages ([#1117](https://github.com/ros2/ros2cli/issues/1117))
- add verbose in service-info verb ([#916](https://github.com/ros2/ros2cli//issues/916))
- Fix handling of empty ROS\_DOMAIN\_ID in ros2cli ([#1112](https://github.com/ros2/ros2cli//issues/1112))
- fix: Also catch a TimeoutError ([#1092](https://github.com/ros2/ros2cli/issues/1092))
- [ros2doctor] Add Action Report ([#1076](https://github.com/ros2/ros2cli/issues/1076))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Add Service report similar to topic report ([#1059](https://github.com/ros2/ros2cli/issues/1059))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- move QoS methods from ros2topic.api to ros2cli.qos. ([#1053](https://github.com/ros2/ros2cli/issues/1053))
- Assert HistoryQoS in test\_ros2cli\_daemon ([#1040](https://github.com/ros2/ros2cli/issues/1040))
- remove add\_subparsers from ros2cli. ([#1032](https://github.com/ros2/ros2cli/issues/1032))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Contributors: Christophe Bedard, David V. Lu!!, Kaju-Bubanja, Lee, Mario Domínguez López, Michael Carlstrom, Michael Carroll, Minju, SPeak, Scott K Logan, Tomoya Fujita, Tony Najjar, Yuyuan Yuan, mosfet80

<a id="ros2cli-common-extensions"></a>

## [ros2cli\_common\_extensions](https://github.com/ros2/ros2cli_common_extensions/tree/lyrical/ros2cli_common_extensions/CHANGELOG.rst)

- Add dependency on ros2plugin in package.xml ([#13](https://github.com/ros2/ros2cli_common_extensions/issues/13))
- Update CMakeLists.txt ([#11](https://github.com/ros2/ros2cli_common_extensions/issues/11))
- Contributors: Maurice Alexander Purnawan, mosfet80

<a id="ros2cli-test-interfaces"></a>

## [ros2cli\_test\_interfaces](https://github.com/ros2/ros2cli/tree/lyrical/ros2cli_test_interfaces/CHANGELOG.rst)

- fix cmake deprecation ([#1082](https://github.com/ros2/ros2cli/issues/1082))
- Contributors: mosfet80

<a id="ros2component"></a>

## [ros2component](https://github.com/ros2/ros2cli/tree/lyrical/ros2component/CHANGELOG.rst)

- Fix `flake8` ([#1215](https://github.com/ros2/ros2cli/issues/1215))
- Add timeout arguments to `ros2 service call`, `ros2 action send_goal`, `ros2 component`, `ros2 lifecycle`, and `ros2 param` ([#1185](https://github.com/ros2/ros2cli/issues/1185))
- Fix future flake8 regressions ([#1196](https://github.com/ros2/ros2cli//issues/1196))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita, mosfet80

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/lyrical/ros2doctor/CHANGELOG.rst)

- Fix future flake8 regressions ([#1196](https://github.com/ros2/ros2cli//issues/1196))
- Remove importlib packages ([#1117](https://github.com/ros2/ros2cli/issues/1117))
- Harden ros2doctor system calls. ([#1118](https://github.com/ros2/ros2cli/issues/1118))
- Add error handling when parsing package locally ([#1108](https://github.com/ros2/ros2cli//issues/1108))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- [ros2doctor] Environment Report ([#1045](https://github.com/ros2/ros2cli/issues/1045))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- add warning notice for ros2 doctor –report. ([#1079](https://github.com/ros2/ros2cli/issues/1079))
- [ros2doctor] Add Action Report ([#1076](https://github.com/ros2/ros2cli/issues/1076))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Add Service report similar to topic report ([#1059](https://github.com/ros2/ros2cli/issues/1059))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Fix stringifying InterfaceFlags when the flags are empty. ([#1026](https://github.com/ros2/ros2cli/issues/1026))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Skip QoS compatibility test on Zenoh ([#985](https://github.com/ros2/ros2cli/issues/985))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mini-1235, mosfet80

<a id="ros2interface"></a>

## [ros2interface](https://github.com/ros2/ros2cli/tree/lyrical/ros2interface/CHANGELOG.rst)

- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Contributors: Christophe Bedard, Michael Carlstrom, Tony Najjar, mosfet80

<a id="ros2launch"></a>

## [ros2launch](https://github.com/ros2/launch_ros/tree/lyrical/ros2launch/CHANGELOG.rst)

- correct typos ([#524](https://github.com/ros2/launch_ros//issues/524))
- fix setuptools deprecations ([#475](https://github.com/ros2/launch_ros/issues/475))
- user control of log file base names, in ros2 launch ([#461](https://github.com/ros2/launch_ros/issues/461)) Co-authored-by: Katherine Scott <[katherineAScott@gmail.com](mailto:katherineAScott%40gmail.com)>
- Contributors: Auguste Lalande, Tanishq Chaudhary, mosfet80

<a id="ros2lifecycle"></a>

## [ros2lifecycle](https://github.com/ros2/ros2cli/tree/lyrical/ros2lifecycle/CHANGELOG.rst)

- Add timeout arguments to `ros2 service call`, `ros2 action send_goal`, `ros2 component`, `ros2 lifecycle`, and `ros2 param` ([#1185](https://github.com/ros2/ros2cli/issues/1185))
- ros2interface output the contents for each node. ([#1163](https://github.com/ros2/ros2cli//issues/1163))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Relax the check from exact to partial match. ([#1055](https://github.com/ros2/ros2cli/issues/1055))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mosfet80

<a id="ros2lifecycle-test-fixtures"></a>

## [ros2lifecycle\_test\_fixtures](https://github.com/ros2/ros2cli/tree/lyrical/ros2lifecycle_test_fixtures/CHANGELOG.rst)

- fix cmake deprecation ([#1082](https://github.com/ros2/ros2cli/issues/1082))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#973](https://github.com/ros2/ros2cli/issues/973))
- Contributors: Shane Loretz, mosfet80

<a id="ros2multicast"></a>

## [ros2multicast](https://github.com/ros2/ros2cli/tree/lyrical/ros2multicast/CHANGELOG.rst)

- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Contributors: Christophe Bedard, Michael Carlstrom, mosfet80

<a id="ros2node"></a>

## [ros2node](https://github.com/ros2/ros2cli/tree/lyrical/ros2node/CHANGELOG.rst)

- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/lyrical/ros2param/CHANGELOG.rst)

- Add timeout arguments to `ros2 service call`, `ros2 action send_goal`, `ros2 component`, `ros2 lifecycle`, and `ros2 param` ([#1185](https://github.com/ros2/ros2cli/issues/1185))
- ros2 param set /node\_name <param1 value1 param2 value2…> support. ([#1204](https://github.com/ros2/ros2cli//issues/1204))
- ros2 param get /node\_name <param1 param2 param3…> support. ([#1203](https://github.com/ros2/ros2cli//issues/1203))
- Add per-node timeout option to ros2 param list ([#1170](https://github.com/ros2/ros2cli//issues/1170))
- Fix Bash completion ([#1182](https://github.com/ros2/ros2cli//issues/1182))
- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- Support “ros2 param get <parameter>” across all nodes. ([#1174](https://github.com/ros2/ros2cli//issues/1174))
- Fix ParameterNameCompleter. ([#1172](https://github.com/ros2/ros2cli//issues/1172))
- Output node parameters upon each receipt ([#1162](https://github.com/ros2/ros2cli//issues/1162))
- skip test\_verb\_load\_wildcard for rmw\_connextdds. ([#1150](https://github.com/ros2/ros2cli/issues/1150))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Relax the check from exact to partial match. ([#1055](https://github.com/ros2/ros2cli/issues/1055))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- fix misspelling. ([#1035](https://github.com/ros2/ros2cli/issues/1035))
- catch ConnectionRefusedError, so that it can fall back to DirectNode. ([#1014](https://github.com/ros2/ros2cli/issues/1014))
- fails the test properly to avoid TypeError exception. ([#1016](https://github.com/ros2/ros2cli/issues/1016))
- Fix loading parameter behavior from yaml file ([#864](https://github.com/ros2/ros2cli/issues/864))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Taiga Arai, Tomoya Fujita, Tony Najjar, mosfet80

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/lyrical/ros2pkg/CHANGELOG.rst)

- Remove “rclrs” duplicate dependency ([#1197](https://github.com/ros2/ros2cli//issues/1197))
- Fix future flake8 regressions ([#1196](https://github.com/ros2/ros2cli//issues/1196))
- Add Native ROS2 Rust Package Create Capability ([#1107](https://github.com/ros2/ros2cli/issues/1107))
- Remove importlib packages ([#1117](https://github.com/ros2/ros2cli/issues/1117))
- add mypy ([#1109](https://github.com/ros2/ros2cli//issues/1109))
- fix cmake deprecation ([#1082](https://github.com/ros2/ros2cli/issues/1082))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Reduce boilerplate in install(TARGETS for library ([#1056](https://github.com/ros2/ros2cli/issues/1056))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Use modern C++17 syntax. ([#982](https://github.com/ros2/ros2cli/issues/982))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#973](https://github.com/ros2/ros2cli/issues/973))
- Try to use the git global user.name for maintainer-name ([#968](https://github.com/ros2/ros2cli/issues/968))
- Update minimum CMake version CMakeLists.txt.em ([#969](https://github.com/ros2/ros2cli/issues/969))
- Contributors: Bartlomiej Styczen, Christophe Bedard, Larry Gezelius, Michael Carlstrom, Parth Patel, Sebastian Castro, Shane Loretz, Shynur, Silvio Traversaro, mosfet80

<a id="ros2plugin"></a>

## [ros2plugin](https://github.com/ros/pluginlib/tree/lyrical/ros2plugin/CHANGELOG.rst)

- Implement package option ([#293](https://github.com/ros/pluginlib/issues/293))
- Improve logging when unable to parse the plugin ([#285](https://github.com/ros/pluginlib/issues/285))
- Add ros2plugin ([#165](https://github.com/ros/pluginlib/issues/165))
- Contributors: Alejandro Hernández Cordero, Jeremie Deray, mini-1235

<a id="ros2run"></a>

## [ros2run](https://github.com/ros2/ros2cli/tree/lyrical/ros2run/CHANGELOG.rst)

- Fix Bash completion ([#1182](https://github.com/ros2/ros2cli//issues/1182))
- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- Add signal handler SIGIN/SIGTERM to ros2run ([#899](https://github.com/ros2/ros2cli/issues/899))
- Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita, Tony Najjar, mosfet80

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/lyrical/ros2service/CHANGELOG.rst)

- Add timeout arguments to `ros2 service call`, `ros2 action send_goal`, `ros2 component`, `ros2 lifecycle`, and `ros2 param` ([#1185](https://github.com/ros2/ros2cli/issues/1185))
- Fix Bash completion ([#1182](https://github.com/ros2/ros2cli//issues/1182))
- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- add verbose in service-info verb ([#916](https://github.com/ros2/ros2cli//issues/916))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Relax the check from exact to partial match. ([#1055](https://github.com/ros2/ros2cli/issues/1055))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- move QoS methods from ros2topic.api to ros2cli.qos. ([#1053](https://github.com/ros2/ros2cli/issues/1053))
- add QoS option to ros2service/ros2action echo commands. ([#1036](https://github.com/ros2/ros2cli/issues/1036))
- Use `get_service` in `ros2service call` ([#994](https://github.com/ros2/ros2cli/issues/994))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Support QoS options for `ros2 service call` ([#966](https://github.com/ros2/ros2cli/issues/966))
- Contributors: Christophe Bedard, Lee, Michael Carlstrom, Michael Carroll, Minju, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80

<a id="ros2test"></a>

## [ros2test](https://github.com/ros2/ros_testing/tree/lyrical/ros2test/CHANGELOG.rst)

- fix setuptools deprecations ([#16](https://github.com/ros2/ros_testing/issues/16))
- Contributors: mosfet80

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/lyrical/ros2topic/CHANGELOG.rst)

- Improve test isolation and suppress Connext license noise ([#1225](https://github.com/ros2/ros2cli/issues/1225))
- Add fzf-based interactive selection to ros2cli commands ([#1151](https://github.com/ros2/ros2cli//issues/1151))
- add “–all/-a” option to “ros2 topic bw” with screen refresh. ([#1130](https://github.com/ros2/ros2cli/issues/1130))
- return explicitly from internal functions. ([#1128](https://github.com/ros2/ros2cli/issues/1128))
- support multiple topics for “ros2 topic bw”. ([#1124](https://github.com/ros2/ros2cli/issues/1124))
- add “–all/-a” option to “ros2 topic hz” with screen refresh. ([#1122](https://github.com/ros2/ros2cli/issues/1122))
- Fujitatomoya/clearup isolated ros2daemon ([#1098](https://github.com/ros2/ros2cli/issues/1098))
- wait for the publisher before test command is executed. ([#1094](https://github.com/ros2/ros2cli/issues/1094))
- Enable test isolation on a few remaining ros2topic tests ([#1087](https://github.com/ros2/ros2cli/issues/1087))
- Restore environment variables after launch tests ([#1086](https://github.com/ros2/ros2cli/issues/1086))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#1062](https://github.com/ros2/ros2cli/issues/1062))
- fix setuptools deprecations ([#1066](https://github.com/ros2/ros2cli/issues/1066))
- Make sure to install py.typed files ([#1058](https://github.com/ros2/ros2cli/issues/1058))
- Export Typing information ([#1041](https://github.com/ros2/ros2cli/issues/1041))
- move QoS methods from ros2topic.api to ros2cli.qos. ([#1053](https://github.com/ros2/ros2cli/issues/1053))
- Custom Completion Finder for fetching topic prototype ([#995](https://github.com/ros2/ros2cli/issues/995))
- Documented now and auto keywords ([#1008](https://github.com/ros2/ros2cli/issues/1008))
- Conditional deserialization of message for `ros2 topic hz` ([#1005](https://github.com/ros2/ros2cli/issues/1005))
- Enable `ros2 topic echo` with entries of array fields ([#996](https://github.com/ros2/ros2cli/issues/996))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Adapt tests to Zenoh ([#988](https://github.com/ros2/ros2cli/issues/988))
- Adjust topic hz and bw command description ([#987](https://github.com/ros2/ros2cli/issues/987))
- Add support for topic QOS for ros2topic bw, delay and hz ([#935](https://github.com/ros2/ros2cli/issues/935))
- Start the simulation from 1 second for the test ([#975](https://github.com/ros2/ros2cli/issues/975))
- Support QoS options for `ros2 service call` ([#966](https://github.com/ros2/ros2cli/issues/966))
- Support ros2 topic pub yaml file input ([#925](https://github.com/ros2/ros2cli/issues/925))
- Contributors: Alejandro Hernández Cordero, Anthony Welte, Christophe Bedard, Fabian Thomsen, Florencia, Kostubh Khandelwal, Leander Stephen D’Souza, Martin Pecka, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80, nomumu

<a id="ros2trace"></a>

## [ros2trace](https://github.com/ros2/ros2_tracing/tree/lyrical/ros2trace/CHANGELOG.rst)

- Ignore A0005 ([#237](https://github.com/ros2/ros2_tracing/issues/237))
- Update trace command’s doc-string ([#213](https://github.com/ros2/ros2_tracing/issues/213))
- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- Add support for starting tracing at runtime ([#191](https://github.com/ros2/ros2_tracing/issues/191))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Contributors: Christophe Bedard, Michael Carlstrom, Shravan Deva, mosfet80

<a id="ros-environment"></a>

## [ros\_environment](https://github.com/ros/ros_environment/tree/lyrical/CHANGELOG.rst)

- Change default ROS\_DISTRO from ‘rolling’ to ‘lyrical’
- fix cmake deprecation ([#42](https://github.com/ros/ros_environment/issues/42))
- Remove CODEOWNERS. ([#40](https://github.com/ros/ros_environment/issues/40))
- Contributors: Chris Lalancette, Shane Loretz, mosfet80

<a id="ros-testing"></a>

## [ros\_testing](https://github.com/ros2/ros_testing/tree/lyrical/ros_testing/CHANGELOG.rst)

- fix cmake deprecation ([#17](https://github.com/ros2/ros_testing/issues/17))
- Contributors: mosfet80

<a id="rosbag2"></a>

## [rosbag2](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2/CHANGELOG.rst)

- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Contributors: mosfet80

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_compression/CHANGELOG.rst)

- Add validation for empty file path in compression process ([#2398](https://github.com/ros2/rosbag2/issues/2398))
- Fix a possible race condition in compression writer on close ([#2362](https://github.com/ros2/rosbag2/issues/2362))
- Update Rosbag2 filename format to `index+name+timestamp` ([#2265](https://github.com/ros2/rosbag2/issues/2265))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Make topics persistent between writer’s close() and open() API calls ([#2229](https://github.com/ros2/rosbag2/issues/2229))
- Address recorder test flakiness by increasing cache size ([#2203](https://github.com/ros2/rosbag2/issues/2203))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Add message loss statistics callbacks and logging ([#2039](https://github.com/ros2/rosbag2/issues/2039))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Bugfix: `ros2 bag convert` dropping messages with compression mode message ([#1975](https://github.com/ros2/rosbag2/issues/1975))
- Contributors: Daisuke Sato, DangitBen, Luke Sy, Michael Orlov, mosfet80

<a id="rosbag2-compression-zstd"></a>

## [rosbag2\_compression\_zstd](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_compression_zstd/CHANGELOG.rst)

- Replace `zstd_vendor` with `zstd_cmake_module` ([#2166](https://github.com/ros2/rosbag2/issues/2166))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_cpp/CHANGELOG.rst)

- Removed clang warning ([#2404](https://github.com/ros2/rosbag2/issues/2404))
- Implement `transient-local topic` repetition for Writer API and split/snapshot integration ([#2386](https://github.com/ros2/rosbag2/issues/2386))
- Add `TransientLocalMessagesCache` and `RecordOptions` for repeating transient-local topics ([#2385](https://github.com/ros2/rosbag2/issues/2385))
- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Fix a possible race condition in compression writer on close ([#2362](https://github.com/ros2/rosbag2/issues/2362))
- Fix incorrect serialization format in metadata ([#2372](https://github.com/ros2/rosbag2/issues/2372))
- Update Rosbag2 filename format to `index+name+timestamp` ([#2265](https://github.com/ros2/rosbag2/issues/2265))
- Support relative includes for IDL in local message definition ([#2241](https://github.com/ros2/rosbag2/issues/2241))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Workaround flaky `bagsize_split_is_at_least_specified_size` test ([#2311](https://github.com/ros2/rosbag2/issues/2311))
- Incorporate upstream minor fixes from Apex.AI ([#2240](https://github.com/ros2/rosbag2/issues/2240))
- Update deprecated ament\_index\_cpp API ([#2268](https://github.com/ros2/rosbag2/issues/2268))
- Make topics persistent between writer’s close() and open() API calls ([#2229](https://github.com/ros2/rosbag2/issues/2229))
- Add nullptr check when pushing new messages to the message cache ([#2219](https://github.com/ros2/rosbag2/issues/2219))
- Address recorder test flakiness by increasing cache size ([#2203](https://github.com/ros2/rosbag2/issues/2203))
- Log reasoning for not found message definition only in debug log ([#2183](https://github.com/ros2/rosbag2/issues/2183))
- Improve error handling in rosbag2\_cpp with null checks and exception throwing ([#2127](https://github.com/ros2/rosbag2/issues/2127))
- Add null pointer checks in `Reader` constructor and `open()` method ([#2135](https://github.com/ros2/rosbag2/issues/2135))
- Use `rclcpp typesupport helpers` in `rosbag2_cpp` ([#2017](https://github.com/ros2/rosbag2/issues/2017))
- Fix callback not called for MESSAGES\_LOST event ([#2105](https://github.com/ros2/rosbag2/issues/2105))
- Improve recorder’s MessageCache performance ([#2104](https://github.com/ros2/rosbag2/issues/2104))
- Fix reindex duration bug when bag file durations overlap ([#2036](https://github.com/ros2/rosbag2/issues/2036))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Add support for searching message definitions in nested subdirectories ([#2055](https://github.com/ros2/rosbag2/issues/2055))
- Add message loss statistics callbacks and logging ([#2039](https://github.com/ros2/rosbag2/issues/2039))
- Use cache to determine action interface inner types ([#2052](https://github.com/ros2/rosbag2/issues/2052))
- Fix service/action message definition issue ([#2041](https://github.com/ros2/rosbag2/issues/2041))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Improve message publishing timing by avoiding sporadic wakeups and fixing incorrect intervals on player start ([#2025](https://github.com/ros2/rosbag2/issues/2025))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Address clang warning in the `TimeControllerClock::wakeup()` ([#1962](https://github.com/ros2/rosbag2/issues/1962))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Chui Vanfleet, Daisuke Sato, Emerson Knapp, Hunter L. Allen, José Faria, Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, YuJin Hong, mosfet80

<a id="rosbag2-examples-cpp"></a>

## [rosbag2\_examples\_cpp](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Update subscription callback signatures ([#2225](https://github.com/ros2/rosbag2/issues/2225))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Add examples for compressing bag files ([#1956](https://github.com/ros2/rosbag2/issues/1956))
- Contributors: Emerson Knapp, Maxime Fleury, mini-1235, mosfet80

<a id="rosbag2-examples-py"></a>

## [rosbag2\_examples\_py](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst)

- Fix setuptools deprecation by removing `tests_require` ([#2092](https://github.com/ros2/rosbag2/issues/2092))
- Add examples for compressing bag files ([#1956](https://github.com/ros2/rosbag2/issues/1956))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Add a simple example showing how to convert bags to the csv file ([#1974](https://github.com/ros2/rosbag2/issues/1974))
- Contributors: Christophe Bedard, Maxime Fleury, Michael Orlov, mosfet80

<a id="rosbag2-interfaces"></a>

## [rosbag2\_interfaces](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_interfaces/CHANGELOG.rst)

- Add support for time based Resume service ([#2357](https://github.com/ros2/rosbag2/issues/2357))
- Allow pause/resume service calls while not in recording ([#2349](https://github.com/ros2/rosbag2/issues/2349))
- Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330](https://github.com/ros2/rosbag2/issues/2330))
- Add error return code to the `~/stop` service request ([#2312](https://github.com/ros2/rosbag2/issues/2312))
- Add Record, Stop, StartDiscovery, StopDiscovery, and IsDiscoveryRunning services for Recorder ([#2248](https://github.com/ros2/rosbag2/issues/2248))
- Publish messages lost statistics to ‘events/messages\_lost’ topic ([#2150](https://github.com/ros2/rosbag2/issues/2150))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Contributors: Michael Orlov, carlos-apex, mosfet80

<a id="rosbag2-performance-benchmarking"></a>

## [rosbag2\_performance\_benchmarking](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Remove unnecessary dependencies on `yaml_cpp_vendor` ([#2353](https://github.com/ros2/rosbag2/issues/2353))
- Fix warning by initializing `number_of_threads` ([#2121](https://github.com/ros2/rosbag2/issues/2121))
- Enable `rosbag2_performance_benchmarking` package to be built by default ([#2093](https://github.com/ros2/rosbag2/issues/2093))
- Fix performance benchmarking data generation and environment variable handling ([#2078](https://github.com/ros2/rosbag2/issues/2078))
- Fix failure in `benchmark_launch` when calling `Process.wait()` twice ([#2076](https://github.com/ros2/rosbag2/issues/2076))
- Fix incorrect results from `prosbag2_performance_benchmarking` for high-frequency topics ([#2077](https://github.com/ros2/rosbag2/issues/2077))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Contributors: Chris Lalancette, Christophe Bedard, Cristóbal Arroyo, Emerson Knapp, Michael Orlov, mosfet80

<a id="rosbag2-performance-benchmarking-msgs"></a>

## [rosbag2\_performance\_benchmarking\_msgs](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_performance/rosbag2_performance_benchmarking_msgs/CHANGELOG.rst)

- Enable `rosbag2_performance_benchmarking` package to be built by default ([#2093](https://github.com/ros2/rosbag2/issues/2093))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Contributors: Michael Orlov, mosfet80

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_py/CHANGELOG.rst)

- Add `--repeat-all-transient-local` flag for automatic transient-local topic detection ([#2391](https://github.com/ros2/rosbag2/issues/2391))
- Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387](https://github.com/ros2/rosbag2/issues/2387))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Move to `build_depend` ([#2332](https://github.com/ros2/rosbag2/issues/2332))
- Improve `ros2 bag convert` performance for fragment cutting and add `--input-options` ([#2325](https://github.com/ros2/rosbag2/issues/2325))
- Add static topics feature for recorder ([#2319](https://github.com/ros2/rosbag2/issues/2319))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Incorporate upstream minor fixes from Apex.AI ([#2240](https://github.com/ros2/rosbag2/issues/2240))
- Add `input_serialization_format` and `output_serialization_format` to `RecordOptions`, deprecating `rmw_serialization_format` ([#2215](https://github.com/ros2/rosbag2/issues/2215))
- Use pybind11 from deb or pixi ([#2154](https://github.com/ros2/rosbag2/issues/2154))
- Publish messages lost statistics to ‘events/messages\_lost’ topic ([#2150](https://github.com/ros2/rosbag2/issues/2150))
- Ensure test topic discovery by recorder in `rosbag2_py` test ([#2132](https://github.com/ros2/rosbag2/issues/2132))
- Fix CMake list append for env vars in rosbag2\_py with clang ([#2116](https://github.com/ros2/rosbag2/issues/2116))
- Add public API for player’s starting time and playback duration ([#2095](https://github.com/ros2/rosbag2/issues/2095))
- Expose more of the player and recorder API to Python, and improve signal handling ([#2062](https://github.com/ros2/rosbag2/issues/2062))
- Add `send_timestamp` to Python interface for reading serialized messages ([#2061](https://github.com/ros2/rosbag2/issues/2061))
- Refactor Python player and recorder APIs into classes ([#2047](https://github.com/ros2/rosbag2/issues/2047))
- Fix service/action message definition issue ([#2041](https://github.com/ros2/rosbag2/issues/2041))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Bugfix: `ros2 bag convert` dropping messages with compression mode message ([#1975](https://github.com/ros2/rosbag2/issues/1975))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, DangitBen, Luke Sy, Michael Carlstrom, Michael Orlov, Om Shivam Verma, Tony Najjar

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage/CHANGELOG.rst)

- Add `TransientLocalMessagesCache` and `RecordOptions` for repeating transient-local topics ([#2385](https://github.com/ros2/rosbag2/issues/2385))
- Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330](https://github.com/ros2/rosbag2/issues/2330))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Improve `ros2 bag convert` performance for fragment cutting and add `--input-options` ([#2325](https://github.com/ros2/rosbag2/issues/2325))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Throw `YAML::Exception` during conversion if the data type mismatches ([#2262](https://github.com/ros2/rosbag2/issues/2262))
- Fix decoder and encode mismatch in YAML deserialization ([#2277](https://github.com/ros2/rosbag2/issues/2277))
- Incorporate upstream minor fixes from Apex.AI ([#2240](https://github.com/ros2/rosbag2/issues/2240))
- Fix memory leak on `make_empty_serialized_message()` ([#2253](https://github.com/ros2/rosbag2/issues/2253))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Fix undefined behavior in the `rosbag2_storage` and `rosbag2_storage_sqlite3` packages ([#1997](https://github.com/ros2/rosbag2/issues/1997))
- Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960](https://github.com/ros2/rosbag2/issues/1960))
- Contributors: Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, carlos-apex, mosfet80

<a id="rosbag2-storage-default-plugins"></a>

## [rosbag2\_storage\_default\_plugins](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_default_plugins/CHANGELOG.rst)

- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Contributors: mosfet80

<a id="rosbag2-storage-mcap"></a>

## [rosbag2\_storage\_mcap](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_mcap/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Remove unnecessary dependencies on `yaml_cpp_vendor` ([#2353](https://github.com/ros2/rosbag2/issues/2353))
- Fix MCAPStorage::seek(time) to advance when timestamp matches current time ([#2157](https://github.com/ros2/rosbag2/issues/2157))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Update `index.ros.org/p/` links for `rosbag2_storage_mcap` ([#2034](https://github.com/ros2/rosbag2/issues/2034))
- Contributors: Chris Lalancette, Christophe Bedard, Emerson Knapp, Michael Orlov, mosfet80

<a id="rosbag2-storage-sqlite3"></a>

## [rosbag2\_storage\_sqlite3](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_sqlite3/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Fix vulnerable string concatenation by using parameterized queries ([#2290](https://github.com/ros2/rosbag2/issues/2290))
- Remove sqlite3\_vendor ([#2164](https://github.com/ros2/rosbag2/issues/2164))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Fix undefined behavior in the `rosbag2_storage` and `rosbag2_storage_sqlite3` packages ([#1997](https://github.com/ros2/rosbag2/issues/1997))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Contributors: Alejandro Hernández Cordero, Christophe Bedard, Emerson Knapp, Luke Sy, Michael Orlov, Tomoya Fujita, mosfet80

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_test_common/CHANGELOG.rst)

- Reduce flakiness in rosbag2 recorder end-to-end tests ([#2370](https://github.com/ros2/rosbag2/issues/2370))
- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Update Rosbag2 filename format to `index+name+timestamp` ([#2265](https://github.com/ros2/rosbag2/issues/2265))
- Update subscription callback signatures ([#2225](https://github.com/ros2/rosbag2/issues/2225))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Address test flakiness by waiting for executor spin ([#2001](https://github.com/ros2/rosbag2/issues/2001))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960](https://github.com/ros2/rosbag2/issues/1960))
- Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp, Michael Orlov, mini-1235, mosfet80

<a id="rosbag2-test-msgdefs"></a>

## [rosbag2\_test\_msgdefs](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_test_msgdefs/CHANGELOG.rst)

- Support relative includes for IDL in local message definition ([#2241](https://github.com/ros2/rosbag2/issues/2241))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Add support for searching message definitions in nested subdirectories ([#2055](https://github.com/ros2/rosbag2/issues/2055))
- Contributors: Hunter L. Allen, Michael Orlov, mosfet80

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_tests/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Update Rosbag2 filename format to `index+name+timestamp` ([#2265](https://github.com/ros2/rosbag2/issues/2265))
- Add static topics feature for recorder ([#2319](https://github.com/ros2/rosbag2/issues/2319))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Workaround flaky `bagsize_split_is_at_least_specified_size` test ([#2311](https://github.com/ros2/rosbag2/issues/2311))
- Add `input_serialization_format` and `output_serialization_format` to `RecordOptions`, deprecating `rmw_serialization_format` ([#2215](https://github.com/ros2/rosbag2/issues/2215))
- Address recorder test flakiness by increasing cache size ([#2203](https://github.com/ros2/rosbag2/issues/2203))
- Use `rclcpp typesupport helpers` in `rosbag2_cpp` ([#2017](https://github.com/ros2/rosbag2/issues/2017))
- Expose more of the player and recorder API to Python, and improve signal handling ([#2062](https://github.com/ros2/rosbag2/issues/2062))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Fix deadlocks in Rosbag2 player when calling stop API ([#2057](https://github.com/ros2/rosbag2/issues/2057))
- Introduce new `BaseWriteInterface` methods `write_messages` and `write_message` to provide operation status, deprecating old write APIs ([#2030](https://github.com/ros2/rosbag2/issues/2030))
- Address test flakiness by waiting for executor spin ([#2001](https://github.com/ros2/rosbag2/issues/2001))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp, Michael Orlov, mosfet80

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_transport/CHANGELOG.rst)

- Apply /bigobj to all MSVC builds in rosbag2\_transport ([#2424](https://github.com/ros2/rosbag2/issues/2424)) ([#2428](https://github.com/ros2/rosbag2/issues/2428))
- fix: Fixed compile errors in rosbag2\_transport for MSVC 2022 and C++20 ([#2407](https://github.com/ros2/rosbag2/issues/2407))
- Fix QoS overrides ignored when topic name has no leading slash ([#2394](https://github.com/ros2/rosbag2/issues/2394))
- Refactor transient-local topic detection and logging in RecorderImpl ([#2395](https://github.com/ros2/rosbag2/issues/2395))
- Fix race condition in `RecordSrvsSimTimeTest` by waiting for clock subscriber ([#2396](https://github.com/ros2/rosbag2/issues/2396))
- Add `--repeat-all-transient-local` flag for automatic transient-local topic detection ([#2391](https://github.com/ros2/rosbag2/issues/2391))
- Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387](https://github.com/ros2/rosbag2/issues/2387))
- Implement `transient-local topic` repetition for Writer API and split/snapshot integration ([#2386](https://github.com/ros2/rosbag2/issues/2386))
- Add `TransientLocalMessagesCache` and `RecordOptions` for repeating transient-local topics ([#2385](https://github.com/ros2/rosbag2/issues/2385))
- Use new ROSIDL aggregate CMake target ([#2384](https://github.com/ros2/rosbag2/issues/2384))
- Address flakiness in the `rosbag2_transport::test_record_services` tests ([#2368](https://github.com/ros2/rosbag2/issues/2368))
- Add support for time based Resume service ([#2357](https://github.com/ros2/rosbag2/issues/2357))
- Address race condition in the `wait_for_playback_to_start()` function ([#2344](https://github.com/ros2/rosbag2/issues/2344))
- Add `set_on_start_recording_callback()` to set the callback for when recording starts ([#2340](https://github.com/ros2/rosbag2/issues/2340))
- Remove unnecessary dependencies on `yaml_cpp_vendor` ([#2353](https://github.com/ros2/rosbag2/issues/2353))
- Allow pause/resume service calls while not in recording ([#2349](https://github.com/ros2/rosbag2/issues/2349))
- Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330](https://github.com/ros2/rosbag2/issues/2330))
- Update Rosbag2 filename format to `index+name+timestamp` ([#2265](https://github.com/ros2/rosbag2/issues/2265))
- Address a possible deadlock in `seek(timestamp)` ([#2345](https://github.com/ros2/rosbag2/issues/2345))
- Add missing fields to `RecordOptions` YAML encode/decode functions and include a compile-time safeguard ([#2334](https://github.com/ros2/rosbag2/issues/2334))
- Implement circular logging by split count (`--max-bag-files`) ([#2218](https://github.com/ros2/rosbag2/issues/2218))
- Improve `ros2 bag convert` performance for fragment cutting and add `--input-options` ([#2325](https://github.com/ros2/rosbag2/issues/2325))
- Add static topics feature for recorder ([#2319](https://github.com/ros2/rosbag2/issues/2319))
- Add `--max-cache-duration` option for time-bounded snapshots ([#2289](https://github.com/ros2/rosbag2/issues/2289))
- Fix the flaky `can_record_again_after_stop` test ([#2313](https://github.com/ros2/rosbag2/issues/2313))
- Add error return code to the `~/stop` service request ([#2312](https://github.com/ros2/rosbag2/issues/2312))
- Add Record, Stop, StartDiscovery, StopDiscovery, and IsDiscoveryRunning services for Recorder ([#2248](https://github.com/ros2/rosbag2/issues/2248))
- Use QoS override settings for inner Rosbag2 publishing topics ([#2286](https://github.com/ros2/rosbag2/issues/2286))
- Fix decoder and encode mismatch in YAML deserialization ([#2277](https://github.com/ros2/rosbag2/issues/2277))
- Incorporate upstream minor fixes from Apex.AI ([#2240](https://github.com/ros2/rosbag2/issues/2240))
- Fix macOS build: Disable thread-safety annotations in `locked_priority_queue.hpp` ([#2245](https://github.com/ros2/rosbag2/issues/2245))
- Fix C++ Recorder failure when stop() then record() are called with the same bag name ([#2224](https://github.com/ros2/rosbag2/issues/2224))
- Add a direct API for `rosbag2_transport::Recorder` ([#2221](https://github.com/ros2/rosbag2/issues/2221))
- Add `input_serialization_format` and `output_serialization_format` to `RecordOptions`, deprecating `rmw_serialization_format` ([#2215](https://github.com/ros2/rosbag2/issues/2215))
- Enable RMW communication isolation in rosbag2\_transport tests ([#2190](https://github.com/ros2/rosbag2/issues/2190))
- Add topic name and type delimiter for hash map keys to avoid collisions ([#2210](https://github.com/ros2/rosbag2/issues/2210))
- Add cache for `TopicFilter` to avoid performance burden on discovery ([#1486](https://github.com/ros2/rosbag2/issues/1486))
- Address recorder test flakiness by increasing cache size ([#2203](https://github.com/ros2/rosbag2/issues/2203))
- Reduce CPU overhead in Rosbag2 recorder discovery by improving discovery logic ([#2201](https://github.com/ros2/rosbag2/issues/2201))
- Fix data races in `PlayerProgressBar` using atomic variables ([#2194](https://github.com/ros2/rosbag2/issues/2194))
- Fix data races in tests with `MockSequentialWriter` ([#2192](https://github.com/ros2/rosbag2/issues/2192))
- Player now respects original message order for same timestamps ([#2172](https://github.com/ros2/rosbag2/issues/2172))
- Return player storage options by value in `get_storage_options()` to avoid dangling reference ([#2181](https://github.com/ros2/rosbag2/issues/2181))
- Fix player not playing when `read_ahead_queue_size` equals 1 ([#2174](https://github.com/ros2/rosbag2/issues/2174))
- Fix multiple race conditions and a deadlock in the player ([#2171](https://github.com/ros2/rosbag2/issues/2171))
- Fix multibag replay stagnation and improve playback performance by managing chronological message order with `ReadersManager` ([#2158](https://github.com/ros2/rosbag2/issues/2158))
- Fix MCAPStorage::seek(time) to advance when timestamp matches current time ([#2157](https://github.com/ros2/rosbag2/issues/2157))
- Publish messages lost statistics to ‘events/messages\_lost’ topic ([#2150](https://github.com/ros2/rosbag2/issues/2150))
- Add `RecorderEventNotifier` class ([#2144](https://github.com/ros2/rosbag2/issues/2144))
- Resolve deadlock during multibag replay and update `wait_for_playback_to_start` ([#2143](https://github.com/ros2/rosbag2/issues/2143))
- Use `rclcpp typesupport helpers` in `rosbag2_cpp` ([#2017](https://github.com/ros2/rosbag2/issues/2017))
- Fix callback not called for MESSAGES\_LOST event ([#2105](https://github.com/ros2/rosbag2/issues/2105))
- Add public API for player’s starting time and playback duration ([#2095](https://github.com/ros2/rosbag2/issues/2095))
- Fix CMAKE deprecation ([#2067](https://github.com/ros2/rosbag2/issues/2067))
- Fix deadlocks in Rosbag2 player when calling stop API ([#2057](https://github.com/ros2/rosbag2/issues/2057))
- Add message loss statistics callbacks and logging ([#2039](https://github.com/ros2/rosbag2/issues/2039))
- Skip flaky `can_record_again_after_stop` test ([#2031](https://github.com/ros2/rosbag2/issues/2031))
- Fix `cout` output when progress bar is disabled ([#2024](https://github.com/ros2/rosbag2/issues/2024))
- Improve message publishing timing by avoiding sporadic wakeups and fixing incorrect intervals on player start ([#2025](https://github.com/ros2/rosbag2/issues/2025))
- Fix `playing_respects_delay` test flakiness ([#2016](https://github.com/ros2/rosbag2/issues/2016))
- Address test flakiness by waiting for executor spin ([#2001](https://github.com/ros2/rosbag2/issues/2001))
- Avoid sending non-existent cancel requests ([#2005](https://github.com/ros2/rosbag2/issues/2005))
- Fix a maybe-uninitialized warning in player\_action\_client.cpp ([#1969](https://github.com/ros2/rosbag2/issues/1969))
- Upstream quality changes from Apex.AI part-2 ([#1924](https://github.com/ros2/rosbag2/issues/1924))
- Bugfix: `ros2 bag convert` dropping messages with compression mode message ([#1975](https://github.com/ros2/rosbag2/issues/1975))
- Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960](https://github.com/ros2/rosbag2/issues/1960))
- Contributors: Barry Xu, Chris Lalancette, Christophe Bedard, Daisuke Sato, DangitBen, Dhruv Patel, Emerson Knapp, Janosch Machowinski, Luke Sy, Michael Carroll, Michael Orlov, Sahil Lakhmani, Scott K Logan, Shane Loretz, Tomoya Fujita, Tony Najjar, baranbologur, carlos-apex, mergify[bot], mosfet80

<a id="rosgraph-msgs"></a>

## [rosgraph\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/rosgraph_msgs/CHANGELOG.rst)

- Actually build the new graph description messages ([#192](https://github.com/ros2/rcl_interfaces/issues/192)) ([#198](https://github.com/ros2/rcl_interfaces/issues/198))
- Add Graph description messages to `rosgraph_msgs` ([#188](https://github.com/ros2/rcl_interfaces/issues/188))
- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: Emerson Knapp, mergify[bot], mosfet80

<a id="rosidl-adapter"></a>

## [rosidl\_adapter](https://github.com/ros2/rosidl/tree/lyrical/rosidl_adapter/CHANGELOG.rst)

- Fix future regressions on flake8 ([#936](https://github.com/ros2/rosidl//issues/936))
- Fix @optional for string literals ([#905](https://github.com/ros2/rosidl/issues/905))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Add Optional Parsing ([#883](https://github.com/ros2/rosidl/issues/883))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- Contributors: Michael Carlstrom, mosfet80

<a id="rosidl-buffer"></a>

## [rosidl\_buffer](https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer/CHANGELOG.rst)

- Add missing std::vector compatible APIs to rosidl::Buffer ([#959](https://github.com/ros2/rosidl/issues/959))
- Bump rosidl\_buffer min CMake version ([#956](https://github.com/ros2/rosidl/issues/956))
- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Add cstdint include to c\_helpers.cpp ([#953](https://github.com/ros2/rosidl/issues/953))
- Add rosidl\_buffer and rosidl\_buffer\_backend for native Buffer type support ([#941](https://github.com/ros2/rosidl/issues/941))
- Contributors: CY Chen, Shane Loretz, mosfet80

<a id="rosidl-buffer-backend"></a>

## [rosidl\_buffer\_backend](https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_backend/CHANGELOG.rst)

- Clarify return of get\_descriptor\_type\_support() ([#958](https://github.com/ros2/rosidl/issues/958))
- Bump rosidl\_buffer min CMake version ([#956](https://github.com/ros2/rosidl/issues/956))
- Add rosidl\_buffer and rosidl\_buffer\_backend for native Buffer type support ([#941](https://github.com/ros2/rosidl/issues/941))
- Contributors: CY Chen, Shane Loretz

<a id="rosidl-buffer-backend-registry"></a>

## [rosidl\_buffer\_backend\_registry](https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_backend_registry/CHANGELOG.rst)

- Add missing ament\_cmake\_gtest dep ([#960](https://github.com/ros2/rosidl/issues/960))
- Bump rosidl\_buffer min CMake version ([#956](https://github.com/ros2/rosidl/issues/956))
- Add rosidl\_buffer\_backend\_registry ([#944](https://github.com/ros2/rosidl/issues/944))
- Contributors: CY Chen, Scott K Logan, Shane Loretz

<a id="rosidl-buffer-py"></a>

## [rosidl\_buffer\_py](https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_py/CHANGELOG.rst)

- Bump rosidl\_buffer min CMake version ([#956](https://github.com/ros2/rosidl/issues/956))
- Fix pybind11 rosdep key ([#955](https://github.com/ros2/rosidl/issues/955))
- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Contributors: CY Chen, Christoph Fröhlich, Shane Loretz

<a id="rosidl-cli"></a>

## [rosidl\_cli](https://github.com/ros2/rosidl/tree/lyrical/rosidl_cli/CHANGELOG.rst)

- Fix future regressions on flake8 ([#936](https://github.com/ros2/rosidl//issues/936))
- remove importlib-metadata ([#917](https://github.com/ros2/rosidl/issues/917))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- fix setuptools deprecations ([#877](https://github.com/ros2/rosidl/issues/877))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Contributors: Francisco Rossi, Michael Carlstrom, mosfet80

<a id="rosidl-cmake"></a>

## [rosidl\_cmake](https://github.com/ros2/rosidl/tree/lyrical/rosidl_cmake/CHANGELOG.rst)

- Install interface files to same folder as idl ([#935](https://github.com/ros2/rosidl/issues/935))
- Create an aggregate target for rosidl generated interfaces targets ([#947](https://github.com/ros2/rosidl//issues/947))
- Add `rosidl_auto_generate_interfaces` function ([#918](https://github.com/ros2/rosidl/issues/918))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- remove deprecated rosidl\_target\_interfaces. ([#898](https://github.com/ros2/rosidl/issues/898))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Contributors: Emerson Knapp, Kotaro Yoshimoto, Michael Carlstrom, Tim Wendt, Tomoya Fujita, mosfet80

<a id="rosidl-core-generators"></a>

## [rosidl\_core\_generators](https://github.com/ros2/rosidl_core/tree/lyrical/rosidl_core_generators/CHANGELOG.rst)

- Revert “Revert “Added rosidl\_generator\_rs ([#7](https://github.com/ros2/rosidl_core/issues/7))” ([#8](https://github.com/ros2/rosidl_core/issues/8))” ([#9](https://github.com/ros2/rosidl_core/issues/9))
- fix cmake deprecation ([#10](https://github.com/ros2/rosidl_core/issues/10))
- Contributors: Esteve Fernandez, mosfet80

<a id="rosidl-core-runtime"></a>

## [rosidl\_core\_runtime](https://github.com/ros2/rosidl_core/tree/lyrical/rosidl_core_runtime/CHANGELOG.rst)

- Add rosidl\_buffer\_py as build\_export\_depend with explicit group resolution ([#14](https://github.com/ros2/rosidl_core/issues/14))
- fix cmake deprecation ([#10](https://github.com/ros2/rosidl_core/issues/10))
- Contributors: CY Chen, mosfet80

<a id="rosidl-default-generators"></a>

## [rosidl\_default\_generators](https://github.com/ros2/rosidl_defaults/tree/lyrical/rosidl_default_generators/CHANGELOG.rst)

- fix cmake deprecation ([#31](https://github.com/ros2/rosidl_defaults/issues/31))
- Contributors: mosfet80

<a id="rosidl-default-runtime"></a>

## [rosidl\_default\_runtime](https://github.com/ros2/rosidl_defaults/tree/lyrical/rosidl_default_runtime/CHANGELOG.rst)

- fix cmake deprecation ([#31](https://github.com/ros2/rosidl_defaults/issues/31))
- Contributors: mosfet80

<a id="rosidl-dynamic-typesupport"></a>

## [rosidl\_dynamic\_typesupport](https://github.com/ros2/rosidl_dynamic_typesupport/tree/lyrical/CHANGELOG.rst)

- Don’t automatically enable verbose makefiles ([#17](https://github.com/ros2/rosidl_dynamic_typesupport/issues/17))
- Contributors: Chris Lalancette

<a id="rosidl-dynamic-typesupport-fastrtps"></a>

## [rosidl\_dynamic\_typesupport\_fastrtps](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/tree/lyrical/CHANGELOG.rst)

- Merge pull request [#11](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/11) from mosfet80/patch-1
- Don’t automatically enable verbose makefiles. ([#9](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/9))
- Contributors: Chris Lalancette, mosfet80

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_c/CHANGELOG.rst)

- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Contributors: Francisco Rossi, Michael Carlstrom, mosfet80

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_cpp/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Use IWYU pragma export to avoid clangd warnings for generated headers ([#902](https://github.com/ros2/rosidl//issues/902))
- rosidl\_generator\_cpp: constexpr message traits and to\_tuple\_ref for generated structs ([#928](https://github.com/ros2/rosidl//issues/928))
- Make `data_type` and `name` traits constexpr ([#929](https://github.com/ros2/rosidl//issues/929))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Add static\_cast ([#884](https://github.com/ros2/rosidl/issues/884))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Add missing cstdint include ([#864](https://github.com/ros2/rosidl/issues/864))
- Removed deprecated methods ([#863](https://github.com/ros2/rosidl/issues/863))
- Contributors: Adam Leeper, Alejandro Hernández Cordero, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80, Øystein Sture

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/lyrical/rosidl_generator_dds_idl/CHANGELOG.rst)

- Update cmake version requirements ([#64](https://github.com/ros2/rosidl_dds/issues/64))
- Contributors: mosfet80

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/lyrical/rosidl_generator_py/CHANGELOG.rst)

- Use absolute names for type hints ([#258](https://github.com/ros2/rosidl_python/issues/258))
- Feature: add depends flag for ament\_python\_install\_package ([#254](https://github.com/ros2/rosidl_python/issues/254))
- Add support for rosidl::Buffer in rosidl Python path for rclpy ([#250](https://github.com/ros2/rosidl_python/issues/250))
- Cast Sequence to list on assignment (with templates) ([#249](https://github.com/ros2/rosidl_python/issues/249))
- Fix linter violations with flake8-import-order 0.19.0 ([#248](https://github.com/ros2/rosidl_python/issues/248))
- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#238](https://github.com/ros2/rosidl_python/issues/238))
- Deprecate using set for container based input ([#243](https://github.com/ros2/rosidl_python//issues/243))
- Update to use new BaseImpl ([#241](https://github.com/ros2/rosidl_python/issues/241))
- remove second call ([#232](https://github.com/ros2/rosidl_python/issues/232))
- Derive Messages from Base Classes ([#230](https://github.com/ros2/rosidl_python/issues/230))
- Remove NoReturn for now ([#229](https://github.com/ros2/rosidl_python/issues/229))
- Static typing for Message, Services, and Actions ([#206](https://github.com/ros2/rosidl_python/issues/206))
- Contributors: Anthony Welte, CY Chen, Michael Carlstrom, Nadav Elkabets

<a id="rosidl-generator-rs"></a>

## [rosidl\_generator\_rs](https://github.com/ros2-rust/rosidl_rust/tree/main/rosidl_generator_rs/CHANGELOG.rst)

- fix(rosidl\_generator\_rs\_generate\_interfaces): Remove poisoning of global CMAKE\_SHARED\_LINKER\_FLAGS variable (#22)
- Change the package metadata to point to the new ros-env crate (#21)
- Fix TransientParseError on Ubuntu Resolute (#20)
- fix: do not monkey-patch \_removesuffix into str ([#18](https://github.com/ros2-rust/rosidl_rust/issues/18))
- fix: add str.removesuffix() backport for Python < 3.9 (RHEL 8) ([#17](https://github.com/ros2-rust/rosidl_rust/issues/17))
- feat: relative Module Path Resolution ([#12](https://github.com/ros2-rust/rosidl_rust/issues/12)) \* Changed all generated code to use relative symbols instead of `crate::` ones. Reworked the rosidl\_generator\_rs slightly to be a bit simpler. Separate actual templates from the files that reuse them. \* WIP For adding documentation to all structs, members, and constants generated from idl’s. \* Clean up all the surfaced warnings from generated code.
- build: update rosidl\_runtime\_rs dependency version to 0.6 ([#14](https://github.com/ros2-rust/rosidl_rust/issues/14))
- fix: update rosidl\_runtime\_rs dependency version to 0.5 ([#11](https://github.com/ros2-rust/rosidl_rust/issues/11))
- Fix use of serde ([#9](https://github.com/ros2-rust/rosidl_rust/issues/9)) \* Fix use of serde \* Include serde for services ———
- Update to the latest version of Action trait ([#7](https://github.com/ros2-rust/rosidl_rust/issues/7)) \* Update to the latest version of Action trait \* Fix use of serde ———
- fix cmake deprecation ([#6](https://github.com/ros2-rust/rosidl_rust/issues/6)) \* fix cmake deprecation cmake version < then 3.10 is deprecated \* Update CMakeLists.txt
- fix: clean up dependencies ([#5](https://github.com/ros2-rust/rosidl_rust/issues/5))
- fix: added missing dependency
- clean up changelog. Removed rosidl\_runtime\_rs as a dependency
- set python executable var to custom cmake commands ([#3](https://github.com/ros2-rust/rosidl_rust/issues/3))
- Contributors: Esteve Fernandez, Grey, Kimberly N. McGuire, Sam Privett, Shane Loretz, Silvio Traversaro, mosfet80

<a id="rosidl-generator-tests"></a>

## [rosidl\_generator\_tests](https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_tests/CHANGELOG.rst)

- Use new aggregate rosidl target instead of \_TARGETS ([#952](https://github.com/ros2/rosidl/issues/952))
- rosidl\_generator\_cpp: constexpr message traits and to\_tuple\_ref for generated structs ([#928](https://github.com/ros2/rosidl//issues/928))
- Make `data_type` and `name` traits constexpr ([#929](https://github.com/ros2/rosidl//issues/929))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Contributors: Alexis Tsogias, Michael Carlstrom, mosfet80, Øystein Sture

<a id="rosidl-generator-type-description"></a>

## [rosidl\_generator\_type\_description](https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_type_description/CHANGELOG.rst)

- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#910](https://github.com/ros2/rosidl//issues/910))
- Add missing dependency on ament\_cmake\_pytest ([#914](https://github.com/ros2/rosidl/issues/914))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Contributors: Anthony Welte, Francisco Rossi, Michael Carlstrom, Scott K Logan, mosfet80

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/lyrical/rosidl_parser/CHANGELOG.rst)

- Fix future regressions on flake8 ([#936](https://github.com/ros2/rosidl//issues/936))
- Add Optional Parsing ([#883](https://github.com/ros2/rosidl/issues/883))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Contributors: Michael Carlstrom, mosfet80

<a id="rosidl-pycommon"></a>

## [rosidl\_pycommon](https://github.com/ros2/rosidl/tree/lyrical/rosidl_pycommon/CHANGELOG.rst)

- fix regressions ([#951](https://github.com/ros2/rosidl/issues/951))
- Fix future regressions on flake8 ([#936](https://github.com/ros2/rosidl//issues/936))
- Add BaseImpl ([#912](https://github.com/ros2/rosidl/issues/912))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Provide base classes in `rosidl_pycommon` ([#887](https://github.com/ros2/rosidl/issues/887))
- fix setuptools deprecation ([#880](https://github.com/ros2/rosidl/issues/880))
- Contributors: Michael Carlstrom, mosfet80

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/lyrical/rosidl_runtime_c/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Fix copy/paste errors in type support docs ([#906](https://github.com/ros2/rosidl/issues/906))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Add an ament\_cmake\_gtest dependency to rosidl\_runtime\_c. ([#865](https://github.com/ros2/rosidl/issues/865))
- Contributors: CY Chen, Chris Lalancette, Christophe Bedard, mosfet80

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/lyrical/rosidl_runtime_cpp/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- rosidl\_generator\_cpp: constexpr message traits and to\_tuple\_ref for generated structs ([#928](https://github.com/ros2/rosidl//issues/928))
- Make `data_type` and `name` traits constexpr ([#929](https://github.com/ros2/rosidl//issues/929))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Add missing cstdint include ([#864](https://github.com/ros2/rosidl/issues/864))
- Contributors: CY Chen, Michael Carlstrom, mosfet80, Øystein Sture

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/lyrical/CHANGELOG.rst)

- Add support for rosidl::Buffer in rosidl Python path for rclpy ([#39](https://github.com/ros2/rosidl_runtime_py/issues/39))
- Fix flake8 ([#40](https://github.com/ros2/rosidl_runtime_py/issues/40))
- Add py.typed to the package ([#37](https://github.com/ros2/rosidl_runtime_py/issues/37))
- fix setuptools deprecations ([#35](https://github.com/ros2/rosidl_runtime_py/issues/35))
- Contributors: CY Chen, Michael Carlstrom, Vladimir Gerts, mosfet80

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_c/CHANGELOG.rst)

- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#168](https://github.com/ros2/rosidl_typesupport/issues/168))
- Contributors: Anthony Welte

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_cpp/CHANGELOG.rst)

- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#168](https://github.com/ros2/rosidl_typesupport/issues/168))
- Remove deprecated rosidl\_typesupport\_cpp/type\_support\_map.h ([#167](https://github.com/ros2/rosidl_typesupport/issues/167))
- De-duplicate type\_support\_map.h header ([#81](https://github.com/ros2/rosidl_typesupport/issues/81))
- Contributors: Anthony Welte, Christophe Bedard

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/lyrical/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- Update rosidl typesupport to support rosidl::Buffer in nested uint8[] ([#151](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/151)) ([#152](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/152))
- Add support for rosidl::Buffer type serialization ([#144](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/144))
- use variable to control shared/static build type ([#138](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/138))
- Switch ament\_index\_python and rosidl\_cli to exec\_depend. ([#137](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/137))
- Removed deprecated code ([#135](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/135))
- fix cmake deprecation ([#134](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/134))
- Check remaining size before resizing sequences ([#130](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/130))
- Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen, Chris Lalancette, Jay Sridharan, Miguel Company, mergify[bot], mosfet80

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/lyrical/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- Clean up logs in buffer serialization functions ([#153](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/153)) ([#154](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/154))
- Update rosidl typesupport to support rosidl::Buffer in nested uint8[] ([#151](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/151)) ([#152](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/152))
- Add missing build dependencies for exported dependencies ([#149](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/149))
- Add support for rosidl::Buffer type serialization ([#144](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/144))
- use variable to control shared/static build type ([#138](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/138))
- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#136](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/136))
- Switch ament\_index\_python and rosidl\_cli to exec\_depend. ([#137](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/137))
- Removed deprecated code ([#135](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/135))
- fix cmake deprecation ([#134](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/134))
- Check remaining size before resizing sequences ([#130](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/130))
- Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen, Chris Lalancette, Jay Sridharan, Miguel Company, Scott K Logan, mergify[bot], mosfet80

<a id="rosidl-typesupport-interface"></a>

## [rosidl\_typesupport\_interface](https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_interface/CHANGELOG.rst)

- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Contributors: mosfet80

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#910](https://github.com/ros2/rosidl//issues/910))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- Add DEPENDS\_EXPLICIT\_ONLY to remove implicit dependencies ([#910](https://github.com/ros2/rosidl//issues/910))
- Export typing Information ([#903](https://github.com/ros2/rosidl/issues/903))
- Uniform cmake minVersion ([#849](https://github.com/ros2/rosidl/issues/849))
- rosidl\_cli: Add type description support ([#857](https://github.com/ros2/rosidl/issues/857))
- Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80

<a id="rosidl-typesupport-introspection-tests"></a>

## [rosidl\_typesupport\_introspection\_tests](https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_tests/CHANGELOG.rst)

- Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942](https://github.com/ros2/rosidl/issues/942))
- fix cmake <3.10 deprecation ([#875](https://github.com/ros2/rosidl/issues/875))
- Disable test failing in coverage jobs, see [#812](https://github.com/ros2/rosidl/issues/812) ([#853](https://github.com/ros2/rosidl/issues/853))
- Contributors: CY Chen, Jorge J. Perez, mosfet80

<a id="rosidl-typesupport-tests"></a>

## [rosidl\_typesupport\_tests](https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_tests/CHANGELOG.rst)

- pass all tests for rmw\_cyclonedds\_cpp. ([#171](https://github.com/ros2/rosidl_typesupport/issues/171))
- Contributors: Tomoya Fujita

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/lyrical/CHANGELOG.rst)

- Enforce ament\_mypy –ament-strict ([#22](https://github.com/ros2/rpyutils/issues/22))
- fix setuptools deprecations ([#17](https://github.com/ros2/rpyutils/issues/17))
- Contributors: Michael Carlstrom, mosfet80

<a id="rqt"></a>

## [rqt](https://github.com/ros-visualization/rqt/tree/lyrical/rqt/CHANGELOG.rst)

- fix setuptools deprecations ([#334](https://github.com/ros-visualization/rqt/issues/334))
- fix setuptools deprecations ([#329](https://github.com/ros-visualization/rqt/issues/329))
- Contributors: mosfet80

<a id="rqt-action"></a>

## [rqt\_action](https://github.com/ros-visualization/rqt_action/tree/lyrical/CHANGELOG.rst)

- fix setuptools deprecations ([#19](https://github.com/ros-visualization/rqt_action/issues/19))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#16](https://github.com/ros-visualization/rqt_action/issues/16))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rqt-bag"></a>

## [rqt\_bag](https://github.com/ros-visualization/rqt_bag/tree/lyrical/rqt_bag/CHANGELOG.rst)

- Fix Qt6 issues (backport [#207](https://github.com/ros-visualization/rqt_bag/issues/207)) ([#208](https://github.com/ros-visualization/rqt_bag/issues/208))
- Support Qt6 ([#206](https://github.com/ros-visualization/rqt_bag/issues/206))
- Cleanup mislabeled BSD license ([#205](https://github.com/ros-visualization/rqt_bag/issues/205))
- Better handling of large bag files ([#178](https://github.com/ros-visualization/rqt_bag/issues/178))
- Display roll, pitch, yaw values for quaternions ([#179](https://github.com/ros-visualization/rqt_bag/issues/179))
- Fix flake8 error in setup.py ([#192](https://github.com/ros-visualization/rqt_bag/issues/192))
- Improved raw view to better handle arrays and time objects ([#173](https://github.com/ros-visualization/rqt_bag/issues/173))
- plot\_view: Fixed display of initial message ([#180](https://github.com/ros-visualization/rqt_bag/issues/180))
- fix setuptools deprecations ([#185](https://github.com/ros-visualization/rqt_bag/issues/185))
- Fixed timeline resolution ([#175](https://github.com/ros-visualization/rqt_bag/issues/175))
- Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael Carlstrom, mergify[bot], mosfet80

<a id="rqt-bag-plugins"></a>

## [rqt\_bag\_plugins](https://github.com/ros-visualization/rqt_bag/tree/lyrical/rqt_bag_plugins/CHANGELOG.rst)

- Support Qt6 ([#206](https://github.com/ros-visualization/rqt_bag/issues/206))
- Display roll, pitch, yaw values for quaternions ([#179](https://github.com/ros-visualization/rqt_bag/issues/179))
- Fix flake8 error in setup.py ([#192](https://github.com/ros-visualization/rqt_bag/issues/192))
- Fixed image helper and added support for PNG-coded compressedDepth ([#176](https://github.com/ros-visualization/rqt_bag/issues/176))
- Improve plot view ([#174](https://github.com/ros-visualization/rqt_bag/issues/174))
- plot\_view: Fixed display of initial message ([#180](https://github.com/ros-visualization/rqt_bag/issues/180))
- fix setuptools deprecations ([#185](https://github.com/ros-visualization/rqt_bag/issues/185))
- Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael Carlstrom, mosfet80

<a id="rqt-console"></a>

## [rqt\_console](https://github.com/ros-visualization/rqt_console/tree/lyrical/CHANGELOG.rst)

- Support Qt6 ([#58](https://github.com/ros-visualization/rqt_console/issues/58))
- fixed copyright test ([#57](https://github.com/ros-visualization/rqt_console/issues/57))
- added copyright header
- fixed flake8 ([#56](https://github.com/ros-visualization/rqt_console/issues/56))
- fixed flake8
- remove residual imports in colored output test-file ([#55](https://github.com/ros-visualization/rqt_console/issues/55))
- remove residual imports
- basic support for colors and bold/bright using ANSI escape codes ([#54](https://github.com/ros-visualization/rqt_console/issues/54))
- replace colorama dependency with manual ansi codes
- add checkbox in the settings
- support more color codes
- basic support for colors and bold/bright
- fix setuptools deprecations ([#50](https://github.com/ros-visualization/rqt_console/issues/50))
- Contributors: Alejandro Hernández Cordero, Arne Hitzmann, Peter, mosfet80, peter

<a id="rqt-graph"></a>

## [rqt\_graph](https://github.com/ros-visualization/rqt_graph/tree/lyrical/CHANGELOG.rst)

- Support Wheel event in qt6 (backport [#116](https://github.com/ros-visualization/rqt_graph/issues/116)) ([#117](https://github.com/ros-visualization/rqt_graph/issues/117))
- Fix: broken dependency ([#115](https://github.com/ros-visualization/rqt_graph//issues/115))
- Support Qt6 ([#114](https://github.com/ros-visualization/rqt_graph//issues/114))
- add warning for type incompatibilities ([#105](https://github.com/ros-visualization/rqt_graph/issues/105))
- Remove rqt\_graph script. ([#66](https://github.com/ros-visualization/rqt_graph/issues/66))
- fix setuptools deprecations ([#107](https://github.com/ros-visualization/rqt_graph/issues/107))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jonas Otto, Matthew Foran, mergify[bot], mosfet80

<a id="rqt-gui"></a>

## [rqt\_gui](https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui/CHANGELOG.rst)

- Fix setupTools deprecations ([#322](https://github.com/ros-visualization/rqt/issues/322))
- Contributors: mosfet80

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui_cpp/CHANGELOG.rst)

- Cleanup headers ([#347](https://github.com/ros-visualization/rqt/issues/347)) ([#350](https://github.com/ros-visualization/rqt/issues/350))
- Use qt-base-dev / libqtwidgets ([#345](https://github.com/ros-visualization/rqt/issues/345))
- fix: include unistd.h for getpid ([#341](https://github.com/ros-visualization/rqt/issues/341))
- Support Qt6 ([#339](https://github.com/ros-visualization/rqt/issues/339))
- Removed deprecated header ([#340](https://github.com/ros-visualization/rqt/issues/340))
- Use qt6 as the default dependency from rosdep ([#337](https://github.com/ros-visualization/rqt/issues/337))
- fix compile with qt6 ([#321](https://github.com/ros-visualization/rqt/issues/321))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Shane Loretz, mergify[bot], mosfet80

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui_py/CHANGELOG.rst)

- Support Qt6 ([#339](https://github.com/ros-visualization/rqt/issues/339))
- Fix setupTools deprecations ([#322](https://github.com/ros-visualization/rqt/issues/322))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rqt-msg"></a>

## [rqt\_msg](https://github.com/ros-visualization/rqt_msg/tree/lyrical/CHANGELOG.rst)

- Support Qt6 ([#27](https://github.com/ros-visualization/rqt_msg/issues/27))
- fix setuptools deprecations ([#23](https://github.com/ros-visualization/rqt_msg/issues/23))
- Remove CODEOWNERS ([#20](https://github.com/ros-visualization/rqt_msg/issues/20))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rqt-plot"></a>

## [rqt\_plot](https://github.com/ros-visualization/rqt_plot/tree/lyrical/CHANGELOG.rst)

- Use qt-base-dev / libqtwidgets ([#128](https://github.com/ros-visualization/rqt_plot/issues/128))
- Support Qt6 ([#127](https://github.com/ros-visualization/rqt_plot/issues/127))
- fix setuptools deprecations ([#123](https://github.com/ros-visualization/rqt_plot/issues/123))
- Added missing test dependency ([#118](https://github.com/ros-visualization/rqt_plot/issues/118))
- Fix for displaying constant curves ([#114](https://github.com/ros-visualization/rqt_plot/issues/114))
- Contributors: Alejandro Hernández Cordero, Martin Pecka, Shane Loretz, mosfet80

<a id="rqt-publisher"></a>

## [rqt\_publisher](https://github.com/ros-visualization/rqt_publisher/tree/lyrical/CHANGELOG.rst)

- fix flake8 (backport [#57](https://github.com/ros-visualization/rqt_publisher/issues/57)) ([#58](https://github.com/ros-visualization/rqt_publisher/issues/58))
- Support Qt6 ([#56](https://github.com/ros-visualization/rqt_publisher/issues/56))
- fix setuptools deprecations ([#52](https://github.com/ros-visualization/rqt_publisher/issues/52))
- Contributors: Alejandro Hernández Cordero, mergify[bot], mosfet80

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/lyrical/rqt_py_common/CHANGELOG.rst)

- Cleanup headers ([#347](https://github.com/ros-visualization/rqt/issues/347)) ([#350](https://github.com/ros-visualization/rqt/issues/350))
- Use qt-base-dev / libqtwidgets ([#345](https://github.com/ros-visualization/rqt/issues/345))
- Support Qt6 ([#339](https://github.com/ros-visualization/rqt/issues/339))
- fix compile with qt6 ([#321](https://github.com/ros-visualization/rqt/issues/321))
- Contributors: Alejandro Hernández Cordero, Shane Loretz, mergify[bot], mosfet80

<a id="rqt-py-console"></a>

## [rqt\_py\_console](https://github.com/ros-visualization/rqt_py_console/tree/lyrical/CHANGELOG.rst)

- Add Qt6 compatibility ([#25](https://github.com/ros-visualization/rqt_py_console/issues/25)) Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- fix setuptools deprecations ([#21](https://github.com/ros-visualization/rqt_py_console/issues/21))
- Contributors: Shane Loretz, mosfet80

<a id="rqt-reconfigure"></a>

## [rqt\_reconfigure](https://github.com/ros-visualization/rqt_reconfigure/tree/lyrical/CHANGELOG.rst)

- Support Qt6 ([#158](https://github.com/ros-visualization/rqt_reconfigure/issues/158))
- Harden behavior if double value or limit is Infinity ([#161](https://github.com/ros-visualization/rqt_reconfigure/issues/161))
- Scale IntegerEditor if range exceeds int32 ([#160](https://github.com/ros-visualization/rqt_reconfigure/issues/160))
- Ignore A005 for future flake8 ([#159](https://github.com/ros-visualization/rqt_reconfigure/issues/159))
- Cleanup mislabeled BSD license ([#157](https://github.com/ros-visualization/rqt_reconfigure/issues/157))
- fix setuptools deprecation ([#153](https://github.com/ros-visualization/rqt_reconfigure/issues/153))
- If updating remote fails, reflect the failure locally ([#144](https://github.com/ros-visualization/rqt_reconfigure/issues/144))
- Remove CODEOWNERS ([#147](https://github.com/ros-visualization/rqt_reconfigure/issues/147))
- Contributors: Alejandro Hernández Cordero, Christoph Fröhlich, Jonathan Selling, Michael Carlstrom, mosfet80

<a id="rqt-service-caller"></a>

## [rqt\_service\_caller](https://github.com/ros-visualization/rqt_service_caller/tree/lyrical/CHANGELOG.rst)

- Support Qt6 ([#38](https://github.com/ros-visualization/rqt_service_caller/issues/38))
- fix setuptools deprecations ([#33](https://github.com/ros-visualization/rqt_service_caller/issues/33))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rqt-shell"></a>

## [rqt\_shell](https://github.com/ros-visualization/rqt_shell/tree/lyrical/CHANGELOG.rst)

- make linters happy
- Fix setuptools deprecation ([#26](https://github.com/ros-visualization/rqt_shell/issues/26))
- Contributors: Alejandro Hernandez Cordero, mosfet80

<a id="rqt-srv"></a>

## [rqt\_srv](https://github.com/ros-visualization/rqt_srv/tree/lyrical/CHANGELOG.rst)

- fix setuptools deprecations ([#16](https://github.com/ros-visualization/rqt_srv/issues/16))
- Remove CODEOWNERS ([#13](https://github.com/ros-visualization/rqt_srv/issues/13))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="rqt-topic"></a>

## [rqt\_topic](https://github.com/ros-visualization/rqt_topic/tree/lyrical/CHANGELOG.rst)

- Support Qt6 ([#67](https://github.com/ros-visualization/rqt_topic/issues/67))
- Add Qt6 compatibility ([#66](https://github.com/ros-visualization/rqt_topic/issues/66))
- Tweak expected error in test for Pydantic v2 compat ([#65](https://github.com/ros-visualization/rqt_topic/issues/65))
- Use choose\_qos() from ros2 topic echo ([#55](https://github.com/ros-visualization/rqt_topic/issues/55))
- Enable flake8 ([#58](https://github.com/ros-visualization/rqt_topic/issues/58))
- Open source rewrite of rqt\_topic ([#47](https://github.com/ros-visualization/rqt_topic/issues/47)) Co-authored-by: Evan Flynn <[evan.flynn@apex.ai](mailto:evan.flynn%40apex.ai)> Co-authored-by: Alejandro Hernandez Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- fix setuptools deprecations ([#57](https://github.com/ros-visualization/rqt_topic/issues/57))
- Contributors: Alejandro Hernández Cordero, Evan Flynn, Romain Reignier, Scott K Logan, Shane Loretz, mosfet80

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/lyrical/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Update Connext from 7.3.0 to 7.7.0, disable monitoring library by default, and use synchronous publishing mode ([#219](https://github.com/ros2/rmw_connextdds/issues/219))
- Fix cmake deprecation ([#198](https://github.com/ros2/rmw_connextdds/issues/198))
- Contributors: Francisco Gallego Salido, mosfet80

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/lyrical/rttest/CHANGELOG.rst)

- cleanups and removed dead code ([#141](https://github.com/ros2/realtime_support/issues/141)) ([#144](https://github.com/ros2/realtime_support/issues/144))
- Fix cmake deprecation ([#134](https://github.com/ros2/realtime_support/issues/134))
- Contributors: mergify[bot], mosfet80

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/lyrical/rviz2/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Use new ROSIDL aggregate CMake target ([#1688](https://github.com/ros2/rviz/issues/1688))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- get rid of deprecated rclcpp::spin\_some() ([#1567](https://github.com/ros2/rviz/issues/1567))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Emerson Knapp, Nathan Brooks, Shane Loretz

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/lyrical/rviz_common/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Compressed Image Display ([#1288](https://github.com/ros2/rviz//issues/1288))
- fix: Fixed compilation on MSVC 2022 ([#1706](https://github.com/ros2/rviz//issues/1706))
- Removed Qt6 warnings ([#1704](https://github.com/ros2/rviz/issues/1704))
- Fixed regresion is RHEL ([#1703](https://github.com/ros2/rviz/issues/1703))
- Remove warnings ([#1693](https://github.com/ros2/rviz/issues/1693))
- Link against `GTest::gmock` target ([#1699](https://github.com/ros2/rviz/issues/1699))
- Reduce `QFile` dependency ([#1652](https://github.com/ros2/rviz/issues/1652))
- Use new ROSIDL aggregate CMake target ([#1688](https://github.com/ros2/rviz/issues/1688))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Cleanups in rviz\_common ([#1686](https://github.com/ros2/rviz/issues/1686))
- Add tests for shallow and deep copy in Config ([#1682](https://github.com/ros2/rviz/issues/1682))
- Build performance optimizations for rviz\_common ([#1677](https://github.com/ros2/rviz/issues/1677))
- Use get\_package\_share\_path ([#1671](https://github.com/ros2/rviz/issues/1671))
- Fix setHidden regression in PropertyTreeWidget ([#1667](https://github.com/ros2/rviz/issues/1667))
- Add topic name filtering when adding new visualizations ([#1662](https://github.com/ros2/rviz/issues/1662))
- use QPointer in QTimer::singleShot to prevent use-after-free ([#1657](https://github.com/ros2/rviz/issues/1657))
- Fix Not loading plugins due to incorrect package path ([#1651](https://github.com/ros2/rviz/issues/1651))
- Updated deprecated ament\_index\_cpp API ([#1647](https://github.com/ros2/rviz/issues/1647))
- Fix crash with no tools ([#1639](https://github.com/ros2/rviz/issues/1639))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- Pointcloud2 display set QoS to best effort ([#1621](https://github.com/ros2/rviz/issues/1621))
- Cleanup deprecated code ([#1619](https://github.com/ros2/rviz//issues/1619))
- Removed support for yaml-cpp lower than 0.5 ([#1605](https://github.com/ros2/rviz//issues/1605))
- Removed duplicated forward class declaration ([#1602](https://github.com/ros2/rviz//issues/1602))
- resolved TODO in visualization manager ([#1603](https://github.com/ros2/rviz//issues/1603))
- Fix incorrect Qt signal connection in combo box ([#1596](https://github.com/ros2/rviz/issues/1596))
- Removed tinyxml2\_vendor dependency ([#1591](https://github.com/ros2/rviz/issues/1591))
- Replace QRegExp with QRegularExpression to support Qt6 ([#1592](https://github.com/ros2/rviz/issues/1592))
- fix crash ([#1587](https://github.com/ros2/rviz/issues/1587))
- added option to change filemode ([#1537](https://github.com/ros2/rviz/issues/1537))
- Removed deprecation warning in tf2 ([#1585](https://github.com/ros2/rviz/issues/1585))
- Std chrono update in default plugins ([#1579](https://github.com/ros2/rviz/issues/1579))
- Removed deprecations ([#1556](https://github.com/ros2/rviz/issues/1556))
- rviz common ros service property ([#1548](https://github.com/ros2/rviz/issues/1548))
- add ros action property ([#1549](https://github.com/ros2/rviz/issues/1549))
- Deprecates update(float, float) methods and provides update(std::chrono::duration, std::chrono::duration) replacements. ([#1533](https://github.com/ros2/rviz//issues/1533))
- Replace deprecated tf2\_ros headers ([#1529](https://github.com/ros2/rviz/issues/1529))
- Postpone hiding of properties until insertion into model is finished ([#1508](https://github.com/ros2/rviz/issues/1508))
- Don’t hide rows of properties not within the model ([#1507](https://github.com/ros2/rviz/issues/1507))
- Remove redundant check ([#1506](https://github.com/ros2/rviz/issues/1506))
- Fix panel deletion ([#1037](https://github.com/ros2/rviz/issues/1037))
- Config::mapGetBool causes segmentation fault when value\_out is nullptr ([#1471](https://github.com/ros2/rviz/issues/1471))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- Fixed crash when a resource is not available ([#1455](https://github.com/ros2/rviz/issues/1455))
- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- addTrackedObject Function Fails to Handle Null Pointer, Causing Crash When nullptr is Passed ([#1375](https://github.com/ros2/rviz/issues/1375))
- Add test to check mapGetString when key is missing ([#1361](https://github.com/ros2/rviz/issues/1361))
- UniformStringStream::parseFloat Fails to Handle Invalid Float Formats Correctly ([#1360](https://github.com/ros2/rviz/issues/1360))
- Fix Potential Null Pointer Dereference in VisualizerApp::getRenderWindow() to Prevent Crashes ([#1359](https://github.com/ros2/rviz/issues/1359))
- Extend support for type adaptation (REP 2007) in rviz\_common for TF-filtered displays ([#1346](https://github.com/ros2/rviz/issues/1346))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, David V. Lu!!, Emerson Knapp, Janosch Machowinski, Joshua Supratman, Mark Johnson, Mateusz Żak, Matteo Princisgh, Matthew Foran, Michael Carroll, Nathan Brooks, Oscmoar07, Patrick Roncagliolo, Shane Loretz, mini-1235, nelson, t0k0shi

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/lyrical/rviz_default_plugins/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Compressed Image Display ([#1288](https://github.com/ros2/rviz//issues/1288))
- Removed Qt6 warnings ([#1704](https://github.com/ros2/rviz/issues/1704))
- Switch rviz service resource retriever to use new repo’s code ([#1698](https://github.com/ros2/rviz/issues/1698))
- Link against `GTest::gmock` target ([#1699](https://github.com/ros2/rviz/issues/1699))
- Improve marker common ([#1687](https://github.com/ros2/rviz/issues/1687))
- Reduce `QFile` dependency ([#1652](https://github.com/ros2/rviz/issues/1652))
- Use new ROSIDL aggregate CMake target ([#1688](https://github.com/ros2/rviz/issues/1688))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Remove redundant compilation of test fixtures ([#1673](https://github.com/ros2/rviz/issues/1673))
- Updated deprecated ament\_index\_cpp API ([#1647](https://github.com/ros2/rviz/issues/1647))
- Add CameraInfo topic property to DepthCloudDisplay ([#1643](https://github.com/ros2/rviz/issues/1643))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- Pointcloud2 display set QoS to best effort ([#1621](https://github.com/ros2/rviz/issues/1621))
- Fix Translation Issue in XYOrbitViewController ([#1630](https://github.com/ros2/rviz/issues/1630))
- Overcome 16384 size limit ([#1622](https://github.com/ros2/rviz/issues/1622))
- Removed already done TODO ([#1604](https://github.com/ros2/rviz//issues/1604))
- Fixed issue 1593 ([#1598](https://github.com/ros2/rviz/issues/1598))
- Removed tf2 warning ([#1586](https://github.com/ros2/rviz/issues/1586))
- Removed deprecation warning in tf2 ([#1585](https://github.com/ros2/rviz/issues/1585))
- Std chrono update in default plugins ([#1579](https://github.com/ros2/rviz/issues/1579))
- Fix pointcloud2 display divide by 0 ([#1581](https://github.com/ros2/rviz/issues/1581))
- add support for ffmpeg\_image\_transport and point\_cloud\_transport ([#1568](https://github.com/ros2/rviz/issues/1568))
- Extend the message filter display for point cloud 2 display ([#1566](https://github.com/ros2/rviz/issues/1566))
- Support image transport lifecycle ([#1472](https://github.com/ros2/rviz//issues/1472))
- Fix QoS profile loading for InitialPoseTool from rviz config files ([#1544](https://github.com/ros2/rviz//issues/1544))
- Replace rmw\_qos\_profile\_t with rclcpp::QoS ([#1525](https://github.com/ros2/rviz/issues/1525))
- Replace deprecated tf2\_ros headers ([#1529](https://github.com/ros2/rviz/issues/1529))
- fix deprecated include ([#1530](https://github.com/ros2/rviz/issues/1530))
- point\_cloud\_transport update API call ([#1526](https://github.com/ros2/rviz/issues/1526))
- Better handling of missing transport plugins ([#1488](https://github.com/ros2/rviz/issues/1488))
- Fixed deprecation warning on point\_cloud\_transport: rmw\_qos\_profile\_t ([#1491](https://github.com/ros2/rviz/issues/1491))
- Add symbol visibility macros to make\*Palette public functions ([#1492](https://github.com/ros2/rviz/issues/1492))
- Fix /rviz/get\_resource ([#1487](https://github.com/ros2/rviz/issues/1487))
- Removed point\_cloud\_transport deprecation ([#1474](https://github.com/ros2/rviz/issues/1474))
- Frame view controller: Removed warnings ([#1470](https://github.com/ros2/rviz/issues/1470))
- Fix compile with qt6 ([#1475](https://github.com/ros2/rviz/issues/1475))
- Fix Issue with Quaternion Angular Distance ([#1473](https://github.com/ros2/rviz/issues/1473))
- PointStampedDisplay: Ignore incoming messages if disabled ([#1036](https://github.com/ros2/rviz/issues/1036))
- Removed unused headers from resouce retriever ([#1463](https://github.com/ros2/rviz/issues/1463))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- [rviz\_default\_plugins] Add missing export dependencies ([#1461](https://github.com/ros2/rviz/issues/1461))
- Backported FrameAligned camera ([#1453](https://github.com/ros2/rviz/issues/1453))
- Changed Marker Displays to allow toggling visibility of namespaces ([#1402](https://github.com/ros2/rviz/issues/1402))
- Do not use ${Qt5Widgets\_INCLUDE\_DIRS} to avoid creating non-relocatable CMake config files ([#1450](https://github.com/ros2/rviz/issues/1450))
- PointCloudDisplay: Fix decay time 0 keeping more than the last message ([#1400](https://github.com/ros2/rviz/issues/1400))
- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- Include chrono ([#1353](https://github.com/ros2/rviz/issues/1353))
- Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Antonio Brandi, Daisuke Nishimatsu, Eesha Kumar, Emerson Knapp, Felix Exner (fexner), Georg Flick, Guillaume Doisy, Harrison Chen, Kenji Brameld (TRACLabs), Kosuke Takeuchi, Lennart Reiher, Mark Johnson, Matthew Foran, Michael Carroll, Nathan Brooks, Shane Loretz, Silvio Traversaro, Stefan Fabian, Stoyan Gaydarov, mosfet80

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/lyrical/rviz_ogre_vendor/CHANGELOG.rst)

- Add patch to remove `binary_function` ([#1691](https://github.com/ros2/rviz/issues/1691))
- Bump cmake version and suppress warning for rviz\_ogre\_vendor ([#1684](https://github.com/ros2/rviz/issues/1684))
- Remove vendoring freetype and zlib on Windows ([#1636](https://github.com/ros2/rviz/issues/1636))
- Add RVIZ\_OGRE\_VENDOR\_MANGLE\_NAME\_OF\_LIBRARIES\_USED\_BY\_RVIZ option to further mangle ogre libraries used by rviz ([#1493](https://github.com/ros2/rviz/issues/1493))
- Add missing glew dependency for ogre vendor package ([#1350](https://github.com/ros2/rviz/issues/1350))
- Contributors: Dhruv Patel, Michael Carroll, Shane Loretz, Silvio Traversaro, Stefan Fabian

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/lyrical/rviz_rendering/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Fix build for Ubuntu 26 ([#1694](https://github.com/ros2/rviz/issues/1694))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Updated deprecated ament\_index\_cpp API ([#1647](https://github.com/ros2/rviz/issues/1647))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- Removed unused files ([#1600](https://github.com/ros2/rviz//issues/1600))
- Removed assimp vendor package ([#1574](https://github.com/ros2/rviz/issues/1574))
- Update OGRE mesh files from ROS1 RViz ([#1536](https://github.com/ros2/rviz//issues/1536)) ([#1559](https://github.com/ros2/rviz//issues/1559))
- add resourceExists check to loadEmbeddedTexture before loading texture ([#1542](https://github.com/ros2/rviz//issues/1542))
- Assign the geometry to the resource group “rviz\_rendering” ([#1502](https://github.com/ros2/rviz/issues/1502))
- Removed windows warning ([#1486](https://github.com/ros2/rviz/issues/1486))
- Handle glTF Y-Up frame convention on mesh load ([#1482](https://github.com/ros2/rviz/issues/1482))
- Removed unused headers from resouce retriever ([#1463](https://github.com/ros2/rviz/issues/1463))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- WrenchVisual::setForceColor and setTorqueColor clamp values ([#1437](https://github.com/ros2/rviz/issues/1437))
- Missing Null Pointer Check in TrianglePolygon Constructor Leads to Crash ([#1434](https://github.com/ros2/rviz/issues/1434))
- BillboardLine::addPoint() does not throw an exception when exceeding max\_points\_per\_line limit ([#1436](https://github.com/ros2/rviz/issues/1436))
- Constructor ScrewVisual::ScrewVisual does not handle null pointers, leading to crashes ([#1435](https://github.com/ros2/rviz/issues/1435))
- Removed Windows warnings ([#1413](https://github.com/ros2/rviz/issues/1413))
- Memory Access Error When Handling Empty Strings in splitStringIntoTrimmedItems Function ([#1412](https://github.com/ros2/rviz/issues/1412))
- Crash due to Unhandled Null Pointer in ParameterEventsFilter Constructor ([#1411](https://github.com/ros2/rviz/issues/1411))
- MovableText constructor does not validate invalid character height, default fallback missing ([#1398](https://github.com/ros2/rviz/issues/1398))
- Invalid Parameter Handling in CovarianceVisual::CovarianceVisual Constructor ([#1396](https://github.com/ros2/rviz/issues/1396))
- Lack of Validity Check for Invalid Parameters in EffortVisual::EffortVisual Constructor ([#1395](https://github.com/ros2/rviz/issues/1395))
- Grid Class Constructor Does Not Handle Null Pointer, Leading to Program Crash ([#1394](https://github.com/ros2/rviz/issues/1394))
- Crash in MovableText::update() when caption is an empty string due to uninitialized resource usage ([#1393](https://github.com/ros2/rviz/issues/1393))
- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, John TGZ, Michael Carlstrom, Michael Carroll, Michel Hidalgo, Nathan Brooks, Shane Loretz, matthias88, mergify[bot], mosfet80

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/lyrical/rviz_rendering_tests/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Updated deprecated ament\_index\_cpp API ([#1647](https://github.com/ros2/rviz/issues/1647))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Michael Carroll, Nathan Brooks, Shane Loretz

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/lyrical/rviz_visual_testing_framework/CHANGELOG.rst)

- Use rosdep keys that select Qt5 or Qt6 by platform ([#1720](https://github.com/ros2/rviz/issues/1720))
- Use new ROSIDL aggregate CMake target ([#1688](https://github.com/ros2/rviz/issues/1688))
- Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689](https://github.com/ros2/rviz/issues/1689))
- Use get\_package\_share\_path ([#1671](https://github.com/ros2/rviz/issues/1671))
- Update ament\_index\_cpp API ([#1649](https://github.com/ros2/rviz/issues/1649))
- Use qt6 as the default dependency from rosdep ([#1635](https://github.com/ros2/rviz/issues/1635))
- Removed deprecation warning in tf2 ([#1585](https://github.com/ros2/rviz/issues/1585))
- Replace deprecated tf2\_ros headers ([#1529](https://github.com/ros2/rviz/issues/1529))
- feat: support both qt5 and qt6 ([#1187](https://github.com/ros2/rviz/issues/1187))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Emerson Knapp, Nathan Brooks, Shane Loretz

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/sensor_msgs/CHANGELOG.rst)

- [ADD] missing PointField type entries ([#301](https://github.com/ros2/common_interfaces/issues/301))
- Update point\_cloud2\_iterator.hpp ([#298](https://github.com/ros2/common_interfaces/issues/298))
- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Enhance NV12 and NV21 Support in sensor\_msgs::image\_encodings ([#264](https://github.com/ros2/common_interfaces/issues/264))
- Contributors: Adam Leeper, Zhaoyuan Cheng, mosfet80, wodtko

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/lyrical/sensor_msgs_py/CHANGELOG.rst)

- Use structured NumPy points.dtype.itemsize as default point\_step in create\_cloud ([#295](https://github.com/ros2/common_interfaces/issues/295))
- fix setuptools deprecation ([#293](https://github.com/ros2/common_interfaces/issues/293))
- Contributors: mosfet80, xndcn

<a id="service-msgs"></a>

## [service\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/service_msgs/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="shape-msgs"></a>

## [shape\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/shape_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="spdlog-vendor"></a>

## [spdlog\_vendor](https://github.com/ros2/spdlog_vendor/tree/lyrical/CHANGELOG.rst)

- Remove CODEOWNERS and mirror-rolling-to-master. ([#38](https://github.com/ros2/spdlog_vendor/issues/38))
- Contributors: Chris Lalancette

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/lyrical/sros2/CHANGELOG.rst)

- Fix `load_file_into_BIO: File could not be found, opened or is empty` error on Windows ([#386](https://github.com/ros2/sros2/issues/386)) ([#387](https://github.com/ros2/sros2/issues/387))
- python3-pytest-timeout is missing for test dependency. ([#377](https://github.com/ros2/sros2/issues/377))
- Clean up isolated ros2 daemon process for tests. ([#375](https://github.com/ros2/sros2/issues/375))
- Remove importlib ([#368](https://github.com/ros2/sros2/issues/368))
- Timezone aware datetimes + remove hack from [#209](https://github.com/ros2/sros2/issues/209) ([#300](https://github.com/ros2/sros2/issues/300))
- fix setuptools deprecations ([#357](https://github.com/ros2/sros2/issues/357))
- Use rmw\_test\_fixture to isolate ros2cli tests ([#356](https://github.com/ros2/sros2/issues/356))
- update utilities to pass instance not class of ec.SECP256R1 ([#352](https://github.com/ros2/sros2/issues/352))
- suppress multi-threaded warnings. ([#346](https://github.com/ros2/sros2/issues/346))
- Switch to get\_rmw\_additional\_env ([#339](https://github.com/ros2/sros2/issues/339))
- Fix github-workflow mypy error ([#336](https://github.com/ros2/sros2/issues/336))
- Contributors: Michael Carlstrom, Mikael Arguedas, Scott K Logan, Tomoya Fujita, cdisco, mergify[bot], mosfet80, yadunund

<a id="sros2-cmake"></a>

## [sros2\_cmake](https://github.com/ros2/sros2/tree/lyrical/sros2_cmake/CHANGELOG.rst)

- Update CMakeLists.txt ([#344](https://github.com/ros2/sros2/issues/344))
- Contributors: mosfet80

<a id="statistics-msgs"></a>

## [statistics\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/statistics_msgs/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="std-msgs"></a>

## [std\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/std_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="std-srvs"></a>

## [std\_srvs](https://github.com/ros2/common_interfaces/tree/lyrical/std_srvs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="stereo-msgs"></a>

## [stereo\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/stereo_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="tango-icons-vendor"></a>

## [tango\_icons\_vendor](https://github.com/ros-visualization/tango_icons_vendor/tree/lyrical/CHANGELOG.rst)

- fix cmake deprecation ([#15](https://github.com/ros-visualization/tango_icons_vendor/issues/15))
- Remove the mirror-rolling-to-master workflow ([#12](https://github.com/ros-visualization/tango_icons_vendor/issues/12))
- Remove CODEOWNERS ([#11](https://github.com/ros-visualization/tango_icons_vendor/issues/11))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, mosfet80

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/lyrical/test_cli/CHANGELOG.rst)

- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Contributors: mosfet80

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/lyrical/test_cli_remapping/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#587](https://github.com/ros2/system_tests/issues/587))
- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Contributors: Emerson Knapp, mosfet80

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/lyrical/test_communication/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#587](https://github.com/ros2/system_tests/issues/587))
- disable interoperability check for CycloneDDS and FastRTPS for WString ([#586](https://github.com/ros2/system_tests/issues/586))
- Fix index ([#585](https://github.com/ros2/system_tests/issues/585))
- Update subscription callback signatures ([#575](https://github.com/ros2/system_tests/issues/575))
- get rid of deprecated rclcpp::spin\_some(). ([#574](https://github.com/ros2/system_tests//issues/574))
- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Use EnableRmwIsolation in launch tests ([#571](https://github.com/ros2/system_tests/issues/571))
- Switch to isolated test fixture macros ([#571](https://github.com/ros2/system_tests/issues/571))
- Add tests for Keyed types ([#568](https://github.com/ros2/system_tests/issues/568))
- Remove use of ament\_target\_dependencies ([#566](https://github.com/ros2/system_tests/issues/566))
- Skip all multi-vendor pub/sub tests with zenoh ([#560](https://github.com/ros2/system_tests/issues/560))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Francisco Gallego Salido, Janosch Machowinski, Michael Carlstrom, Scott K Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80, yadunund

<a id="test-interface-files"></a>

## [test\_interface\_files](https://github.com/ros2/test_interface_files/tree/lyrical/CHANGELOG.rst)

- Update CMakeLists.txt ([#26](https://github.com/ros2/test_interface_files/issues/26))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#23](https://github.com/ros2/test_interface_files/issues/23))
- Contributors: Chris Lalancette, mosfet80

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/lyrical/test_launch_ros/CHANGELOG.rst)

- Add tests for new component container refactor ([#536](https://github.com/ros2/launch_ros/issues/536))
- Surpressing multi-threaded process warning from flake8. ([#520](https://github.com/ros2/launch_ros//issues/520))
- correct typos ([#524](https://github.com/ros2/launch_ros//issues/524))
- set PYTHONUNBUFFERED to 1 to avoid hangs due to lost buffers ([#519](https://github.com/ros2/launch_ros//issues/519))
- Make FindPackage substitutions a Path to get operator / ([#494](https://github.com/ros2/launch_ros/issues/494))
- Expose lifecycle\_node ([#327](https://github.com/ros2/launch_ros/issues/327)) (with test) ([#482](https://github.com/ros2/launch_ros/issues/482))
- Switch osrf\_pycommon dependency to system package ([#431](https://github.com/ros2/launch_ros/issues/431))
- Fix SetUseSimTime for launch frontends ([#488](https://github.com/ros2/launch_ros/issues/488))
- fix setuptools deprecations ([#475](https://github.com/ros2/launch_ros/issues/475))
- Fix: LoadComposableNodes fails to parse wildcard param files correctly ([#460](https://github.com/ros2/launch_ros/issues/460)) ([#465](https://github.com/ros2/launch_ros/issues/465))
- Contributors: Auguste Lalande, Christophe Bedard, Clara Berendsen, Emerson Knapp, Emre Kuru, Jasper van Brakel, Scott K Logan, Skyler Medeiros, Tomoya Fujita, mosfet80

<a id="test-launch-testing"></a>

## [test\_launch\_testing](https://github.com/ros2/launch/tree/lyrical/test_launch_testing/CHANGELOG.rst)

- Fix CMake deprecation ([#899](https://github.com/ros2/launch/issues/899))
- Allow Path in substitutions, instead of requiring cast to str ([#873](https://github.com/ros2/launch/issues/873))
- Contributors: Emerson Knapp, mosfet80

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/lyrical/test_msgs/CHANGELOG.rst)

- Add `ament_cmake_mypy` to `test_msgs` ([#187](https://github.com/ros2/rcl_interfaces/issues/187))
- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: Michael Carlstrom, mosfet80

<a id="test-osrf-testing-tools-cpp"></a>

## [test\_osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/lyrical/test_osrf_testing_tools_cpp/CHANGELOG.rst)

- fix cmake deprecation ([#94](https://github.com/osrf/osrf_testing_tools_cpp/issues/94))
- Contributors: mosfet80

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/lyrical/test_quality_of_service/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#587](https://github.com/ros2/system_tests/issues/587))
- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Switch to isolated test fixture macros ([#571](https://github.com/ros2/system_tests/issues/571))
- Use rmw\_event\_type\_is\_supported to skip tests ([#563](https://github.com/ros2/system_tests/issues/563))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, mosfet80

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/lyrical/test_rclcpp/CHANGELOG.rst)

- Add tests isolation in test\_rclcpp ([#583](https://github.com/ros2/system_tests/issues/583))
- info message comes from deferred signal handler with another thread. ([#576](https://github.com/ros2/system_tests/issues/576))
- get rid of deprecated rclcpp::spin\_some(). ([#574](https://github.com/ros2/system_tests//issues/574))
- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Use EnableRmwIsolation in launch tests ([#571](https://github.com/ros2/system_tests/issues/571))
- Ensure test verifies the existence of all spawning nodes ([#558](https://github.com/ros2/system_tests/issues/558))
- Contributors: Alejandro Hernández Cordero, Julien Enoch, Scott K Logan, Tomoya Fujita, Yuyuan Yuan, mosfet80

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/lyrical/test_rmw_implementation/CHANGELOG.rst)

- Use new aggregate rosidl target instead of \_TARGETS ([#276](https://github.com/ros2/rmw_implementation/issues/276))
- test\_rmw\_implementation: add test isolation ([#275](https://github.com/ros2/rmw_implementation/issues/275))
- Add rmw\_get\_clients\_info\_by\_service , rmw\_servers\_clients\_info\_by\_service ([#238](https://github.com/ros2/rmw_implementation/issues/238))
- fix cmake deprecation ([#267](https://github.com/ros2/rmw_implementation/issues/267))
- Test failing deserialization of invalid sequence length ([#261](https://github.com/ros2/rmw_implementation/issues/261))
- add ignore\_local\_publications\_serialized test. ([#255](https://github.com/ros2/rmw_implementation/issues/255))
- Contributors: Alexis Tsogias, Julien Enoch, Lee, Miguel Company, Minju, Tomoya Fujita, mosfet80

<a id="test-ros2trace"></a>

## [test\_ros2trace](https://github.com/ros2/ros2_tracing/tree/lyrical/test_ros2trace/CHANGELOG.rst)

- Skip test\_ros2trace’s tracing tests for now ([#218](https://github.com/ros2/ros2_tracing/issues/218))
- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- Only check test process events in test\_runtime\_disable ([#193](https://github.com/ros2/ros2_tracing/issues/193))
- Add runtime tracing opt-out mechanism ([#185](https://github.com/ros2/ros2_tracing/issues/185))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Use timeout for everything in test\_ros2trace tests ([#174](https://github.com/ros2/ros2_tracing/issues/174))
- Contributors: Christophe Bedard, Michel Hidalgo, Shravan Deva, mosfet80

<a id="test-security"></a>

## [test\_security](https://github.com/ros2/system_tests/tree/lyrical/test_security/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#587](https://github.com/ros2/system_tests/issues/587))
- fix CMAKE deprecation ([#572](https://github.com/ros2/system_tests/issues/572))
- Contributors: Emerson Knapp, mosfet80

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/lyrical/test_tf2/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- added toMsg for eigen-accel as well as its tests ([#887](https://github.com/ros2/geometry2/issues/887))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Adding NodeInterfaces API Design ([#714](https://github.com/ros2/geometry2/issues/714))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Add `rclcpp::shutdown` ([#762](https://github.com/ros2/geometry2/issues/762))
- Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary Servin, Lucas Wendland, R Kent James, Yuyuan Yuan, mosfet80

<a id="test-tracetools"></a>

## [test\_tracetools](https://github.com/ros2/ros2_tracing/tree/lyrical/test_tracetools/CHANGELOG.rst)

- fix: Fixed compiation on MSVC 2022 ([#243](https://github.com/ros2/ros2_tracing/issues/243))
- Use new ROSIDL aggregate CMake target ([#238](https://github.com/ros2/ros2_tracing/issues/238))
- Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233](https://github.com/ros2/ros2_tracing/issues/233))
- Update subscription callback signatures ([#217](https://github.com/ros2/ros2_tracing/issues/217))
- Add runtime tracing opt-out mechanism ([#185](https://github.com/ros2/ros2_tracing/issues/185))
- Update CMakeLists.txt ([#176](https://github.com/ros2/ros2_tracing/issues/176))
- Contributors: Emerson Knapp, Janosch Machowinski, Michel Hidalgo, Raphael van Kempen, mini-1235, mosfet80

<a id="test-tracetools-launch"></a>

## [test\_tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/lyrical/test_tracetools_launch/CHANGELOG.rst)

- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Make trace action parameters substitutable for xml and yaml launch files ([#188](https://github.com/ros2/ros2_tracing/issues/188))
- Make trace action parameters substitutable ([#187](https://github.com/ros2/ros2_tracing/issues/187))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Contributors: Christophe Bedard, Shravan Deva, mosfet80

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/lyrical/tf2/CHANGELOG.rst)

- Added tests for static cache ([#920](https://github.com/ros2/geometry2/issues/920))
- Replacing with clean index-based iteration and avoid division by zero ([#901](https://github.com/ros2/geometry2/issues/901))
- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Fix StaticCache::getData() returning true on empty cache ([#908](https://github.com/ros2/geometry2/issues/908))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Fix CPP style in tf2 ([#902](https://github.com/ros2/geometry2/issues/902))
- local variable tf2 no longer shadows the tf2:: ([#903](https://github.com/ros2/geometry2/issues/903))
- Replaced char\* with std::string ([#904](https://github.com/ros2/geometry2/issues/904))
- Fix misleading extrapolation time in buffer\_core ([#832](https://github.com/ros2/geometry2/issues/832)) ([#896](https://github.com/ros2/geometry2/issues/896))
- static function to crate quaternions directly from rotation added ([#881](https://github.com/ros2/geometry2/issues/881))
- Expose Doxygen output in tf2, showing former Doxygen front page also as README.md ([#871](https://github.com/ros2/geometry2/issues/871))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Fix various documentation errors in tf2 ([#857](https://github.com/ros2/geometry2/issues/857))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Fix REP url locations ([#847](https://github.com/ros2/geometry2/issues/847))
- Adding explicit handling for normalization of zero-quaternions ([#839](https://github.com/ros2/geometry2/issues/839))
- Cleanup TF2 dependencies ([#843](https://github.com/ros2/geometry2/issues/843))
- Added tf2 documentation to docs.ros.org ([#671](https://github.com/ros2/geometry2/issues/671))
- Add RPY quaternion constructor ([#806](https://github.com/ros2/geometry2/issues/806))
- Default initialize TransformStorage’s frame\_id\_ and child\_frame\_id\_ with UINT32\_MAX ([#783](https://github.com/ros2/geometry2/issues/783))
- Removed deprecated headers tf2 ([#789](https://github.com/ros2/geometry2/issues/789))
- Add isnan support ([#780](https://github.com/ros2/geometry2/issues/780))
- Overflow Issue in durationFromSec() Function when Handling Extremely Large or Small Values ([#785](https://github.com/ros2/geometry2/issues/785))
- Do not clobber callback handles when cancelling pending transformable requests ([#779](https://github.com/ros2/geometry2/issues/779))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: Alejandro Hernández Cordero, Alireza Moayyedi, Andreas, Auguste Lalande, Chris Lalancette, Emerson Knapp, Markus Bader, Michael Carlstrom, Pavel Guzenfeld, R Kent James, Selim Ağırman, Simon Jusner, Tim Clephas, Timo Röhling, cramke, mosfet80

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/lyrical/tf2_bullet/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Set Cmake Policy CMP0144 ([#819](https://github.com/ros2/geometry2/issues/819))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: Cristóbal Arroyo, Emerson Knapp, Gary Servin, R Kent James, mosfet80

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/lyrical/tf2_eigen/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- added toMsg for eigen-accel as well as its tests ([#887](https://github.com/ros2/geometry2/issues/887))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Add fromMsg for converting from Accel to Eigen ([#844](https://github.com/ros2/geometry2/issues/844))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary Servin, R Kent James, mosfet80

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/lyrical/tf2_eigen_kdl/CHANGELOG.rst)

- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Cleanup mislabeled BSD license ([#855](https://github.com/ros2/geometry2/issues/855))
- Removed orocos kdl vendor dependency ([#826](https://github.com/ros2/geometry2/issues/826))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: Alejandro Hernández Cordero, R Kent James, mosfet80

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/lyrical/tf2_geometry_msgs/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- fix: doTransform of VelocityStamped added input vector after transform ([#909](https://github.com/ros2/geometry2/issues/909))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Copy child\_frame\_id from input ([#889](https://github.com/ros2/geometry2/issues/889))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Removed orocos kdl vendor dependency ([#826](https://github.com/ros2/geometry2/issues/826))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Gary Servin, R Kent James, Yannik Meinken, cramke

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/lyrical/tf2_kdl/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Documentation fixes for tf2\_kdl ([#869](https://github.com/ros2/geometry2/issues/869))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Removed orocos kdl vendor dependency ([#826](https://github.com/ros2/geometry2/issues/826))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Emmanuel, Gary Servin, R Kent James, mosfet80

<a id="tf2-msgs"></a>

## [tf2\_msgs](https://github.com/ros2/geometry2/tree/lyrical/tf2_msgs/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: Auguste Lalande, R Kent James, mosfet80

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/lyrical/tf2_py/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Cleanup TF2 dependencies ([#843](https://github.com/ros2/geometry2/issues/843))
- Contributors: Auguste Lalande, Chris Lalancette, Emerson Knapp, R Kent James

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/lyrical/tf2_ros/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Move author tags to file brief ([#870](https://github.com/ros2/geometry2/issues/870))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Prevent log spam from tf2\_ros message\_filter ([#851](https://github.com/ros2/geometry2/issues/851))
- Updated tf2\_echo with some other features ([#802](https://github.com/ros2/geometry2/issues/802)) ([#840](https://github.com/ros2/geometry2/issues/840))
- Replace std::sleep\_for with rclcpp::clock::sleep\_for ([#835](https://github.com/ros2/geometry2/issues/835))
- Removed deprecation rclcpp::spin\_some(node) ([#824](https://github.com/ros2/geometry2/issues/824))
- Adding NodeInterfaces API Design ([#714](https://github.com/ros2/geometry2/issues/714))
- ger rid of deprecated rclcpp::spin\_some(). ([#821](https://github.com/ros2/geometry2/issues/821))
- Ensure variable is considered volatile in message\_filter\_test ([#812](https://github.com/ros2/geometry2/issues/812))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Fix message filter target frames string ([#803](https://github.com/ros2/geometry2/issues/803))
- Remove deprecation warnings ([#790](https://github.com/ros2/geometry2/issues/790))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Add `rclcpp::shutdown` ([#762](https://github.com/ros2/geometry2/issues/762))
- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Emmanuel, Gary Servin, Lucas Wendland, Mirko Ferrati, R Kent James, Sergei Zobov, Tomoya Fujita, Yuyuan Yuan, mergify[bot], mini-1235, mosfet80

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/lyrical/tf2_ros_py/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- flake8 fixes ([#919](https://github.com/ros2/geometry2/issues/919))
- prevent AttributeError when static\_only=true ([#906](https://github.com/ros2/geometry2/issues/906))
- fixed typoe in buffer.py ([#905](https://github.com/ros2/geometry2/issues/905))
- Increase robustness of listener and broadcaster test ([#894](https://github.com/ros2/geometry2/issues/894))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856](https://github.com/ros2/geometry2/issues/856))
- Cleanup TF2 dependencies ([#843](https://github.com/ros2/geometry2/issues/843))
- Fixed inconsistency of C++ and Python implementations of StaticTransformPublisher ([#820](https://github.com/ros2/geometry2/issues/820))
- Fix deprecation warning ([#804](https://github.com/ros2/geometry2/issues/804))
- Remove deprecation warnings ([#790](https://github.com/ros2/geometry2/issues/790))
- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- Contributors: Alejandro Hernández Cordero, Auguste Lalande, Chris Lalancette, Dominik, Emmanuel, Michael Carlstrom, Michael Carroll, R Kent James, mosfet80

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/lyrical/tf2_sensor_msgs/CHANGELOG.rst)

- fix typos ([#921](https://github.com/ros2/geometry2/issues/921))
- Use new ROSIDL aggregate CMake target ([#907](https://github.com/ros2/geometry2/issues/907))
- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Solved TODO with copyright in tf2\_sensor\_msgs ([#836](https://github.com/ros2/geometry2/issues/836))
- Removed orocos kdl vendor dependency ([#826](https://github.com/ros2/geometry2/issues/826))
- Add imu & mag support in `tf2_sensor_msgs` ([#800](https://github.com/ros2/geometry2/issues/800)) ([#813](https://github.com/ros2/geometry2/issues/813))
- Change tf2\_ros C to C++ headers ([#805](https://github.com/ros2/geometry2/issues/805))
- Add normals rotation in `PointCloud2` `doTransform` ([#792](https://github.com/ros2/geometry2/issues/792))
- Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Gary Servin, Patrick Roncagliolo, R Kent James

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/lyrical/tf2_tools/CHANGELOG.rst)

- Modernize conf.py files to only include modified Copyright, eliminati… ([#865](https://github.com/ros2/geometry2/issues/865))
- Fix Setuptools deprecations ([#809](https://github.com/ros2/geometry2/issues/809))
- Contributors: R Kent James, mosfet80

<a id="tlsf"></a>

## [tlsf](https://github.com/ros2/tlsf/tree/lyrical/tlsf/CHANGELOG.rst)

- update cmake requirements ([#18](https://github.com/ros2/tlsf/issues/18))
- Contributors: mosfet80

<a id="tlsf-cpp"></a>

## [tlsf\_cpp](https://github.com/ros2/realtime_support/tree/lyrical/tlsf_cpp/CHANGELOG.rst)

- cleanups and removed dead code ([#141](https://github.com/ros2/realtime_support/issues/141)) ([#144](https://github.com/ros2/realtime_support/issues/144))
- fix: Removed AllocatorMemoryStrategy (backport [#140](https://github.com/ros2/realtime_support/issues/140)) ([#142](https://github.com/ros2/realtime_support/issues/142))
- Remove deprecation warnings ([#139](https://github.com/ros2/realtime_support/issues/139))
- Use new ROSIDL aggregate CMake target ([#137](https://github.com/ros2/realtime_support/issues/137))
- tlsf\_cpp: add test isolation ([#136](https://github.com/ros2/realtime_support/issues/136))
- Update subscription callback signatures ([#135](https://github.com/ros2/realtime_support/issues/135))
- Fix cmake deprecation ([#134](https://github.com/ros2/realtime_support/issues/134))
- Explicitly shutdown context before test exits ([#129](https://github.com/ros2/realtime_support/issues/129))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien Enoch, mergify[bot], mini-1235, mosfet80, yadunund

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/lyrical/topic_monitor/CHANGELOG.rst)

- Add mypy config ([#776](https://github.com/ros2/demos//issues/776))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- fix setuptools deprecations ([#733](https://github.com/ros2/demos/issues/733))
- Update README.md ([#718](https://github.com/ros2/demos/issues/718)) ([#719](https://github.com/ros2/demos/issues/719))
- Contributors: Dan Mascarenhas, Lucas Wendland, mergify[bot], mosfet80

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/lyrical/topic_statistics_demo/CHANGELOG.rst)

- Use new ROSIDL aggregate CMake target ([#781](https://github.com/ros2/demos//issues/781))
- Switching to example\_interfaces ([#674](https://github.com/ros2/demos/issues/674))
- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Contributors: Emerson Knapp, Lucas Wendland, mosfet80

<a id="tracetools"></a>

## [tracetools](https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools/CHANGELOG.rst)

- Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233](https://github.com/ros2/ros2_tracing/issues/233))
- Removed warning ([#225](https://github.com/ros2/ros2_tracing/issues/225))
- Add runtime tracing opt-out mechanism ([#185](https://github.com/ros2/ros2_tracing/issues/185))
- Fix Clang warnings by using proper function prototypes in macros ([#179](https://github.com/ros2/ros2_tracing/issues/179))
- Update CMakeLists.txt ([#176](https://github.com/ros2/ros2_tracing/issues/176))
- Removed clang warning ([#168](https://github.com/ros2/ros2_tracing/issues/168))
- Contributors: Alejandro Hernández Cordero, Michel Hidalgo, Raphael van Kempen, Shravan Deva, mosfet80

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_launch/CHANGELOG.rst)

- tracetools\_launch: use parse\_if\_substitutions for non-string action params ([#234](https://github.com/ros2/ros2_tracing/issues/234))
- Add example launch files for snapshot mode ([#206](https://github.com/ros2/ros2_tracing/issues/206))
- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- Add launch files with preconfigured dual session ([#196](https://github.com/ros2/ros2_tracing/issues/196))
- Add support for starting tracing at runtime ([#191](https://github.com/ros2/ros2_tracing/issues/191))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Make trace action parameters substitutable for xml and yaml launch files ([#188](https://github.com/ros2/ros2_tracing/issues/188))
- Make trace action parameters substitutable ([#187](https://github.com/ros2/ros2_tracing/issues/187))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Contributors: Christophe Bedard, Sarthak Bagga, Shravan Deva, mosfet80

<a id="tracetools-read"></a>

## [tracetools\_read](https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_read/CHANGELOG.rst)

- Work around segfault when reading trace with babeltrace1 Python API ([#246](https://github.com/ros2/ros2_tracing/issues/246))
- Ignore A0005 ([#237](https://github.com/ros2/ros2_tracing/issues/237))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Contributors: Christophe Bedard, Michael Carlstrom, mosfet80

<a id="tracetools-test"></a>

## [tracetools\_test](https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_test/CHANGELOG.rst)

- Set default values on TraceTestCase to avoid errors on >=8.2.0 pytest ([#236](https://github.com/ros2/ros2_tracing/issues/236))
- Only check test process events in test\_runtime\_disable ([#193](https://github.com/ros2/ros2_tracing/issues/193))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Contributors: Christophe Bedard, Clara Berendsen, mosfet80

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_trace/CHANGELOG.rst)

- Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233](https://github.com/ros2/ros2_tracing/issues/233))
- Ignore A0005 ([#237](https://github.com/ros2/ros2_tracing/issues/237))
- Add exec\_depend on procps to tracetools\_trace for ps command ([#227](https://github.com/ros2/ros2_tracing/issues/227))
- Handle SIGTERM and gracefully stop tracing in interactive tracing mode ([#219](https://github.com/ros2/ros2_tracing/issues/219))
- Use overwrite mode for snapshot sessions ([#210](https://github.com/ros2/ros2_tracing/issues/210))
- Allow creating snapshot sessions ([#195](https://github.com/ros2/ros2_tracing/issues/195))
- Add support for starting tracing at runtime ([#191](https://github.com/ros2/ros2_tracing/issues/191))
- fix setuptools deprecation ([#189](https://github.com/ros2/ros2_tracing/issues/189))
- Address typing issues reported by mypy in tracetools\_launch ([#184](https://github.com/ros2/ros2_tracing/issues/184))
- Warn if kernel might be paranoid about ‘perf:thread:’ context fields ([#173](https://github.com/ros2/ros2_tracing/issues/173))
- Fix pluralization in ros2 trace output ([#169](https://github.com/ros2/ros2_tracing/issues/169))
- Contributors: Christophe Bedard, Michael Carlstrom, Raphael van Kempen, Shravan Deva, mosfet80

<a id="trajectory-msgs"></a>

## [trajectory\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/trajectory_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/lyrical/turtlesim/CHANGELOG.rst)

- Add icon for Lyrical Luth ([#196](https://github.com/ros/ros_tutorials/issues/196)) ([#197](https://github.com/ros/ros_tutorials/issues/197))
- Use rosdep keys that select Qt5 or Qt6 by platform ([#195](https://github.com/ros/ros_tutorials/issues/195))
- Use new ROSIDL aggregate CMake target ([#194](https://github.com/ros/ros_tutorials/issues/194))
- Use get\_package\_share\_path ([#193](https://github.com/ros/ros_tutorials/issues/193))
- fix bug loading turtle images ([#192](https://github.com/ros/ros_tutorials//issues/192))
- Updated deprecated ament\_index\_cpp API ([#190](https://github.com/ros/ros_tutorials/issues/190))
- Use qt6 as the default dependency from rosdep ([#189](https://github.com/ros/ros_tutorials/issues/189))
- get rid of deprecated rclcpp::spin\_some() ([#183](https://github.com/ros/ros_tutorials/issues/183))
- Support Qt6 ([#170](https://github.com/ros/ros_tutorials/issues/170))
- Add icon for Kilted Kaiju ([#180](https://github.com/ros/ros_tutorials/issues/180))
- Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, Shane Loretz, dcconner, mergify[bot]

<a id="turtlesim-msgs"></a>

## [turtlesim\_msgs](https://github.com/ros/ros_tutorials/tree/lyrical/turtlesim_msgs/CHANGELOG.rst)

- fix: swap action and message file group names in CMakeLists.txt ([#186](https://github.com/ros/ros_tutorials/issues/186)) ([#187](https://github.com/ros/ros_tutorials/issues/187))
- fix cmake deprecation ([#182](https://github.com/ros/ros_tutorials/issues/182))
- Contributors: mergify[bot], mosfet80

<a id="type-description-interfaces"></a>

## [type\_description\_interfaces](https://github.com/ros2/rcl_interfaces/tree/lyrical/type_description_interfaces/CHANGELOG.rst)

- Fix cmake deprecation ([#180](https://github.com/ros2/rcl_interfaces/issues/180))
- Contributors: mosfet80

<a id="uncrustify-vendor"></a>

## [uncrustify\_vendor](https://github.com/ament/uncrustify_vendor/tree/lyrical/CHANGELOG.rst)

- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#38](https://github.com/ament/uncrustify_vendor/issues/38))
- Contributors: Chris Lalancette

<a id="unique-identifier-msgs"></a>

## [unique\_identifier\_msgs](https://github.com/ros2/unique_identifier_msgs/tree/lyrical/CHANGELOG.rst)

- fix cmake deprecation ([#33](https://github.com/ros2/unique_identifier_msgs/issues/33))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#31](https://github.com/ros2/unique_identifier_msgs/issues/31))
- Contributors: Chris Lalancette, mosfet80

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/lyrical/urdf/CHANGELOG.rst)

- Remove `urdf_world/types.h` deprecation ([#54](https://github.com/ros2/urdf/issues/54))
- Fix CMAKE deprecation ([#48](https://github.com/ros2/urdf/issues/48))
- Removed tinyxml2\_vendor dependency ([#47](https://github.com/ros2/urdf/issues/47))
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/lyrical/urdf_parser_plugin/CHANGELOG.rst)

- Remove `urdf_world/types.h` deprecation ([#54](https://github.com/ros2/urdf/issues/54))
- Fix CMAKE deprecation ([#48](https://github.com/ros2/urdf/issues/48)) cmake version < then 3.10 is deprecated
- Contributors: Alejandro Hernández Cordero, mosfet80

<a id="urdfdom"></a>

## [urdfdom](https://github.com/ros/urdfdom/tree/lyrical/CHANGELOG.rst)

- Support for URDF Specification 1.2 \* Extend parsing of acceleration, deceleration and jerk limits from `limit` tag ([#212](https://github.com/ros/urdfdom/issues/212)) \* Update default limits for the joint limits and safety limits ([#249](https://github.com/ros/urdfdom/issues/249)) \* Add invalid data checks to the Geometry data ([#242](https://github.com/ros/urdfdom/issues/242)) \* Require urdfdom\_headers 3.0.0 ([#257](https://github.com/ros/urdfdom/issues/257))
- Use URDF\_MAJOR\_VERSION for SOVERSION ([#248](https://github.com/ros/urdfdom/issues/248))
- Revert “Extend parsing of acceleration, deceleration and jerk limits from `limit` tag ([#212](https://github.com/ros/urdfdom/issues/212))” This was a breaking change that will be released in 6.0.0
- Prevent CI from failing fast to allow all builds to complete ([#254](https://github.com/ros/urdfdom/issues/254))
- Remove `urdf_world/types.h` deprecation ([#251](https://github.com/ros/urdfdom/issues/251))
- Extend parsing of acceleration, deceleration and jerk limits from `limit` tag ([#212](https://github.com/ros/urdfdom/issues/212))
- ROS 2 CI: build urdfdom\_headers from source ([#246](https://github.com/ros/urdfdom/issues/246))
- Disable system workflow because `urdfdom_headers` isn’t available on Ubuntu 24.04 ([#240](https://github.com/ros/urdfdom/issues/240))
- Fix ROS 2 CI workflow by updating Ubuntu version and checkout action ([#239](https://github.com/ros/urdfdom/issues/239))
- Support for URDF Specification 1.1 \* Add support for capsule geometry type ([#238](https://github.com/ros/urdfdom/issues/238)) \* Add documentation about versioning \* Require version 2.1.0 of urdfdom\_headers Co-authored-by: Steve Peters <[scpeters@openrobotics.org](mailto:scpeters%40openrobotics.org)> \* Support quaternions in URDF 1.1 ([#235](https://github.com/ros/urdfdom/issues/235)) Co-authored-by: Guillaume Doisy <[doisyg@users.noreply.github.com](mailto:doisyg%40users.noreply.github.com)>
- Fix multiple format-string vulnerabilities in URDF parser logging ([#243](https://github.com/ros/urdfdom/issues/243)) User-controlled URDF content was passed directly to CONSOLE\_BRIDGE\_logError() at multiple call sites, allowing printf-style format string interpretation. All affected logging paths now use explicit “%s” format specifiers to ensure input is treated as data and to prevent information disclosure or undefined behavior.
- More logging format string fixes ([#244](https://github.com/ros/urdfdom/issues/244)) \* Add explicit “%s” format strings when logging \* Use %s format string instead of string addition
- Read cmake version from package.xml ([#236](https://github.com/ros/urdfdom/issues/236)) \* Use regex to match version string. Based on suggestion from Chris Lalancette. \* Require cmake minimum version 3.10 Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Revert “Quaternion in urdf (PR123 new attempt) (#231)” ([#231](https://github.com/ros/urdfdom/issues/231))
- Quaternion in urdf (PR123 new attempt) ([#194](https://github.com/ros/urdfdom/issues/194))
- Removed tinyxml2\_vendor dependency ([#225](https://github.com/ros/urdfdom/issues/225))
- Relax the version compatibility for urdfdom\_headers. ([#222](https://github.com/ros/urdfdom/issues/222))
- Removed deprecated code ([#217](https://github.com/ros/urdfdom/issues/217))
- Remove ROS 1 workflows and update ROS 2 ([#218](https://github.com/ros/urdfdom/issues/218))
- Improvements for the URDF xsd specification ([#200](https://github.com/ros/urdfdom/issues/200))
- Update ros2.yaml ([#214](https://github.com/ros/urdfdom/issues/214))
- fix: missing header ([#216](https://github.com/ros/urdfdom/issues/216))
- Contributors: Alejandro Hernández Cordero, Amin Ya, Chris Lalancette, Florencia, Guillaume Doisy, Jose Luis Rivero, Pierre Ballif, Sai Kishor Kothakota, Steve Peters, mosfet80

<a id="urdfdom-headers"></a>

## [urdfdom\_headers](https://github.com/ros/urdfdom_headers/tree/lyrical/CHANGELOG.rst)

- Update lower, upper, effort, and velocity default joint limits ([#95](https://github.com/ros/urdfdom_headers/issues/95))
- Clean up declaration of ModelInterface’s SharedPtrs ([#99](https://github.com/ros/urdfdom_headers/issues/99))
- Extend `JointLimits` class to include acceleration, deceleration and jerk limits ([#83](https://github.com/ros/urdfdom_headers/issues/83))
- Revert “Extend JointLimits class to include acceleration, deceleration and jerk limits ([#83](https://github.com/ros/urdfdom_headers/issues/83))” This was a breaking change that will be released in 3.0.0
- Clean up declaration of ModelInterface’s SharedPtrs ([#99](https://github.com/ros/urdfdom_headers/issues/99))
- Revert cleanup of ModelInterface’s SharedPtrs ([#33](https://github.com/ros/urdfdom_headers/issues/33))
- Revert fix for assumption that CMAKE\_INSTALL\_\*DIR paths are relative ([#90](https://github.com/ros/urdfdom_headers/issues/90)) ([#97](https://github.com/ros/urdfdom_headers/issues/97))
- Clean up declaration of ModelInterface’s SharedPtrs ([#33](https://github.com/ros/urdfdom_headers/issues/33))
- Fix assumption that CMAKE\_INSTALL\_\*DIR paths are relative ([#90](https://github.com/ros/urdfdom_headers/issues/90))
- Extend `JointLimits` class to include acceleration, deceleration and jerk limits ([#83](https://github.com/ros/urdfdom_headers/issues/83))
- Add support for capsule geometry type ([#94](https://github.com/ros/urdfdom_headers/issues/94))
- 2.0.2
- Read cmake version from package.xml ([#92](https://github.com/ros/urdfdom_headers/issues/92)) Use regex to match version string. Copied from [ros/urdfdom#236](https://github.com/ros/urdfdom/issues/236).
- quaternions in urdf (PR 51 new attempt) + bump version ([#77](https://github.com/ros/urdfdom_headers/issues/77))
- fix cmake deprecation ([#89](https://github.com/ros/urdfdom_headers/issues/89)) cmake version < then 3.10 is deprecated
- 2.0.0
- Remove all dependencies from the package.xml. ([#88](https://github.com/ros/urdfdom_headers/issues/88)) This package does not have any header dependencies, so we don’t need any of them here.
- Fix package.xml deps to use vendored packages ([#87](https://github.com/ros/urdfdom_headers/issues/87))
- add package.xml file from release repository ([#85](https://github.com/ros/urdfdom_headers/issues/85))
- Removed headers, implementation was deprecated and removed ([#86](https://github.com/ros/urdfdom_headers/issues/86))
- Remove CODEOWNERS. ([#81](https://github.com/ros/urdfdom_headers/issues/81)) It is outdated and no longer serving its intended purpose.
- Contributors: Aarav Gupta, Alejandro Hernández Cordero, Chris Lalancette, Guillaume Doisy, Jorge J. Perez, Lucien Morey, Michal Sojka, Robert Haschke, Sai Kishor Kothakota, Steve Peters, mosfet80

<a id="visualization-msgs"></a>

## [visualization\_msgs](https://github.com/ros2/common_interfaces/tree/lyrical/visualization_msgs/CHANGELOG.rst)

- Fix CMAKE deprecation ([#288](https://github.com/ros2/common_interfaces/issues/288))
- Contributors: mosfet80

<a id="yaml-cpp-vendor"></a>

## [yaml\_cpp\_vendor](https://github.com/ros2/yaml_cpp_vendor/tree/lyrical/CHANGELOG.rst)

- Replace ament\_vendor with cmake modules ([#56](https://github.com/ros2/yaml_cpp_vendor/issues/56))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#52](https://github.com/ros2/yaml_cpp_vendor/issues/52))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="zenoh-cpp-vendor"></a>

## [zenoh\_cpp\_vendor](https://github.com/ros2/rmw_zenoh/tree/lyrical/zenoh_cpp_vendor/CHANGELOG.rst)

- Use zenoh-cpp 481b71b fixing build with MSVC 2022 in C++20 mode ([#969](https://github.com/ros2/rmw_zenoh/issues/969))
- Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve synchronization with `undeclare` ([#964](https://github.com/ros2/rmw_zenoh/issues/964))
- Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0 ([#960](https://github.com/ros2/rmw_zenoh/issues/960))
- Revert patch of Cargo.lock with new Zenoh commit due to Windows test failures ([#959](https://github.com/ros2/rmw_zenoh/issues/959))
- Update Cargo.lock with new Zenoh commit ([#957](https://github.com/ros2/rmw_zenoh/issues/957))
- Build against `rust >= 1.75` for ROS Lyrical ([#945](https://github.com/ros2/rmw_zenoh/issues/945))
- Bump zenoh to 1.8.0 ([#935](https://github.com/ros2/rmw_zenoh/issues/935))
- Allow use of non-vendored Zenoh if present ([#908](https://github.com/ros2/rmw_zenoh/issues/908))
- Bump `zenoh` to 1.7.1 ([#870](https://github.com/ros2/rmw_zenoh/issues/870))
- Fix REP url locations ([#858](https://github.com/ros2/rmw_zenoh/issues/858))
- Bump zenoh to 1.6.2 ([#842](https://github.com/ros2/rmw_zenoh/issues/842))
- Bump Zenoh to 1.5.1 ([#774](https://github.com/ros2/rmw_zenoh/issues/774))
- Bump Zenoh to v1.5.0 ([#728](https://github.com/ros2/rmw_zenoh/issues/728))
- Change zenoh-c features to use its default + shared-memory + transport\_serial ([#692](https://github.com/ros2/rmw_zenoh/issues/692))
- Bump Zenoh to 1.4.0 ([#652](https://github.com/ros2/rmw_zenoh/issues/652))
- fix: pin rust toolchain to v1.75.0 ([#602](https://github.com/ros2/rmw_zenoh/issues/602))
- fix: use the right commit to bump zenoh to v1.3.2 ([#607](https://github.com/ros2/rmw_zenoh/issues/607))
- Contributors: ChenYing Kuo (CY), Julien Enoch, Shane Loretz, Tim Clephas, Yadunund, Yuyuan Yuan, Øystein Sture

<a id="zenoh-security-tools"></a>

## [zenoh\_security\_tools](https://github.com/ros2/rmw_zenoh/tree/lyrical/zenoh_security_tools/CHANGELOG.rst)

- Address outstanding TODO items ([#896](https://github.com/ros2/rmw_zenoh/issues/896))
- Removed tinyxml2\_vendor dependency ([#829](https://github.com/ros2/rmw_zenoh/issues/829))
- Fix commands in zenoh\_security\_tools README ([#814](https://github.com/ros2/rmw_zenoh/issues/814))
- Revert “fix: handle missing enclaves\_dir argument for zenoh\_security\_tools (#…” ([#802](https://github.com/ros2/rmw_zenoh/issues/802))
- Correct a description error in the zenoh\_security\_tools README ([#789](https://github.com/ros2/rmw_zenoh/issues/789))
- fix: handle missing enclaves\_dir argument for zenoh\_security\_tools ([#788](https://github.com/ros2/rmw_zenoh/issues/788))
- SROS: add ACL rules for TRANSIENT\_LOCAL pub/sub (fix [#753](https://github.com/ros2/rmw_zenoh/issues/753)) ([#779](https://github.com/ros2/rmw_zenoh/issues/779))
- Fix handling of enclave path in zenoh\_security\_tools ([#770](https://github.com/ros2/rmw_zenoh/issues/770))
- Update CMakeLists.txt ([#617](https://github.com/ros2/rmw_zenoh/issues/617))
- Fix warning on Windows ([#615](https://github.com/ros2/rmw_zenoh/issues/615))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Julien Enoch, Tomoya Fujita, Yadunund, mosfet80
