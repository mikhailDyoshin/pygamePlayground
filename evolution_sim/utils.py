from typing import Any, Callable, Iterable
from pygame import Vector2


def screen_wrap(
    position: Vector2, screen_width: float, screen_height: float
) -> Vector2:

    if position.x > screen_width:
        return Vector2(0, position.y)

    if position.x < 0:
        return Vector2(screen_width, position.y)

    if position.y > screen_height:
        return Vector2(position.x, 0)

    if position.y < 0:
        return Vector2(position.x, screen_height)

    return position


def join_any(items: Iterable[Any], separator: str = " ") -> str:
    return separator.join(str(item) for item in items)


def append_to_file(file_name: str, data: tuple[Any, ...], delimeter: str = " "):
    with open(file_name, "a") as f:
        f.write(f"{join_any(data, delimeter)}\n")


def get_data_from_file(file_name: str) -> tuple[list[float], list[float], list[float]]:
    population: list[float] = []
    speed: list[float] = []
    vision: list[float] = []

    with open(file_name) as f:
        for line in f:
            p, s, v = map(float, line.split())
            population.append(p)
            speed.append(s)
            vision.append(v)

    return (population, speed, vision)


def clear_file(file_name: str):
    with open(file_name, "w") as f:
        f.write("")


class PeriodicPrinter:
    def __init__(self, interval_sec: float):
        self.interval_sec = interval_sec
        self.timer = 0.0

    def update(self, dt: float, callback: Callable[[], None]):
        self.timer += dt
        if self.timer >= self.interval_sec:
            callback()
            self.timer -= self.interval_sec
