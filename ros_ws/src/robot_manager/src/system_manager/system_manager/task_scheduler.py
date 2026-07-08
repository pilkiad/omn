"""Task Scheduler.

Decides, for every incoming task request, whether to run it now, queue
it, reject it, or interrupt whatever's currently running -- based on
priority. Pure decision logic, no ROS2 calls in here at all, so it's
trivially unit-testable. The orchestrator wires the result into the
LifecycleManager and RobotStateMachine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import heapq
import itertools


class TaskState(Enum):
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'
    INTERRUPTED = 'INTERRUPTED'
    REJECTED = 'REJECTED'
    DONE = 'DONE'
    FAILED = 'FAILED'


# Priorities from the project spec. Higher wins.
PRIORITY = {
    'emergency_stop': 100,
    'navigation': 50,
    'mapping': 20,
}


@dataclass(order=True)
class _QueueItem:
    neg_priority: int
    seq: int
    task_id: str = field(compare=False)
    task_name: str = field(compare=False)
    priority: int = field(compare=False)


class TaskScheduler:

    def __init__(self, on_state_change=None):
        self._queue = []
        self._counter = itertools.count()
        self._current: Optional[_QueueItem] = None
        self._on_state_change = on_state_change

    @property
    def current_task(self):
        return self._current

    def submit(self, task_id: str, task_name: str) -> TaskState:
        priority = PRIORITY.get(task_name, 0)
        item = _QueueItem(-priority, next(self._counter), task_id, task_name, priority)

        if self._current is None:
            self._current = item
            self._notify(task_id, task_name, TaskState.RUNNING, priority)
            return TaskState.RUNNING

        if priority > self._current.priority:
            interrupted = self._current
            self._notify(interrupted.task_id, interrupted.task_name,
                         TaskState.INTERRUPTED, interrupted.priority)
            heapq.heappush(self._queue, interrupted)
            self._current = item
            self._notify(task_id, task_name, TaskState.RUNNING, priority)
            return TaskState.RUNNING

        if priority == self._current.priority:
            self._notify(task_id, task_name, TaskState.REJECTED, priority,
                        reason='same priority as current task')
            return TaskState.REJECTED

        heapq.heappush(self._queue, item)
        self._notify(task_id, task_name, TaskState.QUEUED, priority)
        return TaskState.QUEUED

    def complete_current(self):
        if self._current is None:
            return
        done = self._current
        self._notify(done.task_id, done.task_name, TaskState.DONE, done.priority)
        self._current = heapq.heappop(self._queue) if self._queue else None
        if self._current:
            self._notify(self._current.task_id, self._current.task_name,
                        TaskState.RUNNING, self._current.priority)

    def _notify(self, task_id, task_name, state, priority, reason=''):
        if self._on_state_change:
            self._on_state_change(task_id, task_name, state, priority, reason)
