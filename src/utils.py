from random import randint
from pygame import Vector2, Surface
from copy import copy

ZERO_VECTOR = Vector2(0, 0)

def screen_center(screen: Surface) -> Vector2:
    return Vector2(
        screen.get_width() / 2, 
        screen.get_height() / 2
    )

def random_color_rgb() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def limit_vector(vector: Vector2, max_magnitude: float) -> Vector2:
    vector_copy = copy(vector)

    if (vector.magnitude() > max_magnitude):
        vector_copy.scale_to_length(max_magnitude)
        return vector_copy
    
    return vector_copy

