---
title: "ROS 2 on Raspberry Pi"
docname: "How-To-Guides/Installing-on-Raspberry-Pi"
source: "How-To-Guides/Installing-on-Raspberry-Pi.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="ros-2-on-raspberry-pi"></a>

# ROS 2 on Raspberry Pi

ROS 2 is supported on both 32 bit (arm32) and 64 bit (arm64) ARM processors.
However, you can see [here](https://reps.openrobotics.org/rep-2000/) that arm64 receives Tier 1 support, while arm32 is Tier 3.
Tier 1 support means distribution specific packages and binary archives are available, while Tier 3 requires the user to compile ROS 2 from source.

The fastest and simplest way to use ROS 2 is to use a Tier 1 supported configuration.

This would mean either installing 64 bit Ubuntu on to the Raspberry Pi, or using the 64 bit version of Raspberry Pi OS and running ROS 2 in Docker.

<a id="ubuntu-linux-on-raspberry-pi-with-binary-ros-2-install"></a>

## Ubuntu Linux on Raspberry Pi with binary ROS 2 install

Ubuntu for Raspberry Pi is available [here](https://ubuntu.com/download/raspberry-pi).

Make sure to confirm that you have selected the correct version as described in [REP-2000](https://reps.openrobotics.org/rep-2000/).

Ubuntu for Raspberry Pi doesn’t include the *backports* and *updates* software suites by default, which are required for the ROS 2 binary install to work.

So, please check and edit the `/etc/apt/sources.list.d/ubuntu.sources` file on your Raspberry Pi before installing ROS 2.

For example, the Ubuntu 24.04 “Noble Numbat” release should have an entry that looks like this:

```
Types: deb
URIs: http://ports.ubuntu.com/ubuntu-ports/
Suites: noble noble-updates noble-backports       # <-- IMPORTANT LINE
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

You can now install ROS 2 using the normal binary installation instructions for Ubuntu Linux.

<a id="raspberry-pi-os-with-ros-2-in-docker"></a>

## Raspberry Pi OS with ROS 2 in docker

Raspberry Pi OS 64 bit version is [available here](https://www.raspberrypi.com/software/operating-systems/).

Raspberry Pi OS is based on Debian which receives Tier 3 support, but it can run Ubuntu docker containers for Tier 1 support.

After flashing the OS, [install Docker](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script).

The official ROS 2 Docker images can be found [here](https://hub.docker.com/_/ros/tags).

You may choose from ros-core, ros-base, or perception.
See [here](https://reps.openrobotics.org/rep-2001/) for more information on these variants.

Fetch and run an image:

```
$ docker pull ros:jazzy-ros-core
$ docker run -it --rm ros:jazzy-ros-core
```

You can also build images yourself:

Clone the [docker\_images git repo](https://github.com/osrf/docker_images) onto the Raspberry Pi, change in to the directory linked above, then to the directory with your preferred variant.

Inside of the directory, build the container with:

```
$ docker build -t ros_docker .
```

On a supported system it will only take a minute or two to build the docker containers, as the source code is already built in to binaries.
