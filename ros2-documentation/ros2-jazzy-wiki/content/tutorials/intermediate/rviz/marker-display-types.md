---
title: "Marker: Display types"
docname: "Tutorials/Intermediate/RViz/Marker-Display-types/Marker-Display-types"
source: "Tutorials/Intermediate/RViz/Marker-Display-types/Marker-Display-types.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Building a Custom RViz Display](rviz-custom-display.md) | [Building a Custom RViz Panel](rviz-custom-panel.md) | [Defining worlds, robots, and sensors](../../advanced/simulators/mvsim/defining-worlds-mvsim.md) | [Gazebo](../../advanced/simulators/gazebo/simulation-gazebo.md) | [Getting started with MVSim](../../advanced/simulators/mvsim/getting-started-mvsim.md)

<a id="marker-display-types"></a>

# Marker: Display types

**Goal:** This tutorial explains the basic Marker types and how to use them.

**Tutorial level:** Intermediate

**Time:** 15 Minutes

Contents

- [Background](#background)
- [The Marker Message](#the-marker-message)

  - [1 Example Usage (C++)](#example-usage-c)
  - [2 Message Parameters](#message-parameters)
  - [3 Object types](#object-types)
  - [4 Rendering Complexity Notes](#rendering-complexity-notes)

<a id="background"></a>

## Background

The Markers display allows programmatic addition of various primitive shapes to the 3D view by sending a
[visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) or
[visualization\_msgs/msg/MarkerArray](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/MarkerArray.msg) message.

![../../../../../_images/marker_overview.png](../../../../assets/images/marker_overview.png)

Start with [Marker: Sending Basic Shapes](marker-sending-basic-shapes.md) for a minimal publisher example that introduces the marker message used throughout this page.

<a id="the-marker-message"></a>

## The Marker Message

<a id="example-usage-c"></a>

### 1 Example Usage (C++)

First we will create a simple publisher node that publishes `Marker` messages from the `visualization_messages` package to the `visualization_marker` topic:

```
auto marker_pub = node->create_publisher<visualization_msgs::msg::Marker>("visualization_marker", 1);
```

After that it is as simple as filling out a [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg)
message and publishing it:

```
visualization_msgs::msg::Marker marker;

marker.header.frame_id = "/my_frame";
marker.header.stamp = rclcpp::Clock().now();

marker.ns = "basic_shapes";
marker.id = 0;

marker.type = visualization_msgs::msg::Marker::SPHERE;

marker.action = visualization_msgs::msg::Marker::ADD;

marker.pose.position.x = 0;
marker.pose.position.y = 0;
marker.pose.position.z = 0;
marker.pose.orientation.x = 0.0;
marker.pose.orientation.y = 0.0;
marker.pose.orientation.z = 0.0;
marker.pose.orientation.w = 1.0;

marker.scale.x = 1.0;
marker.scale.y = 1.0;
marker.scale.z = 1.0;

marker.color.r = 0.0f;
marker.color.g = 1.0f;
marker.color.b = 0.0f;
marker.color.a = 1.0;   // Don't forget to set the alpha!

// only if using a MESH_RESOURCE marker type:
marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";

marker.lifetime = rclcpp::Duration::from_nanoseconds(0);

marker_pub->publish(marker);
```

There is also a [visualization\_msgs/msg/MarkerArray](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/MarkerArray.msg) message, which lets you publish many markers at once.

<a id="message-parameters"></a>

### 2 Message Parameters

The Marker message type is defined in [ROS 2 Common Interfaces](https://github.com/ros2/common_interfaces/tree/jazzy/visualization_msgs/msg) package.
The messages in this package include comments that are helpful in understanding each of the fields in the message.

- `ns`:

  > Namespace for these markers.
  > This plus the id form a unique identifier.
- `id`:

  > Unique id assigned to this marker.
  > It is your responsibility to keep these unique within your namespace.
- `type`:

  > Type of marker (Arrow, Sphere, …).
  > The available types are specified in the message definition.
- `action`:

  > 0 = add/modify, 1 = (deprecated), 2 = delete, 3 = deleteall
- `pose`:

  > Pose marker, specified as x/y/z position and x/y/z/w quaternion orientation.
- `scale`:

  > Scale of the marker.
  > Applied before the position/orientation.
  > A scale of [1, 1, 1] means the object will be 1m by 1m by 1m.
- `color`:

  > Color of the object, specified as r/g/b/a, with values in the range of [0, 1].
  > The, `a` or alpha value, denotes the opacity of the marker with 1 indicating opaque and 0 indicating completely transparent.
  > The default value is 0, or completely transparent.
  > **You must set the a value of your marker to a non-zero value or it will be transparent by default!**
- `points`:

  > Only used for markers of type `Points`, `Line strips`, and `Line` / `Cube` / `Sphere` -lists.
  > It’s also used for the Arrow type, if you want to specify the arrow start and end points.
  > This entry represents a list of `geometry_msgs/Point` types for the center or each marker object you would like rendered.
- `colors`:

  > This field is only used for markers that use the points member.
  > This field specifies per-vertex color r/g/b/ color (no alpha yet) for each entry in `points`.
- `lifetime`:

  > A [duration message value](https://docs.ros.org/en/jazzy/p/builtin_interfaces/msg/Duration.html) used to automatically delete the marker after this period of time.
  > The countdown resets if another marker of the same `namespace` / `id` is received.
- `frame_locked`:

  > Without the `frame_locked` parameter the marker will be placed based on the current transform and will stay there even if the given transform changes later.
  > Setting this parameter tells RViz to retransform the marker to the new current location of the specified frame on every update cycle.
- `text`:

  > The text string used for the `TEXT_VIEW_FACING` marker type
- `mesh_resource`:

  > The resource location for the `MESH_RESOURCE` marker type.
  > Can be any mesh type supported by RViz (`.stl` or Ogre `.mesh` in 1.0, with the addition of COLLADA in 1.1).
  > The format is the URI-form used by [resource\_retriever](https://github.com/ros/resource_retriever/tree/jazzy), including the package:// syntax.

<a id="object-types"></a>

### 3 Object types

<a id="arrow-arrow-0"></a>
<a id="rvizmarkerobjecttypes"></a>

#### 3.1 Arrow (ARROW=0)

![../../../../../_images/ArrowMarker.png](../../../../assets/images/ArrowMarker.png)

The arrow type provides two different ways of specifying where the arrow should begin/end:

- `Position/Orientation`:

  > Pivot point is around the tip of its tail.
  > Identity orientation points it along the +X axis.
  > `scale.x` is the arrow length, `scale.y` is the arrow width and `scale.z` is the arrow height.
- `Start/End Points`:

  > You can also specify a start/end point for the arrow, using the points member.
  > If you put points into the points member, it will assume you want to do things this way.
  >
  > - The point at index 0 is assumed to be the start point, and the point at index 1 is assumed to be the end.
  > - `scale.x` is the shaft diameter, and `scale.y` is the head diameter.
  >   If `scale.z` is not zero, it specifies the head length.

<a id="cube-cube-1"></a>

#### 3.2 Cube (CUBE=1)

![../../../../../_images/CubeMarker.png](../../../../assets/images/CubeMarker.png)

Pivot point is at the center of the cube.

<a id="sphere-sphere-2"></a>

#### 3.3 Sphere (SPHERE=2)

![../../../../../_images/SphereMarker.png](../../../../assets/images/SphereMarker.png)

Pivot point is at the center of the sphere.

`scale.x` is diameter in x direction, `scale.y` in y direction, `scale.z` in z direction.
By setting these to different values you get an ellipsoid instead of a sphere.

<a id="cylinder-cylinder-3"></a>

#### 3.4 Cylinder (CYLINDER=3)

![../../../../../_images/CylinderMarker.png](../../../../assets/images/CylinderMarker.png)

Pivot point is at the center of the cylinder.

`scale.x` is diameter in x direction, `scale.y` in y direction, by setting these to different values you get an ellipse instead of a circle.
Use `scale.z` to specify the height.

<a id="line-strip-line-strip-4"></a>

#### 3.5 Line Strip (LINE\_STRIP=4)

![../../../../../_images/LineStripMarker.png](../../../../assets/images/LineStripMarker.png)

Line strips use the points member of the [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) message.
It will draw a line between every two consecutive points, so 0-1, 1-2, 2-3, 3-4, 4-5…

Line strips also have some special handling for scale: only `scale.x` is used and it controls the width of the line segments.

Note that `pose` is still used (the points in the line will be transformed by them), and the lines will be correct relative to the `frame id` specified in the header.

<a id="line-list-line-list-5"></a>

#### 3.6 Line List (LINE\_LIST=5)

![../../../../../_images/LineListMarker.png](../../../../assets/images/LineListMarker.png)

Line lists use the points member of the [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) message.
It will draw a line between each pair of points, so 0-1, 2-3, 4-5, …

Line lists also have some special handling for scale: only `scale.x` is used and it controls the width of the line segments.

Note that `pose` is still used (the points in the line will be transformed by them), and the lines will be correct relative to the `frame id` specified in the header.

<a id="cube-list-cube-list-6"></a>

#### 3.7 Cube List (CUBE\_LIST=6)

![../../../../../_images/CubeListMarker.png](../../../../assets/images/CubeListMarker.png)

A cube list is a list of cubes with all the same properties except their positions.
Using this object type instead of a [visualization\_msgs/msg/MarkerArray](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/MarkerArray.msg) allows RViz to batch-up rendering,
which causes them to render much faster.
The caveat is that they all must have the same scale.

The `points` member of the [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) message is used for the position of each cube.

<a id="sphere-list-sphere-list-7"></a>

#### 3.8 Sphere List (SPHERE\_LIST=7)

![../../../../../_images/SphereListMarker.png](../../../../assets/images/SphereListMarker.png)

A sphere list is a list of spheres with all the same properties except their positions.
Using this object type instead of a [visualization\_msgs/msg/MarkerArray](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/MarkerArray.msg) allows RViz to batch-up rendering,
which causes them to render much faster.
The caveat is that they all must have the same scale.

The `points` member of the [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) message is used for the position of each sphere.

Note that `pose` is still used (the `points` in the line will be transformed by them), and the lines will be correct relative to the `frame id` specified in the header.

<a id="points-points-8"></a>

#### 3.9 Points (POINTS=8)

![../../../../../_images/PointsMarker.png](../../../../assets/images/PointsMarker.png)

Uses the `points` member of the [visualization\_msgs/msg/Marker](https://github.com/ros2/common_interfaces/blob/jazzy/visualization_msgs/msg/Marker.msg) message.

`Points` have some special handling for scale: `scale.x` is point width, `scale.y` is point height

Note that `pose` is still used (the `points` in the line will be transformed by them), and the lines will be correct relative to the `frame id` specified in the header.

<a id="view-oriented-text-text-view-facing-9"></a>

#### 3.10 View-Oriented Text (TEXT\_VIEW\_FACING=9)

![../../../../../_images/text_view_facing_marker.png](../../../../assets/images/text_view_facing_marker.png)

This marker displays text in a 3D spot in the world.
The text always appears oriented correctly for the RViZ user to see the included text.
Uses the `text` field in the marker.

Only `scale.z` is used.
`scale.z` specifies the height of an uppercase “A”.

<a id="mesh-resource-mesh-resource-10"></a>

#### 3.11 Mesh Resource (MESH\_RESOURCE=10)

![../../../../../_images/mesh_resource_marker.png](../../../../assets/images/mesh_resource_marker.png)

Uses the `mesh_resource` field in the marker.
Can be any mesh type supported by RViz (binary `.stl` or Ogre `.mesh` in 1.0, with the addition of COLLADA (`.dae`) in 1.1).
The format is the URI-form used by [resource\_retriever](https://github.com/ros/resource_retriever/tree/jazzy), including the `package://` syntax.

An example of a mesh an its use is:

```
marker.type = visualization_msgs::Marker::MESH_RESOURCE;
marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";
```

Scale on a mesh is relative.
A scale of (1.0, 1.0, 1.0) means the mesh will display as the exact size specified in the mesh file.
A scale of (1.0, 1.0, 2.0) means the mesh will show up twice as tall, but the same width/depth.

If the `mesh_use_embedded_materials` flag is set to true and the mesh is of a type which supports embedded materials (such as COLLADA),
the material defined in that file will be used instead of the color defined in the marker.

Since version [1.8], even when `mesh_use_embedded_materials` is true,
if the marker `color` is set to anything other than `r=0`, `g=0`, `b=0`, `a=0` the marker `color` and `alpha` will be used to tint the mesh with the embedded material.

<a id="triangle-list-triangle-list-11"></a>

#### 3.12 Triangle List (TRIANGLE\_LIST=11)

![../../../../../_images/triangle_list_marker.png](../../../../assets/images/triangle_list_marker.png)

Uses the points and optionally colors members.
Every set of 3 points is treated as a triangle, so indices 0-1-2, 3-4-5, etc.

Note that `pose` and `scale` are still used (the points in the line will be transformed by them),
and the lines will be correct relative to the `frame id` specified in the header.

<a id="rendering-complexity-notes"></a>

### 4 Rendering Complexity Notes

A single marker is always less expensive to render than many markers.
For example, a single cube list can handle thousands of cubes, where we will not be able to render thousands of individual cube markers.
