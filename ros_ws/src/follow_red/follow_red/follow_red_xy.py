import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3  # x=Relative X, y=Relative Y, z=Status (1=Gefunden)
import cv2
import numpy as np
import math
from pathlib import Path

class CubeWegpunktNode(Node):
    def __init__(self, video_path: Path = 'debug_output.mp4'):
        super().__init__('cube_wegpunkt_publisher')
        self.video_path: Path = video_path

        # Topic bleibt gleich, sendet jetzt aber echte XY-Koordinaten
        self.publisher_ = self.create_publisher(Vector3, '/perception/cube_angle', 10)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.get_logger().error('Camera not found or not accessible!')

        self.frame_width = 640
        self.frame_height = 480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        # Debugging video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(str(self.video_path), fourcc, 20.0, (self.frame_width, self.frame_height))

        self.timer = self.create_timer(0.05, self.process_image_loop)

        # Kameraparameter
        self.screen_center_x = self.frame_width / 2.0
        self.fov_h_deg = 60.0

        # --- KALIBRIERUNG FÜR DISTANZSCHÄTZUNG ---
        # Stell den Würfel genau 1.0 Meter vor die Kamera und trag hier die Pixel-Fläche ein!
        self.KNOWN_DISTANCE = 1.0  # Meter
        self.KNOWN_AREA = 9750.0  # Beispielwert! Bitte mit deinem Tuner/Log abgleichen.

        # Filter
        self.alpha_position = 0.25
        self.alpha_area = 0.20
        self.last_cx = self.screen_center_x
        self.last_area = 0.0
        self.max_area_drop_ratio = 0.60

        self.get_logger().info('Cube Wegpunkt Node gestartet...')

    def create_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        lower_red1 = np.array([0, 120, 45])
        upper_red1 = np.array([5, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

        lower_red2 = np.array([174, 100, 45])
        upper_red2 = np.array([179, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)

        # Morphologisches Schließen füllt Löcher im Würfel
        kernel = np.ones((7, 7), np.uint8)
        mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # NEU: Erosion schält die ausgefransten Ränder (das Umfeld) wieder ab
        erode_kernel = np.ones((3, 3), np.uint8)
        mask_cleaned = cv2.erode(mask_closed, erode_kernel, iterations=1)

        return mask_cleaned

    def estimate_distance(self, current_area: float) -> float:
        """Schätzt die Entfernung zum Würfel basierend auf der Pixel-Fläche."""
        if current_area <= 0:
            return 0.0
        # Distanz verhält sich umgekehrt proportional zur Quadratwurzel der Fläche
        distance = self.KNOWN_DISTANCE * math.sqrt(self.KNOWN_AREA / current_area)
        return distance

    def calculate_angle(self, filtered_cx: float) -> float:
        """Berechnet den horizontalen Winkel (Links = Positiv, Rechts = Negativ)"""
        delta_x = filtered_cx - self.screen_center_x
        angle_deg = (delta_x / self.screen_center_x) * (self.fov_h_deg / 2.0)
        # Invertieren für ROS-Standard (Links von optischer Achse ist positiver Winkel)
        return -math.radians(angle_deg)

    def update_target(self, x: float, w: float, current_area: float) -> tuple[float, float]:
        raw_cx = x + (w / 2.0)

        if self.last_area < 500:
            target_cx = raw_cx
            target_area = current_area
        elif current_area < (self.last_area * self.max_area_drop_ratio):
            target_cx = self.last_cx
            target_area = self.last_area
        else:
            target_cx = self.alpha_position * raw_cx + (1 - self.alpha_position) * self.last_cx
            target_area = self.alpha_area * current_area + (1 - self.alpha_area) * self.last_area

        self.last_cx = target_cx
        self.last_area = target_area
        return target_cx, target_area

    def process_image_loop(self) -> None:
        ret, frame = self.cap.read()
        if not ret: return

        if frame.shape[1] != self.frame_width or frame.shape[0] != self.frame_height:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = self.create_mask(hsv)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Standardwerte: Kein Würfel da
        cube_detected = 0.0
        rel_x = 0.0
        rel_y = 0.0

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            current_area = cv2.contourArea(largest_contour)

            if current_area > 500:
                x, y, w, h = cv2.boundingRect(largest_contour)

                # Berechne die geschätzte quadratische Fläche basierend auf der kleineren Kante des Rechtecks
                true_edge = min(w, h)
                estimated_square_area = float(true_edge * true_edge)
                filtered_cx, filtered_area = self.update_target(x, w, estimated_square_area)

                # Winkel und Distanz basierend auf den gefilteren Werten berechnen
                angle_rad = self.calculate_angle(filtered_cx)
                distance_m = self.estimate_distance(filtered_area)

                # In relative XY-Koordinaten umrechnen
                rel_x = distance_m * math.cos(angle_rad)  # Nach vorne
                rel_y = distance_m * math.sin(angle_rad)  # Nach links
                cube_detected = 1.0

                # Zeichnen (Wir zeichnen das echte Rechteck, aber zeigen die berechneten Meter)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"X: {rel_x:.2f}m, Y: {rel_y:.2f}m", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                self.last_area *= 0.5
                self.last_cx = self.screen_center_x
        else:
            self.last_area *= 0.5
            self.last_cx = self.screen_center_x

        self.video_writer.write(frame)

        # Daten packen und senden
        msg = Vector3()
        msg.x = rel_x          # Relative X-Position zum Roboter (vorwärts)
        msg.y = rel_y          # Relative Y-Position zum Roboter (links/rechts)
        msg.z = cube_detected  # 1.0 = Getrackt, 0.0 = Verloren

        self.publisher_.publish(msg)

        if cube_detected > 0:
            self.get_logger().info(f"Wegpunkt gesendet -> X (vorne): {rel_x:.2f}m, Y (links): {rel_y:.2f}m")
        else:
            self.get_logger().info("Sende: Kein Würfel im Sichtfeld")

        cv2.imshow("Cube Wegpunkt Tracker", frame)
        cv2.waitKey(1)

    def destroy_node(self) -> None:
        self.cap.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = CubeWegpunktNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok(): rclpy.shutdown()

if __name__ == '__main__':
    main()