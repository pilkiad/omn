---
title: "Migrating your package.xml to format 2"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-Package-XML"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-Package-XML.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating C++ Packages Reference](migrating-cpp-packages.md)

<a id="migrating-your-package-xml-to-format-2"></a>

# Migrating your package.xml to format 2

Table of Contents

- [Prerequisites](#prerequisites)
- [Migrate from format 1 to 2](#migrate-from-format-1-to-2)

  - [Add `format` attribute to `<package>`](#add-format-attribute-to-package)
  - [Replace `<run_depend>`](#replace-run-depend)
  - [Convert some `<build_depend>` to `<test_depend>`](#convert-some-build-depend-to-test-depend)
  - [Begin using `<doc_depend>`](#begin-using-doc-depend)
  - [Simplify dependencies with `<depend>`](#simplify-dependencies-with-depend)
- [Test your new `package.xml`](#test-your-new-package-xml)

ROS 2 requires `package.xml` files to use at least [format 2](https://reps.openrobotics.org/rep-0140/).
This guide shows how to migrate a `package.xml` from format 1 to format 2.

If the `<package>` tag at the start of your `package.xml` looks like either of the following, then it is using format 1 and you must migrate it.

```
<package>
```

```
<package format="1">
```

<a id="prerequisites"></a>

## Prerequisites

You should have a working ROS 1 installation.
This enables you to check that the converted `package.xml` is valid by building and testing the package, since ROS 1 supports all `package.xml` format versions.

<a id="migrate-from-format-1-to-2"></a>

## Migrate from format 1 to 2

Format 1 and format 2 differ in how they specify dependencies.
Read the [compatibility section in REP-0140](https://reps.openrobotics.org/rep-0140/#compatibility) for a summary of the differences.

<a id="add-format-attribute-to-package"></a>

### Add `format` attribute to `<package>`

Add or set the `format` attribute to `2` to indicate that the `package.xml` uses format 2.

```
<package format="2">
```

<a id="replace-run-depend"></a>

### Replace `<run_depend>`

The `<run_depend>` tag is no longer allowed.
If you have a dependency specified like this:

```
<run_depend>foo</run_depend>
```

then replace it with one or both of these tags:

```
<build_export_depend>foo</build_export_depend>
<exec_depend>foo</exec_depend>
```

If the dependency is needed when something in your package is executed, then use the `<exec_depend>` tag.
If packages that depend on your package need the dependency when they are built, then use the `<build_export_depend>` tag.
Use both tags if you are unsure.

<a id="convert-some-build-depend-to-test-depend"></a>

### Convert some `<build_depend>` to `<test_depend>`

In format 1 `<test_depend>` declares dependencies that are needed when running your package’s tests.
It still does that in format 2, but it additionally declares dependencies that are needed when building your package’s tests.

Because of the limitations of this tag in format 1, your package may have a test-only dependency specified as a `<build_depend>` like this:

```
<build_depend>testfoo</build_depend>
```

If so, change it to a `<test_depend>`.

```
<test_depend>testfoo</test_depend>
```

> [!NOTE]
>
> If you are using CMake, then make sure your test dependencies are only referenced within a `if(BUILD_TESTING)` block:
>
> ```
> if (BUILD_TESTING)
>     find_package(testfoo REQUIRED)
> endif()
> ```

<a id="begin-using-doc-depend"></a>

### Begin using `<doc_depend>`

Use the new `<doc_depend>` tag to declare dependencies needed for building your package’s documentation.
For example, C++ packages might have this dependency:

```
<doc_depend>doxygen</doc_depend>
```

while Python packages might have this one:

```
<doc_depend>python3-sphinx</doc_depend>
```

See [the guide on documenting ROS 2 packages](../documenting-a-ros-2-package.md) for more information.

<a id="simplify-dependencies-with-depend"></a>

### Simplify dependencies with `<depend>`

`<depend>` is a new tag that makes `package.xml` files more concise.
If your `package.xml` has these three tags for the same dependency:

```
<build_depend>foo</build_depend>
<build_export_depend>foo</build_export_depend>
<exec_depend>foo</exec_depend>
```

then replace them with a single `<depend>` like this:

```
<depend>foo</depend>
```

<a id="test-your-new-package-xml"></a>

## Test your new `package.xml`

Build and test your package as you normally do using `catkin_make`, `cakin_make_isolated`, or the `catkin` build tool.
If everything succeeds, then your `package.xml` is valid.
