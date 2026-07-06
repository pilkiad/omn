---
title: "Writing a listener (C++)"
docname: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Cpp"
source: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Cpp.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](adding-a-frame-cpp.md) | [Adding a frame (Python)](adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-a-listener-c"></a>

# Writing a listener (C++)

**Goal:** Learn how to use tf2 to get access to frame transformations.

**Tutorial level:** Intermediate

**Time:** 10 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Write the listener node](#write-the-listener-node)
  - [2 Update the launch file](#update-the-launch-file)
  - [3 Build](#build)
  - [4 Run](#run)
- [Summary](#summary)

<a id="background"></a>

## Background

In previous tutorials we created a tf2 broadcaster to publish the pose of a turtle to tf2.

In this tutorial we’ll create a tf2 listener to start using tf2.

<a id="prerequisites"></a>

## Prerequisites

This tutorial assumes you have completed the [tf2 static broadcaster tutorial (C++)](writing-a-tf2-static-broadcaster-cpp.md) and the [tf2 broadcaster tutorial (C++)](writing-a-tf2-broadcaster-cpp.md).
In the previous tutorial, we created a `learning_tf2_cpp` package, which is where we will continue working from.

<a id="tasks"></a>

## Tasks

<a id="write-the-listener-node"></a>

### 1 Write the listener node

Let’s first create the source files.
Go to the `learning_tf2_cpp` package we created in the previous tutorial.
Inside the `src` directory download the example listener code by entering the following command:

Linux

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_listener.cpp
```

macOS

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_listener.cpp
```

Windows

In a Windows command line prompt:

```
$ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_listener.cpp -o turtle_tf2_listener.cpp
```

Or in powershell:

```
$ curl https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_listener.cpp -o turtle_tf2_listener.cpp
```

Open the file using your preferred text editor.

```
#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "geometry_msgs/msg/transform_stamped.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "rclcpp/rclcpp.hpp"
#include "tf2/exceptions.hpp"
#include "tf2_ros/transform_listener.hpp"
#include "tf2_ros/buffer.hpp"
#include "turtlesim/srv/spawn.hpp"

using namespace std::chrono_literals;

class FrameListener : public rclcpp::Node
{
public:
  FrameListener()
  : Node("turtle_tf2_frame_listener"),
    turtle_spawning_service_ready_(false),
    turtle_spawned_(false)
  {
    // Declare and acquire `target_frame` parameter
    target_frame_ = this->declare_parameter<std::string>("target_frame", "turtle1");

    tf_buffer_ =
      std::make_unique<tf2_ros::Buffer>(this->get_clock());
    tf_listener_ =
      std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

    // Create a client to spawn a turtle
    spawner_ =
      this->create_client<turtlesim::srv::Spawn>("spawn");

    // Create turtle2 velocity publisher
    publisher_ =
      this->create_publisher<geometry_msgs::msg::Twist>("turtle2/cmd_vel", 1);

    // Call on_timer function every second
    timer_ = this->create_wall_timer(
      1s, [this]() {return this->on_timer();});
  }

private:
  void on_timer()
  {
    // Store frame names in variables that will be used to
    // compute transformations
    std::string fromFrameRel = target_frame_.c_str();
    std::string toFrameRel = "turtle2";

    if (turtle_spawning_service_ready_) {
      if (turtle_spawned_) {
        geometry_msgs::msg::TransformStamped t;

        // Look up for the transformation between target_frame and turtle2 frames
        // and send velocity commands for turtle2 to reach target_frame
        try {
          t = tf_buffer_->lookupTransform(
            toFrameRel, fromFrameRel,
            tf2::TimePointZero);
        } catch (const tf2::TransformException & ex) {
          RCLCPP_INFO(
            this->get_logger(), "Could not transform %s to %s: %s",
            toFrameRel.c_str(), fromFrameRel.c_str(), ex.what());
          return;
        }

        geometry_msgs::msg::Twist msg;

        static const double scaleRotationRate = 1.0;
        msg.angular.z = scaleRotationRate * atan2(
          t.transform.translation.y,
          t.transform.translation.x);

        static const double scaleForwardSpeed = 0.5;
        msg.linear.x = scaleForwardSpeed * sqrt(
          pow(t.transform.translation.x, 2) +
          pow(t.transform.translation.y, 2));

        publisher_->publish(msg);
      } else {
        RCLCPP_INFO(this->get_logger(), "Successfully spawned");
        turtle_spawned_ = true;
      }
    } else {
      // Check if the service is ready
      if (spawner_->service_is_ready()) {
        // Initialize request with turtle name and coordinates
        // Note that x, y and theta are defined as floats in turtlesim/srv/Spawn
        auto request = std::make_shared<turtlesim::srv::Spawn::Request>();
        request->x = 4.0;
        request->y = 2.0;
        request->theta = 0.0;
        request->name = "turtle2";

        // Call request
        using ServiceResponseFuture =
          rclcpp::Client<turtlesim::srv::Spawn>::SharedFuture;
        auto response_received_callback = [this](ServiceResponseFuture future) {
            auto result = future.get();
            if (strcmp(result->name.c_str(), "turtle2") == 0) {
              turtle_spawning_service_ready_ = true;
            } else {
              RCLCPP_ERROR(this->get_logger(), "Service callback result mismatch");
            }
          };
        auto result = spawner_->async_send_request(request, response_received_callback);
      } else {
        RCLCPP_INFO(this->get_logger(), "Service is not ready");
      }
    }
  }

  // Boolean values to store the information
  // if the service for spawning turtle is available
  bool turtle_spawning_service_ready_;
  // if the turtle was successfully spawned
  bool turtle_spawned_;
  rclcpp::Client<turtlesim::srv::Spawn>::SharedPtr spawner_{nullptr};
  rclcpp::TimerBase::SharedPtr timer_{nullptr};
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_{nullptr};
  std::shared_ptr<tf2_ros::TransformListener> tf_listener_{nullptr};
  std::unique_ptr<tf2_ros::Buffer> tf_buffer_;
  std::string target_frame_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<FrameListener>());
  rclcpp::shutdown();
  return 0;
}
```

<a id="examine-the-code"></a>

#### 1.1 Examine the code

To understand how the service behind spawning turtle works, please refer to [writing a simple service and client (C++)](../../beginner-client-libraries/writing-a-simple-cpp-service-and-client.md) tutorial.

Now, let’s take a look at the code that is relevant to get access to frame transformations.
The `tf2_ros` contains a `TransformListener` class that makes the task of receiving transforms easier.

```
#include "tf2_ros/transform_listener.hpp"
```

Here, we create a `TransformListener` object.
Once the listener is created, it starts receiving tf2 transformations over the wire, and buffers them for up to 10 seconds.

```
tf_listener_ =
  std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);
```

Finally, we query the listener for a specific transformation.
We call `lookup_transform` method with following arguments:

1. Target frame
2. Source frame
3. The time at which we want to transform

Providing `tf2::TimePointZero` will just get us the latest available transform.
All this is wrapped in a try-catch block to handle possible exceptions.

```
t = tf_buffer_->lookupTransform(
  toFrameRel, fromFrameRel,
  tf2::TimePointZero);
```

The resulting transformation represents the position and orientation of the target turtle relative to `turtle2`.
The angle between the turtles is then used to calculate a velocity command to follow the target turtle.
For more general information about tf2 see also the [tf2 page in the Concepts section](../../../concepts/intermediate/about-tf2.md).

<a id="cmakelists-txt"></a>

#### 1.2 CMakeLists.txt

Navigate one level back to the `learning_tf2_cpp` directory, where the `CMakeLists.txt` and `package.xml` files are located.

Now open the `CMakeLists.txt` add the executable and name it `turtle_tf2_listener`, which you’ll use later with `ros2 run`.

```
add_executable(turtle_tf2_listener src/turtle_tf2_listener.cpp)
ament_target_dependencies(
    turtle_tf2_listener
    geometry_msgs
    rclcpp
    tf2
    tf2_ros
    turtlesim
)
```

Finally, add the `install(TARGETS…)` section so `ros2 run` can find your executable:

```
install(TARGETS
    turtle_tf2_listener
    DESTINATION lib/${PROJECT_NAME})
```

<a id="update-the-launch-file"></a>

### 2 Update the launch file

Open the launch file called `turtle_tf2_demo_launch` with extension `.py`, `.xml`, or `.yaml` in the `src/learning_tf2_cpp/launch` directory with your text editor, add two new nodes to the launch description, add a launch argument, and add the imports.
The resulting file should look like:

Python

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='learning_tf2_cpp',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),
        Node(
            package='learning_tf2_cpp',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='learning_tf2_cpp',
            executable='turtle_tf2_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])
```

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" />
  <node pkg="learning_tf2_cpp" exec="turtle_tf2_broadcaster" name="broadcaster1">
    <param name="turtlename" value="turtle1" />
  </node>
  <arg name="target_frame" default="turtle1" description="Target frame name." />
  <node pkg="learning_tf2_cpp" exec="turtle_tf2_broadcaster" name="broadcaster2">
    <param name="turtlename" value="turtle2" />
  </node>
  <node pkg="learning_tf2_cpp" exec="turtle_tf2_listener" name="listener">
    <param name="target_frame" value="$(var target_frame)" />
  </node>
</launch>
```

YAML

```
%YAML 1.2
---
launch:
  - node:
      pkg: "turtlesim"
      exec: "turtlesim_node"
      name: "sim"
  - node:
      pkg: "learning_tf2_cpp"
      exec: "turtle_tf2_broadcaster"
      name: "broadcaster1"
      param:
      - name: "turtlename"
        value: "turtle1"
  - arg:
      name: "target_frame"
      default: "turtle1"
      description: "Target frame name."
  - node:
      pkg: "learning_tf2_cpp"
      exec: "turtle_tf2_broadcaster"
      name: "broadcaster2"
      param:
      - name: "turtlename"
        value: "turtle2"
  - node:
      pkg: "learning_tf2_cpp"
      exec: "turtle_tf2_listener"
      name: "listener"
      param:
      - name: "target_frame"
        value: "$(var target_frame)"
```

This will declare a `target_frame` launch argument, start a broadcaster for the second turtle that we will spawn and a listener that will subscribe to those transformations.

<a id="build"></a>

### 3 Build

Run `rosdep` in the root of your workspace to check for missing dependencies.

Linux

```
$ rosdep install -i --from-path src --rosdistro jazzy -y
```

macOS

rosdep only runs on Linux, so you will need to install `geometry_msgs` and `turtlesim` dependencies yourself

Windows

rosdep only runs on Linux, so you will need to install `geometry_msgs` and `turtlesim` dependencies yourself

Still in the root of your workspace, build your package:

Linux

```
$ colcon build --packages-select learning_tf2_cpp
```

macOS

```
$ colcon build --packages-select learning_tf2_cpp
```

Windows

```
$ colcon build --merge-install --packages-select learning_tf2_cpp
```

Open a new terminal, navigate to the root of your workspace, and source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

In a Windows command line prompt:

```
$ call install\setup.bat
```

Or in powershell:

```
$ .\install\setup.ps1
```

<a id="run"></a>

### 4 Run

Now you’re ready to start your full turtle demo:

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

You should see the turtle sim with two turtles.
In the second terminal window type the following command:

```
$ ros2 run turtlesim turtle_teleop_key
```

To see if things work, simply drive around the first turtle using the arrow keys (make sure your terminal window is active, not your simulator window), and you’ll see the second turtle following the first one!

<a id="summary"></a>

## Summary

In this tutorial you learned how to use tf2 to get access to frame transformations.
You also have finished writing your own turtlesim demo that you first tried in [Introduction to tf2](introduction-to-tf2.md) tutorial.
