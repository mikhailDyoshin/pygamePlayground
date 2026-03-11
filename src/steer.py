from pygame import Vector2


def get_target_direction(current_position: Vector2, target: Vector2) -> Vector2:
    return target - current_position


def get_opposite_target_direction(
    current_position: Vector2, target: Vector2
) -> Vector2:
    return -get_target_direction(current_position=current_position, target=target)


def steer(*, velocity: Vector2, position: Vector2, target: Vector2, max_speed: float):
    from moving_dot import random_vector

    desired_direction = get_target_direction(current_position=position, target=target)
    steer = desired_direction.normalize() * max_speed - velocity
    return steer + random_vector(300)
