import random

from pygame import Vector2

LINE_TIMER = 100
SPEED = random.uniform(2, 4)


def screen_wrap(
    position: Vector2,
    screen_width: float,
    screen_height: float,
) -> Vector2:

    if position.x > screen_width:
        return Vector2(screen_width, position.y)

    if position.x < 0:
        return Vector2(0, position.y)

    if position.y > screen_height:
        return Vector2(position.x, screen_height)

    if position.y < 0:
        return Vector2(position.x, 0)

    return position


class Creature:
    def __init__(self, w, h):
        self._x = random.randint(0, w)
        self._y = random.randint(0, h)
        self.coord = Vector2(self._x, self._y)

        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.velocity = Vector2(self.vx, self.vy)

        self.energy = 100
        self.speed = SPEED
        self.vision = 80

        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

        self.child = None
        self.line_timer = LINE_TIMER
        # self.age = 0

        self.dead = False

    def update(self, world):
        if self.dead:
            return

        self.energy -= 0.1
        self.energy -= 0.001 * self.vision
        self.energy -= 0.001 * self.speed

        if self.energy <= 0:
            self.dead = True
            return

        # self.age += 0.1
        # if self.age >= 300:
        #     self.dead = True
        #     return

        # 1. find nearest food
        target = self.find_food(world.food)

        if target:
            self.velocity = self.move_towards(target.coord)
        else:
            self.velocity += self.wander()

        if self.child:
            self.line_timer -= 1

        if self.line_timer <= 0:
            self.child = None
            self.line_timer = LINE_TIMER

        self.coord += self.velocity * self.speed
        self.coord = screen_wrap(self.coord, world.w, world.h)

        self.eat(world)
        self.reproduce(world)

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

    def reproduce(self, world):
        if self.energy > 200 and random.random() < 0.02:
            self.energy /= 2
            self.spawn_child(world)

    def spawn_child(self, world):
        child = Creature(world.w, world.h)

        child.speed = max(0.1, self.speed + random.uniform(-0.2, 0.2))
        child.vision = max(10, self.vision + random.uniform(-10, 10))

        child.coord = Vector2(self.coord.x, self.coord.y)
        child.color = self.mutate_color()
        self.child = child
        world.creatures.append(child)

    def mutate_color(self, mutation_strength: int = 15):
        r, g, b = self.color

        def clamp(x):
            return max(0, min(255, x))

        return (
            clamp(r + random.randint(-mutation_strength, mutation_strength)),
            clamp(g + random.randint(-mutation_strength, mutation_strength)),
            clamp(b + random.randint(-mutation_strength, mutation_strength)),
        )
