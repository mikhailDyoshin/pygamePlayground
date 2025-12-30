# Example file showing a circle moving on screen
import pygame
from movement import get_distance, get_velocity, get_direction, get_acceleration
from fsm import FSM, Event, ShapeData, State, get_shape_data
from periodic_printer import PeriodicPrinter


def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    velocity = pygame.Vector2(0, 0)
    dt = 0

    # FSM
    fsm = FSM()

    # Sizes
    size = 40

    color = (0, 0, 0)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    shape_data = ShapeData(screen, (player_pos.x, player_pos.y), size, color)

    printer = PeriodicPrinter(1.0)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # pygame.draw.circle(screen, "red", player_pos, 40)

        # Moving player
        keys = pygame.key.get_pressed()
        direction = get_direction(keys)
        acc = get_acceleration(direction)
        velocity = get_velocity(velocity, dt, keys)
        player_pos = get_distance(player_pos, velocity, dt)

        if (velocity.length() == 0): fsm.trigger(Event.STOP)

        if (acc.length() == 0): fsm.trigger(Event.SLOW_DOWN)

        if (acc.length() != 0): fsm.trigger(Event.ACCELERATE)

        shape_data = get_shape_data(screen, player_pos, fsm.state)

        fsm.update(shape_data)
        message = f"""
            -----------------------------
            FSM state -> {fsm.state.name}
            Acceleration -> {acc}
            Velocity -> {velocity}
            Position -> {player_pos}
            -----------------------------
        """
        printer.update(dt, message)

        # print(f'Velocity -> {velocity}\nPosition -> {player_pos}')

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__': main()
