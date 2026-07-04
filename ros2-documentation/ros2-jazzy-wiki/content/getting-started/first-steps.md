---
title: "First steps with ROS - learning path"
docname: "First-Steps"
source: "First-Steps.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "getting-started"
tags: ["ros2", "jazzy", "getting-started"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Getting Started hub](../../wiki/task-map.md)
> Related: [About ROS](about-ros.md) | [Citations](../reference/citations.md) | [Concepts](../concepts/overview.md) | [Contact](../reference/contact.md) | [Distributions](../releases/overview.md)

<a id="first-steps-with-ros-learning-path"></a>
<a id="id1"></a>

# First steps with ROS - learning path

ROS (Robot Operating System) is an open-source ecosystem that provides framework, tools, and libraries for building, deploying, running, and maintaining robotic applications.
This page presents a set of articles and hands-on activities to introduce the main concepts behind the ROS framework.
Working through these will give you the essential knowledge needed to start developing applications with ROS.

**Area: ROS-framework | Content-type: learning-path | Experience: beginner**

Contents

- [Summary](#summary)
- [Prerequisites](#prerequisites)
- [Steps](#steps)

  - [1 Learn about fundamental concepts behind ROS](#learn-about-fundamental-concepts-behind-ros)
  - [2 Install ROS and turtlesim](#install-ros-and-turtlesim)
  - [3 Try out working with the main communication components of the ROS framework](#try-out-working-with-the-main-communication-components-of-the-ros-framework)
  - [4 Learn about introspection with logs](#learn-about-introspection-with-logs)
  - [5 Learn about using launch files](#learn-about-using-launch-files)
  - [6 Learn about data recording and playback](#learn-about-data-recording-and-playback)
- [Next steps](#next-steps)

<a id="summary"></a>

## Summary

The ROS framework is the “plumbing” which makes communication between different parts of a robot possible.
It includes messaging, standard interfaces, and support for multiple programming languages and platforms.

You need to understand the fundamental concepts of the framework before you can work with ROS to develop or maintain applications.
The turtlesim tool and the tutorials in this site will help you get up to speed.

<a id="prerequisites"></a>

## Prerequisites

None.
The steps outlined in this article will guide you through downloading and installing everything you need to learn the basics of ROS.

<a id="steps"></a>

## Steps

<a id="learn-about-fundamental-concepts-behind-ros"></a>

### 1 Learn about fundamental concepts behind ROS

- [About ROS](about-ros.md)
- [Nodes](../concepts/basic/about-nodes.md)
- [Interfaces (topics, services, actions)](../concepts/basic/interfaces-topics-services-actions.md)
- [Parameters](../concepts/basic/about-parameters.md)

<a id="install-ros-and-turtlesim"></a>

### 2 Install ROS and turtlesim

ROS installation includes the essential packages for working with ROS.
If you’re familiar with Linux, our recommended platform is Ubuntu (deb packages).
Otherwise, a good alternative installation platform is Windows (binaries): [Installation options](../installation/overview.md)

With turtlesim, a lightweight 2D simulation tool designed for beginners, you can learn core ROS concepts in a simple visual environment: [Install and set up turtlesim](../tutorials/beginner-cli-tools/introducing-turtlesim.md)

<a id="try-out-working-with-the-main-communication-components-of-the-ros-framework"></a>

### 3 Try out working with the main communication components of the ROS framework

Use turtlesim to familiarize yourself with the main communication components and try out messaging in the ROS framework.

1. Complete the nodes tutorial: [Understanding nodes](../tutorials/beginner-cli-tools/understanding-ros2-nodes.md)
2. Complete the topics tutorial: [Understanding topics](../tutorials/beginner-cli-tools/understanding-ros2-topics.md)
3. Complete the services tutorial: [Understanding services](../tutorials/beginner-cli-tools/understanding-ros2-services.md)
4. Complete the parameters tutorial: [Understanding parameters](../tutorials/beginner-cli-tools/understanding-ros2-parameters.md)
5. Complete the actions tutorial: [Understanding actions](../tutorials/beginner-cli-tools/understanding-ros2-actions.md)

<a id="learn-about-introspection-with-logs"></a>

### 4 Learn about introspection with logs

Introspection enables you to see information about how a system is operating.
Nodes use logs to output messages concerning events and status in a variety of ways.

To see introspection through logs in action, complete the rqt\_console tutorial: [Using rqt\_console to view logs](../tutorials/beginner-cli-tools/using-rqt-console.md)

<a id="learn-about-using-launch-files"></a>

### 5 Learn about using launch files

Launch files allow you to start and configure a number of processes containing ROS nodes simultaneously, instead of opening multiple terminals and re-entering configuration details for each node.

Complete the launch files tutorial: [Launching nodes](../tutorials/beginner-cli-tools/launching-multiple-nodes.md)

<a id="learn-about-data-recording-and-playback"></a>

### 6 Learn about data recording and playback

Sometimes it’s useful to replay data to reproduce the results of your tests and experiments, to debug your robot’s behaviour, or to share your work with others.

Complete the recording and playback tutorial: [Recording and playing back data](../tutorials/beginner-cli-tools/recording-and-playing-back-data.md)

<a id="next-steps"></a>

## Next steps

To complete your knowledge of the ROS framework, we recommend familiarizing yourself with ROS client libraries: [Beginner: Client libraries](../tutorials/beginner-client-libraries.md)
