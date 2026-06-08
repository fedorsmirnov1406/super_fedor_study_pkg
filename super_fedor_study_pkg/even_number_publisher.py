#!/usr/bin/env python3
"""Узел-публикатор чётных чисел с детектором переполнения"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        self.publisher = self.create_publisher(Int32, 'even_numbers', 10)
        self.overflow_publisher = self.create_publisher(Int32, 'overflow', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.number = 0
        self.get_logger().info('Публикатор запущен')
    
    def timer_callback(self):
        if self.number >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.number
            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Значение: {self.number}')
            self.number = 0
            return
        
        msg = Int32()
        msg.data = self.number
        self.publisher.publish(msg)
        self.get_logger().info(f'Опубликовано: {self.number}')
        self.number += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Публикатор остановлен')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
