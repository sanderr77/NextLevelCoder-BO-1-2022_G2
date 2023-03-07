from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

import random

class Bird(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list, 0)
        self.rect.y = random.randint(100, 250)
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        if self.rect.x < -self.rect.width:
            obstacles.pop()

