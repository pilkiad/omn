from setuptools import setup
import os
from glob import glob

package_name = 'slam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # HIER IST DIE MAGIE: Wir exportieren den config-Ordner
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        
        # HIER IST DIE MAGIE: Wir exportieren den launch-Ordner
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dein Name',
    maintainer_email='deine.email@beispiel.de',
    description='SLAM Paket mit SLAM Toolbox und Abbruchkriterium',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'slam_analyzer = slam.slam_analyzer:main',
            'odom_downsampler = slam.odom_downsampler:main',
            'tf_filter = slam.tf_filter:main',
            'FrontierManager=slam.FrontierManager:main'
        ],
    }
)