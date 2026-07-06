---
title: "Overview and usage of RQt"
docname: "Concepts/Intermediate/About-RQt"
source: "Concepts/Intermediate/About-RQt.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](../basic/about-actions.md) | [Client libraries](../basic/about-client-libraries.md) | [Composition](about-composition.md) | [Cross-compilation](about-cross-compilation.md) | [Different ROS 2 middleware vendors](about-different-middleware-vendors.md)

<a id="overview-and-usage-of-rqt"></a>

# Overview and usage of RQt

Table of Contents

- [Overview](#overview)
- [System setup](#system-setup)

  - [Installing From debs](#installing-from-debs)
- [RQt Components Structure](#rqt-components-structure)
- [Advantage of RQt framework](#advantage-of-rqt-framework)
- [Further Reading](#further-reading)

<a id="overview"></a>

## Overview

RQt is a graphical user interface framework that implements various tools and interfaces in the form of plugins.
One can run all the existing GUI tools as dockable windows within RQt.
The tools can still run in a traditional standalone method, but RQt makes it easier to manage all the various windows in a single screen layout.

You can run any RQt tools/plugins easily by:

```
$ rqt
```

This GUI allows you to choose any available plugins on your system.
You can also run plugins in standalone windows.
For example, RQt Python Console:

```
$ ros2 run rqt_py_console rqt_py_console
```

Users can create their own plugins for RQt with either `Python` or `C++`.
To see what RQt plugins are available for your system, run:

```
$ ros2 pkg list
```

And then look for packages that start with `rqt_`.

<a id="system-setup"></a>

## System setup

<a id="installing-from-debs"></a>

### Installing From debs

```
$ sudo apt install ros-jazzy-rqt*
```

<a id="rqt-components-structure"></a>

## RQt Components Structure

RQt consists of two metapackages:

- *rqt* - core infrastructure modules.
- *rqt\_common\_plugins* - Commonly useful debugging tools.

<a id="advantage-of-rqt-framework"></a>

## Advantage of RQt framework

Compared to building your own GUIs from scratch:

- Standardized common procedures for GUI (start-shutdown hook, restore previous states).
- Multiple widgets can be docked in a single window.
- Easily turn your existing Qt widgets into RQt plugins.
- Expect support at [Robotics Stack Exchange](https://robotics.stackexchange.com/) (ROS community website for the questions).

From system architecture’s perspective:

- Support multi-platform (basically wherever [QT](http://qt-project.org/) and ROS run) and multi-language (`Python`, `C++`).
- Manageable lifecycle: RQt plugins using a common API makes maintenance & reuse easier.

<a id="further-reading"></a>

## Further Reading

- ROS 2 Discourse [announcement of porting to ROS 2](https://discourse.openrobotics.org/t/rqt-in-ros2/6428))
- [RQt for ROS 1 documentation](https://wiki.ros.org/rqt)
- Brief overview of RQt (from [a Willow Garage intern blog post](http://web.archive.org/web/20130518142837/http://www.willowgarage.com/blog/2012/10/21/ros-gui))
