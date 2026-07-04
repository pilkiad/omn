---
title: "Writing a simple publisher and subscriber (Python)"
docname: "Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber"
source: "Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="writing-a-simple-publisher-and-subscriber-python"></a>
<a id="pypubsub"></a>

# Writing a simple publisher and subscriber (Python)

**Goal:** Create and run a publisher and subscriber node using Python.

**Tutorial level:** Beginner

**Time:** 20 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a package](#create-a-package)
  - [2 Write the publisher node](#write-the-publisher-node)
  - [3 Write the subscriber node](#write-the-subscriber-node)
  - [4 Build and run](#build-and-run)
- [Summary](#summary)
- [Next steps](#next-steps)
- [Related content](#related-content)

<a id="background"></a>

## Background

In this tutorial, you will create [nodes](../beginner-cli-tools/understanding-ros2-nodes.md) that pass information in the form of string messages to each other over a [topic](../beginner-cli-tools/understanding-ros2-topics.md).
The example used here is a simple “talker” and “listener” system;
one node publishes data and the other subscribes to the topic so it can receive that data.

The code used in these examples can be found [here](https://github.com/ros2/examples/tree/jazzy/rclpy/topics).

<a id="prerequisites"></a>

## Prerequisites

In previous tutorials, you learned how to [create a workspace](creating-a-workspace.md) and [create a package](creating-your-first-ros2-package.md).

A basic understanding of Python is recommended, but not entirely necessary.

<a id="tasks"></a>

## Tasks

<a id="create-a-package"></a>

### 1 Create a package

Open a new terminal and [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md) so that `ros2` commands will work.

Navigate into the `ros2_ws` directory created in a [previous tutorial](creating-a-workspace.md#new-directory).

Recall that packages should be created in the `src` directory, not the root of the workspace.
So, navigate into `ros2_ws/src`, and run the package creation command:

```
$ ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub
```

Your terminal will return a message verifying the creation of your package `py_pubsub` and all its necessary files and folders.

<a id="write-the-publisher-node"></a>

### 2 Write the publisher node

Navigate into `ros2_ws/src/py_pubsub/py_pubsub`.
Recall that this directory is a [Python package](https://docs.python.org/3/tutorial/modules.html#packages) with the same name as the ROS 2 package it’s nested in.

Download the example talker code by entering the following command:

Linux

```
$ wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
```

macOS

```
$ wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
```

Windows

In a Windows command line prompt:

```
$ curl -sk https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py -o publisher_member_function.py
```

Or in powershell:

```
$ curl https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py -o publisher_member_function.py
```

Now there will be a new file named `publisher_member_function.py` adjacent to `__init__.py`.

Open the file using your preferred text editor.

```
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

<a id="examine-the-code"></a>

#### 2.1 Examine the code

The first lines of code after the comments import [rclpy](https://docs.ros.org/en/jazzy/p/rclpy/) so its [Node](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html) class can be used.

```
import rclpy
from rclpy.node import Node
```

The next statement imports the built-in [std\_msgs/msg/String](https://docs.ros.org/en/jazzy/p/std_msgs/msg/String.html) message type that the node uses to structure the data that it passes on the topic.

```
from std_msgs.msg import String
```

These lines represent the node’s dependencies.
Recall that dependencies have to be added to `package.xml`, which you’ll do in the next section.

Next, the `MinimalPublisher` class is created, which inherits from (or is a subclass of) [Node](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html).

```
class MinimalPublisher(Node):
```

Following is the definition of the class’s constructor.
`super().__init__` calls the [Node](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html) class’s constructor and gives it your node name, in this case `minimal_publisher`.

[create\_publisher](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html#rclpy.node.Node.create_publisher) declares that the node publishes messages of type [std\_msgs/msg/String](https://docs.ros.org/en/jazzy/p/std_msgs/msg/String.html) (imported from the `std_msgs.msg` module), over a topic named `topic`, and that the “queue size” is 10.
Queue size is a required [Quality of Service](../../concepts/intermediate/about-quality-of-service-settings.md) (QoS) setting that limits the amount of queued messages if a subscriber is not receiving them fast enough.

Next, [create\_timer](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html#rclpy.node.Node.create_timer) is used to create a callback that executes every 0.5 seconds.
`self.i` is a counter used in the callback.

```
def __init__(self):
    super().__init__('minimal_publisher')
    self.publisher_ = self.create_publisher(String, 'topic', 10)
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
```

`timer_callback` creates a message with the counter value appended, publishes it, and prints it to the console with [get\_logger()](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html#rclpy.node.Node.get_logger)’s [info()](https://docs.ros.org/en/jazzy/p/rclpy/rclpy.impl.rcutils_logger.html#rclpy.impl.rcutils_logger.RcutilsLogger.info) function.

```
def timer_callback(self):
    msg = String()
    msg.data = 'Hello World: %d' % self.i
    self.publisher_.publish(msg)
    self.get_logger().info('Publishing: "%s"' % msg.data)
    self.i += 1
```

Lastly, the main function is defined.

```
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
```

First the [rclpy](https://docs.ros.org/en/jazzy/p/rclpy/) library is initialized, then the node is created, and then it “spins” the node (using [spin()](https://docs.ros.org/en/jazzy/p/rclpy/api/init_shutdown.html#rclpy.spin)) so its callbacks are called.

<a id="add-dependencies"></a>

#### 2.2 Add dependencies

Navigate one level back to the `ros2_ws/src/py_pubsub` directory, where the `setup.py`, `setup.cfg`, and `package.xml` files have been created for you.

Open `package.xml` with your text editor.

As mentioned in the [previous tutorial](creating-your-first-ros2-package.md), make sure to fill in the `<description>`, `<maintainer>` and `<license>` tags:

```
<description>Examples of minimal publisher/subscriber using rclpy</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

After the lines above, add the following dependencies corresponding to your node’s import statements:

```
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

This declares the package needs [rclpy](https://docs.ros.org/en/jazzy/p/rclpy/) and [std\_msgs](https://docs.ros.org/en/jazzy/p/std_msgs/) when its code is executed.

Make sure to save the file.

<a id="add-an-entry-point"></a>

#### 2.3 Add an entry point

Open the `setup.py` file.
Again, match the `maintainer`, `maintainer_email`, `description` and `license` fields to your `package.xml`:

```
maintainer='YourName',
maintainer_email='you@email.com',
description='Examples of minimal publisher/subscriber using rclpy',
license='Apache-2.0',
```

Add the following line within the `console_scripts` brackets of the [entry\_points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) field:

```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
        ],
},
```

Don’t forget to save.

<a id="check-setup-cfg"></a>

#### 2.4 Check setup.cfg

The contents of the `setup.cfg` file should be correctly populated automatically, like so:

```
[develop]
script_dir=$base/lib/py_pubsub
[install]
install_scripts=$base/lib/py_pubsub
```

This is simply telling [setuptools](https://setuptools.pypa.io/en/latest/userguide) to put your executables in `lib`, because `ros2 run` will look for them there.

You could build your package now, source the local setup files, and run it, but let’s create the subscriber node first so you can see the full system at work.

<a id="write-the-subscriber-node"></a>

### 3 Write the subscriber node

Return to `ros2_ws/src/py_pubsub/py_pubsub` to create the next node.
Enter the following code in your terminal:

Linux

```
$ wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
```

macOS

```
$ wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
```

Windows

In a Windows command line prompt:

```
$ curl -sk https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py -o subscriber_member_function.py
```

Or in powershell:

```
$ curl https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py -o subscriber_member_function.py
```

Now the directory should have these files:

```
__init__.py  publisher_member_function.py  subscriber_member_function.py
```

<a id="id4"></a>

#### 3.1 Examine the code

Open the `subscriber_member_function.py` with your text editor.

```
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

The subscriber node’s code is nearly identical to the publisher’s.
The constructor creates a subscriber with the same arguments as the publisher using [create\_subscription](https://docs.ros.org/en/jazzy/p/rclpy/api/node.html#rclpy.node.Node.create_subscription).
Recall from the [topics tutorial](../beginner-cli-tools/understanding-ros2-topics.md) that the topic name and message type used by the publisher and subscriber must match to allow them to communicate.

```
self.subscription = self.create_subscription(
    String,
    'topic',
    self.listener_callback,
    10)
```

The subscriber’s constructor and callback don’t include any timer definition, because it doesn’t need one.
Its callback gets called as soon as it receives a message.

The callback definition simply prints an info message to the console, along with the data it received.
Recall that the publisher defines `msg.data = 'Hello World: %d' % self.i`

```
def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
```

The `main` definition is almost exactly the same, replacing the creation and spinning of the publisher with the subscriber.

```
minimal_subscriber = MinimalSubscriber()

rclpy.spin(minimal_subscriber)
```

Since this node has the same dependencies as the publisher, there’s nothing new to add to `package.xml`.
The `setup.cfg` file can also remain untouched.

<a id="id5"></a>

#### 3.2 Add an entry point

Reopen `setup.py` and add the entry point for the subscriber node below the publisher’s entry point.
The [entry\_points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) field should now look like this:

```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},
```

Make sure to save the file, and then your pub/sub system should be ready.

<a id="build-and-run"></a>

### 4 Build and run

You likely already have the [rclpy](https://docs.ros.org/en/jazzy/p/rclpy/) and [std\_msgs](https://docs.ros.org/en/jazzy/p/std_msgs/) packages installed as part of your ROS 2 system.
It’s good practice to run [rosdep](https://docs.ros.org/en/independent/api/rosdep/html/) (check the [rosdep tutorial](../intermediate/rosdep.md)) in the root of your workspace (`ros2_ws`) to check for missing dependencies before building:

Linux

```
$ rosdep install -i --from-path src --rosdistro jazzy -y
```

macOS

rosdep only runs on Linux, so you can skip ahead to next step.

Windows

rosdep only runs on Linux, so you can skip ahead to next step.

Still in the root of your workspace, `ros2_ws`, build your new package:

Linux

```
$ colcon build --packages-select py_pubsub
```

macOS

```
$ colcon build --packages-select py_pubsub
```

Windows

```
$ colcon build --merge-install --packages-select py_pubsub
```

Open a new terminal, navigate to `ros2_ws`, and source the setup files:

Linux

```
$ source install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install/setup.bat
```

Now run the talker node.
The terminal should start publishing info messages every 0.5 seconds, like so:

```
$ ros2 run py_pubsub talker
[info] [minimal_publisher]: publishing: "hello world: 0"
[info] [minimal_publisher]: publishing: "hello world: 1"
[info] [minimal_publisher]: publishing: "hello world: 2"
[info] [minimal_publisher]: publishing: "hello world: 3"
[info] [minimal_publisher]: publishing: "hello world: 4"
...
```

Open another terminal, source the setup files from inside `ros2_ws` again, and then start the listener node.
The listener will start printing messages to the console, starting at whatever message count the publisher is on at that time, like so:

```
$ ros2 run py_pubsub listener
[INFO] [minimal_subscriber]: I heard: "Hello World: 10"
[INFO] [minimal_subscriber]: I heard: "Hello World: 11"
[INFO] [minimal_subscriber]: I heard: "Hello World: 12"
[INFO] [minimal_subscriber]: I heard: "Hello World: 13"
[INFO] [minimal_subscriber]: I heard: "Hello World: 14"
```

Enter `Ctrl+C` in each terminal to stop the nodes from spinning.

<a id="summary"></a>

## Summary

You created two nodes to publish and subscribe to data over a topic.
Before running them, you added their dependencies and entry points to the package configuration files.

<a id="next-steps"></a>

## Next steps

Next you’ll create another simple ROS 2 package using the service/client model.
Again, you can choose to write it in either [C++](writing-a-simple-cpp-service-and-client.md) or [Python](writing-a-simple-py-service-and-client.md).

<a id="related-content"></a>

## Related content

There are several ways you could write a publisher and subscriber in Python; check out the `minimal_publisher` and `minimal_subscriber` packages in the [ros2/examples](https://github.com/ros2/examples/tree/jazzy/rclpy/topics) repo.
