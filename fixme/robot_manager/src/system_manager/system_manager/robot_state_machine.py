"""Global Robot State Machine.

This is the "brain" state -- BOOTING / READY / MAPPING / NAVIGATING /
BUSY / ERROR / RECOVERY / SHUTDOWN. It is deliberately a plain Python
class with no ROS2 dependency, so it can be unit tested without rclpy
running at all. It is NOT the same thing as a lifecycle node's own
state (unconfigured/inactive/active/finalized) -- a node can be ACTIVE
while the robot as a whole is still BUSY or in RECOVERY.
"""

from enum import Enum
from typing import Callable, Optional


class RobotState(Enum):
    BOOTING = 'BOOTING'
    READY = 'READY'
    MAPPING = 'MAPPING'
    NAVIGATING = 'NAVIGATING'
    BUSY = 'BUSY'
    ERROR = 'ERROR'
    RECOVERY = 'RECOVERY'
    SHUTDOWN = 'SHUTDOWN'


# Single source of truth for which transitions are legal. Extend this
# table, don't scatter "if state == X" checks around the codebase.
ALLOWED_TRANSITIONS = {
    RobotState.BOOTING:    {RobotState.READY, RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.READY:      {RobotState.MAPPING, RobotState.NAVIGATING, RobotState.BUSY,
                             RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.MAPPING:    {RobotState.READY, RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.NAVIGATING: {RobotState.READY, RobotState.BUSY, RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.BUSY:       {RobotState.READY, RobotState.NAVIGATING, RobotState.MAPPING,
                             RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.ERROR:      {RobotState.RECOVERY, RobotState.SHUTDOWN},
    RobotState.RECOVERY:   {RobotState.READY, RobotState.ERROR, RobotState.SHUTDOWN},
    RobotState.SHUTDOWN:   set(),
}


class RobotStateMachine:

    def __init__(self, on_change: Optional[Callable[[RobotState, RobotState], None]] = None):
        self._state = RobotState.BOOTING
        self._on_change = on_change

    @property
    def state(self) -> RobotState:
        return self._state

    def can_transition(self, target: RobotState) -> bool:
        return target in ALLOWED_TRANSITIONS[self._state]

    def transition(self, target: RobotState) -> bool:
        if not self.can_transition(target):
            return False
        previous = self._state
        self._state = target
        if self._on_change:
            self._on_change(previous, target)
        return True
