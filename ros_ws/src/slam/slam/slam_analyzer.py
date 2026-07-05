#!/usr/bin/env python3

import rclpy
from rclpy.lifecycle import LifecycleNode, State, TransitionCallbackReturn

from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy

from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String, Bool

import numpy as np
import cv2
import json
from collections import deque


class SlamAnalyzer(LifecycleNode):

    def __init__(self):
        super().__init__('slam_analyzer_node')

        self.get_logger().info("SLAM Analyzer gestartet")

        # ---------------------------
        # PARAMETER
        # ---------------------------
        self.history_length = 10
        self.frontier_threshold = 15.0

        # ---------------------------
        # STATE
        # ---------------------------
        self.latest_map = None
        self.start_time = None

        self.known_cells_history = deque(maxlen=self.history_length)
        self.confidence_history = deque(maxlen=self.history_length)

    # ---------------------------
    # LIFECYCLE
    # ---------------------------
    def on_configure(self, state: State) -> TransitionCallbackReturn:

        self.get_logger().info("Konfiguriere SLAM Analyzer")

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

        self.stop_sub = self.create_subscription(
            Bool,
            '/mapping_finished',
            self.stop_callback,
            10
        )

        # PUBLISHER
        self.conf_pub = self.create_lifecycle_publisher(
            String,
            '/slam_confidence',
            10
        )

        # TIMER
        self.timer = self.create_timer(2.0, self.update)

        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State):
        self.get_logger().info("Analyzer aktiv")
        return super().on_activate(state)

    def on_deactivate(self, state: State):
        self.get_logger().info("Analyzer deaktiviert")
        return super().on_deactivate(state)

    def on_cleanup(self, state: State):
        self.get_logger().info("Cleanup")

        self.destroy_subscription(self.map_sub)
        self.destroy_subscription(self.stop_sub)
        self.destroy_timer(self.timer)
        self.destroy_lifecycle_publisher(self.conf_pub)

        return TransitionCallbackReturn.SUCCESS

    # ---------------------------
    # CALLBACKS
    # ---------------------------
    def map_callback(self, msg):
        if self.start_time is None:
            self.start_time = self.get_clock().now()
            self.get_logger().info("Erste Map empfangen")

        self.latest_map = msg

    def stop_callback(self, msg: Bool):
        if msg.data:
            self.get_logger().info("Mapping beendet Signal empfangen")

    # ---------------------------
    # CORE LOGIC
    # ---------------------------
    def update(self):

        if self.latest_map is None or not self.conf_pub.is_activated:
            return

        data = np.array(self.latest_map.data, dtype=np.int8)
        width = self.latest_map.info.width
        height = self.latest_map.info.height
        data = data.reshape((height, width))

        total_cells = width * height

        # ---------------------------
        # 1. UNKNOWN RATIO
        # ---------------------------
        unknown = np.sum(data == -1)
        unknown_ratio = unknown / total_cells

        # ---------------------------
        # 2. KNOWN CELLS GROWTH
        # ---------------------------
        known = np.sum(data != -1)
        self.known_cells_history.append(known)

        if len(self.known_cells_history) > 1:
            growth = abs(self.known_cells_history[-1] - self.known_cells_history[0])
            growth_ratio = growth / (known + 1e-6)
        else:
            growth_ratio = 1.0

        # ---------------------------
        # 3. FRONTIER DETECTION
        # ---------------------------
        free = (data == 0).astype(np.uint8) * 255
        unknown_img = (data == -1).astype(np.uint8) * 255

        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(free, kernel, iterations=1)

        frontiers = cv2.bitwise_and(dilated, unknown_img)
        frontier_pixels = np.count_nonzero(frontiers)

        frontier_ratio = frontier_pixels / (total_cells + 1e-6)

        # ---------------------------
        # 4. MOTION (hier stark vereinfacht)
        # ---------------------------
        motion = growth_ratio  # Proxy für Stabilität

        # ---------------------------
        # 5. CONFIDENCE SCORE
        # ---------------------------
        Ff = max(0.0, 1.0 - frontier_ratio * 50.0)
        Fg = max(0.0, 1.0 - growth_ratio)
        Fu = max(0.0, 1.0 - unknown_ratio)
        Fm = np.exp(-motion)

        score = (
            0.4 * Ff +
            0.3 * Fg +
            0.2 * Fu +
            0.1 * Fm
        )

        self.confidence_history.append(score)
        smooth_score = np.mean(self.confidence_history)

        # ---------------------------
        # OUTPUT
        # ---------------------------
        msg = String()
        msg.data = json.dumps({
            "confidence": float(smooth_score),
            "frontier_ratio": float(frontier_ratio),
            "unknown_ratio": float(unknown_ratio),
            "growth_ratio": float(growth_ratio)
        })

        self.conf_pub.publish(msg)

        # ---------------------------
        # OPTIONAL STOP CONDITION
        # ---------------------------
        if smooth_score > 0.6:
            self.get_logger().info("SLAM KONVERGIERT (>= 97%)")


def main(args=None):
    rclpy.init(args=args)
    node = SlamAnalyzer()

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