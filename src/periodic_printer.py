class PeriodicPrinter:
    def __init__(self, interval_sec: float):
        self.interval_sec = interval_sec
        self.timer = 0.0

    def update(self, dt: float, message: str):
        self.timer += dt
        if self.timer >= self.interval_sec:
            print(message)
            self.timer -= self.interval_sec
