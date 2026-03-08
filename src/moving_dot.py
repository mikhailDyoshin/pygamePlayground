from pygame import Vector2
from shape import ShapeData
from dataclasses import replace
from random import randint
from typing import Callable


def screen_wrap(position: Vector2, width: float, height: float) -> Vector2:

    if (position.x > width): return Vector2(0, position.y)

    if (position.x < 0): return Vector2(width, position.y)

    if (position.y > height): return Vector2(position.x, 0)

    if (position.y < 0): return Vector2(position.x, height)

    return position


def random_vector(max_projection: int) -> Vector2:
    x_projection = randint(0, max_projection)
    y_projection = randint(0, max_projection)
    return Vector2(
        x_projection*randint(-1, 1), 
        y_projection*randint(-1, 1)
    )

type VectorTransformer = Callable[[Vector2], Vector2]

def randomized(max_projection: int) -> Callable[[VectorTransformer], VectorTransformer]:
    def randomized(func: VectorTransformer) -> VectorTransformer:
        def inner(vector: Vector2) -> Vector2:
            return func(vector) + random_vector(max_projection)
        return inner
    return randomized


def get_velocity(*, v0: Vector2, max_projection: int) -> Vector2:
    return v0 + random_vector(max_projection)

def get_position(*, s0: Vector2, v: Vector2, dt: float) -> Vector2:
    return s0 + v * dt





def update_shape_position(
        *,
        position: Vector2, 
        shape: ShapeData
    ) -> ShapeData:
    return replace(shape, position=position)
