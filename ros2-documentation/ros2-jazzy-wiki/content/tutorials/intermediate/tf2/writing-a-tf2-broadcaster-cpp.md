---
title: "Writing a broadcaster (C++)"
docname: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Cpp"
source: "Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Cpp.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](adding-a-frame-cpp.md) | [Adding a frame (Python)](adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="writing-a-broadcaster-c"></a>

# Writing a broadcaster (C++)

**Goal:** Learn how to broadcast the state of a robot to tf2.

**Tutorial level:** Intermediate

**Time:** 15 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Write the broadcaster node](#write-the-broadcaster-node)
  - [2 Write the launch file](#write-the-launch-file)
  - [3 Build](#build)
  - [4 Run](#run)
- [Summary](#summary)

<a id="background"></a>

## Background

In the next two tutorials we will write the code to reproduce the demo from the [Introduction to tf2](introduction-to-tf2.md) tutorial.
After that, the following tutorials focus on extending the demo with more advanced tf2 features, including the usage of timeouts in transformation lookups and time travel.

<a id="prerequisites"></a>

## Prerequisites

This tutorial assumes you have a working knowledge of ROS 2 and you have completed the [Introduction to tf2 tutorial](introduction-to-tf2.md) and [tf2 static broadcaster tutorial (C++)](writing-a-tf2-static-broadcaster-cpp.md).
We’ll be reusing the `learning_tf2_cpp` package from that last tutorial.

In previous tutorials, you learned how to [create a workspace](../../beginner-client-libraries/creating-a-workspace.md) and [create a package](../../beginner-client-libraries/creating-your-first-ros2-package.md).

<a id="tasks"></a>

## Tasks

<a id="write-the-broadcaster-node"></a>

### 1 Write the broadcaster node

Let’s first create the source files.
Go to the `learning_tf2_cpp` package we created in the previous tutorial.
Inside the `src` directory download the example broadcaster code by entering the following command:

Linux

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_broadcaster.cpp
```

macOS

```
$ wget https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_broadcaster.cpp
```

Windows

In a Windows command line prompt:

```
$ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_broadcaster.cpp -o turtle_tf2_broadcaster.cpp
```

Or in powershell:

```
$ curl https://raw.githubusercontent.com/ros/geometry_tutorials/jazzy/turtle_tf2_cpp/src/turtle_tf2_broadcaster.cpp -o turtle_tf2_broadcaster.cpp
```

Open the file using your preferred text editor.

```
#include <functional>
#include <memory>
#include <sstream>
#include <string>

#include "geometry_msgs/msg/transform_stamped.hpp"
#include "rclcpp/rclcpp.hpp"
#include "tf2/LinearMath/Quaternion.hpp"
#include "tf2_ros/transform_broadcaster.hpp"
#include "turtlesim/msg/pose.hpp"

class FramePublisher : public rclcpp::Node
{
public:
  FramePublisher()
  : Node("turtle_tf2_frame_publisher")
  {
    // Declare and acquire `turtlename` parameter
    turtlename_ = this->declare_parameter<std::string>("turtlename", "turtle");

    // Initialize the transform broadcaster
    tf_broadcaster_ =
      std::make_unique<tf2_ros::TransformBroadcaster>(*this);

    // Subscribe to a turtle{1}{2}/pose topic and call handle_turtle_pose
    // callback function on each message
    std::ostringstream stream;
    stream << "/" << turtlename_.c_str() << "/pose";
    std::string topic_name = stream.str();

    auto handle_turtle_pose = [this](const std::shared_ptr<const turtlesim::msg::Pose> msg){
        geometry_msgs::msg::TransformStamped t;

        // Read message content and assign it to
        // corresponding tf variables
        t.header.stamp = this->get_clock()->now();
        t.header.frame_id = "world";
        t.child_frame_id = turtlename_.c_str();

        // Turtle only exists in 2D, thus we get x and y translation
        // coordinates from the message and set the z coordinate to 0
        t.transform.translation.x = msg->x;
        t.transform.translation.y = msg->y;
        t.transform.translation.z = 0.0;

        // For the same reason, turtle can only rotate around one axis
        // and this why we set rotation in x and y to 0 and obtain
        // rotation in z axis from the message
        tf2::Quaternion q;
        q.setRPY(0, 0, msg->theta);
        t.transform.rotation.x = q.x();
        t.transform.rotation.y = q.y();
        t.transform.rotation.z = q.z();
        t.transform.rotation.w = q.w();

        // Send the transformation
        tf_broadcaster_->sendTransform(t);
    };
    subscription_ = this->create_subscription<turtlesim::msg::Pose>(
      topic_name, 10,
      handle_turtle_pose);
  }

private:
  rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscription_;
  std::unique_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
  std::string turtlename_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<FramePublisher>());
  rclcpp::shutdown();
  return 0;
}
```

<a id="examine-the-code"></a>

#### 1.1 Examine the code

Now, let’s take a look at the code that is relevant to publishing the turtle pose to tf2.
Firstly, we define and acquire a single parameter `turtlename`, which specifies a turtle name, e.g. `turtle1` or `turtle2`.

```
turtlename_ = this->declare_parameter<std::string>("turtlename", "turtle");
```

Afterward, the node subscribes to topic `turtleX/pose` and runs function `handle_turtle_pose` on every incoming message.

```
subscription_ = this->create_subscription<turtlesim::msg::Pose>(
  topic_name, 10,
  handle_turtle_pose);
```

Now, we create a `TransformStamped` object and give it the appropriate metadata.

1. We need to give the transform being published a timestamp, and we’ll just stamp it with the current time by calling `this->get_clock()->now()`.
   This will return the current time used by the `Node`.
2. Then we need to set the name of the parent frame of the link we’re creating, in this case `world`.
3. Finally, we need to set the name of the child node of the link we’re creating, in this case this is the name of the turtle itself.

The handler function for the turtle pose message broadcasts this turtle’s translation and rotation, and publishes it as a transform from frame `world` to frame `turtleX`.

```
geometry_msgs::msg::TransformStamped t;

// Read message content and assign it to
// corresponding tf variables
t.header.stamp = this->get_clock()->now();
t.header.frame_id = "world";
t.child_frame_id = turtlename_.c_str();
```

Here we copy the information from the 3D turtle pose into the 3D transform.

```
// Turtle only exists in 2D, thus we get x and y translation
// coordinates from the message and set the z coordinate to 0
t.transform.translation.x = msg->x;
t.transform.translation.y = msg->y;
t.transform.translation.z = 0.0;

// For the same reason, turtle can only rotate around one axis
// and this why we set rotation in x and y to 0 and obtain
// rotation in z axis from the message
tf2::Quaternion q;
q.setRPY(0, 0, msg->theta);
t.transform.rotation.x = q.x();
t.transform.rotation.y = q.y();
t.transform.rotation.z = q.z();
t.transform.rotation.w = q.w();
```

Finally we take the transform that we constructed and pass it to the `sendTransform` method of the `TransformBroadcaster` that will take care of broadcasting.

```
// Send the transformation
tf_broadcaster_->sendTransform(t);
```

<a id="cmakelists-txt"></a>

#### 1.2 CMakeLists.txt

Navigate one level back to the `learning_tf2_cpp` directory, where the `CMakeLists.txt` and `package.xml` files are located.

Now open the `CMakeLists.txt` add the executable and name it `turtle_tf2_broadcaster`, which you’ll use later with `ros2 run`.

```
add_executable(turtle_tf2_broadcaster src/turtle_tf2_broadcaster.cpp)
ament_target_dependencies(
    turtle_tf2_broadcaster
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
    turtle_tf2_broadcaster
    DESTINATION lib/${PROJECT_NAME})
```

<a id="write-the-launch-file"></a>

### 2 Write the launch file

Now create a launch file for this demo.
Create a `launch` folder in the `src/learning_tf2_cpp` directory.
With your text editor, create a new file called `turtle_tf2_demo_launch` with extension `.py`, `.xml`, or `.yaml` in the `launch` folder, and add the following lines:

XML

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" />
  <node pkg="learning_tf2_cpp" exec="turtle_tf2_broadcaster" name="broadcaster1">
    <param name="turtlename" value="turtle1" />
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
```

Python

```
from launch import LaunchDescription
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
    ])
```

<a id="id1"></a>

#### 2.1 Examine the code

Let’s examine the launch file structure.
Each format has its own way of setting up the launch file:

XML

XML launch files start with an XML declaration and a root `<launch>` element.

```
<?xml version="1.0" encoding="UTF-8"?>
<launch>
```

YAML

YAML launch files start with a YAML version declaration and a `launch:` key.

```
%YAML 1.2
---
launch:
```

Python

In Python launch files, we first import required modules from the `launch` and `launch_ros` packages.
It should be noted that `launch` is a generic launching framework (not ROS 2 specific) and `launch_ros` has ROS 2 specific things, like nodes that we import here.

```
from launch import LaunchDescription
from launch_ros.actions import Node
```

Now we run our nodes that start the turtlesim simulation and broadcast `turtle1` state to the tf2 using our `turtle_tf2_broadcaster` node.

XML

```
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" />
  <node pkg="learning_tf2_cpp" exec="turtle_tf2_broadcaster" name="broadcaster1">
    <param name="turtlename" value="turtle1" />
  </node>
```

YAML

```
  - node:
      pkg: "turtlesim"
      exec: "turtlesim_node"
      name: "sim"
  - node:
      pkg: "learning_tf2_cpp"
```

Python

```
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
    ])
```

<a id="add-dependencies"></a>

#### 2.2 Add dependencies

Navigate one level back to the `learning_tf2_cpp` directory, where the `CMakeLists.txt` and `package.xml` files are located.

Open `package.xml` with your text editor.
Add the following dependencies corresponding to your launch file’s import statements:

```
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

This declares the additional required `launch` and `launch_ros` dependencies when its code is executed.

Make sure to save the file.

<a id="id2"></a>

#### 2.3 CMakeLists.txt

Reopen `CMakeLists.txt` and add the line so that the launch files from the `launch/` folder will be installed.

```
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})
```

You can learn more about creating launch files in [this tutorial](../launch/creating-launch-files.md).

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

Now run the launch file that will start the turtlesim simulation node and `turtle_tf2_broadcaster` node:

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

In the second terminal window type the following command:

```
$ ros2 run turtlesim turtle_teleop_key
```

You will now see that the turtlesim simulation have started with one turtle that you can control.

![../../../../_images/turtlesim_broadcast.png](../../../../assets/images/turtlesim_broadcast.png)

Now, use the `tf2_echo` tool to check if the turtle pose is actually getting broadcast to tf2:

```
$ ros2 run tf2_ros tf2_echo world turtle1
```

This should show you the pose of the first turtle.
Drive around the turtle using the arrow keys (make sure your `turtle_teleop_key` terminal window is active, not your simulator window).
In your console output you will see something similar to this:

```
At time 1625137663.912474878
- Translation: [5.276, 7.930, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.934, -0.357]
At time 1625137664.950813527
- Translation: [3.750, 6.563, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.934, -0.357]
At time 1625137665.906280726
- Translation: [2.320, 5.282, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.934, -0.357]
At time 1625137666.850775673
- Translation: [2.153, 5.133, 0.000]
- Rotation: in Quaternion [0.000, 0.000, -0.365, 0.931]
```

If you run `tf2_echo` for the transform between the `world` and `turtle2`, you should not see a transform, because the second turtle is not there yet.
However, as soon as we add the second turtle in the next tutorial, the pose of `turtle2` will be broadcast to tf2.

<a id="summary"></a>

## Summary

In this tutorial you learned how to broadcast the pose of the robot (position and orientation of the turtle) to tf2 and how to use the `tf2_echo` tool.
To actually use the transforms broadcasted to tf2, you should move on to the next tutorial about creating a [tf2 listener](writing-a-tf2-listener-cpp.md).
