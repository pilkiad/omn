---
title: "ROS 2 Kilted Kaiju Complete Changelog"
docname: "Releases/Kilted-Kaiju-Complete-Changelog"
source: "Releases/Kilted-Kaiju-Complete-Changelog.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [Alphas](alpha-overview.md) | [Ardent Apalone ( ardent )](release-ardent-apalone.md) | [Beta 1 ( Asphalt )](beta1-overview.md) | [Beta 2 ( r2b2 )](beta2-overview.md) | [Beta 3 ( r2b3 )](beta3-overview.md)

<a id="ros-2-kilted-kaiju-complete-changelog"></a>

# ROS 2 Kilted Kaiju Complete Changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

Table of Contents

- [action\_msgs](#action-msgs)
- [action\_tutorials\_cpp](#action-tutorials-cpp)
- [action\_tutorials\_py](#action-tutorials-py)
- [ament\_clang\_format](#ament-clang-format)
- [ament\_clang\_tidy](#ament-clang-tidy)
- [ament\_cmake\_auto](#ament-cmake-auto)
- [ament\_cmake\_core](#ament-cmake-core)
- [ament\_cmake\_gen\_version\_h](#ament-cmake-gen-version-h)
- [ament\_cmake\_gtest](#ament-cmake-gtest)
- [ament\_cmake\_pytest](#ament-cmake-pytest)
- [ament\_cmake\_ros](#ament-cmake-ros)
- [ament\_cmake\_ros\_core](#ament-cmake-ros-core)
- [ament\_cmake\_target\_dependencies](#ament-cmake-target-dependencies)
- [ament\_cmake\_vendor\_package](#ament-cmake-vendor-package)
- [ament\_copyright](#ament-copyright)
- [ament\_cppcheck](#ament-cppcheck)
- [ament\_cpplint](#ament-cpplint)
- [ament\_flake8](#ament-flake8)
- [ament\_index\_python](#ament-index-python)
- [ament\_lint\_auto](#ament-lint-auto)
- [ament\_lint\_cmake](#ament-lint-cmake)
- [ament\_mypy](#ament-mypy)
- [ament\_package](#ament-package)
- [ament\_pclint](#ament-pclint)
- [ament\_pycodestyle](#ament-pycodestyle)
- [ament\_pyflakes](#ament-pyflakes)
- [ament\_uncrustify](#ament-uncrustify)
- [ament\_xmllint](#ament-xmllint)
- [builtin\_interfaces](#builtin-interfaces)
- [camera\_calibration\_parsers](#camera-calibration-parsers)
- [camera\_info\_manager](#camera-info-manager)
- [camera\_info\_manager\_py](#camera-info-manager-py)
- [composition](#composition)
- [demo\_nodes\_cpp](#demo-nodes-cpp)
- [demo\_nodes\_cpp\_native](#demo-nodes-cpp-native)
- [demo\_nodes\_py](#demo-nodes-py)
- [domain\_coordinator](#domain-coordinator)
- [dummy\_map\_server](#dummy-map-server)
- [dummy\_robot\_bringup](#dummy-robot-bringup)
- [dummy\_sensors](#dummy-sensors)
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
- [google\_benchmark\_vendor](#google-benchmark-vendor)
- [gtest\_vendor](#gtest-vendor)
- [gz\_cmake\_vendor](#gz-cmake-vendor)
- [gz\_math\_vendor](#gz-math-vendor)
- [gz\_utils\_vendor](#gz-utils-vendor)
- [image\_tools](#image-tools)
- [image\_transport](#image-transport)
- [image\_transport\_py](#image-transport-py)
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
- [liblz4\_vendor](#liblz4-vendor)
- [libstatistics\_collector](#libstatistics-collector)
- [libyaml\_vendor](#libyaml-vendor)
- [lifecycle](#lifecycle)
- [lifecycle\_py](#lifecycle-py)
- [logging\_demo](#logging-demo)
- [lttngpy](#lttngpy)
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
- [point\_cloud\_transport](#point-cloud-transport)
- [point\_cloud\_transport\_py](#point-cloud-transport-py)
- [python\_orocos\_kdl\_vendor](#python-orocos-kdl-vendor)
- [python\_qt\_binding](#python-qt-binding)
- [qt\_dotgraph](#qt-dotgraph)
- [qt\_gui\_cpp](#qt-gui-cpp)
- [quality\_of\_service\_demo\_cpp](#quality-of-service-demo-cpp)
- [quality\_of\_service\_demo\_py](#quality-of-service-demo-py)
- [rcl](#rcl)
- [rcl\_action](#rcl-action)
- [rcl\_lifecycle](#rcl-lifecycle)
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
- [rmw\_security\_common](#rmw-security-common)
- [rmw\_test\_fixture](#rmw-test-fixture)
- [rmw\_test\_fixture\_implementation](#rmw-test-fixture-implementation)
- [rmw\_zenoh\_cpp](#rmw-zenoh-cpp)
- [robot\_state\_publisher](#robot-state-publisher)
- [ros2action](#ros2action)
- [ros2bag](#ros2bag)
- [ros2cli](#ros2cli)
- [ros2doctor](#ros2doctor)
- [ros2launch](#ros2launch)
- [ros2lifecycle](#ros2lifecycle)
- [ros2lifecycle\_test\_fixtures](#ros2lifecycle-test-fixtures)
- [ros2node](#ros2node)
- [ros2param](#ros2param)
- [ros2pkg](#ros2pkg)
- [ros2run](#ros2run)
- [ros2service](#ros2service)
- [ros2test](#ros2test)
- [ros2topic](#ros2topic)
- [ros2trace](#ros2trace)
- [ros\_environment](#ros-environment)
- [rosbag2](#rosbag2)
- [rosbag2\_compression](#rosbag2-compression)
- [rosbag2\_cpp](#rosbag2-cpp)
- [rosbag2\_examples\_cpp](#rosbag2-examples-cpp)
- [rosbag2\_examples\_py](#rosbag2-examples-py)
- [rosbag2\_py](#rosbag2-py)
- [rosbag2\_storage](#rosbag2-storage)
- [rosbag2\_storage\_mcap](#rosbag2-storage-mcap)
- [rosbag2\_storage\_sqlite3](#rosbag2-storage-sqlite3)
- [rosbag2\_test\_common](#rosbag2-test-common)
- [rosbag2\_test\_msgdefs](#rosbag2-test-msgdefs)
- [rosbag2\_tests](#rosbag2-tests)
- [rosbag2\_transport](#rosbag2-transport)
- [rosidl\_adapter](#rosidl-adapter)
- [rosidl\_cli](#rosidl-cli)
- [rosidl\_core\_generators](#rosidl-core-generators)
- [rosidl\_core\_runtime](#rosidl-core-runtime)
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
- [rosidl\_typesupport\_introspection\_c](#rosidl-typesupport-introspection-c)
- [rosidl\_typesupport\_introspection\_cpp](#rosidl-typesupport-introspection-cpp)
- [rosidl\_typesupport\_introspection\_tests](#rosidl-typesupport-introspection-tests)
- [rosidl\_typesupport\_tests](#rosidl-typesupport-tests)
- [rpyutils](#rpyutils)
- [rqt\_bag](#rqt-bag)
- [rqt\_bag\_plugins](#rqt-bag-plugins)
- [rqt\_console](#rqt-console)
- [rqt\_graph](#rqt-graph)
- [rqt\_gui](#rqt-gui)
- [rqt\_gui\_cpp](#rqt-gui-cpp)
- [rqt\_gui\_py](#rqt-gui-py)
- [rqt\_plot](#rqt-plot)
- [rqt\_publisher](#rqt-publisher)
- [rqt\_py\_common](#rqt-py-common)
- [rqt\_py\_console](#rqt-py-console)
- [rqt\_service\_caller](#rqt-service-caller)
- [rqt\_shell](#rqt-shell)
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
- [rviz\_resource\_interfaces](#rviz-resource-interfaces)
- [rviz\_visual\_testing\_framework](#rviz-visual-testing-framework)
- [sensor\_msgs](#sensor-msgs)
- [sensor\_msgs\_py](#sensor-msgs-py)
- [service\_msgs](#service-msgs)
- [sqlite3\_vendor](#sqlite3-vendor)
- [sros2](#sros2)
- [test\_cli](#test-cli)
- [test\_cli\_remapping](#test-cli-remapping)
- [test\_communication](#test-communication)
- [test\_interface\_files](#test-interface-files)
- [test\_launch\_ros](#test-launch-ros)
- [test\_msgs](#test-msgs)
- [test\_osrf\_testing\_tools\_cpp](#test-osrf-testing-tools-cpp)
- [test\_quality\_of\_service](#test-quality-of-service)
- [test\_rclcpp](#test-rclcpp)
- [test\_rmw\_implementation](#test-rmw-implementation)
- [test\_ros2trace](#test-ros2trace)
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
- [turtlesim](#turtlesim)
- [turtlesim\_msgs](#turtlesim-msgs)
- [type\_description\_interfaces](#type-description-interfaces)
- [unique\_identifier\_msgs](#unique-identifier-msgs)
- [urdf](#urdf)
- [urdf\_parser\_plugin](#urdf-parser-plugin)
- [zenoh\_cpp\_vendor](#zenoh-cpp-vendor)
- [zenoh\_security\_tools](#zenoh-security-tools)

<a id="action-msgs"></a>

## [action\_msgs](https://github.com/ros2/rcl_interfaces/tree/kilted/action_msgs/CHANGELOG.rst)

- Add missing build\_export\_depend on rosidl\_core\_runtime ([#165](https://github.com/ros2/rcl_interfaces/issues/165))
- Contributors: Scott K Logan

<a id="action-tutorials-cpp"></a>

## [action\_tutorials\_cpp](https://github.com/ros2/demos/tree/kilted/action_tutorials/action_tutorials_cpp/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Update action cpp demos to support setting introspection ([#709](https://github.com/ros2/demos/issues/709)) \* Update action cpp demos to support setting introspection \* Add the missing header file declaration ———
- Remove action\_tutorials\_interfaces. ([#701](https://github.com/ros2/demos/issues/701))
- Removed outdated comment ([#699](https://github.com/ros2/demos/issues/699))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, mosfet80

<a id="action-tutorials-py"></a>

## [action\_tutorials\_py](https://github.com/ros2/demos/tree/kilted/action_tutorials/action_tutorials_py/CHANGELOG.rst)

- Update action python demos to support setting introspection ([#708](https://github.com/ros2/demos/issues/708)) \* Update action python demos to support setting introspection \* Correct the errors in the document ———
- Add test\_xmllint.py to all of the ament\_python packages. ([#704](https://github.com/ros2/demos/issues/704))
- Remove action\_tutorials\_interfaces. ([#701](https://github.com/ros2/demos/issues/701))
- Change all of the demos to use the new rclpy context manager. ([#694](https://github.com/ros2/demos/issues/694))
- Contributors: Barry Xu, Chris Lalancette

<a id="ament-clang-format"></a>

## [ament\_clang\_format](https://github.com/ament/ament_lint/tree/kilted/ament_clang_format/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-clang-tidy"></a>

## [ament\_clang\_tidy](https://github.com/ament/ament_lint/tree/kilted/ament_clang_tidy/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- ament\_clang\_tidy - Fix Reporting when WarningsAsErrors is specified in config ([#397](https://github.com/ament/ament_lint/issues/397))
- Contributors: Chris Lalancette, Matt Condino

<a id="ament-cmake-auto"></a>

## [ament\_cmake\_auto](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_auto/CHANGELOG.rst)

- Fix headers destination installed by ament\_auto\_package ([#540](https://github.com/ament/ament_cmake/issues/540))
- Add ament\_auto\_depend\_on\_packages to replace ament\_target\_dependencies ([#571](https://github.com/ament/ament_cmake/issues/571))
- More specific prefix in some cmake\_parse\_argument calls ([#523](https://github.com/ament/ament_cmake/issues/523))
- Contributors: Kevin Egger, Kotaro Yoshimoto, Shane Loretz

<a id="ament-cmake-core"></a>

## [ament\_cmake\_core](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_core/CHANGELOG.rst)

- Create destination directory during symlink install ([#569](https://github.com/ament/ament_cmake/issues/569))
- Support generator expressions when symlinking install(FILES) ([#560](https://github.com/ament/ament_cmake/issues/560))
- Always symlink TARGET\_{LINKER,SONAME}\_FILE on libraries ([#535](https://github.com/ament/ament_cmake/issues/535))
- Fix symlink install of versioned libs on macOS ([#558](https://github.com/ament/ament_cmake/issues/558))
- More specific prefix in some cmake\_parse\_argument calls ([#523](https://github.com/ament/ament_cmake/issues/523))
- Contributors: Ezra Brooks, Kevin Egger, Scott K Logan

<a id="ament-cmake-gen-version-h"></a>

## [ament\_cmake\_gen\_version\_h](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_gen_version_h/CHANGELOG.rst)

- Add ALL target for ament\_generate\_version\_header target. ([#526](https://github.com/ament/ament_cmake/issues/526))
- Contributors: Chris Lalancette

<a id="ament-cmake-gtest"></a>

## [ament\_cmake\_gtest](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_gtest/CHANGELOG.rst)

- set search path args and then append ([#543](https://github.com/ament/ament_cmake/issues/543))
- Contributors: Will

<a id="ament-cmake-pytest"></a>

## [ament\_cmake\_pytest](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_pytest/CHANGELOG.rst)

- Don’t write Python bytecode when invoking pytest ([#533](https://github.com/ament/ament_cmake/issues/533))
- Contributors: Scott K Logan

<a id="ament-cmake-ros"></a>

## [ament\_cmake\_ros](https://github.com/ros2/ament_cmake_ros/tree/kilted/ament_cmake_ros/CHANGELOG.rst)

- Add ament\_add\_ros\_isolated\_{gmock,gtest}\_test macros ([#29](https://github.com/ros2/ament_cmake_ros/issues/29))
- Switch from ‘domain\_coordinator’ to ‘rmw\_test\_fixture’ ([#28](https://github.com/ros2/ament_cmake_ros/issues/28))
- Add ament\_add\_ros\_isolated\_test function ([#27](https://github.com/ros2/ament_cmake_ros/issues/27))
- Split generic parts of ament\_cmake\_ros into \_core package ([#20](https://github.com/ros2/ament_cmake_ros/issues/20))
- Contributors: Scott K Logan

<a id="ament-cmake-ros-core"></a>

## [ament\_cmake\_ros\_core](https://github.com/ros2/ament_cmake_ros/tree/kilted/ament_cmake_ros_core/CHANGELOG.rst)

- Add missing build\_export\_depend on ament\_cmake\_libraries ([#37](https://github.com/ros2/ament_cmake_ros/issues/37))
- Split generic parts of ament\_cmake\_ros into \_core package ([#20](https://github.com/ros2/ament_cmake_ros/issues/20))
- Contributors: Scott K Logan

<a id="ament-cmake-target-dependencies"></a>

## [ament\_cmake\_target\_dependencies](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_target_dependencies/CHANGELOG.rst)

- Deprecate ament\_target\_dependencies() ([#572](https://github.com/ament/ament_cmake/issues/572))
- Contributors: Shane Loretz

<a id="ament-cmake-vendor-package"></a>

## [ament\_cmake\_vendor\_package](https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_vendor_package/CHANGELOG.rst)

- Add explicit git dependency from ament\_cmake\_vendor\_package ([#554](https://github.com/ament/ament_cmake/issues/554))
- Contributors: Scott K Logan

<a id="ament-copyright"></a>

## [ament\_copyright](https://github.com/ament/ament_lint/tree/kilted/ament_copyright/CHANGELOG.rst)

- Improve ament\_copyright performance drastically. ([#515](https://github.com/ament/ament_lint/issues/515))
- Fix error path for search\_copyright\_information. ([#491](https://github.com/ament/ament_lint/issues/491))
- Contributors: Chris Lalancette

<a id="ament-cppcheck"></a>

## [ament\_cppcheck](https://github.com/ament/ament_lint/tree/kilted/ament_cppcheck/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-cpplint"></a>

## [ament\_cpplint](https://github.com/ament/ament_lint/tree/kilted/ament_cpplint/CHANGELOG.rst)

- Enable a quiet mode for cpplint ([#532](https://github.com/ament/ament_lint/issues/532))
- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette, Nils-Christian Iseke

<a id="ament-flake8"></a>

## [ament\_flake8](https://github.com/ament/ament_lint/tree/kilted/ament_flake8/CHANGELOG.rst)

- Add the rest of the flake8 plugins as dependencies. ([#503](https://github.com/ament/ament_lint/issues/503))
- Contributors: Chris Lalancette

<a id="ament-index-python"></a>

## [ament\_index\_python](https://github.com/ament/ament_index/tree/kilted/ament_index_python/CHANGELOG.rst)

- Add py.typed to package\_data ([#100](https://github.com/ament/ament_index/issues/100))
- Add test\_xmllint to ament\_index\_python. ([#96](https://github.com/ament/ament_index/issues/96))
- Add ament\_mypy unit test and export types ([#95](https://github.com/ament/ament_index/issues/95))
- Contributors: Chris Lalancette, Michael Carlstrom

<a id="ament-lint-auto"></a>

## [ament\_lint\_auto](https://github.com/ament/ament_lint/tree/kilted/ament_lint_auto/CHANGELOG.rst)

- Add docu for AMENT\_LINT\_AUTO\_EXCLUDE ([#524](https://github.com/ament/ament_lint/issues/524))
- Contributors: Alexander Reimann

<a id="ament-lint-cmake"></a>

## [ament\_lint\_cmake](https://github.com/ament/ament_lint/tree/kilted/ament_lint_cmake/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-mypy"></a>

## [ament\_mypy](https://github.com/ament/ament_lint/tree/kilted/ament_mypy/CHANGELOG.rst)

- Fix Windows Regression by removing removesuffix() ([#530](https://github.com/ament/ament_lint/issues/530))
- Export typing information ([#487](https://github.com/ament/ament_lint/issues/487))
- Add support for type stubs ([#516](https://github.com/ament/ament_lint/issues/516))
- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette, Michael Carlstrom

<a id="ament-package"></a>

## [ament\_package](https://github.com/ament/ament_package/tree/kilted/CHANGELOG.rst)

- Simplify removing leading and trailing separators ([#152](https://github.com/ament/ament_package/issues/152))
- Remove CODEOWNERS and mirror-rolling-to-master. ([#149](https://github.com/ament/ament_package/issues/149))
- Always consider .dsv files, even when no shell specific script exists ([#147](https://github.com/ament/ament_package/issues/147))
- Contributors: Addisu Z. Taddese, Chris Lalancette, Rob Woolley

<a id="ament-pclint"></a>

## [ament\_pclint](https://github.com/ament/ament_lint/tree/kilted/ament_pclint/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-pycodestyle"></a>

## [ament\_pycodestyle](https://github.com/ament/ament_lint/tree/kilted/ament_pycodestyle/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-pyflakes"></a>

## [ament\_pyflakes](https://github.com/ament/ament_lint/tree/kilted/ament_pyflakes/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-uncrustify"></a>

## [ament\_uncrustify](https://github.com/ament/ament_lint/tree/kilted/ament_uncrustify/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="ament-xmllint"></a>

## [ament\_xmllint](https://github.com/ament/ament_lint/tree/kilted/ament_xmllint/CHANGELOG.rst)

- Add ament\_xmllint testing for all packages that we can. ([#508](https://github.com/ament/ament_lint/issues/508))
- Contributors: Chris Lalancette

<a id="builtin-interfaces"></a>

## [builtin\_interfaces](https://github.com/ros2/rcl_interfaces/tree/kilted/builtin_interfaces/CHANGELOG.rst)

- Add missing build\_export\_depend on rosidl\_core\_runtime ([#165](https://github.com/ros2/rcl_interfaces/issues/165))
- Contributors: Scott K Logan

<a id="camera-calibration-parsers"></a>

## [camera\_calibration\_parsers](https://github.com/ros-perception/image_common/tree/kilted/camera_calibration_parsers/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#345](https://github.com/ros-perception/image_common/issues/345))
- Added common linters to camera\_calibration\_parsers ([#317](https://github.com/ros-perception/image_common/issues/317))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="camera-info-manager"></a>

## [camera\_info\_manager](https://github.com/ros-perception/image_common/tree/kilted/camera_info_manager/CHANGELOG.rst)

- Add optional namespace to /set\_camera\_info service in CameraInfoManager ([#324](https://github.com/ros-perception/image_common/issues/324))
- Added common test to camera info manager ([#318](https://github.com/ros-perception/image_common/issues/318))
- Contributors: Alejandro Hernández Cordero, Jan Hernas

<a id="camera-info-manager-py"></a>

## [camera\_info\_manager\_py](https://github.com/ros-perception/image_common/tree/kilted/camera_info_manager_py/CHANGELOG.rst)

- Cleanup of camera\_info\_manager\_py. ([#340](https://github.com/ros-perception/image_common/issues/340))
- Add `camera_info_manager_py` ([#335](https://github.com/ros-perception/image_common/issues/335))
- Bump package version to synchronize with image\_common
- Ros2 ([#2](https://github.com/clearpathrobotics/camera_info_manager_py/issues/2)) \* Run magic converter \* Ament\_python package \* Fix some imports \* Remove references to cpp camera info manager. Disable tests \* Linting \* Fully Remove old tests \* Add lint tests \* Final tests \* Remove pep257 from depends
- changelog
- added CPR maintainer
- Release to Melodic and Noetic
- Only use rostest when testing enabled, thanks to Lukas Bulwahn.
- Move repository to ros-perception.
- Add namespace parameter to constructor, so a driver can handle multiple cameras. Enhancement thanks to Martin Llofriu.
- Make unit tests conditional on `CATKIN_ENABLE_TESTING`.
- Release to Groovy and Hydro.
- Set null calibration even when URL invalid (#7).
- Release to Groovy and Hydro.
- Convert to catkin.
- Remove roslib dependency.
- Release to Groovy and Hydro.
- Initial Python camera\_info\_manager release to Fuerte.
- Contributors: Alejandro Hernández Cordero, Chris Iverach-Brereton, Chris Lalancette, Jack O’Quin, José Mastrangelo, Lucas Walter, Lukas Bulwahn, Martin Pecka, Michael Hosmar, mllofriu

<a id="composition"></a>

## [composition](https://github.com/ros2/demos/tree/kilted/composition/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Fix typo in composition comment ([#703](https://github.com/ros2/demos/issues/703))
- Change references from “jazzy” to “rolling” on the rolling branch. ([#687](https://github.com/ros2/demos/issues/687))
- [composition] add launch action console output in the verify section ([#677](https://github.com/ros2/demos/issues/677))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Mikael Arguedas, Shane Loretz, mosfet80

<a id="demo-nodes-cpp"></a>

## [demo\_nodes\_cpp](https://github.com/ros2/demos/tree/kilted/demo_nodes_cpp/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- [demo\_nodes\_cpp] some readme and executable name fixups ([#678](https://github.com/ros2/demos/issues/678))
- Fix gcc warnings when building with optimizations. ([#672](https://github.com/ros2/demos/issues/672))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael Arguedas, mosfet80

<a id="demo-nodes-cpp-native"></a>

## [demo\_nodes\_cpp\_native](https://github.com/ros2/demos/tree/kilted/demo_nodes_cpp_native/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Shane Loretz, mosfet80

<a id="demo-nodes-py"></a>

## [demo\_nodes\_py](https://github.com/ros2/demos/tree/kilted/demo_nodes_py/CHANGELOG.rst)

- Revert “Revert “fix loading parameter behavior from yaml file. ([#656](https://github.com/ros2/demos/issues/656))” ([#660](https://github.com/ros2/demos/issues/660))” ([#661](https://github.com/ros2/demos/issues/661))
- Add test\_xmllint.py to all of the ament\_python packages. ([#704](https://github.com/ros2/demos/issues/704))
- Change all of the demos to use the new rclpy context manager. ([#694](https://github.com/ros2/demos/issues/694))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="domain-coordinator"></a>

## [domain\_coordinator](https://github.com/ros2/ament_cmake_ros/tree/kilted/domain_coordinator/CHANGELOG.rst)

- Add test\_xmllint to domain\_coordinator. ([#17](https://github.com/ros2/ament_cmake_ros/issues/17))
- Contributors: Chris Lalancette

<a id="dummy-map-server"></a>

## [dummy\_map\_server](https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_map_server/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Shane Loretz, mosfet80

<a id="dummy-robot-bringup"></a>

## [dummy\_robot\_bringup](https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_robot_bringup/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Contributors: mosfet80

<a id="dummy-sensors"></a>

## [dummy\_sensors](https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_sensors/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Update dummy\_sensors readme to echo the correct topic ([#675](https://github.com/ros2/demos/issues/675))
- Contributors: Shane Loretz, jmackay2, mosfet80

<a id="examples-rclcpp-async-client"></a>

## [examples\_rclcpp\_async\_client](https://github.com/ros2/examples/tree/kilted/rclcpp/services/async_client/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-cbg-executor"></a>

## [examples\_rclcpp\_cbg\_executor](https://github.com/ros2/examples/tree/kilted/rclcpp/executors/cbg_executor/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-action-client"></a>

## [examples\_rclcpp\_minimal\_action\_client](https://github.com/ros2/examples/tree/kilted/rclcpp/actions/minimal_action_client/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Removed outdated comment ([#388](https://github.com/ros2/examples/issues/388))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="examples-rclcpp-minimal-action-server"></a>

## [examples\_rclcpp\_minimal\_action\_server](https://github.com/ros2/examples/tree/kilted/rclcpp/actions/minimal_action_server/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Removed outdated comment ([#388](https://github.com/ros2/examples/issues/388))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="examples-rclcpp-minimal-client"></a>

## [examples\_rclcpp\_minimal\_client](https://github.com/ros2/examples/tree/kilted/rclcpp/services/minimal_client/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-composition"></a>

## [examples\_rclcpp\_minimal\_composition](https://github.com/ros2/examples/tree/kilted/rclcpp/composition/minimal_composition/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-publisher"></a>

## [examples\_rclcpp\_minimal\_publisher](https://github.com/ros2/examples/tree/kilted/rclcpp/topics/minimal_publisher/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-service"></a>

## [examples\_rclcpp\_minimal\_service](https://github.com/ros2/examples/tree/kilted/rclcpp/services/minimal_service/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-subscriber"></a>

## [examples\_rclcpp\_minimal\_subscriber](https://github.com/ros2/examples/tree/kilted/rclcpp/topics/minimal_subscriber/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-minimal-timer"></a>

## [examples\_rclcpp\_minimal\_timer](https://github.com/ros2/examples/tree/kilted/rclcpp/timers/minimal_timer/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-multithreaded-executor"></a>

## [examples\_rclcpp\_multithreaded\_executor](https://github.com/ros2/examples/tree/kilted/rclcpp/executors/multithreaded_executor/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclcpp-wait-set"></a>

## [examples\_rclcpp\_wait\_set](https://github.com/ros2/examples/tree/kilted/rclcpp/wait_set/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#404](https://github.com/ros2/examples/issues/404))
- Contributors: Shane Loretz

<a id="examples-rclpy-executors"></a>

## [examples\_rclpy\_executors](https://github.com/ros2/examples/tree/kilted/rclpy/executors/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-guard-conditions"></a>

## [examples\_rclpy\_guard\_conditions](https://github.com/ros2/examples/tree/kilted/rclpy/guard_conditions/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-minimal-action-client"></a>

## [examples\_rclpy\_minimal\_action\_client](https://github.com/ros2/examples/tree/kilted/rclpy/actions/minimal_action_client/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-minimal-action-server"></a>

## [examples\_rclpy\_minimal\_action\_server](https://github.com/ros2/examples/tree/kilted/rclpy/actions/minimal_action_server/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Add guard on Python single goal action server example ([#380](https://github.com/ros2/examples/issues/380))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette, Ruddick Lawrence

<a id="examples-rclpy-minimal-client"></a>

## [examples\_rclpy\_minimal\_client](https://github.com/ros2/examples/tree/kilted/rclpy/services/minimal_client/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Use a single executor instance for spinning in client\_async\_callback. ([#382](https://github.com/ros2/examples/issues/382))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-minimal-publisher"></a>

## [examples\_rclpy\_minimal\_publisher](https://github.com/ros2/examples/tree/kilted/rclpy/topics/minimal_publisher/CHANGELOG.rst)

- Address flake8 errors for examples\_rclpy\_minimal\_publisher ([#410](https://github.com/ros2/examples/issues/410))
- Add publisher\_member\_function\_with\_wait\_for\_all\_acked.py ([#407](https://github.com/ros2/examples/issues/407))
- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="examples-rclpy-minimal-service"></a>

## [examples\_rclpy\_minimal\_service](https://github.com/ros2/examples/tree/kilted/rclpy/services/minimal_service/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-minimal-subscriber"></a>

## [examples\_rclpy\_minimal\_subscriber](https://github.com/ros2/examples/tree/kilted/rclpy/topics/minimal_subscriber/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-rclpy-pointcloud-publisher"></a>

## [examples\_rclpy\_pointcloud\_publisher](https://github.com/ros2/examples/tree/kilted/rclpy/topics/pointcloud_publisher/CHANGELOG.rst)

- Add in ament\_xmllint for the ament\_python packages. ([#397](https://github.com/ros2/examples/issues/397))
- Switch to using the rclpy context manager everywhere. ([#389](https://github.com/ros2/examples/issues/389))
- Update the shutdown handling in all of the Python examples. ([#379](https://github.com/ros2/examples/issues/379))
- Contributors: Chris Lalancette

<a id="examples-tf2-py"></a>

## [examples\_tf2\_py](https://github.com/ros2/geometry2/tree/kilted/examples_tf2_py/CHANGELOG.rst)

- Add in test\_xmllint for geometry2 python packages. ([#725](https://github.com/ros2/geometry2/issues/725))
- Switch to using a context manager for the python examples. ([#700](https://github.com/ros2/geometry2/issues/700)) That way we can be sure to always clean up, but use less code doing so.
- Contributors: Chris Lalancette

<a id="foonathan-memory-vendor"></a>

## [foonathan\_memory\_vendor](https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst)

- Improve mechanism to find an installation of foonathan\_memory (#67)

<a id="geometry2"></a>

## [geometry2](https://github.com/ros2/geometry2/tree/kilted/geometry2/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: mosfet80

<a id="geometry-msgs"></a>

## [geometry\_msgs](https://github.com/ros2/common_interfaces/tree/kilted/geometry_msgs/CHANGELOG.rst)

- Complete Removal of PoseStampedArray ([#270](https://github.com/ros2/common_interfaces/issues/270))
- Move geometry\_msgs/PoseStampedArray to nav\_msgs/Goals ([#269](https://github.com/ros2/common_interfaces/issues/269))
- Add PoseStampedArray ([#262](https://github.com/ros2/common_interfaces/issues/262))
- Contributors: Tony Najjar, Tully Foote

<a id="gmock-vendor"></a>

## [gmock\_vendor](https://github.com/ament/googletest/tree/kilted/googlemock/CHANGELOG.rst)

- Bump minimum CMake version to 3.15 ([#31](https://github.com/ament/googletest/issues/31))
- Contributors: mosfet80

<a id="google-benchmark-vendor"></a>

## [google\_benchmark\_vendor](https://github.com/ament/google_benchmark_vendor/tree/kilted/CHANGELOG.rst)

- Bump minimum CMake version to 3.10 ([#35](https://github.com/ament/google_benchmark_vendor/issues/35))
- Remove CODEOWNERS and mirror-rolling-to-main workflow. ([#31](https://github.com/ament/google_benchmark_vendor/issues/31))
- Contributors: Chris Lalancette, mosfet80

<a id="gtest-vendor"></a>

## [gtest\_vendor](https://github.com/ament/googletest/tree/kilted/googletest/CHANGELOG.rst)

- Bump minimum CMake version to 3.15 ([#33](https://github.com/ament/googletest/issues/33))
- Contributors: mosfet80

<a id="gz-cmake-vendor"></a>

## [gz\_cmake\_vendor](https://github.com/gazebo-release/gz_cmake_vendor/tree/kilted/CHANGELOG.rst)

- Bump version to 4.1.1 ([#13](https://github.com/gazebo-release/gz_cmake_vendor/issues/13))
- Bump version to 4.1.0 ([#11](https://github.com/gazebo-release/gz_cmake_vendor/issues/11))
- Bump version to 4.0.0 ([#10](https://github.com/gazebo-release/gz_cmake_vendor/issues/10))
- Fixes the cmake-config used during find\_package ([#8](https://github.com/gazebo-release/gz_cmake_vendor/issues/8)) The provided cmake-config was not actually working if one did `` ` find_package(gz_cmake_vendor) find_package(gz-cmake) ` `` This because the config file tried to create aliases to targets that don’t exist. For example, gz-cmake4::gz-cmake4 is not exported by gz-cmake.
- Remove the BUILD\_DOCS cmake argument. ([#9](https://github.com/gazebo-release/gz_cmake_vendor/issues/9)) It is apparently deprecated in newer Gazebo.
- Apply prerelease suffix and remove patch ([#7](https://github.com/gazebo-release/gz_cmake_vendor/issues/7))
- Upgrade to Ionic
- Contributors: Addisu Z. Taddese, Chris Lalancette, Steve Peters

<a id="gz-math-vendor"></a>

## [gz\_math\_vendor](https://github.com/gazebo-release/gz_math_vendor/tree/kilted/CHANGELOG.rst)

- Bump version to 8.1.1 ([#10](https://github.com/gazebo-release/gz_math_vendor/issues/10))
- Bump version to 8.1.0 ([#8](https://github.com/gazebo-release/gz_math_vendor/issues/8)) \* This is a rerelease since #7 did not actually bump the version of the vendored package.
- Bump version to 8.1.0 ([#7](https://github.com/gazebo-release/gz_math_vendor/issues/7))
- Bump version to 8.0.0 ([#5](https://github.com/gazebo-release/gz_math_vendor/issues/5))
- Apply prerelease suffix ([#4](https://github.com/gazebo-release/gz_math_vendor/issues/4))
- Upgrade to Ionic
- Update vendored package version to 7.5.0
- Contributors: Addisu Z. Taddese, Carlos Agüero, Michael Carroll

<a id="gz-utils-vendor"></a>

## [gz\_utils\_vendor](https://github.com/gazebo-release/gz_utils_vendor/tree/kilted/CHANGELOG.rst)

- Bump version to 3.1.1 ([#10](https://github.com/gazebo-release/gz_utils_vendor/issues/10))
- Bump version to 3.1.0 ([#8](https://github.com/gazebo-release/gz_utils_vendor/issues/8))
- Bump version to 3.0.0 ([#7](https://github.com/gazebo-release/gz_utils_vendor/issues/7))
- Add in a dependency on spdlog\_vendor. ([#6](https://github.com/gazebo-release/gz_utils_vendor/issues/6)) \* Add in a dependency on spdlog\_vendor. That way when building on e.g. Windows, the paths to spdlog will be setup properly before trying to build this vendor package. \* Also remove the spdlog dependency. That’s because we will just depend on the vendor package to provide that dependency for us as necessary. ———
- Remove the BUILD\_DOCS cmake argument. ([#5](https://github.com/gazebo-release/gz_utils_vendor/issues/5)) It is apparently deprecated in newer Gazebo.
- Apply prerelease suffix ([#4](https://github.com/gazebo-release/gz_utils_vendor/issues/4))
- Upgrade to Ionic
- Contributors: Addisu Z. Taddese, Carlos Agüero, Chris Lalancette, Michael Carroll

<a id="image-tools"></a>

## [image\_tools](https://github.com/ros2/demos/tree/kilted/image_tools/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Lint image\_tools/CMakeLists.txt ([#712](https://github.com/ros2/demos/issues/712))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Contributors: Alejandro Hernández Cordero, mosfet80, yadunund

<a id="image-transport"></a>

## [image\_transport](https://github.com/ros-perception/image_common/tree/kilted/image_transport/CHANGELOG.rst)

- Remove windows warnings ([#350](https://github.com/ros-perception/image_common/issues/350))
- Add `rclcpp::shutdown` ([#347](https://github.com/ros-perception/image_common/issues/347))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#345](https://github.com/ros-perception/image_common/issues/345))
- feat: python bindings for image\_transport and publish ([#323](https://github.com/ros-perception/image_common/issues/323)) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Apply remappings to base topic before creating transport-specific topics ([#326](https://github.com/ros-perception/image_common/issues/326))
- Add lazy subscription to republisher ([#325](https://github.com/ros-perception/image_common/issues/325))
- Fix node name ([#321](https://github.com/ros-perception/image_common/issues/321))
- Updated deprecated message filter headers ([#320](https://github.com/ros-perception/image_common/issues/320))
- Removed outdated comment ([#319](https://github.com/ros-perception/image_common/issues/319))
- Preparing for qos deprecation ([#315](https://github.com/ros-perception/image_common/issues/315))
- Removed warning ([#312](https://github.com/ros-perception/image_common/issues/312))
- Support zero-copy intra-process publishing ([#306](https://github.com/ros-perception/image_common/issues/306))
- Add missing sub and pub options ([#308](https://github.com/ros-perception/image_common/issues/308)) Co-authored-by: Angsa Deployment Team <[team@angsa-robotics.com](mailto:team%40angsa-robotics.com)>
- Contributors: Alejandro Hernández Cordero, Błażej Sowa, Földi Tamás, Lucas Wendland, Michal Sojka, Shane Loretz, Tony Najjar, Yuyuan Yuan

<a id="image-transport-py"></a>

## [image\_transport\_py](https://github.com/ros-perception/image_common/tree/kilted/image_transport_py/CHANGELOG.rst)

- Add in python3-dev build dependency ([#334](https://github.com/ros-perception/image_common/issues/334))
- feat: python bindings for image\_transport and publish ([#323](https://github.com/ros-perception/image_common/issues/323)) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Contributors: Chris Lalancette, Földi Tamás

<a id="interactive-markers"></a>

## [interactive\_markers](https://github.com/ros-visualization/interactive_markers/tree/kilted/CHANGELOG.rst)

- Deprecating tf2 C Headers ([#109](https://github.com/ros-visualization/interactive_markers/issues/109))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#110](https://github.com/ros-visualization/interactive_markers/issues/110))
- Use non deprecated API ([#108](https://github.com/ros-visualization/interactive_markers/issues/108))
- Contributors: Alejandro Hernández Cordero, Lucas Wendland

<a id="intra-process-demo"></a>

## [intra\_process\_demo](https://github.com/ros2/demos/tree/kilted/intra_process_demo/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Removed pre-compiler check for opencv3 ([#695](https://github.com/ros2/demos/issues/695))
- [intra\_process\_demo] executable name in README.md fix-up ([#690](https://github.com/ros2/demos/issues/690))
- Contributors: Alejandro Hernández Cordero, Trushant Adeshara, mosfet80

<a id="kdl-parser"></a>

## [kdl\_parser](https://github.com/ros/kdl_parser/tree/kilted/kdl_parser/CHANGELOG.rst)

- update urdf model header ([#85](https://github.com/ros/kdl_parser/issues/85))
- Contributors: Alejandro Hernández Cordero

<a id="laser-geometry"></a>

## [laser\_geometry](https://github.com/ros-perception/laser_geometry/tree/kilted/CHANGELOG.rst)

- Deprecating tf2 C Headers ([#98](https://github.com/ros-perception/laser_geometry/issues/98))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#100](https://github.com/ros-perception/laser_geometry/issues/100))
- Stop using python\_cmake\_module. ([#93](https://github.com/ros-perception/laser_geometry/issues/93))
- Added common linters ([#96](https://github.com/ros-perception/laser_geometry/issues/96))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Lucas Wendland

<a id="launch"></a>

## [launch](https://github.com/ros2/launch/tree/kilted/launch/CHANGELOG.rst)

- Provide copy of launch configs to TimerAction’s entities ([#836](https://github.com/ros2/launch/issues/836))
- Allow concatenating each path component of PathJoinSubstitution ([#838](https://github.com/ros2/launch/issues/838))
- Add StringJoinSubstitution substitution ([#843](https://github.com/ros2/launch/issues/843))
- Add missing test\_depend for launch ([#850](https://github.com/ros2/launch/issues/850))
- Document substitutions concatenation in architecture doc ([#845](https://github.com/ros2/launch/issues/845))
- Update docs to use proper RST literals ([#837](https://github.com/ros2/launch/issues/837))
- Fix function params indentation ([#833](https://github.com/ros2/launch/issues/833))
- Add ForEach action to repeat entities using iteration-specific values ([#802](https://github.com/ros2/launch/issues/802))
- Create py.typed ([#828](https://github.com/ros2/launch/issues/828))
- Improve error reporting by adding file locations to exceptions ([#823](https://github.com/ros2/launch/issues/823))
- add test coverage for substitution edgecases involving E notation ([#824](https://github.com/ros2/launch/issues/824))
- Cleanup the launch dependencies. ([#819](https://github.com/ros2/launch/issues/819))
- Fix ‘set up’ typo ([#813](https://github.com/ros2/launch/issues/813))
- Add test\_xmllint to all of the ament\_python packages. ([#804](https://github.com/ros2/launch/issues/804))
- Fix typo in comment ([#783](https://github.com/ros2/launch/issues/783))
- Contributors: Chris Lalancette, Christian Ruf, Christophe Bedard, Michael Carlstrom, Roland Arsenault, danielcranston

<a id="launch-pytest"></a>

## [launch\_pytest](https://github.com/ros2/launch/tree/kilted/launch_pytest/CHANGELOG.rst)

- Cleanup the launch dependencies. ([#819](https://github.com/ros2/launch/issues/819))
- Add test\_xmllint to all of the ament\_python packages. ([#804](https://github.com/ros2/launch/issues/804))
- Switch to using an rclpy context manager. ([#787](https://github.com/ros2/launch/issues/787))
- Contributors: Chris Lalancette

<a id="launch-ros"></a>

## [launch\_ros](https://github.com/ros2/launch_ros/tree/kilted/launch_ros/CHANGELOG.rst)

- Remove the slash stripping since leading slash matters ([#456](https://github.com/ros2/launch_ros/issues/456))
- Fixing lifecycle node autostart issue [#445](https://github.com/ros2/launch_ros/issues/445) ([#449](https://github.com/ros2/launch_ros/issues/449))
- Change docstring markdown code blocks to RST ([#450](https://github.com/ros2/launch_ros/issues/450))
- Autostarting lifecycle nodes and example launch file demo ([#430](https://github.com/ros2/launch_ros/issues/430))
- Add YAML dumper representator for str type to keep quotes always. ([#436](https://github.com/ros2/launch_ros/issues/436))
- Mock launch components causing rosdoc2 to fail Python API ([#425](https://github.com/ros2/launch_ros/issues/425))
- Add ament\_xmllint to the ament\_python packages. ([#423](https://github.com/ros2/launch_ros/issues/423))
- Fix url in setup.py ([#413](https://github.com/ros2/launch_ros/issues/413))
- Contributors: Chris Lalancette, Christophe Bedard, Olivia/F.F., R Kent James, Steve Macenski, Tomoya Fujita, Wei HU

<a id="launch-testing"></a>

## [launch\_testing](https://github.com/ros2/launch/tree/kilted/launch_testing/CHANGELOG.rst)

- Fix function params indentation ([#833](https://github.com/ros2/launch/issues/833))
- Cleanup the launch dependencies. ([#819](https://github.com/ros2/launch/issues/819))
- Add test\_xmllint to all of the ament\_python packages. ([#804](https://github.com/ros2/launch/issues/804))
- Add mechanism to disable workaround for dependency groups ([#775](https://github.com/ros2/launch/issues/775))
- Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan

<a id="launch-testing-ament-cmake"></a>

## [launch\_testing\_ament\_cmake](https://github.com/ros2/launch/tree/kilted/launch_testing_ament_cmake/CHANGELOG.rst)

- Add CMake parameter to override launch\_testing module ([#854](https://github.com/ros2/launch/issues/854))
- Stop using python\_cmake\_module. ([#760](https://github.com/ros2/launch/issues/760))
- Don’t write Python bytecode when invoking launch tests ([#785](https://github.com/ros2/launch/issues/785))
- Contributors: Chris Lalancette, Scott K Logan

<a id="launch-testing-examples"></a>

## [launch\_testing\_examples](https://github.com/ros2/examples/tree/kilted/launch_testing/launch_testing_examples/CHANGELOG.rst)

- Add test\_xmllint.py. ([#401](https://github.com/ros2/examples/issues/401))
- Contributors: Chris Lalancette

<a id="launch-testing-ros"></a>

## [launch\_testing\_ros](https://github.com/ros2/launch_ros/tree/kilted/launch_testing_ros/CHANGELOG.rst)

- `WaitForTopics`: let the user inject a trigger function to be executed after starting the subscribers ([#356](https://github.com/ros2/launch_ros/issues/356))
- Add EnableRmwIsolation action for starting rmw\_test\_fixture ([#459](https://github.com/ros2/launch_ros/issues/459))
- Fix function params indentation ([#446](https://github.com/ros2/launch_ros/issues/446))
- Add ament\_xmllint to the ament\_python packages. ([#423](https://github.com/ros2/launch_ros/issues/423))
- Switch to use rclpy.init context manager. ([#402](https://github.com/ros2/launch_ros/issues/402))
- Contributors: Chris Lalancette, Christophe Bedard, Giorgio Pintaudi, Scott K Logan

<a id="launch-xml"></a>

## [launch\_xml](https://github.com/ros2/launch/tree/kilted/launch_xml/CHANGELOG.rst)

- Add ForEach action to repeat entities using iteration-specific values ([#802](https://github.com/ros2/launch/issues/802))
- Stop loading extensions during launch\_{xml,yaml} tests. ([#820](https://github.com/ros2/launch/issues/820))
- Cleanup the launch dependencies. ([#819](https://github.com/ros2/launch/issues/819))
- Add test\_xmllint to all of the ament\_python packages. ([#804](https://github.com/ros2/launch/issues/804))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="launch-yaml"></a>

## [launch\_yaml](https://github.com/ros2/launch/tree/kilted/launch_yaml/CHANGELOG.rst)

- Add ForEach action to repeat entities using iteration-specific values ([#802](https://github.com/ros2/launch/issues/802))
- Stop loading extensions during launch\_{xml,yaml} tests. ([#820](https://github.com/ros2/launch/issues/820))
- Cleanup the launch dependencies. ([#819](https://github.com/ros2/launch/issues/819))
- Add test\_xmllint to all of the ament\_python packages. ([#804](https://github.com/ros2/launch/issues/804))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="libcurl-vendor"></a>

## [libcurl\_vendor](https://github.com/ros/resource_retriever/tree/kilted/libcurl_vendor/CHANGELOG.rst)

- uniform MinCMakeVersion ([#108](https://github.com/ros/resource_retriever/issues/108))
- Add “lib” to the Windows curl search path. ([#96](https://github.com/ros/resource_retriever/issues/96)) In CMake 3.3, a commit made it so that the find\_package module in CMake had a compatibility mode where it would automatically search for packages in a <prefix>/lib subdirectory. In CMake 3.6, this compatibility mode was reverted for all platforms *except* Windows. That means that since CMake 3.3, we haven’t actually been using the path as specified in `curl_DIR`, but we have instead been inadvertently relying on that fallback behavior. In CMake 3.28, that compatibilty mode was also removed for Windows, meaning that we are now failing to find\_package(curl) in downstream packages (like resource\_retriever). Fix this by adding in the “lib” directory that always should have been there. I’ll note that this *only* affects our Windows builds, because this code is in a if(WIN32) block.
- Contributors: Chris Lalancette, mosfet80

<a id="liblz4-vendor"></a>

## [liblz4\_vendor](https://github.com/ros2/rosbag2/tree/kilted/liblz4_vendor/CHANGELOG.rst)

- Add in a library prefix for lz4 from conda on Windows. ([#1846](https://github.com/ros2/rosbag2/issues/1846))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="libstatistics-collector"></a>

## [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector/tree/kilted/CHANGELOG.rst)

- Bump codecov/codecov-action from 4.5.0 to 4.6.0
- Fix MovingAverageStatistics::max\_ Default Value ([#201](https://github.com/ros-tooling/libstatistics_collector/issues/201))
- Removed deprecated classes ([#200](https://github.com/ros-tooling/libstatistics_collector/issues/200))
- fix: add void annotation ([#194](https://github.com/ros-tooling/libstatistics_collector/issues/194))
- Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Jeffery Hsu, dependabot[bot]

<a id="libyaml-vendor"></a>

## [libyaml\_vendor](https://github.com/ros2/libyaml_vendor/tree/kilted/CHANGELOG.rst)

- Only set CRT\_SECURE\_NO\_WARNINGS if it hasn’t already been set. ([#64](https://github.com/ros2/libyaml_vendor/issues/64))
- Contributors: Chris Lalancette

<a id="lifecycle"></a>

## [lifecycle](https://github.com/ros2/demos/tree/kilted/lifecycle/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Shane Loretz, mosfet80

<a id="lifecycle-py"></a>

## [lifecycle\_py](https://github.com/ros2/demos/tree/kilted/lifecycle_py/CHANGELOG.rst)

- Add test\_xmllint.py to all of the ament\_python packages. ([#704](https://github.com/ros2/demos/issues/704))
- Change all of the demos to use the new rclpy context manager. ([#694](https://github.com/ros2/demos/issues/694))
- Contributors: Chris Lalancette

<a id="logging-demo"></a>

## [logging\_demo](https://github.com/ros2/demos/tree/kilted/logging_demo/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Shane Loretz, mosfet80

<a id="lttngpy"></a>

## [lttngpy](https://github.com/ros2/ros2_tracing/tree/kilted/lttngpy/CHANGELOG.rst)

- Remove SHARED from pybind11\_add\_module ([#154](https://github.com/ros2/ros2_tracing/issues/154))
- Add python3-dev build\_depend to lttngpy. ([#146](https://github.com/ros2/ros2_tracing/issues/146))
- Don’t try to build on BSD ([#142](https://github.com/ros2/ros2_tracing/issues/142))
- Allow enabling syscalls through `ros2 trace` or the Trace action ([#137](https://github.com/ros2/ros2_tracing/issues/137))
- Remove python\_cmake\_module use. ([#91](https://github.com/ros2/ros2_tracing/issues/91))
- Add missing dependency on pkg-config to lttngpy ([#130](https://github.com/ros2/ros2_tracing/issues/130))
- Contributors: Chris Lalancette, Christophe Bedard, Nathan Wiebe Neufeldt, Scott K Logan, Silvio Traversaro

<a id="mcap-vendor"></a>

## [mcap\_vendor](https://github.com/ros2/rosbag2/tree/kilted/mcap_vendor/CHANGELOG.rst)

- Update mcap ([#1774](https://github.com/ros2/rosbag2/issues/1774)) Update mcap cpp to last version
- Update mcap-releases-cpp- into CMakeLists.txt ([#1612](https://github.com/ros2/rosbag2/issues/1612))
- Contributors: mosfet80

<a id="message-filters"></a>

## [message\_filters](https://github.com/ros2/message_filters/tree/kilted/CHANGELOG.rst)

- Removed windows warnings ([#171](https://github.com/ros2/message_filters/issues/171))
- More generic subscriber implementation using NodeInterfaces from rclcpp ([#113](https://github.com/ros2/message_filters/issues/113))
- Feature/time sequencer python ([#156](https://github.com/ros2/message_filters/issues/156))
- Add sync\_arrival\_time flag to ApproximateTimeSynchronizer ([#166](https://github.com/ros2/message_filters/issues/166))
- fix: add `rclcpp::shutdown` ([#167](https://github.com/ros2/message_filters/issues/167))
- fix typo: Cache.getLastestTime -> Cache.getLatestTime ([#165](https://github.com/ros2/message_filters//issues/165))
- Add temporal offset between topics between ApproximateTimeSynchronizer ([#154](https://github.com/ros2/message_filters/issues/154))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#158](https://github.com/ros2/message_filters/issues/158))
- Updated Python docs ([#150](https://github.com/ros2/message_filters/issues/150))
- Adds an input aligner filter ([#148](https://github.com/ros2/message_filters/issues/148))
- Stop using python\_cmake\_module. ([#114](https://github.com/ros2/message_filters/issues/114))
- Fix the wording in the deprecation messages. ([#144](https://github.com/ros2/message_filters/issues/144))
- Apply some simplifications and deduplications to ExactTime sync policy ([#142](https://github.com/ros2/message_filters/issues/142))
- Minor fixes for [#93](https://github.com/ros2/message_filters/issues/93) ([#143](https://github.com/ros2/message_filters/issues/143))
- Bugfix/segfault when getting surrounding interval of empty cache ([#116](https://github.com/ros2/message_filters/issues/116))
- Migrate to C++11 variadic templates ([#93](https://github.com/ros2/message_filters/issues/93))
- [LatestTimeSync] Fix crash when Synchronizeris started before the messges are available. ([#137](https://github.com/ros2/message_filters/issues/137))
- Fix cppcheck warning on Windwos ([#138](https://github.com/ros2/message_filters/issues/138))
- Adding ament\_lint\_common ([#120](https://github.com/ros2/message_filters/issues/120))
- Deprecating all C headers ([#135](https://github.com/ros2/message_filters/issues/135))
- Cleanups ([#134](https://github.com/ros2/message_filters/issues/134))
- fix link of index.rst in README.md ([#133](https://github.com/ros2/message_filters/issues/133))
- Revert “Adding explicit constructors ([#129](https://github.com/ros2/message_filters/issues/129))” ([#132](https://github.com/ros2/message_filters/issues/132))
- fix: fallback Time used incorrect clock ([#118](https://github.com/ros2/message_filters/issues/118))
- Adding explicit constructors ([#129](https://github.com/ros2/message_filters/issues/129))
- Deprecated qos\_profile in Subscriber ([#127](https://github.com/ros2/message_filters/issues/127))
- Adding cpplint ([#125](https://github.com/ros2/message_filters/issues/125))
- Move Docs From Wiki ([#119](https://github.com/ros2/message_filters/issues/119))
- Adding lint\_cmake ([#126](https://github.com/ros2/message_filters/issues/126))
- Adding Uncrustify Changes ([#124](https://github.com/ros2/message_filters/issues/124))
- Adding Copyright Linter ([#122](https://github.com/ros2/message_filters/issues/122))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christopher Wecht, Clément Chupin, Dominik, Dr. Denis, Iván López Broceño, Kalvik, Lucas Wendland, Matthias Holoch, Michal Staniaszek, Russ, Saif Sidhik, Sascha Arnold, Yuyuan Yuan

<a id="mimick-vendor"></a>

## [mimick\_vendor](https://github.com/ros2/mimick_vendor/tree/kilted/CHANGELOG.rst)

- Update hash to fix windows failures ([#39](https://github.com/ros2/mimick_vendor/issues/39))
- Update to the commit that includes DT\_GNU\_HASH. ([#37](https://github.com/ros2/mimick_vendor/issues/37))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="nav-msgs"></a>

## [nav\_msgs](https://github.com/ros2/common_interfaces/tree/kilted/nav_msgs/CHANGELOG.rst)

- Move geometry\_msgs/PoseStampedArray to nav\_msgs/Goals ([#269](https://github.com/ros2/common_interfaces/issues/269))
- Contributors: Tully Foote

<a id="orocos-kdl-vendor"></a>

## [orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/kilted/orocos_kdl_vendor/CHANGELOG.rst)

- Use the same cmake version ([#36](https://github.com/ros2/orocos_kdl_vendor/issues/36))
- Resolve compatibility issue with newer cmake ([#35](https://github.com/ros2/orocos_kdl_vendor/issues/35))
- fix: add cxx\_standard to avoid c++ check error ([#30](https://github.com/ros2/orocos_kdl_vendor/issues/30))
- Ensure that orocos\_kdl\_vendor doesn’t accidentally find itself. ([#27](https://github.com/ros2/orocos_kdl_vendor/issues/27))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Homalozoa X, Øystein Sture

<a id="osrf-pycommon"></a>

## [osrf\_pycommon](https://github.com/osrf/osrf_pycommon/tree/master/CHANGELOG.rst)

- Merge pull request [#103](https://github.com/osrf/osrf_pycommon/issues/103) from christophebedard/christophebedard/fix-typo-on-each-verb
- Align stdeb dependencies with setup.py ([#101](https://github.com/osrf/osrf_pycommon/issues/101)) Follow-up to 4b2f3a8e4969f33dced1dc2db2296230e7a55b1d
- Add ‘+upstream’ suffix to published deb version ([#102](https://github.com/osrf/osrf_pycommon/issues/102)) Using a debian version suffix which falls late alphabetically appears to give our packages preference by apt. If a user enables a repository which distributes packages created by OSRF or ROS, it is likely that they wish to use these packages instead of the ones packaged by their platform.
- Upload coverage results to codecov ([#100](https://github.com/osrf/osrf_pycommon/issues/100))
- Update ci.yaml ([#96](https://github.com/osrf/osrf_pycommon/issues/96)) fix node.js <20 deprecation Co-authored-by: Scott K Logan <[logans@cottsay.net](mailto:logans%40cottsay.net)>
- Updated python version ([#97](https://github.com/osrf/osrf_pycommon/issues/97)) Python version 3.7 is no longer supported as of June 27, 2023 Co-authored-by: Scott K Logan <[logans@cottsay.net](mailto:logans%40cottsay.net)>
- Resolve outstanding resource warnings when running tests ([#99](https://github.com/osrf/osrf_pycommon/issues/99))
- Update deb platforms for release ([#95](https://github.com/osrf/osrf_pycommon/issues/95)) Added: \* Ubuntu Noble (24.04 LTS pre-release) \* Debian Trixie (testing) Dropped: \* Debian Bullseye (oldstable) Retained: \* Debian Bookworm (stable) \* Ubuntu Focal (20.04 LTS) \* Ubuntu Jammy (22.04 LTS)
- Remove CODEOWNERS. ([#98](https://github.com/osrf/osrf_pycommon/issues/98)) It is out of date and no longer serving its intended purpose.
- Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan, Steven! Ragnarök, mosfet80

<a id="osrf-testing-tools-cpp"></a>

## [osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/kilted/osrf_testing_tools_cpp/CHANGELOG.rst)

- Update CMakeLists.txt ([#85](https://github.com/osrf/osrf_testing_tools_cpp/issues/85))
- Contributors: mosfet80

<a id="pendulum-control"></a>

## [pendulum\_control](https://github.com/ros2/demos/tree/kilted/pendulum_control/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#711](https://github.com/ros2/demos/issues/711))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#707](https://github.com/ros2/demos/issues/707))
- Contributors: Alejandro Hernández Cordero, Shane Loretz, mosfet80

<a id="pendulum-msgs"></a>

## [pendulum\_msgs](https://github.com/ros2/demos/tree/kilted/pendulum_msgs/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Contributors: mosfet80

<a id="performance-test-fixture"></a>

## [performance\_test\_fixture](https://github.com/ros2/performance_test_fixture/tree/kilted/CHANGELOG.rst)

- Fix a warning when building on Ubuntu Noble. ([#26](https://github.com/ros2/performance_test_fixture/issues/26))
- Contributors: Chris Lalancette

<a id="pluginlib"></a>

## [pluginlib](https://github.com/ros/pluginlib/tree/kilted/CHANGELOG.rst)

- Heavily cleanup pluginlib. ([#265](https://github.com/ros/pluginlib/issues/265))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#268](https://github.com/ros/pluginlib/issues/268))
- Fix Minor Spelling Mistakes ([#260](https://github.com/ros/pluginlib/issues/260))
- Removed deprecated method ([#256](https://github.com/ros/pluginlib/issues/256))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, David V. Lu!!

<a id="point-cloud-transport"></a>

## [point\_cloud\_transport](https://github.com/ros-perception/point_cloud_transport/tree/kilted/point_cloud_transport/CHANGELOG.rst)

- Add `rclcpp::shutdown` ([#110](https://github.com/ros-perception/point_cloud_transport/issues/110))
- Updated deprecated message filter headers ([#94](https://github.com/ros-perception/point_cloud_transport/issues/94))
- Removed warning ([#89](https://github.com/ros-perception/point_cloud_transport/issues/89))
- republisher: qos override pub and sub ([#88](https://github.com/ros-perception/point_cloud_transport/issues/88))
- Stop using ament\_target\_dependencies. ([#86](https://github.com/ros-perception/point_cloud_transport/issues/86)) We are slowly moving away from its use, so stop using it here. While we are in here, notice some things that makes this easier: 1. pluginlib is absolutely a public dependency of this package. Because of that, we can just rely on the PUBLIC export of it, and we don’t need to link it into every test. But that also means we don’t need some of the forward-declarations that were in loader\_fwds.hpp, as we can just get those through the header file. 2. republish.hpp doesn’t really need to exist at all. That’s because it is only a header file, but the implementation is in an executable. Thus, no downstream could ever use it. So just remove the file and put the declaration straight into the cpp file.
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Yuyuan Yuan

<a id="point-cloud-transport-py"></a>

## [point\_cloud\_transport\_py](https://github.com/ros-perception/point_cloud_transport/tree/kilted/point_cloud_transport_py/CHANGELOG.rst)

- Add in dependency on python3-dev. ([#103](https://github.com/ros-perception/point_cloud_transport/issues/103))
- Remove use of python\_cmake\_module. ([#63](https://github.com/ros-perception/point_cloud_transport/issues/63))
- remove extra semicolon ([#98](https://github.com/ros-perception/point_cloud_transport/issues/98))
- Contributors: Chris Lalancette, Manu

<a id="python-orocos-kdl-vendor"></a>

## [python\_orocos\_kdl\_vendor](https://github.com/ros2/orocos_kdl_vendor/tree/kilted/python_orocos_kdl_vendor/CHANGELOG.rst)

- fix: use fetchcontent\_makeavailable to fix CMP0169 ([#32](https://github.com/ros2/orocos_kdl_vendor/issues/32))
- Remove the use of python\_cmake\_module ([#26](https://github.com/ros2/orocos_kdl_vendor/issues/26))
- Contributors: Chris Lalancette, Homalozoa X

<a id="python-qt-binding"></a>

## [python\_qt\_binding](https://github.com/ros-visualization/python_qt_binding/tree/kilted/CHANGELOG.rst)

- Skip running the tests on Windows Debug. ([#142](https://github.com/ros-visualization/python_qt_binding/issues/142))
- Contributors: Chris Lalancette

<a id="qt-dotgraph"></a>

## [qt\_dotgraph](https://github.com/ros-visualization/qt_gui_core/tree/kilted/qt_dotgraph/CHANGELOG.rst)

- Convert qt\_dotgraph to a pure Python package. ([#300](https://github.com/ros-visualization/qt_gui_core/issues/300))
- Cleanup qt\_dotgraph and make the tests more robust. ([#296](https://github.com/ros-visualization/qt_gui_core/issues/296))
- Skip running the tests on Windows Debug. ([#292](https://github.com/ros-visualization/qt_gui_core/issues/292))
- Contributors: Chris Lalancette

<a id="qt-gui-cpp"></a>

## [qt\_gui\_cpp](https://github.com/ros-visualization/qt_gui_core/tree/kilted/qt_gui_cpp/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#302](https://github.com/ros-visualization/qt_gui_core/issues/302))
- Add common linters and make them happy to qt\_gui\_cpp ([#295](https://github.com/ros-visualization/qt_gui_core/issues/295))
- Deprecated h headers ([#294](https://github.com/ros-visualization/qt_gui_core/issues/294))
- Contributors: Alejandro Hernández Cordero, Shane Loretz

<a id="quality-of-service-demo-cpp"></a>

## [quality\_of\_service\_demo\_cpp](https://github.com/ros2/demos/tree/kilted/quality_of_service_demo/rclcpp/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714)) demo\_nodes\_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
- Contributors: mosfet80

<a id="quality-of-service-demo-py"></a>

## [quality\_of\_service\_demo\_py](https://github.com/ros2/demos/tree/kilted/quality_of_service_demo/rclpy/CHANGELOG.rst)

- Add test\_xmllint.py to all of the ament\_python packages. ([#704](https://github.com/ros2/demos/issues/704))
- Change all of the demos to use the new rclpy context manager. ([#694](https://github.com/ros2/demos/issues/694))
- Contributors: Chris Lalancette

<a id="rcl"></a>

## [rcl](https://github.com/ros2/rcl/tree/kilted/rcl/CHANGELOG.rst)

- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#1218](https://github.com/ros2/rcl/issues/1218))
- Fix typo in message header include in doc ([#1219](https://github.com/ros2/rcl/issues/1219))
- use rmw\_event\_type\_is\_supported ([#1214](https://github.com/ros2/rcl/issues/1214))
- No need to add public symbol visibility macros in implementation. ([#1213](https://github.com/ros2/rcl/issues/1213))
- Add new interfaces to enable intropsection for action ([#1207](https://github.com/ros2/rcl/issues/1207))
- Use FASTDDS\_DEFAULT\_PROFILES\_FILE instead. ([#1211](https://github.com/ros2/rcl/issues/1211))
- Relieve timer test period not to miss the cycle. ([#1209](https://github.com/ros2/rcl/issues/1209))
- fix(rcl\_action): Allow to pass the timer to action during initialization ([#1201](https://github.com/ros2/rcl/issues/1201)) \* fix(timer): Use impl pointer in jump callback The interface description does not explicitly state that a rcl\_timer\_t may not be copied around. Therefore users may do this. By using a known never changing pointer in the callbacks, we avoid segfaults, even if the ‘user’ decides to copy the rcl\_timer\_t around.
- move qos\_profile\_rosout\_default to rmw. ([#1195](https://github.com/ros2/rcl/issues/1195))
- Update example usage for rcl\_wait\_set\_init to pass correct number of args ([#1204](https://github.com/ros2/rcl/issues/1204))
- Clean up error handling in many rcl{\_action,\_lifecycle} codepaths ([#1202](https://github.com/ros2/rcl/issues/1202)) \* Shorten the delay in test\_action\_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. \* Small style cleanups in test\_action\_server.cpp \* Reset the error in rcl\_node\_type\_cache\_register\_type(). That is, if rcutils\_hash\_map\_set() fails, it sets its own error, so overriding it with our own will cause a warning to print. Make sure to clear it before setting our own. \* Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl\_timer\_init2. \* Record the return value from rcl\_node\_type\_cache\_register\_type. Otherwise, in a failure situation we set the error but we actually return RCL\_RET\_OK to the upper layers, which is odd. \* Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn’t make much sense. Just remove the duplicate code. \* Use the rcl\_timer\_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. \* Don’t overwrite the error from rcl\_action\_goal\_handle\_get\_info() It already sets the error, so rcl\_action\_server\_goal\_exists() should not set it again. \* Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. \* Move the copying of the options earlier in rcl\_subscription\_init. That way when we go to cleanup in the “fail” case, the options actually exist and are valid. This avoids an ugly warning during cleanup. \* Make sure to set the error on failure of rcl\_action\_get\_##\_service\_name This makes it match the generated code for the action\_client. \* Reset the errors during RCUTILS\_FAULT\_INJECTION testing. That way subsequent failures won’t print out ugly error strings. \* Make sure to return errors in \_rcl\_parse\_resource\_match . That is, if rcl\_lexer\_lookahead2\_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. \* Don’t overwrite error by rcl\_validate\_enclave\_name. It leads to ugly warnings. \* Add acomment that rmw\_validate\_namespace\_with\_size sets the error \* Make sure to reset error in rcl\_node\_type\_cache\_init. Otherwise we get a warning about overwriting the error from rcutils\_hash\_map\_init. \* Conditionally set error message in rcl\_publisher\_is\_valid. Only when rcl\_context\_is\_valid doesn’t set the error. \* Don’t overwrite error from rcl\_node\_get\_logger\_name. It already sets the error in the failure case. \* Make sure to reset errors when testing network flow endpoints. That’s because some of the RMW implementations may not support this feature, and thus set errors. \* Make sure to reset errors in rcl\_expand\_topic\_name. That way we can set more useful errors for the upper layers. \* Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. \* Make sure to reset errors in rcl\_lifecycle tests. That way we won’t get ugly “overwritten” warnings on subsequent tests. ———
- Make the event skipping more generic. ([#1197](https://github.com/ros2/rcl/issues/1197))
- Heavy cleanup of test\_events.cpp. ([#1196](https://github.com/ros2/rcl/issues/1196))
- Cleanup test\_graph.cpp. ([#1193](https://github.com/ros2/rcl/issues/1193))
- Expect a minimum of two nodes to be alive in test\_graph ([#1192](https://github.com/ros2/rcl/issues/1192))
- escalate RCL\_RET\_ACTION\_xxx to 40XX. ([#1191](https://github.com/ros2/rcl/issues/1191))
- Fix NULL allocator and racy condition. ([#1188](https://github.com/ros2/rcl/issues/1188))
- Properly initialize the char array used in type hash calculations. ([#1182](https://github.com/ros2/rcl/issues/1182))
- Increased timeouts ([#1181](https://github.com/ros2/rcl/issues/1181))
- Skip some event tests on rmw\_zenoh ([#1180](https://github.com/ros2/rcl/issues/1180))
- doc: rcl\_logging\_spdlog is the default impl. ([#1177](https://github.com/ros2/rcl/issues/1177))
- Update wait.h documentation for rcl\_wait ([#1176](https://github.com/ros2/rcl/issues/1176))
- Change the starting time of the goal expiration timeout ([#1121](https://github.com/ros2/rcl/issues/1121))
- Removed deprecated localhost\_only ([#1169](https://github.com/ros2/rcl/issues/1169))
- Fix typo in rcl\_validate\_enclave\_name\_with\_size() doc ([#1168](https://github.com/ros2/rcl/issues/1168))
- Removed deprecated rcl\_init\_timer() ([#1167](https://github.com/ros2/rcl/issues/1167))
- Cleanup test\_count\_matched test to handle non-DDS RMWs ([#1164](https://github.com/ros2/rcl/issues/1164)) \* Make check\_state a class method in test\_count\_matched. This allows us to pass fewer parameters into each each invocation, and allows us to hide some more of the implementation inside the class. \* Rename “ops” to “opts” in test\_count\_matched. It just better reflects what these structures are. \* Cleanup pub/subs with a scope\_exit in test\_count\_matched. This just ensures that they are always cleaned up, even if we exit early. Note that we specifically do *not* use it for test\_count\_matched\_functions, since the cleanup is intentionally interleaved with other tests. \* Check with the RMW layer to see whether QoS is compatible. Some RMWs may have different compatibility than DDS, so check with the RMW layer to see what we should expect for the number of publishers and subscriptions.
- Add mechanism to disable workaround for dependency groups ([#1151](https://github.com/ros2/rcl/issues/1151))
- remap\_impl: minor typo ([#1158](https://github.com/ros2/rcl/issues/1158))
- Fix up rmw\_cyclonedds timestamp testing. ([#1156](https://github.com/ros2/rcl/issues/1156))
- Add ‘mimick’ label to tests which use Mimick ([#1152](https://github.com/ros2/rcl/issues/1152))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Felix Penzlin, G.A. vd. Hoorn, Janosch Machowinski, Scott K Logan, Tomoya Fujita, Yadu, yadunund

<a id="rcl-action"></a>

## [rcl\_action](https://github.com/ros2/rcl/tree/kilted/rcl_action/CHANGELOG.rst)

- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#1218](https://github.com/ros2/rcl/issues/1218))
- No need to add public symbol visibility macros in implementation. ([#1213](https://github.com/ros2/rcl/issues/1213))
- fix ‘rcl\_action\_server\_configure\_action\_introspection’: inconsistent dll linkage. ([#1212](https://github.com/ros2/rcl/issues/1212))
- Add new interfaces to enable intropsection for action ([#1207](https://github.com/ros2/rcl/issues/1207))
- fix(rcl\_action): Allow to pass the timer to action during initialization ([#1201](https://github.com/ros2/rcl/issues/1201)) \* fix(timer): Use impl pointer in jump callback The interface description does not explicitly state that a rcl\_timer\_t may not be copied around. Therefore users may do this. By using a known never changing pointer in the callbacks, we avoid segfaults, even if the ‘user’ decides to copy the rcl\_timer\_t around.
- Added remapping resolution for action names ([#1170](https://github.com/ros2/rcl/issues/1170)) \* Added remapping resolution for action names \* Fix cpplint/uncrustify \* Simplified returned error codes in case name resolution failes. \* Renamed action\_name field to remapped\_action\_name. \* Removed unnecessary resolved\_action\_name stack variable \* Added tests for action name remapping. \* Add tests for action name remapping using local arguments ———
- Clean up error handling in many rcl{\_action,\_lifecycle} codepaths ([#1202](https://github.com/ros2/rcl/issues/1202)) \* Shorten the delay in test\_action\_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. \* Small style cleanups in test\_action\_server.cpp \* Reset the error in rcl\_node\_type\_cache\_register\_type(). That is, if rcutils\_hash\_map\_set() fails, it sets its own error, so overriding it with our own will cause a warning to print. Make sure to clear it before setting our own. \* Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl\_timer\_init2. \* Record the return value from rcl\_node\_type\_cache\_register\_type. Otherwise, in a failure situation we set the error but we actually return RCL\_RET\_OK to the upper layers, which is odd. \* Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn’t make much sense. Just remove the duplicate code. \* Use the rcl\_timer\_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. \* Don’t overwrite the error from rcl\_action\_goal\_handle\_get\_info() It already sets the error, so rcl\_action\_server\_goal\_exists() should not set it again. \* Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. \* Move the copying of the options earlier in rcl\_subscription\_init. That way when we go to cleanup in the “fail” case, the options actually exist and are valid. This avoids an ugly warning during cleanup. \* Make sure to set the error on failure of rcl\_action\_get\_##\_service\_name This makes it match the generated code for the action\_client. \* Reset the errors during RCUTILS\_FAULT\_INJECTION testing. That way subsequent failures won’t print out ugly error strings. \* Make sure to return errors in \_rcl\_parse\_resource\_match . That is, if rcl\_lexer\_lookahead2\_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. \* Don’t overwrite error by rcl\_validate\_enclave\_name. It leads to ugly warnings. \* Add acomment that rmw\_validate\_namespace\_with\_size sets the error \* Make sure to reset error in rcl\_node\_type\_cache\_init. Otherwise we get a warning about overwriting the error from rcutils\_hash\_map\_init. \* Conditionally set error message in rcl\_publisher\_is\_valid. Only when rcl\_context\_is\_valid doesn’t set the error. \* Don’t overwrite error from rcl\_node\_get\_logger\_name. It already sets the error in the failure case. \* Make sure to reset errors when testing network flow endpoints. That’s because some of the RMW implementations may not support this feature, and thus set errors. \* Make sure to reset errors in rcl\_expand\_topic\_name. That way we can set more useful errors for the upper layers. \* Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. \* Make sure to reset errors in rcl\_lifecycle tests. That way we won’t get ugly “overwritten” warnings on subsequent tests. ———
- Cleanup test\_graph.cpp. ([#1193](https://github.com/ros2/rcl/issues/1193))
- Expect a minimum of two nodes to be alive in test\_graph ([#1192](https://github.com/ros2/rcl/issues/1192))
- escalate RCL\_RET\_ACTION\_xxx to 40XX. ([#1191](https://github.com/ros2/rcl/issues/1191))
- Fix NULL allocator and racy condition. ([#1188](https://github.com/ros2/rcl/issues/1188))
- Increased timeouts ([#1181](https://github.com/ros2/rcl/issues/1181))
- Change the starting time of the goal expiration timeout ([#1121](https://github.com/ros2/rcl/issues/1121))
- Increase the test\_action\_interaction timeouts. ([#1172](https://github.com/ros2/rcl/issues/1172)) While I can’t reproduce the problem locally, I suspect that waiting only 1 second for the entities to become ready isn’t enough in all cases, particularly on Windows, with Connext, and when we are running in parallel with other tests. Thus, increase the timeout for the rcl\_wait() in all of the test\_action\_interaction tests, which should hopefully be enough to make this always pass.
- Stop compiling rcl\_action tests multiple times. ([#1165](https://github.com/ros2/rcl/issues/1165)) We don’t need to compile the tests once for each RMW; we can just compile it once and then use the RMW\_IMPLEMENTATION environment variable to run the tests on the different RMWs. This speeds up compilation.
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Janosch Machowinski, Justus Braun, Tomoya Fujita, Yadu, yadunund

<a id="rcl-lifecycle"></a>

## [rcl\_lifecycle](https://github.com/ros2/rcl/tree/kilted/rcl_lifecycle/CHANGELOG.rst)

- add rcl\_print\_transition\_map. ([#1217](https://github.com/ros2/rcl/issues/1217))
- Enable test isolation in rcl\_lifecycle ([#1216](https://github.com/ros2/rcl/issues/1216))
- Clean up error handling in many rcl{\_action,\_lifecycle} codepaths ([#1202](https://github.com/ros2/rcl/issues/1202)) \* Shorten the delay in test\_action\_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. \* Small style cleanups in test\_action\_server.cpp \* Reset the error in rcl\_node\_type\_cache\_register\_type(). That is, if rcutils\_hash\_map\_set() fails, it sets its own error, so overriding it with our own will cause a warning to print. Make sure to clear it before setting our own. \* Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl\_timer\_init2. \* Record the return value from rcl\_node\_type\_cache\_register\_type. Otherwise, in a failure situation we set the error but we actually return RCL\_RET\_OK to the upper layers, which is odd. \* Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn’t make much sense. Just remove the duplicate code. \* Use the rcl\_timer\_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. \* Don’t overwrite the error from rcl\_action\_goal\_handle\_get\_info() It already sets the error, so rcl\_action\_server\_goal\_exists() should not set it again. \* Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. \* Move the copying of the options earlier in rcl\_subscription\_init. That way when we go to cleanup in the “fail” case, the options actually exist and are valid. This avoids an ugly warning during cleanup. \* Make sure to set the error on failure of rcl\_action\_get\_##\_service\_name This makes it match the generated code for the action\_client. \* Reset the errors during RCUTILS\_FAULT\_INJECTION testing. That way subsequent failures won’t print out ugly error strings. \* Make sure to return errors in \_rcl\_parse\_resource\_match . That is, if rcl\_lexer\_lookahead2\_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. \* Don’t overwrite error by rcl\_validate\_enclave\_name. It leads to ugly warnings. \* Add acomment that rmw\_validate\_namespace\_with\_size sets the error \* Make sure to reset error in rcl\_node\_type\_cache\_init. Otherwise we get a warning about overwriting the error from rcutils\_hash\_map\_init. \* Conditionally set error message in rcl\_publisher\_is\_valid. Only when rcl\_context\_is\_valid doesn’t set the error. \* Don’t overwrite error from rcl\_node\_get\_logger\_name. It already sets the error in the failure case. \* Make sure to reset errors when testing network flow endpoints. That’s because some of the RMW implementations may not support this feature, and thus set errors. \* Make sure to reset errors in rcl\_expand\_topic\_name. That way we can set more useful errors for the upper layers. \* Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. \* Make sure to reset errors in rcl\_lifecycle tests. That way we won’t get ugly “overwritten” warnings on subsequent tests. ———
- Fix NULL allocator and racy condition. ([#1188](https://github.com/ros2/rcl/issues/1188))
- Fix typo in rcl\_lifecycle\_com\_interface\_t doc ([#1174](https://github.com/ros2/rcl/issues/1174))
- Fix a memory leak in test\_rcl\_lifecycle. ([#1173](https://github.com/ros2/rcl/issues/1173)) This one came about probably as a result of a bad merge. But essentially we were forcing the srv\_change\_state com\_interface to be nullptr, but forgetting to save off the old pointer early enough. Thus, we could never restore the old one before we went to “fini”, and the memory would be leaked. Fix this by remembering the impl pointer earlier.
- Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan, Tomoya Fujita

<a id="rcl-logging-noop"></a>

## [rcl\_logging\_noop](https://github.com/ros2/rcl_logging/tree/kilted/rcl_logging_noop/CHANGELOG.rst)

- rcl\_logging\_interface is only valid path with build environment. ([#122](https://github.com/ros2/rcl_logging/issues/122))
- README update and some cleanups. ([#120](https://github.com/ros2/rcl_logging/issues/120))
- Contributors: Tomoya Fujita

<a id="rcl-logging-spdlog"></a>

## [rcl\_logging\_spdlog](https://github.com/ros2/rcl_logging/tree/kilted/rcl_logging_spdlog/CHANGELOG.rst)

- rcl\_logging\_interface is only valid path with build environment. ([#122](https://github.com/ros2/rcl_logging/issues/122))
- README update and some cleanups. ([#120](https://github.com/ros2/rcl_logging/issues/120))
- Updated deprecated API ([#117](https://github.com/ros2/rcl_logging/issues/117))
- Contributors: Alejandro Hernández Cordero, Tomoya Fujita

<a id="rcl-yaml-param-parser"></a>

## [rcl\_yaml\_param\_parser](https://github.com/ros2/rcl/tree/kilted/rcl_yaml_param_parser/CHANGELOG.rst)

- Cleanup errors after error paths in rcl\_yaml\_param\_parser tests. ([#1203](https://github.com/ros2/rcl/issues/1203)) This gets rid of ugly “overwritten” warnings in the tests.
- Add ‘mimick’ label to tests which use Mimick ([#1152](https://github.com/ros2/rcl/issues/1152))
- Contributors: Chris Lalancette, Scott K Logan

<a id="rclcpp"></a>

## [rclcpp](https://github.com/ros2/rclcpp/tree/kilted/rclcpp/CHANGELOG.rst)

- Fix a race condition ([#2819](https://github.com/ros2/rclcpp/issues/2819))
- Remove redundant typesupport check in serialization module ([#2808](https://github.com/ros2/rclcpp/issues/2808))
- Remove get\_typesupport\_handle implementation. ([#2806](https://github.com/ros2/rclcpp/issues/2806))
- Use NodeParameterInterface instead of /parameter\_event to update “use\_sim\_time” ([#2378](https://github.com/ros2/rclcpp/issues/2378))
- Remove cancel\_clock\_executor\_promise\_. ([#2797](https://github.com/ros2/rclcpp/issues/2797))
- Enable parameter update recursively only when QoS override parameters. ([#2742](https://github.com/ros2/rclcpp/issues/2742))
- Removed trailing whitespace from the codebase. ([#2791](https://github.com/ros2/rclcpp/issues/2791))
- Expanded docstring of `get_rmw_qos_profile()` ([#2787](https://github.com/ros2/rclcpp/issues/2787))
- Set envars to run tests with rmw\_zenoh\_cpp with multicast discovery ([#2776](https://github.com/ros2/rclcpp/issues/2776))
- fix: Compilefix for clang ([#2775](https://github.com/ros2/rclcpp/issues/2775))
- add exception doc for configure\_introspection. ([#2773](https://github.com/ros2/rclcpp/issues/2773))
- feat: Add ClockWaiter and ClockConditionalVariable ([#2691](https://github.com/ros2/rclcpp/issues/2691))
- doc: Added warning to not instantiate Clock directly with RCL\_ROS\_TIME ([#2768](https://github.com/ros2/rclcpp/issues/2768))
- Use rmw\_event\_type\_is\_supported in test\_qos\_event ([#2761](https://github.com/ros2/rclcpp/issues/2761))
- Support action typesupport helper ([#2750](https://github.com/ros2/rclcpp/issues/2750))
- use maybe\_unused attribute for the portability. ([#2758](https://github.com/ros2/rclcpp/issues/2758))
- Executor strong reference fix ([#2745](https://github.com/ros2/rclcpp/issues/2745))
- Cleanup of <https://github.com/ros2/rclcpp/pull/2683> ([#2714](https://github.com/ros2/rclcpp/issues/2714))
- Fix typo in doc section for get\_service\_typesupport\_handle ([#2751](https://github.com/ros2/rclcpp/issues/2751))
- Test case and fix for for <https://github.com/ros2/rclcpp/issues/2652> ([#2713](https://github.com/ros2/rclcpp/issues/2713))
- fix(timer): Delete node, after executor thread terminated ([#2737](https://github.com/ros2/rclcpp/issues/2737))
- update doc section for spin\_xxx methods. ([#2730](https://github.com/ros2/rclcpp/issues/2730))
- fix: Expose timers used by rclcpp::Waitables ([#2699](https://github.com/ros2/rclcpp/issues/2699))
- use rmw\_qos\_profile\_rosout\_default instead of rcl. ([#2663](https://github.com/ros2/rclcpp/issues/2663))
- fix(Executor): Fixed entities not beeing executed after just beeing added ([#2724](https://github.com/ros2/rclcpp/issues/2724))
- fix: make the loop condition align with the description ([#2726](https://github.com/ros2/rclcpp/issues/2726))
- Collect log messages from rcl, and reset. ([#2720](https://github.com/ros2/rclcpp/issues/2720))
- Fix transient local IPC publish ([#2708](https://github.com/ros2/rclcpp/issues/2708))
- apply actual QoS from rmw to the IPC publisher. ([#2707](https://github.com/ros2/rclcpp/issues/2707))
- Adding in topic name to logging on IPC issues ([#2706](https://github.com/ros2/rclcpp/issues/2706))
- fix TestTimeSource.ROS\_time\_valid\_attach\_detach. ([#2700](https://github.com/ros2/rclcpp/issues/2700))
- Update docstring for `rclcpp::Node::now()` ([#2696](https://github.com/ros2/rclcpp/issues/2696))
- Re-enable executor test on rmw\_connextdds. ([#2693](https://github.com/ros2/rclcpp/issues/2693))
- Fix warnings on Windows. ([#2692](https://github.com/ros2/rclcpp/issues/2692))
- Omnibus fixes for running tests with Connext. ([#2684](https://github.com/ros2/rclcpp/issues/2684))
- fix(Executor): Fix segfault if callback group is deleted during rmw\_wait ([#2683](https://github.com/ros2/rclcpp/issues/2683))
- accept custom allocator for LoanedMessage. ([#2672](https://github.com/ros2/rclcpp/issues/2672))
- a couple of typo fixes in doc section for LoanedMessage. ([#2676](https://github.com/ros2/rclcpp/issues/2676))
- Make sure callback\_end tracepoint is triggered in AnyServiceCallback ([#2670](https://github.com/ros2/rclcpp/issues/2670))
- Correct the incorrect comments in generic\_client.hpp ([#2662](https://github.com/ros2/rclcpp/issues/2662))
- Fix NodeOptions assignment operator ([#2656](https://github.com/ros2/rclcpp/issues/2656))
- set QoS History KEEP\_ALL explicitly for statistics publisher. ([#2650](https://github.com/ros2/rclcpp/issues/2650))
- Fix test\_intra\_process\_manager.cpp with rmw\_zenoh\_cpp ([#2653](https://github.com/ros2/rclcpp/issues/2653))
- Fixed test\_events\_executors in zenoh ([#2643](https://github.com/ros2/rclcpp/issues/2643))
- rmw\_fastrtps supports service event gid uniqueness test. ([#2638](https://github.com/ros2/rclcpp/issues/2638))
- print warning if event callback is not supported instead of passing exception. ([#2648](https://github.com/ros2/rclcpp/issues/2648))
- Implement callback support of async\_send\_request for service generic client ([#2614](https://github.com/ros2/rclcpp/issues/2614))
- Fixed test qos rmw zenoh ([#2639](https://github.com/ros2/rclcpp/issues/2639))
- verify client gid uniqueness for a single service event. ([#2636](https://github.com/ros2/rclcpp/issues/2636))
- Skip some tests in test\_qos\_event and run others with event types supported by rmw\_zenoh ([#2626](https://github.com/ros2/rclcpp/issues/2626))
- Shutdown the context before context’s destructor is invoked in tests ([#2633](https://github.com/ros2/rclcpp/issues/2633))
- Skip rmw zenoh content filtering tests ([#2627](https://github.com/ros2/rclcpp/issues/2627))
- Use InvalidServiceTypeError for unavailable service type in GenericClient ([#2629](https://github.com/ros2/rclcpp/issues/2629))
- Implement generic service ([#2617](https://github.com/ros2/rclcpp/issues/2617))
- fix events-executor warm-up bug and add unit-tests ([#2591](https://github.com/ros2/rclcpp/issues/2591))
- remove unnecessary gtest-skip in test\_executors ([#2600](https://github.com/ros2/rclcpp/issues/2600))
- Correct node name in service test code ([#2615](https://github.com/ros2/rclcpp/issues/2615))
- Minor naming fixes for ParameterValue to\_string() function ([#2609](https://github.com/ros2/rclcpp/issues/2609))
- Removed clang warnings ([#2605](https://github.com/ros2/rclcpp/issues/2605))
- Fix a couple of issues in the documentation. ([#2608](https://github.com/ros2/rclcpp/issues/2608))
- deprecate the static single threaded executor ([#2598](https://github.com/ros2/rclcpp/issues/2598))
- Fix name of ParameterEventHandler class in doc ([#2604](https://github.com/ros2/rclcpp/issues/2604))
- subscriber\_statistics\_collectors\_ should be protected by mutex. ([#2592](https://github.com/ros2/rclcpp/issues/2592))
- Fix bug in timers lifecycle for events executor ([#2586](https://github.com/ros2/rclcpp/issues/2586))
- fix rclcpp/test/rclcpp/CMakeLists.txt to check for the correct targets existance ([#2596](https://github.com/ros2/rclcpp/issues/2596))
- Shut down context during init if logging config fails ([#2594](https://github.com/ros2/rclcpp/issues/2594))
- Make more of the Waitable API abstract ([#2593](https://github.com/ros2/rclcpp/issues/2593))
- Only compile the tests once. ([#2590](https://github.com/ros2/rclcpp/issues/2590))
- Updated rcpputils path API ([#2579](https://github.com/ros2/rclcpp/issues/2579))
- Make the subscriber\_triggered\_to\_receive\_message test more reliable. ([#2584](https://github.com/ros2/rclcpp/issues/2584)) \* Make the subscriber\_triggered\_to\_receive\_message test more reliable. In the current code, inside of the timer we create the subscription and the publisher, publish immediately, and expect the subscription to get it immediately. But it may be the case that discovery hasn’t even happened between the publisher and the subscription by the time the publish call happens. To make this more reliable, create the subscription and publish *before* we ever create and spin on the timer. This at least gives 100 milliseconds for discovery to happen. That may not be quite enough to make this reliable on all platforms, but in my local testing this helps a lot. Prior to this change I can make this fail one out of 10 times, and after the change I’ve run 100 times with no failures.
- Have the EventsExecutor use more common code ([#2570](https://github.com/ros2/rclcpp/issues/2570)) \* move notify waitable setup to its own function \* move mutex lock to retrieve\_entity utility \* use entities\_need\_rebuild\_ atomic bool in events-executors \* remove duplicated set\_on\_ready\_callback for notify\_waitable \* use mutex from base class rather than a new recursive mutex \* use current\_collection\_ member in events-executor \* delay adding notify waitable to collection \* postpone clearing the current collection \* commonize notify waitable and collection \* commonize add/remove node/cbg methods \* fix linter errors ———
- Removed deprecated methods and classes ([#2575](https://github.com/ros2/rclcpp/issues/2575))
- Release ownership of entities after spinning cancelled ([#2556](https://github.com/ros2/rclcpp/issues/2556)) \* Release ownership of entities after spinning cancelled \* Move release action to every exit point in different spin functions \* Move wait\_result\_.reset() before setting spinning to false \* Update test code \* Move test code to test\_executors.cpp ———
- Split test\_executors.cpp even further. ([#2572](https://github.com/ros2/rclcpp/issues/2572)) That’s because it is too large for Windows Debug to compile, so split into smaller bits. Even with this split, the file is too big; that’s likely because we are using TYPED\_TEST here, which generates multiple symbols per test case. To deal with this, without further breaking up the file, also add in the /bigobj flag when compiling on Windows Debug.
- avoid adding notify waitable twice to events-executor collection ([#2564](https://github.com/ros2/rclcpp/issues/2564)) \* avoid adding notify waitable twice to events-executor entities collection \* remove redundant mutex lock ———
- Remove unnecessary msg includes in tests ([#2566](https://github.com/ros2/rclcpp/issues/2566))
- Fix copy-paste errors in function docs ([#2565](https://github.com/ros2/rclcpp/issues/2565))
- Fix typo in function doc ([#2563](https://github.com/ros2/rclcpp/issues/2563))
- Add test creating two content filter topics with the same topic name ([#2546](https://github.com/ros2/rclcpp/issues/2546)) ([#2549](https://github.com/ros2/rclcpp/issues/2549))
- add impl pointer for ExecutorOptions ([#2523](https://github.com/ros2/rclcpp/issues/2523))
- Fixup Executor::spin\_all() regression fix ([#2517](https://github.com/ros2/rclcpp/issues/2517))
- Add ‘mimick’ label to tests which use Mimick ([#2516](https://github.com/ros2/rclcpp/issues/2516))
- Contributors: Abhishek Kashyap, Alberto Soragna, Alejandro Hernández Cordero, Alexis Pojomovsky, Barry Xu, Chris Lalancette, Christophe Bedard, Hsin-Yi, Janosch Machowinski, Jeffery Hsu, Kang, Leander Stephen D’Souza, Patrick Roncagliolo, Pedro de Azeredo, Romain DESILLE, Scott K Logan, Steve Macenski, Tanishq Chaudhary, Tomoya Fujita, William Woodall, Yuyuan Yuan, jmachowinski

<a id="rclcpp-action"></a>

## [rclcpp\_action](https://github.com/ros2/rclcpp/tree/kilted/rclcpp_action/CHANGELOG.rst)

- Use std::recursive\_mutex for action requests. ([#2798](https://github.com/ros2/rclcpp/issues/2798))
- Remove warning ([#2790](https://github.com/ros2/rclcpp/issues/2790))
- Harden rclcpp\_action::convert(). ([#2786](https://github.com/ros2/rclcpp/issues/2786))
- Add new interfaces to enable introspection for action ([#2743](https://github.com/ros2/rclcpp/issues/2743))
- use maybe\_unused attribute for the portability. ([#2758](https://github.com/ros2/rclcpp/issues/2758))
- fix: Expose timers used by rclcpp::Waitables ([#2699](https://github.com/ros2/rclcpp/issues/2699))
- Collect log messages from rcl, and reset. ([#2720](https://github.com/ros2/rclcpp/issues/2720))
- Make ament\_cmake a buildtool dependency ([#2689](https://github.com/ros2/rclcpp/issues/2689))
- Fix documentation typo in server\_goal\_handle.hpp ([#2669](https://github.com/ros2/rclcpp/issues/2669))
- Increase the timeout for the cppcheck on rclcpp\_action. ([#2640](https://github.com/ros2/rclcpp/issues/2640))
- add smart pointer macros definitions to action server and client base classes ([#2631](https://github.com/ros2/rclcpp/issues/2631))
- Fix typo in function doc ([#2563](https://github.com/ros2/rclcpp/issues/2563))
- Add ‘mimick’ label to tests which use Mimick ([#2516](https://github.com/ros2/rclcpp/issues/2516))
- Contributors: Alberto Soragna, Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Janosch Machowinski, Nathan Wiebe Neufeldt, Scott K Logan, Tomoya Fujita, YR

<a id="rclcpp-components"></a>

## [rclcpp\_components](https://github.com/ros2/rclcpp/tree/kilted/rclcpp_components/CHANGELOG.rst)

- Removed trailing whitespace from the codebase. ([#2791](https://github.com/ros2/rclcpp/issues/2791))
- add NO\_UNDEFINED\_SYMBOLS to rclcpp\_components\_register\_node cmake macro ([#2746](https://github.com/ros2/rclcpp/issues/2746)) ([#2764](https://github.com/ros2/rclcpp/issues/2764))
- use maybe\_unused attribute for the portability. ([#2758](https://github.com/ros2/rclcpp/issues/2758))
- ComponentManager should just ignore unknown extra argument in the bas… ([#2723](https://github.com/ros2/rclcpp/issues/2723))
- Add parsing for rest of obvious boolean extra arguments and throw for unsupported ones ([#2685](https://github.com/ros2/rclcpp/issues/2685))
- Shutdown the context before context’s destructor is invoked in tests ([#2633](https://github.com/ros2/rclcpp/issues/2633))
- Fix typo in rclcpp\_components benchmark\_components ([#2602](https://github.com/ros2/rclcpp/issues/2602))
- Updated rcpputils path API ([#2579](https://github.com/ros2/rclcpp/issues/2579))
- remove deprecated APIs from component\_manager.hpp ([#2585](https://github.com/ros2/rclcpp/issues/2585))
- Contributors: Alberto Soragna, Alejandro Hernández Cordero, Christophe Bedard, Jonas Otto, Leander Stephen D’Souza, Tomoya Fujita, rcp1

<a id="rclcpp-lifecycle"></a>

## [rclcpp\_lifecycle](https://github.com/ros2/rclcpp/tree/kilted/rclcpp_lifecycle/CHANGELOG.rst)

- should pull valid transition before trying to change the state. ([#2774](https://github.com/ros2/rclcpp/issues/2774))
- use maybe\_unused attribute for the portability. ([#2758](https://github.com/ros2/rclcpp/issues/2758))
- Collect log messages from rcl, and reset. ([#2720](https://github.com/ros2/rclcpp/issues/2720))
- Update docstring for `rclcpp::Node::now()` ([#2696](https://github.com/ros2/rclcpp/issues/2696))
- Fix error message in rclcpp\_lifecycle::State::reset() ([#2647](https://github.com/ros2/rclcpp/issues/2647))
- Shutdown the context before context’s destructor is invoked in tests ([#2633](https://github.com/ros2/rclcpp/issues/2633))
- LifecycleNode bugfix and add test cases ([#2562](https://github.com/ros2/rclcpp/issues/2562))
- Properly test get\_service\_names\_and\_types\_by\_node in rclcpp\_lifecycle ([#2599](https://github.com/ros2/rclcpp/issues/2599))
- Removed deprecated methods and classes ([#2575](https://github.com/ros2/rclcpp/issues/2575))
- Fix the lifecycle tests on RHEL-9. ([#2583](https://github.com/ros2/rclcpp/issues/2583)) \* Fix the lifecycle tests on RHEL-9. The full explanation is in the comment, but basically since RHEL doesn’t support mocking\_utils::inject\_on\_return, we have to split out certain tests to make sure resources within a process don’t collide. Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- revert call shutdown in LifecycleNode destructor ([#2557](https://github.com/ros2/rclcpp/issues/2557))
- LifecycleNode shutdown on dtor only with valid context. ([#2545](https://github.com/ros2/rclcpp/issues/2545))
- call shutdown in LifecycleNode dtor to avoid leaving the device in unknown state (2nd) ([#2528](https://github.com/ros2/rclcpp/issues/2528))
- rclcpp::shutdown should not be called before LifecycleNode dtor. ([#2527](https://github.com/ros2/rclcpp/issues/2527))
- Revert “call shutdown in LifecycleNode dtor to avoid leaving the device in un… ([#2450](https://github.com/ros2/rclcpp/issues/2450))” ([#2522](https://github.com/ros2/rclcpp/issues/2522))
- Add ‘mimick’ label to tests which use Mimick ([#2516](https://github.com/ros2/rclcpp/issues/2516))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Patrick Roncagliolo, Scott K Logan, Tomoya Fujita

<a id="rclpy"></a>

## [rclpy](https://github.com/ros2/rclpy/tree/kilted/rclpy/CHANGELOG.rst)

- Update parameter types ([#1441](https://github.com/ros2/rclpy/issues/1441))
- Add TypeError string arg for better clarity ([#1442](https://github.com/ros2/rclpy/issues/1442))
- Fix loading parameter behavior from yaml file. ([#1193](https://github.com/ros2/rclpy/issues/1193))
- Update `lifecycle` types ([#1440](https://github.com/ros2/rclpy/issues/1440))
- Update \_rclpy\_pybind11.pyi order and add EventsExecutor ([#1436](https://github.com/ros2/rclpy/issues/1436))
- Update Clock Types ([#1433](https://github.com/ros2/rclpy/issues/1433))
- Introduce EventsExecutor implementation ([#1391](https://github.com/ros2/rclpy/issues/1391))
- Fix Duration, Clock, and QoS Docs ([#1428](https://github.com/ros2/rclpy/issues/1428))
- Add exception doc for configure\_introspection. ([#1434](https://github.com/ros2/rclpy/issues/1434))
- Fix Task constructor type bug ([#1431](https://github.com/ros2/rclpy/issues/1431))
- Add new interfaces to enable intropsection for action ([#1413](https://github.com/ros2/rclpy/issues/1413))
- Check parameter callback signature during registration. ([#1425](https://github.com/ros2/rclpy/issues/1425))
- Fix function params indentation ([#1426](https://github.com/ros2/rclpy/issues/1426))
- Update Service and Action Protocols ([#1409](https://github.com/ros2/rclpy/issues/1409))
- Remove `SHARED` from `pybind11_add_module` ([#1305](https://github.com/ros2/rclpy/issues/1305))
- Publish action goal status once accepted before execution. ([#1228](https://github.com/ros2/rclpy/issues/1228))
- Add missing dependencies so that rosdoc2 shows Node ([#1408](https://github.com/ros2/rclpy/issues/1408))
- add QoS Profile/Depth support to Node. ([#1376](https://github.com/ros2/rclpy/issues/1376))
- Various typing fixes ([#1402](https://github.com/ros2/rclpy/issues/1402))
- Add types to Action with rhel roscli fix ([#1361](https://github.com/ros2/rclpy/issues/1361))
- Check if Task(Future) is canceled. ([#1377](https://github.com/ros2/rclpy/issues/1377))
- Executors types ([#1370](https://github.com/ros2/rclpy/issues/1370))
- event\_handler.py types ([#1340](https://github.com/ros2/rclpy/issues/1340))
- Add support for operator overloading of `Duration` ([#1387](https://github.com/ros2/rclpy/issues/1387))
- Service/Client Implementation types ([#1384](https://github.com/ros2/rclpy/issues/1384))
- avoid lifecycle node transition exception ([#1319](https://github.com/ros2/rclpy/issues/1319))
- Client:call generates TimeoutError exception when it is timed out. ([#1271](https://github.com/ros2/rclpy/issues/1271))
- Add in python3-dev build dependency. ([#1380](https://github.com/ros2/rclpy/issues/1380))
- Fix the race condition while calling rcl\_shutdown ([#1353](https://github.com/ros2/rclpy/issues/1353))
- Use @deprecated to mark deprecated APIs for type checkers. ([#1350](https://github.com/ros2/rclpy/issues/1350))
- init ([#1358](https://github.com/ros2/rclpy/issues/1358))
- Avoid redundant done callbacks of the future while repeatedly calling spin\_until\_future\_complete ([#1374](https://github.com/ros2/rclpy/issues/1374))
- Clean qos zenoh tests ([#1369](https://github.com/ros2/rclpy/issues/1369))
- adjust warn message that requested goal is already expired. ([#1363](https://github.com/ros2/rclpy/issues/1363))
- Adds types to Lifecycle Objects ([#1338](https://github.com/ros2/rclpy/issues/1338))
- Remove python\_cmake\_module use ([#1220](https://github.com/ros2/rclpy/issues/1220))
- TestClient.test\_service\_timestamps failing consistently. ([#1364](https://github.com/ros2/rclpy/issues/1364))
- Revert “Add types to Action Server and Action Client ([#1349](https://github.com/ros2/rclpy/issues/1349))” ([#1359](https://github.com/ros2/rclpy/issues/1359))
- Revert “Executors types ([#1345](https://github.com/ros2/rclpy/issues/1345))” ([#1360](https://github.com/ros2/rclpy/issues/1360))
- remove mock\_compat ([#1357](https://github.com/ros2/rclpy/issues/1357))
- Executors types ([#1345](https://github.com/ros2/rclpy/issues/1345))
- Add types to Action Server and Action Client ([#1349](https://github.com/ros2/rclpy/issues/1349))
- Remove TODO for OpenSplice DDS issue. ([#1354](https://github.com/ros2/rclpy/issues/1354))
- Add types to parameter\_client.py ([#1348](https://github.com/ros2/rclpy/issues/1348))
- Add types to Node.py ([#1346](https://github.com/ros2/rclpy/issues/1346))
- Add types to signals.py ([#1344](https://github.com/ros2/rclpy/issues/1344))
- Fixes spin\_until\_future\_complete inside callback ([#1316](https://github.com/ros2/rclpy/issues/1316))
- add types ([#1339](https://github.com/ros2/rclpy/issues/1339))
- Add types to wait\_for\_message.py and moves Handles into type stubs ([#1325](https://github.com/ros2/rclpy/issues/1325))
- Add types to waitable.py ([#1328](https://github.com/ros2/rclpy/issues/1328))
- Replace rclpyHandle with type stubs ([#1326](https://github.com/ros2/rclpy/issues/1326))
- Fix time subtraction ([#1312](https://github.com/ros2/rclpy/issues/1312))
- Adds types to TypeDescriptionService. ([#1329](https://github.com/ros2/rclpy/issues/1329))
- Import DurationHandle not DurationType ([#1332](https://github.com/ros2/rclpy/issues/1332))
- Creates PublisherHandle and updates publisher.py ([#1310](https://github.com/ros2/rclpy/issues/1310))
- Subscription types ([#1281](https://github.com/ros2/rclpy/issues/1281))
- Add types to qos.py ([#1255](https://github.com/ros2/rclpy/issues/1255))
- minor improvements ([#1330](https://github.com/ros2/rclpy/issues/1330))
- Initialize signal handlers after context ([#1331](https://github.com/ros2/rclpy/issues/1331))
- shutdown ThreadPoolExecutor in MultiThreadedExecutor. ([#1309](https://github.com/ros2/rclpy/issues/1309))
- Generics Services and Clients ([#1275](https://github.com/ros2/rclpy/issues/1275))
- Add types to ParameterService ([#1262](https://github.com/ros2/rclpy/issues/1262))
- Add types to timer.py ([#1260](https://github.com/ros2/rclpy/issues/1260))
- Add types to rcutils\_logger.py ([#1249](https://github.com/ros2/rclpy/issues/1249))
- Add types to topic\_endpoint\_info.oy ([#1253](https://github.com/ros2/rclpy/issues/1253))
- Add types to parameter.py. ([#1246](https://github.com/ros2/rclpy/issues/1246))
- Guard condition types. ([#1252](https://github.com/ros2/rclpy/issues/1252))
- Add types to callback\_groups.py ([#1251](https://github.com/ros2/rclpy/issues/1251))
- Utilities.py types. ([#1250](https://github.com/ros2/rclpy/issues/1250))
- reduce result\_timeout to 10 secs from 15 mins. ([#1171](https://github.com/ros2/rclpy/issues/1171))
- Add TimerInfo to timer callback. ([#1292](https://github.com/ros2/rclpy/issues/1292))
- Add types to task.py ([#1254](https://github.com/ros2/rclpy/issues/1254))
- Fix a bad bug in fetching the lifecycle transitions. ([#1321](https://github.com/ros2/rclpy/issues/1321))
- Fix a bug when using multiple rclpy.init context managers. ([#1314](https://github.com/ros2/rclpy/issues/1314))
- Executor executes the tasks in FIFO order. ([#1304](https://github.com/ros2/rclpy/issues/1304))
- Add top-level try\_shutdown method. ([#1302](https://github.com/ros2/rclpy/issues/1302))
- Make rclpy initialization context-manager aware. ([#1298](https://github.com/ros2/rclpy/issues/1298))
- Docstring specifying proper destruction and creation of Rate, Timer and GuardCondition ([#1286](https://github.com/ros2/rclpy/issues/1286))
- Make timers context-aware. ([#1296](https://github.com/ros2/rclpy/issues/1296))
- Make service lients context-aware. ([#1295](https://github.com/ros2/rclpy/issues/1295))
- Make service servers context-manager aware. ([#1294](https://github.com/ros2/rclpy/issues/1294))
- Make nodes context-manager aware. ([#1293](https://github.com/ros2/rclpy/issues/1293))
- Make subscriptions context-manager aware. ([#1291](https://github.com/ros2/rclpy/issues/1291))
- Make publishers context-manager aware. ([#1289](https://github.com/ros2/rclpy/issues/1289))
- (NumberOfEntities) improve performance ([#1285](https://github.com/ros2/rclpy/issues/1285))
- Using Generics for messages ([#1239](https://github.com/ros2/rclpy/issues/1239))
- Contributors: Alejandro Hernández Cordero, Arjo Chakravarty, Barry Xu, Brad Martin, Chris Lalancette, Christophe Bedard, Elian NEPPEL, Jonathan, Matthijs van der Burgh, Michael Carlstrom, Nadav Elkabets, R Kent James, Shane Loretz, Tomoya Fujita, Wolf Vollprecht, Zahi Kakish

<a id="rcpputils"></a>

## [rcpputils](https://github.com/ros2/rcpputils/tree/kilted/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#211](https://github.com/ros2/rcpputils/issues/211))
- Added marco to disable deprecation warnings ([#210](https://github.com/ros2/rcpputils/issues/210))
- Added missing include ([#207](https://github.com/ros2/rcpputils/issues/207))
- Clear the rcutils error when throwing an exception. ([#206](https://github.com/ros2/rcpputils/issues/206))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#204](https://github.com/ros2/rcpputils/issues/204))
- fix memory leak for remove\_all(). ([#201](https://github.com/ros2/rcpputils/issues/201))
- Suppress clang error because of deprecation ([#199](https://github.com/ros2/rcpputils/issues/199))
- Deprecated path class ([#196](https://github.com/ros2/rcpputils/issues/196))
- Replace create\_temp\_directory with the new create\_temporary\_directory ([#198](https://github.com/ros2/rcpputils/issues/198)) \* Replace create\_temp\_directory with the new create\_temporary\_directory - The newly added `create_temporary_directory(..)` uses std::filesystem::path and doesn’t have platform-specific code. - Also deprecated `create_temp_directory(..)` and `temp_directory_path`
- Removed deprecated header get\_env.hpp ([#195](https://github.com/ros2/rcpputils/issues/195))
- Removed rolling mean accumulator deprecated header ([#194](https://github.com/ros2/rcpputils/issues/194))
- Removed deprecated clamp methods ([#193](https://github.com/ros2/rcpputils/issues/193))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch Machowinski, Michael Carroll, Michael Orlov, Tomoya Fujita

<a id="rcutils"></a>

## [rcutils](https://github.com/ros2/rcutils/tree/kilted/CHANGELOG.rst)

- Handle spaces in start\_process arguments on Windows ([#494](https://github.com/ros2/rcutils/issues/494))
- Add utility functions for invoking a subprocess ([#491](https://github.com/ros2/rcutils/issues/491)) ([#492](https://github.com/ros2/rcutils/issues/492))
- Add rcutils\_join function for concatenating strings ([#490](https://github.com/ros2/rcutils/issues/490))
- Switch to ament\_cmake\_ros\_core package ([#489](https://github.com/ros2/rcutils/issues/489))
- Cleanup error handling in rcutils. ([#485](https://github.com/ros2/rcutils/issues/485))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#483](https://github.com/ros2/rcutils/issues/483))
- Fix setting allocator to NULL. ([#478](https://github.com/ros2/rcutils/issues/478))
- Add new API to set envar while specifying overwrite ([#473](https://github.com/ros2/rcutils/issues/473))
- Remove completely unnecessary use of CLASSNAME. ([#471](https://github.com/ros2/rcutils/issues/471))
- load dll built by MINGW with lib prefix ([#470](https://github.com/ros2/rcutils/issues/470))
- add mingw support ([#468](https://github.com/ros2/rcutils/issues/468))
- Fix filesystem iteration on Windows ([#469](https://github.com/ros2/rcutils/issues/469))
- Add ‘mimick’ label to tests which use Mimick ([#466](https://github.com/ros2/rcutils/issues/466))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Felix F Xu, Michael Carroll, Scott K Logan, Yadu

<a id="resource-retriever"></a>

## [resource\_retriever](https://github.com/ros/resource_retriever/tree/kilted/resource_retriever/CHANGELOG.rst)

- Fixed clang compile error ([#112](https://github.com/ros/resource_retriever/issues/112))
- Removed windows warnings ([#111](https://github.com/ros/resource_retriever/issues/111))
- Add a plugin mechanism to resource\_retriever ([#103](https://github.com/ros/resource_retriever/issues/103))
- uniform MinCMakeVersion ([#108](https://github.com/ros/resource_retriever/issues/108))
- Stop using python\_cmake\_module. ([#94](https://github.com/ros/resource_retriever/issues/94))
- Allow spaces ([#100](https://github.com/ros/resource_retriever/issues/100))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael Carroll, mosfet80

<a id="rmw"></a>

## [rmw](https://github.com/ros2/rmw/tree/kilted/rmw/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#397](https://github.com/ros2/rmw/issues/397))
- Added rmw\_event\_type\_is\_supported ([#395](https://github.com/ros2/rmw/issues/395))
- add enclave option functions. ([#393](https://github.com/ros2/rmw/issues/393))
- a couple of typo fixes for doc section. ([#391](https://github.com/ros2/rmw/issues/391))
- update cmake version ([#389](https://github.com/ros2/rmw/issues/389))
- get\_zero\_initialized\_xxx functions return zero initialized structure. ([#380](https://github.com/ros2/rmw/issues/380)) \* get\_zero\_initialized\_xxx functions return zero initialized structure. \* introduce RMW\_EVENT\_TYPE\_MAX in rmw\_event\_type\_t. \* add a comment and more tests for rmw\_event\_type. ———
- move qos\_profile\_rosout\_default from rcl. ([#381](https://github.com/ros2/rmw/issues/381))
- Fix ugly overwritten warning messages on error paths. ([#387](https://github.com/ros2/rmw/issues/387)) This mostly has to do with calling rmw\_reset\_error() in the proper time in the tests, but we also change one test for an allocator to properly check for a valid allocator.
- Fix rmw\_validate\_namespace{\_with\_size} error handling. ([#386](https://github.com/ros2/rmw/issues/386)) \* Fix rmw\_validate\_namespace{\_with\_size} error handling. It should always set an error, even on invalid arguments.
- Fix arg name in rmw\_take\_response() doc ([#384](https://github.com/ros2/rmw/issues/384))
- Initialize the NULL strucutre with static value. ([#378](https://github.com/ros2/rmw/issues/378))
- remove rmw\_localhost\_only\_t. ([#376](https://github.com/ros2/rmw/issues/376))
- Fix typo with RMW\_DURATION\_UNSPECIFIED ([#375](https://github.com/ros2/rmw/issues/375))
- Fix typo in rmw\_validate\_\*\_with\_size() doc ([#374](https://github.com/ros2/rmw/issues/374))
- removed deprecated rmw\_node\_assert\_liveliness() ([#373](https://github.com/ros2/rmw/issues/373))
- add mingw support ([#370](https://github.com/ros2/rmw/issues/370))
- Minor typo fix ([#368](https://github.com/ros2/rmw/issues/368))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Felix F Xu, G.A. vd. Hoorn, Michael Carroll, Tomoya Fujita

<a id="rmw-connextdds"></a>

## [rmw\_connextdds](https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextdds/CHANGELOG.rst)

- Switch buildtool to ament\_cmake package ([#183](https://github.com/ros2/rmw_connextdds/issues/183))
- Export a modern CMake target ([#179](https://github.com/ros2/rmw_connextdds/issues/179))
- Added rmw\_event\_type\_is\_supported ([#173](https://github.com/ros2/rmw_connextdds/issues/173))
- Contributors: Alejandro Hernández Cordero, Scott K Logan, Shane Loretz

<a id="rmw-connextdds-common"></a>

## [rmw\_connextdds\_common](https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextdds_common/CHANGELOG.rst)

- Address cpplit and gcc warnings. ([#184](https://github.com/ros2/rmw_connextdds/issues/184))
- Support topic instances ([#178](https://github.com/ros2/rmw_connextdds/issues/178))
- Switch buildtool to ament\_cmake package ([#183](https://github.com/ros2/rmw_connextdds/issues/183))
- Discovery race condition mitigation ([#174](https://github.com/ros2/rmw_connextdds/issues/174))
- Added rmw\_event\_type\_is\_supported ([#173](https://github.com/ros2/rmw_connextdds/issues/173))
- use rmw\_enclave\_options\_xxx APIs instead. ([#172](https://github.com/ros2/rmw_connextdds/issues/172))
- fix security certificate error message format. ([#171](https://github.com/ros2/rmw_connextdds/issues/171))
- Use rmw\_security\_common ([#167](https://github.com/ros2/rmw_connextdds/issues/167))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#169](https://github.com/ros2/rmw_connextdds/issues/169))
- introduce RMW\_EVENT\_TYPE\_MAX in rmw\_event\_type\_t. ([#162](https://github.com/ros2/rmw_connextdds/issues/162))
- Instrument client/service for end-to-end request/response tracking ([#163](https://github.com/ros2/rmw_connextdds/issues/163))
- fix: “Failed to parse type hash” message was overly spammy (ros2-50) ([#149](https://github.com/ros2/rmw_connextdds/issues/149))
- remove rmw\_localhost\_only\_t. ([#156](https://github.com/ros2/rmw_connextdds/issues/156))
- Make rmw\_service\_server\_is\_available return RMW\_RET\_INVALID\_ARGUMENT ([#150](https://github.com/ros2/rmw_connextdds/issues/150))
- Use rmw\_namespace\_validation\_result\_string() in rmw\_create\_node ([#151](https://github.com/ros2/rmw_connextdds/issues/151))
- Make rmw\_destroy\_wait\_set return RMW\_RET\_INVALID\_ARGUMENT ([#152](https://github.com/ros2/rmw_connextdds/issues/152))
- Contributors: Alejandro Hernández Cordero, Christophe Bedard, Francisco Gallego Salido, Scott K Logan, Shane Loretz, Taxo Rubio RTI, Tomoya Fujita

<a id="rmw-connextddsmicro"></a>

## [rmw\_connextddsmicro](https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextddsmicro/CHANGELOG.rst)

- Mark the package rmw\_connextddsmicro as deprecated ([#182](https://github.com/ros2/rmw_connextdds/issues/182))
- Switch buildtool to ament\_cmake package ([#183](https://github.com/ros2/rmw_connextdds/issues/183))
- Added rmw\_event\_type\_is\_supported ([#173](https://github.com/ros2/rmw_connextdds/issues/173))
- Contributors: Alejandro Hernández Cordero, Francisco Gallego Salido, Scott K Logan

<a id="rmw-cyclonedds-cpp"></a>

## [rmw\_cyclonedds\_cpp](https://github.com/ros2/rmw_cyclonedds/tree/kilted/rmw_cyclonedds_cpp/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#538](https://github.com/ros2/rmw_cyclonedds/issues/538))
- Added rmw\_event\_type\_is\_supported ([#532](https://github.com/ros2/rmw_cyclonedds/issues/532))
- use rmw\_enclave\_options\_xxx APIs instead. ([#531](https://github.com/ros2/rmw_cyclonedds/issues/531))
- use rmw\_security\_common ([#529](https://github.com/ros2/rmw_cyclonedds/issues/529))
- introduce RMW\_EVENT\_TYPE\_MAX in rmw\_event\_type\_t. ([#518](https://github.com/ros2/rmw_cyclonedds/issues/518))
- Reset the error before setting a new one. ([#526](https://github.com/ros2/rmw_cyclonedds/issues/526))
- Instrument client/service for end-to-end request/response tracking ([#521](https://github.com/ros2/rmw_cyclonedds/issues/521))
- Drop support for float128. ([#522](https://github.com/ros2/rmw_cyclonedds/issues/522))
- use RMW\_GID\_STORAGE\_SIZE to client\_service\_id\_t. ([#515](https://github.com/ros2/rmw_cyclonedds/issues/515))
- remove rmw\_localhost\_only\_t. ([#508](https://github.com/ros2/rmw_cyclonedds/issues/508))
- Fix the triggering of guard conditions. ([#504](https://github.com/ros2/rmw_cyclonedds/issues/504)) When a guard condition goes active, we have to remember to increase the trig\_idx so we look at the next trigger. Otherwise, we can get into situations where we skip a triggered member.
- Make rmw\_service\_server\_is\_available return RMW\_RET\_INVALID\_ARGUMENT ([#496](https://github.com/ros2/rmw_cyclonedds/issues/496))
- Use rmw\_namespace\_validation\_result\_string() in rmw\_create\_node ([#497](https://github.com/ros2/rmw_cyclonedds/issues/497))
- Make rmw\_destroy\_wait\_set return RMW\_RET\_INVALID\_ARGUMENT ([#498](https://github.com/ros2/rmw_cyclonedds/issues/498))
- Set received\_timestamp to system\_clock::now() in message\_info ([#491](https://github.com/ros2/rmw_cyclonedds/issues/491))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Erik Boasson, Joe Speed, Jose Tomas Lorente, Michael Orlov, Scott K Logan, Tomoya Fujita

<a id="rmw-dds-common"></a>

## [rmw\_dds\_common](https://github.com/ros2/rmw_dds_common/tree/kilted/rmw_dds_common/CHANGELOG.rst)

- Deprecated security methods ([#77](https://github.com/ros2/rmw_dds_common/issues/77))
- Contributors: Alejandro Hernández Cordero

<a id="rmw-fastrtps-cpp"></a>

## [rmw\_fastrtps\_cpp](https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_cpp/CHANGELOG.rst)

- Address RHEL warnings and missing includes. ([#819](https://github.com/ros2/rmw_fastrtps/issues/819))
- Support topic instances ([#753](https://github.com/ros2/rmw_fastrtps/issues/753))
- Switch to ament\_cmake\_ros\_core package ([#818](https://github.com/ros2/rmw_fastrtps/issues/818))
- Added rmw\_event\_type\_is\_supported ([#809](https://github.com/ros2/rmw_fastrtps/issues/809))
- use rmw\_enclave\_options\_xxx APIs instead. ([#808](https://github.com/ros2/rmw_fastrtps/issues/808))
- Add deprecation warning for FASTRTPS\_DEFAULT\_PROFILES\_FILE ([#806](https://github.com/ros2/rmw_fastrtps/issues/806))
- Export a modern CMake target ([#805](https://github.com/ros2/rmw_fastrtps/issues/805))
- Changes to build against Fast DDS 3.0 ([#776](https://github.com/ros2/rmw_fastrtps/issues/776))
- Fix some overwritten errors in rmw\_fastrtps. ([#799](https://github.com/ros2/rmw_fastrtps/issues/799))
- Instrument client/service for end-to-end request/response tracking ([#787](https://github.com/ros2/rmw_fastrtps/issues/787))
- Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan, Shane Loretz, Tomoya Fujita

<a id="rmw-fastrtps-dynamic-cpp"></a>

## [rmw\_fastrtps\_dynamic\_cpp](https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst)

- Address RHEL warnings and missing includes. ([#819](https://github.com/ros2/rmw_fastrtps/issues/819))
- Support topic instances ([#753](https://github.com/ros2/rmw_fastrtps/issues/753))
- Switch to ament\_cmake\_ros\_core package ([#818](https://github.com/ros2/rmw_fastrtps/issues/818))
- Make rmw\_fastrtps\_dynamic\_cpp export a modern CMake target ([#814](https://github.com/ros2/rmw_fastrtps/issues/814))
- Added rmw\_event\_type\_is\_supported ([#809](https://github.com/ros2/rmw_fastrtps/issues/809))
- use rmw\_enclave\_options\_xxx APIs instead. ([#808](https://github.com/ros2/rmw_fastrtps/issues/808))
- Add deprecation warning for FASTRTPS\_DEFAULT\_PROFILES\_FILE ([#806](https://github.com/ros2/rmw_fastrtps/issues/806))
- Changes to build against Fast DDS 3.0 ([#776](https://github.com/ros2/rmw_fastrtps/issues/776))
- Fix some overwritten errors in rmw\_fastrtps. ([#799](https://github.com/ros2/rmw_fastrtps/issues/799))
- Instrument client/service for end-to-end request/response tracking ([#787](https://github.com/ros2/rmw_fastrtps/issues/787))
- Add tracing instrumentation to rmw\_fastrtps\_dynamic\_cpp ([#772](https://github.com/ros2/rmw_fastrtps/issues/772))
- Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan, Shane Loretz, Tomoya Fujita

<a id="rmw-fastrtps-shared-cpp"></a>

## [rmw\_fastrtps\_shared\_cpp](https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_shared_cpp/CHANGELOG.rst)

- Address RHEL warnings and missing includes. ([#819](https://github.com/ros2/rmw_fastrtps/issues/819))
- Support topic instances ([#753](https://github.com/ros2/rmw_fastrtps/issues/753))
- Switch to ament\_cmake\_ros\_core package ([#818](https://github.com/ros2/rmw_fastrtps/issues/818))
- Added rmw\_event\_type\_is\_supported ([#809](https://github.com/ros2/rmw_fastrtps/issues/809))
- use rmw\_enclave\_options\_xxx APIs instead. ([#808](https://github.com/ros2/rmw_fastrtps/issues/808))
- Add deprecation warning for FASTRTPS\_DEFAULT\_PROFILES\_FILE ([#806](https://github.com/ros2/rmw_fastrtps/issues/806))
- Use rmw\_security\_common ([#803](https://github.com/ros2/rmw_fastrtps/issues/803))
- introduce RMW\_EVENT\_TYPE\_MAX in rmw\_event\_type\_t. ([#785](https://github.com/ros2/rmw_fastrtps/issues/785))
- Changes to build against Fast DDS 3.0 ([#776](https://github.com/ros2/rmw_fastrtps/issues/776))
- Cleanup one test in rmw\_fastrtps\_shared\_cpp. ([#794](https://github.com/ros2/rmw_fastrtps/issues/794))
- Instrument client/service for end-to-end request/response tracking ([#787](https://github.com/ros2/rmw_fastrtps/issues/787))
- Drop support for float128. ([#788](https://github.com/ros2/rmw_fastrtps/issues/788))
- Keep reference to `DomainParticipantFactory` ([#770](https://github.com/ros2/rmw_fastrtps/issues/770))
- Use client’s reader guid for service introspection event gid ([#781](https://github.com/ros2/rmw_fastrtps/issues/781))
- Revert “Unique Client GID for Service Introspectino Event. ([#779](https://github.com/ros2/rmw_fastrtps/issues/779))” ([#780](https://github.com/ros2/rmw_fastrtps/issues/780))
- Unique Client GID for Service Introspectino Event. ([#779](https://github.com/ros2/rmw_fastrtps/issues/779))
- remove rmw\_localhost\_only\_t. ([#773](https://github.com/ros2/rmw_fastrtps/issues/773))
- Make rmw\_service\_server\_is\_available return RMW\_RET\_INVALID\_ARGUMENT ([#763](https://github.com/ros2/rmw_fastrtps/issues/763))
- Use rmw\_namespace\_validation\_result\_string() in rmw\_create\_node ([#765](https://github.com/ros2/rmw_fastrtps/issues/765))
- Make rmw\_destroy\_wait\_set return RMW\_RET\_INVALID\_ARGUMENT ([#766](https://github.com/ros2/rmw_fastrtps/issues/766))
- Use unique mangled names when creating Content Filter Topics ([#762](https://github.com/ros2/rmw_fastrtps/issues/762))
- Add support for data representation ([#756](https://github.com/ros2/rmw_fastrtps/issues/756))
- Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Jorge J. Perez, Mario Domínguez López, Miguel Company, Scott K Logan, Tomoya Fujita

<a id="rmw-implementation"></a>

## [rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/kilted/rmw_implementation/CHANGELOG.rst)

- Added rmw\_event\_type\_is\_supported ([#250](https://github.com/ros2/rmw_implementation/issues/250))
- Make sure to find\_package(rmw) in rmw\_implementation. ([#242](https://github.com/ros2/rmw_implementation/issues/242))
- Add mechanism to disable workaround for dependency groups ([#229](https://github.com/ros2/rmw_implementation/issues/229))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Scott K Logan

<a id="rmw-implementation-cmake"></a>

## [rmw\_implementation\_cmake](https://github.com/ros2/rmw/tree/kilted/rmw_implementation_cmake/CHANGELOG.rst)

- update cmake version ([#389](https://github.com/ros2/rmw/issues/389))
- Contributors: Alejandro Hernández Cordero

<a id="rmw-security-common"></a>

## [rmw\_security\_common](https://github.com/ros2/rmw/tree/kilted/rmw_security_common/CHANGELOG.rst)

- Export rmw dependency ([#400](https://github.com/ros2/rmw/issues/400))
- Added rmw\_security\_common ([#388](https://github.com/ros2/rmw/issues/388))
- Contributors: Alejandro Hernández Cordero, yadunund

<a id="rmw-test-fixture"></a>

## [rmw\_test\_fixture](https://github.com/ros2/ament_cmake_ros/tree/kilted/rmw_test_fixture/CHANGELOG.rst)

- Resolve windows warnings in rmw\_test\_fixture ([#22](https://github.com/ros2/ament_cmake_ros/issues/22))
- Add rmw\_test\_fixture for supporting RMW-isolated testing ([#21](https://github.com/ros2/ament_cmake_ros/issues/21))
- Contributors: Alejandro Hernández Cordero, Scott K Logan

<a id="rmw-test-fixture-implementation"></a>

## [rmw\_test\_fixture\_implementation](https://github.com/ros2/ament_cmake_ros/tree/kilted/rmw_test_fixture_implementation/CHANGELOG.rst)

- Don’t set ROS\_AUTOMATIC\_DISCOVERY\_RANGE in rmw\_test\_fixture ([#33](https://github.com/ros2/ament_cmake_ros/issues/33))
- Fix rmw\_test\_fixture DLL import on Windows ([#32](https://github.com/ros2/ament_cmake_ros/issues/32))
- Fix range for rmw\_test\_fixture\_default port locking ([#31](https://github.com/ros2/ament_cmake_ros/issues/31))
- Stop loading RMW to load the test fixture ([#30](https://github.com/ros2/ament_cmake_ros/issues/30))
- Add ‘default’ rmw\_test\_fixture based on domain\_coordinator ([#26](https://github.com/ros2/ament_cmake_ros/issues/26))
- Install run\_rmw\_isolated executable to lib subdirectory ([#25](https://github.com/ros2/ament_cmake_ros/issues/25))
- Ignore Ctrl-C in run\_rmw\_isolated on Windows ([#24](https://github.com/ros2/ament_cmake_ros/issues/24))
- Resolve windows warnings in rmw\_test\_fixture ([#22](https://github.com/ros2/ament_cmake_ros/issues/22))
- Add rmw\_test\_fixture for supporting RMW-isolated testing ([#21](https://github.com/ros2/ament_cmake_ros/issues/21))
- Contributors: Alejandro Hernández Cordero, Scott K Logan

<a id="rmw-zenoh-cpp"></a>

## [rmw\_zenoh\_cpp](https://github.com/ros2/rmw_zenoh/tree/kilted/rmw_zenoh_cpp/CHANGELOG.rst)

- Change serialization format in attachment\_helpers.cpp ([#601](https://github.com/ros2/rmw_zenoh/issues/601))
- Bump Zenoh to v1.3.2 and improve e2e reliability with HeartbeatSporadic ([#591](https://github.com/ros2/rmw_zenoh/issues/591))
- Implement rmw\_test\_fixture to start the Zenoh router ([#583](https://github.com/ros2/rmw_zenoh/issues/583))
- Add quality declaration ([#483](https://github.com/ros2/rmw_zenoh/issues/483))
- Trigger qos event callback if there are changes before registration ([#587](https://github.com/ros2/rmw_zenoh/issues/587))
- Set wait\_set->triggered flag to false ([#575](https://github.com/ros2/rmw_zenoh/issues/575))
- Add space after `id` token in `rmw_zenohd` log string ([#576](https://github.com/ros2/rmw_zenoh/issues/576))
- Use `std::unique_lock` to unlock correctly on Windows ([#570](https://github.com/ros2/rmw_zenoh/issues/570))
- Switch to std::map for TopicTypeMap ([#546](https://github.com/ros2/rmw_zenoh/issues/546))
- Support zenoh config override ([#551](https://github.com/ros2/rmw_zenoh/issues/551))
- Align the config with the latest Zenoh. ([#556](https://github.com/ros2/rmw_zenoh/issues/556))
- Added documentation note in the code ([#540](https://github.com/ros2/rmw_zenoh/issues/540))
- fix: unlock the mutex before making get ([#537](https://github.com/ros2/rmw_zenoh/issues/537))
- Take wait\_set\_lock before condition\_variable notification for subscriptions ([#528](https://github.com/ros2/rmw_zenoh/issues/528))
- Switch default durability to volatile ([#521](https://github.com/ros2/rmw_zenoh/issues/521))
- Added rmw\_event\_type\_is\_supported ([#502](https://github.com/ros2/rmw_zenoh/issues/502))
- Fixed windows warning ([#500](https://github.com/ros2/rmw_zenoh/issues/500))
- Config: tune some values for ROS use case, especially with large number of Nodes (>200) ([#509](https://github.com/ros2/rmw_zenoh/issues/509))
- Honor ignore\_local\_publications in subscription options ([#508](https://github.com/ros2/rmw_zenoh/issues/508))
- Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5 ([#503](https://github.com/ros2/rmw_zenoh/issues/503))
- Fix calculation of current\_count\_change when event status is updated ([#504](https://github.com/ros2/rmw_zenoh/issues/504))
- Fix checks for invalid arguments ([#497](https://github.com/ros2/rmw_zenoh/issues/497))
- Fail creation of entities if qos contains unknown settings ([#494](https://github.com/ros2/rmw_zenoh/issues/494))
- use rmw\_enclave\_options\_xxx APIs instead. ([#491](https://github.com/ros2/rmw_zenoh/issues/491))
- Enable Zenoh UDP transport ([#486](https://github.com/ros2/rmw_zenoh/issues/486))
- fix: use the default destructor that automatically drops the zenoh reply/query and hence sends the final signal ([#473](https://github.com/ros2/rmw_zenoh/issues/473))
- Introduce the advanced publisher and subscriber ([#368](https://github.com/ros2/rmw_zenoh/issues/368))
- Switch to debug log if topic\_name not in topic\_map ([#454](https://github.com/ros2/rmw_zenoh/issues/454))
- Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) ([#456](https://github.com/ros2/rmw_zenoh/issues/456))
- Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) ([#446](https://github.com/ros2/rmw_zenoh/issues/446))
- Inform users that peers will not discover and communicate with one another until the router is started ([#440](https://github.com/ros2/rmw_zenoh/issues/440))
- Clear the error after rmw\_serialized\_message\_resize() ([#435](https://github.com/ros2/rmw_zenoh/issues/435))
- Fix `ZENOH_ROUTER_CHECK_ATTEMPTS` which was not respected ([#427](https://github.com/ros2/rmw_zenoh/issues/427))
- fix: use the default destructor to drop the member `Payload` ([#419](https://github.com/ros2/rmw_zenoh/issues/419))
- Remove `gid_hash\_` from `AttachmentData` ([#416](https://github.com/ros2/rmw_zenoh/issues/416))
- Sync the config with the default config in Zenoh. ([#396](https://github.com/ros2/rmw_zenoh/issues/396))
- fix: check the context validity before accessing the session ([#403](https://github.com/ros2/rmw_zenoh/issues/403))
- Fix wan’t typo ([#400](https://github.com/ros2/rmw_zenoh/issues/400))
- An alternative middleware for ROS 2 based on Zenoh.
- Contributors: Alejandro Hernández Cordero, Alex Day, Bernd Pfrommer, ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard, CihatAltiparmak, Esteve Fernandez, Franco Cipollone, Geoffrey Biggs, Hans-Martin, Hugal31, James Mount, Julien Enoch, Luca Cominardi, Mahmoud Mazouz, Morgan Quigley, Nate Koenig, Patrick Roncagliolo, Scott K Logan, Shivang Vijay, Tim Clephas, Tomoya Fujita, Yadunund, Yuyuan Yuan, methylDragon, yadunund, yellowhatter

<a id="robot-state-publisher"></a>

## [robot\_state\_publisher](https://github.com/ros/robot_state_publisher/tree/kilted/CHANGELOG.rst)

- Use `emplace()` with `std::map` ([#231](https://github.com/ros/robot_state_publisher/issues/231))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#229](https://github.com/ros/robot_state_publisher/issues/229))
- update urdf model header ([#223](https://github.com/ros/robot_state_publisher/issues/223))
- Contributors: Alejandro Hernández Cordero, Patrick Roncagliolo

<a id="ros2action"></a>

## [ros2action](https://github.com/ros2/ros2cli/tree/kilted/ros2action/CHANGELOG.rst)

- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Support ‘ros2 action echo’ ([#978](https://github.com/ros2/ros2cli/issues/978))
- Correct the license content ([#979](https://github.com/ros2/ros2cli/issues/979))
- Maintaining consistency of automatically putting time stamps in the service and action calls similiar to publishing in rostopics. ([#961](https://github.com/ros2/ros2cli/issues/961))
- ros2action: add SIGINT handler to manage cancel request. ([#956](https://github.com/ros2/ros2cli/issues/956))
- node name print bug fix with ros2 action info. ([#926](https://github.com/ros2/ros2cli/issues/926))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- support ‘ros2 action find’. ([#917](https://github.com/ros2/ros2cli/issues/917))
- Contributors: Barry Xu, Chris Lalancette, Michael Carroll, Sukhvansh Jain, Tomoya Fujita

<a id="ros2bag"></a>

## [ros2bag](https://github.com/ros2/rosbag2/tree/kilted/ros2bag/CHANGELOG.rst)

- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Fix for failing test\_record\_qos\_profiles on Windows ([#1949](https://github.com/ros2/rosbag2/issues/1949))
- Progress bar for ros2 bag play ([#1836](https://github.com/ros2/rosbag2/issues/1836))
- Update CLI play verb metavar ([#1906](https://github.com/ros2/rosbag2/issues/1906))
- Add test\_xmllint.py to python packages. ([#1879](https://github.com/ros2/rosbag2/issues/1879))
- Add support for replaying based on publication timestamp ([#1876](https://github.com/ros2/rosbag2/issues/1876))
- Publish clock after delay is over and disable delay on next loops ([#1861](https://github.com/ros2/rosbag2/issues/1861))
- Support replaying multiple bags ([#1848](https://github.com/ros2/rosbag2/issues/1848))
- Rename rclpy.qos.QoS\*Policy to rclpy.qos.\*Policy ([#1832](https://github.com/ros2/rosbag2/issues/1832))
- Add “–sort” CLI option to the “ros2 bag info” command ([#1804](https://github.com/ros2/rosbag2/issues/1804))
- Add cli option compression-threads-priority ([#1768](https://github.com/ros2/rosbag2/issues/1768))
- Add computation of size contribution to info verb ([#1726](https://github.com/ros2/rosbag2/issues/1726))
- fix(start-offset): allow specifying a start offset of 0 ([#1682](https://github.com/ros2/rosbag2/issues/1682))
- Exclude recorded /clock topic when –clock option is specified ([#1646](https://github.com/ros2/rosbag2/issues/1646))
- Sweep cleanup in rosbag2 recorder CLI args verification code ([#1633](https://github.com/ros2/rosbag2/issues/1633))
- Add –log-level to ros2 bag play and record ([#1625](https://github.com/ros2/rosbag2/issues/1625))
- Add optional ‘–topics’ CLI argument for ‘ros2 bag record’ ([#1632](https://github.com/ros2/rosbag2/issues/1632))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Kosuke Takeuchi, Michael Orlov, Nicola Loi, Patrick Roncagliolo, Rein Appeldoorn, Roman, Sanoronas

<a id="ros2cli"></a>

## [ros2cli](https://github.com/ros2/ros2cli/tree/kilted/ros2cli/CHANGELOG.rst)

- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Rename the test\_{daemon,direct}.py tests. ([#959](https://github.com/ros2/ros2cli/issues/959))
- replace removeprefix with string slicing. ([#953](https://github.com/ros2/ros2cli/issues/953))
- Fix instability in the ros2 daemon. ([#947](https://github.com/ros2/ros2cli/issues/947))
- Drop dependency on python3-pkg-resources ([#946](https://github.com/ros2/ros2cli/issues/946))
- NodeStrategy supports node name argument. ([#941](https://github.com/ros2/ros2cli/issues/941))
- Switch to using the rclpy.init context manager. ([#920](https://github.com/ros2/ros2cli/issues/920))
- Contributors: Chris Lalancette, Michael Carroll, Scott K Logan, Tomoya Fujita

<a id="ros2doctor"></a>

## [ros2doctor](https://github.com/ros2/ros2cli/tree/kilted/ros2doctor/CHANGELOG.rst)

- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Skip QoS compatibility test on Zenoh ([#985](https://github.com/ros2/ros2cli/issues/985))
- New flag and code update for its use ([#942](https://github.com/ros2/ros2cli/issues/942))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- Revamp how we get network information in ros2doctor. ([#910](https://github.com/ros2/ros2cli/issues/910))
- Contributors: Alejandro Hernández Cordero, Angel LoGa, Chris Lalancette, Michael Carroll

<a id="ros2launch"></a>

## [ros2launch](https://github.com/ros2/launch_ros/tree/kilted/ros2launch/CHANGELOG.rst)

- Add ament\_xmllint to the ament\_python packages. ([#423](https://github.com/ros2/launch_ros/issues/423))
- Fix url in setup.py ([#413](https://github.com/ros2/launch_ros/issues/413))
- Add mechanism to disable workaround for dependency groups ([#397](https://github.com/ros2/launch_ros/issues/397))
- Contributors: Chris Lalancette, Scott K Logan, Wei HU

<a id="ros2lifecycle"></a>

## [ros2lifecycle](https://github.com/ros2/ros2cli/tree/kilted/ros2lifecycle/CHANGELOG.rst)

- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Contributors: Michael Carroll

<a id="ros2lifecycle-test-fixtures"></a>

## [ros2lifecycle\_test\_fixtures](https://github.com/ros2/ros2cli/tree/kilted/ros2lifecycle_test_fixtures/CHANGELOG.rst)

- Use target\_link\_libraries instead of ament\_target\_dependencies ([#973](https://github.com/ros2/ros2cli/issues/973))
- Contributors: Shane Loretz

<a id="ros2node"></a>

## [ros2node](https://github.com/ros2/ros2cli/tree/kilted/ros2node/CHANGELOG.rst)

- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- ros2node requires fully qualified node name. ([#923](https://github.com/ros2/ros2cli/issues/923))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita

<a id="ros2param"></a>

## [ros2param](https://github.com/ros2/ros2cli/tree/kilted/ros2param/CHANGELOG.rst)

- Fix loading parameter behavior from yaml file ([#864](https://github.com/ros2/ros2cli/issues/864))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- cosmetic fixes for ros2param dump command. ([#933](https://github.com/ros2/ros2cli/issues/933))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita

<a id="ros2pkg"></a>

## [ros2pkg](https://github.com/ros2/ros2cli/tree/kilted/ros2pkg/CHANGELOG.rst)

- Use modern C++17 syntax. ([#982](https://github.com/ros2/ros2cli/issues/982))
- Use target\_link\_libraries instead of ament\_target\_dependencies ([#973](https://github.com/ros2/ros2cli/issues/973))
- Try to use the git global user.name for maintainer-name ([#968](https://github.com/ros2/ros2cli/issues/968))
- Update minimum CMake version CMakeLists.txt.em ([#969](https://github.com/ros2/ros2cli/issues/969))
- Add ament\_xmllint test by default to ament\_python packages. ([#957](https://github.com/ros2/ros2cli/issues/957))
- Drop dependency on python3-pkg-resources ([#946](https://github.com/ros2/ros2cli/issues/946))
- Support empy4 and empy3 ([#921](https://github.com/ros2/ros2cli/issues/921))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Larry Gezelius, Scott K Logan, Sebastian Castro, Shane Loretz, Shynur

<a id="ros2run"></a>

## [ros2run](https://github.com/ros2/ros2cli/tree/kilted/ros2run/CHANGELOG.rst)

- Add signal handler SIGIN/SIGTERM to ros2run ([#899](https://github.com/ros2/ros2cli/issues/899))
- Contributors: Tomoya Fujita

<a id="ros2service"></a>

## [ros2service](https://github.com/ros2/ros2cli/tree/kilted/ros2service/CHANGELOG.rst)

- Use `get_service` in `ros2service call` ([#994](https://github.com/ros2/ros2cli/issues/994))
- Allow zenoh tests to run with multicast ([#992](https://github.com/ros2/ros2cli/issues/992))
- Support QoS options for `ros2 service call` ([#966](https://github.com/ros2/ros2cli/issues/966))
- Maintaining consistency of automatically putting time stamps in the service and action calls similiar to publishing in rostopics. ([#961](https://github.com/ros2/ros2cli/issues/961))
- Switch to using the rclpy.init context manager. ([#920](https://github.com/ros2/ros2cli/issues/920))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- Contributors: Chris Lalancette, Michael Carlstrom, Michael Carroll, Sukhvansh Jain, Tomoya Fujita

<a id="ros2test"></a>

## [ros2test](https://github.com/ros2/ros_testing/tree/kilted/ros2test/CHANGELOG.rst)

- Add in test\_xmllint to ros2test. ([#13](https://github.com/ros2/ros_testing/issues/13))
- Contributors: Chris Lalancette

<a id="ros2topic"></a>

## [ros2topic](https://github.com/ros2/ros2cli/tree/kilted/ros2topic/CHANGELOG.rst)

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
- support multiple fields in ros2topic echo ([#964](https://github.com/ros2/ros2cli/issues/964))
- NodeStrategy supports node name argument. ([#941](https://github.com/ros2/ros2cli/issues/941))
- feat(echo –clear): add –clear option to echo ([#819](https://github.com/ros2/ros2cli/issues/819))
- Support multiple topics via ros2 topic hz. ([#929](https://github.com/ros2/ros2cli/issues/929))
- Remove TODO for OpenSplice DDS issue. ([#928](https://github.com/ros2/ros2cli/issues/928))
- Switch to using rclpy.init context manager. ([#918](https://github.com/ros2/ros2cli/issues/918))
- Contributors: Alejandro Hernández Cordero, Anthony Welte, Chris Lalancette, Fabian Thomsen, Florencia, Guillaume Beuzeboc, Kostubh Khandelwal, Leander Stephen D’Souza, Martin Pecka, Michael Carroll, SangtaekLee, Tomoya Fujita

<a id="ros2trace"></a>

## [ros2trace](https://github.com/ros2/ros2_tracing/tree/kilted/ros2trace/CHANGELOG.rst)

- Expose types for tracing tools ([#153](https://github.com/ros2/ros2_tracing/issues/153))
- Contributors: Michael Carlstrom

<a id="ros-environment"></a>

## [ros\_environment](https://github.com/ros/ros_environment/tree/kilted/CHANGELOG.rst)

- Update ROS\_DISTRO for Kilted Kaiju ([#41](https://github.com/ros/ros_environment/issues/41))
- Remove CODEOWNERS. ([#40](https://github.com/ros/ros_environment/issues/40))
- Contributors: Chris Lalancette, Scott K Logan

<a id="rosbag2"></a>

## [rosbag2](https://github.com/ros2/rosbag2/tree/kilted/rosbag2/CHANGELOG.rst)

- Support replaying multiple bags ([#1848](https://github.com/ros2/rosbag2/issues/1848))
- Contributors: Christophe Bedard

<a id="rosbag2-compression"></a>

## [rosbag2\_compression](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_compression/CHANGELOG.rst)

- Bugfix: Update metadata with new file\_info before saving it first time ([#1843](https://github.com/ros2/rosbag2/issues/1843))
- Make snapshot writing into a new file each time it is triggered ([#1842](https://github.com/ros2/rosbag2/issues/1842))
- Add cli option compression-threads-priority ([#1768](https://github.com/ros2/rosbag2/issues/1768))
- Bugfix for bag\_split event callbacks called to early with file compression ([#1643](https://github.com/ros2/rosbag2/issues/1643))
- Fix for regression in `open_succeeds_twice` and `minimal_writer_example` tests ([#1667](https://github.com/ros2/rosbag2/issues/1667))
- Bugfix for writer not being able to open again after closing ([#1599](https://github.com/ros2/rosbag2/issues/1599))
- Contributors: Alejandro Hernández Cordero, Michael Orlov, Roman, yschulz

<a id="rosbag2-cpp"></a>

## [rosbag2\_cpp](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_cpp/CHANGELOG.rst)

- Add support for finding action types message definitions in the `LocalMessageDefinitionSource` class to be able to store actions message definitions during recording. ([#1965](https://github.com/ros2/rosbag2/issues/1965))
- Add message sequence number to the messages write API ([#1961](https://github.com/ros2/rosbag2/issues/1961))
- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Set environment variables to run tests with `rmw_zenoh_cpp` with multicast discovery ([#1946](https://github.com/ros2/rosbag2/issues/1946))
- Add more logging info to storage and reader/writer open operations ([#1881](https://github.com/ros2/rosbag2/issues/1881))
- Add PlayerClock::wakeup() to interrupt sleeping ([#1869](https://github.com/ros2/rosbag2/issues/1869))
- Support replaying multiple bags ([#1848](https://github.com/ros2/rosbag2/issues/1848))
- Bugfix: Update metadata with new file\_info before saving it first time ([#1843](https://github.com/ros2/rosbag2/issues/1843))
- Make snapshot writing into a new file each time it is triggered ([#1842](https://github.com/ros2/rosbag2/issues/1842))
- Bugfix for rosbag2\_cpp serialization converter ([#1814](https://github.com/ros2/rosbag2/issues/1814))
- Allow unknown types in bag rewrite ([#1812](https://github.com/ros2/rosbag2/issues/1812))
- Add computation of size contribution to info verb ([#1726](https://github.com/ros2/rosbag2/issues/1726))
- [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740](https://github.com/ros2/rosbag2/issues/1740))
- Removed deprecated write method ([#1738](https://github.com/ros2/rosbag2/issues/1738))
- Bugfix for bag\_split event callbacks called to early with file compression ([#1643](https://github.com/ros2/rosbag2/issues/1643))
- Add topics with zero message counts to the SQLiteStorage::get\_metadata(). ([#1725](https://github.com/ros2/rosbag2/issues/1725))
- Propagate “custom\_data” and “ros\_distro” in to the metadata.yaml file during re-indexing ([#1700](https://github.com/ros2/rosbag2/issues/1700))
- Bugfix for writer not being able to open again after closing ([#1599](https://github.com/ros2/rosbag2/issues/1599))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Cole Tucker, Michael Orlov, Nicola Loi, Tomoya Fujita, Yadunund, yschulz

<a id="rosbag2-examples-cpp"></a>

## [rosbag2\_examples\_cpp](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst)

- Add rosbag2\_examples\_cpp/simple\_bag\_reader.cpp. ([#1683](https://github.com/ros2/rosbag2/issues/1683))
- Contributors: Tomoya Fujita

<a id="rosbag2-examples-py"></a>

## [rosbag2\_examples\_py](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst)

- avoid using internal modules for examples. ([#1905](https://github.com/ros2/rosbag2/issues/1905))
- Add test\_xmllint.py to python packages. ([#1879](https://github.com/ros2/rosbag2/issues/1879))
- simple\_bag\_reader.py should publish the data for each timer callback. ([#1767](https://github.com/ros2/rosbag2/issues/1767))
- Change the python examples to use the rclpy context manager. ([#1758](https://github.com/ros2/rosbag2/issues/1758))
- Add rosbag2\_examples\_cpp/simple\_bag\_reader.cpp. ([#1683](https://github.com/ros2/rosbag2/issues/1683))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="rosbag2-py"></a>

## [rosbag2\_py](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_py/CHANGELOG.rst)

- Add message sequence number to the messages write API ([#1961](https://github.com/ros2/rosbag2/issues/1961))
- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Add bindings to close method in PyReader and PyCompressionReader ([#1935](https://github.com/ros2/rosbag2/issues/1935))
- Remove SHARED from pybind11\_add\_module ([#1929](https://github.com/ros2/rosbag2/issues/1929))
- Progress bar for ros2 bag play ([#1836](https://github.com/ros2/rosbag2/issues/1836))
- Upstream quality changes from Apex.AI part 1 ([#1903](https://github.com/ros2/rosbag2/issues/1903))
- Add support for replaying based on publication timestamp ([#1876](https://github.com/ros2/rosbag2/issues/1876))
- Support replaying multiple bags ([#1848](https://github.com/ros2/rosbag2/issues/1848))
- Add in python3-dev build dependency. ([#1863](https://github.com/ros2/rosbag2/issues/1863))
- Add “–sort” CLI option to the “ros2 bag info” command ([#1804](https://github.com/ros2/rosbag2/issues/1804))
- Remove use of python\_cmake\_module ([#1570](https://github.com/ros2/rosbag2/issues/1570))
- Added method to introspect QoS in Python ([#1648](https://github.com/ros2/rosbag2/issues/1648))
- Update CI scripts to use Ubuntu Noble distros and bump action scripts to latest versions ([#1709](https://github.com/ros2/rosbag2/issues/1709))
- Add cli option compression-threads-priority ([#1768](https://github.com/ros2/rosbag2/issues/1768))
- Add computation of size contribution to info verb ([#1726](https://github.com/ros2/rosbag2/issues/1726))
- Bugfix for wrong timestamps in ros2 bag info ([#1745](https://github.com/ros2/rosbag2/issues/1745))
- Add bindings for LocalMessageDefinitionSource ([#1697](https://github.com/ros2/rosbag2/issues/1697))
- Add –log-level to ros2 bag play and record ([#1625](https://github.com/ros2/rosbag2/issues/1625))
- Included to\_rclcpp\_qos\_vector to Python wrappers ([#1642](https://github.com/ros2/rosbag2/issues/1642))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Roman, Sanoronas, Silvio Traversaro, methylDragon, Øystein Sture

<a id="rosbag2-storage"></a>

## [rosbag2\_storage](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage/CHANGELOG.rst)

- Add message sequence number to the messages write API ([#1961](https://github.com/ros2/rosbag2/issues/1961))
- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Add more logging info to storage and reader/writer open operations ([#1881](https://github.com/ros2/rosbag2/issues/1881))
- Contributors: Barry Xu, Michael Orlov

<a id="rosbag2-storage-mcap"></a>

## [rosbag2\_storage\_mcap](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage_mcap/CHANGELOG.rst)

- Add message sequence number to the messages write API ([#1961](https://github.com/ros2/rosbag2/issues/1961))
- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Upstream quality changes from Apex.AI part 1 ([#1903](https://github.com/ros2/rosbag2/issues/1903))
- Add vscode gitignore rule and remove vscode folder ([#1698](https://github.com/ros2/rosbag2/issues/1698))
- Contributors: Barry Xu, Michael Orlov, methylDragon

<a id="rosbag2-storage-sqlite3"></a>

## [rosbag2\_storage\_sqlite3](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage_sqlite3/CHANGELOG.rst)

- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Fix incorrect zero size for sqlite storage ([#1759](https://github.com/ros2/rosbag2/issues/1759))
- Fix for failing throws\_on\_invalid\_pragma\_in\_config\_file on Windows ([#1742](https://github.com/ros2/rosbag2/issues/1742))
- Add topics with zero message counts to the SQLiteStorage::get\_metadata(). ([#1725](https://github.com/ros2/rosbag2/issues/1725))
- Contributors: Barry Xu, Michael Orlov, Roman, Tomoya Fujita

<a id="rosbag2-test-common"></a>

## [rosbag2\_test\_common](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_test_common/CHANGELOG.rst)

- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Upstream quality changes from Apex.AI part 1 ([#1903](https://github.com/ros2/rosbag2/issues/1903))
- Use tmpfs in rosbag2 temporary\_directory\_fixture ([#1901](https://github.com/ros2/rosbag2/issues/1901))
- Add debug information for flaky can\_record\_again\_after\_stop test ([#1871](https://github.com/ros2/rosbag2/issues/1871))
- Remove use of python\_cmake\_module ([#1570](https://github.com/ros2/rosbag2/issues/1570))
- Improve the reliability of rosbag2 tests ([#1796](https://github.com/ros2/rosbag2/issues/1796))
- Small cleanups to the rosbag2 tests. ([#1792](https://github.com/ros2/rosbag2/issues/1792))
- [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740](https://github.com/ros2/rosbag2/issues/1740))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Michael Orlov

<a id="rosbag2-test-msgdefs"></a>

## [rosbag2\_test\_msgdefs](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_test_msgdefs/CHANGELOG.rst)

- Add support for finding action types message definitions in the `LocalMessageDefinitionSource` class to be able to store actions message definitions during recording. ([#1965](https://github.com/ros2/rosbag2/issues/1965))
- Contributors: Tomoya Fujita

<a id="rosbag2-tests"></a>

## [rosbag2\_tests](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_tests/CHANGELOG.rst)

- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Upstream quality changes from Apex.AI part 1 ([#1903](https://github.com/ros2/rosbag2/issues/1903))
- Increase timeout to 180s for test\_rosbag2\_record\_end\_to\_end ([#1889](https://github.com/ros2/rosbag2/issues/1889))
- Add “–sort” CLI option to the “ros2 bag info” command ([#1804](https://github.com/ros2/rosbag2/issues/1804))
- Improve the reliability of rosbag2 tests ([#1796](https://github.com/ros2/rosbag2/issues/1796))
- Small cleanups to the rosbag2 tests. ([#1792](https://github.com/ros2/rosbag2/issues/1792))
- Add computation of size contribution to info verb ([#1726](https://github.com/ros2/rosbag2/issues/1726))
- Bugfix for wrong timestamps in ros2 bag info ([#1745](https://github.com/ros2/rosbag2/issues/1745))
- Fix for a false negative integration test with bag split in recorder ([#1743](https://github.com/ros2/rosbag2/issues/1743))
- Propagate “custom\_data” and “ros\_distro” in to the metadata.yaml file during re-indexing ([#1700](https://github.com/ros2/rosbag2/issues/1700))
- Sweep cleanup in rosbag2 recorder CLI args verification code ([#1633](https://github.com/ros2/rosbag2/issues/1633))
- Fix for regression in `open_succeeds_twice` and `minimal_writer_example` tests ([#1667](https://github.com/ros2/rosbag2/issues/1667))
- Add optional ‘–topics’ CLI argument for ‘ros2 bag record’ ([#1632](https://github.com/ros2/rosbag2/issues/1632))
- Bugfix for writer not being able to open again after closing ([#1599](https://github.com/ros2/rosbag2/issues/1599))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Cole Tucker, Michael Orlov, Nicola Loi, Sanoronas, yadunund, yschulz

<a id="rosbag2-transport"></a>

## [rosbag2\_transport](https://github.com/ros2/rosbag2/tree/kilted/rosbag2_transport/CHANGELOG.rst)

- Add actions replay feature ([#1955](https://github.com/ros2/rosbag2/issues/1955))
- Implement actions recording and displaying information about recorded actions features ([#1939](https://github.com/ros2/rosbag2/issues/1939))
- Set environment variables to run tests with `rmw_zenoh_cpp` with multicast discovery ([#1946](https://github.com/ros2/rosbag2/issues/1946))
- Initialize filter with namespaced updated topics and services. (rolling) ([#1944](https://github.com/ros2/rosbag2/issues/1944))
- Fix: QoS incompatibilities are not expected with rmw\_zenoh\_cpp ([#1936](https://github.com/ros2/rosbag2/issues/1936))
- Address windows warnings in the progress bar class ([#1927](https://github.com/ros2/rosbag2/issues/1927))
- Don’t delete existing subscription if failed to create a new one ([#1923](https://github.com/ros2/rosbag2/issues/1923))
- Progress bar for ros2 bag play ([#1836](https://github.com/ros2/rosbag2/issues/1836))
- Upstream quality changes from Apex.AI part 1 ([#1903](https://github.com/ros2/rosbag2/issues/1903))
- Use tmpfs in rosbag2 temporary\_directory\_fixture ([#1901](https://github.com/ros2/rosbag2/issues/1901))
- Bugfix: Recorder discovery does not restart after being stopped ([#1894](https://github.com/ros2/rosbag2/issues/1894))
- Bugfix. Event publisher not starting for second run after stop ([#1888](https://github.com/ros2/rosbag2/issues/1888))
- Add support for replaying based on publication timestamp ([#1876](https://github.com/ros2/rosbag2/issues/1876))
- Publish clock after delay is over and disable delay on next loops ([#1861](https://github.com/ros2/rosbag2/issues/1861))
- Add PlayerClock::wakeup() to interrupt sleeping ([#1869](https://github.com/ros2/rosbag2/issues/1869))
- Add debug information for flaky can\_record\_again\_after\_stop test ([#1871](https://github.com/ros2/rosbag2/issues/1871))
- Support replaying multiple bags ([#1848](https://github.com/ros2/rosbag2/issues/1848))
- Reintroduce `Don't warn for unknown types if topics are not selected` ([#1825](https://github.com/ros2/rosbag2/issues/1825))
- Allow unknown types in bag rewrite ([#1812](https://github.com/ros2/rosbag2/issues/1812))
- Improve the reliability of rosbag2 tests ([#1796](https://github.com/ros2/rosbag2/issues/1796))
- Removed warnings ([#1794](https://github.com/ros2/rosbag2/issues/1794))
- Small cleanups to the rosbag2 tests. ([#1792](https://github.com/ros2/rosbag2/issues/1792))
- Add cli option compression-threads-priority ([#1768](https://github.com/ros2/rosbag2/issues/1768))
- [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740](https://github.com/ros2/rosbag2/issues/1740))
- Bugfix for bag\_split event callbacks called to early with file compression ([#1643](https://github.com/ros2/rosbag2/issues/1643))
- Bugfix for issue where unable to create composable nodes with compression ([#1679](https://github.com/ros2/rosbag2/issues/1679))
- Add support for “all” and “exclude” in RecordOptions YAML decoder ([#1664](https://github.com/ros2/rosbag2/issues/1664))
- Add unit tests to cover message’s send and received timestamps during recording ([#1641](https://github.com/ros2/rosbag2/issues/1641))
- Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Ramon Wijnands, Roderick Taylor, Roman, Yuyuan Yuan, Øystein Sture

<a id="rosidl-adapter"></a>

## [rosidl\_adapter](https://github.com/ros2/rosidl/tree/kilted/rosidl_adapter/CHANGELOG.rst)

- Types for rosidl\_adapter ([#828](https://github.com/ros2/rosidl/issues/828))
- Support empy3 and empy4 ([#821](https://github.com/ros2/rosidl/issues/821))
- Contributors: Alejandro Hernández Cordero, Michael Carlstrom

<a id="rosidl-cli"></a>

## [rosidl\_cli](https://github.com/ros2/rosidl/tree/kilted/rosidl_cli/CHANGELOG.rst)

- Rosidl cli types with `specs_set` fix ([#831](https://github.com/ros2/rosidl/issues/831))
- Contributors: Chris Lalancette, Michael Carlstrom

<a id="rosidl-core-generators"></a>

## [rosidl\_core\_generators](https://github.com/ros2/rosidl_core/tree/kilted/rosidl_core_generators/CHANGELOG.rst)

- Add mechanism to disable workaround for dependency groups ([#3](https://github.com/ros2/rosidl_core/issues/3))
- Contributors: Scott K Logan

<a id="rosidl-core-runtime"></a>

## [rosidl\_core\_runtime](https://github.com/ros2/rosidl_core/tree/kilted/rosidl_core_runtime/CHANGELOG.rst)

- Add mechanism to disable workaround for dependency groups ([#3](https://github.com/ros2/rosidl_core/issues/3))
- Contributors: Scott K Logan

<a id="rosidl-default-runtime"></a>

## [rosidl\_default\_runtime](https://github.com/ros2/rosidl_defaults/tree/kilted/rosidl_default_runtime/CHANGELOG.rst)

- Minor update to quality declaration ([#27](https://github.com/ros2/rosidl_defaults/issues/27))
- Contributors: Christophe Bedard

<a id="rosidl-dynamic-typesupport"></a>

## [rosidl\_dynamic\_typesupport](https://github.com/ros2/rosidl_dynamic_typesupport/tree/kilted/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#15](https://github.com/ros2/rosidl_dynamic_typesupport/issues/15))
- Bump minimum CMake version to 3.20 ([#14](https://github.com/ros2/rosidl_dynamic_typesupport/issues/14))
- Drop support for long double/float128. ([#12](https://github.com/ros2/rosidl_dynamic_typesupport/issues/12))
- Contributors: Chris Lalancette, Michael Carroll, mosfet80

<a id="rosidl-dynamic-typesupport-fastrtps"></a>

## [rosidl\_dynamic\_typesupport\_fastrtps](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/tree/kilted/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#8](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/8))
- Changes to build against Fast DDS 3.0 ([#5](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/5))
- Drop support for long double/float128. ([#6](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/6))
- Contributors: Chris Lalancette, Miguel Company, Scott K Logan

<a id="rosidl-generator-c"></a>

## [rosidl\_generator\_c](https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_c/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#856](https://github.com/ros2/rosidl/issues/856))
- Deterministic iteration order for reproducible codegen ([#846](https://github.com/ros2/rosidl/issues/846))
- Add types `rosidl_pycommon` ([#824](https://github.com/ros2/rosidl/issues/824))
- Contributors: Harry Sarson, Michael Carlstrom, Michael Carroll

<a id="rosidl-generator-cpp"></a>

## [rosidl\_generator\_cpp](https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_cpp/CHANGELOG.rst)

- Add name and data\_type traits for actions ([#848](https://github.com/ros2/rosidl/issues/848))
- Add types `rosidl_pycommon` ([#824](https://github.com/ros2/rosidl/issues/824))
- Contributors: Michael Carlstrom, Nathan Wiebe Neufeldt

<a id="rosidl-generator-dds-idl"></a>

## [rosidl\_generator\_dds\_idl](https://github.com/ros2/rosidl_dds/tree/kilted/rosidl_generator_dds_idl/CHANGELOG.rst)

- Update cmake version requirements ([#64](https://github.com/ros2/rosidl_dds/issues/64))
- Contributors: mosfet80

<a id="rosidl-generator-py"></a>

## [rosidl\_generator\_py](https://github.com/ros2/rosidl_python/tree/kilted/rosidl_generator_py/CHANGELOG.rst)

- Fix `__eq__` for Array fields ([#224](https://github.com/ros2/rosidl_python/issues/224))
- Remove use of ament\_target\_dependencies ([#222](https://github.com/ros2/rosidl_python/issues/222))
- Revamp how we check for the correct class. ([#218](https://github.com/ros2/rosidl_python/issues/218))
- Remove python\_cmake\_module and set hints ([#204](https://github.com/ros2/rosidl_python/issues/204))
- Add rosidl\_generator\_py to the rosidl\_runtime\_packages group ([#212](https://github.com/ros2/rosidl_python/issues/212))
- Contributors: Chris Lalancette, Michael Carlstrom, Scott K Logan, Shane Loretz

<a id="rosidl-generator-tests"></a>

## [rosidl\_generator\_tests](https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_tests/CHANGELOG.rst)

- Add name and data\_type traits for actions ([#848](https://github.com/ros2/rosidl/issues/848))
- Silence one more gcc false-positive. ([#814](https://github.com/ros2/rosidl/issues/814))
- Switch to using fastjsonschema for schema validation. ([#809](https://github.com/ros2/rosidl/issues/809))
- Contributors: Chris Lalancette, Nathan Wiebe Neufeldt

<a id="rosidl-generator-type-description"></a>

## [rosidl\_generator\_type\_description](https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_type_description/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#856](https://github.com/ros2/rosidl/issues/856))
- Contributors: Michael Carroll

<a id="rosidl-parser"></a>

## [rosidl\_parser](https://github.com/ros2/rosidl/tree/kilted/rosidl_parser/CHANGELOG.rst)

- Finish adding types to `rosidl_parser` ([#832](https://github.com/ros2/rosidl/issues/832))
- Add types to definition.py in `rosidl_parser` ([#791](https://github.com/ros2/rosidl/issues/791))
- Contributors: Michael Carlstrom

<a id="rosidl-pycommon"></a>

## [rosidl\_pycommon](https://github.com/ros2/rosidl/tree/kilted/rosidl_pycommon/CHANGELOG.rst)

- Add test\_xmllint to rosidl\_pycommon. ([#833](https://github.com/ros2/rosidl/issues/833))
- Add types `rosidl_pycommon` ([#824](https://github.com/ros2/rosidl/issues/824))
- Support empy3 and empy4 ([#821](https://github.com/ros2/rosidl/issues/821))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael Carlstrom

<a id="rosidl-runtime-c"></a>

## [rosidl\_runtime\_c](https://github.com/ros2/rosidl/tree/kilted/rosidl_runtime_c/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#856](https://github.com/ros2/rosidl/issues/856))
- Implement `resize` function for String ([#806](https://github.com/ros2/rosidl/issues/806))
- Fix u16 docs and improve docs formatting ([#805](https://github.com/ros2/rosidl/issues/805))
- Contributors: Christophe Bedard, Michael Carroll, WATANABE Aoi

<a id="rosidl-runtime-cpp"></a>

## [rosidl\_runtime\_cpp](https://github.com/ros2/rosidl/tree/kilted/rosidl_runtime_cpp/CHANGELOG.rst)

- Suppress warnings in the benchmarks for upstream GCC false positives. ([#810](https://github.com/ros2/rosidl/issues/810))
- Contributors: Chris Lalancette

<a id="rosidl-runtime-py"></a>

## [rosidl\_runtime\_py](https://github.com/ros2/rosidl_runtime_py/tree/kilted/CHANGELOG.rst)

- Use deepcopy in set\_message\_fields for safety. ([#34](https://github.com/ros2/rosidl_runtime_py/issues/34))
- Remove CODEOWNERS and mirror-rolling-to-master. ([#31](https://github.com/ros2/rosidl_runtime_py/issues/31))
- Contributors: Chris Lalancette, Tomoya Fujita

<a id="rosidl-typesupport-c"></a>

## [rosidl\_typesupport\_c](https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_c/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#166](https://github.com/ros2/rosidl_typesupport/issues/166))
- Uniform cmake requirement ([#163](https://github.com/ros2/rosidl_typesupport/issues/163))
- Cleanup warning message in rosidl\_typesupport\_c tests. ([#161](https://github.com/ros2/rosidl_typesupport/issues/161))
- Add mechanism to disable workaround for dependency groups ([#157](https://github.com/ros2/rosidl_typesupport/issues/157))
- Add ‘mimick’ label to tests which use Mimick ([#158](https://github.com/ros2/rosidl_typesupport/issues/158))
- Contributors: Chris Lalancette, Scott K Logan, mosfet80

<a id="rosidl-typesupport-cpp"></a>

## [rosidl\_typesupport\_cpp](https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_cpp/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#166](https://github.com/ros2/rosidl_typesupport/issues/166))
- Uniform cmake requirement ([#163](https://github.com/ros2/rosidl_typesupport/issues/163))
- Add mechanism to disable workaround for dependency groups ([#157](https://github.com/ros2/rosidl_typesupport/issues/157))
- Contributors: Scott K Logan, mosfet80

<a id="rosidl-typesupport-fastrtps-c"></a>

## [rosidl\_typesupport\_fastrtps\_c](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/kilted/rosidl_typesupport_fastrtps_c/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#127](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/127))
- Remove dependency on fastrtps\_cmake\_module ([#120](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/120))
- Remove CODEOWNERS and mirror-rolling-to-master workflow ([#124](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/124))
- Remove deprecated functions benchmark tests ([#122](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/122))
- Contributors: Chris Lalancette, Miguel Company, Scott K Logan

<a id="rosidl-typesupport-fastrtps-cpp"></a>

## [rosidl\_typesupport\_fastrtps\_cpp](https://github.com/ros2/rosidl_typesupport_fastrtps/tree/kilted/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#127](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/127))
- Remove dependency on fastrtps\_cmake\_module ([#120](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/120))
- Remove CODEOWNERS and mirror-rolling-to-master workflow ([#124](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/124))
- Remove deprecated functions benchmark tests ([#122](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/122))
- Contributors: Chris Lalancette, Miguel Company, Scott K Logan

<a id="rosidl-typesupport-introspection-c"></a>

## [rosidl\_typesupport\_introspection\_c](https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_c/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#860](https://github.com/ros2/rosidl/issues/860))
- Add types `rosidl_pycommon` ([#824](https://github.com/ros2/rosidl/issues/824))
- Contributors: Michael Carlstrom, Scott K Logan

<a id="rosidl-typesupport-introspection-cpp"></a>

## [rosidl\_typesupport\_introspection\_cpp](https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_cpp/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#860](https://github.com/ros2/rosidl/issues/860))
- Add types `rosidl_pycommon` ([#824](https://github.com/ros2/rosidl/issues/824))
- Contributors: Michael Carlstrom, Scott K Logan

<a id="rosidl-typesupport-introspection-tests"></a>

## [rosidl\_typesupport\_introspection\_tests](https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_tests/CHANGELOG.rst)

- Suppress false positive warnings from gcc. ([#811](https://github.com/ros2/rosidl/issues/811))
- Contributors: Chris Lalancette

<a id="rosidl-typesupport-tests"></a>

## [rosidl\_typesupport\_tests](https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_tests/CHANGELOG.rst)

- Uniform cmake requirement ([#163](https://github.com/ros2/rosidl_typesupport/issues/163))
- Contributors: mosfet80

<a id="rpyutils"></a>

## [rpyutils](https://github.com/ros2/rpyutils/tree/kilted/CHANGELOG.rst)

- Add py.typed to Package Data ([#16](https://github.com/ros2/rpyutils/issues/16))
- Add Create py.typed ([#15](https://github.com/ros2/rpyutils/issues/15))
- Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#13](https://github.com/ros2/rpyutils/issues/13))
- Add types and ament\_mypy to rpyutils. ([#12](https://github.com/ros2/rpyutils/issues/12))
- Contributors: Chris Lalancette, Michael Carlstrom

<a id="rqt-bag"></a>

## [rqt\_bag](https://github.com/ros-visualization/rqt_bag/tree/kilted/rqt_bag/CHANGELOG.rst)

- Add standard tests for rqt\_bag and rqt\_bag\_plugins ([#171](https://github.com/ros-visualization/rqt_bag/issues/171))
- Updated player QoS ([#164](https://github.com/ros-visualization/rqt_bag/issues/164))
- Adapted to rosbag2\_py ([#156](https://github.com/ros-visualization/rqt_bag/issues/156))
- Fixed button icons ([#159](https://github.com/ros-visualization/rqt_bag/issues/159))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-bag-plugins"></a>

## [rqt\_bag\_plugins](https://github.com/ros-visualization/rqt_bag/tree/kilted/rqt_bag_plugins/CHANGELOG.rst)

- Add standard tests for rqt\_bag and rqt\_bag\_plugins ([#171](https://github.com/ros-visualization/rqt_bag/issues/171))
- Adapted to rosbag2\_py ([#156](https://github.com/ros-visualization/rqt_bag/issues/156))
- Fixed image timeline renderer ([#158](https://github.com/ros-visualization/rqt_bag/issues/158))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-console"></a>

## [rqt\_console](https://github.com/ros-visualization/rqt_console/tree/kilted/CHANGELOG.rst)

- Add in standard tests. ([#48](https://github.com/ros-visualization/rqt_console/issues/48))
- Remove CODEOWNERS and mirror-rolling-to-main workflow ([#46](https://github.com/ros-visualization/rqt_console/issues/46))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-graph"></a>

## [rqt\_graph](https://github.com/ros-visualization/rqt_graph/tree/kilted/CHANGELOG.rst)

- Add in standard tests. ([#104](https://github.com/ros-visualization/rqt_graph/issues/104))
- Remove CODEOWNERS ([#102](https://github.com/ros-visualization/rqt_graph/issues/102))
- Fixed fit\_in\_view icon button ([#95](https://github.com/ros-visualization/rqt_graph/issues/95))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-gui"></a>

## [rqt\_gui](https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui/CHANGELOG.rst)

- Add in standard tests for rqt\_gui and rqt\_gui\_py ([#318](https://github.com/ros-visualization/rqt/issues/318))
- Contributors: Chris Lalancette

<a id="rqt-gui-cpp"></a>

## [rqt\_gui\_cpp](https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui_cpp/CHANGELOG.rst)

- Added common test to rqt\_gui\_cpp and deprecate h headers ([#311](https://github.com/ros-visualization/rqt/issues/311))
- Updated deprecated qt\_gui\_cpp headers ([#309](https://github.com/ros-visualization/rqt/issues/309))
- Contributors: Alejandro Hernández Cordero

<a id="rqt-gui-py"></a>

## [rqt\_gui\_py](https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui_py/CHANGELOG.rst)

- Add in standard tests for rqt\_gui and rqt\_gui\_py ([#318](https://github.com/ros-visualization/rqt/issues/318))
- Contributors: Chris Lalancette

<a id="rqt-plot"></a>

## [rqt\_plot](https://github.com/ros-visualization/rqt_plot/tree/kilted/CHANGELOG.rst)

- Add unit tests for topic name validation & field expansion ([#108](https://github.com/ros-visualization/rqt_plot/issues/108))
- Fix double slash when plotting all sub-fields with trailing slash ([#107](https://github.com/ros-visualization/rqt_plot/issues/107))
- Fix listing of nested basic type fields ([#101](https://github.com/ros-visualization/rqt_plot/issues/101))
- Fix f-string and add single quote around field name ([#100](https://github.com/ros-visualization/rqt_plot/issues/100))
- Add single quotes around topic in validation msg for consistency ([#99](https://github.com/ros-visualization/rqt_plot/issues/99)) This is more consistent with the other messages below.
- Add in the rest of the standard ament\_python tests. ([#98](https://github.com/ros-visualization/rqt_plot/issues/98))
- Remove CODEOWNERS ([#96](https://github.com/ros-visualization/rqt_plot/issues/96))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard

<a id="rqt-publisher"></a>

## [rqt\_publisher](https://github.com/ros-visualization/rqt_publisher/tree/kilted/CHANGELOG.rst)

- Add in the remaining standard ament\_python tests. ([#49](https://github.com/ros-visualization/rqt_publisher/issues/49))
- Add in LICENSE. ([#46](https://github.com/ros-visualization/rqt_publisher/issues/46))
- Remove CODEOWNERS ([#47](https://github.com/ros-visualization/rqt_publisher/issues/47))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-py-common"></a>

## [rqt\_py\_common](https://github.com/ros-visualization/rqt/tree/kilted/rqt_py_common/CHANGELOG.rst)

- Stop using python\_cmake\_module. ([#304](https://github.com/ros-visualization/rqt/issues/304))
- Use an rclpy context manager. ([#312](https://github.com/ros-visualization/rqt/issues/312))
- Added common test to rqt\_py\_common ([#310](https://github.com/ros-visualization/rqt/issues/310))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-py-console"></a>

## [rqt\_py\_console](https://github.com/ros-visualization/rqt_py_console/tree/kilted/CHANGELOG.rst)

- Add the standard tests to rqt\_py\_console. ([#19](https://github.com/ros-visualization/rqt_py_console/issues/19))
- Remove CODEOWNERS ([#17](https://github.com/ros-visualization/rqt_py_console/issues/17))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-service-caller"></a>

## [rqt\_service\_caller](https://github.com/ros-visualization/rqt_service_caller/tree/kilted/CHANGELOG.rst)

- Update rqt\_service\_caller to our standard policies. ([#31](https://github.com/ros-visualization/rqt_service_caller/issues/31))
- Remove CODEOWNERS ([#29](https://github.com/ros-visualization/rqt_service_caller/issues/29))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-shell"></a>

## [rqt\_shell](https://github.com/ros-visualization/rqt_shell/tree/kilted/CHANGELOG.rst)

- Add in standard tests to rqt\_shell. ([#24](https://github.com/ros-visualization/rqt_shell/issues/24)) That way we know it conforms to our standards.
- Remove CODEOWNERS ([#22](https://github.com/ros-visualization/rqt_shell/issues/22))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette

<a id="rqt-topic"></a>

## [rqt\_topic](https://github.com/ros-visualization/rqt_topic/tree/kilted/CHANGELOG.rst)

- Override subscriber qos ([#51](https://github.com/ros-visualization/rqt_topic//issues/51))
- Remove CODEOWNERS ([#52](https://github.com/ros-visualization/rqt_topic//issues/52))
- Contributors: Alejandro Hernández Cordero

<a id="rti-connext-dds-cmake-module"></a>

## [rti\_connext\_dds\_cmake\_module](https://github.com/ros2/rmw_connextdds/tree/kilted/rti_connext_dds_cmake_module/CHANGELOG.rst)

- Update Connext to 7.3.0 ([#181](https://github.com/ros2/rmw_connextdds/issues/181))
- Quiet a warning when CONNEXTDDS\_DIR or NDDSHOME is not found. ([#158](https://github.com/ros2/rmw_connextdds/issues/158))
- Contributors: Chris Lalancette, lobolanja

<a id="rttest"></a>

## [rttest](https://github.com/ros2/realtime_support/tree/kilted/rttest/CHANGELOG.rst)

- Don’t try to build on BSD ([#126](https://github.com/ros2/realtime_support/issues/126))
- Contributors: Scott K Logan

<a id="rviz2"></a>

## [rviz2](https://github.com/ros2/rviz/tree/kilted/rviz2/CHANGELOG.rst)

- Expose the possibility to create ROS node with custom `NodeOptions` ([#1347](https://github.com/ros2/rviz/issues/1347))
- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Detect wayland and make sure X rendering is used. ([#1253](https://github.com/ros2/rviz/issues/1253))
- Fixed RViz2 linters ([#1231](https://github.com/ros2/rviz/issues/1231))
- Contributors: Alejandro Hernández Cordero, Matthew Elwin, Patrick Roncagliolo, mosfet80

<a id="rviz-assimp-vendor"></a>

## [rviz\_assimp\_vendor](https://github.com/ros2/rviz/tree/kilted/rviz_assimp_vendor/CHANGELOG.rst)

- Revert “Update ASSIMP\_VENDOR CMakeLists.txt ([#1226](https://github.com/ros2/rviz/issues/1226))” ([#1249](https://github.com/ros2/rviz/issues/1249))
- Update ASSIMP\_VENDOR CMakeLists.txt ([#1226](https://github.com/ros2/rviz/issues/1226)) CLEAN UNUSED CHECK SE MIN ASSIMP VERSION TO 5.3.1 SET C++ VERSION TO 17
- Contributors: Chris Lalancette, mosfet80

<a id="rviz-common"></a>

## [rviz\_common](https://github.com/ros2/rviz/tree/kilted/rviz_common/CHANGELOG.rst)

- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- addTrackedObject Function Fails to Handle Null Pointer, Causing Crash When nullptr is Passed ([#1375](https://github.com/ros2/rviz/issues/1375))
- Add test to check mapGetString when key is missing ([#1361](https://github.com/ros2/rviz/issues/1361))
- UniformStringStream::parseFloat Fails to Handle Invalid Float Formats Correctly ([#1360](https://github.com/ros2/rviz/issues/1360))
- Fix Potential Null Pointer Dereference in VisualizerApp::getRenderWindow() to Prevent Crashes ([#1359](https://github.com/ros2/rviz/issues/1359))
- Extend support for type adaptation (REP 2007) in rviz\_common for TF-filtered displays ([#1346](https://github.com/ros2/rviz/issues/1346))
- Expose the possibility to create ROS node with custom `NodeOptions` ([#1347](https://github.com/ros2/rviz/issues/1347))
- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Add basic support for type adaptation (REP 2007) in `rviz_common` for displays ([#1331](https://github.com/ros2/rviz/issues/1331))
- Fix preferred tools loading names ([#1321](https://github.com/ros2/rviz/issues/1321))
- Add RVIZ\_COMMON\_PUBLIC macro to ToolManager ([#1323](https://github.com/ros2/rviz/issues/1323))
- Clean visualization\_manager.cpp ([#1317](https://github.com/ros2/rviz/issues/1317))
- Fix Deprecated tf2 headers ([#1289](https://github.com/ros2/rviz/issues/1289))
- include QString ([#1298](https://github.com/ros2/rviz/issues/1298))
- Handle time source exception ([#1285](https://github.com/ros2/rviz/issues/1285))
- Fully handle `Tool::processKeyEvent` return value ([#1270](https://github.com/ros2/rviz/issues/1270))
- Handle `Tool::Finished` returned by `processKeyEvent` ([#1257](https://github.com/ros2/rviz/issues/1257))
- Added more time to copyright on Windwos ([#1252](https://github.com/ros2/rviz/issues/1252))
- Added common test for rviz\_common ([#1232](https://github.com/ros2/rviz/issues/1232))
- Set ContentsMargins for RenderPanel to 0 to avoid borders in fullscreen mode. Fixes [#1024](https://github.com/ros2/rviz/issues/1024) ([#1228](https://github.com/ros2/rviz/issues/1228))
- Updated deprecated message filter headers ([#1239](https://github.com/ros2/rviz/issues/1239))
- Correclty load icons of panels with whitespaces in their name ([#1241](https://github.com/ros2/rviz/issues/1241))
- Prepping for qos deprecation ([#1214](https://github.com/ros2/rviz/issues/1214))
- Replace ESC shortcut for exiting full screen with solution from <https://github.com/ros-visualization/rviz/pull/1416> ([#1205](https://github.com/ros2/rviz/issues/1205))
- Contributors: Alejandro Hernández Cordero, Bo Chen, Lucas Wendland, Matthew Foran, Michael Carroll, Michael Ripperger, Patrick Roncagliolo, RaduPopescu, Silvio Traversaro, mosfet80

<a id="rviz-default-plugins"></a>

## [rviz\_default\_plugins](https://github.com/ros2/rviz/tree/kilted/rviz_default_plugins/CHANGELOG.rst)

- PointCloudDisplay: Fix decay time 0 keeping more than the last message ([#1400](https://github.com/ros2/rviz/issues/1400))
- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- Include chrono ([#1353](https://github.com/ros2/rviz/issues/1353))
- fix: add rclcpp::shutdown ([#1343](https://github.com/ros2/rviz/issues/1343))
- Nv12 color format ([#1318](https://github.com/ros2/rviz/issues/1318)) Co-authored-by: zycczy <[zycczyby@gmail.com](mailto:zycczyby%40gmail.com)>
- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Initialize lookup table only once at compile time ([#1330](https://github.com/ros2/rviz/issues/1330)) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Fixed the XY Orbit controller move ([#1327](https://github.com/ros2/rviz/issues/1327)) Co-authored-by: Terry Scott <[tscott@seegrid.com](mailto:tscott%40seegrid.com)>
- Fix Deprecated tf2 headers ([#1289](https://github.com/ros2/rviz/issues/1289))
- Change EffortDisplay superclass from MessageFilterDisplay to RosTopicDisplay to avoid dropping messages with empty frame\_id. ([#1312](https://github.com/ros2/rviz/issues/1312))
- Fix access control for Accel, Effort and Twist displays ([#1311](https://github.com/ros2/rviz/issues/1311))
- remove unused variable ([#1301](https://github.com/ros2/rviz/issues/1301))
- include QString ([#1298](https://github.com/ros2/rviz/issues/1298))
- Clean code for Image display ([#1271](https://github.com/ros2/rviz/issues/1271))
- Handle time source exception ([#1285](https://github.com/ros2/rviz/issues/1285))
- replace deprecated encodings ‘yuv422’ and ‘yuv422\_yuy2’ ([#1276](https://github.com/ros2/rviz/issues/1276))
- Update urdf model.h deprecation ([#1266](https://github.com/ros2/rviz/issues/1266))
- Enabling manual space width for TextViewFacingMarker ([#1261](https://github.com/ros2/rviz/issues/1261))
- Added more time to copyright on Windwos ([#1252](https://github.com/ros2/rviz/issues/1252))
- Updated deprecated message filter headers ([#1239](https://github.com/ros2/rviz/issues/1239))
- Fixed RViz default plugin license linter ([#1230](https://github.com/ros2/rviz/issues/1230))
- Contributors: Alejandro Hernández Cordero, Christian Rauch, Lucas Wendland, Matthew Foran, Michael Carroll, Patrick Roncagliolo, Peng Wang, Stefan Fabian, Terry Scott, Tom Moore, Yuyuan Yuan, disRecord, mosfet80, quic-zhaoyuan, suchetanrs

<a id="rviz-ogre-vendor"></a>

## [rviz\_ogre\_vendor](https://github.com/ros2/rviz/tree/kilted/rviz_ogre_vendor/CHANGELOG.rst)

- Add missing glew dependency for ogre vendor package ([#1350](https://github.com/ros2/rviz/issues/1350))
- Use official freetype github mirror instead of savannah ([#1348](https://github.com/ros2/rviz/issues/1348))
- Fix flags for both clang and gcc. ([#1219](https://github.com/ros2/rviz/issues/1219))
- Update freetype lib ([#1216](https://github.com/ros2/rviz/issues/1216))
- Update zlib into CMakeLists.txt ([#1128](https://github.com/ros2/rviz/issues/1128)) Changes in 1.3 (18 Aug 2023) - Remove K&R function definitions and zlib2ansi - Fix bug in deflateBound() for level 0 and memLevel 9 - Fix bug when gzungetc() is used immediately after gzopen() - Fix bug when using gzflush() with a very small buffer - Fix crash when gzsetparams() attempted for transparent write - Fix test/example.c to work with FORCE\_STORED - Rewrite of zran in examples (see zran.c version history) - Fix minizip to allow it to open an empty zip file - Fix reading disk number start on zip64 files in minizip - Fix logic error in minizip argument processing - Add minizip testing to Makefile - Read multiple bytes instead of byte-by-byte in minizip unzip.c - Add memory sanitizer to configure (–memory) - Various portability improvements - Various documentation improvements - Various spelling and typo corrections Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Contributors: Chris Lalancette, Silvio Traversaro, Stefan Fabian, mosfet80

<a id="rviz-rendering"></a>

## [rviz\_rendering](https://github.com/ros2/rviz/tree/kilted/rviz_rendering/CHANGELOG.rst)

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
- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Clean ogre\_render\_window\_impl.cpp ([#1334](https://github.com/ros2/rviz/issues/1334))
- include QString ([#1298](https://github.com/ros2/rviz/issues/1298))
- Use consistent conditionals in render\_system.hpp ([#1294](https://github.com/ros2/rviz/issues/1294))
- Avoid redefinition of default color materials ([#1281](https://github.com/ros2/rviz/issues/1281))
- Added more time to copyright on Windwos ([#1252](https://github.com/ros2/rviz/issues/1252))
- Fix: issue [#1220](https://github.com/ros2/rviz/issues/1220). ([#1237](https://github.com/ros2/rviz/issues/1237)) Co-authored-by: Alejandro Hernández Cordero <[ahcorde@gmail.com](mailto:ahcorde%40gmail.com)>
- Added common test: rviz\_rendering ([#1233](https://github.com/ros2/rviz/issues/1233))
- Contributors: Alejandro Hernández Cordero, Masayoshi Dohi, Matthew Foran, Michael Carroll, Scott K Logan, chama1176, mosfet80

<a id="rviz-rendering-tests"></a>

## [rviz\_rendering\_tests](https://github.com/ros2/rviz/tree/kilted/rviz_rendering_tests/CHANGELOG.rst)

- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Added common test to rviz\_rendering\_tests ([#1234](https://github.com/ros2/rviz/issues/1234))
- Contributors: Alejandro Hernández Cordero, Michael Carroll, mosfet80

<a id="rviz-resource-interfaces"></a>

## [rviz\_resource\_interfaces](https://github.com/ros2/rviz/tree/kilted/rviz_resource_interfaces/CHANGELOG.rst)

- Work in progress using the new resource retriever apis ([#1262](https://github.com/ros2/rviz/issues/1262))
- Contributors: Michael Carroll

<a id="rviz-visual-testing-framework"></a>

## [rviz\_visual\_testing\_framework](https://github.com/ros2/rviz/tree/kilted/rviz_visual_testing_framework/CHANGELOG.rst)

- uniform CMAKE requirement ([#1335](https://github.com/ros2/rviz/issues/1335))
- Fix Deprecated tf2 headers ([#1289](https://github.com/ros2/rviz/issues/1289))
- include QString ([#1298](https://github.com/ros2/rviz/issues/1298))
- Added common test to rviz\_visual\_testing\_framework ([#1235](https://github.com/ros2/rviz/issues/1235))
- Contributors: Alejandro Hernández Cordero, Lucas Wendland, Matthew Foran, mosfet80

<a id="sensor-msgs"></a>

## [sensor\_msgs](https://github.com/ros2/common_interfaces/tree/kilted/sensor_msgs/CHANGELOG.rst)

- Add NV12 to color formats ([#253](https://github.com/ros2/common_interfaces/issues/253))
- Contributors: Lukas Schäper

<a id="sensor-msgs-py"></a>

## [sensor\_msgs\_py](https://github.com/ros2/common_interfaces/tree/kilted/sensor_msgs_py/CHANGELOG.rst)

- Add ament\_xmllint to sensor\_msgs\_py. ([#259](https://github.com/ros2/common_interfaces/issues/259))
- Fix formatting in sensor\_msgs\_py ([#248](https://github.com/ros2/common_interfaces/issues/248))
- Contributors: Chris Lalancette, Christophe Bedard

<a id="service-msgs"></a>

## [service\_msgs](https://github.com/ros2/rcl_interfaces/tree/kilted/service_msgs/CHANGELOG.rst)

- Add missing build\_export\_depend on rosidl\_core\_runtime ([#165](https://github.com/ros2/rcl_interfaces/issues/165))
- Contributors: Scott K Logan

<a id="sqlite3-vendor"></a>

## [sqlite3\_vendor](https://github.com/ros2/rosbag2/tree/kilted/sqlite3_vendor/CHANGELOG.rst)

- Bump sqlite3 to 3.45.1 ([#1737](https://github.com/ros2/rosbag2/issues/1737))
- Contributors: Christophe Bedard

<a id="sros2"></a>

## [sros2](https://github.com/ros2/sros2/tree/kilted/sros2/CHANGELOG.rst)

- Switch to get\_rmw\_additional\_env ([#339](https://github.com/ros2/sros2/issues/339))
- Fix github-workflow mypy error ([#336](https://github.com/ros2/sros2/issues/336))
- Give more time to generate policies in tests ([#323](https://github.com/ros2/sros2/issues/323))
- Switch to context manager for rclpy tests. ([#322](https://github.com/ros2/sros2/issues/322))
- [FIX] remove dangerous mutable default arguments in generate\_artifacts ([#318](https://github.com/ros2/sros2/issues/318))
- Fix sros2 tests on Windows Debug. ([#317](https://github.com/ros2/sros2/issues/317))
- [TESTS] Update tests and add test for generate\_artifacts ([#311](https://github.com/ros2/sros2/issues/311))
- remove deprecated create\_key and list\_keys verbs ([#302](https://github.com/ros2/sros2/issues/302))
- Fix linux tutorial: cloning example policies and set of default policies for a node ([#295](https://github.com/ros2/sros2/issues/295))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael Arguedas, Tomoya Fujita, yadunund

<a id="test-cli"></a>

## [test\_cli](https://github.com/ros2/system_tests/tree/kilted/test_cli/CHANGELOG.rst)

- Stop using python\_cmake\_module. ([#536](https://github.com/ros2/system_tests/issues/536))
- Use rclpy.init context manager where we can. ([#547](https://github.com/ros2/system_tests/issues/547)) This allows us to cleanup, while using a lot less code to try and track it.
- Contributors: Chris Lalancette

<a id="test-cli-remapping"></a>

## [test\_cli\_remapping](https://github.com/ros2/system_tests/tree/kilted/test_cli_remapping/CHANGELOG.rst)

- Stop using python\_cmake\_module. ([#536](https://github.com/ros2/system_tests/issues/536))
- Use rclpy.init context manager where we can. ([#547](https://github.com/ros2/system_tests/issues/547)) This allows us to cleanup, while using a lot less code to try and track it.
- Contributors: Chris Lalancette

<a id="test-communication"></a>

## [test\_communication](https://github.com/ros2/system_tests/tree/kilted/test_communication/CHANGELOG.rst)

- Use EnableRmwIsolation in launch tests ([#571](https://github.com/ros2/system_tests/issues/571))
- Switch to isolated test fixture macros ([#571](https://github.com/ros2/system_tests/issues/571))
- Add tests for Keyed types ([#568](https://github.com/ros2/system_tests/issues/568))
- Remove use of ament\_target\_dependencies ([#566](https://github.com/ros2/system_tests/issues/566))
- Skip all multi-vendor pub/sub tests with zenoh ([#560](https://github.com/ros2/system_tests/issues/560))
- Stop using python\_cmake\_module. ([#536](https://github.com/ros2/system_tests/issues/536))
- Use rclpy.init context manager where we can. ([#547](https://github.com/ros2/system_tests/issues/547)) This allows us to cleanup, while using a lot less code to try and track it.
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Francisco Gallego Salido, Scott K Logan, Shane Loretz, yadunund

<a id="test-interface-files"></a>

## [test\_interface\_files](https://github.com/ros2/test_interface_files/tree/kilted/CHANGELOG.rst)

- Drop long double from the IDL. ([#22](https://github.com/ros2/test_interface_files/issues/22))
- Contributors: Chris Lalancette

<a id="test-launch-ros"></a>

## [test\_launch\_ros](https://github.com/ros2/launch_ros/tree/kilted/test_launch_ros/CHANGELOG.rst)

- Add python3-pytest-timeout to test\_launch\_ros. ([#454](https://github.com/ros2/launch_ros/issues/454))
- Autostarting lifecycle nodes and example launch file demo ([#430](https://github.com/ros2/launch_ros/issues/430))
- Add ament\_xmllint to the ament\_python packages. ([#423](https://github.com/ros2/launch_ros/issues/423))
- Add in a timeout for test\_launch\_ros. ([#417](https://github.com/ros2/launch_ros/issues/417))
- Fix url in setup.py ([#413](https://github.com/ros2/launch_ros/issues/413))
- Revamp the test\_load\_composable\_nodes test. ([#403](https://github.com/ros2/launch_ros/issues/403))
- Switch to use rclpy.init context manager. ([#402](https://github.com/ros2/launch_ros/issues/402))
- Contributors: Chris Lalancette, Steve Macenski, Tomoya Fujita, Wei HU

<a id="test-msgs"></a>

## [test\_msgs](https://github.com/ros2/rcl_interfaces/tree/kilted/test_msgs/CHANGELOG.rst)

- Added test messages with keys ([#173](https://github.com/ros2/rcl_interfaces/issues/173))
- Contributors: Francisco Gallego Salido

<a id="test-osrf-testing-tools-cpp"></a>

## [test\_osrf\_testing\_tools\_cpp](https://github.com/osrf/osrf_testing_tools_cpp/tree/kilted/test_osrf_testing_tools_cpp/CHANGELOG.rst)

- Update CMakeLists.txt ([#85](https://github.com/osrf/osrf_testing_tools_cpp/issues/85))
- Contributors: mosfet80

<a id="test-quality-of-service"></a>

## [test\_quality\_of\_service](https://github.com/ros2/system_tests/tree/kilted/test_quality_of_service/CHANGELOG.rst)

- Switch to isolated test fixture macros ([#571](https://github.com/ros2/system_tests/issues/571))
- Use rmw\_event\_type\_is\_supported to skip tests ([#563](https://github.com/ros2/system_tests/issues/563))
- Fixed some qos test related with Zenoh ([#551](https://github.com/ros2/system_tests/issues/551))
- Contributors: Alejandro Hernández Cordero, Scott K Logan

<a id="test-rclcpp"></a>

## [test\_rclcpp](https://github.com/ros2/system_tests/tree/kilted/test_rclcpp/CHANGELOG.rst)

- Use EnableRmwIsolation in launch tests ([#571](https://github.com/ros2/system_tests/issues/571))
- Ensure test verifies the existence of all spawning nodes ([#558](https://github.com/ros2/system_tests/issues/558))
- chore: Adopted to API changes in rclcpp ([#556](https://github.com/ros2/system_tests/issues/556))
- Implement the pure-virtual functions in the Waitable class. ([#548](https://github.com/ros2/system_tests/issues/548))
- Update deprecated methods ([#546](https://github.com/ros2/system_tests/issues/546))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch Machowinski, Scott K Logan, Yuyuan Yuan

<a id="test-rmw-implementation"></a>

## [test\_rmw\_implementation](https://github.com/ros2/rmw_implementation/tree/kilted/test_rmw_implementation/CHANGELOG.rst)

- Added rmw\_event\_type\_is\_supported ([#250](https://github.com/ros2/rmw_implementation/issues/250)) \* Added rmw\_event\_check\_compatible \* fix return typoe \* updated name and use in wait\_set test ———
- Update expectations of tests to remain compatible with non-DDS middlewares ([#248](https://github.com/ros2/rmw_implementation/issues/248))
- use rmw\_enclave\_options\_xxx APIs instead. ([#247](https://github.com/ros2/rmw_implementation/issues/247))
- Fix up some overwritten errors. ([#246](https://github.com/ros2/rmw_implementation/issues/246)) That is, make sure to clear out errors where we should. We also slightly rewrite some of the testing around unsupported APIs, so that they make more sense.
- Do not deref msg ptr for rmw\_{publish,return}\_loaned\_message\*() ([#240](https://github.com/ros2/rmw_implementation/issues/240))
- remove rmw\_localhost\_only\_t. ([#239](https://github.com/ros2/rmw_implementation/issues/239))
- Expect rmw\_service\_server\_is\_available to ret RMW\_RET\_INVALID\_ARGUMENT ([#231](https://github.com/ros2/rmw_implementation/issues/231))
- Expect rmw\_destroy\_wait\_set to ret RMW\_RET\_INVALID\_ARGUMENT ([#234](https://github.com/ros2/rmw_implementation/issues/234))
- Add test creating two content filter topics with the same topic name ([#230](https://github.com/ros2/rmw_implementation/issues/230)) ([#233](https://github.com/ros2/rmw_implementation/issues/233))
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Tomoya Fujita, yadunund

<a id="test-ros2trace"></a>

## [test\_ros2trace](https://github.com/ros2/ros2_tracing/tree/kilted/test_ros2trace/CHANGELOG.rst)

- Add timeout to test\_ros2trace tests that wait on stdout ([#167](https://github.com/ros2/ros2_tracing/issues/167))
- Allow enabling syscalls through `ros2 trace` or the Trace action ([#137](https://github.com/ros2/ros2_tracing/issues/137))
- Contributors: Christophe Bedard

<a id="test-tf2"></a>

## [test\_tf2](https://github.com/ros2/geometry2/tree/kilted/test_tf2/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Add `rclcpp::shutdown` ([#762](https://github.com/ros2/geometry2/issues/762))
- Remove many extra conversions from Matrix3x3 to Quaternion ([#741](https://github.com/ros2/geometry2/issues/741)) Co-authored-by: jmachowinski <[jmachowinski@users.noreply.github.com](mailto:jmachowinski%40users.noreply.github.com)> Co-authored-by: Katherine Scott <[katherineAScott@gmail.com](mailto:katherineAScott%40gmail.com)>
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Switch to using a context manager for the python examples. ([#700](https://github.com/ros2/geometry2/issues/700)) That way we can be sure to always clean up, but use less code doing so.
- Contributors: Chris Lalancette, Lucas Wendland, Yuyuan Yuan, kyle-basis, mosfet80

<a id="test-tracetools"></a>

## [test\_tracetools](https://github.com/ros2/ros2_tracing/tree/kilted/test_tracetools/CHANGELOG.rst)

- Run test\_tracetools tests against rmw\_zenoh\_cpp ([#140](https://github.com/ros2/ros2_tracing/issues/140))
- Use ament\_add\_ros\_isolated\_\* in test\_tracetools ([#159](https://github.com/ros2/ros2_tracing/issues/159))
- Instrument client/service for end-to-end request/response tracking ([#145](https://github.com/ros2/ros2_tracing/issues/145))
- Don’t try to build on BSD ([#142](https://github.com/ros2/ros2_tracing/issues/142)) The ‘BSD’ variable was added in CMake 3.25. Note that variables which are not defined will evaluate to ‘False’, so this shouldn’t regress platforms using CMake versions older than 3.25.
- Refactor and split test\_service into test\_{service,client} ([#144](https://github.com/ros2/ros2_tracing/issues/144))
- Change expected rmw GID array size to 16 bytes ([#138](https://github.com/ros2/ros2_tracing/issues/138))
- Run test\_tracetools tests against rmw\_fastrtps\_dynamic\_cpp too ([#127](https://github.com/ros2/ros2_tracing/issues/127))
- Make test\_tracetools ping pubs/subs transient\_local ([#125](https://github.com/ros2/ros2_tracing/issues/125))
- Run relevant test\_tracetools tests with all instrumented rmw impls ([#116](https://github.com/ros2/ros2_tracing/issues/116))
- Contributors: Christophe Bedard, Scott K Logan

<a id="test-tracetools-launch"></a>

## [test\_tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/kilted/test_tracetools_launch/CHANGELOG.rst)

- Fix or ignore new mypy issues ([#161](https://github.com/ros2/ros2_tracing/issues/161))
- Allow enabling syscalls through `ros2 trace` or the Trace action ([#137](https://github.com/ros2/ros2_tracing/issues/137))
- Contributors: Christophe Bedard

<a id="tf2"></a>

## [tf2](https://github.com/ros2/geometry2/tree/kilted/tf2/CHANGELOG.rst)

- Add isnan support ([#780](https://github.com/ros2/geometry2/issues/780))
- Overflow Issue in durationFromSec() Function when Handling Extremely Large or Small Values ([#785](https://github.com/ros2/geometry2/issues/785))
- Do not clobber callback handles when cancelling pending transformable requests ([#779](https://github.com/ros2/geometry2/issues/779))
- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Remove many extra conversions from Matrix3x3 to Quaternion ([#741](https://github.com/ros2/geometry2/issues/741)) Co-authored-by: jmachowinski <[jmachowinski@users.noreply.github.com](mailto:jmachowinski%40users.noreply.github.com)> Co-authored-by: Katherine Scott <[katherineAScott@gmail.com](mailto:katherineAScott%40gmail.com)>
- Cleanup deprecation warnings. ([#744](https://github.com/ros2/geometry2/issues/744)) The deprecation warnings were not printing out properly on GCC, at least; it would warn that #warning was not standard, and it would also not print out the actual warning. Also “deprecated” was spelled wrong. Fix all of these issues here.
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Removed unused var in tf2 ([#735](https://github.com/ros2/geometry2/issues/735))
- Error String Filled ([#715](https://github.com/ros2/geometry2//issues/715))
- Removed deprecated enuns ([#699](https://github.com/ros2/geometry2//issues/699))
- [TimeCache] Improve performance for insertData() and pruneList() ([#680](https://github.com/ros2/geometry2/issues/680)) Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Removed warning ([#682](https://github.com/ros2/geometry2/issues/682))
- Add cache\_benchmark ([#679](https://github.com/ros2/geometry2/issues/679)) \* Add cache\_benchmark Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- [cache\_unittest] Add direct implementation testing on ordering, pruning ([#678](https://github.com/ros2/geometry2/issues/678)) \* [cache\_unittest] Add direct implementation testing on ordering, pruning \* do getAllItems() approach \* Return a reference instead. \* mark getAllItems as internal \* Fix warning on Windows. Co-authored-by: Chris Lalancette <[clalancette@gmail.com](mailto:clalancette%40gmail.com)>
- Contributors: Alejandro Hernández Cordero, Chris Lalancette, Eric Cousineau, Lucas Wendland, Michael Carlstrom, Timo Röhling, cramke, kyle-basis, mosfet80

<a id="tf2-bullet"></a>

## [tf2\_bullet](https://github.com/ros2/geometry2/tree/kilted/tf2_bullet/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Contributors: Lucas Wendland, mosfet80

<a id="tf2-eigen"></a>

## [tf2\_eigen](https://github.com/ros2/geometry2/tree/kilted/tf2_eigen/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Contributors: Lucas Wendland, mosfet80

<a id="tf2-eigen-kdl"></a>

## [tf2\_eigen\_kdl](https://github.com/ros2/geometry2/tree/kilted/tf2_eigen_kdl/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Contributors: Lucas Wendland, mosfet80

<a id="tf2-geometry-msgs"></a>

## [tf2\_geometry\_msgs](https://github.com/ros2/geometry2/tree/kilted/tf2_geometry_msgs/CHANGELOG.rst)

- Remove many extra conversions from Matrix3x3 to Quaternion ([#741](https://github.com/ros2/geometry2/issues/741)) Co-authored-by: jmachowinski <[jmachowinski@users.noreply.github.com](mailto:jmachowinski%40users.noreply.github.com)> Co-authored-by: Katherine Scott <[katherineAScott@gmail.com](mailto:katherineAScott%40gmail.com)>
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Add a python3-dev dependency to tf2\_py. ([#733](https://github.com/ros2/geometry2/issues/733))
- Fix tf2\_geometry\_msgs\_INCLUDE\_DIRS. ([#729](https://github.com/ros2/geometry2/issues/729))
- Remove use of python\_cmake\_module ([#651](https://github.com/ros2/geometry2//issues/651))
- Contributors: Chris Lalancette, Lucas Wendland, kyle-basis, rkeating-planted

<a id="tf2-kdl"></a>

## [tf2\_kdl](https://github.com/ros2/geometry2/tree/kilted/tf2_kdl/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- tf2\_kdl: add python\_orocos\_kdl\_vendor dependency ([#745](https://github.com/ros2/geometry2/issues/745)) \* tf2\_kdl: add python\_orocos\_kdl\_vendor dependency The tf2\_kdl Python API depends on PyKDL, which is provided by python\_orocos\_kdl\_vendor. \* tf2\_kdl: remove tf2\_msgs test dependency This dependency is not needed.
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Contributors: Ben Wolsieffer, Emmanuel, Lucas Wendland, mosfet80

<a id="tf2-msgs"></a>

## [tf2\_msgs](https://github.com/ros2/geometry2/tree/kilted/tf2_msgs/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Contributors: mosfet80

<a id="tf2-py"></a>

## [tf2\_py](https://github.com/ros2/geometry2/tree/kilted/tf2_py/CHANGELOG.rst)

- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Add a python3-dev dependency to tf2\_py. ([#733](https://github.com/ros2/geometry2/issues/733))
- Remove use of python\_cmake\_module ([#651](https://github.com/ros2/geometry2//issues/651))
- Contributors: Chris Lalancette, Lucas Wendland

<a id="tf2-ros"></a>

## [tf2\_ros](https://github.com/ros2/geometry2/tree/kilted/tf2_ros/CHANGELOG.rst)

- Uniform cmake min version ([#764](https://github.com/ros2/geometry2/issues/764))
- Add `rclcpp::shutdown` ([#762](https://github.com/ros2/geometry2/issues/762))
- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- specified quaternion order to be xyzw ([#718](https://github.com/ros2/geometry2/issues/718))
- Add configurable TF topics ([#709](https://github.com/ros2/geometry2//issues/709))
- Adding static transform listener ([#673](https://github.com/ros2/geometry2/issues/673))
- Updated deprecated message filter headers ([#702](https://github.com/ros2/geometry2/issues/702))
- Update qos for deprecation ([#695](https://github.com/ros2/geometry2/issues/695))
- Cli tools documentation ([#653](https://github.com/ros2/geometry2/issues/653))
- Contributors: Abhishek Kashyap, Alejandro Hernández Cordero, Emmanuel, Lucas Wendland, Ryan, Tom Moore, Yuyuan Yuan, mosfet80

<a id="tf2-ros-py"></a>

## [tf2\_ros\_py](https://github.com/ros2/geometry2/tree/kilted/tf2_ros_py/CHANGELOG.rst)

- Fix external docs mappings ([#757](https://github.com/ros2/geometry2/issues/757))
- Add in the linters for tf2\_ros\_py. ([#740](https://github.com/ros2/geometry2/issues/740))
- Adding StaticTransformListener in Python ([#719](https://github.com/ros2/geometry2/issues/719))
- Add in test\_xmllint for geometry2 python packages. ([#725](https://github.com/ros2/geometry2/issues/725))
- Add configurable TF topics ([#709](https://github.com/ros2/geometry2//issues/709))
- Fix the time\_jump\_callback signature. ([#711](https://github.com/ros2/geometry2//issues/711))
- Switch to using a context manager for the python examples. ([#700](https://github.com/ros2/geometry2/issues/700)) That way we can be sure to always clean up, but use less code doing so.
- Contributors: Chris Lalancette, Emmanuel, Lucas Wendland, Ryan

<a id="tf2-sensor-msgs"></a>

## [tf2\_sensor\_msgs](https://github.com/ros2/geometry2/tree/kilted/tf2_sensor_msgs/CHANGELOG.rst)

- Deprecate C Headers ([#720](https://github.com/ros2/geometry2/issues/720))
- Add a python3-dev dependency to tf2\_py. ([#733](https://github.com/ros2/geometry2/issues/733))
- Remove use of python\_cmake\_module ([#651](https://github.com/ros2/geometry2//issues/651))
- Contributors: Chris Lalancette, Lucas Wendland

<a id="tf2-tools"></a>

## [tf2\_tools](https://github.com/ros2/geometry2/tree/kilted/tf2_tools/CHANGELOG.rst)

- Add in test\_xmllint for geometry2 python packages. ([#725](https://github.com/ros2/geometry2/issues/725))
- Add configurable TF topics ([#709](https://github.com/ros2/geometry2//issues/709))
- [view\_frames] log filenames after it’s been determined ([#674](https://github.com/ros2/geometry2/issues/674))
- Contributors: Chris Lalancette, Mikael Arguedas, Ryan

<a id="tlsf"></a>

## [tlsf](https://github.com/ros2/tlsf/tree/kilted/tlsf/CHANGELOG.rst)

- Fixed link ([#15](https://github.com/ros2/tlsf/issues/15))
- Contributors: Alejandro Hernández Cordero

<a id="tlsf-cpp"></a>

## [tlsf\_cpp](https://github.com/ros2/realtime_support/tree/kilted/tlsf_cpp/CHANGELOG.rst)

- Explicitly shutdown context before test exits ([#129](https://github.com/ros2/realtime_support/issues/129))
- Reduce the number of files we compile. ([#125](https://github.com/ros2/realtime_support/issues/125))
- Contributors: Chris Lalancette, yadunund

<a id="topic-monitor"></a>

## [topic\_monitor](https://github.com/ros2/demos/tree/kilted/topic_monitor/CHANGELOG.rst)

- Add test\_xmllint.py to all of the ament\_python packages. ([#704](https://github.com/ros2/demos/issues/704))
- Contributors: Chris Lalancette

<a id="topic-statistics-demo"></a>

## [topic\_statistics\_demo](https://github.com/ros2/demos/tree/kilted/topic_statistics_demo/CHANGELOG.rst)

- Uniform CMAKE min VERSION ([#714](https://github.com/ros2/demos/issues/714))
- Contributors: mosfet80

<a id="tracetools"></a>

## [tracetools](https://github.com/ros2/ros2_tracing/tree/kilted/tracetools/CHANGELOG.rst)

- Switch to ament\_cmake\_ros\_core package ([#162](https://github.com/ros2/ros2_tracing/issues/162))
- Instrument client/service for end-to-end request/response tracking ([#145](https://github.com/ros2/ros2_tracing/issues/145))
- Don’t try to build on BSD ([#142](https://github.com/ros2/ros2_tracing/issues/142))
- Change expected rmw GID array size to 16 bytes ([#138](https://github.com/ros2/ros2_tracing/issues/138))
- Fix up two different C problems. ([#129](https://github.com/ros2/ros2_tracing/issues/129))
- Ignore zero-variadic-macro-arguments warnings from lttng-ust macros ([#126](https://github.com/ros2/ros2_tracing/issues/126))
- Remove deprecated TRACEPOINT macros ([#123](https://github.com/ros2/ros2_tracing/issues/123))
- Fix type for buffer index argument in tracepoint event declaration. ([#117](https://github.com/ros2/ros2_tracing/issues/117))
- Contributors: Chris Lalancette, Christophe Bedard, Mattis Kieffer, Michael Carroll, Scott K Logan

<a id="tracetools-launch"></a>

## [tracetools\_launch](https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_launch/CHANGELOG.rst)

- Fix or ignore new mypy issues ([#161](https://github.com/ros2/ros2_tracing/issues/161))
- Improve Python typing annotations ([#152](https://github.com/ros2/ros2_tracing/issues/152))
- Expose types for tracing tools ([#153](https://github.com/ros2/ros2_tracing/issues/153))
- Allow enabling syscalls through `ros2 trace` or the Trace action ([#137](https://github.com/ros2/ros2_tracing/issues/137))
- Contributors: Christophe Bedard, Michael Carlstrom

<a id="tracetools-read"></a>

## [tracetools\_read](https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_read/CHANGELOG.rst)

- Improve Python typing annotations ([#152](https://github.com/ros2/ros2_tracing/issues/152))
- Expose types for tracing tools ([#153](https://github.com/ros2/ros2_tracing/issues/153))
- Contributors: Christophe Bedard, Michael Carlstrom

<a id="tracetools-test"></a>

## [tracetools\_test](https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_test/CHANGELOG.rst)

- Fix or ignore new mypy issues ([#161](https://github.com/ros2/ros2_tracing/issues/161))
- Improve Python typing annotations ([#152](https://github.com/ros2/ros2_tracing/issues/152))
- Expose types for tracing tools ([#153](https://github.com/ros2/ros2_tracing/issues/153))
- Run relevant test\_tracetools tests with all instrumented rmw impls ([#116](https://github.com/ros2/ros2_tracing/issues/116))
- Contributors: Christophe Bedard, Michael Carlstrom

<a id="tracetools-trace"></a>

## [tracetools\_trace](https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_trace/CHANGELOG.rst)

- Improve Python typing annotations ([#152](https://github.com/ros2/ros2_tracing/issues/152))
- Expose types for tracing tools ([#153](https://github.com/ros2/ros2_tracing/issues/153))
- Remove unnecessary ‘type: ignore’ comments in tracetools\_trace ([#151](https://github.com/ros2/ros2_tracing/issues/151))
- Instrument client/service for end-to-end request/response tracking ([#145](https://github.com/ros2/ros2_tracing/issues/145))
- Allow enabling syscalls through `ros2 trace` or the Trace action ([#137](https://github.com/ros2/ros2_tracing/issues/137))
- Contributors: Christophe Bedard, Michael Carlstrom

<a id="turtlesim"></a>

## [turtlesim](https://github.com/ros/ros_tutorials/tree/kilted/turtlesim/CHANGELOG.rst)

- Create turtlesim\_msgs ([#169](https://github.com/ros/ros_tutorials/issues/169))
- Add icon for Jazzy. ([#167](https://github.com/ros/ros_tutorials/issues/167))
- [teleop\_turtle\_key] update usage string to match keys captured by keyboard ([#165](https://github.com/ros/ros_tutorials/issues/165))
- Contributors: Alejandro Hernández Cordero, Marco A. Gutierrez, Mikael Arguedas

<a id="turtlesim-msgs"></a>

## [turtlesim\_msgs](https://github.com/ros/ros_tutorials/tree/kilted/turtlesim_msgs/CHANGELOG.rst)

- Create turtlesim\_msgs ([#169](https://github.com/ros/ros_tutorials/issues/169))
- Contributors: Alejandro Hernández Cordero

<a id="type-description-interfaces"></a>

## [type\_description\_interfaces](https://github.com/ros2/rcl_interfaces/tree/kilted/type_description_interfaces/CHANGELOG.rst)

- Add missing build\_export\_depend on rosidl\_core\_runtime ([#165](https://github.com/ros2/rcl_interfaces/issues/165))
- Contributors: Scott K Logan

<a id="unique-identifier-msgs"></a>

## [unique\_identifier\_msgs](https://github.com/ros2/unique_identifier_msgs/tree/kilted/CHANGELOG.rst)

- Add missing build\_export\_depend on rosidl\_core\_runtime ([#30](https://github.com/ros2/unique_identifier_msgs/issues/30))
- Contributors: Scott K Logan

<a id="urdf"></a>

## [urdf](https://github.com/ros2/urdf/tree/kilted/urdf/CHANGELOG.rst)

- make linters happy ([#45](https://github.com/ros2/urdf/issues/45))
- Added documentation with rosdoc2 ([#40](https://github.com/ros2/urdf/issues/40))
- Added commom linters ([#39](https://github.com/ros2/urdf/issues/39))
- Use rcutils to log ([#37](https://github.com/ros2/urdf/issues/37))
- Enable test\_robot\_model\_parser test ([#38](https://github.com/ros2/urdf/issues/38))
- Contributors: Alejandro Hernández Cordero

<a id="urdf-parser-plugin"></a>

## [urdf\_parser\_plugin](https://github.com/ros2/urdf/tree/kilted/urdf_parser_plugin/CHANGELOG.rst)

- Added commom linters ([#39](https://github.com/ros2/urdf/issues/39))
- Contributors: Alejandro Hernández Cordero

<a id="zenoh-cpp-vendor"></a>

## [zenoh\_cpp\_vendor](https://github.com/ros2/rmw_zenoh/tree/kilted/zenoh_cpp_vendor/CHANGELOG.rst)

- Bump Zenoh to v1.3.2 and improve e2e reliability with HeartbeatSporadic ([#591](https://github.com/ros2/rmw_zenoh/issues/591))
- Add quality declaration ([#483](https://github.com/ros2/rmw_zenoh/issues/483))
- Fix liveliness crash in debug mode ([#544](https://github.com/ros2/rmw_zenoh/issues/544))
- Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5 ([#503](https://github.com/ros2/rmw_zenoh/issues/503))
- Enable Zenoh UDP transport ([#486](https://github.com/ros2/rmw_zenoh/issues/486))
- Bump zenoh-c to 261493 and zenoh-cpp to 5dfb68c ([#463](https://github.com/ros2/rmw_zenoh/issues/463))
- Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) ([#456](https://github.com/ros2/rmw_zenoh/issues/456))
- Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) ([#446](https://github.com/ros2/rmw_zenoh/issues/446))
- Bump zenoh-c and zenoh-cpp to 1.1.1 ([#424](https://github.com/ros2/rmw_zenoh/issues/424))
- Update Zenoh version ([#405](https://github.com/ros2/rmw_zenoh/issues/405))
- Vendors zenoh-cpp for rmw\_zenoh.
- Contributors: Alejandro Hernández Cordero, ChenYing Kuo (CY), Chris Lalancette, Franco Cipollone, Hugal31, Julien Enoch, Luca Cominardi, Yadunund, Yuyuan Yuan

<a id="zenoh-security-tools"></a>

## [zenoh\_security\_tools](https://github.com/ros2/rmw_zenoh/tree/kilted/zenoh_security_tools/CHANGELOG.rst)

- Add zenoh\_security\_tools ([#595](https://github.com/ros2/rmw_zenoh/issues/595))
- Contributors: yadunund
