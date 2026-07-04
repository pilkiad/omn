---
title: "Testing with pre-release binaries"
docname: "Installation/Testing"
source: "Installation/Testing.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Installation hub](../../wiki/task-map.md)
> Related: [Alternatives](alternatives.md) | [Maintain source checkout](maintaining-a-source-checkout.md) | [Mirrors](ros-2-mirrors.md) | [RHEL (RPM packages)](rhel-install-rpms.md) | [RMW implementations](rmw-implementations.md)

<a id="testing-with-pre-release-binaries"></a>

# Testing with pre-release binaries

Many ROS packages are provided as pre-built binaries.
Usually, you will get the released version of binaries when following [Installation](overview.md).
There are also pre-released versions of binaries that are useful for testing before making an official release.
This article describes several options if you would like to try out pre-released versions of ROS binaries.

When packages are released into a ROS distribution (using bloom), the buildfarm builds them into deb packages which are stored temporarily in the **building** apt repository.
As dependent packages are rebuilt, an automatic process periodically synchronizes the packages in **building** to a secondary repository called **ros-testing**.
**ros-testing** is intended as a soaking area where developers and bleeding-edge users may give the packages extra testing, before they are manually synced into the public ros repository from which users typically install packages.

Approximately every two weeks, the rosdistro’s release manager manually synchronizes the contents of **ros-testing** into the **main** ROS repository.

<a id="deb-testing-repository"></a>

## deb testing repository

For Debian-based operating systems, you can install binary packages from the **ros-testing** repository.

1. Make sure you have a working ROS 2 installation from deb packages (see [Installation](overview.md)).
2. Install the ros2-testing-apt-source package.
   This will automatically uninstall the ros2-apt-source package since only one repository may be enabled at a time.

   ```
   $ sudo apt install -y ros2-testing-apt-source
   ```
3. Update the apt index:

   ```
   $ sudo apt update
   ```
4. You can now install individual packages from the testing repository, for example:

   ```
   $ sudo apt install ros-jazzy-my-just-released-package
   ```
5. Alternatively, you can move your entire ROS 2 installation to the testing repository:

   ```
   $ sudo apt dist-upgrade
   ```
6. Once you are finished testing, you can switch back to the normal repository by re-installing the ros-apt-source package:

   ```
   $ sudo apt install -y ros2-apt-source
   ```

   and doing an update and upgrade:

   ```
   $ sudo apt update
   $ sudo apt dist-upgrade
   ```

<a id="rhel-testing-repository"></a>

## RHEL testing repository

For RHEL you can install binary packages from the **ros-testing** repository, by enabling the testing repository on the source configuration:

1. Make sure you have a working ROS 2 installation for rpm packages (see the [RHEL installation instructions](rhel-install-rpms.md)).
2. Enable testing and disable main repository:

   ```
   $ sudo dnf config-manager --set-enabled ros2-testing
   $ sudo dnf config-manager --set-disabled ros2
   ```
3. Update the dnf index:

   ```
   $ sudo dnf update
   ```
4. You can now install individual packages from the testing repository, for example:

> ```
> $ sudo dnf install ros-jazzy-my-just-released-package
> ```

5. Once you are finished testing, you can switch back to the normal repository by re-enabling the main repository:

> ```
> $ sudo dnf config-manager --set-disabled ros2-testing
> $ sudo dnf config-manager --set-enabled ros2
> ```
>
> and doing an update and upgrade:
>
> ```
> $ sudo dnf update
> $ sudo dnf system-upgrade
> ```

<a id="binary-archives"></a>
<a id="prerelease-binaries"></a>

## Binary archives

For core packages, we run nightly packaging jobs for Ubuntu Linux, RHEL, and Windows.
These packaging jobs produce archives with pre-built binaries that can be downloaded and extracted to your filesystem.

1. Make sure you have all dependencies installed according to the [latest development setup](alternatives/latest-development-setup.md) for your platform.
2. Go to <https://ci.ros2.org/view/packaging/> and select a packaging job from the list corresponding to your platform.
3. Under the heading “Last Successful Artifacts” you should see a download link (e.g. for Windows, `ros2-package-windows-AMD64.zip`).
4. Download and extract the archive to your file system.
5. To use the binary archive installation, source the `setup.*` file that can be found in the root of the archive.

   Ubuntu Linux and RHEL

   ```
   $ source path/to/extracted/archive/setup.bash
   ```

   Windows

   ```
   $ call path\to\extracted\archive\setup.bat
   ```

<a id="docker"></a>

## Docker

For Ubuntu Linux, there is also a nightly Docker image based on the nightly binary archive.

1. Pull the Docker image:

   ```
   $ docker pull osrf/ros2:nightly
   ```
2. Start an interactive container:

   ```
   $ docker run -it osrf/ros2:nightly
   ```

For support on running GUI applications in Docker, take a look at the tutorial [User GUI’s with Docker](https://wiki.ros.org/docker/Tutorials/GUI) or the tool [rocker](https://github.com/osrf/rocker).
