from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    
    def __init__(self, image_list):
        self.type = random.randint(0, 2)
        super().__init__(image_list) #hace referencia a la clase padre, pero por algun motivo si lo coloco arriba de self.type sale error (averiguar)
        self.rect.y = 360 - self.rect.height  
