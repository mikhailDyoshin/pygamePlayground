import random

from pygame import Vector2


def screen_wrap(
    position: Vector2, screen_width: float, screen_height: float
) -> Vector2:

    if position.x > screen_width:
        return Vector2(0, position.y)

    if position.x < 0:
        return Vector2(screen_width, position.y)

    if position.y > screen_height:
        return Vector2(position.x, 0)

    if position.y < 0:
        return Vector2(position.x, screen_height)

    return position


class Creature:
    def __init__(self, w, h):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.coord = Vector2(self.x, self.y)

        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.velocity = Vector2(self.vx, self.vy)

        self.energy = 100
        self.speed = random.uniform(1, 2)
        self.vision = 80

        self.dead = False

    def update(self, world):
        if self.dead:
            return

        self.energy -= 0.1
        if self.energy <= 0:
            self.dead = True
            return

        # 1. find nearest food
        target = self.find_food(world.food)

        if target:
            self.velocity = self.move_towards(target.coord)
        else:
            self.velocity += self.wander()

        self.coord += self.velocity * self.speed
        self.coord = screen_wrap(self.coord, world.w, world.h)

        self.eat(world)

    def find_food(self, food_list):
        closest = None
        closest_dist = float("inf")

        for f in food_list:
            d = self.coord.distance_squared_to(f.coord)
            if d < self.vision**2 and d < closest_dist:
                closest = f
                closest_dist = d

        return closest

    def move_towards(self, target):
        direction = (target - self.coord).normalize()
        return direction

    def wander(self):
        return Vector2(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2))

    def eat(self, world):
        for f in world.food:
            if self.coord.distance_to(f.coord) < 5:
                self.energy += f.energy
                world.food.remove(f)
                break
