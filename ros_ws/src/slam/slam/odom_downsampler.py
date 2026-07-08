#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class OdomDownsampler(Node):
    def __init__(self):
        super().__init__('odom_downsampler')
        
        # Konfiguration der Ziel-Frequenz
        self.target_frequency = 10.0  # Hz
        self.timer_period = 1.0 / self.target_frequency
        
        self.latest_msg = None
        
        # Abonnent für das extrem schnelle Original-Topic
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        
        # Publisher für das Topic
        self.publisher = self.create_publisher(
            Odometry,
            '/odom_downsampler',
            10
        )
        
        # HIER IST DIE MAGIE: Der TF Broadcaster versorgt SLAM mit den räumlichen Daten
        self.tf_broadcaster = TransformBroadcaster(self)
        
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        self.get_logger().info(
            f"Odom-Throttler mit TF-Broadcaster aktiv! Drosselt auf {self.target_frequency} Hz."
        )

    def odom_callback(self, msg: Odometry):
        self.latest_msg = msg

    def timer_callback(self):
        if self.latest_msg is not None:
            # 1. Topic publizieren
            self.publisher.publish(self.latest_msg)
            
            # 2. Transformation (TF) für SLAM generieren und senden
            t = TransformStamped()
            
            # Übernehme den Zeitstempel und die Frame-IDs aus der Original-Nachricht
            t.header.stamp = self.latest_msg.header.stamp
            t.header.frame_id = self.latest_msg.header.frame_id  # Meistens 'odom'
            t.child_frame_id = self.latest_msg.child_frame_id    # Meistens 'base_footprint' oder 'base_link'
            
            # Position extrahieren
            t.transform.translation.x = self.latest_msg.pose.pose.position.x
            t.transform.translation.y = self.latest_msg.pose.pose.position.y
            t.transform.translation.z = self.latest_msg.pose.pose.position.z
            
            # Rotation (Quaternion) extrahieren
            t.transform.rotation = self.latest_msg.pose.pose.orientation
            
            # In den TF-Baum senden
            self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = OdomDownsampler()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()