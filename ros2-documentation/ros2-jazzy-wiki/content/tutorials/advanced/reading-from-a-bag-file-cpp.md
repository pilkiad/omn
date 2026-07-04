---
title: "Reading from a bag file (C++)"
docname: "Tutorials/Advanced/Reading-From-A-Bag-File-CPP"
source: "Tutorials/Advanced/Reading-From-A-Bag-File-CPP.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="reading-from-a-bag-file-c"></a>

# Reading from a bag file (C++)

**Goal:** Read data from a bag without using the CLI.

**Tutorial level:** Advanced

**Time:** 10 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a Package](#create-a-package)
  - [2 Write the C++ Reader](#write-the-c-reader)
  - [3 Build and run](#build-and-run)
- [Summary](#summary)

<a id="background"></a>

## Background

`rosbag2` doesn’t just provide the `ros2 bag` command line tool.
It also provides a C++ API for reading from and writing to a bag from your own source code.
This allows you to read the contents from a bag without having to play the bag, which can sometimes be useful.

<a id="prerequisites"></a>

## Prerequisites

You should have the `rosbag2` packages installed as part of your regular ROS 2 setup.

If you need to install ROS 2, see the [Installation instructions](../../installation/overview.md).

You should have already completed the [basic ROS 2 bag tutorial](../beginner-cli-tools/recording-and-playing-back-data.md), and we will be using the `subset` bag you created there.

<a id="tasks"></a>

## Tasks

<a id="create-a-package"></a>

### 1 Create a Package

Open a new terminal and [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md) so that `ros2` commands will work.

In a new or existing [workspace](../beginner-client-libraries/creating-a-workspace.md#new-directory), navigate to the `src` directory and create
a new package:

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 bag_reading_cpp --dependencies rclcpp rosbag2_transport turtlesim
```

Your terminal will return a message verifying the creation of your package `bag_reading_cpp` and all its necessary files and folders.
The `--dependencies` argument will automatically add the necessary dependency lines to `package.xml` and `CMakeLists.txt`.
In this case, the package will use the `rosbag2_transport` package as well as the `rclcpp` package.
A dependency on the `turtlesim` package is also required for working with the custom turtlesim messages.

<a id="update-package-xml"></a>

#### 1.1 Update `package.xml`

Because you used the `--dependencies` option during package creation, you don’t have to manually add dependencies to `package.xml` or `CMakeLists.txt`.
As always, though, make sure to add the description, maintainer email and name, and license information to `package.xml`.

```
<description>C++ bag reading tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

<a id="write-the-c-reader"></a>

### 2 Write the C++ Reader

Inside your package’s `src` directory, create a new file called `simple_bag_reader.cpp` and paste the following code into it.

```
#include <chrono>
#include <functional>
#include <iostream>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "rclcpp/serialization.hpp"
#include "rosbag2_transport/reader_writer_factory.hpp"
#include "turtlesim/msg/pose.hpp"

using namespace std::chrono_literals;

class PlaybackNode : public rclcpp::Node
{
  public:
    PlaybackNode(const std::string & bag_filename)
    : Node("playback_node")
    {
      publisher_ = this->create_publisher<turtlesim::msg::Pose>("/turtle1/pose", 10);

      timer_ = this->create_wall_timer(100ms,
          [this](){return this->timer_callback();}
      );

      rosbag2_storage::StorageOptions storage_options;
      storage_options.uri = bag_filename;
      reader_ = rosbag2_transport::ReaderWriterFactory::make_reader(storage_options);
      reader_->open(storage_options);
    }

  private:
    void timer_callback()
    {
      while (reader_->has_next()) {
        rosbag2_storage::SerializedBagMessageSharedPtr msg = reader_->read_next();

        if (msg->topic_name != "/turtle1/pose") {
          continue;
        }

        rclcpp::SerializedMessage serialized_msg(*msg->serialized_data);
        turtlesim::msg::Pose::SharedPtr ros_msg = std::make_shared<turtlesim::msg::Pose>();

        serialization_.deserialize_message(&serialized_msg, ros_msg.get());

        publisher_->publish(*ros_msg);
        std::cout << '(' << ros_msg->x << ", " << ros_msg->y << ")\n";

        break;
      }
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<turtlesim::msg::Pose>::SharedPtr publisher_;

    rclcpp::Serialization<turtlesim::msg::Pose> serialization_;
    std::unique_ptr<rosbag2_cpp::Reader> reader_;
};

int main(int argc, char ** argv)
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <bag>" << std::endl;
    return 1;
  }

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PlaybackNode>(argv[1]));
  rclcpp::shutdown();

  return 0;
}
```

<a id="examine-the-code"></a>

#### 2.1 Examine the code

The `#include` statements at the top are the package dependencies.
Note the inclusion of headers from the `rosbag2_transport` package for the functions and structures necessary to work with bag files.

The next line creates the node which will read from the bag file and play back the data.

```
class PlaybackNode : public rclcpp::Node
```

Now, we can create a timer callback which will run at 10 hz.
Our goal is to replay one message to the `/turtle1/pose` topic each time the callback is run.
Note the constructor takes a path to the bag file as a parameter.

```
public:
  PlaybackNode(const std::string & bag_filename)
  : Node("playback_node")
  {
    publisher_ = this->create_publisher<turtlesim::msg::Pose>("/turtle1/pose", 10);

    timer_ = this->create_wall_timer(100ms,
      [this](){return this->timer_callback();}
    );
```

We also open the bag in the constructor.
The `rosbag2_transport::ReaderWriterFactory` is a class that can construct a compressed or uncompressed reader or writer based on the storage options.

```
rosbag2_storage::StorageOptions storage_options;
storage_options.uri = bag_filename;
reader_ = rosbag2_transport::ReaderWriterFactory::make_reader(storage_options);
reader_->open(storage_options);
```

Now, inside our timer callback, we loop through messages in the bag until we read a message recorded from our desired topic.
Note that the serialized message has timestamp metadata in addition to the topic name.

```
void timer_callback()
{
  while (reader_->has_next()) {
    rosbag2_storage::SerializedBagMessageSharedPtr msg = reader_->read_next();

    if (msg->topic_name != "/turtle1/pose") {
      continue;
    }
```

We then construct an `rclcpp::SerializedMessage` object from the serialized data we just read.
Additionally, we need to create a ROS 2 deserialized message which will hold the result of our deserialization.
Then, we can pass both these objects to the `rclcpp::Serialization::deserialize_message` method.

```
rclcpp::SerializedMessage serialized_msg(*msg->serialized_data);
turtlesim::msg::Pose::SharedPtr ros_msg = std::make_shared<turtlesim::msg::Pose>();

serialization_.deserialize_message(&serialized_msg, ros_msg.get());
```

Finally, we publish the deserialized message and print out the xy coordinate to the terminal.
We also break out of the loop so that we publish the next message during the next timer callback.

```
  publisher_->publish(*ros_msg);
  std::cout << '(' << ros_msg->x << ", " << ros_msg->y << ")\n";

  break;
}
```

We must also declare the private variables used throughout the node.

```
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<turtlesim::msg::Pose>::SharedPtr publisher_;

  rclcpp::Serialization<turtlesim::msg::Pose> serialization_;
  std::unique_ptr<rosbag2_cpp::Reader> reader_;
};
```

Lastly, we create the main function which will check that the user passes an argument for the bag file path and spins our node.

```
int main(int argc, char ** argv)
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <bag>" << std::endl;
    return 1;
  }

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PlaybackNode>(argv[1]));
  rclcpp::shutdown();

  return 0;
}
```

<a id="add-executable"></a>

#### 2.2 Add executable

Now open the `CMakeLists.txt` file.

Below the dependencies block, which contains `find_package(rosbag2_transport REQUIRED)`, add the following lines of code.

```
add_executable(simple_bag_reader src/simple_bag_reader.cpp)
ament_target_dependencies(simple_bag_reader rclcpp rosbag2_transport turtlesim)

install(TARGETS
  simple_bag_reader
  DESTINATION lib/${PROJECT_NAME}
)
```

<a id="build-and-run"></a>

### 3 Build and run

Navigate back to the root of your workspace and build your new package.

Linux

```
$ colcon build --packages-select bag_reading_cpp
```

macOS

```
$ colcon build --packages-select bag_reading_cpp
```

Windows

```
$ colcon build --merge-install --packages-select bag_reading_cpp
```

Next, source the setup files.

Linux

```
$ source install/setup.bash
```

macOS

```
$ source install/setup.bash
```

Windows

```
$ call install/setup.bat
```

Now, run the script.
Make sure to replace `/path/to/subset` with the path to your `subset` bag.

```
$ ros2 run bag_reading_cpp simple_bag_reader /path/to/subset
```

You should see the (x, y) coordinates of the turtle printed to the console.

<a id="summary"></a>

## Summary

You created a C++ executable that reads data from a bag.
You then compiled and ran the executable which printed some information from the bag to the console.
