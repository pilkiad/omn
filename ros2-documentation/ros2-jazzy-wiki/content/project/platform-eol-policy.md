---
title: "Platform EOL Policy"
docname: "The-ROS2-Project/Platform-EOL-Policy"
source: "The-ROS2-Project/Platform-EOL-Policy.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "project"
tags: ["ros2", "jazzy", "project"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Project hub](../../wiki/tooling-map.md)
> Related: [Contributing](contributing.md) | [Feature Ideas](feature-ideas.md) | [Features Status](features.md) | [Marketing](marketing.md) | [Metrics](metrics.md)

<a id="platform-eol-policy"></a>
<a id="platformeolpolicy"></a>

# Platform EOL Policy

Table of Contents

- [Policy](#policy)
- [For ROS Bosses](#for-ros-bosses)

[ROS distributions](../releases/overview.md) do not support end-of-life (EOL) platforms, even if the ROS distribution is still active.
This page explains:

- What users of EOL platforms should expect
- What ROS Bosses should do

<a id="policy"></a>

## Policy

Every ROS distribution supports certain **platforms**, such as Windows 11 or Ubuntu 24.04.
**Vendors** of these platforms, such as Microsoft or Canonical, decide how long they will support one of their platforms.
When a vendor decides a platform has reached EOL, they usually stop publishing critical bug and security fixes.
To protect ourselves from potentially unpatched security vulnerabilities, we proactively remove all jobs on EOL platforms from the ROS build farm.

If you are using a platform that is no longer supported by its vendor, you should expect to stop receiving updated ROS packages.
Existing ROS packages will remain available and functional, but they will no longer be updated.
However, ROS Bosses may choose to update packages on an EOL platform in exceptional circumstances.

<a id="for-ros-bosses"></a>

## For ROS Bosses

Before a target platform reaches EOL:

- Make sure the ROS distribution documentation includes EOL dates for any platform that reaches EOL before the ROS distribution.
- Post an announcement about the platform reaching EOL at least 2 syncs (roughly 60-90 days) beforehand so that package maintainers have time to update their packages.
- Open a [pull request disabling buildfarm jobs for that platform](https://github.com/ros2/ros_buildfarm_config) and seek review from the [Infrastructure PMC](https://osralliance.org/wp-content/uploads/2024/03/infrastructure_project_charter.pdf).
- Make one last sync to that platform.

After a target platform reaches EOL:

- Update the ROS distribution docs to state the platform will not receive updated ROS packages.
- Announce that the ROS distribution has dropped support for that platform on Discourse.
- Consider making one last release to that platform if:
  :   - You did not already do so prior to EOL, and
      - The updates seem unlikely to have regressions, and
      - The ROS Buildfarm still has runners for that platform.
- Merge your pull request to disable the buildfarm jobs.
