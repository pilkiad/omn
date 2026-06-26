import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np
import os
from collections import deque
import matplotlib.pyplot as plt
from pathlib import Path

class CubeFollowerNode(Node):
    def __init__(self, video_path: Path = 'debug_output.mp4', plot_path: Path = 'tracking_performance.png'):
        super().__init__('cube_follower')
        self.video_path: Path = video_path
        self.plot_path: Path = plot_path
        self.publisher_ = self.create_publisher(Twist, '/base/cmd_vel', 10)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.get_logger().error('Camera not found or not accessible. Please check your connection and try again.!')

        self.frame_width = 640
        self.frame_height = 480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        # Debugging video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(str(self.video_path), fourcc, 20.0, (self.frame_width, self.frame_height))

        # Timer (20 HZ)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.process_image_loop)

        # Roationscaler
        self.screen_center_x = self.frame_width / 2.0
        self.angular_gain = 0.002

        # Forward speedscaler
        self.target_area = 20000.0   # Nearest Cube position
        self.linear_gain = 0.00001
        self.max_linear_speed = 1.0

        self.get_logger().info('Cube Follower Node started...')

        # Filter-Configuration
        self.alpha_position = 0.25 # Weighting new position on old position
        self.alpha_area = 0.20 # Weighting new area on old area

        # Last known position and area
        self.last_cx = self.screen_center_x
        self.last_area = 0.0

        # Gating-Configuration
        self.max_area_drop_ratio = 0.60

        # Data for plotting
        self.raw_areas = []
        self.filtered_areas = []
        self.linear_speeds = []
        self.angular_speeds = []
        self.timestamps = []
        self.start_time = self.get_clock().now()

    def create_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        # Optimierte Rot-Filterung aus dem Tuner (Beide Enden des HSV-Kreises)
        lower_red1 = np.array([0, 100, 45])
        upper_red1 = np.array([5, 255, 255])  # Angepasst auf deine 45° (OpenCV-Hue 22)
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

        lower_red2 = np.array([174, 100, 45]) # Spiegelung: 179 - 22
        upper_red2 = np.array([179, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)

        # Morphologisches Schließen füllt Löcher im blutroten Würfel
        kernel = np.ones((7, 7), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        return mask

    def calculate_speed(self, x: int, w: int) -> tuple[float, float]:
        """
        Calculates smoothly scaled linear and angular speeds.
        """
        # 1. Rotation
        error_x: float = self.screen_center_x - self.last_cx
        angular_speed: float = error_x * self.angular_gain

        # 2. Basis-Vorwärtsgeschwindigkeit
        error_area: float = self.target_area - self.last_area
        base_linear_speed = 0.0

        if error_area > 0:
            base_linear_speed = error_area * self.linear_gain
            base_linear_speed = min(base_linear_speed, self.max_linear_speed)

        # 3. WEICHE BREMSE (Scaling Factor):
        max_allowed_error = 100.0  # Erhöht von 60, da wir jetzt weich ausblenden!

        # Berechne den Skalierungsfaktor zwischen 0.0 und 1.0
        scaling_factor = 1.0 - (min(abs(error_x), max_allowed_error) / max_allowed_error)

        # Sicherheitsstopp, wenn die Wand berührt wird
        touches_wall: bool = (x <= 2) or ((x + w) >= (self.frame_width - 2))
        if touches_wall:
            scaling_factor = 0.0

        # Berechne die gewünschte lineare Geschwindigkeit für diesen Frame
        target_linear_speed = base_linear_speed * scaling_factor

        # 4. STOSSDÄMPFER FÜR DIE MOTOREN (Geschwindigkeitsglättung)
        # Verhindert, dass der Roboter beim plötzlichen Verlust abrupt stoppt.
        alpha_speed = 0.30  # Wie schnell die Motoren auf Änderungen reagieren dürfen

        # Wir holen uns die echte aktuelle Geschwindigkeit (falls vorhanden) oder nutzen das Letzte aus der Liste
        last_sent_linear = self.linear_speeds[-1] if self.linear_speeds else 0.0

        smoothed_linear_speed = alpha_speed * target_linear_speed + (1 - alpha_speed) * last_sent_linear

        return smoothed_linear_speed, angular_speed

    def update_target_position_and_area(self, x: float, w: float, current_area: float) -> tuple[float, float]:
        raw_cx = x + (w / 2.0)

        # FIX: Fall 1 - Wenn der Würfel neu im Bild erscheint, Filter überspringen
        if self.last_area < 500:
            target_cx = raw_cx
            target_area = current_area

        # FIX: Fall 2 - Gating greift NUR bei unplausibel heftigen Einbrüchen nach unten
        elif current_area < (self.last_area * self.max_area_drop_ratio):
            target_cx = self.last_cx
            target_area = self.last_area

        # FIX: Fall 3 - Normalbetrieb oder Flächenzunahme (wird sofort akzeptiert & geglättet)
        else:
            target_cx = self.alpha_position * raw_cx + (1 - self.alpha_position) * self.last_cx
            target_area = self.alpha_area * current_area + (1 - self.alpha_area) * self.last_area

        self.last_cx = target_cx
        self.last_area = target_area
        return target_cx, target_area

    def process_image_loop(self) -> None:
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warn('Image not readable!')
            return

        if frame.shape[1] != self.frame_width or frame.shape[0] != self.frame_height:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = self.create_mask(hsv)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        linear_speed = 0.0
        angular_speed = 0.0
        current_area = 0.0
        target_area = 0.0

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            current_area = cv2.contourArea(largest_contour)

            if current_area > 500:
                x, y, w, h = cv2.boundingRect(largest_contour)
                # Holt sich die gefilterten Werte zurück
                _, target_area = self.update_target_position_and_area(x, w, current_area)
                linear_speed, angular_speed = self.calculate_speed(x, w)

                # Draw
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"Area: {int(target_area)}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                self.last_area *= 0.5
                target_area = self.last_area
                self.last_cx = self.screen_center_x # Setzt Rotation im Verlustfall zurück
        else:
            self.last_area *= 0.5
            target_area = self.last_area
            self.last_cx = self.screen_center_x # Setzt Rotation im Verlustfall zurück

        elapsed_time = (self.get_clock().now() - self.start_time).nanoseconds / 1e9

        # Save data for plotting
        self.timestamps.append(elapsed_time)
        self.raw_areas.append(current_area)
        self.filtered_areas.append(target_area)
        self.linear_speeds.append(linear_speed)
        self.angular_speeds.append(angular_speed)

        self.video_writer.write(frame)

        msg = Twist()
        msg.linear.x = linear_speed
        msg.angular.z = angular_speed
        self.publisher_.publish(msg)
        self.get_logger().info(f"Send: Linear={linear_speed:.2f}, Angular={angular_speed:.2f}")

        cv2.imshow("Cube Tracking", frame)
        cv2.waitKey(1)

    def plot_data(self) -> None:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        # Plot 1: Flächenfilterung
        ax1.plot(self.timestamps, self.raw_areas, label='Fläche Roh (Messung)', color='red', alpha=0.5)
        ax1.plot(self.timestamps, self.filtered_areas, label='Fläche Gefiltert', color='green', linewidth=2)
        ax1.set_ylabel('Pixel-Fläche')
        ax1.set_title('Flächenfilterung & Robotergeschwindigkeiten')
        ax1.legend()
        ax1.grid(True)

        # Plot 2: Ausgegebenen Geschwindigkeiten
        ax2.plot(self.timestamps, self.linear_speeds, label='Linear Speed (x)', color='blue')
        ax2.plot(self.timestamps, self.angular_speeds, label='Angular Speed (z)', color='orange')
        ax2.set_xlabel('Zeit (Sekunden)')
        ax2.set_ylabel('Geschwindigkeit (m/s bzw. rad/s)')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()
        plt.savefig(self.plot_path)
        self.get_logger().info(f'Plot erfolgreich gespeichert unter: {str(self.plot_path)}')

    def destroy_node(self) -> None:
        self.cap.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
        self.get_logger().info('Video saved.')

        if self.timestamps:
            self.plot_data()

        super().destroy_node()

def run_hsv_tuner() -> None:
    """Optimierter HSV-Tuner für Rot-/Blutrot-Töne (erfasst beide Enden des Farbkreises)"""
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Tuner")

    # Trackbars erstellen
    # "Rot-Bereich" bestimmt, wie weit wir von der 0 nach oben UND von 179 nach unten gehen
    cv2.createTrackbar("Rot-Bereich (H)", "Tuner", 10, 45, lambda x: None)
    cv2.createTrackbar("Min S", "Tuner", 100, 255, lambda x: None)
    cv2.createTrackbar("Max S", "Tuner", 255, 255, lambda x: None)
    cv2.createTrackbar("Min V", "Tuner", 45, 255, lambda x: None)
    cv2.createTrackbar("Max V", "Tuner", 255, 255, lambda x: None)

    print("--- ROT-TUNER GESTARTET ---")
    print("Drücke 'q' zum Beenden.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Werte auslesen
        h_range = cv2.getTrackbarPos("Rot-Bereich (H)", "Tuner")
        s_min = cv2.getTrackbarPos("Min S", "Tuner")
        s_max = cv2.getTrackbarPos("Max S", "Tuner")
        v_min = cv2.getTrackbarPos("Min V", "Tuner")
        v_max = cv2.getTrackbarPos("Max V", "Tuner")

        # Maske 1: Von 0 bis H-Bereich
        lower1 = np.array([0, s_min, v_min])
        upper1 = np.array([h_range, s_max, v_max])
        mask1 = cv2.inRange(hsv, lower1, upper1)

        # Maske 2: Von (179 - H-Bereich) bis 179
        lower2 = np.array([179 - h_range, s_min, v_min])
        upper2 = np.array([179, s_max, v_max])
        mask2 = cv2.inRange(hsv, lower2, upper2)

        # Kombinieren
        mask = cv2.bitwise_or(mask1, mask2)

        # Optional: Direkt das Morphologie-Ergebnis anzeigen lassen!
        kernel = np.ones((7, 7), np.uint8)
        mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Live-Anzeige (Oben: Reine Maske, Unten: Nach Morphologie)
        cv2.imshow("Tuner", np.hstack([mask, mask_closed]))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n--- DEINE OPTIMALEN WERTE FÜR DEN CODE: ---")
            print(f"lower_red1 = np.array([0, {s_min}, {v_min}])")
            print(f"upper_red1 = np.array([{h_range}, {s_max}, {v_max}])")
            print(f"lower_red2 = np.array([{179 - h_range}, {s_min}, {v_min}])")
            print(f"upper_red2 = np.array([179, {s_max}, {v_max}])\n")
            break

    cap.release()
    cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = CubeFollowerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()