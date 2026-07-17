import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'robot_manager'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    package_data={
        package_name: ['web/*'],
    },
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='OMN team',
    maintainer_email='jassimhameed007@gmail.com',
    description='Supervisory robot manager with lifecycle, health monitor, '
                'task management and web dashboard for the Tortugabot.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_manager = robot_manager.robot_manager_node:main',
            'dashboard_sim = robot_manager.dashboard_server:main',
            'pose_publisher = robot_manager.pose_publisher:main',
        ],
    },
)
