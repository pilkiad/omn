import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'system_manager'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml') + glob('config/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shein',
    maintainer_email='you@example.com',
    description='System Manager: lifecycle orchestration, health, recovery, scheduling, dashboard backend',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'orchestrator_node = system_manager.orchestrator_node:main',
        ],
    },
)
