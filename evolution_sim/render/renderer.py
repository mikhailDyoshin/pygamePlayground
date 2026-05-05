import pygame

from world.world import World


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, world: World):
        self.screen.fill((10, 10, 20))
        avg_speed = sum(c.speed for c in world.creatures) / len(world.creatures)
        avg_vision = sum(c.vision for c in world.creatures) / len(world.creatures)
        strings = (
            f"Population: {len(world.creatures)}",
            f"Food: {len(world.food)}",
            f"Average speed: {avg_speed}",
            f"Average vision: {avg_vision}",
        )

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
                pygame.draw.line(self.screen, (255, 255, 255), c.coord, c.child.coord)

        for i, s in enumerate(strings):
            self._draw_text(s, (10, 10 + i * 20))

    def _draw_creatures_number(self, creatures_number: str, placement: tuple[int, int]):
        self._draw_text(creatures_number, placement)

    def _draw_text(self, text: str, placement: tuple[int, int]):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, placement)
