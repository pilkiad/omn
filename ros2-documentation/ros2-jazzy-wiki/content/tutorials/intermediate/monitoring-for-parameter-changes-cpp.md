---
title: "Monitoring for parameter changes (C++)"
docname: "Tutorials/Intermediate/Monitoring-For-Parameter-Changes-CPP"
source: "Tutorials/Intermediate/Monitoring-For-Parameter-Changes-CPP.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="monitoring-for-parameter-changes-c"></a>

# Monitoring for parameter changes (C++)

**Goal:** Learn to use the ParameterEventHandler class to monitor and respond to parameter changes.

**Tutorial level:** Intermediate

**Time:** 20 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a package](#create-a-package)
  - [2 Write the C++ node](#write-the-c-node)
  - [3 Build and run](#build-and-run)
- [Extensions](#extensions)

  - [Monitor changes to another node’s parameters](#monitor-changes-to-another-node-s-parameters)
  - [Monitor all node parameters simultaneously](#monitor-all-node-parameters-simultaneously)
- [Summary](#summary)
- [Related content](#related-content)

<a id="background"></a>

## Background

Often a node needs to respond to changes to its own parameters or another node’s parameters.
The ParameterEventHandler class makes it easy to listen for parameter changes so that your code can respond to them.
This tutorial will show you how to use the C++ version of the ParameterEventHandler class to monitor for changes to a node’s own parameters as well as changes to another node’s parameters.

<a id="prerequisites"></a>

## Prerequisites

Before starting this tutorial, you should first complete the following tutorials:

- [Understanding parameters](../beginner-cli-tools/understanding-ros2-parameters.md)
- [Using parameters in a class (C++)](../beginner-client-libraries/using-parameters-in-a-class-cpp.md)

<a id="tasks"></a>

## Tasks

In this tutorial, you will create a new package to contain some sample code, write some C++ code to use the ParameterEventHandler class, and test the resulting code.

<a id="create-a-package"></a>

### 1 Create a package

First, open a new terminal and [source your ROS 2 installation](../beginner-cli-tools/configuring-ros2-environment.md) so that `ros2` commands will work.

Follow [these instructions](../beginner-client-libraries/creating-a-workspace.md#new-directory) to create a new workspace named `ros2_ws`.

Recall that packages should be created in the `src` directory, not the root of the workspace.
So, navigate into `ros2_ws/src` and then create a new package there:

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_parameter_event_handler --dependencies rclcpp
```

Your terminal will return a message verifying the creation of your package `cpp_parameter_event_handler` and all its necessary files and folders.

The `--dependencies` argument will automatically add the necessary dependency lines to `package.xml` and `CMakeLists.txt`.

<a id="update-package-xml"></a>

#### 1.1 Update `package.xml`

Because you used the `--dependencies` option during package creation, you don’t have to manually add dependencies to `package.xml` or `CMakeLists.txt`.
As always, though, make sure to add the description, maintainer email and name, and license information to `package.xml`.

```
<description>C++ parameter events client tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

<a id="write-the-c-node"></a>

### 2 Write the C++ node

Inside the `ros2_ws/src/cpp_parameter_event_handler/src` directory, create a new file called `parameter_event_handler.cpp` and paste the following code within:

```
#include <memory>

#include "rclcpp/rclcpp.hpp"

class SampleNodeWithParameters : public rclcpp::Node
{
public:
  SampleNodeWithParameters()
  : Node("node_with_parameters")
  {
    this->declare_parameter("an_int_param", 0);

    // Create a parameter subscriber that can be used to monitor parameter changes
    // (for this node's parameters as well as other nodes' parameters)
    param_subscriber_ = std::make_shared<rclcpp::ParameterEventHandler>(this);

    // Set a callback for this node's integer parameter, "an_int_param"
    auto cb = [this](const rclcpp::Parameter & p) {
        RCLCPP_INFO(
          this->get_logger(), "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
          p.get_name().c_str(),
          p.get_type_name().c_str(),
          p.as_int());
      };
    cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);
  }

private:
  std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
  std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SampleNodeWithParameters>());
  rclcpp::shutdown();

  return 0;
}
```

<a id="examine-the-code"></a>

#### 2.1 Examine the code

The first statement, `#include <memory>` is included so that the code can utilize the std::make\_shared template.
The next, `#include "rclcpp/rclcpp.hpp"` is included to allow the code to reference the various functionality provided by the rclcpp interface, including the ParameterEventHandler class.

After the class declaration, the code defines a class, `SampleNodeWithParameters`.
The constructor for the class declares an integer parameter `an_int_param`, with a default value of 0.
Next, the code creates a `ParameterEventHandler` that will be used to monitor changes to parameters.
Finally, the code creates a lambda function and sets it as the callback to invoke whenever `an_int_param` is updated.

> [!NOTE]
>
> It is very important to save the handle that is returned by `add_parameter_callback`; otherwise, the callback will not be properly registered.

```
SampleNodeWithParameters()
: Node("node_with_parameters")
{
  this->declare_parameter("an_int_param", 0);

  // Create a parameter subscriber that can be used to monitor parameter changes
  // (for this node's parameters as well as other nodes' parameters)
  param_subscriber_ = std::make_shared<rclcpp::ParameterEventHandler>(this);

  // Set a callback for this node's integer parameter, "an_int_param"
  auto cb = [this](const rclcpp::Parameter & p) {
      RCLCPP_INFO(
        this->get_logger(), "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
        p.get_name().c_str(),
        p.get_type_name().c_str(),
        p.as_int());
    };
  cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);
}
```

Following the `SampleNodeWithParameters` is a typical `main` function which initializes ROS, spins the sample node so that it can send and receive messages, and then shuts down after the user enters ^C at the console.

```
int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SampleNodeWithParameters>());
  rclcpp::shutdown();

  return 0;
}
```

<a id="add-executable"></a>

#### 2.2 Add executable

To build this code, first open the `CMakeLists.txt` file and add the following lines of code below the dependency `find_package(rclcpp REQUIRED)`

```
add_executable(parameter_event_handler src/parameter_event_handler.cpp)
ament_target_dependencies(parameter_event_handler rclcpp)

install(TARGETS
  parameter_event_handler
  DESTINATION lib/${PROJECT_NAME}
)
```

<a id="build-and-run"></a>

### 3 Build and run

It’s good practice to run `rosdep` in the root of your workspace (`ros2_ws`) to check for missing dependencies before building:

Linux

```
$ rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
```

macOS

rosdep only runs on Linux, so you can skip ahead to next step.

Windows

rosdep only runs on Linux, so you can skip ahead to next step.

Navigate back to the root of your workspace, `ros2_ws`, and build your new package:

```
$ colcon build --packages-select cpp_parameter_event_handler
```

Open a new terminal, navigate to `ros2_ws`, and source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install/setup.bat
```

Now run the node:

```
$ ros2 run cpp_parameter_event_handler parameter_event_handler
```

The node is now active and has a single parameter and will print a message whenever this parameter is updated.
To test this, open up another terminal and source the ROS setup file as before (`. install/setup.bash`) and execute the following command:

```
$ ros2 param set node_with_parameters an_int_param 43
```

The terminal running the node will display a message similar to the following:

```
[INFO] [1606950498.422461764] [node_with_parameters]: cb: Received an update to parameter "an_int_param" of type integer: "43"
```

The callback we set previously in the node has been invoked and has displayed the new updated value.
You can now terminate the running parameter\_event\_handler sample using ^C in the terminal.

<a id="extensions"></a>

## Extensions

So far, we built and tested a small node that monitors a single parameter owned by the node itself.
Using this node as a base, two other usecases where the ParameterEventHandler can be useful are presented below.

<a id="monitor-changes-to-another-node-s-parameters"></a>

### Monitor changes to another node’s parameters

You can also use the ParameterEventHandler to monitor parameter changes to another node’s parameters.
Let’s update the SampleNodeWithParameters class to also monitor for changes to a parameter in another node.
We will use the parameter\_blackboard demo application to host a double parameter that we will monitor for updates.

First update the constructor to add the following code after the existing code:

```
// Now, add a callback to monitor any changes to the remote node's parameter. In this
// case, we supply the remote node name.
auto cb2 = [this](const rclcpp::Parameter & p) {
    RCLCPP_INFO(
      this->get_logger(), "cb2: Received an update to parameter \"%s\" of type: %s: \"%.02lf\"",
      p.get_name().c_str(),
      p.get_type_name().c_str(),
      p.as_double());
  };
auto remote_node_name = std::string("parameter_blackboard");
auto remote_param_name = std::string("a_double_param");
cb_handle2_ = param_subscriber_->add_parameter_callback(remote_param_name, cb2, remote_node_name);
```

Then add another member variable, `cb_handle2` for the additional callback handle:

```
private:
  std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
  std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
  std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle2_;  // Add this
};
```

In a terminal, navigate back to the root of your workspace, `ros2_ws`, and build your updated package as before:

```
$ colcon build --packages-select cpp_parameter_event_handler
```

Then source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install/setup.bat
```

Now, to test monitoring of remote parameters, first run the newly-built parameter\_event\_handler code:

```
$ ros2 run cpp_parameter_event_handler parameter_event_handler
```

Next, from another terminal (with ROS initialized), run the parameter\_blackboard demo application, as follows:

```
$ ros2 run demo_nodes_cpp parameter_blackboard
```

Finally, from a third terminal (with ROS initialized), let’s set a parameter on the parameter\_blackboard node:

```
$ ros2 param set parameter_blackboard a_double_param 3.45
```

Upon executing this command, you should see output in the parameter\_event\_handler window, indicating that the callback function was invoked upon the parameter update:

```
[INFO] [1606952588.237531933] [node_with_parameters]: cb2: Received an update to parameter "a_double_param" of type: double: "3.45"
```

<a id="monitor-all-node-parameters-simultaneously"></a>

### Monitor all node parameters simultaneously

If you need to monitor multiple nodes or parameters at the same time, it would be cumbersome to have to call `add_parameter_callback` once for each of them.
In this case, you can use `add_parameter_event_callback` to register a single callback that fires when *any* parameters of *any* nodes change.

To do this, first update the SampleNodeWithParameters constructor to add the following code:

```
this->declare_parameter("another_double_param", 0.0);

...

auto event_cb = [this](const rcl_interfaces::msg::ParameterEvent & parameter_event) {
    RCLCPP_INFO(
      this->get_logger(), "Received parameter event from node \"%s\"",
      parameter_event.node.c_str());

    for (const auto& p : parameter_event.changed_parameters) {
      RCLCPP_INFO(
        this->get_logger(), "Inside event: \"%s\" changed to %s",
        p.name.c_str(),
        rclcpp::Parameter::from_parameter_msg(p).value_to_string().c_str());
    };
  };
event_cb_handle_ = param_subscriber_->add_parameter_event_callback(event_cb);
```

This declares a new double parameter `another_double_param` and adds an event callback that will monitor both parameters.
Note that the `parameter_event` is of type [rcl\_interfaces/msg/ParameterEvent](https://docs.ros.org/en/jazzy/p/rcl_interfaces/msg/ParameterEvent.html).
Although it’s not shown in this tutorial, event callbacks can also be used to monitor when parameters are added or deleted.

Finally, don’t forget to add the event callback handle as a private member:

```
private:
  ...
  std::shared_ptr<rclcpp::ParameterEventCallbackHandle> event_cb_handle_;
```

Navigate back to the root of your workspace, `ros2_ws`, and rebuild your updated package as before:

```
$ colcon build --packages-select cpp_parameter_event_handler
```

Then source the setup files:

Linux

```
$ . install/setup.bash
```

macOS

```
$ . install/setup.bash
```

Windows

```
$ call install\setup.bat
```

To test the new event callback, first run the parameter\_event\_handler node:

```
$ ros2 run cpp_parameter_event_handler parameter_event_handler
```

Then, from a second terminal (with ROS sourced), let’s set the original int parameter:

```
$ ros2 param set node_with_parameters an_int_param 44
```

Upon executing this command, you should see both the single-parameter callback, as well as the event callback being fired:

```
[INFO] [1747144403.418980063] [node_with_parameters]: cb: Received an update to parameter "an_int_param" of type integer: "44"
[INFO] [1747144403.419086611] [node_with_parameters]: Received parameter event from node "/node_with_parameters"
[INFO] [1747144403.419114103] [node_with_parameters]: Inside event: "an_int_param" changed to 44
```

Now set the new double parameter:

```
$ ros2 param set node_with_parameters another_double_param 4.4
```

Since no single-parameter callback was added (via `add_parameter_callback`) for the double parameter, we should see only the event callback fire:

```
[INFO] [1747144452.917437113] [node_with_parameters]: Received parameter event from node "/node_with_parameters"
[INFO] [1747144452.917591649] [node_with_parameters]: Inside event: "another_double_param" changed to 4.400000
```

> [!NOTE]
>
> When setting multiple parameters at once, it’s best to use `set_parameters_atomically`, explained in [Parameters](../../concepts/basic/about-parameters.md).
> This way, the event callback is only fired once.

<a id="summary"></a>

## Summary

You created a node with a parameter and used the ParameterEventHandler class to set a callback to monitor changes to that parameter.
You also used the same class to monitor changes to a remote node, and to monitor all parameters in a single event callback.
The ParameterEventHandler is a convenient way to monitor for parameter changes so that you can then respond to the updated values.

<a id="related-content"></a>

## Related content

To learn how to adapt ROS 1 parameter files for ROS 2, see the [Migrating YAML parameter files from ROS 1 to ROS2](../../how-to/migrating-from-ros1/migrating-parameters.md) tutorial.
