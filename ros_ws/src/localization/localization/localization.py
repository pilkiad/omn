import math
import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped


class ScanMatcherLocalization(Node):

    def __init__(self):
        super().__init__("scan_match_localization")

        # Map + scan
        self.map = None
        self.scan = None

        self.have_map = False
        self.have_scan = False

        # Current pose estimate (MAP frame)
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Subscriptions
        self.create_subscription(OccupancyGrid, "/map", self.map_cb, 1)
        self.create_subscription(LaserScan, "/scan", self.scan_cb, 1)

        # Output pose
        self.pose_pub = self.create_publisher(PoseStamped, "/pos", 10)

        # Main loop
        self.timer = self.create_timer(0.2, self.update)

        self.get_logger().info("Scan matcher localization started (NO ODOM MODE)")

    # ---------------- CALLBACKS ----------------

    def map_cb(self, msg):
        self.map = msg
        self.have_map = True

    def scan_cb(self, msg):
        self.scan = msg
        self.have_scan = True

    # ---------------- MAIN LOOP ----------------

    def update(self):

        if not (self.have_map):
            self.get_logger().warn("Waiting for map")
            return
        if not (self.have_scan):
            self.get_logger().warn("Waiting for scan")
            return

        self.localize()
        self.publish_pose()

    # ---------------- LOCALIZATION ----------------

    def localize(self):

        best_score = -1e9
        best_x = self.x
        best_y = self.y
        best_theta = self.theta

        # SEARCH WINDOW (must be large without odom)
        SEARCH_X = 2.0
        SEARCH_Y = 2.0
        SEARCH_THETA = math.radians(180)

        STEP_X = 0.10
        STEP_Y = 0.10
        STEP_THETA = math.radians(10)

        ox = self.map.info.origin.position.x
        oy = self.map.info.origin.position.y
        res = self.map.info.resolution
        width = self.map.info.width
        height = self.map.info.height
        grid = self.map.data

        def score_pose(px, py, pth):

            score = 0.0

            for i, r in enumerate(self.scan.ranges):

                if math.isinf(r) or r <= 0.05:
                    continue

                angle = pth + self.scan.angle_min + i * self.scan.angle_increment

                hx = px + r * math.cos(angle)
                hy = py + r * math.sin(angle)

                mx = int((hx - ox) / res)
                my = int((hy - oy) / res)

                if 0 <= mx < width and 0 <= my < height:
                    cell = grid[my * width + mx]

                    # Likelihood field style scoring
                    if cell > 50:
                        score += 1.0
                    elif cell == 0:
                        score -= 0.2

            return score

        dx = -SEARCH_X
        while dx <= SEARCH_X:

            dy = -SEARCH_Y
            while dy <= SEARCH_Y:

                dth = -SEARCH_THETA
                while dth <= SEARCH_THETA:

                    px = self.x + dx
                    py = self.y + dy
                    pth = self.theta + dth

                    s = score_pose(px, py, pth)

                    if s > best_score:
                        best_score = s
                        best_x = px
                        best_y = py
                        best_theta = pth

                    dth += STEP_THETA

                dy += STEP_Y

            dx += STEP_X

        self.x = best_x
        self.y = best_y
        self.theta = best_theta

        self.get_logger().info(
            f"Best pose: ({self.x:.2f}, {self.y:.2f}) score={best_score:.1f}"
        )

    # ---------------- PUBLISH ----------------

    def publish_pose(self):

        msg = PoseStamped()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()

        msg.pose.position.x = self.x
        msg.pose.position.y = self.y

        msg.pose.orientation.z = math.sin(self.theta / 2.0)
        msg.pose.orientation.w = math.cos(self.theta / 2.0)

        self.pose_pub.publish(msg)


def main():
    rclpy.init()
    node = ScanMatcherLocalization()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()