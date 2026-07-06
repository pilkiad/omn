---
title: "Topic statistics"
docname: "Concepts/Intermediate/About-Topic-Statistics"
source: "Concepts/Intermediate/About-Topic-Statistics.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](../basic/about-actions.md) | [Client libraries](../basic/about-client-libraries.md) | [Composition](about-composition.md) | [Cross-compilation](about-cross-compilation.md) | [Different ROS 2 middleware vendors](about-different-middleware-vendors.md)

<a id="topic-statistics"></a>

# Topic statistics

Table of Contents

- [Overview](#overview)
- [How statistics are calculated](#how-statistics-are-calculated)
- [Types of statistics calculated](#types-of-statistics-calculated)
- [Behavior](#behavior)
- [Comparison to ROS 1](#comparison-to-ros-1)
- [Support](#support)

<a id="overview"></a>

## Overview

ROS 2 provides integrated measurement of statistics for messages received by any subscription.
Allowing a user to collect subscription statistics enables them to characterize the performance of their system or aid in diagnosis of any present issues.

The measurements provided are the received message age and received message period.
For each measurement the statistics provided are the average, maximum, minimum, standard deviation, and sample count.
These statistics are calculated in a moving window.

<a id="how-statistics-are-calculated"></a>

## How statistics are calculated

Each statistic set is calculated in constant time and constant memory by using the utilities implemented in the [libstatistics\_collector](https://github.com/ros-tooling/libstatistics_collector) package.
When a new message is received by a subscription, this is a new sample for calculation in the current measurement window.
The average calculated is simply a [moving average](https://en.wikipedia.org/wiki/Moving_average).
The maximum, minimum, and sample count are updated upon receipt of each new sample, whereas the standard deviation is calculated using [Welford’s online algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm).

<a id="types-of-statistics-calculated"></a>

## Types of statistics calculated

- Received message period

  - Units: milliseconds
  - Uses the system clock to measure the period between received messages
- Received message age

  - Units: milliseconds
  - Requires a message to have a timestamp populated in the header field in order to calculate the age of the message as sent from a publisher

<a id="behavior"></a>

## Behavior

By default, Topic Statistics measurements are not enabled.
After enabling this feature for a specific node via the subscription configuration options, both received message age and received message period measurements are enabled for that specific subscription.

The data is published as a [statistics\_msg/msg/MetricsMessage](https://github.com/ros2/rcl_interfaces/blob/jazzy/statistics_msgs/msg/MetricsMessage.msg) at a configurable period (default 1 second) to a configurable topic (default `/statistics`).
Note that the publishing period also serves as the sample collection window period.

Since received message period requires a message timestamp in a header field, empty data is published.
That is, all statistics values are NaN if no timestamp is found.
Publishing NaN values instead of not publishing at all avoids the absence of a signal problem and is meant to explicitly show that a measurement could not be made.

The first sample of each window for the received message period statistic does not yield a measurement.
This is because calculating this statistic requires knowing the time the previous message arrived, so subsequent samples in the window yield measurements.

<a id="comparison-to-ros-1"></a>

## Comparison to ROS 1

Similar to ROS 1 [Topic Statistics](https://wiki.ros.org/Topics#Topic_statistics), both message age and message period are calculated, albeit from the subscription side.
Other ROS 1 metrics, e.g., the number of dropped messages or traffic volume, are currently not provided.

<a id="support"></a>

## Support

This feature is currently supported in ROS 2 Foxy for C++ only (rclcpp).
Future work and improvements, such as Python support, can be found
[here](https://github.com/ros2/ros2/issues/917).
