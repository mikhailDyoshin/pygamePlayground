from typing import Callable


class PeriodicPrinter:
    def __init__(self, interval_sec: float):
        self.interval_sec = interval_sec
        self.timer = 0.0

    def update(self, dt: float, callback: Callable):
        self.timer += dt
        if self.timer >= self.interval_sec:
            callback()
            self.timer -= self.interval_sec
