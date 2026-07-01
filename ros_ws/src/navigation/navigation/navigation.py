import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped

class Navigation(Node):
    def __init__(self):
        super().__init__("navigation")

        self.x = 0
        self.y = 0

        self.env_map = []

        self.goal_x = 0
        self.goal_y = 0

        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            "/map",
            self.map_callback,
            1
        )

        self.pose_subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            "/pose",
            self.pose_callback,
            1
        )

        self.goal_pose_subscription = self.create_subscription(
            PoseStamped,
            "/goal_pose",
            self.goal_pose_callback,
            1
        )

    def map_callback(self, msg):
        width = msg.info.width
        height = msg.info.height

        self.env_map = msg.data

        # TODO: figure out path from our position to target position using map

    def pose_callback(self, msg):
        position = msg.pose.pose.position

        self.x = position.x
        self.y = position.y

    def goal_pose_callback(self, msg):
        self.goal_x = msg.pose.position.x
        self.goal_y = msg.pose.posiiton.y

def main():
    rclpy.init()
    navigation = Navigation()
    try:
        rclpy.spin(navigation)
    except KeyboardInterrupt:
        pass
    finally:
        navigation.destroy_node()
        rclpy.shutdown()