"""SLAM performance tracking.

Consumes the JSON payload published by the teammates' ``slam_analyzer`` node on
``/slam_confidence``::

    {"confidence": 0.83, "frontier_ratio": 0.01,
     "unknown_ratio": 0.44, "growth_ratio": 0.02}

and keeps a bounded time series for the dashboard chart, plus the debounced
convergence check that decides when mapping is complete (confidence must stay
above the threshold for a hold period — same intent as the original
system_manager, but self-contained and unit-testable).
"""

import time
from collections import deque


class SlamMetrics:
    def __init__(self, history_length=120, convergence_threshold=0.97,
                 hold_seconds=5.0, clock=time.time):
        self._clock = clock
        self.history = deque(maxlen=history_length)
        self.convergence_threshold = convergence_threshold
        self.hold_seconds = hold_seconds
        self.latest = None
        self._above_since = None
        self.converged = False

    def update(self, confidence, frontier_ratio=None, unknown_ratio=None,
               growth_ratio=None, stamp=None):
        now = stamp if stamp is not None else self._clock()

        # The analyzer may report confidence either as 0..1 or as a percent.
        if confidence > 1.0:
            confidence = confidence / 100.0
        confidence = max(0.0, min(1.0, confidence))

        sample = {
            'time': now,
            'confidence': confidence,
            'frontier_ratio': frontier_ratio,
            'unknown_ratio': unknown_ratio,
            'growth_ratio': growth_ratio,
        }
        self.latest = sample
        self.history.append(sample)

        # Debounced convergence: threshold must hold continuously.
        if confidence >= self.convergence_threshold:
            if self._above_since is None:
                self._above_since = now
            elif now - self._above_since >= self.hold_seconds:
                self.converged = True
        else:
            self._above_since = None

        return self.converged

    def hold_progress(self, now=None):
        """0..1 progress of the convergence hold timer."""
        if self.converged:
            return 1.0
        if self._above_since is None:
            return 0.0
        now = now if now is not None else self._clock()
        return min(1.0, (now - self._above_since) / self.hold_seconds)

    def reset_convergence(self):
        self.converged = False
        self._above_since = None

    def snapshot(self):
        return {
            'latest': self.latest,
            'converged': self.converged,
            'threshold': self.convergence_threshold,
            'hold_progress': round(self.hold_progress(), 3),
            'history': list(self.history),
        }
