from copy import copy
from random import randint
from typing import Any
from pygame import Surface, Vector2

ZERO_VECTOR = Vector2(0, 0)


def screen_center(screen: Surface) -> Vector2:
    return Vector2(screen.get_width() / 2, screen.get_height() / 2)


def random_color_rgb() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def limit_vector(vector: Vector2, max_magnitude: float) -> Vector2:
    vector_copy = copy(vector)

    if vector.magnitude() > max_magnitude:
        vector_copy.scale_to_length(max_magnitude)
        return vector_copy

    return vector_copy


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


def append_to_file(file_name: str, data: tuple[Any, ...], delimeter: str = " "):
    with open(file_name, "a") as f:
        f.write(delimeter.join(data))


def clear_file(file_name: str):
    with open(file_name, "w") as f:
        f.write("")
