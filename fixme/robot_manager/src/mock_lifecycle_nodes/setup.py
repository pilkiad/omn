import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'mock_lifecycle_nodes'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shein',
    maintainer_email='you@example.com',
    description='Fake LifecycleNode stand-ins for testing the System Manager',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mock_lifecycle_node = mock_lifecycle_nodes.mock_lifecycle_node:main',
        ],
    },
)
