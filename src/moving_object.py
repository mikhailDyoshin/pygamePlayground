from dataclasses import dataclass, replace

from pygame import Rect, Surface, Vector2, draw

from moving_dot import get_position, get_velocity, screen_wrap
from steer import steer
from utils import ZERO_VECTOR, limit_vector, random_color_rgb, screen_center


@dataclass(frozen=True)
class Kinematics:
    velocity: Vector2
    position: Vector2


@dataclass(frozen=True)
class Size:
    width: float
    height: float


@dataclass(frozen=True)
class MovingObject:
    kinematics: Kinematics
    size: Size
    color: tuple[int, int, int]

    def _get_kinematics(
        self, *, screen: Surface, dt: float, target: Vector2 | None = None
    ) -> Kinematics:
        if target:
            steering_velocity = self.kinematics.velocity + steer(
                velocity=self.kinematics.velocity,
                position=self.kinematics.position,
                target=target,
                max_speed=200,
            )
            # print(f'Steering: {steering_velocity.magnitude()}')
        else:
            steering_velocity = self.kinematics.velocity
            # print(f'Not Steering: {steering_velocity.magnitude()}')

        velocity_with_noise = get_velocity(v0=steering_velocity, max_projection=100)

        limited_velocity = limit_vector(velocity_with_noise, 300)
        position = screen_wrap(
            position=get_position(
                s0=self.kinematics.position, v=limited_velocity, dt=dt
            ),
            width=screen.get_width(),
            height=screen.get_height(),
        )
        return Kinematics(velocity=limited_velocity, position=position)

    def update_kinematics(
        self, *, screen: Surface, dt: float, target: Vector2 | None = None
    ) -> "MovingObject":
        return replace(
            self, kinematics=self._get_kinematics(screen=screen, target=target, dt=dt)
        )

    def update_color(self, color: tuple[int, int, int]) -> "MovingObject":
        return replace(self, color=color)


def update_objects(
    objects: dict[str, MovingObject],
    screen: Surface,
    dt: float,
    target: Vector2 | None = None,
) -> dict[str, MovingObject]:
    return {
        key: mv.update_kinematics(screen=screen, dt=dt, target=target)
        for key, mv in objects.items()
    }


def draw_ellipse(*, screen: Surface, obj: MovingObject):
    rect = Rect(obj.kinematics.position, (obj.size.width, obj.size.height))
    draw.ellipse(screen, obj.color, rect)


def display_objects(objects: dict[str, MovingObject], screen: Surface) -> None:
    for obj in objects.values():
        draw_ellipse(screen=screen, obj=obj)


def initiate_dots(number: int, size: Size, screen: Surface) -> dict[str, MovingObject]:
    return {
        str(n): MovingObject(
            kinematics=Kinematics(velocity=ZERO_VECTOR, position=screen_center(screen)),
            size=size,
            color=random_color_rgb(),
        )
        for n in range(number)
    }
