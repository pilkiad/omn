from collections import deque
from typing import Optional

from .models import Task


class TaskQueue:
    """FIFO queue for robot tasks."""

    def __init__(self):
        """Initialize an empty task queue."""
        self._queue = deque()

    def add_task(self, task: Task) -> None:
        """Add a task to the end of the queue."""

        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task.")

        self._queue.append(task)

    def get_next_task(self) -> Optional[Task]:
        """
        Remove and return the next task.

        Returns:
            Task if available, otherwise None.
        """

        if self.is_empty():
            return None

        return self._queue.popleft()

    def peek(self) -> Optional[Task]:
        """Return the next task without removing it."""

        if self.is_empty():
            return None

        return self._queue[0]

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""

        return len(self._queue) == 0

    def size(self) -> int:
        """Return the number of queued tasks."""

        return len(self._queue)