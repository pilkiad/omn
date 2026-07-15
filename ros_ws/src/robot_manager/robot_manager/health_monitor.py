"""Component health monitor.

Pure-Python (no ROS imports). Each monitored component is fed "beats"
(one per received message); the monitor derives message rate and age and
classifies the component as OK / WARN / DOWN.

Components marked ``critical`` drive the lifecycle: if any critical
component goes DOWN the robot manager raises a CRITICAL_FAULT.
"""

import time

STATUS_OK = 'ok'
STATUS_WARN = 'warn'
STATUS_DOWN = 'down'
STATUS_UNKNOWN = 'unknown'

_STATUS_RANK = {STATUS_OK: 0, STATUS_UNKNOWN: 1, STATUS_WARN: 2, STATUS_DOWN: 3}


class ComponentHealth:
    def __init__(self, name, label, expected_rate_hz, warn_after_s, down_after_s,
                 critical=False, clock=time.time):
        self.name = name
        self.label = label
        self.expected_rate_hz = expected_rate_hz
        self.warn_after_s = warn_after_s
        self.down_after_s = down_after_s
        self.critical = critical
        self._clock = clock
        self._beat_times = []
        self.last_beat = None
        self.total_beats = 0

    def beat(self, stamp=None):
        now = stamp if stamp is not None else self._clock()
        self.last_beat = now
        self.total_beats += 1
        self._beat_times.append(now)
        # Keep a 5-second window for rate estimation.
        cutoff = now - 5.0
        while self._beat_times and self._beat_times[0] < cutoff:
            self._beat_times.pop(0)

    def rate(self, now=None):
        now = now if now is not None else self._clock()
        recent = [t for t in self._beat_times if t >= now - 5.0]
        if len(recent) < 2:
            return 0.0
        span = recent[-1] - recent[0]
        if span <= 0.0:
            return 0.0
        return (len(recent) - 1) / span

    def age(self, now=None):
        if self.last_beat is None:
            return None
        now = now if now is not None else self._clock()
        return max(0.0, now - self.last_beat)

    def status(self, now=None):
        now = now if now is not None else self._clock()
        age = self.age(now)
        if age is None:
            return STATUS_UNKNOWN
        if age >= self.down_after_s:
            return STATUS_DOWN
        if age >= self.warn_after_s:
            return STATUS_WARN
        return STATUS_OK

    def snapshot(self, now=None):
        now = now if now is not None else self._clock()
        age = self.age(now)
        return {
            'name': self.name,
            'label': self.label,
            'status': self.status(now),
            'critical': self.critical,
            'rate_hz': round(self.rate(now), 2),
            'expected_rate_hz': self.expected_rate_hz,
            'age_s': round(age, 2) if age is not None else None,
            'total_messages': self.total_beats,
        }


class HealthMonitor:
    def __init__(self, clock=time.time):
        self._clock = clock
        self._components = {}
        self.battery_percent = None  # None = no battery telemetry available

    def add_component(self, name, label, expected_rate_hz, warn_after_s,
                      down_after_s, critical=False):
        self._components[name] = ComponentHealth(
            name, label, expected_rate_hz, warn_after_s, down_after_s,
            critical=critical, clock=self._clock)
        return self._components[name]

    def beat(self, name, stamp=None):
        component = self._components.get(name)
        if component is not None:
            component.beat(stamp)

    def set_battery(self, percent):
        self.battery_percent = percent

    def component(self, name):
        return self._components.get(name)

    def overall_status(self, now=None):
        now = now if now is not None else self._clock()
        worst = STATUS_OK
        for component in self._components.values():
            status = component.status(now)
            if status == STATUS_UNKNOWN and not component.critical:
                continue
            if _STATUS_RANK[status] > _STATUS_RANK[worst]:
                worst = status
        return worst

    def critical_failure(self, now=None):
        """Name of the first critical component that is DOWN, else None."""
        now = now if now is not None else self._clock()
        for component in self._components.values():
            if component.critical and component.status(now) == STATUS_DOWN:
                return component.name
        return None

    def all_critical_ok(self, now=None):
        now = now if now is not None else self._clock()
        return all(
            component.status(now) == STATUS_OK
            for component in self._components.values()
            if component.critical
        )

    def snapshot(self, now=None):
        now = now if now is not None else self._clock()
        return {
            'overall': self.overall_status(now),
            'battery_percent': self.battery_percent,
            'components': [
                component.snapshot(now)
                for component in self._components.values()
            ],
        }
