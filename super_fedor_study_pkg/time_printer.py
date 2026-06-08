#!/usr/bin/env python3
"""Узел для вывода текущего времени каждые 5 секунд"""

import rclpy
from rclpy.node import Node
from datetime import datetime

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info('Узел time_printer запущен')
        self.counter = 0
    
    def timer_callback(self):
        self.counter += 1
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.get_logger().info(f'[{self.counter}] Текущее время: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Узел остановлен')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
