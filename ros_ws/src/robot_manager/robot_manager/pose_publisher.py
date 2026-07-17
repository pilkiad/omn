#!/usr/bin/env python3
"""
pose_publisher
--------------

Small bridge node owned by robot_manager.

The real-robot stack (roboclaw, urg_node_2, slam_toolbox, navigation,
collision_avoidance) has no node that publishes geometry_msgs/PoseStamped
on /pose. robot_manager marks /pose as a *critical* health component, and
the navigation package also subscribes directly to /pose to know where the
robot is. Without this bridge, health monitoring will never go green and
navigation will never plan a path, even though every other node looks
"active".

This node subscribes to roboclaw's /odom (nav_msgs/Odometry) and republishes
it as geometry_msgs/PoseStamped on /pose, which is exactly what robot_manager
and navigation expect.

This lives entirely inside robot_manager (no other package is touched or
modified) and starts automatically as part of robot_manager.launch.py.
"""

import math

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import rclpy
from rclpy.node import Node


class PosePublisher(Node):
    def __init__(self):
        super().__init__('pose_publisher')

        self.declare_parameter('input_topic', '/odom')
        self.declare_parameter('output_topic', '/pose')
        self.declare_parameter('output_frame_id', 'map')
        self.declare_parameter('initial_x', 0.0)
        self.declare_parameter('initial_y', 0.0)
        self.declare_parameter('initial_yaw', 0.0)

        self.input_topic = self._get_str('input_topic')
        self.output_topic = self._get_str('output_topic')
        self.output_frame_id = self._get_str('output_frame_id')
        self.initial_x = self._get_double('initial_x')
        self.initial_y = self._get_double('initial_y')
        self.initial_yaw = self._get_double('initial_yaw')

        self.cos_initial_yaw = math.cos(self.initial_yaw)
        self.sin_initial_yaw = math.sin(self.initial_yaw)

        self._last_odom_time = None

        self.subscription = self.create_subscription(
            Odometry,
            self.input_topic,
            self.odom_callback,
            10,
        )
        self.publisher = self.create_publisher(
            PoseStamped,
            self.output_topic,
            10,
        )

        # Warn once if no odometry ever shows up, so this failure is obvious
        # in the log instead of silently leaving /pose empty.
        self._startup_check_timer = self.create_timer(5.0, self._check_input_alive)

        self.get_logger().info(
            f'pose_publisher bridging {self.input_topic} (Odometry) '
            f'-> {self.output_topic} (PoseStamped, frame="{self.output_frame_id}")'
        )

    def _get_str(self, name):
        return self.get_parameter(name).get_parameter_value().string_value

    def _get_double(self, name):
        return self.get_parameter(name).get_parameter_value().double_value

    def _check_input_alive(self):
        if self._last_odom_time is None:
            self.get_logger().warning(
                f'No messages received yet on {self.input_topic}. '
                'Is roboclaw running and publishing odometry?'
            )

    def odom_callback(self, msg):
        self._last_odom_time = self.get_clock().now()

        odom_pose = msg.pose.pose

        pose = PoseStamped()
        pose.header.stamp = msg.header.stamp
        pose.header.frame_id = self.output_frame_id or msg.header.frame_id

        pose.pose.position.x = (
            self.initial_x
            + self.cos_initial_yaw * odom_pose.position.x
            - self.sin_initial_yaw * odom_pose.position.y
        )
        pose.pose.position.y = (
            self.initial_y
            + self.sin_initial_yaw * odom_pose.position.x
            + self.cos_initial_yaw * odom_pose.position.y
        )
        pose.pose.position.z = odom_pose.position.z

        yaw = self.initial_yaw + self._yaw_from_quaternion(odom_pose.orientation)
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = math.sin(yaw / 2.0)
        pose.pose.orientation.w = math.cos(yaw / 2.0)

        self.publisher.publish(pose)

    @staticmethod
    def _yaw_from_quaternion(quaternion):
        siny_cosp = 2.0 * (quaternion.w * quaternion.z + quaternion.x * quaternion.y)
        cosy_cosp = 1.0 - 2.0 * (quaternion.y * quaternion.y + quaternion.z * quaternion.z)
        return math.atan2(siny_cosp, cosy_cosp)


def main(args=None):
    rclpy.init(args=args)
    node = PosePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()