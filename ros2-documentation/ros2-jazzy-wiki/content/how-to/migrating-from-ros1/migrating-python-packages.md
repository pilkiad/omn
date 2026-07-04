---
title: "Migrating Python Packages Reference"
docname: "How-To-Guides/Migrating-from-ROS1/Migrating-Python-Packages"
source: "How-To-Guides/Migrating-from-ROS1/Migrating-Python-Packages.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](../releasing/first-time-release.md) | [Index Your Packages](../releasing/index-your-packages.md) | [Migrating a C++ Package Example](migrating-cpp-package-example.md) | [Migrating a Python Package Example](migrating-python-package-example.md) | [Migrating C++ Packages Reference](migrating-cpp-packages.md)

<a id="migrating-python-packages-reference"></a>

# Migrating Python Packages Reference

This page is a reference on how to migrate Python packages from ROS 1 to ROS 2.
If this is your first time migrating a Python package, then follow [this guide to migrate an example Python package](migrating-python-package-example.md) first.

Table of Contents

- [Build tool](#build-tool)
- [Build system](#build-system)

  - [Update the files to use *setup.py*](#update-the-files-to-use-setup-py)
- [Update source code](#update-source-code)

  - [Node Initialization](#node-initialization)
  - [ROS Parameters](#ros-parameters)
  - [Creating a Publisher](#creating-a-publisher)
  - [Creating a Subscriber](#creating-a-subscriber)
  - [Creating a Service](#creating-a-service)
  - [Creating a Service Client](#creating-a-service-client)

<a id="build-tool"></a>

## Build tool

Instead of using `catkin_make`, `catkin_make_isolated` or `catkin build` ROS 2 uses the command line tool [colcon](https://design.ros2.org/articles/build_tool.html) to build and install a set of packages.
See the [beginner tutorial](../../tutorials/beginner-client-libraries/colcon-tutorial.md) to get started with `colcon`.

<a id="build-system"></a>

## Build system

For pure Python packages, ROS 2 uses the standard `setup.py` installation mechanism familiar to Python developers.

<a id="update-the-files-to-use-setup-py"></a>

### Update the files to use *setup.py*

If the ROS 1 package uses CMake only to invoke the `setup.py` file and does not contain anything beside Python code (e.g. no messages, services, etc.) it should be converted into a pure Python package in ROS 2:

- Update or add the build type in the `package.xml` file:

  ```
  <export>
    <build_type>ament_python</build_type>
  </export>
  ```
- Remove the `CMakeLists.txt` file
- Update the `setup.py` file to be a standard Python setup script

ROS 2 supports Python 3 only.
While each package can choose to also support Python 2 it must invoke executables with Python 3 if it uses any API provided by other ROS 2 packages.

<a id="update-source-code"></a>

## Update source code

<a id="node-initialization"></a>

### Node Initialization

In ROS 1:

```
rospy.init_node('asdf')

rospy.loginfo('Created node')
```

In ROS 2:

```
rclpy.init(args=sys.argv)
node = rclpy.create_node('asdf')

node.get_logger().info('Created node')
```

<a id="ros-parameters"></a>

### ROS Parameters

In ROS 1:

```
 port = rospy.get_param('port', '/dev/ttyUSB0')
 assert isinstance(port, str), 'port parameter must be a str'

 baudrate = rospy.get_param('baudrate', 115200)
 assert isinstance(baudrate, int), 'baudrate parameter must be an integer'

rospy.logwarn('port: ' + port)
```

In ROS 2:

```
port = node.declare_parameter('port', '/dev/ttyUSB0').value
assert isinstance(port, str), 'port parameter must be a str'

baudrate = node.declare_parameter('baudrate', 115200).value
assert isinstance(baudrate, int), 'baudrate parameter must be an integer'

node.get_logger().warn('port: ' + port)
```

<a id="creating-a-publisher"></a>

### Creating a Publisher

In ROS 1:

```
pub = rospy.Publisher('chatter', String)
# or
pub = rospy.Publisher('chatter', String, queue_size=10)
```

In ROS 2:

```
pub = node.create_publisher(String, 'chatter', rclpy.qos.QoSProfile())
# or
pub = node.create_publisher(String, 'chatter', 10)
```

<a id="creating-a-subscriber"></a>

### Creating a Subscriber

In ROS 1:

```
sub = rospy.Subscriber('chatter', String, callback)
# or
sub = rospy.Subscriber('chatter', String, callback, queue_size=10)
```

In ROS 2:

```
sub = node.create_subscription(String, 'chatter', callback, rclpy.qos.QoSProfile())
# or
sub = node.create_subscription(String, 'chatter', callback, 10)
```

<a id="creating-a-service"></a>

### Creating a Service

In ROS 1:

```
srv = rospy.Service('add_two_ints', AddTwoInts, add_two_ints_callback)
```

In ROS 2:

```
srv = node.create_service(AddTwoInts, 'add_two_ints', add_two_ints_callback)
```

<a id="creating-a-service-client"></a>

### Creating a Service Client

In ROS 1:

```
rospy.wait_for_service('add_two_ints')
add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
resp = add_two_ints(req)
```

In ROS 2:

```
add_two_ints = node.create_client(AddTwoInts, 'add_two_ints')
while not add_two_ints.wait_for_service(timeout_sec=1.0):
    node.get_logger().info('service not available, waiting again...')
resp = add_two_ints.call_async(req)
rclpy.spin_until_future_complete(node, resp)
```

> [!WARNING]
>
> Do not use `rclpy.spin_until_future_complete` in a ROS 2 callback.
> For more details see the [sync deadlock article](../sync-vs-async.md).
