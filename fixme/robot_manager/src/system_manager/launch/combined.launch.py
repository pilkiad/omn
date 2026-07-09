"""Example: combined launch file for incremental rollout.

Copy this into system_manager/launch/ as combined.launch.py and edit
the two lists below as teammates finish their nodes. Nothing in your
system_manager package changes -- only this file.
"""
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


# --- EDIT THIS LIST as teammates finish ------------------------------
# Move a name from READY_REAL_NODES to here once their package exists
# and builds. Remove it from mock_lifecycle_nodes's own node list too
# (or just leave the mock running -- your system manager only sees
# ONE node per name on the ROS2 graph, whichever launches first, so
# don't launch both the mock and the real node for the same name).
READY_REAL_NODES = {
    # 'camera_processor': ('camera_processor', 'camera_processor_node'),
    # 'lidar_processor':  ('lidar_processor',  'lidar_processor_node'),
}
# -----------------------------------------------------------------------

STILL_MOCKED = [
    name for name in
    ['camera_processor', 'lidar_processor', 'mapping',
     'localization', 'navigation', 'motion_controller']
    if name not in READY_REAL_NODES
]


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('system_manager'), 'config', 'managed_nodes.yaml')

    actions = [
        # Your orchestrator -- unchanged no matter who is real vs mocked
        Node(
            package='system_manager',
            executable='orchestrator_node',
            name='system_manager',
            output='screen',
            parameters=[config],
        ),
    ]

    # Real teammate nodes that are ready
    for node_name, (package, executable) in READY_REAL_NODES.items():
        actions.append(Node(
            package=package,
            executable=executable,
            name=node_name,
            output='screen',
        ))

    # Mock stand-ins for whoever isn't ready yet
    for node_name in STILL_MOCKED:
        actions.append(Node(
            package='mock_lifecycle_nodes',
            executable='mock_lifecycle_node',
            name=node_name,
            output='screen',
        ))

    return LaunchDescription(actions)