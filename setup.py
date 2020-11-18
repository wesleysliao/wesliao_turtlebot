import os
from glob import glob
from setuptools import setup

package_name = 'wesliao_turtlebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name), glob('launch/*.py')),
        # Include model and simulation files
        (os.path.join('share', package_name), glob('urdf/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wesliao',
    maintainer_email='wesliao@iu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'state_publisher = wesliao_turtlebot.state_publisher:main'
        ],
    },
)
