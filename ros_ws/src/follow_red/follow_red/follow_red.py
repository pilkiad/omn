import rclpy
from rclpy.lifecycle import LifecycleNode
from collision_interfaces.msg import TargetVector
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
import cv2
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from collections import deque


class CubeWaypointNode(LifecycleNode):
    def __init__(self, video_path: Path = 'debug_output.mp4', plot_path: Path = 'debug_tracking_performance.png'):
        super().__init__('camera_processor')
        self.video_path: Path = video_path
        self.plot_path: Path = plot_path

        self.declare_parameter('send_polar', True)
        self.send_polar_instead_of_xy = self.get_parameter('send_polar').get_parameter_value().bool_value

        self.cap = None
        self.video_writer = None
        self.publisher_ = None
        self.goal_pose_publisher_ = None
        self.status_publisher = None
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

        # Ringbuffer for smooth movement detection
        self.history_len = 5
        self.history_x = deque(maxlen=self.history_len)
        self.history_y = deque(maxlen=self.history_len)

        # Deadband for movement detection
        self.MOVEMENT_THRESHOLD = 0.15
        self.last_sent_x = None
        self.last_sent_y = None

        # Trajectory storage for 2D map
        self.path_x = []
        self.path_y = []

        # Throttled logging
        self._frame_count = 0
        self._log_interval = 40  # log every 40 frames (~2s at 20Hz)

        self.get_logger().info(
            f'[__init__] Cube Node created (state=unconfigured). Modus: '
            f'{"POLAR (Linear/Angular)" if self.send_polar_instead_of_xy else "POSE (X/Y -> /goal_pose)"}'
            f' -- Waiting for trigger_configure() ...'
        )

    def _open_camera(self) -> bool:
        self.get_logger().info('_open_camera: trying cv2.VideoCapture(0) ...')
        self.cap = cv2.VideoCapture(0)
        opened = self.cap.isOpened()
        self.get_logger().info(f'_open_camera: cv2.VideoCapture(0).isOpened() = {opened}')
        if not opened:
            self.get_logger().error('_open_camera: FAILED - camera not accessible')
            return False
        self.get_logger().info('_open_camera: camera opened, setting frame size ...')
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        self.get_logger().info(f'_open_camera: SUCCESS (frame={self.frame_width}x{self.frame_height})')
        return True

    def _create_video_writer(self):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(
            str(self.video_path), fourcc, 20.0, (self.frame_width, self.frame_height)
        )

    def on_configure(self, state) -> rclpy.lifecycle.TransitionCallbackReturn:
        self.get_logger().info('on_configure: starting ...')
        self.get_logger().info(f'on_configure: send_polar={self.send_polar_instead_of_xy}')

        self.get_logger().info('on_configure: calling _open_camera ...')
        if not self._open_camera():
            self.get_logger().error('on_configure: FAILED - camera not found or not accessible')
            return rclpy.lifecycle.TransitionCallbackReturn.FAILURE

        self.get_logger().info('on_configure: calling _create_video_writer ...')
        self._create_video_writer()
        self.get_logger().info('on_configure: video writer created')

        if self.send_polar_instead_of_xy:
            self.get_logger().info('on_configure: creating TargetVector publisher on /target_vector')
            self.publisher_ = self.create_lifecycle_publisher(TargetVector, '/target_vector', 10)
            self.goal_pose_publisher_ = None
        else:
            self.get_logger().info('on_configure: creating PoseStamped publisher on /goal_pose')
            self.goal_pose_publisher_ = self.create_lifecycle_publisher(PoseStamped, '/goal_pose', 10)
            self.publisher_ = None

        self.get_logger().info('on_configure: creating status publisher on /follow_red_status ...')
        self.status_publisher = self.create_lifecycle_publisher(String, '/follow_red_status', 10)

        self.get_logger().info('on_configure: publisher created, creating timer ...')
        self.timer = self.create_timer(0.05, self.process_image_loop)

        self.get_logger().info('on_configure: SUCCESS - Lifecycle Node configured.')
        self._publish_status('configured')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def on_activate(self, state) -> rclpy.lifecycle.TransitionCallbackReturn:
        self._frame_count = 0
        self.history_x.clear()
        self.history_y.clear()
        self.last_sent_x = None
        self.last_sent_y = None

        self.get_logger().info(
            f'Lifecycle Node ACTIVATED. '
            f'Publisher: {"target_vector" if self.send_polar_instead_of_xy else "goal_pose"} '
            f'(exists={self.publisher_ is not None or self.goal_pose_publisher_ is not None})'
        )

        self._publish_status('active')
        return super().on_activate(state)

    def on_deactivate(self, state) -> rclpy.lifecycle.TransitionCallbackReturn:
        self.get_logger().info('Lifecycle Node deactivated.')
        self._publish_status('inactive')
        return super().on_deactivate(state)

    def _cleanup_resources(self):
        if self.timer is not None:
            self.destroy_timer(self.timer)
            self.timer = None
        if self.publisher_ is not None:
            self.destroy_lifecycle_publisher(self.publisher_)
            self.publisher_ = None
        if self.goal_pose_publisher_ is not None:
            self.destroy_lifecycle_publisher(self.goal_pose_publisher_)
            self.goal_pose_publisher_ = None
        if self.status_publisher is not None:
            self.destroy_lifecycle_publisher(self.status_publisher)
            self.status_publisher = None
        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        cv2.destroyAllWindows()

    def on_cleanup(self, state) -> rclpy.lifecycle.TransitionCallbackReturn:
        self._publish_status('unconfigured')
        self._cleanup_resources()
        self.get_logger().info('Lifecycle Node cleaned up.')
        return rclpy.lifecycle.TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state) -> rclpy.lifecycle.TransitionCallbackReturn:
        self._publish_status('shutdown')
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

    def _publish_status(self, status: str):
        if self.status_publisher is not None and self.status_publisher.is_activated:
            msg = String()
            msg.data = status
            self.status_publisher.publish(msg)

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
        self._frame_count += 1
        throttled = (self._frame_count % self._log_interval == 0)

        if self.cap is None or not self.cap.isOpened():
            if throttled:
                self.get_logger().warn(
                    f'[frame={self._frame_count}] Camera not open! cap={self.cap is not None}, '
                    f'isOpened={self.cap.isOpened() if self.cap else "N/A"}'
                )
            return

        ret, frame = self.cap.read()
        if not ret:
            if throttled:
                self.get_logger().warn(f'[frame={self._frame_count}] cap.read() returned False')
            return

        if throttled:
            self.get_logger().info(
                f'[frame={self._frame_count}] Camera reading OK, shape={frame.shape}'
            )

        if frame.shape[1] != self.frame_width or frame.shape[0] != self.frame_height:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = self.create_mask(hsv)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cube_detected = False
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

                rel_x = distance_m * math.cos(angle_rad)
                rel_y = distance_m * math.sin(angle_rad)

                self.history_x.append(rel_x)
                self.history_y.append(rel_y)

                smooth_x = np.median(self.history_x)
                smooth_y = np.median(self.history_y)

                self.path_x.append(smooth_x)
                self.path_y.append(smooth_y)
                cube_detected = True

                smooth_distance = math.hypot(smooth_x, smooth_y)
                smooth_angle = math.atan2(smooth_y, smooth_x)

                if throttled:
                    self.get_logger().info(
                        f'[frame={self._frame_count}] CUBE DETECTED: '
                        f'area={current_area:.0f}px, distance={smooth_distance:.2f}m, angle={math.degrees(smooth_angle):.1f}°'
                    )

                should_send = False
                if self.last_sent_x is None or self.last_sent_y is None:
                    should_send = True
                else:
                    move_distance = math.hypot(smooth_x - self.last_sent_x, smooth_y - self.last_sent_y)
                    if move_distance >= self.MOVEMENT_THRESHOLD:
                        should_send = True

                if should_send:
                    self.last_sent_x = smooth_x
                    self.last_sent_y = smooth_y

                    if self.send_polar_instead_of_xy:
                        val_linear = smooth_distance
                        val_angular = smooth_angle
                        self._publish_status(f'tracking: lin={val_linear:.2f}, ang={math.degrees(val_angular):.0f}°')
                    else:
                        val_linear = smooth_x
                        val_angular = smooth_y
                        self._publish_status(f'goal_pose: x={val_linear:.2f}, y={val_angular:.2f}')
                else:
                    if throttled:
                        self.get_logger().info(f'[frame={self._frame_count}] Target movement within deadband. Skipping publish.')

                overlay_text = f"X: {smooth_x:.2f}m, Y: {smooth_y:.2f}m" if not self.send_polar_instead_of_xy else f"Lin: {smooth_distance:.2f}m, Ang: {math.degrees(smooth_angle):.1f}°"
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, overlay_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                self.last_area *= 0.5
                self.last_cx = self.screen_center_x
        else:
            self.last_area *= 0.5
            self.last_cx = self.screen_center_x

        if throttled and contours:
            largest_contour = max(contours, key=cv2.contourArea)
            max_area = cv2.contourArea(largest_contour)
            if max_area <= 500:
                self.get_logger().info(
                    f'[frame={self._frame_count}] {len(contours)} contour(s) found, '
                    f'largest area={max_area:.0f}px (< 500 threshold)'
                )
                self._publish_status('searching')
        elif throttled and not contours:
            self.get_logger().info(f'[frame={self._frame_count}] No red contours detected')
            self._publish_status('searching')

        if self.video_writer is not None:
            self.video_writer.write(frame)

        if val_linear == 0.0 and val_angular == 0.0:
            return

        if self.send_polar_instead_of_xy:
            if self.publisher_ is not None and self.publisher_.is_activated:
                msg = TargetVector()
                msg.linear = val_linear
                msg.angular = val_angular
                self.publisher_.publish(msg)
                if throttled:
                    self.get_logger().info(
                        f'[frame={self._frame_count}] PUBLISHED to /target_vector: '
                        f'linear={val_linear:.2f}m, angular={math.degrees(val_angular):.1f}°'
                    )
            elif throttled:
                self.get_logger().error(
                    f'[frame={self._frame_count}] Cannot publish: self.publisher_ is None!'
                )
        else:
            if self.goal_pose_publisher_ is not None and self.goal_pose_publisher_.is_activated:
                msg = PoseStamped()
                msg.header.frame_id = 'base_footprint'
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.pose.position.x = val_linear
                msg.pose.position.y = val_angular
                msg.pose.position.z = 0.0
                msg.pose.orientation.w = 1.0
                self.goal_pose_publisher_.publish(msg)
                if throttled:
                    self.get_logger().info(
                        f'[frame={self._frame_count}] PUBLISHED to /goal_pose: '
                        f'x={val_linear:.2f}m, y={val_angular:.2f}m'
                    )
            elif throttled:
                self.get_logger().error(
                    f'[frame={self._frame_count}] Cannot publish: /goal_pose publisher is None or not activated!'
                )

    def plot_data(self) -> None:
        if not self.path_x:
            return
        plt.figure(figsize=(8, 8))
        plt.plot(self.path_y, self.path_x, label='Cube Trajectory (Filtered)', color='red', marker='o', markersize=3, alpha=0.6)
        plt.scatter(0, 0, color='blue', s=150, marker='^', label='Robot (Origin)')
        plt.xlabel('Y (Lateral) / Meters')
        plt.ylabel('X (Forward) / Meters')
        plt.axis('equal')
        plt.grid(True)
        plt.savefig(self.plot_path)
        plt.close()

    def destroy_node(self) -> None:
        self._cleanup_resources()
        super().destroy_node()


def main():
    rclpy.init()
    node = CubeWaypointNode()

    node.trigger_configure()
    node.trigger_activate()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.path_x:
            node.plot_data()

        try:
            node.trigger_deactivate()
            node.trigger_cleanup()
            node.trigger_shutdown()
        except Exception:
            pass

        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()