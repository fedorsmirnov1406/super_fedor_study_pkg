#!/usr/bin/env python3
"""Узел-слушатель событий переполнения"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.callback,
            10
        )
        self.get_logger().info('Слушатель переполнения запущен')
    
    def callback(self, msg):
        self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Значение: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Слушатель остановлен')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
