import pygame

from world.world import World


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, world: World):
        self.screen.fill((10, 10, 20))

        # food
        for f in world.food:
            pygame.draw.circle(
                self.screen, (0, 200, 0), (int(f.coord.x), int(f.coord.y)), 3
            )

        # creatures
        for c in world.creatures:
            pygame.draw.circle(
                self.screen, c.color, (int(c.coord.x), int(c.coord.y)), 5
            )
            if c.child:
                # print(f"Parent: {c.coord}, Child: {c.child.coord}")
                pygame.draw.line(self.screen, (255, 255, 255), c.coord, c.child.coord)

        self._draw_creatures_number(str(len(world.creatures)), (10, 10))
        self._draw_creatures_number(str(len(world.food)), (10, 30))

    def _draw_creatures_number(self, creatures_number: str, placement: tuple[int, int]):
        self._draw_text(creatures_number, placement)

    def _draw_text(self, text: str, placement: tuple[int, int]):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, placement)
