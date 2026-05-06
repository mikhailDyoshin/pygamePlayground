import random

from pygame import Vector2


class Food:
    def __init__(self, w, h):
        FOOD_ZONES = [
            (w * 0.25, h * 0.5, 10, 10),
            (w * 0.75, h * 0.5, 60, 10),
        ]
        zone = random.choice(FOOD_ZONES)
        x, y, density, nutrition = zone
        self.coord = Vector2(random.gauss(x, density), random.gauss(y, density))
        self.energy = nutrition
