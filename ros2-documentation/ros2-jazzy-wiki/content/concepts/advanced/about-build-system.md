---
title: "The build system"
docname: "Concepts/Advanced/About-Build-System"
source: "Concepts/Advanced/About-Build-System.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](../basic/about-actions.md) | [Client libraries](../basic/about-client-libraries.md) | [Composition](../intermediate/about-composition.md) | [Cross-compilation](../intermediate/about-cross-compilation.md) | [Different ROS 2 middleware vendors](../intermediate/about-different-middleware-vendors.md)

<a id="the-build-system"></a>

# The build system

Table of Contents

- [Build tool](#build-tool)
- [Build helpers](#build-helpers)

  - [The `ament_package` package](#the-ament-package-package)
  - [The `ament_cmake` repository](#the-ament-cmake-repository)
  - [The `ament_lint` repository](#the-ament-lint-repository)
- [Meta-build tool](#meta-build-tool)

The build system is what allows developers to build their ROS 2 code as needed.
ROS 2 relies heavily on the division of code into packages, with each package containing a manifest file (`package.xml`).
This manifest file contains essential metadata about the package, including its dependencies on other packages.
This manifest is required for the meta-build tool to function.

The ROS 2 build system consists of 3 major concepts.

<a id="build-tool"></a>

## Build tool

This is the software that controls the compilation and testing of a single package.
In ROS 2 this is usually CMake for C++, and setuptools for Python, but other build tools are supported.

<a id="build-helpers"></a>

## Build helpers

These are helper functions that hook into the build tool to improve the developer experience.
ROS 2 packages typically rely on the `ament` series of packages for this.
`ament` consists of a few important repositories which are all in the [GitHub organization](https://github.com/ament).

<a id="the-ament-package-package"></a>

### The `ament_package` package

Located on [GitHub](https://github.com/) at [ament/ament\_package](https://github.com/ament/ament_package), this repository contains a single [ament Python package](#term-ament-Python-package) that provides various utilities for [ament packages](#term-ament-package), e.g. templates for environment hooks.

All [ament packages](#term-ament-package) must contain a single [package.xml](#term-package.xml) file at the root of the package regardless of their underlying build system.
The [package.xml](#term-package.xml) “manifest” file contains information that is required in order to process and operate on a [package](../../reference/glossary.md#term-package).
This [package](../../reference/glossary.md#term-package) information includes things like the [package](../../reference/glossary.md#term-package)’s name, which is globally unique, and the package’s dependencies.
The [package.xml](#term-package.xml) file also serves as the marker file which indicates the location of the [package](../../reference/glossary.md#term-package) on the file system.

Parsing of the [package.xml](#term-package.xml) files is provided by `catkin_pkg` (as in ROS 1), while functionality to locate [packages](../../reference/glossary.md#term-package) by searching the file system for these [package.xml](#term-package.xml) files is provided by build tools such as `colcon`.

package.xml
:   Package manifest file which marks the root of a [package](../../reference/glossary.md#term-package) and contains meta information about the [package](../../reference/glossary.md#term-package) including its name, version, description, maintainer, license, dependencies, and more.
    The contents of the manifest are in machine readable XML format and the contents are described in the [REPs](../../reference/glossary.md#term-REP) [127](https://reps.openrobotics.org/rep-0127/) and [140](https://reps.openrobotics.org/rep-0140/), with the possibility of further modifications in future [REPs](../../reference/glossary.md#term-REP).

So anytime some [package](../../reference/glossary.md#term-package) is referred to as an [ament package](#term-ament-package), it means that it is a single unit of software (source code, build files, tests, documentation, and other resources) which is described using a [package.xml](#term-package.xml) manifest file.

ament package
:   Any [package](../../reference/glossary.md#term-package) which contains a [package.xml](#term-package.xml) and follows the packaging guidelines of `ament`, regardless of the underlying build system.

Since the term [ament package](#term-ament-package) is build system agnostic, there can be different kinds of [ament packages](#term-ament-package), e.g. [ament CMake package](#term-ament-CMake-package), [ament Python package](#term-ament-Python-package), etc.

Here is a list of common package types that you might run into in this software stack:

CMake package
:   Any [package](../../reference/glossary.md#term-package) containing a plain CMake project and a [package.xml](#term-package.xml) manifest file.

ament CMake package
:   A [CMake package](#term-CMake-package) that also follows the `ament` packaging guidelines.

Python package
:   Any [package](../../reference/glossary.md#term-package) containing a [setuptools](https://pypi.org/project/setuptools/) based Python project and a [package.xml](#term-package.xml) manifest file.

ament Python package
:   A [Python package](#term-Python-package) that also follows the `ament` packaging guidelines.

<a id="the-ament-cmake-repository"></a>

### The `ament_cmake` repository

Located on [GitHub](https://github.com/) at [ament/ament\_cmake](https://github.com/ament/ament_cmake), this repository contains many “ament CMake” and pure CMake packages which provide the infrastructure in CMake that is required to create “ament CMake” packages.
In this context “ament CMake” packages means: `ament` packages that are built using CMake.
So the [packages](../../reference/glossary.md#term-package) in this repository provide the necessary CMake functions/macros and CMake Modules to facilitate creating more “ament CMake” (or `ament_cmake`) packages.
Packages of this type are identified with the `<build_type>ament_cmake</build_type>` tag in the `<export>` tag of the [package.xml](#term-package.xml) file.

The [packages](../../reference/glossary.md#term-package) in this repository are extremely modular, but there is a single “bottleneck” [package](../../reference/glossary.md#term-package) called `ament_cmake`.
Anyone can depend on the `ament_cmake` [package](../../reference/glossary.md#term-package) to get all of the aggregate functionality of the [packages](../../reference/glossary.md#term-package) in this repository.
Here a list of the [packages](../../reference/glossary.md#term-package) in the repository along with a short description:

- `ament_cmake`

  - aggregates all other [packages](../../reference/glossary.md#term-package) in this repository, users need only to depend on this
- `ament_cmake_auto`

  - provides convenience CMake functions which automatically handle a lot of the tedious parts of writing a [package](../../reference/glossary.md#term-package)’s `CMakeLists.txt` file
- `ament_cmake_core`

  - provides all built-in core concepts for `ament`, e.g. environment hooks, resource indexing, symbolic linking install and others
- `ament_cmake_gmock`

  - adds convenience functions for making gmock based unit tests
- `ament_cmake_gtest`

  - adds convenience functions for making gtest based automated tests
- `ament_cmake_nose`

  - adds convenience functions for making nosetests based python automated tests
- `ament_cmake_python`

  - provides CMake functions for [packages](../../reference/glossary.md#term-package) that contain Python code
  - see the [ament\_cmake\_python user documentation](../../how-to/ament-cmake-python-documentation.md)
- `ament_cmake_test`

  - aggregates different kinds of tests, e.g. gtest and nosetests, under a single target using [CTest](https://cmake.org/Wiki/CMake/Testing_With_CTest)

The `ament_cmake_core` [package](../../reference/glossary.md#term-package) contains a lot of the CMake infrastructure that makes it possible to cleanly pass information between [packages](../../reference/glossary.md#term-package) using conventional interfaces.
This makes the [packages](../../reference/glossary.md#term-package) have more decoupled build interfaces with other [packages](../../reference/glossary.md#term-package), promoting their reuse and encouraging conventions in the build systems of different [packages](../../reference/glossary.md#term-package).
For instance, it provides a standard way to pass include directories, libraries, definitions, and dependencies between [packages](../../reference/glossary.md#term-package) so that consumers of this information can access this information in a conventional way.

The `ament_cmake_core` [package](../../reference/glossary.md#term-package) also provides features of the `ament` build system like symbolic link installation, which allows you to symbolically link files from either the source space or the build space into the install space rather than copying them.
This allows you to install once and then edit non-generated resources like Python code and configuration files without having to rerun the install step for them to take effect.
This feature essentially replaces the “devel space” from `catkin` because it has most of the advantages with few of the complications or drawbacks.

Another feature provided by `ament_cmake_core` is the [package](../../reference/glossary.md#term-package) resource indexing which is a way for [packages](../../reference/glossary.md#term-package) to indicate that they contain a resource of some type.
The design of this feature makes it much more efficient to answer simple questions like what [packages](../../reference/glossary.md#term-package) are in this prefix (e.g. `/usr/local`) because it only requires that you list the files in a single possible location under that prefix.
You can read more about this feature in the [design docs](https://github.com/ament/ament_cmake/blob/jazzy/ament_cmake_core/doc/resource_index.md) for the resource index.

Like `catkin`, `ament_cmake_core` also provides environment setup files and [package](../../reference/glossary.md#term-package) specific environment hooks.
The environment setup files, often named something like `setup.bash`, are a place for [package](../../reference/glossary.md#term-package) developers to define changes to the environment that are needed to utilize their [package](../../reference/glossary.md#term-package).
The developers are able to do this using an “environment hook” which is basically an arbitrary bit of shell code that can set or modify environment variables, define shell functions, setup auto-completion rules, etc…
This feature is how, for example, ROS 1 set the `ROS_DISTRO` environment variable without `catkin` knowing anything about the ROS distribution.

<a id="the-ament-lint-repository"></a>

### The `ament_lint` repository

Located on [GitHub](https://github.com/) at [ament/ament\_lint](https://github.com/ament/ament_lint), this repository provides several [packages](../../reference/glossary.md#term-package) which provide linting and testing services in a convenient and consistent manner.
Currently there are [packages](../../reference/glossary.md#term-package) to support C++ style linting using `uncrustify`, static C++ code checks using `cppcheck`, checking for copyright in source code, Python style linting using `pep8`, and other things.
The list of helper packages will likely grow in the future.

<a id="meta-build-tool"></a>

## Meta-build tool

This is a piece of software that knows how to topologically order a group of packages, and build or test them in the correct dependency order.
This software will call into the Build Tool to do the actual work of compiling, testing, and installing the package.

In ROS 2, the tool named [colcon](https://colcon.readthedocs.io/en/released/) is used for this.
