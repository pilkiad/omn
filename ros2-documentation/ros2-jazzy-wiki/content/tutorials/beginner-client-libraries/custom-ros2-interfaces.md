---
title: "Creating custom msg and srv files"
docname: "Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces"
source: "Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](../miscellaneous/building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](../miscellaneous/building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="creating-custom-msg-and-srv-files"></a>
<a id="custominterfaces"></a>

# Creating custom msg and srv files

**Goal:** Define custom interface files (`.msg` and `.srv`) and use them with Python and C++ nodes.

**Tutorial level:** Beginner

**Time:** 20 minutes

Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)

  - [1 Create a new package](#create-a-new-package)
  - [2 Create custom definitions](#create-custom-definitions)
  - [3 `CMakeLists.txt`](#cmakelists-txt)
  - [4 `package.xml`](#package-xml)
  - [5 Build the `tutorial_interfaces` package](#build-the-tutorial-interfaces-package)
  - [6 Confirm msg and srv creation](#confirm-msg-and-srv-creation)
  - [7 Test the new interfaces](#test-the-new-interfaces)
- [Summary](#summary)
- [Next steps](#next-steps)

<a id="background"></a>

## Background

In previous tutorials you utilized message and service interfaces to learn about [topics](../beginner-cli-tools/understanding-ros2-topics.md), [services](../beginner-cli-tools/understanding-ros2-services.md), and simple publisher/subscriber ([C++](writing-a-simple-cpp-publisher-and-subscriber.md)/[Python](writing-a-simple-py-publisher-and-subscriber.md)) and service/client ([C++](writing-a-simple-cpp-service-and-client.md)/[Python](writing-a-simple-py-service-and-client.md)) nodes.
The interfaces you used were predefined in those cases.

While it’s good practice to use predefined interface definitions, you will probably need to define your own messages and services sometimes as well.
This tutorial will introduce you to the simplest method of creating custom interface definitions.

<a id="prerequisites"></a>

## Prerequisites

You should have a [ROS 2 workspace](creating-a-workspace.md).

This tutorial also uses the packages created in the publisher/subscriber ([C++](writing-a-simple-cpp-publisher-and-subscriber.md) and [Python](writing-a-simple-py-publisher-and-subscriber.md)) and service/client ([C++](writing-a-simple-cpp-service-and-client.md) and [Python](writing-a-simple-py-service-and-client.md)) tutorials to try out the new custom messages.

<a id="tasks"></a>

## Tasks

<a id="create-a-new-package"></a>

### 1 Create a new package

For this tutorial you will be creating custom `.msg` and `.srv` files in their own package, and then utilizing them in a separate package.
Both packages should be in the same workspace.

Since we will use the pub/sub and service/client packages created in earlier tutorials, make sure you are in the same workspace as those packages (`ros2_ws/src`), and then run the following command to create a new package:

```
$ ros2 pkg create --build-type ament_cmake --license Apache-2.0 tutorial_interfaces
```

`tutorial_interfaces` is the name of the new package.
Note that it is, and can only be, an ament\_cmake package, but this doesn’t restrict in which type of packages you can use your messages and services.
You can create your own custom interfaces in an ament\_cmake package, and then use it in a C++ or Python node, which will be covered in the last section.

The `.msg` and `.srv` files are required to be placed in directories called `msg` and `srv` respectively.
Create the directories in `ros2_ws/src/tutorial_interfaces`:

```
$ mkdir msg srv
```

<a id="create-custom-definitions"></a>

### 2 Create custom definitions

<a id="msg-definition"></a>

#### 2.1 msg definition

In the `tutorial_interfaces/msg` directory you just created, make a new file called `Num.msg` with one line of code declaring its data structure:

```
int64 num
```

This is a custom message that transfers a single 64-bit integer called `num`.

Also in the `tutorial_interfaces/msg` directory you just created, make a new file called `Sphere.msg` with the following content:

```
geometry_msgs/Point center
float64 radius
```

This custom message uses a message from another message package (`geometry_msgs/Point` in this case).

<a id="srv-definition"></a>

#### 2.2 srv definition

Back in the `tutorial_interfaces/srv` directory you just created, make a new file called `AddThreeInts.srv` with the following request and response structure:

```
int64 a
int64 b
int64 c
---
int64 sum
```

This is your custom service that requests three integers named `a`, `b`, and `c`, and responds with an integer called `sum`.

<a id="cmakelists-txt"></a>

### 3 `CMakeLists.txt`

To convert the interfaces you defined into language-specific code (like C++ and Python) so that they can be used in those languages, add the following lines to `CMakeLists.txt`:

```
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)
```

> [!NOTE]
>
> The first argument (library name) in the `rosidl_generate_interfaces` must start with the name of the package, e.g., simply `${PROJECT_NAME}` or `${PROJECT_NAME}_suffix`.
> See <https://github.com/ros2/rosidl/issues/441#issuecomment-591025515>.

<a id="package-xml"></a>

### 4 `package.xml`

Because the interfaces rely on `rosidl_default_generators` for generating language-specific code, you need to declare a build tool dependency on it.
`rosidl_default_runtime` is a runtime or execution-stage dependency, needed to be able to use the interfaces later.
The `rosidl_interface_packages` is the name of the dependency group that your package, `tutorial_interfaces`, should be associated with, declared using the `<member_of_group>` tag.

Add the following lines within the `<package>` element of `package.xml`:

```
<depend>geometry_msgs</depend>
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

<a id="build-the-tutorial-interfaces-package"></a>

### 5 Build the `tutorial_interfaces` package

Now that all the parts of your custom interfaces package are in place, you can build the package.
In the root of your workspace (`~/ros2_ws`), run the following command:

Linux

```
$ colcon build --packages-select tutorial_interfaces
```

macOS

```
$ colcon build --packages-select tutorial_interfaces
```

Windows

```
$ colcon build --merge-install --packages-select tutorial_interfaces
```

Now the interfaces will be discoverable by other ROS 2 packages.

<a id="confirm-msg-and-srv-creation"></a>

### 6 Confirm msg and srv creation

In a new terminal, run the following command from within your workspace (`ros2_ws`) to source it:

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

Now you can confirm that your interface creation worked by using the `ros2 interface show` command.
The output you see in your terminal should look similar to the following:

```
$ ros2 interface show tutorial_interfaces/msg/Num
int64 num
```

```
$ ros2 interface show tutorial_interfaces/msg/Sphere
geometry_msgs/Point center
        float64 x
        float64 y
        float64 z
float64 radius
```

```
$ ros2 interface show tutorial_interfaces/srv/AddThreeInts
int64 a
int64 b
int64 c
---
int64 sum
```

<a id="test-the-new-interfaces"></a>

### 7 Test the new interfaces

For this step you can use the packages you created in previous tutorials.
A few simple modifications to the nodes, `CMakeLists.txt` and `package.xml` files will allow you to use your new interfaces.

<a id="testing-num-msg-with-pub-sub"></a>

#### 7.1 Testing `Num.msg` with pub/sub

With a few modifications to the publisher/subscriber package created in a previous tutorial ([C++](writing-a-simple-cpp-publisher-and-subscriber.md) or [Python](writing-a-simple-py-publisher-and-subscriber.md)), you can see `Num.msg` in action.
Since you’ll be changing the standard string msg to a numerical one, the output will be slightly different.

**Publisher**

C++

```
#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/msg/num.hpp"                                            // CHANGE

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<tutorial_interfaces::msg::Num>("topic", 10);  // CHANGE

    auto timer_callback = [this](){
      auto message = tutorial_interfaces::msg::Num();                                   // CHANGE
      message.num = this->count_++;                                                     // CHANGE
      RCLCPP_INFO_STREAM(this->get_logger(), "Publishing: '" << message.num << "'");    // CHANGE
      publisher_->publish(message);
    };
    timer_ = this->create_wall_timer(500ms, timer_callback);
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_;             // CHANGE
  size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
```

Python

```
import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num                            # CHANGE

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Num, 'topic', 10)  # CHANGE
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()                                                # CHANGE
        msg.num = self.i                                           # CHANGE
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.num)       # CHANGE
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**Subscriber**

C++

```
#include <functional>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/msg/num.hpp"                                       // CHANGE

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {
    auto topic_callback = [this](const tutorial_interfaces::msg::Num & msg){     // CHANGE
      RCLCPP_INFO_STREAM(this->get_logger(), "I heard: '" << msg.num << "'");    // CHANGE
    };
    subscription_ = this->create_subscription<tutorial_interfaces::msg::Num>(    // CHANGE
      "topic", 10, topic_callback);
  }

private:
  rclcpp::Subscription<tutorial_interfaces::msg::Num>::SharedPtr subscription_;  // CHANGE
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
```

Python

```
import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num                        # CHANGE

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Num,                                               # CHANGE
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.num)  # CHANGE

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**CMakeLists.txt**

Add the following lines (C++ only):

```
#...

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tutorial_interfaces REQUIRED)                      # CHANGE

add_executable(talker src/publisher_lambda_function.cpp)
ament_target_dependencies(talker rclcpp tutorial_interfaces)    # CHANGE

add_executable(listener src/subscriber_lambda_function.cpp)
ament_target_dependencies(listener rclcpp tutorial_interfaces)  # CHANGE

install(TARGETS
  talker
  listener
  DESTINATION lib/${PROJECT_NAME})

ament_package()
```

**package.xml**

Add the following line:

C++

```
<depend>tutorial_interfaces</depend>
```

Python

```
<exec_depend>tutorial_interfaces</exec_depend>
```

After making the above edits and saving all the changes, build the package:

C++

On Linux/macOS:

```
$ colcon build --packages-select cpp_pubsub
```

On Windows:

```
$ colcon build --merge-install --packages-select cpp_pubsub
```

Python

On Linux/macOS:

```
$ colcon build --packages-select py_pubsub
```

On Windows:

```
$ colcon build --merge-install --packages-select py_pubsub
```

Then open two new terminals, source `ros2_ws` in each, and run:

C++

```
$ ros2 run cpp_pubsub talker
```

```
$ ros2 run cpp_pubsub listener
```

Python

```
$ ros2 run py_pubsub talker
```

```
$ ros2 run py_pubsub listener
```

Since `Num.msg` relays only an integer, the talker should only be publishing integer values, as opposed to the string it published previously:

```
[INFO] [minimal_publisher]: Publishing: '0'
[INFO] [minimal_publisher]: Publishing: '1'
[INFO] [minimal_publisher]: Publishing: '2'
```

<a id="testing-addthreeints-srv-with-service-client"></a>

#### 7.2 Testing `AddThreeInts.srv` with service/client

With a few modifications to the service/client package created in a previous tutorial ([C++](writing-a-simple-cpp-service-and-client.md) or [Python](writing-a-simple-py-service-and-client.md)), you can see `AddThreeInts.srv` in action.
Since you’ll be changing the original two integer request srv to a three integer request srv, the output will be slightly different.

**Service**

C++

```
#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/srv/add_three_ints.hpp"                                        // CHANGE

#include <memory>

void add(const std::shared_ptr<tutorial_interfaces::srv::AddThreeInts::Request> request,     // CHANGE
          std::shared_ptr<tutorial_interfaces::srv::AddThreeInts::Response>       response)  // CHANGE
{
  response->sum = request->a + request->b + request->c;                                      // CHANGE
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request\na: %ld" " b: %ld" " c: %ld",  // CHANGE
                request->a, request->b, request->c);                                         // CHANGE
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "sending back response: [%ld]", (long int)response->sum);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("add_three_ints_server");   // CHANGE

  rclcpp::Service<tutorial_interfaces::srv::AddThreeInts>::SharedPtr service =               // CHANGE
    node->create_service<tutorial_interfaces::srv::AddThreeInts>("add_three_ints",  &add);   // CHANGE

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add three ints.");                     // CHANGE

  rclcpp::spin(node);
  rclcpp::shutdown();
}
```

Python

```
from tutorial_interfaces.srv import AddThreeInts                                                           # CHANGE

import rclpy
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)       # CHANGE

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c                                                   # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))  # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**Client**

C++

```
#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/srv/add_three_ints.hpp"                                       // CHANGE

#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  if (argc != 4) { // CHANGE
      RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "usage: add_three_ints_client X Y Z");      // CHANGE
      return 1;
  }

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("add_three_ints_client");  // CHANGE
  rclcpp::Client<tutorial_interfaces::srv::AddThreeInts>::SharedPtr client =                // CHANGE
    node->create_client<tutorial_interfaces::srv::AddThreeInts>("add_three_ints");          // CHANGE

  auto request = std::make_shared<tutorial_interfaces::srv::AddThreeInts::Request>();       // CHANGE
  request->a = atoll(argv[1]);
  request->b = atoll(argv[2]);
  request->c = atoll(argv[3]);                                                              // CHANGE

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Interrupted while waiting for the service. Exiting.");
      return 0;
    }
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "service not available, waiting again...");
  }

  auto result = client->async_send_request(request);
  // Wait for the result.
  if (rclcpp::spin_until_future_complete(node, result) ==
    rclcpp::FutureReturnCode::SUCCESS)
  {
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Sum: %ld", result.get()->sum);
  } else {
    RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Failed to call service add_three_ints");    // CHANGE
  }

  rclcpp::shutdown();
  return 0;
}
```

Python

```
from tutorial_interfaces.srv import AddThreeInts                            # CHANGE
import sys
import rclpy
from rclpy.node import Node

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddThreeInts.Request()                                   # CHANGE

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.req.c = int(sys.argv[3])                                       # CHANGE
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result of add_three_ints: for %d + %d + %d = %d' %                                # CHANGE
                    (minimal_client.req.a, minimal_client.req.b, minimal_client.req.c, response.sum))  # CHANGE
            break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**CMakeLists.txt**

Add the following lines (C++ only):

```
#...

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tutorial_interfaces REQUIRED)         # CHANGE

add_executable(server src/add_two_ints_server.cpp)
ament_target_dependencies(server
  rclcpp tutorial_interfaces)                      # CHANGE

add_executable(client src/add_two_ints_client.cpp)
ament_target_dependencies(client
  rclcpp tutorial_interfaces)                      # CHANGE

install(TARGETS
  server
  client
  DESTINATION lib/${PROJECT_NAME})

ament_package()
```

**package.xml**

Add the following line:

C++

```
<depend>tutorial_interfaces</depend>
```

Python

```
<exec_depend>tutorial_interfaces</exec_depend>
```

After making the above edits and saving all the changes, build the package:

C++

On Linux/macOS:

```
$ colcon build --packages-select cpp_srvcli
```

On Windows:

```
$ colcon build --merge-install --packages-select cpp_srvcli
```

Python

On Linux/macOS:

```
$ colcon build --packages-select py_srvcli
```

On Windows:

```
$ colcon build --merge-install --packages-select py_srvcli
```

Then open two new terminals, source `ros2_ws` in each, and run:

C++

```
$ ros2 run cpp_srvcli server
```

```
$ ros2 run cpp_srvcli client 2 3 1
```

Python

```
$ ros2 run py_srvcli service
```

```
$ ros2 run py_srvcli client 2 3 1
```

<a id="summary"></a>

## Summary

In this tutorial, you learned how to create custom interfaces in their own package and how to utilize those interfaces in other packages.

This tutorial only scratches the surface about defining custom interfaces.
You can learn more about it in [About ROS 2 interfaces](../../concepts/basic/about-interfaces.md).

<a id="next-steps"></a>

## Next steps

The [next tutorial](single-package-define-and-use-interface.md) covers more ways to use interfaces in ROS 2.
