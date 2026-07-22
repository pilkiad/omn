#!/usr/bin/env python3

import math
import numpy as np

from scipy.ndimage import distance_transform_edt

import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class ScanMatcherLocalization(Node):

    def __init__(self):

        super().__init__(
            "scan_match_localization"
        )

        self.has_map = False

        self.distance_field = None

        self.map_width = 0
        self.map_height = 0

        self.resolution = 0.0

        self.origin_x = 0
        self.origin_y = 0

        self.scan = None
        self.scan_received = False

        self.x = 1.0
        self.y = -1.0
        self.theta = 0.0

        self.cov_x = 0.5
        self.cov_y = 0.5
        self.cov_theta = math.radians(20)

        # Latest odometry pose
        self.odom_x = 0.0
        self.odom_y = 0.0
        self.odom_theta = 0.0

        # Previous odometry pose
        self.last_odom_x = None
        self.last_odom_y = None
        self.last_odom_theta = None

        self.odom_received = False

        self.tf_broadcaster = TransformBroadcaster(self)

        self.create_subscription(
            OccupancyGrid,
            "/map",
            self.map_callback,
            1
        )

        self.create_subscription(
            LaserScan,
            "/scan",
            self.scan_callback,
            1
        )

        self.create_subscription(
            Odometry,
            "/odom",
            self.odom_callback,
            10
        )

        self.pose_pub = self.create_publisher(
            PoseWithCovarianceStamped,
            "/pos",
            10
        )


        self.timer = self.create_timer(
            0.5,
            self.update
        )


        self.get_logger().info(
            "Scan matcher started"
        )

    def map_callback(self,msg):

        if self.has_map:
            return


        self.map_width = msg.info.width
        self.map_height = msg.info.height

        self.resolution = msg.info.resolution

        self.origin_x = (
            msg.info.origin.position.x
        )

        self.origin_y = (
            msg.info.origin.position.y
        )


        grid = np.array(
            msg.data,
            dtype=np.int8
        )


        grid = grid.reshape(
            self.map_height,
            self.map_width
        )


        # free cells

        free = grid < 50

        # unknown = obstacle

        free[grid < 0] = False


        distance = distance_transform_edt(
            free
        )


        self.distance_field = (
            distance *
            self.resolution
        )


        self.has_map = True


        self.get_logger().info(
            "Likelihood field created"
        )

    def odom_callback(self, msg):

        self.odom_x = msg.pose.pose.position.x
        self.odom_y = msg.pose.pose.position.y

        q = msg.pose.pose.orientation

        self.odom_theta = math.atan2(
            2.0 * (q.w * q.z + q.x * q.y),
            1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        )

        self.odom_received = True

    def scan_callback(self,msg):

        self.scan = msg

        self.scan_received = True

    def publish_map_to_odom(self):

        if not self.odom_received:
            return


        tf = TransformStamped()

        tf.header.stamp = (
            self.get_clock()
            .now()
            .to_msg()
        )

        tf.header.frame_id = "map"
        tf.child_frame_id = "odom"


        # localization correction
        dx = self.x - self.odom_x
        dy = self.y - self.odom_y

        c = math.cos(self.odom_theta)
        s = math.sin(self.odom_theta)


        tf.transform.translation.x = (
            c*dx + s*dy
        )

        tf.transform.translation.y = (
            -s*dx + c*dy
        )

        tf.transform.translation.z = 0.0


        yaw = (
            self.theta -
            self.odom_theta
        )


        tf.transform.rotation.z = math.sin(
            yaw / 2.0
        )

        tf.transform.rotation.w = math.cos(
            yaw / 2.0
        )


        self.tf_broadcaster.sendTransform(tf)

    def update(self):

        if not self.has_map:
            return

        if not self.scan_received:
            return

        if not self.odom_received:
            return


        self.localize()

        self.publish_pose()
        self.publish_map_to_odom()

    def localize(self):

        # First call
        if self.last_odom_x is None:

            self.last_odom_x = self.odom_x
            self.last_odom_y = self.odom_y
            self.last_odom_theta = self.odom_theta

        else:

            dx = self.odom_x - self.last_odom_x
            dy = self.odom_y - self.last_odom_y

            dtheta = self.normalize_angle(
                self.odom_theta - self.last_odom_theta
            )

            # Predict map pose
            self.x += dx
            self.y += dy
            self.theta = self.normalize_angle(
                self.theta + dtheta
            )


            # Odometry increases uncertainty

            motion = math.sqrt(
                dx*dx + dy*dy
            )

            self.cov_x += motion * 0.05
            self.cov_y += motion * 0.05
            self.cov_theta += abs(dtheta)*0.1

            self.last_odom_x = self.odom_x
            self.last_odom_y = self.odom_y
            self.last_odom_theta = self.odom_theta


        beams = self.prepare_scan()

        if self.cov_x > 5.0:

            pose = self.random_global_search(
                beams
            )

            if pose:
                self.x = pose[0]
                self.y = pose[1]
                self.theta = pose[2]

                self.cov_x = 1.0
                self.cov_y = 1.0
                self.cov_theta = math.radians(30)


        if len(beams) < 20:
            return


        # coarse

        pose = self.search(
            self.x,
            self.y,
            self.theta,

            0.5,
            math.radians(8),

            0.03,
            math.radians(2),

            beams
        )


        # medium

        pose = self.search(
            *pose,

            0.08,
            math.radians(4),

            0.02,
            math.radians(1),

            beams
        )


        # fine

        pose = self.search(
            *pose,

            0.03,
            math.radians(1),

            0.01,
            math.radians(0.25),

            beams
        )


        self.x = pose[0]
        self.y = pose[1]
        self.theta = self.normalize_angle(
            pose[2]
        )

        # Laser correction reduces uncertainty
        self.cov_x *= 0.5
        self.cov_y *= 0.5
        self.cov_theta *= 0.5

    def prepare_scan(self):

        points = []


        step = 5


        for i in range(
            0,
            len(self.scan.ranges),
            step
        ):

            r = self.scan.ranges[i]


            if math.isinf(r):
                continue

            if r < self.scan.range_min:
                continue

            if r > self.scan.range_max:
                continue


            angle = (
                self.scan.angle_min
                +
                i *
                self.scan.angle_increment
            )


            points.append(
                [
                    r*np.cos(angle),
                    r*np.sin(angle)
                ]
            )


        return np.array(points)

    def search(
        self,
        cx,
        cy,
        ct,

        xy_window,
        theta_window,

        xy_step,
        theta_step,

        beams
    ):


        best_score = -999999

        best = (
            cx,
            cy,
            ct
        )


        x_values = np.arange(
            -xy_window,
            xy_window+xy_step,
            xy_step
        )


        y_values = np.arange(
            -xy_window,
            xy_window+xy_step,
            xy_step
        )


        t_values = np.arange(
            -theta_window,
            theta_window+theta_step,
            theta_step
        )


        for dx in x_values:

            for dy in y_values:

                for dt in t_values:


                    score = self.score_pose(
                        cx+dx,
                        cy+dy,
                        ct+dt,
                        beams
                    )


                    if score > best_score:

                        best_score = score

                        best = (
                            cx+dx,
                            cy+dy,
                            ct+dt
                        )


        self.get_logger().info(
            f"score {best_score:.1f}"
        )


        return best

    def score_pose(
        self,
        x,
        y,
        theta,
        beams
    ):


        c = np.cos(theta)
        s = np.sin(theta)


        rx = beams[:,0]
        ry = beams[:,1]


        wx = (
            x
            +
            c*rx
            -
            s*ry
        )

        wy = (
            y
            +
            s*rx
            +
            c*ry
        )


        mx = (
            (wx-self.origin_x)
            /
            self.resolution
        ).astype(int)


        my = (
            (wy-self.origin_y)
            /
            self.resolution
        ).astype(int)



        valid = (

            (mx >=0)
            &
            (my >=0)

            &
            (mx < self.map_width)

            &
            (my < self.map_height)

        )


        if np.sum(valid)==0:
            return -9999


        distances = self.distance_field[
            my[valid],
            mx[valid]
        ]


        sigma = 0.2


        score = np.mean(
            np.exp(
                -(distances**2)
                /
                (2*sigma*sigma)
            )
        )

        score -= (
            0.2 *
            math.hypot(
                x-self.x,
                y-self.y
            )
        )

        score -= (
            0.05 *
            abs(
                self.normalize_angle(
                    theta-self.theta
                )
            )
        )

        score -= 0.5 * abs(
            self.normalize_angle(theta - self.theta)
        )
        return score

    def normalize_angle(self,a):

        return math.atan2(
            math.sin(a),
            math.cos(a)
        )

#    def publish_pose(self):
#
#        msg = PoseStamped()
#
#        msg.header.frame_id="map"
#
#        msg.header.stamp=(
#            self.get_clock()
#            .now()
#            .to_msg()
#        )
#
#
#        msg.pose.position.x=self.x
#        msg.pose.position.y=self.y
#
#
#        msg.pose.orientation.z=math.sin(
#            self.theta/2
#        )
#
#        msg.pose.orientation.w=math.cos(
#            self.theta/2
#        )
#
#
#        self.pose_pub.publish(msg)
        
    def publish_pose(self):

        msg = PoseWithCovarianceStamped()

        msg.header.frame_id = "map"
        msg.header.stamp = (
            self.get_clock()
            .now()
            .to_msg()
        )

        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y

        msg.pose.pose.orientation.z = math.sin(
            self.theta / 2
        )

        msg.pose.pose.orientation.w = math.cos(
            self.theta / 2
        )


        covariance = [0.0] * 36

        covariance[0] = self.cov_x
        covariance[7] = self.cov_y
        covariance[35] = self.cov_theta


        msg.pose.covariance = covariance


        self.pose_pub.publish(msg)


    def random_global_search(self, beams):

        best_score = -99999
        best_pose = None


        for _ in range(500):

            x = np.random.uniform(
                self.origin_x,
                self.origin_x +
                self.map_width*self.resolution
            )

            y = np.random.uniform(
                self.origin_y,
                self.origin_y +
                self.map_height*self.resolution
            )

            theta = np.random.uniform(
                -math.pi,
                math.pi
            )


            score = self.score_pose(
                x,
                y,
                theta,
                beams
            )


            if score > best_score:

                best_score = score

                best_pose = (
                    x,
                    y,
                    theta
                )


        return best_pose



def main(args=None):

    rclpy.init(args=args)

    node=ScanMatcherLocalization()

    rclpy.spin(node)


    node.destroy_node()

    rclpy.shutdown()



if __name__=="__main__":
    main()