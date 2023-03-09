from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

import random

class Bird(Obstacle):

    def __init__(self, image_list):
        self.type = random.randint(0,1 )
        super().__init__(image_list, self.type)
        self.rect.y = 250

