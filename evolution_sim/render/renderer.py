import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, world):
        self.screen.fill((10, 10, 20))

        # food
        for f in world.food:
            pygame.draw.circle(self.screen, (0, 200, 0), (int(f.x), int(f.y)), 3)

        # creatures
        for c in world.creatures:
            color = (200, 100, 255)
            pygame.draw.circle(self.screen, color, (int(c.x), int(c.y)), 5)
