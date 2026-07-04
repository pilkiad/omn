---
title: "Configuring environment"
docname: "Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment"
source: "Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="configuring-environment"></a>
<a id="configros2"></a>

# Configuring environment

**Goal:** This tutorial will show you how to prepare your ROS 2 environment.

**Tutorial level:** Beginner

**Time:** 5 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Source the setup files](#source-the-setup-files)
  - [2 Add sourcing to your shell startup script](#add-sourcing-to-your-shell-startup-script)
  - [3 Check environment variables](#check-environment-variables)
- [Summary](#summary)
- [Next steps](#next-steps)

<a id="background"></a>

## Background

ROS 2 relies on the notion of combining workspaces using the shell environment.
“Workspace” is a ROS term for the location on your system where you’re developing with ROS 2.
The core ROS 2 workspace is called the underlay.
Subsequent local workspaces are called overlays.
When developing with ROS 2, you will typically have several workspaces active concurrently.

Combining workspaces makes developing against different versions of ROS 2, or against different sets of packages, easier.
It also allows the installation of several ROS 2 distributions (or “distros”, e.g. Dashing and Eloquent) on the same computer and switching between them.

This is accomplished by sourcing setup files every time you open a new shell, or by adding the source command to your shell startup script once.
Without sourcing the setup files, you won’t be able to access ROS 2 commands, or find or use ROS 2 packages.
In other words, you won’t be able to use ROS 2.

<a id="prerequisites"></a>

## Prerequisites

Before starting these tutorials, install ROS 2 by following the instructions on the ROS 2 [Installation](../../installation/overview.md) page.

The commands used in this tutorial assume you followed the binary packages installation guide for your operating system (deb packages for Linux).
You can still follow along if you built from source, but the path to your setup files will likely be different.
You also won’t be able to use the `sudo apt install ros-<distro>-<package>` command (used frequently in the beginner level tutorials) if you install from source.

If you are using Linux or macOS, but are not already familiar with the shell, [this tutorial](https://www.linux.com/training-tutorials/bash-101-working-cli/) will help.

<a id="tasks"></a>

## Tasks

<a id="source-the-setup-files"></a>

### 1 Source the setup files

You will need to run this command on every new shell you open to have access to the ROS 2 commands, like so:

Linux

```
$ source /opt/ros/jazzy/setup.bash
```

Replace `.bash` with your shell if you’re not using bash.
Possible values are: `setup.bash`, `setup.sh`, `setup.zsh`.

macOS

```
$ . ~/ros2_install/ros2-osx/setup.bash
```

Windows

```
$ call C:\dev\ros2\local_setup.bat
```

> [!NOTE]
>
> The exact command depends on where you installed ROS 2.
> If you’re having problems, ensure the file path leads to your installation.

<a id="add-sourcing-to-your-shell-startup-script"></a>

### 2 Add sourcing to your shell startup script

If you don’t want to have to source the setup file every time you open a new shell (skipping task 1), then you can add the command to your shell startup script:

Linux

```
$ echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

To undo this, locate your system’s shell startup script and remove the appended source command.

macOS

```
$ echo "source ~/ros2_install/ros2-osx/setup.bash" >> ~/.bash_profile
```

To undo this, locate your system’s shell startup script and remove the appended source command.

Windows

Only for PowerShell users, create a folder in ‘My Documents’ called ‘WindowsPowerShell’.
Within ‘WindowsPowerShell’, create file ‘Microsoft.PowerShell\_profile.ps1’.
Inside the file, paste:

```
$ C:\dev\ros2_jazzy\local_setup.ps1
```

PowerShell will request permission to run this script every time a new shell is opened.
To avoid that issue you can run:

```
$ Unblock-File C:\dev\ros2_jazzy\local_setup.ps1
```

To undo this, remove the new ‘Microsoft.PowerShell\_profile.ps1’ file.

<a id="check-environment-variables"></a>

### 3 Check environment variables

Sourcing ROS 2 setup files will set several environment variables necessary for operating ROS 2.
If you ever have problems finding or using your ROS 2 packages, make sure that your environment is properly set up using the following command:

Linux

```
$ printenv | grep -i ROS
```

macOS

```
$ printenv | grep -i ROS
```

Windows

```
$ set | findstr -i ROS
```

Check that variables like `ROS_DISTRO` and `ROS_VERSION` are set.

```
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DISTRO=jazzy
```

If the environment variables are not set correctly, return to the ROS 2 package installation section of the installation guide you followed.
If you need more specific help (because environment setup files can come from different places), you can [get answers](https://robotics.stackexchange.com/) from the community.

<a id="the-ros-domain-id-variable"></a>

#### 3.1 The `ROS_DOMAIN_ID` variable

See the [domain ID](../../concepts/intermediate/about-domain-id.md) article for details on ROS domain IDs.

Once you have determined a unique integer for your group of ROS 2 nodes, you can set the environment variable with the following command:

Linux

```
$ export ROS_DOMAIN_ID=<your_domain_id>
```

To maintain this setting between shell sessions, you can add the command to your shell startup script:

```
$ echo "export ROS_DOMAIN_ID=<your_domain_id>" >> ~/.bashrc
```

macOS

```
$ export ROS_DOMAIN_ID=<your_domain_id>
```

To maintain this setting between shell sessions, you can add the command to your shell startup script:

```
$ echo "export ROS_DOMAIN_ID=<your_domain_id>" >> ~/.bash_profile
```

Windows

```
$ set ROS_DOMAIN_ID=<your_domain_id>
```

If you want to make this permanent between shell sessions, also run:

```
$ setx ROS_DOMAIN_ID <your_domain_id>
```

<a id="the-ros-automatic-discovery-range-variable"></a>

#### 3.2 The `ROS_AUTOMATIC_DISCOVERY_RANGE` variable

By default, ROS 2 communication is not limited to localhost.
`ROS_AUTOMATIC_DISCOVERY_RANGE` environment variable allows you to limit ROS 2 discovery range.
Using `ROS_AUTOMATIC_DISCOVERY_RANGE` is helpful in certain settings, such as classrooms, where multiple robots may publish to the same topic causing strange behaviors.
See [Improved Dynamic Discovery](../advanced/improved-dynamic-discovery.md#improveddynamicdiscovery) for more details.

<a id="summary"></a>

## Summary

The ROS 2 development environment needs to be correctly configured before use.
This can be done in two ways: either sourcing the setup files in every new shell you open, or adding the source command to your startup script.

If you ever face any problems locating or using packages with ROS 2, the first thing you should do is check your environment variables and ensure they are set to the version and distro you intended.

<a id="next-steps"></a>

## Next steps

Now that you have a working ROS 2 installation and you know how to source its setup files, you can start learning the ins and outs of ROS 2 with the [turtlesim tool](introducing-turtlesim.md).
