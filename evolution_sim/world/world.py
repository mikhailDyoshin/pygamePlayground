from evolution_sim.agents.creature import Creature
from evolution_sim.world.food import Food

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

        self.avg_speed = 0
        self.avg_vision = 0
        self.population = len(self.creatures)

    def update(self):
        # food update (static for now)
        for c in self.creatures:
            c.update(self)

        # cleanup dead creatures
        self.creatures = [c for c in self.creatures if not c.dead]

        # slowly respawn food
        if len(self.food) < FOOD_NUMBER:
            self.food.append(Food(self.w, self.h))

        self.avg_speed = (
            sum(c.speed for c in self.creatures) / self.population
            if self.population != 0
            else 0
        )
        self.avg_vision = (
            sum(c.vision for c in self.creatures) / self.population
            if self.population != 0
            else 0
        )

        self.population = len(self.creatures)
