from nav_msgs.msg import OccupancyGrid
from nav_msgs.srv import GetMap
import rclpy
from rclpy.node import Node


class MapServiceToTopic(Node):
    def __init__(self):
        super().__init__('map_service_to_topic')

        self.declare_parameter('service_name', '/map_server/map')
        self.declare_parameter('topic_name', '/map')
        self.declare_parameter('publish_period', 1.0)

        service_name = self.string_parameter('service_name')
        topic_name = self.string_parameter('topic_name')
        publish_period = self.double_parameter('publish_period')

        self.map = None
        self.pending_request = None

        self.client = self.create_client(GetMap, service_name)
        self.publisher = self.create_publisher(OccupancyGrid, topic_name, 10)
        self.timer = self.create_timer(publish_period, self.timer_callback)

    def string_parameter(self, name):
        return self.get_parameter(name).get_parameter_value().string_value

    def double_parameter(self, name):
        return self.get_parameter(name).get_parameter_value().double_value

    def timer_callback(self):
        if self.map is not None:
            self.publisher.publish(self.map)
            return

        if self.pending_request is None:
            if self.client.service_is_ready():
                self.pending_request = self.client.call_async(GetMap.Request())
            return

        if not self.pending_request.done():
            return

        try:
            response = self.pending_request.result()
        except Exception as exc:
            self.get_logger().warn(f'Failed to request map: {exc}')
            self.pending_request = None
            return

        self.map = response.map
        self.publisher.publish(self.map)
        self.get_logger().info(
            f'Republishing {self.map.info.width}x{self.map.info.height} map'
        )


def main():
    rclpy.init()
    node = MapServiceToTopic()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.destroy_node()
        except (Exception, KeyboardInterrupt):
            pass
        if rclpy.ok():
            rclpy.shutdown()
