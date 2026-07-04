---
title: "Running Tests in ROS 2 from the Command Line"
docname: "Tutorials/Intermediate/Testing/CLI"
source: "Tutorials/Intermediate/Testing/CLI.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="running-tests-in-ros-2-from-the-command-line"></a>

# Running Tests in ROS 2 from the Command Line

<a id="prerequisites"></a>

## Prerequisites

You will need a workspace setup with packages that have tests in them.

<a id="build-and-run-your-tests"></a>

## Build and run your tests

To compile and run the tests, simply run the [test](https://colcon.readthedocs.io/en/released/reference/verb/test.html) verb from `colcon` at the root of your workspace.

```
$ colcon test --ctest-args tests [package_selection_args]
```

Where `package_selection_args` are optional package selection arguments for `colcon` to limit which packages are built and run.
Find more info in the [colcon documentation on Package selection arguments](https://colcon.readthedocs.io/en/released/reference/package-selection-arguments.html)

[Sourcing the workspace](../../beginner-client-libraries/colcon-tutorial.md#colcon-tutorial-source-the-environment) before testing should not be necessary.
`colcon test` makes sure that the tests run with the right environment, have access to their dependencies, etc.

<a id="examine-test-results"></a>

## Examine Test Results

To see the results, simply run the [test-result](https://colcon.readthedocs.io/en/released/reference/verb/test-result.html) verb from `colcon`.

```
$ colcon test-result --all
```

To see the exact test cases which fail, use the `--verbose` flag:

```
$ colcon test-result --all --verbose
```

<a id="debugging-tests-with-gdb"></a>

## Debugging tests with GDB

For detailed guidance on debugging tests using GDB, refer to the [GDB Tutorial](../../../how-to/getting-backtraces-in-ros-2.md).
