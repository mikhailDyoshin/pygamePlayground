# Example file showing a circle moving on screen
import pygame
from moving_object import MovingObject, Size, update_objects, display_objects, initiate_dots
from periodic_printer import PeriodicPrinter

DOT_SIZE = Size(1, 1)

# printer = PeriodicPrinter(interval=1)

def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    clock = pygame.time.Clock()
    running = True
    dt = 0

    dots: tuple[MovingObject, ...] = initiate_dots(number=1000, size=DOT_SIZE, screen=screen)

    

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

        # if mouse_position:
        #     printer.update(dt, f"Steering: {dots[0].kinematics.velocity.magnitude()}")
        # else:
        #     printer.update(dt, f"Not Steering: {dots[0].kinematics.velocity.magnitude()}")


        display_objects(dots, screen=screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__': main()
