""" Dashboard
    │
    ▼
SystemManager
    │
    ▼
TaskScheduler
    │
    ▼
TaskQueue
"""

from datetime import datetime
from typing import Optional

from .models import (
    GoalPose,
    Task,
    TaskPriority,
    TaskStatus,
    TaskType,
)
from .task_queue import TaskQueue

class TaskScheduler:
    """
    Responsible for creating, scheduling and tracking robot tasks.

    This class does NOT execute tasks.
    It only manages their lifecycle.
    """

    def __init__(self):
        self._queue = TaskQueue()
        self._current_task: Optional[Task] = None
        self._next_task_id = 1

    def schedule_navigation(
        self,
        goal: GoalPose,
        priority: TaskPriority = TaskPriority.NORMAL,
    ) -> Task:
        """
        Create a navigation task and add it to the queue.
        """

        task = Task(
            id=self._next_task_id,
            type=TaskType.NAVIGATION,
            goal=goal,
            priority=priority,
        )

        self._next_task_id += 1

        self._queue.add_task(task)

        return task

    def schedule_mapping(
        self,
        goal: GoalPose,
        priority: TaskPriority = TaskPriority.NORMAL,
    ) -> Task:
        """
        Create a mapping task and add it to the queue.
        """

        task = Task(
            id=self._next_task_id,
            type=TaskType.MAPPING,
            goal=goal,
            priority=priority,
        )

        self._next_task_id += 1

        self._queue.add_task(task)

        return task

    def dispatch_next_task(self) -> Optional[Task]:
        """
        Move the next queued task to the current task.

        Returns:
            Task if dispatched, otherwise None.
        """

        if self.has_active_task():
            return None

        task = self._queue.get_next_task()

        if task is None:
            return None

        self._current_task = task
        self._current_task.update_status(TaskStatus.RUNNING)

        return task

    def complete_current_task(self) -> bool:
        """Mark the current task as completed."""

        if self._current_task is None:
            return False

        self._current_task.update_status(TaskStatus.COMPLETED)
        self._current_task = None

        return True

    def fail_current_task(self) -> bool:
        """Mark the current task as failed."""

        if self._current_task is None:
            return False

        self._current_task.update_status(TaskStatus.FAILED)
        self._current_task = None

        return True

    def cancel_current_task(self) -> bool:
        """Cancel the current task."""

        if self._current_task is None:
            return False

        self._current_task.update_status(TaskStatus.CANCELLED)
        self._current_task = None

        return True

    def get_current_task(self) -> Optional[Task]:
        """Return the current task."""

        return self._current_task

    def has_active_task(self) -> bool:
        """Return True if a task is currently active."""

        return self._current_task is not None

    def has_pending_tasks(self) -> bool:
        """Return True if tasks are waiting in the queue."""

        return not self._queue.is_empty()

    def pending_task_count(self) -> int:
        """Return the number of queued tasks."""

        return self._queue.size()