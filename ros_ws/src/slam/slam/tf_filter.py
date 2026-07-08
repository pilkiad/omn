#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage

class TfFilterNode(Node):
    def __init__(self):
        super().__init__('tf_filter')
        
        # Abonnieren des umgeleiteten "Geister-Topics" aus dem ROSbag
        self.subscription = self.create_subscription(
            TFMessage,
            '/tf_recorded',
            self.tf_callback,
            10
        )
        
        # Publizieren auf das echte TF-Topic für die SLAM Toolbox
        self.publisher = self.create_publisher(TFMessage, '/tf', 10)
        
        self.get_logger().info("TF-Filter aktiv! Blockiere alte Odometrie UND alte Map-Daten aus dem Bag-File.")

    def tf_callback(self, msg: TFMessage):
        filtered_msg = TFMessage()
        
        for transform in msg.transforms:
            frame_id = transform.header.frame_id
            child_frame_id = transform.child_frame_id
            
            # 1. Blockiere die verrauschte Original-Odometrie (unser Downsampler übernimmt das)
            if frame_id == 'odom' and child_frame_id == 'base_footprint':
                continue
                
            # 2. Blockiere ALTE Karten-Daten aus dem Bag-File, um TF-Kollisionen zu verhindern!
            if frame_id == 'map' and child_frame_id == 'odom':
                continue
                
            # Alle anderen Transformationen (z.B. Laser-Mounts) werden sicher durchgelassen
            filtered_msg.transforms.append(transform)
        
        # Nur publizieren, wenn nach dem Filtern noch saubere Transformationen übrig sind
        if filtered_msg.transforms:
            self.publisher.publish(filtered_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TfFilterNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()