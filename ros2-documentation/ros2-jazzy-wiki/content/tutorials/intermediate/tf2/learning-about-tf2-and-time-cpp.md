---
title: "Using time (C++)"
docname: "Tutorials/Intermediate/Tf2/Learning-About-Tf2-And-Time-Cpp"
source: "Tutorials/Intermediate/Tf2/Learning-About-Tf2-And-Time-Cpp.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](adding-a-frame-cpp.md) | [Adding a frame (Python)](adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="using-time-c"></a>
<a id="learningabouttf2andtimecpp"></a>

# Using time (C++)

**Goal:** Learn how to get a transform at a specific time and wait for a transform to be available on the tf2 tree using `lookupTransform()` function.

**Tutorial level:** Intermediate

**Time:** 10 minutes

Contents

- [Background](#background)
- [Tasks](#tasks)

  - [1 Update the listener node](#update-the-listener-node)
  - [2 Fix the listener node](#fix-the-listener-node)
  - [3 Check the results](#check-the-results)
- [Summary](#summary)

<a id="background"></a>

## Background

In previous tutorials, we recreated the turtle demo by writing a [tf2 broadcaster](writing-a-tf2-broadcaster-cpp.md) and a [tf2 listener](writing-a-tf2-listener-cpp.md).
We also learned how to [add a new frame to the transformation tree](adding-a-frame-cpp.md) and learned how tf2 keeps track of a tree of coordinate frames.
This tree changes over time, and tf2 stores a time snapshot for every transform (for up to 10 seconds by default).
Until now we used the `lookupTransform()` function to get access to the latest available transforms in that tf2 tree, without knowing at what time that transform was recorded.
This tutorial will teach you how to get a transform at a specific time.

<a id="tasks"></a>

## Tasks

<a id="update-the-listener-node"></a>

### 1 Update the listener node

Let’s go back to where we ended in the [adding a frame tutorial](adding-a-frame-cpp.md).
Go to the `learning_tf2_cpp` package.
Open `turtle_tf2_listener.cpp` and take a look at the `lookupTransform()` call:

```
try {
    t = tf_buffer_->lookupTransform(
       toFrameRel,
       fromFrameRel,
       tf2::TimePointZero);
} catch (const tf2::TransformException & ex) {
```

You can see that we specified a time equal to 0 by calling `tf2::TimePointZero`.

> [!NOTE]
>
> The `tf2` package has it’s own time type `tf2::TimePoint`, which is different from `rclcpp::Time`.
> Many APIs in the package `tf2_ros` automatically convert between `rclcpp::Time` and `tf2::TimePoint`.
>
> `rclcpp::Time(0, 0, this->get_clock()->get_clock_type())` could have been used here, but it would have been converted to `tf2::TimePointZero` anyways.

For tf2, time 0 means “the latest available” transform in the buffer.
Now, change this line to get the transform at the current time, `this->get_clock()->now()`:

```
rclcpp::Time now = this->get_clock()->now();
try {
    t = tf_buffer_->lookupTransform(
        toFrameRel, fromFrameRel,
        now);
} catch (const tf2::TransformException & ex) {
```

Now build the package and try to run the launch file.

```
$ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.xml # .py or .yaml are also acceptable
[INFO] [1629873136.345688064] [listener]: Could not transform turtle2 to turtle1: Lookup would
require extrapolation into the future.  Requested time 1629873136.345539 but the latest data
is at time 1629873136.338804, when looking up transform from frame [turtle1] to frame [turtle2]
```

The output tells you that the frame does not exist or that the data is in the future.

To understand why is this happening we need to understand how buffers work.
Firstly, each listener has a buffer where it stores all the coordinate transforms coming from the different tf2 broadcasters.
Secondly, when a broadcaster sends out a transform, it takes some time before that transform gets into the buffer (usually a couple of milliseconds).
As a result, when you request a frame transform at time “now”, you should wait a few milliseconds for that information to arrive.

<a id="fix-the-listener-node"></a>

### 2 Fix the listener node

tf2 provides a nice tool that will wait until a transform becomes available.
You use this by adding a timeout parameter to `lookupTransform()`.
To fix this, edit your code as shown below (add the last timeout parameter):

```
rclcpp::Time now = this->get_clock()->now();
try {
    t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        now,
        50ms);
} catch (const tf2::TransformException & ex) {
```

The `lookupTransform()` can take four arguments, where the last one is an optional timeout.
It will block for up to that duration waiting for it to timeout.

<a id="check-the-results"></a>

### 3 Check the results

You can now build the package and run the launch file.

XML

```
$ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.xml
```

YAML

```
$ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.yaml
```

Python

```
$ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.py
```

You should notice that `lookupTransform()` will actually block until the transform between the two turtles becomes available (this will usually take a few milliseconds).
Once the timeout has been reached (fifty milliseconds in this case), an exception will be raised only if the transform is still not available.

<a id="summary"></a>

## Summary

In this tutorial, you learned how to acquire a transform at a specific timestamp and how to wait for a transform to be available on the tf2 tree when using the `lookupTransform()` function.
