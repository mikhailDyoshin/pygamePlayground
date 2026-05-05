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
