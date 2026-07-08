from .models import RobotState


class InvalidStateTransition(Exception):
    """Raised when an invalid robot state transition is attempted."""


class StateMachine:
    """Manages robot state transitions."""

    _ALLOWED_TRANSITIONS = {
        RobotState.UNKNOWN: {
            RobotState.INITIALIZING,
            RobotState.SHUTDOWN,
        },
        RobotState.INITIALIZING: {
            RobotState.READY,
            RobotState.ERROR,
            RobotState.SHUTDOWN,
        },
        RobotState.READY: {
            RobotState.BUSY,
            RobotState.ERROR,
            RobotState.EMERGENCY_STOPPED,
            RobotState.SHUTDOWN,
        },
        RobotState.BUSY: {
            RobotState.READY,
            RobotState.ERROR,
            RobotState.EMERGENCY_STOPPED,
            RobotState.SHUTDOWN,
        },
        RobotState.ERROR: {
            RobotState.INITIALIZING,
            RobotState.EMERGENCY_STOPPED,
            RobotState.SHUTDOWN,
        },
        RobotState.EMERGENCY_STOPPED: {
            RobotState.INITIALIZING,
            RobotState.SHUTDOWN,
        },
        RobotState.SHUTDOWN: set(),
    }

    def __init__(self):
        self._current_state = RobotState.UNKNOWN

    def get_state(self) -> RobotState:
        return self._current_state

    def can_transition(self, new_state: RobotState) -> bool:
        return new_state in self._ALLOWED_TRANSITIONS[self._current_state]

    def transition(self, new_state: RobotState) -> bool:
        if not self.can_transition(new_state):
            return False

        self._current_state = new_state
        return True