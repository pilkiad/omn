"""Lifecycle Manager.

THIS is the module that connects to your teammates' code -- and it does
so purely through the standard ROS2 lifecycle interface, never by
importing their packages:

  /<node_name>/change_state   (service, lifecycle_msgs/srv/ChangeState)
  /<node_name>/get_state      (service, lifecycle_msgs/srv/GetState)

Every rclpy/rclcpp LifecycleNode exposes these two services automatically
the moment a teammate writes `class MappingNode(LifecycleNode):`. You
don't need their code to be finished, or even correct -- you only need
to agree on the node's NAME (e.g. "mapping"). That name is the entire
contract between your package and theirs.

IMPORTANT IMPLEMENTATION NOTE:
get_state()/change_state() are called from inside HealthMonitor's timer
callback, which itself runs inside the orchestrator node's main
rclpy.spin() executor. Calling rclpy.spin_until_future_complete() on
that SAME executor from inside one of its own callbacks raises
"RuntimeError: Executor is already spinning" -- rclpy's single-threaded
executor is not reentrant. To avoid that, this module creates its own
private node + executor, spun in a background thread, used only for
these blocking service calls. The main orchestrator node's executor is
never touched here.
"""

import threading

import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.node import Node
from lifecycle_msgs.srv import ChangeState, GetState
from lifecycle_msgs.msg import Transition, State


TRANSITION_LABEL = {
    Transition.TRANSITION_CONFIGURE: 'configure',
    Transition.TRANSITION_CLEANUP: 'cleanup',
    Transition.TRANSITION_ACTIVATE: 'activate',
    Transition.TRANSITION_DEACTIVATE: 'deactivate',
    Transition.TRANSITION_UNCONFIGURED_SHUTDOWN: 'shutdown',
    Transition.TRANSITION_INACTIVE_SHUTDOWN: 'shutdown',
    Transition.TRANSITION_ACTIVE_SHUTDOWN: 'shutdown',
}

STATE_LABEL = {
    State.PRIMARY_STATE_UNCONFIGURED: 'unconfigured',
    State.PRIMARY_STATE_INACTIVE: 'inactive',
    State.PRIMARY_STATE_ACTIVE: 'active',
    State.PRIMARY_STATE_FINALIZED: 'finalized',
}


class LifecycleManager:

    def __init__(self, node: Node, managed_node_names, service_timeout_sec: float = 3.0):
        self._node = node
        self._logger = node.get_logger()
        self._timeout = service_timeout_sec
        self._managed_node_names = list(managed_node_names)

        # Private node + executor, dedicated to blocking service calls.
        # Kept separate from the orchestrator node's own executor so we
        # never spin an executor from inside one of its own callbacks.
        self._client_node = rclpy.create_node(f'{node.get_name()}_lifecycle_client')
        self._client_executor = SingleThreadedExecutor()
        self._client_executor.add_node(self._client_node)
        self._client_thread = threading.Thread(target=self._client_executor.spin, daemon=True)
        self._client_thread.start()

        self._change_state_clients = {}
        self._get_state_clients = {}
        for name in self._managed_node_names:
            self._change_state_clients[name] = self._client_node.create_client(
                ChangeState, f'/{name}/change_state')
            self._get_state_clients[name] = self._client_node.create_client(
                GetState, f'/{name}/get_state')

    def _call(self, client, request, timeout_sec=None):
        """Block the calling thread until `client`'s async call resolves,
        without touching the orchestrator node's own executor.
        """
        timeout_sec = self._timeout if timeout_sec is None else timeout_sec
        if not client.wait_for_service(timeout_sec=timeout_sec):
            return None

        future = client.call_async(request)
        done = threading.Event()
        future.add_done_callback(lambda _f: done.set())

        if not done.wait(timeout=timeout_sec):
            return None
        return future.result()

    def wait_for_node(self, name: str, timeout_sec: float = 5.0) -> bool:
        return self._change_state_clients[name].wait_for_service(timeout_sec=timeout_sec)

    def get_state(self, name: str):
        client = self._get_state_clients[name]
        if not client.service_is_ready():
            return None
        result = self._call(client, GetState.Request())
        if result is None:
            return None
        return STATE_LABEL.get(result.current_state.id, 'unknown')

    def change_state(self, name: str, transition_id: int) -> bool:
        client = self._change_state_clients[name]
        label = TRANSITION_LABEL.get(transition_id, str(transition_id))

        request = ChangeState.Request()
        request.transition.id = transition_id
        result = self._call(client, request)

        if result is None:
            self._logger.error(f'{name}: {label} timed out or service unavailable')
            return False

        if result.success:
            self._logger.info(f'{name}: {label} OK')
        else:
            self._logger.error(f'{name}: {label} REJECTED')
        return result.success

    def configure(self, name: str) -> bool:
        return self.change_state(name, Transition.TRANSITION_CONFIGURE)

    def activate(self, name: str) -> bool:
        return self.change_state(name, Transition.TRANSITION_ACTIVATE)

    def deactivate(self, name: str) -> bool:
        return self.change_state(name, Transition.TRANSITION_DEACTIVATE)

    def cleanup(self, name: str) -> bool:
        return self.change_state(name, Transition.TRANSITION_CLEANUP)

    def shutdown_node(self, name: str) -> bool:
        return self.change_state(name, Transition.TRANSITION_ACTIVE_SHUTDOWN)

    def bring_up_in_order(self, order):
        """Configure then activate each node, strictly in the given
        startup order. Stops at the first node that fails, so you never
        end up with (say) navigation active while localization isn't.
        """
        for name in order:
            if not self.wait_for_node(name, timeout_sec=10.0):
                self._logger.error(f'{name}: service never appeared, aborting startup')
                return False
            if not self.configure(name):
                return False
            if not self.activate(name):
                return False
        return True

    def shutdown(self):
        """Stop the background client executor/thread and destroy the
        private client node. Call this from the orchestrator node's
        shutdown path.
        """
        self._client_executor.shutdown()
        self._client_node.destroy_node()
        self._client_thread.join(timeout=2.0)
