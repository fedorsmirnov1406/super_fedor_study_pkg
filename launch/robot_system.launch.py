#!/usr/bin/env python3
"""Launch-файл для запуска системы с выбором режима"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='fast',
        description='Режим работы: fast или slow'
    )
    
    mode = LaunchConfiguration('mode')
    
    # Быстрый режим
    fast_node = Node(
        package='super_fedor_study_pkg',
        executable='even_publisher',
        name='even_pub_fast',
        output='screen',
        parameters=[{
            'publish_frequency': 20.0,
            'overflow_threshold': 50,
            'topic_name': 'even_numbers_fast',
        }],
    )
    
    # Медленный режим
    slow_node = Node(
        package='super_fedor_study_pkg',
        executable='even_publisher',
        name='even_pub_slow',
        output='screen',
        parameters=[{
            'publish_frequency': 5.0,
            'overflow_threshold': 150,
            'topic_name': 'even_numbers_slow',
        }],
    )
    
    # Слушатель (всегда запускается)
    listener = Node(
        package='super_fedor_study_pkg',
        executable='overflow_listener',
        name='overflow_listener',
        output='screen',
    )
    
    return LaunchDescription([
        mode_arg,
        fast_node,
        slow_node,
        listener,
    ])
