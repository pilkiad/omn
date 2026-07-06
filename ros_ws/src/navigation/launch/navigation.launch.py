from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='navigation',
            executable='navigation',
            name='navigation',
        ),
        Node(
            package='collision_avoidance',
            executable='collision_avoidance',
            name='collision_avoidance',
        ),
    ])
