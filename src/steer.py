from pygame import Vector2

def steer(*, velocity: Vector2, position: Vector2, target: Vector2, max_speed: float):
    from moving_dot import random_vector
    desired = target - position
    desired = desired.normalize() * max_speed
    steer = desired - velocity
    return steer + random_vector(300)
