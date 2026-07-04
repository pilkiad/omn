---
title: "Writing Basic Tests with Python"
docname: "Tutorials/Intermediate/Testing/Python"
source: "Tutorials/Intermediate/Testing/Python.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-basic-tests-with-python"></a>

# Writing Basic Tests with Python

Starting point: we’ll assume you have a [basic ament\_python package](../../beginner-client-libraries/creating-your-first-ros2-package.md#createpkg) set up already and you want to add some tests to it.

If you are using ament\_cmake\_python, refer to the [ament\_cmake\_python docs](../../../how-to/ament-cmake-python-documentation.md) for how to make tests discoverable.
The test contents and invocation with `colcon` remain the same.

<a id="package-setup"></a>

## Package Setup

<a id="setup-py"></a>

### setup.py

Your `setup.py` must have a test dependency on `pytest` within the call to `setup(...)`:

```
tests_require=['pytest'],
```

<a id="test-files-and-folders"></a>

### Test Files and Folders

Your test code needs to go in a folder named `tests` in the root of your package.

Any file that contains tests that you want to run must have the pattern `test_FOO.py` where `FOO` can be replaced with anything.

<a id="example-package-layout"></a>

#### Example package layout:

```
awesome_ros_package/
  awesome_ros_package/
      __init__.py
      fozzie.py
  package.xml
  setup.cfg
  setup.py
  tests/
      test_init.py
      test_copyright.py
      test_fozzie.py
```

<a id="test-contents"></a>

## Test Contents

You can now write tests to your heart’s content.
There are [plenty of resources on pytest](https://docs.pytest.org), but in short, you can write functions with the `test_` prefix and include whatever assert statements you’d like.

```
def test_math():
    assert 2 + 2 == 5   # This should fail for most mathematical systems
```

<a id="running-tests"></a>

## Running Tests

See the [tutorial on how to run tests from the command line](cli.md) for more information on running the tests and inspecting the test results.

<a id="special-commands"></a>

## Special Commands

Beyond the [standard colcon testing commands](cli.md) you can also specify arguments to the `pytest` framework from the command line with the `--pytest-args` flag.
For example, you can specify the name of the function to run with

Linux/macOS

```
$ colcon test --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function
```

Windows

```
$ colcon test --merge-install --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function
```

To see the pytest output while running the tests, use these flags:

```
$ colcon test --event-handlers console_cohesion+
```
