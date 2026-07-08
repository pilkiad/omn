from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum,auto



"""
======================================================================
ROBOT MISSION & HEALTH MANAGEMENT MODELS
======================================================================

This module defines the schema for managing robot tasks, states, 
and system health monitoring.

Core Architecture:
  ├── RobotState     - Current physical/operational state of the robot.
  ├── TaskType       - Enum/Choices for types of tasks (e.g., Navigation, Idle).
  ├── TaskStatus     - Enum/Choices for task lifecycle (e.g., Pending, Active, Failed).
  ├── HealthStatus   - System-wide health metrics and node status.
  ├── RecoveryStatus - Tracks active recovery behaviors during node failures.
  ├── TaskPriority   - Enum for task urgency (e.g., Low, Medium, High).
  ├── GoalPose       - Spatial coordinates (X, Y, Z, Orientation) for navigation goals.
  └── Task           - The primary execution unit linking State, Priority, and Goal.
======================================================================
"""


class RobotState(Enum):
    """Represents the overall state of the robot."""

    UNKNOWN = auto()
    INITIALIZING = auto()
    READY = auto()
    BUSY = auto()
    ERROR = auto()
    EMERGENCY_STOPPED = auto()
    SHUTDOWN = auto()
   
class TaskType(Enum):
    """Types of user-requested tasks."""

    NAVIGATION = auto()
    MAPPING = auto()

class TaskStatus(Enum):
    """Represents the execution status of a task."""

    QUEUED = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    CANCELLED = auto()

class HealthStatus(Enum):
    """Represents the overall health of the robot."""

    UNKNOWN = auto()
    HEALTHY = auto()
    DEGRADED = auto()
    CRITICAL = auto()

class RecoveryStatus(Enum):
    """Recovery process status."""

    NOT_REQUIRED = auto()
    IN_PROGRESS = auto()
    RECOVERED = auto()
    FAILED = auto()

class TaskPriority(Enum):
    """Task priority."""

    LOW = auto()
    NORMAL = auto()
    HIGH = auto()

@dataclass
class GoalPose:
    """2D navigation goal."""

    x: float
    y: float
    yaw: float

@dataclass
class Task:
    """Represents a robot task."""

    id: int
    type: TaskType
    goal: GoalPose

    priority: TaskPriority = TaskPriority.NORMAL
    status: TaskStatus = TaskStatus.QUEUED

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def update_status(self, status: TaskStatus) -> None:
        """
        Update the task status and refresh the update timestamp.
        """
        self.status = status
        self.updated_at = datetime.now()