---
title: "Running ROS 2 nodes in Docker [community-contributed]"
docname: "How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers"
source: "How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="running-ros-2-nodes-in-docker-community-contributed"></a>

# Running ROS 2 nodes in Docker [community-contributed]

<a id="run-two-nodes-in-a-single-docker-container"></a>

## Run two nodes in a single docker container

Pull the ROS docker image with tag “jazzy-desktop”.

```
$ docker pull osrf/ros:jazzy-desktop
```

Run the image in a container in interactive mode.

```
$ docker run -it osrf/ros:jazzy-desktop
```

Your best friend is the `ros2` command line help now.

```
$ ros2 --help
```

E.g. list all installed packages.

```
$ ros2 pkg list
(you will see a list of packages)
```

E.g. list all executables:

```
$ ros2 pkg executables
(you will see a list of <package> <executable>)
```

Run a minimal example of 2 C++ nodes (1 topic subscriber `listener`, 1 topic publisher `talker`) from the package `demo_nodes_cpp` in this container:

```
$ ros2 run demo_nodes_cpp listener &
$ ros2 run demo_nodes_cpp talker
```

<a id="run-two-nodes-in-two-separate-docker-containers"></a>

## Run two nodes in two separate docker containers

Open a terminal.
Run the image in a container in interactive mode and launch a topic publisher (executable `talker` from the package `demo_nodes_cpp`) with `ros2 run`:

```
$ docker run -it --rm osrf/ros:jazzy-desktop ros2 run demo_nodes_cpp talker
```

Open a second terminal.
Run the image in a container in interactive mode and launch a topic subscriber (executable `listener` from the package `demo_nodes_cpp`) with `ros2 run`:

```
$ docker run -it --rm osrf/ros:jazzy-desktop ros2 run demo_nodes_cpp listener
```

As an alternative to the command line invocation, you can create a `docker-compose.yml` file (here version 2) with the following (minimal) content:

```
version: '2'

services:
  talker:
    image: osrf/ros:jazzy-desktop
    command: ros2 run demo_nodes_cpp talker
  listener:
    image: osrf/ros:jazzy-desktop
    command: ros2 run demo_nodes_cpp listener
    depends_on:
      - talker
```

To run the containers call `docker compose up` in the same directory.
You can close the containers with `Ctrl+C`.
