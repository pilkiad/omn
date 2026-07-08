"""One-command full demo: 6 mock teammate nodes + System Manager + RViz
with the dashboard already loaded.

Run with:
    ros2 launch mock_lifecycle_nodes mock_nodes_with_rviz.launch.py
"""
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


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

    rviz_config = os.path.join(
        get_package_share_directory('system_manager'), 'config', 'dashboard.rviz')

    nodes.append(Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen',
    ))

    return LaunchDescription(nodes)
