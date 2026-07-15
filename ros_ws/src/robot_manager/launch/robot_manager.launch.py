"""Launch the robot manager (supervisor + dashboard).

Assumes the rest of the stack (drivers, slam_toolbox, slam_analyzer,
navigation2, collision_avoidance, odom_to_pos/TF) is launched separately,
exactly as the team already does. The manager only observes and commands
existing topics.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'dashboard_port', default_value='8765',
            description='HTTP port for the web dashboard'),
        DeclareLaunchArgument(
            'assume_map_available', default_value='false',
            description='Skip the mapping phase (a saved map already exists)'),
        Node(
            package='robot_manager',
            executable='robot_manager',
            name='robot_manager',
            output='screen',
            parameters=[{
                'dashboard_port': LaunchConfiguration('dashboard_port'),
                'assume_map_available':
                    LaunchConfiguration('assume_map_available'),
            }],
        ),
    ])
