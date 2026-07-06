---
title: "rosbag2: Overriding QoS Policies"
docname: "How-To-Guides/Overriding-QoS-Policies-For-Recording-And-Playback"
source: "How-To-Guides/Overriding-QoS-Policies-For-Recording-And-Playback.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="rosbag2-overriding-qos-policies"></a>
<a id="ros2bag-qos-override"></a>

# rosbag2: Overriding QoS Policies

**Goal:** Override Ros2Bag QoS profile settings for recording and playback.

Contents

- [Background](#background)
- [Using QoS Overrides](#using-qos-overrides)
- [Example](#example)

<a id="background"></a>

## Background

With the introduction of DDS in ROS 2, Quality of Service (QoS) compatibility for publisher/subscriber nodes needs to be considered when recording and playing back data.
More detail on how QoS works can be found [here](../concepts/intermediate/about-quality-of-service-settings.md).
For the purposes of this guide, it is sufficient to know that only the reliability and durability policies affect whether publishers/subscribers are compatible and can receive data from one other.

Ros2Bag adapts its requested/offered QoS profile when recording/playing data from a topic to prevent dropped messages.
During playback, Ros2bag also attempts to preserve the policy originally offered by the topic.
Certain situations may require specifying explicit QoS profile settings so Ros2Bag can record/playback topics.
These QoS profile overrides can be specified via the CLI using the `--qos-profile-overrides-path` flag.

<a id="using-qos-overrides"></a>

## Using QoS Overrides

The YAML schema for the profile overrides is a dictionary of topic names with key/value pairs for each QoS policy:

```
topic_name: str
  qos_policy_name: str
  ...
  qos_duration: object
    sec: int
    nsec: int
```

If a policy value is not specified, the value will fallback to the default used by Ros2Bag.
If you specify a Duration based policy such as `deadline` or `lifespan`, you will need to specify both seconds and nanoseconds.
Policy values are determined by the policy’s short keys which can be found using `ros2topic` verbs such as `ros2 topic pub --help`.
All values are replicated below for reference.

```
history: [keep_all, keep_last]
depth: int
reliability: [system_default, reliable, best_effort, unknown]
durability: [system_default, transient_local, volatile, unknown]
deadline:
  sec: int
  nsec: int
lifespan:
  sec: int
  nsec: int
liveliness: [system_default, automatic, manual_by_topic, unknown]
liveliness_lease_duration:
  sec: int
  nsec: int
avoid_ros_namespace_conventions: [true, false]
```

<a id="example"></a>

## Example

Consider a topic `/talker` offering a `transient_local` Durability policy.
ROS 2 publishers by default request `volatile` Durability.

```
$ ros2 topic pub -r 0.1 --qos-durability transient_local /talker std_msgs/String "data: Hello World"
```

In order for Ros2Bag to record the data, we would want to override the recording policy for that specific topic like so:

```
# durability_override.yaml
/talker:
  durability: transient_local
  history: keep_all
```

And call it from the CLI:

```
$ ros2 bag record -a -o my_bag --qos-profile-overrides-path durability_override.yaml
```

If we want to playback the bag file but with a different Reliability policy, we can specify one as such;

```
# reliability_override.yaml
/talker:
  reliability: best_effort
  history: keep_all
```

And call it from the CLI:

```
$ ros2 bag play --qos-profile-overrides-path reliability_override.yaml my_bag
```

We can see the results with `ros2 topic`

```
$ ros2 topic echo --qos-reliability best_effort /talker std_msgs/String
```
