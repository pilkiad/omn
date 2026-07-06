---
title: "Logging"
docname: "Tutorials/Demos/Logging-and-logger-configuration"
source: "Tutorials/Demos/Logging-and-logger-configuration.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](service-introspection.md)

<a id="logging"></a>

# Logging

Table of Contents

- [Using log statements in code](#using-log-statements-in-code)

  - [Basic logging](#basic-logging)
  - [Logging only the first time](#logging-only-the-first-time)
  - [Logging all but the first time](#logging-all-but-the-first-time)
  - [Logging throttled](#logging-throttled)
  - [Logging throttled all but the first time](#logging-throttled-all-but-the-first-time)
- [Logging demo](#logging-demo)
- [Logging directory configuration](#logging-directory-configuration)
- [Logger level configuration: programmatically](#logger-level-configuration-programmatically)
- [Logger level configuration: externally](#logger-level-configuration-externally)

  - [Using the logger config component](#using-the-logger-config-component)
- [Logger level configuration: command line](#logger-level-configuration-command-line)

  - [Console output formatting](#console-output-formatting)
  - [Console output colorizing](#console-output-colorizing)
  - [Default stream for console output](#default-stream-for-console-output)
  - [Line buffered console output](#line-buffered-console-output)
- [Setting the log file name prefix](#setting-the-log-file-name-prefix)

See [the logging page](../../concepts/intermediate/about-logging.md) for details on available functionality.

<a id="using-log-statements-in-code"></a>

## Using log statements in code

<a id="basic-logging"></a>

### Basic logging

The following code will output a log message from a ROS 2 node at `DEBUG` severity:

C++

```
// printf style
RCLCPP_DEBUG(node->get_logger(), "My log message %d", 4);

// C++ stream style
RCLCPP_DEBUG_STREAM(node->get_logger(), "My log message " << 4);
```

Python

```
node.get_logger().debug('My log message %d' % (4))
```

Note that in both cases, no trailing newline is added, as the logging infrastructure will automatically add one.

<a id="logging-only-the-first-time"></a>

### Logging only the first time

The following code will output a log message from a ROS 2 node at `INFO` severity, but only the first time it is hit:

C++

```
// printf style
RCLCPP_INFO_ONCE(node->get_logger(), "My log message %d", 4);

// C++ stream style
RCLCPP_INFO_STREAM_ONCE(node->get_logger(), "My log message " << 4);
```

Python

```
num = 4
node.get_logger().info(f'My log message {num}', once=True)
```

<a id="logging-all-but-the-first-time"></a>

### Logging all but the first time

The following code will output a log message from a ROS 2 node at `WARN` severity, but not the very first time it is hit:

C++

```
// printf style
RCLCPP_WARN_SKIPFIRST(node->get_logger(), "My log message %d", 4);

// C++ stream style
RCLCPP_WARN_STREAM_SKIPFIRST(node->get_logger(), "My log message " << 4);
```

Python

```
num = 4
node.get_logger().warning('My log message {0}'.format(num), skip_first=True)
```

<a id="logging-throttled"></a>

### Logging throttled

The following code will output a log message from a ROS 2 node at `ERROR` severity, but no more than once per second.

The interval parameter specifying milliseconds between messages should have an integer data type so it can be converted to a `rcutils_duration_value_t` (an `int64_t`):

C++

```
// printf style
RCLCPP_ERROR_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message %d", 4);

// C++ stream style
RCLCPP_ERROR_STREAM_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message " << 4);

// For now, use the nanoseconds() method to use an existing rclcpp::Duration value, see https://github.com/ros2/rclcpp/issues/1929
RCLCPP_ERROR_STREAM_THROTTLE(node->get_logger(), *node->get_clock(), msg_interval.nanoseconds()/1000000, "My log message " << 4);
```

Python

```
num = 4
node.get_logger().error(f'My log message {num}', throttle_duration_sec=1)
```

<a id="logging-throttled-all-but-the-first-time"></a>

### Logging throttled all but the first time

The following code will output a log message from a ROS 2 node at `DEBUG` severity, no more than once per second, skipping the very first time it is hit:

C++

```
// printf style
RCLCPP_DEBUG_SKIPFIRST_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message %d", 4);

RCLCPP_DEBUG_SKIPFIRST_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message " << 4);
```

Python

```
num = 4
node.get_logger().debug(f'My log message {num}', skip_first=True, throttle_duration_sec=1.0)
```

<a id="logging-demo"></a>

## Logging demo

In this [demo](https://github.com/ros2/demos/tree/jazzy/logging_demo), different types of log calls are shown and the severity level of different loggers is configured locally and externally.

Start the demo with:

```
$ ros2 run logging_demo logging_demo_main
```

Over time you will see output from various log calls with different properties.
To start with you will only see output from log calls with severity `INFO` and above (`WARN`, `ERROR`, `FATAL`).
Note that the first message will only be logged once, though the line is reached on each iteration, as that is a property of the log call used for that message.

<a id="logging-directory-configuration"></a>

## Logging directory configuration

The logging directory can be configured through two environment variables: `ROS_LOG_DIR` and `ROS_HOME`.
The logic is as follows:

- Use `$ROS_LOG_DIR` if `ROS_LOG_DIR` is set and not empty.
- Otherwise, use `$ROS_HOME/log`, using `~/.ros` for `ROS_HOME` if not set or if empty.

For example, to set the logging directory to `~/my_logs`:

Linux

```
$ export ROS_LOG_DIR=~/my_logs
$ ros2 run logging_demo logging_demo_main
```

macOS

```
$ export ROS_LOG_DIR=~/my_logs
$ ros2 run logging_demo logging_demo_main
```

Windows

```
$ set "ROS_LOG_DIR=~/my_logs"
$ ros2 run logging_demo logging_demo_main
```

You will then find the logs under `~/my_logs/`.

Alternatively, you can set `ROS_HOME` and the logging directory will be relative to it (`$ROS_HOME/log`).
`ROS_HOME` is intended to be used by anything that needs a base directory.
Note that `ROS_LOG_DIR` has to be either unset or empty.
For example, with `ROS_HOME` set to `~/my_ros_home`:

Linux

```
$ export ROS_HOME=~/my_ros_home
$ ros2 run logging_demo logging_demo_main
```

macOS

```
$ export ROS_HOME=~/my_ros_home
$ ros2 run logging_demo logging_demo_main
```

Windows

```
$ set "ROS_HOME=~/my_ros_home"
$ ros2 run logging_demo logging_demo_main
```

You will then find the logs under `~/my_ros_home/log/`.

<a id="logger-level-configuration-programmatically"></a>

## Logger level configuration: programmatically

After 10 iterations the level of the logger will be set to `DEBUG`, which will cause additional messages to be logged.

Some of these debug messages cause additional functions/expressions to be evaluated, which were previously skipped as `DEBUG` log calls were not enabled.
See [the source code](https://github.com/ros2/demos/blob/jazzy/logging_demo/src/logger_usage_component.cpp) of the demo for further explanation of the calls used, and see the rclcpp logging documentation for a full list of supported logging calls.

<a id="logger-level-configuration-externally"></a>

## Logger level configuration: externally

ROS 2 nodes have services available to configure the logging level externally at runtime.
These services are disabled by default.
The following code shows how to enable the logger service while creating the node.

C++

```
// Create a node with logger service enabled
auto node = std::make_shared<rclcpp::Node>("NodeWithLoggerService", rclcpp::NodeOptions().enable_logger_service(true));
```

Python

```
# Create a node with logger service enabled
node = Node('NodeWithLoggerService', enable_logger_service=True)
```

If you run one of the nodes as configured above, you will find 2 services when running `ros2 service list`:

```
$ ros2 service list
...
/NodeWithLoggerService/get_logger_levels
/NodeWithLoggerService/set_logger_levels
...
```

- get\_logger\_levels

  > Use this service to get logger levels for specified logger names.
  >
  > Run `ros2 service call` to get logger levels for `NodeWithLoggerService` and `rcl`.
  >
  > ```
  > $ ros2 service call /NodeWithLoggerService/get_logger_levels rcl_interfaces/srv/GetLoggerLevels '{names: ["NodeWithLoggerService", "rcl"]}'
  >
  > requester: making request: rcl_interfaces.srv.GetLoggerLevels_Request(names=['NodeWithLoggerService', 'rcl'])
  >
  > response:
  > rcl_interfaces.srv.GetLoggerLevels_Response(levels=[rcl_interfaces.msg.LoggerLevel(name='NodeWithLoggerService', level=0), rcl_interfaces.msg.LoggerLevel(name='rcl', level=0)])
  > ```
- set\_logger\_levels

  > Use this service to set logger levels for specified logger names.
  >
  > Run `ros2 service call` to set logger levels for `NodeWithLoggerService` and `rcl`.
  >
  > ```
  > $ ros2 service call /NodeWithLoggerService/set_logger_levels rcl_interfaces/srv/SetLoggerLevels '{levels: [{name: "NodeWithLoggerService", level: 20}, {name: "rcl", level: 10}]}'
  >
  > requester: making request: rcl_interfaces.srv.SetLoggerLevels_Request(levels=[rcl_interfaces.msg.LoggerLevel(name='NodeWithLoggerService', level=20), rcl_interfaces.msg.LoggerLevel(name='rcl', level=10)])
  >
  > response:
  > rcl_interfaces.srv.SetLoggerLevels_Response(results=[rcl_interfaces.msg.SetLoggerLevelsResult(successful=True, reason=''), rcl_interfaces.msg.SetLoggerLevelsResult(successful=True, reason='')])
  > ```

There is also demo code showing how to set or get the logger level via the logger service.

> - rclcpp: [demo code](https://github.com/ros2/demos/tree/jazzy/demo_nodes_cpp/src/logging/use_logger_service.cpp)
>
>   > ```
>   > $ ros2 run demo_nodes_cpp use_logger_service
>   > ```
> - rclpy: [demo code](https://github.com/ros2/demos/tree/jazzy/demo_nodes_py/demo_nodes_py/logging/use_logger_service.py)
>
>   > ```
>   > $ ros2 run demo_nodes_py use_logger_service
>   > ```

> [!WARNING]
>
> Currently, there is a limitation that `get_logger_levels` and `set_logger_levels` services are not thread-safe.
> This means that you need to ensure that only one thread is calling the services at a time.
> Please see the details in <https://github.com/ros2/rcutils/issues/397>

<a id="using-the-logger-config-component"></a>

### Using the logger config component

The server that responds to the logger configuration requests has been developed as a component so that it may be added to an existing composition-based system.
For example, if you are using [a container to run your nodes](../intermediate/composition.md), to be able to configure your loggers you only need to request that it additionally load the `logging_demo::LoggerConfig` component into the container.

As an example, if you want to debug the `composition::Talker` demo, you can start the talker as normal with:

Shell 1:

```
$ ros2 run rclcpp_components component_container
```

Shell 2:

```
$ ros2 component load /ComponentManager composition composition::Talker
```

And then when you want to enable debug logging, load the `LoggerConfig` component with:

Shell 2

```
$ ros2 component load /ComponentManager logging_demo logging_demo::LoggerConfig
```

And finally, configure all unset loggers to the debug severity by addressing the empty-named logger.
Note that loggers that have been specifically configured to use a particular severity will not be affected by this call.

Shell 2:

```
$ ros2 service call /config_logger logging_demo/srv/ConfigLogger "{logger_name: '', level: DEBUG}"
```

You should see debug output from any previously unset loggers in the process start to appear, including from the ROS 2 core.

<a id="logger-level-configuration-command-line"></a>

## Logger level configuration: command line

As of the Bouncy ROS 2 release, the severity level for loggers that have not had their severity set explicitly can be configured from the command line.
Restart the demo including the following command line argument:

```
$ ros2 run logging_demo logging_demo_main --ros-args --log-level debug
```

This configures the default severity for any unset logger to the debug severity level.
You should see debug output from loggers from the demo itself and from the ROS 2 core.

The severity level for individual loggers can be configured from the command-line.
Restart the demo including the following command line arguments:

```
$ ros2 run logging_demo logging_demo_main --ros-args --log-level logger_usage_demo:=debug
```

<a id="console-output-formatting"></a>

### Console output formatting

If you would like more or less verbose formatting, you can use the `RCUTILS_CONSOLE_OUTPUT_FORMAT` environment variable.
For example, to additionally get the timestamp and location of the log calls, stop the demo and restart it with the environment variable set:

Linux

```
$ export RCUTILS_CONSOLE_OUTPUT_FORMAT="[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})"
$ ros2 run logging_demo logging_demo_main
```

macOS

```
$ export RCUTILS_CONSOLE_OUTPUT_FORMAT="[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})"
$ ros2 run logging_demo logging_demo_main
```

Windows

```
$ set "RCUTILS_CONSOLE_OUTPUT_FORMAT=[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})"
$ ros2 run logging_demo logging_demo_main
```

You should see the timestamp in seconds and the function name, filename and line number additionally printed with each message.

For more information on configuring the console logger formatting, see the [logger console configuration](../../concepts/intermediate/about-logging.md#logging-configuration-environment-variables)

<a id="console-output-colorizing"></a>

### Console output colorizing

By default, the output is colorized when it’s targeting a terminal.
If you would like to force enabling or disabling it, you can use the `RCUTILS_COLORIZED_OUTPUT` environment variable.
For example:

Linux

```
$ export RCUTILS_COLORIZED_OUTPUT=0  # 1 for forcing it
$ ros2 run logging_demo logging_demo_main
```

macOS

```
$ export RCUTILS_COLORIZED_OUTPUT=0  # 1 for forcing it
$ ros2 run logging_demo logging_demo_main
```

Windows

```
$ set "RCUTILS_COLORIZED_OUTPUT=0" :: 1 for forcing it
$ ros2 run logging_demo logging_demo_main
```

You should see that debug, warn, error and fatal logs aren’t colorized now.

> [!NOTE]
>
> In Linux and MacOS forcing colorized output means that if you redirect the output to a file, the ansi escape color codes will appear on it.
> In windows the colorization method relies on console APIs.
> If it is forced you will get a new warning saying that colorization failed.
> The default behavior already checks if the output is a console or not, so forcing colorization is not recommended.

> [!NOTE]
>
> If you start several nodes via `ros2 launch`, no node has an active terminal attached to it (unless you set `emulate_tty=True`).
> This means that to get colorized output for `ros2 launch`, you need to set `RCUTILS_COLORIZED_OUTPUT=1` explicitly.

<a id="default-stream-for-console-output"></a>

### Default stream for console output

In Foxy and later, the output from all debug levels goes to stderr by default.
It is possible to force all output to go to stdout by setting the `RCUTILS_LOGGING_USE_STDOUT` environment variable to `1`.
For example:

Linux

```
$ export RCUTILS_LOGGING_USE_STDOUT=1
```

macOS

```
$ export RCUTILS_LOGGING_USE_STDOUT=1
```

Windows

```
$ set "RCUTILS_LOGGING_USE_STDOUT=1"
```

<a id="line-buffered-console-output"></a>

### Line buffered console output

By default, all logging output is unbuffered.
You can force it to be buffered by setting the `RCUTILS_LOGGING_BUFFERED_STREAM` environment variable to 1.
For example:

Linux

```
$ export RCUTILS_LOGGING_BUFFERED_STREAM=1
```

macOS

```
$ export RCUTILS_LOGGING_BUFFERED_STREAM=1
```

Windows

```
$ set "RCUTILS_LOGGING_BUFFERED_STREAM=1"
```

Then run:

```
$ ros2 run logging_demo logging_demo_main
```

<a id="setting-the-log-file-name-prefix"></a>

## Setting the log file name prefix

By default, the log file name is based on the executable file name followed by process ID and system timestamp on file creation.
You can change the log file name prefix to one of your choice using the `--log-file-name` command line argument:

```
$ ros2 run demo_nodes_cpp talker --ros-args --log-file-name filename
```

This configures the log file name prefix to `filename`, instead of the executable file name (which is `talker` in this case).
