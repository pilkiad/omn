---
title: "Project Governance"
docname: "The-ROS2-Project/Governance"
source: "The-ROS2-Project/Governance.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "project"
tags: ["ros2", "jazzy", "project"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Project hub](../../wiki/tooling-map.md)
> Related: [Contributing](contributing.md) | [Feature Ideas](feature-ideas.md) | [Features Status](features.md) | [Marketing](marketing.md) | [Metrics](metrics.md)

<a id="project-governance"></a>
<a id="governance"></a>

# Project Governance

Table of Contents

- [The Open Source Robotics Alliance (OSRA)](#the-open-source-robotics-alliance-osra)

  - [The Technical Governance Committee (TGC)](#the-technical-governance-committee-tgc)
  - [The ROS Project Management Committee (ROS PMC)](#the-ros-project-management-committee-ros-pmc)
  - [ROS Project Management Committee (PMC) Meetings](#ros-project-management-committee-pmc-meetings)
  - [Current ROS PMC Constituents](#current-ros-pmc-constituents)
  - [Current ROS Committers](#current-ros-committers)
  - [Past ROS PMC Constituents](#past-ros-pmc-constituents)
  - [Repositories managed by the ROS PMC](#repositories-managed-by-the-ros-pmc)
- [Upcoming ROS Events](#upcoming-ros-events)

<a id="the-open-source-robotics-alliance-osra"></a>

## The Open Source Robotics Alliance (OSRA)

Since 2024, the ROS 2 project has been governed by the [Open Source Robotics Alliance (OSRA)](https://osralliance.org/).
The information below is meant to give a quick overview of the project governance, but for full information please see [the OSRA’s website](https://osralliance.org/how-it-works/).

<a id="the-technical-governance-committee-tgc"></a>

### The Technical Governance Committee (TGC)

The Technical Governance Committee is responsible for the oversight of all projects within the OSRA.
The TGC is made up of a combination of paid members, project management leaders, OSRF leaders, and members based on merits.
For more details about the TGC, please see [the Charter for the OSRA](https://osralliance.org/staging/wp-content/uploads/2024/03/OSRA-Program-Charter.pdf).
One of the projects that the TGC oversees is ROS 2, which is managed by the ROS Project Management Committee.

<a id="the-ros-project-management-committee-ros-pmc"></a>

### The ROS Project Management Committee (ROS PMC)

The ROS Project Management Committee is responsible for the day-to-day operations of the ROS 2 project.
The ROS PMC consists of the Project Leader, the ROS PMC Members (who have full voting rights), a Supporting Individual Representative, and the Chair of the TGC.
The project also has Committers, who help manage one or more repositories but are not a part of the PMC.
The Project Leader, all PMC Members, and all Committers are chosen on a meritocratic basis.

The day-to-day operations of the ROS PMC include managing the members and committers, managing the repositories that make up ROS 2, reviewing and merging code from the ROS community, maintaining the repositories, and making technical decisions that decide the direction of the project.

For more details about the ROS PMC, please see the [Charter for the ROS Project](https://osralliance.org/staging/wp-content/uploads/2024/03/ros_project_charter.pdf).

<a id="ros-project-management-committee-pmc-meetings"></a>

### ROS Project Management Committee (PMC) Meetings

Community members are encouraged to observe the ROS 2 PMC meetings and submit agenda items via a PMC constituent.
To add an item to the ROS PMC agenda please contact one of the ROS PMC constituents list below.
ROS PMC meetings are conducted using Zoom and presently occur every Tuesday at 17:00 UTC (09:00 PST / 12:00 EST / 18:00 CET / +1 02:00 JST).
To join the ROS PMC meeting please use the [link available in our official OSRA Google calendar](https://calendar.google.com/calendar/u/0/embed?src=agf3kajirket8khktupm9go748@group.calendar.google.com&ctz=Etc%2FUTC).

<a id="current-ros-pmc-constituents"></a>

### Current ROS PMC Constituents

The ROS PMC currently consists of the following constituents:

| Name | Affiliation | GitHub handle | PMC role | Time Zone (optional) |
| --- | --- | --- | --- | --- |
| Christophe Bédard | [KUKA](https://www.kuka.com/) | [christophebedard](https://github.com/christophebedard) | Member | PST (UTC-8)/PDT (UTC-7) |
| Michael Carroll | [KUKA](https://www.kuka.com/) | [mjcarroll](https://github.com/mjcarroll) | (Interim) Project Leader | CST (UTC-6)/CDT (UTC-5) |
| Miguel Company | [eProsima](https://www.eprosima.com/) | [MiguelCompany](https://github.com/MiguelCompany) | Member | CET (UTC+1)/CEST (UTC+2) |
| Tomoya Fujita | [Sony](https://www.sony.com/) | [fujitatomoya](https://github.com/fujitatomoya) | Member | JST (UTC+9) |
| Marco A. Gutiérrez | [Intrinsic](https://www.intrinsic.ai/) | [marcoag](https://github.com/marcoag) | Member | SGT (UTC+8) |
| Alejandro Hernandez Cordero | [Honu Robotics](https://www.honurobotics.com/) | [ahcorde](https://github.com/ahcorde) | Member | CET (UTC+1)/CEST (UTC+2) |
| Emerson Knapp | [Polymath Robotics](https://www.polymathrobotics.com/) | [emersonknapp](https://github.com/emersonknapp/) | Member | PST (UTC-8)/PDT (UTC-7) |
| Chris Lalancette | Independent | [clalancette](https://github.com/clalancette) | Member (former Project Leader) | N/A |
| Scott Logan | [Intrinsic](https://www.intrinsic.ai/) | [cottsay](https://github.com/cottsay) | Member | CST (UTC-6)/CDT (UTC-5) |
| Shane Loretz | [Intrinsic](https://www.intrinsic.ai/) | [sloretz](https://github.com/sloretz) | Member | PST (UTC-8)/PDT (UTC-7) |
| Audrow Nash | [Intrinsic](https://www.intrinsic.ai/) | [Audrow](https://github.com/audrow) | Member | CST (UTC-6)/CDT (UTC-5) |
| Michael Orlov | [Apex.AI](https://www.apex.ai/) | [MichaelOrlov](https://github.com/MichaelOrlov) | Member | PST (UTC-8)/PDT (UTC-7) |
| Steven! Ragnarök | [Intrinsic](https://www.intrinsic.ai/) | [nuclearsandwich](https://github.com/nuclearsandwich) | Member / Infrastructure Project Lead | PST (UTC-8)/PDT (UTC-7) |
| Alberto Soragna | [Outrider](https://www.outrider.ai/) | [alsora](https://github.com/alsora) | Member | CET (UTC+1)/CEST (UTC+2) |
| Yadunund Vijay | [Intrinsic](https://www.intrinsic.ai/) | [Yadunund](https://github.com/Yadunund) | Member | PST (UTC-8)/PDT (UTC-7) |
| William Woodall | [Intrinsic](https://www.intrinsic.ai/) | [wjwwood](https://github.com/wjwwood) | Member | PST (UTC-8)/PDT (UTC-7) |

<a id="current-ros-committers"></a>

### Current ROS Committers

The ROS committers (who are not also part of the ROS PMC) consists of the following constituents:

| Name | Affiliation | GitHub handle | Time Zone (optional) |
| --- | --- | --- | --- |
| Barry Xu | [Sony](https://www.sony.com/) | [Barry-Xu-2018](https://github.com/Barry-Xu-2018) | CST (UTC+8) |
| Brandon Ong | [Intrinsic](https://www.intrinsic.ai/) | [methylDragon](https://github.com/methylDragon) | PST (UTC-8)/PDT (UTC-7) |
| Dharini Dutia | [Intrinsic](https://www.intrinsic.ai/) | [quarkytale](https://github.com/quarkytale) | PST (UTC-8)/PDT (UTC-7) |
| Janosch Machowinski | [cellumation](https://cellumation.com/) | [jmachowinski](https://github.com/jmachowinski) | CET (UTC+1) |
| Julien Enoch | [Zettascale](https://www.zettascale.tech/) | [JEnoch](https://github.com/JEnoch) | CET (UTC+1)/CEST (UTC+2) |
| Kat Scott | [Intrinsic](https://www.intrinsic.ai/) | [kscottz](https://github.com/kscottz) | PST (UTC-8)/PDT (UTC-7) |
| Michael (Robert) Carlstrom | [CivRobotics](https://www.civrobotics.com/) | [InvincibleRMC](https://github.com/InvincibleRMC) | PST (UTC-8)/PDT (UTC-7) |
| Skyler Medeiros | [Polymath Robotics](https://www.polymathrobotics.com/) | [skyegalaxy](https://github.com/skyegalaxy) | PST (UTC-8)/PDT (UTC-7) |
| Steve Peters | [Intrinsic](https://www.intrinsic.ai/) | [scpeters](https://github.com/scpeters) | PST (UTC-8)/PDT (UTC-7) |
| Tully Foote | [Intrinsic](https://www.intrinsic.ai/) | [tfoote](https://github.com/tfoote) | PST (UTC-8)/PDT (UTC-7) |
| Andrew Symington | [Intrinsic](https://www.intrinsic.ai/) | [asymingt](https://github.com/asymingt) | PST (UTC-8)/PDT (UTC-7) |
| Yuyuan Yuan | [Zettascale](https://www.zettascale.tech/) | [YuanYuYuan](https://github.com/YuanYuYuan) | TST (UTC+8) |

<a id="past-ros-pmc-constituents"></a>

### Past ROS PMC Constituents

The ROS PMC thanks the following past constituents for their service:

| Name | PMC role | GitHub handle (optional) |
| --- | --- | --- |
| None yet | None yet | None yet |

<a id="repositories-managed-by-the-ros-pmc"></a>

### Repositories managed by the ROS PMC

The following repositories are managed by the ROS PMC:

| Repository URL |
| --- |
| <https://github.com/ament/ament_cmake> |
| <https://github.com/ament/ament_index> |
| <https://github.com/ament/ament_lint> |
| <https://github.com/ament/ament_package> |
| <https://github.com/ament/google_benchmark_vendor> |
| <https://github.com/ament/googletest> |
| <https://github.com/ament/uncrustify_vendor> |
| <https://github.com/gazebo-release/gz_cmake_vendor> |
| <https://github.com/gazebo-release/gz_math_vendor> |
| <https://github.com/gazebo-release/gz_utils_vendor> |
| <https://github.com/osrf/osrf_pycommon> |
| <https://github.com/osrf/osrf_testing_tools_cpp> |
| <https://github.com/ros-infrastructure/rep> |
| <https://github.com/ros-infrastructure/rosdoc2> |
| <https://github.com/ros-perception/image_common> |
| <https://github.com/ros-perception/laser_geometry> |
| <https://github.com/ros-perception/point_cloud_transport> |
| <https://github.com/ros-perception/pointcloud_to_laserscan> |
| <https://github.com/ros-planning/navigation_msgs> |
| <https://github.com/ros-tooling/keyboard_handler> |
| <https://github.com/ros-tooling/libstatistics_collector> |
| <https://github.com/ros-visualization/interactive_markers> |
| <https://github.com/ros-visualization/python_qt_binding> |
| <https://github.com/ros-visualization/qt_gui_core> |
| <https://github.com/ros-visualization/rqt> |
| <https://github.com/ros-visualization/rqt_action> |
| <https://github.com/ros-visualization/rqt_bag> |
| <https://github.com/ros-visualization/rqt_console> |
| <https://github.com/ros-visualization/rqt_graph> |
| <https://github.com/ros-visualization/rqt_msg> |
| <https://github.com/ros-visualization/rqt_plot> |
| <https://github.com/ros-visualization/rqt_publisher> |
| <https://github.com/ros-visualization/rqt_py_console> |
| <https://github.com/ros-visualization/rqt_reconfigure> |
| <https://github.com/ros-visualization/rqt_service_caller> |
| <https://github.com/ros-visualization/rqt_shell> |
| <https://github.com/ros-visualization/rqt_srv> |
| <https://github.com/ros-visualization/rqt_topic> |
| <https://github.com/ros-visualization/tango_icons_vendor> |
| <https://github.com/ros-visualization/visualization_tutorials> |
| <https://github.com/ros/angles> |
| <https://github.com/ros/class_loader> |
| <https://github.com/ros/console_bridge> |
| <https://github.com/ros/eigen_stl_containers> |
| <https://github.com/ros/geometry_tutorials> |
| <https://github.com/ros/kdl_parser> |
| <https://github.com/ros/pluginlib> |
| <https://github.com/ros/resource_retriever> |
| <https://github.com/ros/robot_state_publisher> |
| <https://github.com/ros/ros_environment> |
| <https://github.com/ros/ros_tutorials> |
| <https://github.com/ros/rosdistro> |
| <https://github.com/ros/urdf_parser_py> |
| <https://github.com/ros/urdfdom> |
| <https://github.com/ros/urdfdom_headers> |
| <https://github.com/ros2/ament_cmake_ros> |
| <https://github.com/ros2/common_interfaces> |
| <https://github.com/ros2/console_bridge_vendor> |
| <https://github.com/ros2/demos> |
| <https://github.com/ros2/design> |
| <https://github.com/ros2/eigen3_cmake_module> |
| <https://github.com/ros2/example_interfaces> |
| <https://github.com/ros2/examples> |
| <https://github.com/ros2/geometry2> |
| <https://github.com/ros2/launch> |
| <https://github.com/ros2/launch_ros> |
| <https://github.com/ros2/libyaml_vendor> |
| <https://github.com/ros2/message_filters> |
| <https://github.com/ros2/mimick_vendor> |
| <https://github.com/ros2/orocos_kdl_vendor> |
| <https://github.com/ros2/performance_test_fixture> |
| <https://github.com/ros2/pybind11_vendor> |
| <https://github.com/ros2/rcl> |
| <https://github.com/ros2/rcl_interfaces> |
| <https://github.com/ros2/rcl_logging> |
| <https://github.com/ros2/rclcpp> |
| <https://github.com/ros2/rclpy> |
| <https://github.com/ros2/rcpputils> |
| <https://github.com/ros2/rcutils> |
| <https://github.com/ros2/realtime_support> |
| <https://github.com/ros2/rmw> |
| <https://github.com/ros2/rmw_connextdds> |
| <https://github.com/ros2/rmw_cyclonedds> |
| <https://github.com/ros2/rmw_dds_common> |
| <https://github.com/ros2/rmw_fastrtps> |
| <https://github.com/ros2/rmw_implementation> |
| <https://github.com/ros2/rmw_zenoh> |
| <https://github.com/ros2/ros_testing> |
| <https://github.com/ros2/ros2> |
| <https://github.com/ros2/ros2_documentation> |
| <https://github.com/ros2/ros2_tracing> |
| <https://github.com/ros2/ros2cli> |
| <https://github.com/ros2/ros2cli_common_extensions> |
| <https://github.com/ros2/rosbag2> |
| <https://github.com/ros2/rosidl> |
| <https://github.com/ros2/rosidl_core> |
| <https://github.com/ros2/rosidl_dds> |
| <https://github.com/ros2/rosidl_defaults> |
| <https://github.com/ros2/rosidl_dynamic_typesupport> |
| <https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps> |
| <https://github.com/ros2/rosidl_python> |
| <https://github.com/ros2/rosidl_runtime_py> |
| <https://github.com/ros2/rosidl_typesupport> |
| <https://github.com/ros2/rosidl_typesupport_fastrtps> |
| <https://github.com/ros2/rpyutils> |
| <https://github.com/ros2/rviz> |
| <https://github.com/ros2/spdlog_vendor> |
| <https://github.com/ros2/sros2> |
| <https://github.com/ros2/system_tests> |
| <https://github.com/ros2/test_interface_files> |
| <https://github.com/ros2/tinyxml_vendor> |
| <https://github.com/ros2/tinyxml2_vendor> |
| <https://github.com/ros2/tlsf> |
| <https://github.com/ros2/unique_identifier_msgs> |
| <https://github.com/ros2/urdf> |
| <https://github.com/ros2/yaml_cpp_vendor> |

<a id="upcoming-ros-events"></a>

## Upcoming ROS Events

Upcoming official Open Source Robotics Foundation events can be found in this [Google Calendar](https://calendar.google.com/calendar/embed?src=agf3kajirket8khktupm9go748%40group.calendar.google.com&ctz=America%2FLos_Angeles).
It can be accessed via [iCal](https://calendar.google.com/calendar/ical/agf3kajirket8khktupm9go748%40group.calendar.google.com/public/basic.ics).

.responsiveCal {
position: relative; padding-bottom: 75%; height: 0; overflow: hidden;
}
.responsiveCal iframe {
position: absolute; top:0; left: 0; width: 100%; height: 100%;
}
@media all and (min-width: 768px) {
.deskContent {display:block;}
.phoneContent {display:none;}
}
@media all and (max-width: 767px) {
.deskContent {display:none;}
.phoneContent {display:block;}
}
  

Upcoming unofficial ROS community events can be found in this [Google Calendar](https://calendar.google.com/calendar/embed?src=c_3fc5c4d6ece9d80d49f136c1dcd54d7f44e1acefdbe87228c92ff268e85e2ea0@group.calendar.google.com).
It can be accessed via [iCal](https://calendar.google.com/calendar/ical/c_3fc5c4d6ece9d80d49f136c1dcd54d7f44e1acefdbe87228c92ff268e85e2ea0@group.calendar.google.com/public/basic.ics).
If you have an individual event or series of events that you’d like to post, please [submit it using this form](https://bit.ly/OSRFCalendarForm).
