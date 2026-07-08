#!/usr/bin/env python3

import rclpy
from rclpy.lifecycle import LifecycleNode, State, TransitionCallbackReturn
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy

from nav_msgs.msg import OccupancyGrid
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import String

import numpy as np
import cv2
import json
import math
import uuid
import time

class FrontierManager(LifecycleNode):

    def __init__(self):
        super().__init__('frontier_manager_node')
        self.get_logger().info("Frontier Manager gestartet")

        # ---------------------------
        # PARAMETER
        # ---------------------------
        self.min_frontier_area = 5.0      # Mindestgröße in Zellen (Rauschfilter)
        self.tracking_distance = 1.5      # Max. Distanz in Metern, um ein Frontier wiederzuerkennen
        
        # ---------------------------
        # STATE / DATENBANK
        # ---------------------------
        self.latest_map = None
        
        # Format: { 'id_string': { ...frontier_data... } }
        self.active_frontiers = {}

    # ---------------------------
    # LIFECYCLE
    # ---------------------------
    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Konfiguriere Frontier Manager")

        qos = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            depth=10
        )

        # SUBSCRIBER
        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            qos
        )

        # PUBLISHER
        # JSON String für den SystemManager / Explorer
        self.frontier_pub = self.create_lifecycle_publisher(
            String,
            '/frontiers_data',
            10
        )
        
        # Marker für RViz Visualisierung
        self.marker_pub = self.create_lifecycle_publisher(
            MarkerArray,
            '/frontiers_markers',
            10
        )

        # TIMER (z.B. 1 Hz für die Verarbeitung reicht völlig aus)
        self.timer = self.create_timer(1.0, self.update_frontiers)

        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State):
        self.get_logger().info("Frontier Manager aktiv")
        return super().on_activate(state)

    def on_deactivate(self, state: State):
        self.get_logger().info("Frontier Manager deaktiviert")
        return super().on_deactivate(state)

    def on_cleanup(self, state: State):
        self.get_logger().info("Cleanup")
        self.destroy_subscription(self.map_sub)
        self.destroy_timer(self.timer)
        self.destroy_lifecycle_publisher(self.frontier_pub)
        self.destroy_lifecycle_publisher(self.marker_pub)
        return TransitionCallbackReturn.SUCCESS

    # ---------------------------
    # CALLBACKS
    # ---------------------------
    def map_callback(self, msg):
        self.latest_map = msg

    # ---------------------------
    # CORE LOGIC: MATHEMATIK & BILDVERARBEITUNG
    # ---------------------------
    def update_frontiers(self):
        if self.latest_map is None or not self.frontier_pub.is_activated:
            return

        # 1. Map extrahieren
        data = np.array(self.latest_map.data, dtype=np.int8)
        width = self.latest_map.info.width
        height = self.latest_map.info.height
        resolution = self.latest_map.info.resolution
        origin_x = self.latest_map.info.origin.position.x
        origin_y = self.latest_map.info.origin.position.y
        
        data = data.reshape((height, width))

        # 2. Regionen definieren
        free = (data == 0).astype(np.uint8) * 255
        unknown = (data == -1).astype(np.uint8) * 255

        # 3. Frontier Maske berechnen (Dilate auf Free, geschnitten mit Unknown)
        kernel = np.ones((3, 3), np.uint8)
        dilated_free = cv2.dilate(free, kernel, iterations=1)
        frontier_mask = cv2.bitwise_and(dilated_free, unknown)

        # 4. Räumliches Clustering (Konturen finden)
        contours, _ = cv2.findContours(frontier_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        current_frame_frontiers = []

        for contour in contours:
            area = cv2.contourArea(contour)
            
            # Filter: Zu kleine Fragmente (Sensorrauschen) ignorieren
            if area < self.min_frontier_area:
                continue

            # Schwerpunkt des Clusters im Grid berechnen (Map Coordinates)
            M = cv2.moments(contour)
            if M["m00"] == 0:
                continue
                
            cx_map = int(M["m10"] / M["m00"])
            cy_map = int(M["m01"] / M["m00"])

            # Transformation von Map (Pixel) zu World (Meter)
            cx_world = cx_map * resolution + origin_x
            cy_world = cy_map * resolution + origin_y

            current_frame_frontiers.append({
                'center_map': (cx_map, cy_map),
                'center_world': (cx_world, cy_world),
                'area': float(area),
                'timestamp': time.time()
            })

        self.track_and_update_frontiers(current_frame_frontiers)
        self.publish_data()
        self.publish_markers()

    # ---------------------------
    # CORE LOGIC: TRACKING (TEMPORAL HYSTERESIS)
    # ---------------------------
    def track_and_update_frontiers(self, current_frontiers):
        """
        Vergleicht neu gefundene Frontiers mit der bestehenden Datenbank.
        Verhindert, dass IDs bei jeder Map-Aktualisierung gelöscht und neu erstellt werden.
        """
        new_database = {}
        
        for curr_f in current_frontiers:
            best_match_id = None
            min_dist = float('inf')

            # Finde das nächste bekannte Frontier in der Datenbank
            for fid, known_f in self.active_frontiers.items():
                dx = curr_f['center_world'][0] - known_f['center_world'][0]
                dy = curr_f['center_world'][1] - known_f['center_world'][1]
                dist = math.hypot(dx, dy)

                if dist < min_dist and dist < self.tracking_distance:
                    min_dist = dist
                    best_match_id = fid

            if best_match_id is not None:
                # Update bestehendes Frontier
                f_data = self.active_frontiers[best_match_id]
                f_data['center_map'] = curr_f['center_map']
                f_data['center_world'] = curr_f['center_world']
                f_data['area'] = curr_f['area']
                f_data['last_seen'] = curr_f['timestamp']
                new_database[best_match_id] = f_data
            else:
                # Neues Frontier anlegen
                new_id = str(uuid.uuid4())[:8] # Kurze, eindeutige ID
                new_database[new_id] = {
                    'id': new_id,
                    'center_map': curr_f['center_map'],
                    'center_world': curr_f['center_world'],
                    'area': curr_f['area'],
                    'discovered_time': curr_f['timestamp'],
                    'last_seen': curr_f['timestamp'],
                    'visited': False,
                    'active': True
                }

        # Datenbank überschreiben (Frontiers, die nicht im aktuellen Frame waren, fallen raus.
        # Alternativ kann man sie auf 'active = False' setzen, wenn man eine Hysteresis will)
        self.active_frontiers = new_database

    # ---------------------------
    # OUTPUT
    # ---------------------------
    def publish_data(self):
        """ Serialisiert die Frontier-Datenbank als JSON für den Explorer """
        msg = String()
        # Nur relevante Daten exportieren
        export_data = list(self.active_frontiers.values())
        msg.data = json.dumps(export_data)
        self.frontier_pub.publish(msg)

    def publish_markers(self):
        """ Erzeugt RViz Marker zur visuellen Kontrolle """
        marker_array = MarkerArray()
        
        for idx, (fid, f) in enumerate(self.active_frontiers.items()):
            marker = Marker()
            marker.header.frame_id = self.latest_map.header.frame_id
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = "frontiers"
            marker.id = idx
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            
            # Position (World Coordinates)
            marker.pose.position.x = float(f['center_world'][0])
            marker.pose.position.y = float(f['center_world'][1])
            marker.pose.position.z = 0.0
            
            # Größe abhängig von der Frontier-Area
            scale = min(1.0, max(0.2, math.sqrt(f['area']) * 0.05))
            marker.scale.x = scale
            marker.scale.y = scale
            marker.scale.z = scale
            
            # Farbe (Cyan für aktive Frontiers)
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 1.0
            marker.color.a = 0.8
            
            marker_array.markers.append(marker)
            
            # Text Marker für die ID
            text_marker = Marker()
            text_marker.header.frame_id = self.latest_map.header.frame_id
            text_marker.ns = "frontier_labels"
            text_marker.id = idx + 1000
            text_marker.type = Marker.TEXT_VIEW_FACING
            text_marker.action = Marker.ADD
            text_marker.pose.position.x = float(f['center_world'][0])
            text_marker.pose.position.y = float(f['center_world'][1]) + scale + 0.2
            text_marker.pose.position.z = 0.0
            text_marker.scale.z = 0.3
            text_marker.color.r = 1.0
            text_marker.color.g = 1.0
            text_marker.color.b = 1.0
            text_marker.color.a = 1.0
            text_marker.text = f"F_{f['id']}"
            
            marker_array.markers.append(text_marker)

        # Marker publizieren
        if marker_array.markers:
            self.marker_pub.publish(marker_array)

def main(args=None):
    rclpy.init(args=args)
    node = FrontierManager()

    node.trigger_configure()
    node.trigger_activate()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.trigger_deactivate()
        node.trigger_cleanup()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()