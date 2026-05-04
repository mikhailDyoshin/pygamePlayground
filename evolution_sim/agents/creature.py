import math
import random


class Creature:
    def __init__(self, w, h):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)

        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

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
            self.move_towards(target.x, target.y)
        else:
            self.wander()

        self.x += self.vx * self.speed
        self.y += self.vy * self.speed

        self.eat(world)

    def find_food(self, food_list):
        closest = None
        closest_dist = float("inf")

        for f in food_list:
            d = (self.x - f.x) ** 2 + (self.y - f.y) ** 2
            if d < self.vision**2 and d < closest_dist:
                closest = f
                closest_dist = d

        return closest

    def move_towards(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        dist = math.sqrt(dx * dx + dy * dy) + 0.0001

        self.vx = dx / dist
        self.vy = dy / dist

    def wander(self):
        self.vx += random.uniform(-0.2, 0.2)
        self.vy += random.uniform(-0.2, 0.2)

    def eat(self, world):
        for f in world.food:
            if abs(self.x - f.x) < 5 and abs(self.y - f.y) < 5:
                self.energy += f.energy
                world.food.remove(f)
                break
