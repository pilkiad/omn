"""Robot lifecycle state machine.

Pure-Python (no ROS imports) so it can be unit-tested and reused by both the
real ROS 2 node and the simulation backend.

The lifecycle models the whole mission flow of the Tortugabot stack:

    BOOT --> INITIALIZING --> MAPPING --> SAVING_MAP --> READY <--> EXECUTING
                  ^                                        |
                  |            (from any state)            v
                  +------- ESTOPPED / FAULT  <-------------+

- BOOT          process started, nothing verified yet
- INITIALIZING  waiting for critical sensor inputs (/scan, /pose)
- MAPPING       SLAM active; monitored via /slam_confidence
- SAVING_MAP    SLAM converged; calling /slam_toolbox/save_map
- READY         healthy, map available, waiting for a task
- EXECUTING     a task (e.g. point-to-point navigation) is active
- ESTOPPED      operator emergency stop; robot commanded to zero velocity
- FAULT         a critical health failure (sensor loss); task aborted
- SHUTDOWN      terminal state
"""

import time
from enum import Enum


class RobotState(Enum):
    BOOT = 'boot'
    INITIALIZING = 'initializing'
    MAPPING = 'mapping'
    SAVING_MAP = 'saving_map'
    READY = 'ready'
    EXECUTING = 'executing'
    ESTOPPED = 'estopped'
    FAULT = 'fault'
    SHUTDOWN = 'shutdown'


class RobotEvent(Enum):
    START = 'start'
    SENSORS_READY_MAP_MISSING = 'sensors_ready_map_missing'
    SENSORS_READY_MAP_AVAILABLE = 'sensors_ready_map_available'
    SLAM_CONVERGED = 'slam_converged'
    MAP_SAVED = 'map_saved'
    MAP_SAVE_FAILED = 'map_save_failed'
    TASK_STARTED = 'task_started'
    TASK_FINISHED = 'task_finished'
    REMAP_REQUESTED = 'remap_requested'
    MAPPING_CANCELLED = 'mapping_cancelled'
    ESTOP_PRESSED = 'estop_pressed'
    ESTOP_RELEASED = 'estop_released'
    CRITICAL_FAULT = 'critical_fault'
    FAULT_CLEARED = 'fault_cleared'
    SHUTDOWN = 'shutdown'


# Events accepted from ANY state.
_GLOBAL_TRANSITIONS = {
    RobotEvent.ESTOP_PRESSED: RobotState.ESTOPPED,
    RobotEvent.CRITICAL_FAULT: RobotState.FAULT,
    RobotEvent.SHUTDOWN: RobotState.SHUTDOWN,
}

_TRANSITIONS = {
    (RobotState.BOOT, RobotEvent.START): RobotState.INITIALIZING,
    (RobotState.INITIALIZING, RobotEvent.SENSORS_READY_MAP_MISSING): RobotState.MAPPING,
    (RobotState.INITIALIZING, RobotEvent.SENSORS_READY_MAP_AVAILABLE): RobotState.READY,
    (RobotState.MAPPING, RobotEvent.SLAM_CONVERGED): RobotState.SAVING_MAP,
    (RobotState.SAVING_MAP, RobotEvent.MAP_SAVED): RobotState.READY,
    (RobotState.SAVING_MAP, RobotEvent.MAP_SAVE_FAILED): RobotState.MAPPING,
    (RobotState.READY, RobotEvent.TASK_STARTED): RobotState.EXECUTING,
    (RobotState.READY, RobotEvent.REMAP_REQUESTED): RobotState.MAPPING,
    (RobotState.MAPPING, RobotEvent.MAPPING_CANCELLED): RobotState.READY,
    (RobotState.SAVING_MAP, RobotEvent.MAPPING_CANCELLED): RobotState.READY,
    (RobotState.EXECUTING, RobotEvent.TASK_FINISHED): RobotState.READY,
    (RobotState.ESTOPPED, RobotEvent.ESTOP_RELEASED): RobotState.INITIALIZING,
    (RobotState.FAULT, RobotEvent.FAULT_CLEARED): RobotState.INITIALIZING,
}

# States in which the robot may be commanded to move.
MOTION_ALLOWED_STATES = (RobotState.MAPPING, RobotState.READY, RobotState.EXECUTING)


class RobotLifecycle:
    """Event-driven finite state machine with a transition history."""

    def __init__(self, history_length=50, clock=time.time):
        self._clock = clock
        self.state = RobotState.BOOT
        self.history = []
        self._history_length = history_length
        self._record(None, self.state, 'boot')

    def _record(self, event, new_state, note=''):
        self.history.append({
            'time': self._clock(),
            'event': event.value if event else None,
            'state': new_state.value,
            'note': note,
        })
        if len(self.history) > self._history_length:
            self.history.pop(0)

    def can_handle(self, event):
        if event in _GLOBAL_TRANSITIONS:
            # Re-entering the same state is a no-op, not a transition.
            return _GLOBAL_TRANSITIONS[event] != self.state
        return (self.state, event) in _TRANSITIONS

    def handle(self, event, note=''):
        """Apply an event. Returns True if a transition happened."""
        if event in _GLOBAL_TRANSITIONS:
            target = _GLOBAL_TRANSITIONS[event]
            if target == self.state:
                return False
        elif (self.state, event) in _TRANSITIONS:
            target = _TRANSITIONS[(self.state, event)]
        else:
            return False

        self.state = target
        self._record(event, target, note)
        return True

    @property
    def motion_allowed(self):
        return self.state in MOTION_ALLOWED_STATES

    def snapshot(self):
        return {
            'state': self.state.value,
            'motion_allowed': self.motion_allowed,
            'history': list(self.history),
        }
