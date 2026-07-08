class LifecycleManager:
    """
    Simple lifecycle manager for the demo.
    """

    def __init__(self):
        self._nodes = {}

    def configure(self, node_name: str) -> bool:
        self._nodes[node_name] = "INACTIVE"
        return True

    def activate(self, node_name: str) -> bool:
        self._nodes[node_name] = "ACTIVE"
        return True

    def deactivate(self, node_name: str) -> bool:
        self._nodes[node_name] = "INACTIVE"
        return True

    def cleanup(self, node_name: str) -> bool:
        self._nodes[node_name] = "UNCONFIGURED"
        return True

    def shutdown(self, node_name: str) -> bool:
        self._nodes[node_name] = "FINALIZED"
        return True

    def get_state(self, node_name: str):
        return self._nodes.get(node_name, "UNKNOWN")