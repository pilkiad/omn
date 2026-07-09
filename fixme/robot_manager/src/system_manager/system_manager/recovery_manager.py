"""Recovery Manager.

Executes the failure policy table below. All decision logic lives in
the table, not in branching code -- extending it later (a new node, a
new dependency chain) is a data change, not a code change. This mirrors
the exact policies from the project spec:

  Localization fails -> deactivate navigation, motion_controller ->
                         recover localization -> reactivate in reverse
  Navigation fails    -> deactivate motion_controller -> recover navigation
                         -> reactivate motion_controller
  Controller fails    -> emergency stop
  Camera fails        -> recover camera (no dependents)
"""

from rclpy.node import Node


FAILURE_POLICY = {
    'camera_processor': {
        'deactivate_first': [],
        'reactivate_after': [],
    },
    'lidar_processor': {
        'deactivate_first': [],
        'reactivate_after': [],
    },
    'mapping': {
        'deactivate_first': [],
        'reactivate_after': [],
    },
    'localization': {
        'deactivate_first': ['navigation', 'motion_controller'],
        'reactivate_after': ['motion_controller', 'navigation'],
    },
    'navigation': {
        'deactivate_first': ['motion_controller'],
        'reactivate_after': ['motion_controller'],
    },
    'motion_controller': {
        'deactivate_first': [],
        'reactivate_after': [],
        'emergency_stop': True,
    },
}


class RecoveryManager:

    def __init__(self, node: Node, lifecycle_manager, health_monitor,
                 on_recovery_start=None, on_recovery_done=None, on_emergency_stop=None):
        self._node = node
        self._logger = node.get_logger()
        self._lm = lifecycle_manager
        self._hm = health_monitor
        self._on_recovery_start = on_recovery_start
        self._on_recovery_done = on_recovery_done
        self._on_emergency_stop = on_emergency_stop

    def handle_failure(self, failed_node: str):
        policy = FAILURE_POLICY.get(failed_node)
        if policy is None:
            self._logger.warn(f'No recovery policy defined for {failed_node}, doing nothing')
            return

        if policy.get('emergency_stop'):
            self._logger.error(f'{failed_node} failed -- EMERGENCY STOP')
            if self._on_emergency_stop:
                self._on_emergency_stop(failed_node)
            return

        if self._on_recovery_start:
            self._on_recovery_start(failed_node)

        for name in policy['deactivate_first']:
            self._hm.stop_expecting(name)
            self._lm.deactivate(name)

        self._logger.info(f'Recovering {failed_node}...')
        self._hm.stop_expecting(failed_node)
        self._lm.deactivate(failed_node)
        self._lm.cleanup(failed_node)
        recovered = self._lm.configure(failed_node) and self._lm.activate(failed_node)

        if not recovered:
            self._logger.error(f'{failed_node} could not be recovered')
            if self._on_emergency_stop:
                self._on_emergency_stop(failed_node)
            return

        self._hm.expect_active(failed_node)

        for name in policy['reactivate_after']:
            self._lm.activate(name)
            self._hm.expect_active(name)

        self._logger.info(f'{failed_node} recovered, downstream nodes reactivated')
        if self._on_recovery_done:
            self._on_recovery_done(failed_node)
