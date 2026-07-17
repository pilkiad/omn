import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    package_name = 'system_manager'

    return LaunchDescription([
        
        # 1. DAS BACKEND (State-Machine, Schutzmatrix & eingebetteter HTTP-Server)
        Node(
            package=package_name,
            executable='dashboard_backend_node',
            name='dashboard_backend_node',
            output='screen'
        ),
        
        # 2. RVIZ2 (Fuer die visuelle Kontrolle von Map, Lidar und Robotermodell)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])