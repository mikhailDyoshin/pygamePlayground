# Example file showing a circle moving on screen
from functools import partial

import pygame  # type: ignore

from find_neighbours import find_neighbours, radius_rule
from moving_object import (
    MovingObject,
    Size,
    display_objects,
    initiate_dots,
    update_objects,
)
from periodic_printer import PeriodicPrinter
from utils import random_color_rgb

DIMENSION = 20
DOT_SIZE = Size(DIMENSION, DIMENSION)
DOTS_NUMBER = 7
printer = PeriodicPrinter(interval_sec=1)


def main():
    v = pygame.Vector2(2, 0)
    print(v)
    print(v.magnitude())

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    clock = pygame.time.Clock()
    running = True
    dt = 0

    dots: dict[str, MovingObject] = initiate_dots(
        number=DOTS_NUMBER, size=DOT_SIZE, screen=screen
    )

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        mouse_position: pygame.Vector2 | None = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_position = event.pos

        screen.fill("black")

        dots = update_objects(dots, screen, dt, mouse_position)

        for d in dots:
            ns = find_neighbours(dots[d], dots, partial(radius_rule, radius=50))
            for key, n in ns.items():
                dots[key] = n.update_color(random_color_rgb())

        display_objects(dots, screen=screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
