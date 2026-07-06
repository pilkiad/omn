---
title: "Package Docs"
docname: "Package-Docs"
source: "Package-Docs.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "reference"
tags: ["ros2", "jazzy", "reference"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Reference hub](../../wiki/tooling-map.md)
> Related: [About ROS](../getting-started/about-ros.md) | [Citations](citations.md) | [Concepts](../concepts/overview.md) | [Contact](contact.md) | [Distributions](../releases/overview.md)

<a id="package-docs"></a>

# Package Docs

ROS package documentation, that is to say documentation for specific packages you install via apt or some other tool, can be found in multiple places.
Here is a brief list of where to look for specific ROS package documentation.

- Most ROS 2 packages have their package level documentation [included in this index page](https://docs.ros.org/en/jazzy/p/).
- All ROS 2 package’s documentation is hosted alongside its information on the [ROS Index](https://index.ros.org/).
  Searching for packages on ROS Index will yield their information such as released distributions, `README.md` files, URLs, and other important metadata.

<a id="larger-packages"></a>

## Larger Packages

Larger packages like MoveIt, Nav2, and microROS, are given their own domain or subdomain on ros.org.
Here is a short list.

- [MoveIt](https://moveit.ai/)
- [Navigation2](https://nav2.org/)
- [Control](https://control.ros.org/master/index.html)
- [microROS (embedded systems)](https://micro.ros.org/)

<a id="api-documentation"></a>

## API Documentation

You can find the API level documentation for the ROS client libraries in the Jazzy distribution using the links below:

- [rclcpp - C++ client library](https://docs.ros.org/en/jazzy/p/rclcpp/generated/index.html)
- [rclcpp\_lifecycle - C++ lifecycle library](https://docs.ros.org/en/jazzy/p/rclcpp_lifecycle/generated/index.html)
- [rclcpp\_components - C++ components library](https://docs.ros.org/en/jazzy/p/rclcpp_components/generated/index.html)
- [rclcpp\_action - C++ actions library](https://docs.ros.org/en/jazzy/p/rclcpp_action/generated/index.html)

<a id="adding-your-package-to-docs-ros-org"></a>

## Adding Your Package to docs.ros.org

All released ROS 2 packages are automatically added to docs.ros.org and [ROS Index](https://index.ros.org/).
If you would like to enable or configure your own package please see: [Documenting a ROS 2 package](../how-to/documenting-a-ros-2-package.md).
