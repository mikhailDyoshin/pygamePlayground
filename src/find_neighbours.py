# from pygame import Vector2
from moving_object import MovingObject
from typing import Callable

type FindNeighbourRule = Callable[..., bool]


def radius_rule(o1: MovingObject, o2: MovingObject, radius: float) -> bool:
    return (o1.kinematics.position - o2.kinematics.position).magnitude() <= radius


def find_neighbours(
    moving_object: MovingObject,
    objects: dict[str, MovingObject],
    rule: FindNeighbourRule,
) -> dict[str, MovingObject]:
    return {
        key: o
        for key, o in objects.items()
        if rule(moving_object, o) and moving_object != o
    }
