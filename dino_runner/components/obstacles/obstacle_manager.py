from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random

CACTUS_LIST = [SMALL_CACTUS, LARGE_CACTUS]

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(random.choice(CACTUS_LIST)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    

#agregar el bird 
#Agregar los 2 cactus (probablemente utilizando random.choice donde importamos el cactus pequeño y el grande y simplemente lo colocamos dentro de un parentesis)
#SMALL_CACTUS, LARGE_CACTUS,...
