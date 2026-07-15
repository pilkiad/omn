"""Task manager: which task the robot is performing and its status.

Pure-Python (no ROS imports). Holds one active task plus a bounded history.
Task types map onto what the existing stack can do:

- ``navigate``  point-to-point navigation (goal published on /goal_pose,
                executed by the teammates' navigation2 A* node)
- ``map``       build a map with SLAM until confidence converges
- ``explore``   autonomous wandering (sim) / exploration node (robot)
- ``follow_red``  follow a person holding the red cube (follow_red node
                  publishes /target_vector, executed by collision_avoidance)
"""

import itertools
import time

TASK_NAVIGATE = 'navigate'
TASK_MAP = 'map'
TASK_EXPLORE = 'explore'
TASK_FOLLOW_RED = 'follow_red'

STATUS_PENDING = 'pending'
STATUS_ACTIVE = 'active'
STATUS_SUCCEEDED = 'succeeded'
STATUS_FAILED = 'failed'
STATUS_CANCELLED = 'cancelled'

_FINISHED = (STATUS_SUCCEEDED, STATUS_FAILED, STATUS_CANCELLED)


class Task:
    _ids = itertools.count(1)

    def __init__(self, task_type, params=None, clock=time.time):
        self.id = next(Task._ids)
        self.type = task_type
        self.params = params or {}
        self.status = STATUS_PENDING
        self.progress = 0.0
        self.detail = ''
        self.created = clock()
        self.started = None
        self.finished = None
        self._clock = clock

    @property
    def done(self):
        return self.status in _FINISHED

    def label(self):
        if self.type == TASK_NAVIGATE:
            x = self.params.get('x', 0.0)
            y = self.params.get('y', 0.0)
            return 'Navigate to ({:.2f}, {:.2f})'.format(x, y)
        if self.type == TASK_MAP:
            return 'Map the environment (SLAM)'
        if self.type == TASK_EXPLORE:
            return 'Explore autonomously'
        if self.type == TASK_FOLLOW_RED:
            return 'Follow the red cube'
        return self.type

    def snapshot(self):
        duration = None
        if self.started is not None:
            end = self.finished if self.finished is not None else self._clock()
            duration = round(end - self.started, 1)
        return {
            'id': self.id,
            'type': self.type,
            'label': self.label(),
            'params': self.params,
            'status': self.status,
            'progress': round(self.progress, 3),
            'detail': self.detail,
            'duration_s': duration,
        }


class TaskManager:
    def __init__(self, history_length=20, clock=time.time):
        self._clock = clock
        self.active = None
        self.history = []
        self._history_length = history_length

    def start(self, task_type, params=None):
        """Start a task. Returns the task, or None if one is already active."""
        if self.active is not None and not self.active.done:
            return None
        task = Task(task_type, params, clock=self._clock)
        task.status = STATUS_ACTIVE
        task.started = self._clock()
        self.active = task
        return task

    def update_progress(self, progress, detail=''):
        if self.active is not None and not self.active.done:
            self.active.progress = max(0.0, min(1.0, progress))
            if detail:
                self.active.detail = detail

    def _finish(self, status, detail=''):
        if self.active is None or self.active.done:
            return None
        self.active.status = status
        self.active.finished = self._clock()
        self.active.detail = detail or self.active.detail
        if status == STATUS_SUCCEEDED:
            self.active.progress = 1.0
        finished = self.active
        self.history.insert(0, finished)
        if len(self.history) > self._history_length:
            self.history.pop()
        return finished

    def succeed(self, detail=''):
        return self._finish(STATUS_SUCCEEDED, detail)

    def fail(self, detail=''):
        return self._finish(STATUS_FAILED, detail)

    def cancel(self, detail='cancelled by operator'):
        return self._finish(STATUS_CANCELLED, detail)

    @property
    def busy(self):
        return self.active is not None and not self.active.done

    def snapshot(self):
        return {
            'active': self.active.snapshot() if self.busy else None,
            'history': [task.snapshot() for task in self.history],
        }
