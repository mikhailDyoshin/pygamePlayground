
class PeriodicPrinter:
    def __init__(self, interval: float):
        self.interval = interval
        self.timer = 0.0

    def update(self, dt: float, message: str):
        self.timer += dt
        if self.timer >= self.interval:
            print(message)
            self.timer -= self.interval
            