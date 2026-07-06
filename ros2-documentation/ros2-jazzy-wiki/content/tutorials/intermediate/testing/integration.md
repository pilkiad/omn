---
title: "Writing Basic Integration Tests with launch_testing"
docname: "Tutorials/Intermediate/Testing/Integration"
source: "Tutorials/Intermediate/Testing/Integration.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-basic-integration-tests-with-launch-testing"></a>

# Writing Basic Integration Tests with launch\_testing

**Goal:** Create and run integration tests on the ROS 2 turtlesim node.

**Tutorial level:** Intermediate

**Time:** 20 minutes

Contents

- [Prerequisites](#prerequisites)
- [Background](#background)
- [Overview](#overview)
- [Steps](#steps)

  - [1 Describe the test in the test launch file](#describe-the-test-in-the-test-launch-file)
  - [2 Register the test in the CMakeLists.txt](#register-the-test-in-the-cmakelists-txt)
  - [3 Dependencies and package organization](#dependencies-and-package-organization)
  - [4 Running tests and report generation](#running-tests-and-report-generation)
- [Summary](#summary)
- [Related content](#related-content)

<a id="prerequisites"></a>

## Prerequisites

Before starting this tutorial, it is recommended to have completed the following tutorials on launching nodes:

- [Launching Multiple Nodes](../../beginner-cli-tools/launching-multiple-nodes.md)
- [Creating Launch files](../launch/creating-launch-files.md)

<a id="background"></a>

## Background

Where unit tests focus on validating a very specific piece of functionality, integration tests focus on validating the interaction between pieces of code.
In ROS 2 this is often accomplished by launching a system of one or several nodes, for example the [Gazebo simulator](https://gazebosim.org/home) and the [Nav2 navigation](https://github.com/ros-planning/navigation2.git) stack.
As a result, these tests are more complex both to set up and to run.

A key aspect of ROS 2 integration testing is that nodes that are part of different tests shouldn’t communicate with each other, even when run in parallel.
This will be achieved here using a specific test runner that picks unique [ROS domain IDs](../../../concepts/intermediate/about-domain-id.md).
In addition, integration tests have to fit in the overall testing workflow.
A standardized approach is to ensure each test outputs an XUnit file, which are easily parsed using common test tooling.

<a id="overview"></a>

## Overview

The main tool in use here is the [launch\_testing](https://docs.ros.org/en/jazzy/p/launch_testing/index.html) package
([launch\_testing repository](https://github.com/ros2/launch/tree/jazzy/launch_testing)).
This ROS-agnostic functionality can extend a Python launch file with both active tests (that run while the nodes are also running) and post-shutdown tests (which run once after all nodes have exited).
`launch_testing` relies on the Python standard module [unittest](https://docs.python.org/3/library/unittest.html) for the actual testing.
To get our integration tests run as part of `colcon test`, we register the launch file in the `CMakeLists.txt`.

<a id="steps"></a>

## Steps

<a id="describe-the-test-in-the-test-launch-file"></a>

### 1 Describe the test in the test launch file

Both the nodes under test and the tests themselves are launched using a Python launch file, which resembles a ROS 2 Python launch file.
It is customary to make the integration test launch file names follow the pattern `test/test_*.py`.

There are two common types of tests in integration testing: active tests, which run while the nodes under test are running, and post-shutdown tests, which are run after exiting the nodes.
We will cover both in this tutorial.

<a id="imports"></a>

#### 1.1 Imports

We first start by importing the Python modules we will be using.
Only two modules are specific to testing: the general-purpose `unittest`, and `launch_testing`.

```
import os
import sys
import time
import unittest

import launch
import launch_ros
import launch_testing.actions
import rclpy
from turtlesim.msg import Pose
```

<a id="generate-the-test-description"></a>

#### 1.2 Generate the test description

The function `generate_test_description` describes what to launch, similar to `generate_launch_description` in a ROS 2 Python launch file.
In the example below, we launch the turtlesim node and half a second later our tests.

In more complex integration test setups, you will probably want to launch a system of several nodes, together with additional nodes that perform mocking or must otherwise interact with the nodes under test.

```
def generate_test_description():
    return (
        launch.LaunchDescription(
            [
                # Nodes under test
                launch_ros.actions.Node(
                    package='turtlesim',
                    namespace='',
                    executable='turtlesim_node',
                    name='turtle1',
                ),
                # Launch tests 0.5 s later
                launch.actions.TimerAction(
                    period=0.5, actions=[launch_testing.actions.ReadyToTest()]),
            ]
        ), {},
    )
```

<a id="active-tests"></a>

#### 1.3 Active tests

The active tests interact with the running nodes.
In this tutorial, we will check whether the turtlesim node publishes pose messages (by listening to the node’s ‘turtle1/pose’ topic) and whether it logs that it spawned the turtle (by listening to stderr).

The active tests are defined as methods of a class inheriting from [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase).
The child class, here `TestTurtleSim`, contains the following methods:

- `test_*`: the test methods, each performing some ROS communication with the nodes under test and/or listening to the process output (passed in through `proc_output`).
  They are executed sequentially.
- `setUp`, `tearDown`: respectively run before (to prepare the test fixture) and after executing each test method.
  By creating the node in the `setUp` method, we use a different node instance for each test to reduce the risk of tests communicating with each other.
- `setUpClass`, `tearDownClass`: these class methods respectively run once before and after executing all the test methods.

It’s highly recommended to go through [launch\_testing’s detailed documentation on this topic](https://docs.ros.org/en/jazzy/p/launch_testing/index.html).

```
# Active tests
class TestTurtleSim(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = rclpy.create_node('test_turtlesim')

    def tearDown(self):
        self.node.destroy_node()

    def test_publishes_pose(self, proc_output):
        """Check whether pose messages published"""
        msgs_rx = []
        sub = self.node.create_subscription(
            Pose, 'turtle1/pose',
            lambda msg: msgs_rx.append(msg), 100)
        try:
            # Listen to the pose topic for 10 s
            end_time = time.time() + 10
            while time.time() < end_time:
                # spin to get subscriber callback executed
                rclpy.spin_once(self.node, timeout_sec=1)
            # There should have been 100 messages received
            assert len(msgs_rx) > 100
        finally:
            self.node.destroy_subscription(sub)

    def test_logs_spawning(self, proc_output):
        """Check whether logging properly"""
        proc_output.assertWaitFor(
            'Spawning turtle [turtle1] at x=',
            timeout=5, stream='stderr')
```

Note that the way we listen to the ‘turtle1/pose’ topic in `test_publishes_pose` differs from [the usual approach](../../beginner-client-libraries/writing-a-simple-py-publisher-and-subscriber.md).
Instead of calling the blocking `rclpy.spin`, we trigger the `spin_once` method - which executes the first available callback (our subscriber callback if a message arrived within 1 second) - until we have gathered all messages published over the last 10 seconds.
The package [launch\_testing\_ros](https://docs.ros.org/en/jazzy/p/launch_testing_ros/index.html) provides some convenience functions to achieve similar behavior,
such as [WaitForTopics](https://docs.ros.org/en/jazzy/p/launch_testing_ros/launch_testing_ros.wait_for_topics.html).

If you want to go further, you can implement a third test that publishes a twist message, asking the turtle to move, and subsequently checks that it moved by asserting that the pose message changed.
This effectively automates part of the [Turtlesim introduction tutorial](../../beginner-cli-tools/introducing-turtlesim.md).

<a id="post-shutdown-tests"></a>

#### 1.4 Post-shutdown tests

The classes marked with the `launch_testing.post_shutdown_test` decorator are run after letting the nodes under test exit.
A typical test here is whether the nodes exited cleanly, for which `launch_testing` provides the method
[asserts.assertExitCodes](https://docs.ros.org/en/jazzy/p/launch_testing/launch_testing.asserts.html#launch_testing.asserts.assertExitCodes).

```
# Post-shutdown tests
@launch_testing.post_shutdown_test()
class TestTurtleSimShutdown(unittest.TestCase):
    def test_exit_codes(self, proc_info):
        """Check if the processes exited normally."""
        launch_testing.asserts.assertExitCodes(proc_info)
```

<a id="register-the-test-in-the-cmakelists-txt"></a>

### 2 Register the test in the CMakeLists.txt

Registering the test in the `CMakeLists.txt` fulfills two functions:

- it integrates it in the `CTest` framework ROS 2 CMake-based packages rely on
  (and hence it will be called when running `colcon test`).
- it allows to specify *how* the test is to be run -
  in this case, with a unique domain id to ensure test isolation.

This latter aspect is realized using the special test runner [run\_test\_isolated.py](https://github.com/ros2/ament_cmake_ros/blob/jazzy/ament_cmake_ros/cmake/run_test_isolated.py).
To ease adding several integration tests, we define the CMake function `add_ros_isolated_launch_test` such that each additional test requires only a single line.

```
cmake_minimum_required(VERSION 3.8)
project(app)

########
# test #
########

if(BUILD_TESTING)
  # Integration tests
  find_package(ament_cmake_ros REQUIRED)
  find_package(launch_testing_ament_cmake REQUIRED)
  function(add_ros_isolated_launch_test path)
    set(RUNNER "${ament_cmake_ros_DIR}/run_test_isolated.py")
    add_launch_test("${path}" RUNNER "${RUNNER}" ${ARGN})
  endfunction()
  add_ros_isolated_launch_test(test/test_integration.py)
endif()
```

<a id="dependencies-and-package-organization"></a>

### 3 Dependencies and package organization

Finally, add the following dependencies to your `package.xml`:

```
<test_depend>ament_cmake_ros</test_depend>
<test_depend>launch</test_depend>
<test_depend>launch_ros</test_depend>
<test_depend>launch_testing</test_depend>
<test_depend>launch_testing_ament_cmake</test_depend>
<test_depend>rclpy</test_depend>
<test_depend>turtlesim</test_depend>
```

After following the above steps, your package (here named ‘app’) ought to look as follows:

```
app/
  CMakeLists.txt
  package.xml
  tests/
      test_integration.py
```

Integration tests can be part of any ROS package.
One can dedicate one or more packages to just integration testing, or alternatively add them to the package of which they test the functionality.
In this tutorial, we go with the first option as we will test the existing turtlesim node.

<a id="running-tests-and-report-generation"></a>

### 4 Running tests and report generation

For running the integration test and examining the results, see the tutorial [Running Tests in ROS 2 from the Command Line](cli.md).

<a id="summary"></a>

## Summary

In this tutorial, we explored the process of creating and running integration tests on the ROS 2 turtlesim node.
We discussed the integration test launch file and covered writing active tests and post-shutdown tests.
To recap, the four key elements of the integration test launch file are:

- The function `generate_test_description`: This launches our nodes under tests as well as our tests.
- `launch_testing.actions.ReadyToTest()`: This alerts the test framework that the tests should be run, and ensures that the active tests and the nodes are run together.
- An undecorated class inheriting from `unittest.TestCase`: This houses the active tests, including set up and teardown, and gives access to ROS logging through `proc_output`.
- A second class inheriting from `unittest.TestCase` decorated with `@launch_testing.post_shutdown_test()`: These are tests that run after all nodes have shutdown; it is common to assert that the nodes exited cleanly.

The launch test is subsequently registered in the `CMakeLists.txt` using the custom cmake macro `add_ros_isolated_launch_test` which ensures that each launch test runs with a unique `ROS_DOMAIN_ID`,
avoiding undesired cross communication.

<a id="related-content"></a>

## Related content

- [Why automatic tests?](testing-main.md)
- [C++ unit testing with GTest](cpp.md)
  and [Python unit testing with Pytest](python.md)
- [launch\_pytest documentation](https://docs.ros.org/en/jazzy/p/launch_pytest/index.html),
  an alternative launch integration testing package to `launch_testing`
