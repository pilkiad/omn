---
title: "Writing Basic Tests with C++ with GTest"
docname: "Tutorials/Intermediate/Testing/Cpp"
source: "Tutorials/Intermediate/Testing/Cpp.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-basic-tests-with-c-with-gtest"></a>

# Writing Basic Tests with C++ with GTest

Starting point: we’ll assume you have a [basic ament\_cmake package](../../beginner-client-libraries/creating-your-first-ros2-package.md#createpkg) set up already and you want to add some tests to it.

In this tutorial, we’ll be using [gtest](https://google.github.io/googletest/primer.html).

<a id="package-setup"></a>

## Package Setup

<a id="source-code"></a>

### Source Code

We’ll start off with our code in a file called `test/tutorial_test.cpp`

```
#include <gtest/gtest.h>

TEST(package_name, a_first_test)
{
  ASSERT_EQ(4, 2 + 2);
}

int main(int argc, char ** argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
```

<a id="package-xml"></a>

### package.xml

Add the following line to `package.xml`

```
<test_depend>ament_cmake_gtest</test_depend>
```

<a id="cmakelists-txt"></a>

### CMakeLists.txt

```
if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  ament_add_gtest(${PROJECT_NAME}_tutorial_test test/tutorial_test.cpp)
  target_include_directories(${PROJECT_NAME}_tutorial_test PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
  )
  # target_link_libraries(${PROJECT_NAME}_tutorial_test name_of_local_library)
endif()
```

The testing code is wrapped in the `if/endif` block to avoid building tests where possible.
`ament_add_gtest` functions much like `add_executable` so you’ll need to call `target_include_directories` and `target_link_libraries` as you normally would.
The `target_link_libraries` call is shown commented out because `name_of_local_library` is a placeholder, uncomment it and replace `name_of_local_library` with the actual target name from your `add_library()` call only if your tests depend on a library built in this package.

<a id="running-tests"></a>

## Running Tests

See the [tutorial on how to run tests from the command line](cli.md) for more information on running the tests and inspecting the test results.
