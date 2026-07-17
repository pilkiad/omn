import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    # -----------------------------------------------------------------------
    # HINWEIS ZUM PACKAGE-NAMEN:
    # Ich gehe davon aus, dass dein Package 'my_robot_web' heißt,
    # da dies im Backend-Code so definiert war. 
    # Falls es anders heißt, ändere 'my_robot_web' entsprechend ab.
    # -----------------------------------------------------------------------
    package_name = 'system_manager'
    
    # Optional: Falls du eine vorgefertigte RViz-Konfiguration hast, 
    # kannst du diesen Pfad einkommentieren und unten bei arguments übergeben.
    # rviz_config_path = os.path.join(get_package_share_directory(package_name), 'rviz', 'default.rviz')

    return LaunchDescription([
        
        # 1. DAS BACKEND (Deine State-Machine & Schutzmatrix)
        Node(
            package=package_name,
            executable='dashboard_backend_node', # Der Name, wie er in der setup.py unter entry_points steht
            name='dashboard_backend_node',
            output='screen'
        ),
        
        # 2. DAS FRONTEND-GATEWAY (Zwingend für die index.html / roslibjs)
        # Stellt den WebSocket auf ws://localhost:9090 bereit.
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_websocket',
            output='screen',
            parameters=[{
                'port': 9090,
                'topic_whitelist': ['.*'],
                'max_message_size': 10000000,
            }]
        ),
        
        # 3. RVIZ2 (Für die visuelle Kontrolle von Map, Lidar und Robotermodell)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
            # arguments=['-d', rviz_config_path] # Einkommentieren für automatische Config-Ladung
        )
    ])