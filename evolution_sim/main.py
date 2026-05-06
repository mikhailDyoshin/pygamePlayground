import pygame
from evolution_sim.render.renderer import Renderer
from evolution_sim.world.world import World
from evolution_sim.utils import clear_file, append_to_file, PeriodicPrinter

clear_file("data.txt")

WIDTH, HEIGHT = 900, 600


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    periodic_printer = PeriodicPrinter(10000)
    world = World(WIDTH, HEIGHT)
    renderer = Renderer(screen)

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        world.update()
        renderer.draw(world)

        pygame.display.flip()
        data = (world.population, world.avg_speed, world.avg_vision)
        periodic_printer.update(dt, lambda: append_to_file("data.txt", data))

    pygame.quit()
