import pygame

from world.world import World


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, world: World):
        self.screen.fill((10, 10, 20))

        # food
        for f in world.food:
            pygame.draw.circle(
                self.screen, (0, 200, 0), (int(f.coord.x), int(f.coord.y)), 3
            )

        # creatures
        for c in world.creatures:
            color = (200, 100, 255)
            pygame.draw.circle(self.screen, color, (int(c.coord.x), int(c.coord.y)), 5)
