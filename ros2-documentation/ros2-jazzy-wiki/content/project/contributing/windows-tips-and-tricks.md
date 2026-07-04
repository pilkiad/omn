---
title: "Windows Tips and Tricks"
docname: "The-ROS2-Project/Contributing/Windows-Tips-and-Tricks"
source: "The-ROS2-Project/Contributing/Windows-Tips-and-Tricks.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "project"
tags: ["ros2", "jazzy", "project"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Project hub](../../../wiki/tooling-map.md)
> Related: [Add Your Project](../adopters/add-your-project.md) | [Code style and language versions](code-style-language-versions.md) | [Contributing to ROS 2 Documentation](contributing-to-ros-2-documentation.md) | [Quality guide: ensuring code quality](quality-guide.md) | [ROS 2 developer guide](developer-guide.md)

<a id="windows-tips-and-tricks"></a>

# Windows Tips and Tricks

Table of Contents

- [Maximum Path Length](#maximum-path-length)
- [Symbol Visibility](#symbol-visibility)

  - [Visibility Control Headers](#visibility-control-headers)
  - [WINDOWS\_EXPORT\_ALL\_SYMBOLS Target Property](#windows-export-all-symbols-target-property)
- [Debug builds](#debug-builds)
- [Forward-slash vs. back-slash](#forward-slash-vs-back-slash)
- [Patching vendored packages](#patching-vendored-packages)
- [Windows slow timers (slowness in general)](#windows-slow-timers-slowness-in-general)
- [Shells](#shells)

ROS 2 supports Windows 10 as a Tier 1 platform, which means that all code that goes into the ROS 2 core must support Windows.
For those used to traditional development on Linux or other Unix-like systems, developing on Windows can be a bit of a challenge.
This document aims to lay out some of those differences.

<a id="maximum-path-length"></a>

## Maximum Path Length

By default, Windows has a [maximum path length](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) of 260 characters.
Practically speaking, 4 of those characters are always used by the drive letter, colon, initial backslash, and final NULL character.
That means that only 256 characters are available for the *sum* of all parts of the path.
This has two practical consequences for ROS 2:

- Some of the ROS 2 internal path names are fairly long.
  Because of this, we always recommend using a short path name for the root of your ROS 2 directory, like `C:\dev`.
- When building ROS 2 from source, the default isolated build mode of colcon can generate very long path names.
  To avoid these very long path names, use `--merge-install` when building on Windows.

**Note**: It is possible to change Windows to have much longer maximum path lengths.
See [this article](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd#enable-long-paths-in-windows-10-version-1607-and-later) for more information.

<a id="symbol-visibility"></a>
<a id="windows-symbol-visibility"></a>

## Symbol Visibility

The Microsoft Visual C++ Compiler (MSVC) exposes symbols from a Dynamic Link Library (DLL) only if they are explicitly exported.
The clang and gcc compilers have an option to do the same, but it is off by default.
As a result, when a library previously built on Linux is built on Windows, other libraries may be unable to resolve the external symbols.
Below are examples of common error messages which can be caused by symbols not being exposed:

```
error C2448: '__attribute__': function-style initializer appears to be a function definition
'visibility': identifier not found
```

```
CMake Error at C:/ws_ros2/install/random_numbers/share/random_numbers/cmake/ament_cmake_export_libraries-extras.cmake:48 (message):
   Package 'random_numbers' exports the library 'random_numbers' which
   couldn't be found
```

Symbol Visibility also impacts binary loading.
If you are finding that a composable node does not run or a Qt Visualizer isn’t working, it may be that the hosting process can not find an expected symbol export from the binary.
To diagnose this on Windows, the Windows developer tools includes a program called Gflags to enable various options.
One of those options is called *Loader Snaps* which enables you to detect load failures while debugging.
Please visit the Microsoft Documentation for more information on [Gflags](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/setting-and-clearing-image-file-flags) and [Loaders snaps](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/show-loader-snaps).

Two solutions to export symbols on Windows are Visibility Control Headers and the `WINDOWS_EXPORT_ALL_SYMBOLS` property.
Microsoft recommends ROS developers use Visibility Control Headers to control the export of symbols from a binary.
Visibility Control Headers provide more control over the symbol export macro and offer other benefits including smaller binary size and reduced link times.

<a id="visibility-control-headers"></a>

### Visibility Control Headers

The purpose of Visibility Control Headers headers is to define a macro for each shared library which correctly declares symbols as dllimport or dllexport.
This is decided based on whether the library is being consumed or being built itself.
The logic in the macro also takes the compiler into account and includes logic to select the appropriate syntax.
The [GCC visibility documentation](https://gcc.gnu.org/wiki/Visibility) includes step by step instructions for adding explicit symbol visibility to a library “yielding the highest quality code with the greatest reductions in binary size, load times and link times”.
A header named `visibility_control.h` can be placed in the `includes` folder for each library as shown in the example below.
The example below shows how a visibility control header would be added for a `my_lib` library with a class called `example_class`.
Add a visibility header to the include folder for the library.
The boiler plate logic is used with the library name used in the macro to make it unique in the project.
In another library, `MY_LIB` would be replaced with the library name.

```
#ifndef MY_LIB__VISIBILITY_CONTROL_H_
#define MY_LIB__VISIBILITY_CONTROL_H_
#if defined _WIN32 || defined __CYGWIN__
#ifdef __GNUC__
   #define MY_LIB_EXPORT __attribute__ ((dllexport))
   #define MY_LIB_IMPORT __attribute__ ((dllimport))
#else
   #define MY_LIB_EXPORT __declspec(dllexport)
   #define MY_LIB_IMPORT __declspec(dllimport)
#endif
#ifdef MY_LIB_BUILDING_LIBRARY
   #define MY_LIB_PUBLIC MY_LIB_EXPORT
#else
   #define MY_LIB_PUBLIC MY_LIB_IMPORT
#endif
#define MY_LIB_PUBLIC_TYPE MY_LIB_PUBLIC
#define MY_LIB_LOCAL
#else
 // Linux visibility settings
#define MY_LIB_PUBLIC_TYPE
#endif
#endif  // MY_LIB__VISIBILITY_CONTROL_H_
```

For a complete example of this header, see [rviz\_rendering](https://github.com/ros2/rviz/blob/ros2/rviz_rendering/include/rviz_rendering/visibility_control.hpp).

To use the macro, add `MY_LIB_PUBLIC` before symbols which need to be visible to external libraries.
For example:

```
Class MY_LIB_PUBLIC example_class {}

MY_LIB_PUBLIC void example_function (){}
```

In order to build your library with correctly exported symbols, you will need to add the following to your CMakeLists.txt file:

```
target_compile_definitions(${PROJECT_NAME}
  PRIVATE "MY_LIB_BUILDING_LIBRARY")
```

<a id="windows-export-all-symbols-target-property"></a>

### WINDOWS\_EXPORT\_ALL\_SYMBOLS Target Property

CMake implements the `WINDOWS_EXPORT_ALL_SYMBOLS` property on Windows, which causes function symbols to be automatically exported.
More detail of how it works can be found in the [WINDOWS\_EXPORT\_ALL\_SYMBOLS CMake Documentation](https://cmake.org/cmake/help/latest/prop_tgt/WINDOWS_EXPORT_ALL_SYMBOLS.html).
The property can be implemented by adding the following to the CMakeLists file:

```
set_target_properties(${LIB_NAME} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
```

If there is more than one library in a CMakeLists file you will need to call `set_target_properties` on each of them separately.

Note that a binary on Windows can only export 65,536 symbols.
If a binary exports more than that, you will get an error and should use the visibility\_control headers.
There is an exception to this method in the case of global data symbols.
For example, a global static data member like the one below.

```
class Example_class
{
public:
static const int Global_data_num;
```

In these cases dllimprort/dllexport must be applied explicitly.
This can be done using generate\_export\_header as described in the following article: [Create dlls on Windows without declspec() using new CMake export all feature](https://blog.kitware.com/create-dlls-on-windows-without-declspec-using-new-cmake-export-all-feature/).

Finally, it is important that the header file that exports the symbols be included into at least one of the `.cpp` files in the package so that the macros will get expanded and placed into the resulting binary.
Otherwise the symbols will still not be callable.

<a id="debug-builds"></a>

## Debug builds

When building in Debug mode on Windows, several very important things change.
The first is that all DLLs get `_d` automatically appended to the library name.
So if the library is called `libfoo.dll`, in Debug mode it will be `libfoo_d.dll`.
The dynamic linker on Windows also knows to look for libraries of that form, so it will not find libraries without the `_d` prefix.
Additionally, Windows turns on a whole set of compile-time and run-time checks in Debug mode that is far more strict than Release builds.
For these reasons, it is a good idea to run a Windows Debug build and test on many pull requests.

<a id="forward-slash-vs-back-slash"></a>

## Forward-slash vs. back-slash

In Windows the default path separator is a backslash (`\`), which differs from the forward-slash (`/`) used in Linux and macOS.
Most of the Windows APIs can deal with either as a path separator, but this is not universally true.
For instance, the `cmd.exe` shell can only do tab-completion when using the backslash character, not the forward-slash.
For maximum compatibility on Windows, a backslash should always be used as the path separator on Windows.

<a id="patching-vendored-packages"></a>

## Patching vendored packages

When vendoring a package in ROS 2, it is often necessary to apply a patch to fix a bug, add a feature, etc.
The typical way to do this is to modify the `ExternalProject_add` call to add a `PATCH` command, using the `patch` executable.
Unfortunately, the `patch` executable as delivered by chocolatey requires Administrator access to run.
The workaround is to use `git apply-patch` when applying patches to external projects.

`git apply-patch` has its own issues in that it only works properly when applied to a git repository.
For that reason, external projects should always use the `GIT` method to obtain the project and then use the `PATCH_COMMAND` to invoke `git apply-patch`.

An example usage of all of the above looks something like:

```
ExternalProject_Add(mylibrary-${version}
  GIT_REPOSITORY https://github.com/lib/mylibrary.git
  GIT_TAG ${version}
  GIT_CONFIG advice.detachedHead=false
  # Suppress git update due to https://gitlab.kitware.com/cmake/cmake/-/issues/16419
  # See https://github.com/ament/uncrustify_vendor/pull/22 for details
  UPDATE_COMMAND ""
  TIMEOUT 600
  CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_install
    ${extra_cmake_args}
    -Wno-dev
  PATCH_COMMAND
    ${CMAKE_COMMAND} -E chdir <SOURCE_DIR> git apply -p1 --ignore-space-change --whitespace=nowarn ${CMAKE_CURRENT_SOURCE_DIR}/install-patch.diff
)
```

<a id="windows-slow-timers-slowness-in-general"></a>

## Windows slow timers (slowness in general)

Software running on Windows is, in general, much slower than that running on Linux.
This is due to a number of factors, from the default time slice (every 20 ms, according to the [documentation](https://docs.microsoft.com/en-us/windows/win32/procthread/multitasking)), to the number of anti-virus and anti-malware processes running, to the number of background processes running.
Because of all of this, tests should *never* expect tight timing on Windows.
All tests should have generous timeouts, and only expect events to happen eventually (this will also prevent tests from being flakey on Linux).

<a id="shells"></a>

## Shells

There are two main command-line shells on Windows: the venerable `cmd.exe`, and PowerShell.

`cmd.exe` is the command shell that most closely emulates the old DOS shell, though with greatly enhanced capabilities.
It is completely text based, and only understands DOS/Windows `batch` files.

PowerShell is the newer, object-based shell that Microsoft recommends for most new applications.
It understands `ps1` files for configuration.

ROS 2 supports both `cmd.exe` and PowerShell, so any changes (especially to things like `ament` or `colcon`) should be tested on both.
