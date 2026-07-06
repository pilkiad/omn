---
title: "Maintain source checkout"
docname: "Installation/Maintaining-a-Source-Checkout"
source: "Installation/Maintaining-a-Source-Checkout.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Installation hub](../../wiki/task-map.md)
> Related: [Alternatives](alternatives.md) | [Mirrors](ros-2-mirrors.md) | [RHEL (RPM packages)](rhel-install-rpms.md) | [RMW implementations](rmw-implementations.md) | [Testing with pre-release binaries](testing.md)

<a id="maintain-source-checkout"></a>
<a id="maintainingsource"></a>

# Maintain source checkout

> [!NOTE]
>
> For instructions on maintaining a source checkout of the **latest development version** of ROS 2, refer to
> [Maintaining a source checkout of ROS 2 Rolling](https://docs.ros.org/en/rolling/Installation/Maintaining-a-Source-Checkout.html)

- [Update your repository list](#update-your-repository-list)

  - [Latest ROS 2 Jazzy branches](#latest-ros-2-jazzy-branches)
- [Update your repositories](#update-your-repositories)
- [Download the new source code](#download-the-new-source-code)
- [Rebuild your workspace](#rebuild-your-workspace)
- [Inspect your source checkout](#inspect-your-source-checkout)

If you have installed ROS 2 from source, there may have been changes made to the source code since the time that you checked it out.
To keep your source checkout up to date, you will have to periodically update your `ros2.repos` file, download the latest sources, and rebuild your workspace.

<a id="update-your-repository-list"></a>

## Update your repository list

Each ROS 2 release includes a `ros2.repos` file that contains the list of repositories and their version for that release.

<a id="latest-ros-2-jazzy-branches"></a>

### Latest ROS 2 Jazzy branches

If you wish to checkout the latest code for ROS 2 Jazzy, you can get the relevant repository list by running:

Linux

```
$ cd ~/ros2_jazzy
$ mv -i ros2.repos ros2.repos.old
$ wget https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos
```

macOS

```
$ cd ~/ros2_jazzy
$ mv -i ros2.repos ros2.repos.old
$ wget https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos
```

Windows

Use a Windows command line interface:

```
$ cd \dev\ros2_jazzy
$ curl -sk https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos -o ros2.repos
```

Or a powershell:

```
$ cd \dev\ros2_jazzy
$ curl https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos -o ros2.repos
```

<a id="update-your-repositories"></a>

## Update your repositories

You will notice that in the [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos) file, each repository has a `version` associated with it that points to a particular commit hash, tag, or branch name.
It is possible that these versions refer to new tags/branches that your local copy of the repositories will not recognize as they are out-of-date.
Because of this, you should update the repositories that you have already checked out with the following command:

```
$ vcs custom --args remote update
```

<a id="download-the-new-source-code"></a>

## Download the new source code

You should now be able to download the sources associated with the new repository list with:

Linux

```
$ vcs import src < ros2.repos
$ vcs pull src
```

macOS

```
$ vcs import src < ros2.repos
$ vcs pull src
```

Windows

In a Windows command line interface:

```
$ vcs import --input ros2.repos src
$ vcs pull src
```

Or in powershell:

```
$ vcs import --input ros2.repos src
$ vcs pull src
```

<a id="rebuild-your-workspace"></a>

## Rebuild your workspace

Now that the workspace is up to date with the latest sources, remove your previous install and rebuild your workspace with, for example:

```
$ colcon build --symlink-install
```

<a id="inspect-your-source-checkout"></a>

## Inspect your source checkout

During your development you may have deviated from the original state of your workspace from when you imported the repository list.
If you wish to know the versions of the set of repositories in your workspace, you can export the information using the following command:

Linux

```
$ cd ~/ros2_jazzy
$ vcs export src > my_ros2.repos
```

macOS

```
$ cd ~/ros2_jazzy
$ vcs export src > my_ros2.repos
```

Windows

```
$ cd \dev\ros2_jazzy
$ vcs export src > my_ros2.repos
```

This `my_ros2.repos` file can then be shared with others so that they can reproduce the state of the repositories in your workspace.
