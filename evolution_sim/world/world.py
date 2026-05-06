from evolution_sim.agents.creature import Creature, SPEED_COST, VISION_COST
from evolution_sim.world.food import Food

FOOD_NUMBER = 20
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
        self.avg_speed_cost = 0
        self.avg_vision = 0
        self.avg_vision_cost = 0
        self.population = len(self.creatures)

    def update(self):
        # food update (static for now)
        for c in self.creatures:
            c.update(self)

        # cleanup dead creatures
        self.creatures = [c for c in self.creatures if not c.dead]
        self.population = len(self.creatures)

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
        self.avg_speed_cost = self.avg_speed * SPEED_COST
        self.avg_vision_cost = self.avg_vision * VISION_COST
