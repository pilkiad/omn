---
title: "Cross-compilation"
docname: "Concepts/Intermediate/About-Cross-Compilation"
source: "Concepts/Intermediate/About-Cross-Compilation.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](../basic/about-actions.md) | [Client libraries](../basic/about-client-libraries.md) | [Composition](about-composition.md) | [Different ROS 2 middleware vendors](about-different-middleware-vendors.md) | [Discovery](../basic/about-discovery.md)

<a id="cross-compilation"></a>

# Cross-compilation

Table of Contents

- [Overview](#overview)
- [How does it work ?](#how-does-it-work)
- [Alternatives](#alternatives)

<a id="overview"></a>

## Overview

Open Robotics provides pre-built ROS 2 packages for multiple platforms, but a number of developers still rely on [cross-compilation](https://en.wikipedia.org/wiki/Cross_compiler) for different reasons such as:
:   - The development machine does not match the target system.
    - Tuning the build for specific core architecture (e.g. setting -mcpu=cortex-a53 -mfpu=neon-fp-armv8 when building for Raspberry Pi3).
    - Targeting a file system other than the ones supported by the pre-built images released by Open Robotics.

<a id="how-does-it-work"></a>

## How does it work ?

Cross-compiling simple software (e.g. no dependencies on external libraries) is relatively simple and only requiring a cross-compiler toolchain to be used instead of the native toolchain.

There are a number of factors which make this process more complex:
:   - The software being built must support the target architecture.
      Architecture specific code must be properly isolated and enabled during the build according to the target architecture.
      Examples include assembly code.
    - All dependencies (e.g. libraries) must be present, either as pre-built or cross-compiled packages, before the target software using them is cross-compiled.
    - When building software stacks (as opposed to standalone software) using build tools (e.g. colcon), it is expected that the build tool provides a mechanism to allow the developer to enable cross-compilation on the underlying build system used by each piece of software in the stack.

<a id="alternatives"></a>

## Alternatives

An alternative to cross-compilation is to [build multi-platform Docker images](https://github.com/docker/buildx#building-multi-platform-images) using `docker buildx`.
