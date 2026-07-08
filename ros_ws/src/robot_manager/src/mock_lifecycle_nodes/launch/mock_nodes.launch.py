"""Bring up all 6 mock teammate nodes AND your System Manager together.
This is your one-command end-to-end test rig, usable before any
teammate has written a single line of code.

Run with:
    ros2 launch mock_lifecycle_nodes mock_nodes.launch.py
"""
from launch import LaunchDescription
from launch_ros.actions import Node


MOCK_NODE_NAMES = [
    'camera_processor',
    'lidar_processor',
    'mapping',
    'localization',
    'navigation',
    'motion_controller',
]


def generate_launch_description():
    nodes = []
    for name in MOCK_NODE_NAMES:
        nodes.append(Node(
            package='mock_lifecycle_nodes',
            executable='mock_lifecycle_node',
            name=name,
            output='screen',
        ))

    nodes.append(Node(
        package='system_manager',
        executable='orchestrator_node',
        name='system_manager',
        output='screen',
        parameters=[{'managed_node_names': MOCK_NODE_NAMES}],
    ))

    return LaunchDescription(nodes)
