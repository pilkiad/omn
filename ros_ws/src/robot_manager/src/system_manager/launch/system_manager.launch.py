"""Launch the System Manager against your teammates' REAL nodes.

Use this once teammates' packages exist. Their launch files (or your
top-level launch file) should bring their nodes up UNCONFIGURED --
do not activate them yourselves. The System Manager is what calls
configure/activate, in the correct order, once every node's
change_state service is available.
"""
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('system_manager'), 'config', 'managed_nodes.yaml')

    return LaunchDescription([
        Node(
            package='system_manager',
            executable='orchestrator_node',
            name='system_manager',
            output='screen',
            parameters=[config],
        ),
    ])
