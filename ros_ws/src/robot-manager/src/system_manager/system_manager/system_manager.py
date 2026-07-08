from .models import GoalPose, RobotState
from .state_machine import StateMachine
from .task_scheduler import TaskScheduler
from .health_monitor import HealthMonitor
from .lifecycle_manager import LifecycleManager



class SystemManager:
    """
    Central coordinator for the robot.
    """

    def __init__(self):
        self._state_machine = StateMachine()
        self._task_scheduler = TaskScheduler()
        self._health_monitor = HealthMonitor()
        self._lifecycle_manager = LifecycleManager()


    def activate_navigation(self):
        self._lifecycle_manager.configure("nav2")
        return self._lifecycle_manager.activate("nav2")


    def activate_mapping(self):
        self._lifecycle_manager.configure("slam_toolbox")
        return self._lifecycle_manager.activate("slam_toolbox")


    def get_navigation_state(self):
        return self._lifecycle_manager.get_state("nav2")


    def get_mapping_state(self):
        return self._lifecycle_manager.get_state("slam_toolbox")



    def get_health_status(self):
        return self._health_monitor.get_health_status()


    def is_robot_healthy(self):
        return self._health_monitor.is_healthy()

    # ------------------------------------------------------------------
    # Robot State
    # ------------------------------------------------------------------

    def get_robot_state(self) -> RobotState:
        return self._state_machine.get_state()

    def initialize_robot(self) -> bool:
        """
        Initialize the robot.

        UNKNOWN -> INITIALIZING -> READY
        """

        if not self._state_machine.transition(RobotState.INITIALIZING):
            return False

        return self._state_machine.transition(RobotState.READY)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def schedule_navigation(self, x: float, y: float, yaw: float = 0.0):
        goal = GoalPose(x=x, y=y, yaw=yaw)
        return self._task_scheduler.schedule_navigation(goal)

    def schedule_mapping(self, x: float, y: float, yaw: float = 0.0):
        goal = GoalPose(x=x, y=y, yaw=yaw)
        return self._task_scheduler.schedule_mapping(goal)

    # ------------------------------------------------------------------
    # Task Control
    # ------------------------------------------------------------------

    def dispatch_next_task(self):
        """
        Dispatch the next queued task.
        """

        task = self._task_scheduler.dispatch_next_task()

        if task is None:
            return None

        if self.get_robot_state() == RobotState.READY:
            self._state_machine.transition(RobotState.BUSY)

        return task

    def complete_current_task(self) -> bool:
        success = self._task_scheduler.complete_current_task()

        if success:
            self._state_machine.transition(RobotState.READY)

        return success

    def fail_current_task(self) -> bool:
        success = self._task_scheduler.fail_current_task()

        if success:
            self._state_machine.transition(RobotState.ERROR)

        return success

    def cancel_current_task(self) -> bool:
        success = self._task_scheduler.cancel_current_task()

        if success:
            self._state_machine.transition(RobotState.READY)

        return success

    # ------------------------------------------------------------------
    # Information
    # ------------------------------------------------------------------

    def get_current_task(self):
        return self._task_scheduler.get_current_task()

    def pending_task_count(self):
        return self._task_scheduler.pending_task_count()