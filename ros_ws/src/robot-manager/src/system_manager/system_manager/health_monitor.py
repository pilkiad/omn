from .models import HealthStatus


class HealthMonitor:
    """
    Tracks the overall health status of the robot.
    """

    def __init__(self):
        self._health_status = HealthStatus.HEALTHY

    def get_health_status(self) -> HealthStatus:
        """Return the current health status."""
        return self._health_status

    def set_health_status(self, status: HealthStatus) -> None:
        """Update the current health status."""
        self._health_status = status

    def is_healthy(self) -> bool:
        """Return True if the robot is healthy."""
        return self._health_status == HealthStatus.HEALTHY