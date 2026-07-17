"""Launch the robot manager (supervisor + dashboard).

Assumes the rest of the stack (drivers, slam_toolbox, slam_analyzer,
navigation, collision_avoidance) is launched separately, exactly as the
team already does. The manager only observes and commands existing topics.

The one exception is /pose: nothing else in the stack publishes it, and
robot_manager treats /pose as a critical health item, so this launch file
also starts robot_manager's own pose_publisher node, which bridges
roboclaw's /odom into /pose. No other team's package is touched by this;
pose_publisher lives entirely inside robot_manager.
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
        DeclareLaunchArgument(
            'odom_topic', default_value='/odom',
            description='Odometry topic published by roboclaw'),
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
        Node(
            package='robot_manager',
            executable='pose_publisher',
            name='pose_publisher',
            output='screen',
            parameters=[{
                'input_topic': LaunchConfiguration('odom_topic'),
                'output_topic': '/pose',
                'output_frame_id': 'map',
            }],
        ),
    ])