#!/usr/bin/env python3

import time
import json
import rclpy
from rclpy.lifecycle import Node, State, TransitionCallbackReturn
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from enum import Enum

# Nachrichten und Services
from std_msgs.msg import String
from slam_toolbox.srv import SaveMap

class InternalState(Enum):
    UNCONFIGURED = 0
    CONFIGURED = 1
    WAIT_FOR_COMPLETION = 2
    SAVE_MAP = 3
    STOP_MAPPING = 4
    FINISHED = 5

class SystemManagerNode(Node):
    def __init__(self):
        super().__init__('system_manager')
        self.internal_state = InternalState.UNCONFIGURED

        # Platzhalter für ROS-Entitäten
        self.confidence_sub = None
        self.save_map_client = None

        # Variable für die zeitliche Stabilitätsprüfung (Debouncing)
        self.threshold_start_time = None

        self.get_logger().info("System-Manager initialisiert. Lifecycle-Status: UNCONFIGURED")

    # ==========================================
    # ROS 2 Lifecycle Callbacks
    # ==========================================
    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Konfiguriere Knoten...")

        # Callback-Gruppe für asynchrone Service-Aufrufe
        self.cb_group = MutuallyExclusiveCallbackGroup()

        # Abonnent für den SLAM Analyzer: QoS exakt auf 10 (Symmetrie zum Publisher)
        self.confidence_sub = self.create_subscription(
            String,
            '/slam_confidence',
            self.confidence_callback,
            10,
            callback_group=self.cb_group
        )

        # Service-Client für SLAM Toolbox
        self.save_map_client = self.create_client(
            SaveMap,
            '/slam_toolbox/save_map',
            callback_group=self.cb_group
        )

        self.internal_state = InternalState.CONFIGURED
        self.get_logger().info("Konfiguration abgeschlossen. Lifecycle-Status: INACTIVE")
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Aktiviere Knoten...")

        # Warten, bis der Service verfügbar ist
        if not self.save_map_client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error("Service /slam_toolbox/save_map nicht verfügbar! Bitte SLAM-Toolbox prüfen.")
            return TransitionCallbackReturn.FAILURE

        self.internal_state = InternalState.WAIT_FOR_COMPLETION
        # Reset der Stabilitätsprüfung bei jedem Neustart
        self.threshold_start_time = None

        self.get_logger().info("Knoten aktiviert. Interne FSM: WAIT_FOR_COMPLETION. Warte auf Daten...")
        return TransitionCallbackReturn.SUCCESS

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Deaktiviere Knoten...")
        self.internal_state = InternalState.CONFIGURED
        return TransitionCallbackReturn.SUCCESS

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Räume Knoten auf (Cleanup)...")
        self.destroy_subscription(self.confidence_sub)
        self.destroy_client(self.save_map_client)
        self.internal_state = InternalState.UNCONFIGURED
        return TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Fahre Knoten herunter...")
        return TransitionCallbackReturn.SUCCESS

    # ==========================================
    # Interne FSM & Logik (JSON Parsing + Stabilitätsprüfung)
    # ==========================================
    def confidence_callback(self, msg: String):
        # Ignoriere Daten, wenn wir nicht auf den Abschluss warten
        if self.internal_state != InternalState.WAIT_FOR_COMPLETION:
            return

        try:
            # 1. JSON-String parsen
            data_dict = json.loads(msg.data)
            current_confidence = float(data_dict.get("confidence", 0.0))

            # 2. Schwellenwert bestimmen
            threshold = 97.0 if current_confidence > 1.0 else 0.97

            # HEARTBEAT-LOG: Zeigt dir an, dass Daten aktiv verarbeitet werden
            self.get_logger().info(f"[Daten-Stream] Lese Confidence: {current_confidence:.4f} (Ziel: {threshold})")

            # 3. Zeitliche Stabilitätsprüfung (Debouncing)
            if current_confidence >= threshold:
                current_time = self.get_clock().now()

                # Wenn dies das erste Mal ist, dass der Wert erreicht wird, starte die Uhr
                if self.threshold_start_time is None:
                    self.threshold_start_time = current_time
                    self.get_logger().info(f"Schwellenwert ({threshold}) erreicht. Starte 5-Sekunden-Timer...")
                else:
                    # Berechne die verstrichene Zeit in Sekunden
                    elapsed_time = current_time - self.threshold_start_time
                    elapsed_seconds = elapsed_time.nanoseconds / 1e9

                    self.get_logger().info(f"Countdown: Stabil seit {elapsed_seconds:.1f}/5.0 Sekunden...")

                    # Wenn die 5 Sekunden voll sind, löse die Aktion aus
                    if elapsed_seconds >= 5.0:
                        self.get_logger().info(f"Stabilität von 5 Sekunden erfolgreich erreicht! Wechsle zu SAVE_MAP.")
                        self.internal_state = InternalState.SAVE_MAP
                        self.threshold_start_time = None # Timer sicherheitshalber zurücksetzen
                        self.trigger_save_map()
            else:
                # Fällt der Wert unter den Schwellenwert, breche den Vorgang gnadenlos ab
                if self.threshold_start_time is not None:
                    self.get_logger().warn(f"Confidence auf {current_confidence:.4f} abgefallen. Timer wurde abgebrochen!")
                    self.threshold_start_time = None # Reset

        except json.JSONDecodeError as e:
            self.get_logger().error(f"Fehler beim Parsen der JSON-Nachricht: {e}")
        except ValueError as e:
            self.get_logger().error(f"Fehler bei der Typenumwandlung: {e}")

    def trigger_save_map(self):
        req = SaveMap.Request()
        req.name = String()
        # Generiere einen eindeutigen Kartennamen basierend auf dem Zeitstempel
        map_name = f"auto_map_{int(time.time())}"
        req.name.data = map_name

        self.get_logger().info(f"Sende Service-Call zum Speichern der Karte: '{map_name}'")

        # Asynchroner Aufruf blockiert das System nicht
        future = self.save_map_client.call_async(req)
        future.add_done_callback(self.save_map_response_callback)

    def save_map_response_callback(self, future):
        try:
            response = future.result()
            if response.result == SaveMap.Response.RESULT_SUCCESS:
                self.get_logger().info("Karte erfolgreich gespeichert.")
                self.transition_to_stop_mapping()
            else:
                self.get_logger().error(f"Fehler beim Speichern der Karte. Fehlercode: {response.result}")
                # Fallback: Zurück in den Wartezustand
                self.internal_state = InternalState.WAIT_FOR_COMPLETION
        except Exception as e:
            self.get_logger().error(f"Service-Aufruf fehlgeschlagen: {e}")
            self.internal_state = InternalState.WAIT_FOR_COMPLETION

    def transition_to_stop_mapping(self):
        self.internal_state = InternalState.STOP_MAPPING
        self.get_logger().info("Interne FSM: STOP_MAPPING")

        self.get_logger().info("Mapping-Prozess wird beendet (simuliert)...")
        time.sleep(1.0) # Simuliere die Dauer des Stoppvorgangs

        self.transition_to_finished()

    def transition_to_finished(self):
        self.internal_state = InternalState.FINISHED
        self.get_logger().info("Interne FSM: FINISHED. Das System ist bereit für die Navigation.")


def main(args=None):
    rclpy.init(args=args)
    node = SystemManagerNode()

    try:
        executor = rclpy.executors.MultiThreadedExecutor()
        executor.add_node(node)
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()