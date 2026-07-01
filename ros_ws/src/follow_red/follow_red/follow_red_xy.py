import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3  # x = Relative X, y = Relative Y, z = Status (1.0 = Found)
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from pathlib import Path

class CubeWegpunktNode(Node):
    def __init__(self, video_path: Path = 'debug_output.mp4', plot_path: Path = 'tracking_performance.png'):
        super().__init__('cube_wegpunkt_publisher')
        self.video_path: Path = video_path
        self.plot_path: Path = plot_path

        # Publisher for the relative position of the tracked cube
        self.publisher_ = self.create_publisher(Vector3, '/perception/cube_angle', 10)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.get_logger().error('Camera not found or not accessible!')

        # Camera frame settings
        self.frame_width = 640
        self.frame_height = 480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        # Video writer for debugging
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(str(self.video_path), fourcc, 20.0, (self.frame_width, self.frame_height))

        # Core processing loop timer (20 Hz)
        self.timer = self.create_timer(0.05, self.process_image_loop)

        # Camera geometry parameters
        self.screen_center_x = self.frame_width / 2.0
        self.fov_h_deg = 60.0

        # --- Distance Estimation Calibration ---
        # Calibration baseline: Cube placed at exactly 1.0 meter from the camera
        self.KNOWN_DISTANCE = 1.0  # meters
        self.KNOWN_AREA = 9750.0   # Calibrated pixel area

        # Low-pass filter configurations and outlier handling
        self.alpha_position = 0.25
        self.alpha_area = 0.20
        self.last_cx = self.screen_center_x
        self.last_area = 0.0
        self.max_area_drop_ratio = 0.60

        # Trajectory storage for post-processing evaluation map
        self.path_x = []
        self.path_y = []

        self.get_logger().info('Cube Wegpunkt Node started. Path recording active.')

    def create_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        """Filters the HSV image for red color ranges and applies morphological cleaning."""
        # Red color wraps around the HSV 0/180 boundary -> two masks required
        lower_red1 = np.array([0, 120, 45])
        upper_red1 = np.array([5, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

        lower_red2 = np.array([174, 100, 45])
        upper_red2 = np.array([179, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)

        # Morphological close to fill holes within the detected cube
        kernel = np.ones((7, 7), np.uint8)
        mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Erosion to remove small noisy peripheral artifacts
        erode_kernel = np.ones((3, 3), np.uint8)
        mask_cleaned = cv2.erode(mask_closed, erode_kernel, iterations=1)

        return mask_cleaned

    def estimate_distance(self, current_area: float) -> float:
        """Estimates distance based on the inverse square root law of the pixel area."""
        if current_area <= 0:
            return 0.0
        return self.KNOWN_DISTANCE * math.sqrt(self.KNOWN_AREA / current_area)

    def calculate_angle(self, filtered_cx: float) -> float:
        """Calculates horizontal angle in radians (Positive = Left, Negative = Right) per ROS standard."""
        delta_x = filtered_cx - self.screen_center_x
        angle_deg = (delta_x / self.screen_center_x) * (self.fov_h_deg / 2.0)
        return -math.radians(angle_deg)

    def update_target(self, x: float, w: float, current_area: float) -> tuple[float, float]:
        """Applies a low-pass filter to the target center and area to smooth out noise."""
        raw_cx = x + (w / 2.0)

        # Initialization phase
        if self.last_area < 500:
            target_cx = raw_cx
            target_area = current_area
        # Outlier rejection (sudden drastic area drop)
        elif current_area < (self.last_area * self.max_area_drop_ratio):
            target_cx = self.last_cx
            target_area = self.last_area
        # Standard Exponential Moving Average (EMA) filter
        else:
            target_cx = self.alpha_position * raw_cx + (1 - self.alpha_position) * self.last_cx
            target_area = self.alpha_area * current_area + (1 - self.alpha_area) * self.last_area

        self.last_cx = target_cx
        self.last_area = target_area
        return target_cx, target_area

    def process_image_loop(self) -> None:
        """Main capture, processing, and ROS publishing loop."""
        ret, frame = self.cap.read()
        if not ret:
            return

        if frame.shape[1] != self.frame_width or frame.shape[0] != self.frame_height:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = self.create_mask(hsv)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Default values: No cube detected
        cube_detected = 0.0
        rel_x = 0.0
        rel_y = 0.0

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            current_area = cv2.contourArea(largest_contour)

            if current_area > 500: # Minimum pixel threshold
                x, y, w, h = cv2.boundingRect(largest_contour)

                # Use the shorter side to compute a robust bounding square area independent of orientation angles
                true_edge = min(w, h)
                estimated_square_area = float(true_edge * true_edge)
                filtered_cx, filtered_area = self.update_target(x, w, estimated_square_area)

                angle_rad = self.calculate_angle(filtered_cx)
                distance_m = self.estimate_distance(filtered_area)

                # Transform polar coordinates to relative Cartesian coordinates (ROS frame: X=Forward, Y=Left)
                rel_x = distance_m * math.cos(angle_rad)
                rel_y = distance_m * math.sin(angle_rad)
                cube_detected = 1.0

                # Cache track data for plotting
                self.path_x.append(rel_x)
                self.path_y.append(rel_y)

                # Draw telemetry on the frame
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

        # Construct and publish message
        msg = Vector3()
        msg.x = rel_x          # Forward relative distance (meters)
        msg.y = rel_y          # Lateral relative distance (meters, left is positive)
        msg.z = cube_detected  # Tracking flag status (1.0 = Tracked, 0.0 = Lost)
        self.publisher_.publish(msg)

        if cube_detected > 0:
            self.get_logger().info(f"Waypoint sent -> X (forward): {rel_x:.2f}m, Y (left): {rel_y:.2f}m")
        else:
            self.get_logger().info("Sende: No target cube in sight")

        cv2.imshow("Cube Wegpunkt Tracker", frame)
        cv2.waitKey(1)

    def plot_data(self) -> None:
        """Generates and saves a 2D map of the tracked cube trajectory relative to the robot."""
        if not self.path_x:
            self.get_logger().warn('No path data available to generate map.')
            return

        plt.figure(figsize=(8, 8))

        # Map ROS coordinates to the plot layout (ROS X -> Plot Y, ROS Y -> Plot X)
        plt.plot(self.path_y, self.path_x, label='Cube Trajectory (Relative)', color='red', marker='o', markersize=3, alpha=0.6)

        # Highlight key positions
        plt.scatter(self.path_y[0], self.path_x[0], color='green', s=100, label='Start Position', zorder=5)
        plt.scatter(self.path_y[-1], self.path_x[-1], color='darkred', s=100, label='Last Position', zorder=5)

        # Robot origin position (0,0)
        plt.scatter(0, 0, color='blue', s=150, marker='^', label='Robot (Origin)', zorder=6)

        # Labeling according to ROS standard conventions
        plt.xlabel('Y-Coordinate / Lateral Deviation (Meters)')
        plt.ylabel('X-Coordinate / Forward Distance (Meters)')
        plt.title('2D Waypoint Map: Relative Target Trajectory')

        plt.axis('equal')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()

        plt.tight_layout()
        plt.savefig(self.plot_path)
        self.get_logger().info(f'Waypoint map successfully saved to: {str(self.plot_path)}')
        plt.close()

    def destroy_node(self) -> None:
        """Releases hardware resources and triggers final plot generation on shutdown."""
        self.cap.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
        self.get_logger().info('Video resources released.')

        if self.path_x:
            self.plot_data()

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
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()