from setuptools import setup

package_name = 'super_fedor_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fedor',
    maintainer_email='fedor@todo.todo',
    description='Мой первый ROS 2 пакет',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'time_printer = super_fedor_study_pkg.time_printer:main',
        ],
    },
)
