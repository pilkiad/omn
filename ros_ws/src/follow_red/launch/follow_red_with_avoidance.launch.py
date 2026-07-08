from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    collision_avoidance_node = Node(
        package='collision_avoidance',
        executable='collision_avoidance',
        name='collision_avoidance',
    )

    follow_red_node = Node(
        package='follow_red',
        executable='follow_red',
        name='follow_red',
    )

    return LaunchDescription([
        # Starte collision_avoidance zuerst
        collision_avoidance_node,
        # Starte follow_red nach 2 Sekunden Verzögerung,
        # damit collision_avoidance Zeit hat zu initialisieren
        TimerAction(
            period=2.0,
            actions=[follow_red_node],
        ),
    ])