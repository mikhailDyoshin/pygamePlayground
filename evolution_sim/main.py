import pygame
from render.renderer import Renderer
from world.world import World

WIDTH, HEIGHT = 900, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

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

pygame.quit()
