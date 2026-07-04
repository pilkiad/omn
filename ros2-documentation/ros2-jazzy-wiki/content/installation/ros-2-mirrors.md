---
title: "Mirrors"
docname: "Installation/ROS-2-Mirrors"
source: "Installation/ROS-2-Mirrors.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "installation"
tags: ["ros2", "jazzy", "installation"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Installation hub](../../wiki/task-map.md)
> Related: [Alternatives](alternatives.md) | [Maintain source checkout](maintaining-a-source-checkout.md) | [RHEL (RPM packages)](rhel-install-rpms.md) | [RMW implementations](rmw-implementations.md) | [Testing with pre-release binaries](testing.md)

<a id="mirrors"></a>

# Mirrors

Table of Contents

- [Mirrors](#mirrors)

  - [Docs Mirrors](#docs-mirrors)
  - [Debian/Ubuntu (APT) Repository Mirrors](#debian-ubuntu-apt-repository-mirrors)

    - [Asia](#asia)
    - [Europe](#europe)
    - [North America](#north-america)
    - [Oceania](#oceania)
    - [South America and Africa](#south-america-and-africa)
  - [Creating a mirror](#creating-a-mirror)

    - [Using a Mirror](#using-a-mirror)
  - [Setting up a Mirror](#setting-up-a-mirror)

    - [Adding your mirror to this list](#adding-your-mirror-to-this-list)
  - [Mirroring docs.ros.org](#mirroring-docs-ros-org)

<a id="docs-mirrors"></a>

## Docs Mirrors

Mirrors of the ROS Docs act as a backup when the [main site](http://docs.ros.org) is unavailable, and may provide faster access to users who are geographically closer to the mirror.

<a id="debian-ubuntu-apt-repository-mirrors"></a>

## Debian/Ubuntu (APT) Repository Mirrors

To use these mirrors, replace the official ROS repository URL with the one listed below in your APT configuration.

<a id="asia"></a>

### Asia

|  |  |  |
| --- | --- | --- |
| Tsinghua University (TUNA) | China | <https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu/> |
| USTC | China | <https://mirrors.ustc.edu.cn/ros2/ubuntu/> |
| Alibaba Cloud (Aliyun) | China | <https://mirrors.aliyun.com/ros2/ubuntu/> |
| Qilu University of Technology (QLU) | China | <https://mirrors.qlu.edu.cn/ros2/ubuntu/> |
| Chongqing University (CQU) | China | <https://mirrors.cqu.edu.cn/ros2/ubuntu/> |

<a id="europe"></a>

### Europe

|  |  |  |
| --- | --- | --- |
| Delft University of Technology | the Netherlands | <http://ftp.tudelft.nl/ros2/ubuntu/> |

<a id="north-america"></a>

### North America

|  |  |  |
| --- | --- | --- |
| University of Maryland (UMD) | USA | <http://mirror.umd.edu/packages.ros.org/ros2/ubuntu/> |

<a id="oceania"></a>

### Oceania

|  |  |  |
| --- | --- | --- |
| AARNet | Australia | <https://mirror.aarnet.edu.au/pub/ros2-packages/ubuntu/> |

<a id="south-america-and-africa"></a>

### South America and Africa

There are currently no officially verified ROS 2 mirrors for these regions.
If you are hosting a mirror in South America or Africa and would like it listed here, please see the **Hosting a Mirror** section below.

<a id="creating-a-mirror"></a>

## Creating a mirror

If you are maintaining a mirror please join the Mirrors category on discourse.openrobotics.org: <https://discourse.openrobotics.org/c/infrastructure-project/infra-mirrors/> for both feedback and prompt updates.

<a id="using-a-mirror"></a>

### Using a Mirror

To use a mirror, replace `packages.ros.org` with the mirror URL in your `ros2-latest.list` file:

```
# Example for TUNA mirror
sudo sed -i 's|http://packages.ros.org/ros2/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu|g' /etc/apt/sources.list.d/ros2-latest.list
sudo apt update
```

<a id="setting-up-a-mirror"></a>

## Setting up a Mirror

The ROS infrastructure uses `rsync` to distribute packages.
To create a local mirror of the ROS 2 repositories:

1. **Storage Requirement:** Ensure you have at least 500GB of available disk space.
2. **Sync Command:** Use `rsync` to pull from the official OSUOSL endpoints:

```
# Sync the main ROS 2 repository
rsync -azv rsync.osuosl.org::ros2-main /your/local/path --delete
```

3. **Maintenance:** Set up a `cron` job to sync every 6-12 hours.

<a id="adding-your-mirror-to-this-list"></a>

### Adding your mirror to this list

To be officially listed, your mirror must meet the following requirements:

- Support **HTTPS**.
- Sync at least once every 24 hours.
- Provide a contact email for infrastructure alerts.

Once verified, please open a Pull Request against this page or post in the [Mirrors Discourse](https://discourse.openrobotics.org/c/infrastructure-project/infra-mirrors/).

<a id="mirroring-docs-ros-org"></a>

## Mirroring docs.ros.org

Mirroring the documentation site requires specific configuration to prevent search engine fragmentation.
If you are interested in hosting a regional mirror of the documentation, please **contact the infrastructure team** via Discourse before proceeding.
