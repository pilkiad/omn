---
title: "How to use ros2_tracing to trace and analyze an application"
docname: "Tutorials/Advanced/ROS2-Tracing-Trace-and-Analyze"
source: "Tutorials/Advanced/ROS2-Tracing-Trace-and-Analyze.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="how-to-use-ros2-tracing-to-trace-and-analyze-an-application"></a>

# How to use ros2\_tracing to trace and analyze an application

This tutorial shows how to use [ros2\_tracing](https://github.com/ros2/ros2_tracing) to trace and analyze a ROS 2 application.
For this tutorial, the application will be [performance\_test](https://gitlab.com/ApexAI/performance_test).

<a id="overview"></a>

## Overview

This tutorial covers:

1. running and tracing a `performance_test` run
2. analyzing the trace data using [tracetools\_analysis](https://github.com/ros-tracing/tracetools_analysis) to plot the callback durations using [Jupyter Notebook](https://jupyter.org/)

<a id="prerequisites"></a>

## Prerequisites

This tutorial is aimed at real-time Linux systems.
See the [real-time system setup tutorial](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md).
However, the tutorial will work if you are using a non-real-time Linux system.

<a id="installing-and-building"></a>

## Installing and building

Install ROS 2 on Linux by following the [installation instructions](../../installation/overview.md).

> [!NOTE]
>
> This tutorial should generally work with all supported Linux distributions.
> However, you might need to adapt some commands.

Install `babeltrace` and `ros2trace`.

```
$ sudo apt-get update
$ sudo apt-get install -y babeltrace ros-jazzy-ros2trace ros-jazzy-tracetools-analysis
```

Source the ROS 2 installation and verify that tracing is enabled:

```
$ source /opt/ros/jazzy/setup.bash
$ ros2 run tracetools status
Tracing enabled
```

Then create a workspace, and clone `performance_test` and `tracetools_analysis`.

```
$ cd ~/
$ mkdir -p tracing_ws/src
$ cd tracing_ws/src/
$ git clone https://gitlab.com/ApexAI/performance_test.git
$ git clone https://github.com/ros-tracing/tracetools_analysis.git -b jazzy
$ cd ..
```

Install dependencies with rosdep.

```
$ rosdep update
$ rosdep install --from-paths src --ignore-src -y --skip-keys test_tracetools
```

Then build and configure `performance_test` for ROS 2.
See its [documentation](https://gitlab.com/ApexAI/performance_test/-/tree/master/performance_test#performance_test).

```
$ colcon build --packages-select performance_test --cmake-args -DPERFORMANCE_TEST_RCLCPP_ENABLED=ON
```

Next, we will run a `performance_test` experiment and trace it.

<a id="tracing"></a>

## Tracing

<a id="step-1-trace"></a>

### Step 1: Trace

In one terminal, source the workspace and set up tracing.
When running the command, a list of ROS 2 userspace events will be printed.
It will also print the path to the directory that will contain the resulting trace (under `~/.ros/tracing`).
In Terminal 1 run:

```
$ cd ~/tracing_ws
$ source install/setup.bash
$ ros2 trace --session-name perf-test --list
```

Press enter to start tracing.

<a id="step-2-run-application"></a>

### Step 2: Run Application

In a second terminal, source the workspace.
In Terminal 2 run:

```
$ cd ~/tracing_ws
$ source install/setup.bash
```

Then run the `performance_test` experiment (or your own application).
We simply create an experiment with a node publishing ~1 MB messages to another node as fast as possible for 60 seconds using the second highest real-time priority so that we don’t interfere with critical kernel threads.
We need to run `performance_test` as `root` to be able to use real-time priorities.
In Terminal 2 run:

```
$ sudo ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60 --use-rt-prio 98
```

If that last command doesn’t work for you (with an error like: “error while loading shared libraries”), run the slightly-different command below.
This is because, for security reasons, we need to manually pass `*PATH` environment variables for some shared libraries to be found (see [this explanation](https://unix.stackexchange.com/a/251374)).
In Terminal 2 run:

```
$ sudo env PATH="$PATH" LD_LIBRARY_PATH="$LD_LIBRARY_PATH" ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60 --use-rt-prio 98
```

> [!NOTE]
>
> If you’re not using a real-time kernel, simply run:
> In Terminal 2 run:
>
> ```
> $ ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60
> ```

<a id="step-3-validate-trace"></a>

### Step 3: Validate Trace

Once the experiment is done, in the first terminal, press enter again to stop tracing.
Use `babeltrace` to quickly look at the resulting trace.

```
$ babeltrace ~/.ros/tracing/perf-test | less
```

The output of the above command is a human-readable version of the raw Common Trace Format (CTF) data, which is a list of trace events.
Each event has a timestamp, an event type, some information on the process that generated the event, and the values of the fields of the given event type.

Use the arrow keys to scroll, or press `q` to exit.

Next, we will analyze the trace.

<a id="analysis"></a>

## Analysis

[tracetools\_analysis](https://github.com/ros-tracing/tracetools_analysis) provides a Python API to easily analyze traces.
We can use it in a [Jupyter notebook](https://jupyter.org/) with [bokeh](https://docs.bokeh.org/en/latest/index.html) to plot the data.
The `tracetools_analysis` repository contains a [few sample notebooks](https://github.com/ros-tracing/tracetools_analysis/tree/jazzy/tracetools_analysis/analysis), including [one notebook to analyze subscription callback durations](https://github.com/ros-tracing/tracetools_analysis/blob/jazzy/tracetools_analysis/analysis/callback_duration.ipynb).

For this tutorial, we will plot the durations of the subscription callback in the subscriber node.

Install Jupyter notebook and bokeh, and then open the sample notebook.

```
$ pip3 install bokeh
$ jupyter notebook ~/tracing_ws/src/tracetools_analysis/tracetools_analysis/analysis/callback_duration.ipynb
```

This will open the notebook in the browser.

Replace the value for the `path` variable in the second cell to the path to the trace directory:

```
path = '~/.ros/tracing/perf-test'
```

Run the notebook by clicking the *Run* button for each cell.
Running the cell that does the trace processing might take a few minutes on the first run, but subsequent runs will be much quicker.

You should get a plot that looks similar to this:

![callback durations result plot](../../../assets/images/ros2_tracing_guide_result_plot.png)

We can see that most of the callbacks take less than 0.01 ms, but there are some outliers taking over 0.02 or 0.03 ms.

<a id="conclusion"></a>

## Conclusion

This tutorial showed how to install tracing-related tools.
Then it showed how to trace a [performance\_test](https://gitlab.com/ApexAI/performance_test) experiment using [ros2\_tracing](https://github.com/ros2/ros2_tracing) and plot the callback durations using [tracetools\_analysis](https://github.com/ros-tracing/tracetools_analysis).

For more trace analyses, take a look at the [other sample notebooks](https://github.com/ros-tracing/tracetools_analysis/tree/jazzy/tracetools_analysis/analysis) and the [tracetools\_analysis API documentation](https://docs.ros.org/en/jazzy/p/tracetools_analysis/).
The [ros2\_tracing design document](https://github.com/ros2/ros2_tracing/blob/jazzy/doc/design_ros_2.md) also contains a lot of information.
