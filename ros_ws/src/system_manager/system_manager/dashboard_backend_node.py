#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
from lifecycle_msgs.srv import GetState
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped
from rcl_interfaces.msg import Log
import base64
import collections
import json
import subprocess
import threading
import os
import signal
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from ament_index_python.packages import get_package_share_directory, PackageNotFoundError

def _resolve_web_root():
    """Find the www/ directory — installed share dir first, then source tree."""
    try:
        share = get_package_share_directory('system_manager')
        candidate = os.path.join(share, 'www')
        if os.path.isdir(candidate):
            return candidate
    except PackageNotFoundError:
        pass
    return os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'www'))

WEB_ROOT = _resolve_web_root()

_CONTENT_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.ico': 'image/x-icon',
}


def _make_handler(backend_node):
    class DashboardHandler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'

        def _send_json(self, obj, status=200):
            body = json.dumps(obj).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)

        def _send_file(self, relative_path):
            path = os.path.normpath(os.path.join(WEB_ROOT, relative_path))
            if not path.startswith(WEB_ROOT) or not os.path.isfile(path):
                self.send_error(404)
                return
            ext = os.path.splitext(path)[1].lower()
            with open(path, 'rb') as f:
                body = f.read()
            self.send_response(200)
            self.send_header('Content-Type',
                             _CONTENT_TYPES.get(ext, 'application/octet-stream'))
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            path = self.path.split('?', 1)[0]
            if path == '/':
                self._send_file('alt.html')
            elif path == '/alt.html':
                self._send_file('alt.html')
            elif path == '/index.html':
                self._send_file('index.html')
            elif path == '/api/state':
                self._send_json(backend_node.get_state())
            elif path == '/events':
                self._stream_events()
            elif path.startswith('/www/'):
                self._send_file(path[len('/www/'):])
            else:
                self._send_file(path.lstrip('/'))

        def do_POST(self):
            path = self.path.split('?', 1)[0]
            if path != '/api/command':
                self.send_error(404)
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                payload = json.loads(self.rfile.read(length) or b'{}')
            except (ValueError, json.JSONDecodeError):
                self._send_json({'ok': False, 'error': 'invalid JSON'}, 400)
                return
            try:
                backend_node.handle_command(payload)
                result = {'ok': True}
            except Exception as e:
                result = {'ok': False, 'error': str(e)}
            self._send_json(result)

        def _stream_events(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            try:
                while True:
                    state = backend_node.get_state()
                    data = json.dumps(state)
                    chunk = 'event: state\ndata: {}\n\n'.format(data)
                    self.wfile.write(chunk.encode('utf-8'))
                    self.wfile.flush()
                    time.sleep(0.2)
            except (BrokenPipeError, ConnectionResetError,
                    ConnectionAbortedError, OSError):
                return

        def log_message(self, format, *args):
            pass

    return DashboardHandler


class DashboardBackendNode(Node):
    def __init__(self):
        super().__init__('dashboard_backend_node')

        self.metrics_sub = self.create_subscription(
            String,
            '/slam_confidence',
            self.slam_confidence_callback,
            10
        )

        self.unstuck_state_sub = self.create_subscription(
            Bool,
            '/toggle_unstuck',
            self.unstuck_state_callback,
            10
        )
        self.unstuck_state = False

        self.unstuck_pub = self.create_publisher(Bool, '/toggle_unstuck', 10)

        self.latest_map = None
        self.latest_robot_pose = None
        self.latest_path = None
        self.latest_goal = None
        self.latest_logs = collections.deque(maxlen=200)
        self.tf_cache = {}

        self.create_subscription(
            OccupancyGrid, '/map', self.map_callback, 10)
        self.create_subscription(
            Path, '/planned_path', self.path_callback, 10)
        self.create_subscription(
            PoseStamped, '/goal_pose', self.goal_callback, 10)
        self.create_subscription(
            Log, '/rosout', self.rosout_callback, 10)

        try:
            from tf2_msgs.msg import TFMessage
            self.create_subscription(
                TFMessage, '/tf', self._handle_tf, 100)
            self.create_subscription(
                TFMessage, '/tf_static', self._handle_tf, 100)
        except ImportError:
            self.get_logger().warn('tf2_msgs not available, robot pose disabled')

        self.goal_pub = self.create_publisher(
            PoseStamped, '/goal_pose', 10)

        self.cmd_sub = self.create_subscription(
            String,
            '/web_interface/api_command',
            self.command_callback,
            10
        )

        self.button_status_pub = self.create_publisher(
            String,
            '/web_interface/button_states',
            10
        )

        self.node_states_pub = self.create_publisher(
            String,
            '/web_interface/node_states',
            10
        )

        self.lifecycle_nodes = [
            'slam_toolbox',
            'blind_exploration',
            'collision_avoidance',
            'exploration',
            'follow_red',
            'navigation',
            'roboclaw',
            'urg_node_2',
        ]
        self.node_states = {node: "OFFLINE" for node in self.lifecycle_nodes}
        self.state_clients = {}

        for node_name in self.lifecycle_nodes:
            cli = self.create_client(GetState, f'/{node_name}/get_state')
            self.state_clients[node_name] = cli

        self.lifecycle_timer = self.create_timer(2.0, self.check_lifecycle_states)

        self.active_processes = {}
        self.process_lock = threading.Lock()

        self.sequential_active = False
        self.sequential_stage = 0

        self.latest_slam_metrics = {}

        self.status_timer = self.create_timer(0.5, self.publish_button_states)

        self._start_http_server()
        self.print_welcome_banner()

    def _start_http_server(self):
        port = int(os.environ.get('DASHBOARD_PORT', '8088'))
        try:
            self.httpd = ThreadingHTTPServer(
                ('0.0.0.0', port), _make_handler(self))
            t = threading.Thread(target=self.httpd.serve_forever, daemon=True)
            t.start()
            self.get_logger().info(
                f'Dashboard HTTP server running on http://0.0.0.0:{port}')
        except OSError as e:
            self.get_logger().error(f'Failed to start HTTP server: {e}')

    def get_state(self):
        with self.process_lock:
            button_states = {
                "slam": False,
                "blind_exploration": False,
                "exploration": False,
                "navigation": False,
                "follow_red": False,
                "sequential_start": self.sequential_active,
                "unstuck": self.unstuck_state
            }
            for key in self.active_processes:
                if self.active_processes[key].poll() is None:
                    button_states[key] = True

        for key in self.lifecycle_nodes:
            if key not in button_states:
                button_states[key] = self.node_states.get(
                    key, 'OFFLINE').lower() == 'active'

        return {
            "button_states": button_states,
            "node_states": dict(self.node_states),
            "slam_metrics": self.latest_slam_metrics,
            "map": self.latest_map,
            "robot_pose": self.latest_robot_pose,
            "path": self.latest_path,
            "goal": self.latest_goal,
            "logs": list(self.latest_logs),
        }

    def handle_command(self, payload):
        action = payload.get("action")
        target = payload.get("target")
        if action == "navigate" and "x" in payload and "y" in payload:
            goal = PoseStamped()
            goal.header.stamp = self.get_clock().now().to_msg()
            goal.header.frame_id = 'map'
            goal.pose.position.x = float(payload["x"])
            goal.pose.position.y = float(payload["y"])
            goal.pose.orientation.w = 1.0
            self.goal_pub.publish(goal)
            self.get_logger().info(
                f"Navigation goal sent: ({payload['x']}, {payload['y']})")
            return
        args = payload.get("args", "")
        msg = String()
        msg.data = json.dumps(
            {"action": action, "target": target, "args": args})
        self.command_callback(msg)

    def check_lifecycle_states(self):
        """Fragt asynchron (non-blocking) den Status der Lifecycle Nodes ab."""
        for node_name, cli in self.state_clients.items():
            if cli.service_is_ready():
                req = GetState.Request()
                future = cli.call_async(req)
                future.add_done_callback(lambda f, n=node_name: self.lifecycle_state_cb(f, n))
            else:
                self.node_states[node_name] = "OFFLINE"

        # Publizieren des aktuellen Dictionaries an das Webinterface
        msg = String()
        msg.data = json.dumps(self.node_states)
        self.node_states_pub.publish(msg)

    def lifecycle_state_cb(self, future, node_name):
        """Callback, wenn die Service-Antwort eines Lifecycle-Nodes eintrifft."""
        try:
            response = future.result()
            # Der Status ist ein Label wie "unconfigured", "inactive", "active"
            self.node_states[node_name] = response.current_state.label
        except Exception:
            self.node_states[node_name] = "ERROR"

    def print_welcome_banner(self):
        package_name = 'system_manager'
        html_url = ""
        try:
            pkg_share = get_package_share_directory(package_name)
            path_option_1 = os.path.join(pkg_share, 'www', 'alt.html')
            path_option_2 = os.path.join(pkg_share, 'www', 'index.html')
            if os.path.exists(path_option_1):
                html_url = f"file://{os.path.abspath(path_option_1)}"
            elif os.path.exists(path_option_2):
                html_url = f"file://{os.path.abspath(path_option_2)}"
            else:
                html_url = f"file://{os.getcwd()}/src/{package_name}/www/alt.html"
        except PackageNotFoundError:
            html_url = "Oeffne deine lokale 'alt.html' im Browser"

        port = int(os.environ.get('DASHBOARD_PORT', '8088'))
        self.get_logger().info("\n" + "="*70 + "\n"
                               "DASHBOARD ACTIVE\n"
                               + "="*70 + "\n"
                               "WEBINTERFACE:\n"
                               f"  http://localhost:{port}/alt.html\n"
                               f"  Or: {html_url}\n"
                               + "="*70)

    def publish_button_states(self):
        """Überprüft den Systemstatus aller Prozesse und publiziert das Ergebnis."""
        states = {
            "slam": False,
            "blind_exploration": False,
            "exploration": False,
            "navigation": False,
            "follow_red": False,
            "sequential_start": self.sequential_active,
            "unstuck": self.unstuck_state
        }

        with self.process_lock:
            for key in self.active_processes:
                if self.active_processes[key].poll() is None:
                    states[key] = True

        for key in self.lifecycle_nodes:
            if key not in states:
                states[key] = self.node_states.get(key, 'OFFLINE').lower() == 'active'

        msg = String()
        msg.data = json.dumps(states)
        self.button_status_pub.publish(msg)

    def unstuck_state_callback(self, msg):
        self.unstuck_state = msg.data

    def slam_confidence_callback(self, msg):
        try:
            raw_data = msg.data
            parsed_json = json.loads(raw_data)

            confidence = parsed_json.get("confidence", 0.0)
            frontier_ratio = parsed_json.get("frontier_ratio", 0.0)
            unknown_ratio = parsed_json.get("unknown_ratio", 0.0)
            growth_ratio = parsed_json.get("growth_ratio", 0.0)

            self.latest_slam_metrics = {
                "confidence": confidence,
                "frontier_ratio": frontier_ratio,
                "unknown_ratio": unknown_ratio,
                "growth_ratio": growth_ratio,
            }

            if self.sequential_active and self.sequential_stage == 1:
                if confidence >= 0.30:
                    self.get_logger().info("\n" + "🌟"*20)
                    self.get_logger().info(f"🎯 ZIEL ERREICHT! Confidence liegt bei {confidence*100:.1f}%.")
                    self.get_logger().info("🔄 SCHALTE UM: Von [Blind Exploration] auf [Intelligent Exploration]!")
                    self.get_logger().info("🌟"*20 + "\n")

                    self.sequential_stage = 2
                    self.ensure_node_is_killed("blind_exploration")
                    self.toggle_node("exploration", ["ros2", "launch", "exploration", "exploration.launch.py"])

            self.get_logger().debug(
                f"[Metriken] Conf: {confidence*100:.1f}% | "
                f"Frontier: {frontier_ratio*100:.1f}% | "
                f"Growth: {growth_ratio*100:.1f}%"
            )
        except Exception as e:
            self.get_logger().error(f"Fehler im Metriken-Callback: {e}")

    def map_callback(self, msg):
        info = msg.info
        w, h = info.width, info.height
        if not w or not h or not msg.data:
            return
        cells = bytes(255 if b < 0 else b for b in msg.data)
        self.latest_map = {
            'width': w, 'height': h,
            'resolution': info.resolution,
            'origin_x': info.origin.position.x,
            'origin_y': info.origin.position.y,
            'data_b64': base64.b64encode(cells).decode('ascii'),
        }

    def _handle_tf(self, msg):
        for tf_msg in msg.transforms:
            key = f"{tf_msg.header.frame_id}->{tf_msg.child_frame_id}"
            self.tf_cache[key] = tf_msg.transform
        resolved = self._resolve_base_footprint()
        if resolved:
            self.latest_robot_pose = resolved

    def _resolve_base_footprint(self):
        bf = self.tf_cache.get('map->base_footprint')
        if bf:
            return {
                'x': bf.translation.x, 'y': bf.translation.y,
                'qz': bf.rotation.z, 'qw': bf.rotation.w
            }
        map_odom = self.tf_cache.get('map->odom')
        odom_bf = self.tf_cache.get('odom->base_footprint')
        if map_odom and odom_bf:
            import math
            cy = 2 * math.atan2(map_odom.rotation.z, map_odom.rotation.w)
            return {
                'x': map_odom.translation.x + math.cos(cy) * odom_bf.translation.x - math.sin(cy) * odom_bf.translation.y,
                'y': map_odom.translation.y + math.sin(cy) * odom_bf.translation.x + math.cos(cy) * odom_bf.translation.y,
                'qz': odom_bf.rotation.z, 'qw': odom_bf.rotation.w
            }
        if odom_bf:
            return {
                'x': odom_bf.translation.x, 'y': odom_bf.translation.y,
                'qz': odom_bf.rotation.z, 'qw': odom_bf.rotation.w
            }
        return None

    def path_callback(self, msg):
        if msg.poses:
            self.latest_path = [
                {'x': p.pose.position.x, 'y': p.pose.position.y}
                for p in msg.poses
            ]
        else:
            self.latest_path = None

    def goal_callback(self, msg):
        self.latest_goal = {
            'x': msg.pose.position.x, 'y': msg.pose.position.y,
            'qz': msg.pose.orientation.z, 'qw': msg.pose.orientation.w
        }

    def rosout_callback(self, msg):
        import datetime
        sec = msg.stamp.sec if msg.stamp else int(time.time())
        nsec = msg.stamp.nanosec if msg.stamp else 0
        d = datetime.datetime.fromtimestamp(sec + nsec / 1e9)
        entry = {
            'time': d.strftime('%H:%M:%S.') + f'{nsec // 1000000:03d}',
            'name': msg.name or '',
            'msg': msg.msg or '',
            'level': msg.level or 20,
        }
        self.latest_logs.append(entry)

    def command_callback(self, msg):
        """Callback für Befehle aus der Web-GUI mit Schutz-Matrix & State-Machine."""
        try:
            command_data = json.loads(msg.data)
            action = command_data.get("action")
            target = command_data.get("target")

            self.get_logger().info(f"Befehl erhalten -> Action: {action} | Target: {target}")

            if action == "launch":
                if target not in ["sequential_start", "slam"] and self.sequential_active:
                    self.get_logger().warn("⚠️ Manueller Eingriff! Sequentieller Automatik-Modus wird beendet.")
                    self.sequential_active = False
                    self.sequential_stage = 0

                if target == "sequential_start":
                    if self.sequential_active:
                        self.get_logger().info("🛑 Sequenz MANUELL ABGEBROCHEN. (SLAM laeuft ungestoert weiter)")
                        self.sequential_active = False
                        self.sequential_stage = 0
                        self.ensure_node_is_killed("blind_exploration")
                        self.ensure_node_is_killed("exploration")
                    else:
                        self.get_logger().info("⚡ SEQUENTIELLER MODUS GESTARTET! (Erwartet, dass SLAM bereits laeuft)")
                        self.sequential_active = True
                        self.sequential_stage = 1

                        self.ensure_node_is_killed("blind_exploration")
                        self.ensure_node_is_killed("exploration")
                        self.ensure_node_is_killed("navigation")
                        self.ensure_node_is_killed("follow_red")

                        self.get_logger().info("🚀 PHASE 1: Starte NUR [Blind Exploration]...")
                        self.toggle_node("blind_exploration", ["ros2", "launch", "exploration", "blind_exploration.launch.py"])

                elif target == "slam":
                    self.toggle_node("slam", ["ros2", "launch", "slam", "slam_mapping.launch.py"])

                elif target == "blind_exploration":
                    self.ensure_node_is_killed("exploration")
                    self.ensure_node_is_killed("navigation")
                    self.ensure_node_is_killed("follow_red")
                    self.toggle_node("blind_exploration", ["ros2", "launch", "exploration", "blind_exploration.launch.py"])

                elif target == "exploration":
                    self.ensure_node_is_killed("blind_exploration")
                    self.ensure_node_is_killed("follow_red")
                    self.toggle_node("exploration", ["ros2", "launch", "exploration", "exploration.launch.py"])

                elif target == "navigation":
                    self.ensure_node_is_killed("blind_exploration")
                    self.ensure_node_is_killed("exploration")
                    self.ensure_node_is_killed("follow_red")
                    self.toggle_node("navigation", ["ros2", "launch", "navigation", "navigation.launch.py"])

                elif target == "follow_red":
                    self.ensure_node_is_killed("blind_exploration")
                    self.ensure_node_is_killed("exploration")
                    self.ensure_node_is_killed("navigation")
                    self.toggle_node("follow_red", ["ros2", "launch", "follow_red", "follow_red_with_avoidance.launch.py"])

                elif target == "urg_node_2":
                    self.toggle_node("urg_node_2", ["ros2", "launch", "urg_node_2", "urg_node_2.launch.py"])

                elif target == "roboclaw":
                    self.toggle_node("roboclaw", ["ros2", "launch", "roboclaw", "roboclaw.launch.py"])

                else:
                    self.get_logger().warn(f"Unbekanntes Launch-Ziel: {target}")

            elif action == "toggle":
                if target == "unstuck":
                    new_state = not self.unstuck_state
                    self.get_logger().info(f"🔄 Unstuck toggled to: {new_state}")
                    msg = Bool()
                    msg.data = new_state
                    self.unstuck_pub.publish(msg)
                else:
                    self.get_logger().warn(f"Unbekanntes Toggle-Ziel: {target}")

        except json.JSONDecodeError as e:
            self.get_logger().error(f"Fehler beim Parsen des Befehls-JSON: {e}")

    def kill_process_group(self, proc):
        """Killt eine gesamte Prozessgruppe sauber."""
        try:
            pgid = os.getpgid(proc.pid)
            self.get_logger().info(f"Sende SIGTERM an Prozessgruppe PGID: {pgid}")
            os.killpg(pgid, signal.SIGTERM)

            for _ in range(10):
                if proc.poll() is not None:
                    return True
                time.sleep(0.2)

            self.get_logger().warn(f"Prozessgruppe {pgid} reagiert nicht. Erzwinge SIGKILL...")
            os.killpg(pgid, signal.SIGKILL)
            proc.wait()
            return True
        except ProcessLookupError:
            return True
        except Exception as e:
            self.get_logger().error(f"Fehler beim Beenden der Prozessgruppe: {e}")
            return False

    def ensure_node_is_killed(self, target_key):
        """Prüft, ob ein Prozess läuft, und killt ihn."""
        with self.process_lock:
            if target_key in self.active_processes:
                proc = self.active_processes[target_key]
                if proc.poll() is None:
                    self.get_logger().warn(f"⚠️ [SCHUTZ-TRIGGER] {target_key.upper()} wird beendet...")
                    self.kill_process_group(proc)
                self.active_processes.pop(target_key, None)

    def toggle_node(self, target_key, launch_cmd):
        """Startet oder beendet einen Node."""
        with self.process_lock:
            is_running = False
            if target_key in self.active_processes:
                proc = self.active_processes[target_key]
                if proc.poll() is None:
                    is_running = True

            if is_running:
                self.get_logger().warn(f"🛑 [{target_key.upper()}] laeuft bereits. Beende gesamte Gruppe...")
                proc = self.active_processes[target_key]
                self.kill_process_group(proc)
                self.active_processes.pop(target_key, None)
            else:
                self.get_logger().info(f"🚀 [{target_key.upper()}] wird gestartet...")
                def run_subprocess():
                    try:
                        proc = subprocess.Popen(
                            launch_cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            preexec_fn=os.setsid
                        )
                        with self.process_lock:
                            self.active_processes[target_key] = proc
                        proc.communicate()
                    except Exception as e:
                        self.get_logger().error(f"❌ Fehler bei Ausfuehrung von [{target_key.upper()}]: {e}")
                    finally:
                        with self.process_lock:
                            if target_key in self.active_processes and self.active_processes[target_key] == proc:
                                self.active_processes.pop(target_key, None)
                                self.get_logger().info(f"ℹ️ [{target_key.upper()}] beendet.")
                threading.Thread(target=run_subprocess, daemon=True).start()

def main(args=None):
    rclpy.init(args=args)
    node = DashboardBackendNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Backend wird beendet...")
    finally:
        if hasattr(node, 'httpd'):
            node.httpd.shutdown()
        for name, process in list(node.active_processes.items()):
            if process.poll() is None:
                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                except Exception:
                    pass
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()