import random

from pygame import Vector2


class Food:
    def __init__(self, w, h):
        self._x = random.randint(0, w)
        self._y = random.randint(0, h)
        self.coord = Vector2(self._x, self._y)
        self.energy = 20
