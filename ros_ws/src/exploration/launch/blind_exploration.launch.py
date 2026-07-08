from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='exploration',
            executable='blind_exploration',
            name='blind_exploration',
        ),
        Node(
            package='collision_avoidance',
            executable='collision_avoidance',
            name='collision_avoidance',
        ),
    ])
