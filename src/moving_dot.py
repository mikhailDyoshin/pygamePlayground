from pygame import Vector2
from shape import ShapeData
from dataclasses import replace


def screen_wrap(position: Vector2, width: float) -> Vector2:
    return Vector2(0, position.y) if position.x > width else position


def get_position(*, s0: Vector2, v: Vector2, dt: float) -> Vector2:
    return s0 + v * dt


def update_shape_position(
        *,
        position: Vector2, 
        shape: ShapeData
    ) -> ShapeData:
    return replace(shape, position=position)
