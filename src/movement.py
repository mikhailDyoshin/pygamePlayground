from pygame import (K_w, K_s, K_a, K_d, Vector2)
from pygame.key import ScancodeWrapper
from enum import Enum


FRICTION = 0.6 # per second
ACCELERATION = 300 # px/s^2
STOP_EPSILON = 5

class Direction(Enum):
    UP = Vector2(x=0, y=-1)
    DOWN = Vector2(x=0, y=1)
    LEFT = Vector2(x=-1, y=0)
    RIGHT = Vector2(x=1, y=0)


movement_dict = {
    K_a: Direction.LEFT,
    K_d: Direction.RIGHT,
    K_w: Direction.UP,
    K_s: Direction.DOWN,
}


def get_direction(pressed_keys: ScancodeWrapper) -> Vector2:
    init_vector = Vector2(0, 0)

    for key in movement_dict.keys():
        if (pressed_keys[key]):
            init_vector += movement_dict[key].value
    
    return init_vector


def get_acceleration(move: Vector2) -> Vector2:
    return Vector2(move.x * ACCELERATION, move.y * ACCELERATION)


def get_velocity(v0: Vector2, dt: float, pressed_keys: ScancodeWrapper) -> Vector2:
    acc = get_acceleration(get_direction(pressed_keys))

    if (acc.length() == 0 and v0.length() < STOP_EPSILON): return Vector2(0, 0)

    vel = (v0 + acc * dt)
    vel *= FRICTION ** dt
    return vel


def get_distance(s0: Vector2, v0: Vector2, dt: float) -> Vector2:
    return s0 + v0 * dt


def get_new_position(
        *, 
        keys: ScancodeWrapper, 
        dt: float, 
        current_velocity: Vector2, 
        current_position: Vector2
    ):
    return get_distance(
        current_position, 
        get_velocity(current_velocity, dt, keys), 
        dt
    )
