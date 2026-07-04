import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'navigation_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'maps'),
            glob('maps/*')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
        (os.path.join('share', package_name, 'rviz'),
            glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arian',
    maintainer_email='pilkiad+github@proton.me',
    description='Gazebo Sim smoke test harness for navigation.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'map_service_to_topic = navigation_gazebo.map_service_to_topic:main',
            'odom_to_pos = navigation_gazebo.odom_to_pos:main',
            'target_vector_to_cmd_vel = navigation_gazebo.target_vector_to_cmd_vel:main',
        ],
    },
)
