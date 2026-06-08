#!/usr/bin/env python3
"""Узел-публикатор чётных чисел с параметрами"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Объявляем параметры
        self.declare_parameter('publish_frequency', 10.0)
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_name', 'even_numbers')
        
        # Читаем параметры
        freq = self.get_parameter('publish_frequency').value
        threshold = self.get_parameter('overflow_threshold').value
        topic = self.get_parameter('topic_name').value
        
        self.publisher = self.create_publisher(Int32, topic, 10)
        self.overflow_publisher = self.create_publisher(Int32, 'overflow', 10)
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)
        
        self.number = 0
        self.threshold = threshold
        self.get_logger().info(f'Публикатор запущен: частота={freq} Гц, порог={threshold}')
    
    def timer_callback(self):
        if self.number >= self.threshold:
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
