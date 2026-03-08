from dataclasses import dataclass, replace
from pygame import Vector2, Surface, draw, Rect
from moving_dot import get_velocity, get_position, screen_wrap
from utils import ZERO_VECTOR, screen_center, random_color_rgb, limit_vector


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

    def _get_kinematics(self, screen: Surface, dt: float) -> Kinematics:
        velocity = get_velocity(v0=self.kinematics.velocity, max_projection=10)
        limited_velocity = limit_vector(velocity, 300)
        position = screen_wrap(
            position=get_position(s0=self.kinematics.position, v=limited_velocity, dt=dt), 
            width=screen.get_width(),
            height=screen.get_height()
        )
        return Kinematics(
            velocity=limited_velocity,
            position=position
        )
    
    def update_kinematics(self, screen: Surface, dt: float) -> 'MovingObject':
        return replace(self, kinematics=self._get_kinematics(screen, dt))
    
def update_objects(objects: tuple[MovingObject, ...], screen: Surface, dt: float) -> tuple[MovingObject, ...]:
    return tuple([mv.update_kinematics(screen, dt) for mv in objects])

def draw_ellipse(
        *,
        screen: Surface, 
        obj: MovingObject
    ):
    rect = Rect(obj.kinematics.position, (obj.size.width, obj.size.height))
    draw.ellipse(screen, obj.color, rect)


def display_objects(objects: tuple[MovingObject, ...], screen: Surface) -> None:
    for obj in objects:
        draw_ellipse(screen=screen, obj=obj)


def initiate_dots(number: int, screen: Surface) -> tuple[MovingObject, ...]:
    return tuple([
            MovingObject(
                kinematics=Kinematics(velocity=ZERO_VECTOR, position=screen_center(screen)),
                size=Size(4, 4), 
                color=random_color_rgb()
            ) 
            for _ in range(number)]
        )