import rclpy
from rclpy.lifecycle import LifecycleNode
from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import PoseStamped
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from pathlib import Path


class CubeWaypointNode(LifecycleNode):
    def __init__(self, video_path: Path = 'debug_output.mp4', plot_path: Path = 'debug_tracking_performance.png'):
        super().__init__('camera_processor')
        self.video_path: Path = video_path
        self.plot_path: Path = plot_path

        # --- TEST-SWITCH ---
        # True  -> Sendet .linear (Distanz) und .angular (Winkel) an die Collision Avoidance
        # False -> Sendet stattdessen PoseStamped (X/Y) an /goal_pose für Navigation
        self.declare_parameter('send_polar', True)
        self.send_polar_instead_of_xy = self.get_parameter('send_polar').get_parameter_value().bool_value

        # Kamera-/VideoWriter-Referenzen – werden erst in on_configure() geöffnet
        self.cap = None
        self.video_writer = None
        self.publisher_ = None
        self.goal_pose_publisher_ = None
        self.timer = None

        # Camera frame settings
        self.frame_width = 640
        self.frame_height = 480

        # Camera geometry parameters
        self.screen_center_x = self.frame_width / 2.0
        self.fov_h_deg = 60.0

        # --- Distance Estimation Calibration ---
        self.KNOWN_DISTANCE = 1.0  # meters
        self.KNOWN_AREA = 9750.0   # Calibrated pixel area

        # Low-pass filter configurations
        self.alpha_position = 0.25
        self.alpha_area = 0.20
        self.last_cx = self.screen_center_x
        self.last_area = 0.0
        self.max_area_drop_ratio = 0.60

        # Trajectory storage for 2D map
        self.path_x = []
        self.path_y = []

        self.get_logger().info(
            f'Cube Node gestartet. Modus: '
            f'{"POLAR (Linear/Angular)" if self.send_polar_instead_of_xy else "POSE (X/Y -> /goal_pose)"}'
        )

    def _open_camera(self) -> bool:
        """Öffnet die Kamera und konfiguriert sie."""
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            return False
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        return True

    def _create_video_writer(self):
        """Erstellt den VideoWriter für Debug-Aufzeichnung."""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(
            str(self.video_path), fourcc, 20.0, (self.frame_width, self.frame_height)
        )

    def on_configure(self) -> None:
        if not self._open_camera():
            self.get_logger().error('Camera not found or not accessible!')
            return rclpy.lifecycle.TransitionCallbackReturn.FAILURE

        self._create_video_writer()

        if self.send_polar_instead_of_xy:
            self.publisher_ = self.create_publisher(TargetVector, '/target_vector', 10)
            self.goal_pose_publisher_ = None
        else:
            self.goal_pose_publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)
            self.publisher_ = None

        # Core processing loop timer (20 Hz)
        self.timer = self.create_timer(0.05, self.process_image_loop)

        self.get_logger().info('Lifecycle Node configured.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def on_activate(self) -> None:
        if self.publisher_:
            self.publisher_.on_activate()
        if self.goal_pose_publisher_:
            self.goal_pose_publisher_.on_activate()
        self.get_logger().info('Lifecycle Node activated.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def on_deactivate(self) -> None:
        if self.publisher_:
            self.publisher_.on_deactivate()
        if self.goal_pose_publisher_:
            self.goal_pose_publisher_.on_deactivate()
        self.get_logger().info('Lifecycle Node deactivated.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def _cleanup_resources(self):
        """Gibt Kamera, VideoWriter und Timer frei."""
        if self.timer is not None:
            self.destroy_timer(self.timer)
            self.timer = None
        if self.publisher_ is not None:
            self.publisher_.on_cleanup()
            self.publisher_ = None
        if self.goal_pose_publisher_ is not None:
            self.goal_pose_publisher_.on_cleanup()
            self.goal_pose_publisher_ = None
        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        cv2.destroyAllWindows()

    def on_cleanup(self) -> None:
        self._cleanup_resources()
        self.get_logger().info('Lifecycle Node cleaned up.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state) -> None:
        self._cleanup_resources()
        if self.path_x:
            self.plot_data()
        self.get_logger().info('Lifecycle Node shut down.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def create_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        lower_red1 = np.array([0, 140, 70])
        upper_red1 = np.array([5, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

        lower_red2 = np.array([174, 140, 70])
        upper_red2 = np.array([179, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)
        kernel = np.ones((7, 7), np.uint8)
        mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        erode_kernel = np.ones((3, 3), np.uint8)
        return cv2.erode(mask_closed, erode_kernel, iterations=1)

    def estimate_distance(self, current_area: float) -> float:
        if current_area <= 0:
            return 0.0
        return self.KNOWN_DISTANCE * math.sqrt(self.KNOWN_AREA / current_area)

    def calculate_angle(self, filtered_cx: float) -> float:
        delta_x = filtered_cx - self.screen_center_x
        angle_deg = (delta_x / self.screen_center_x) * (self.fov_h_deg / 2.0)
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
        if self.cap is None or not self.cap.isOpened():
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        if frame.shape[1] != self.frame_width or frame.shape[0] != self.frame_height:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = self.create_mask(hsv)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cube_detected = 0.0
        val_linear = 0.0
        val_angular = 0.0

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            current_area = cv2.contourArea(largest_contour)

            if current_area > 500:
                x, y, w, h = cv2.boundingRect(largest_contour)
                true_edge = min(w, h)
                estimated_square_area = float(true_edge * true_edge)
                filtered_cx, filtered_area = self.update_target(x, w, estimated_square_area)

                angle_rad = self.calculate_angle(filtered_cx)
                distance_m = self.estimate_distance(filtered_area)

                # Für deinen Map-Plot im Hintergrund behalten wir echten XY-Werte bei
                rel_x = distance_m * math.cos(angle_rad)
                rel_y = distance_m * math.sin(angle_rad)
                self.path_x.append(rel_x)
                self.path_y.append(rel_y)
                cube_detected = 1.0

                # --- SWITCH LOGIK FÜR DAS GEWÜNSCHTE OUTPUT FORMAT ---
                if self.send_polar_instead_of_xy:
                    # Genauso will es die Collision Avoidance haben:
                    val_linear = distance_m
                    val_angular = angle_rad
                    overlay_text = f"Lin: {val_linear:.2f}m, Ang: {math.degrees(val_angular):.1f}deg"
                else:
                    # Altes Verhalten (Testzwecke)
                    val_linear = rel_x
                    val_angular = rel_y
                    overlay_text = f"X: {val_linear:.2f}m, Y: {val_angular:.2f}m"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, overlay_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                self.last_area *= 0.5
                self.last_cx = self.screen_center_x
        else:
            self.last_area *= 0.5
            self.last_cx = self.screen_center_x

        if self.video_writer is not None:
            self.video_writer.write(frame)

        if val_linear == 0.0 and val_angular == 0.0:
            return

        if self.send_polar_instead_of_xy:
            if self.publisher_ is not None:
                msg = TargetVector()
                msg.linear = val_linear
                msg.angular = val_angular
                self.publisher_.publish(msg)
        else:
            if self.goal_pose_publisher_ is not None:
                msg = PoseStamped()
                msg.header.frame_id = 'map'
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.pose.position.x = val_linear
                msg.pose.position.y = val_angular
                msg.pose.position.z = 0.0
                msg.pose.orientation.w = 1.0
                self.goal_pose_publisher_.publish(msg)

        if cube_detected > 0:
            self.get_logger().info(f"Sende Target -> Linear: {val_linear:.2f}, Angular: {val_angular:.2f}")

    def plot_data(self) -> None:
        if not self.path_x:
            return
        plt.figure(figsize=(8, 8))
        plt.plot(self.path_y, self.path_x, label='Cube Trajectory', color='red', marker='o', markersize=3, alpha=0.6)
        plt.scatter(0, 0, color='blue', s=150, marker='^', label='Robot (Origin)')
        plt.xlabel('Y (Lateral) / Meters')
        plt.ylabel('X (Forward) / Meters')
        plt.axis('equal')
        plt.grid(True)
        plt.savefig(self.plot_path)
        plt.close()

    def destroy_node(self) -> None:
        self._cleanup_resources()
        if self.path_x:
            self.plot_data()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CubeWaypointNode()
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