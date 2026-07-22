from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    collision_avoidance_node = Node(
        package='collision_avoidance',
        executable='collision_avoidance',
        name='collision_avoidance',
    )

    navigation_node = Node(
        package='navigation',
        executable='navigation',
        name='navigation',
    )

    follow_red_node = Node(
        package='follow_red',
        executable='follow_red',
        name='follow_red',
        parameters=[{'send_polar': False}],
    )

    return LaunchDescription([
        collision_avoidance_node,
        TimerAction(
            period=2.0,
            actions=[navigation_node, follow_red_node],
        ),
    ])