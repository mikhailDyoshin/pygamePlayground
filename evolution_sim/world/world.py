from agents.creature import Creature
from world.food import Food

FOOD_NUMBER = 10
CREATURES_NUMBER = 10


class World:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.creatures: list[Creature] = []
        self.food: list[Food] = []

        for _ in range(CREATURES_NUMBER):
            self.creatures.append(Creature(w, h))

        for _ in range(FOOD_NUMBER):
            self.food.append(Food(w, h))

    def update(self):
        # food update (static for now)
        for c in self.creatures:
            c.update(self)

        # cleanup dead creatures
        self.creatures = [c for c in self.creatures if not c.dead]

        # slowly respawn food
        if len(self.food) < FOOD_NUMBER:
            self.food.append(Food(self.w, self.h))
