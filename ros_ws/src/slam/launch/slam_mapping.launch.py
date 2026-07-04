#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from launch_ros.actions import Node


def generate_launch_description():

    # -------------------------------------------------
    # Paketpfade
    # -------------------------------------------------
    slam_pkg_dir = get_package_share_directory("slam")
    slam_toolbox_dir = get_package_share_directory("slam_toolbox")

    # -------------------------------------------------
    # YAML-Datei
    # -------------------------------------------------
    config_file = os.path.join(
        slam_pkg_dir,
        "config",
        "slam_config.yaml"
    )

    print(f"Config: {config_file}")
    print(f"Exists: {os.path.exists(config_file)}")

    # -------------------------------------------------
    # TF base_footprint -> laser
    # -------------------------------------------------
    static_tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="static_tf_pub_laser",
        arguments=[
            "0.10",
            "0.0",
            "0.20",
            "0.0",
            "0.0",
            "0.0",
            "base_footprint",
            "laser"
        ],
        output="screen"
    )

    # -------------------------------------------------
    # Offizielle SLAM Toolbox Launch-Datei
    # (kümmert sich automatisch um den Lifecycle)
    # -------------------------------------------------
    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                slam_toolbox_dir,
                "launch",
                "online_async_launch.py"
            )
        ),
        launch_arguments={
            "slam_params_file": config_file,
            "use_sim_time": "true",
        }.items()
    )

   # odom_downsampler_node = Node(
   # package='slam',
   # executable='odom_downsampler',
   # name='odom_downsampler',
   # output='screen')

    # -------------------------------------------------
    # Dein Analyzer
    # -------------------------------------------------
    slam_analyzer_node = Node(
        package="slam",
        executable="slam_analyzer",
        name="slam_analyzer_node",
        output="screen"
    )

    # -------------------------------------------------
    # LaunchDescription
    # -------------------------------------------------
    return LaunchDescription([
        static_tf_node,
        slam_toolbox_launch,
        slam_analyzer_node,
       # odom_downsampler_node
    ])