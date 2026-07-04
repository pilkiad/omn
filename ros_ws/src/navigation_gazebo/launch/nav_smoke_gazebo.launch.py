import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory('navigation_gazebo')
    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')

    world_path = os.path.join(package_share, 'worlds', 'nav_smoke.sdf')
    bridge_config = os.path.join(package_share, 'config', 'nav_smoke_bridge.yaml')
    map_yaml = os.path.join(package_share, 'maps', 'nav_smoke_map.yaml')

    gui = LaunchConfiguration('gui')
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_collision_avoidance = LaunchConfiguration('use_collision_avoidance')

    gz_sim_launch = os.path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
    gz_server_launch = os.path.join(ros_gz_sim_share, 'launch', 'gz_server.launch.py')

    return LaunchDescription([
        DeclareLaunchArgument(
            'gui',
            default_value='false',
            description='Start Gazebo with the GUI.',
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use Gazebo simulation time.',
        ),
        DeclareLaunchArgument(
            'use_collision_avoidance',
            default_value='false',
            description='Launch collision_avoidance for /base/cmd_vel comparison.',
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_sim_launch),
            launch_arguments={
                'gz_args': f'-r {world_path}',
                'on_exit_shutdown': 'true',
            }.items(),
            condition=IfCondition(gui),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_server_launch),
            launch_arguments={
                'world_sdf_file': world_path,
            }.items(),
            condition=UnlessCondition(gui),
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='nav_smoke_bridge',
            output='screen',
            parameters=[{
                'config_file': bridge_config,
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{
                'yaml_filename': map_yaml,
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_map_server',
            output='screen',
            parameters=[{
                'autostart': True,
                'node_names': ['map_server'],
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='navigation_gazebo',
            executable='map_service_to_topic',
            name='map_service_to_topic',
            output='screen',
            parameters=[{
                'service_name': '/map_server/map',
                'topic_name': '/map',
                'publish_period': 1.0,
            }],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom',
            output='screen',
            arguments=[
                '--frame-id', 'map',
                '--child-frame-id', 'odom',
            ],
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        Node(
            package='navigation_gazebo',
            executable='odom_to_pos',
            name='odom_to_pos',
            output='screen',
            parameters=[{
                'output_frame_id': 'map',
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='navigation',
            executable='navigation',
            name='navigation',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        Node(
            package='navigation_gazebo',
            executable='target_vector_to_cmd_vel',
            name='target_vector_to_cmd_vel',
            output='screen',
            parameters=[{
                'input_topic': '/target_vector',
                'output_topic': '/cmd_vel',
                'stale_timeout': 0.75,
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='collision_avoidance',
            executable='collision_avoidance',
            name='collision_avoidance',
            output='screen',
            condition=IfCondition(use_collision_avoidance),
            parameters=[{'use_sim_time': use_sim_time}],
        ),
    ])
