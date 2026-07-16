#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from lifecycle_msgs.srv import GetState  # NEU: Lifecycle Management Service
import json
import subprocess
import threading
import os
import signal
import time
from ament_index_python.packages import get_package_share_directory, PackageNotFoundError

class DashboardBackendNode(Node):
    def __init__(self):
        super().__init__('dashboard_backend_node')

        # 1. SUBSCRIBER FÜR DASHBOARD-METRIKEN
        self.metrics_sub = self.create_subscription(
            String,
            '/slam_confidence',
            self.slam_confidence_callback,
            10
        )

        # 2. SUBSCRIBER FÜR STEUERUNGSBEFEHLE AUS DEM WEBINTERFACE
        self.cmd_sub = self.create_subscription(
            String,
            '/web_interface/api_command',
            self.command_callback,
            10
        )

        # 3. PUBLISHER FÜR DEN AKTUELLEN LAUNCH-STATUS DER BUTTONS
        self.button_status_pub = self.create_publisher(
            String,
            '/web_interface/button_states',
            10
        )

        # 4. PUBLISHER FÜR LIFECYCLE NODE STATES
        self.node_states_pub = self.create_publisher(
            String,
            '/web_interface/node_states',
            10
        )

        # --- LIFECYCLE MANAGEMENT KONFIGURATION ---
        # HIER triffst du die Auswahl, welche Knoten überwacht werden sollen.
        # Passe die Namen exakt so an, wie sie in deinem System heißen.
        self.lifecycle_nodes = [
            'slam_toolbox',
            'blind_exploration',
            'collision_avoidance',
            'exploration',
            'follow_red',
            'navigation',
        ]
        self.node_states = {node: "OFFLINE" for node in self.lifecycle_nodes}
        self.state_clients = {}

        # Erstelle für jeden Knoten einen eigenen asynchronen Service-Client
        for node_name in self.lifecycle_nodes:
            cli = self.create_client(GetState, f'/{node_name}/get_state')
            self.state_clients[node_name] = cli

        # Timer: Prüft alle 2.0 Sekunden asynchron den Status der Lifecycle Nodes
        self.lifecycle_timer = self.create_timer(2.0, self.check_lifecycle_states)

        # Dictionary für aktive Prozesse und Lock
        self.active_processes = {}
        self.process_lock = threading.Lock()

        # --- STATE MACHINE FÜR DEN SEQUENTIELLEN START ---
        self.sequential_active = False
        self.sequential_stage = 0  # 0=Aus, 1=Blind Exploration, 2=Intelligent Exploration

        # Timer: Prüft alle 0.5 Sekunden den Status der Prozesse
        self.status_timer = self.create_timer(0.5, self.publish_button_states)

        # Willkommens-Banner ausgeben
        self.print_welcome_banner()

    def check_lifecycle_states(self):
        """Fragt asynchron (non-blocking) den Status der Lifecycle Nodes ab."""
        for node_name, cli in self.state_clients.items():
            if cli.service_is_ready():
                req = GetState.Request()
                future = cli.call_async(req)
                # Lambda fängt den aktuellen node_name und das future auf
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
        """Sucht die index.html im Workspace und gibt eine klickbare URL aus."""
        package_name = 'my_robot_web'
        html_url = ""
        try:
            pkg_share = get_package_share_directory(package_name)
            path_option_1 = os.path.join(pkg_share, 'www', 'index.html')
            path_option_2 = os.path.join(pkg_share, 'index.html')

            if os.path.exists(path_option_1):
                html_url = f"file://{os.path.abspath(path_option_1)}"
            elif os.path.exists(path_option_2):
                html_url = f"file://{os.path.abspath(path_option_2)}"
            else:
                html_url = f"file://{os.getcwd()}/src/{package_name}/www/index.html"
        except PackageNotFoundError:
            html_url = "Oeffne deine lokale 'index.html' im Browser"

        self.get_logger().info("\n" + "="*70 + "\n"
                               "🤖 SCHRITT 11: LIFECYCLE NODE MONITORING AKTIV!\n"
                               + "="*70 + "\n"
                               "🌐 WEBINTERFACE STARTEN:\n"
                               "  Halte [Strg] gedrueckt und klicke auf diesen Link:\n\n"
                               f"  👉  \033[4;36m{html_url}\033[0m  👈\n\n"
                               + "="*70 + "\n"
                               "Lifecycle Feature:\n"
                               "  Die Status-Zustaende der Hauptknoten (Active, Unconfigured etc.)\n"
                               "  werden nun in Echtzeit im Dashboard angezeigt!\n"
                               + "="*70)

    def publish_button_states(self):
        """Überprüft den Systemstatus aller Prozesse und publiziert das Ergebnis."""
        states = {
            "slam": False,
            "blind_exploration": False,
            "exploration": False,
            "navigation": False,
            "follow_red": False,
            "sequential_start": self.sequential_active
        }

        with self.process_lock:
            # Prüfe normale Prozesse
            for key in ["slam", "blind_exploration", "exploration", "navigation", "follow_red"]:
                if key in self.active_processes:
                    if self.active_processes[key].poll() is None:
                        states[key] = True

        msg = String()
        msg.data = json.dumps(states)
        self.button_status_pub.publish(msg)

    def slam_confidence_callback(self, msg):
        """Callback für die Verarbeitung der Dashboard-Metriken (Autonomer Umschalter)."""
        try:
            raw_data = msg.data
            parsed_json = json.loads(raw_data)

            confidence = parsed_json.get("confidence", 0.0)
            frontier_ratio = parsed_json.get("frontier_ratio", 0.0)
            unknown_ratio = parsed_json.get("unknown_ratio", 0.0)
            growth_ratio = parsed_json.get("growth_ratio", 0.0)

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

                else:
                    self.get_logger().warn(f"Unbekanntes Launch-Ziel: {target}")

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