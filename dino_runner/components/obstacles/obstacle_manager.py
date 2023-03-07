from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

import pygame
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.choice([True, False]):
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            
            if random.choice([True, False]):
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def check_collisions (self):
        for i, obstacle in enumerate(self.obstacles):
            for other_obstacle in self.obstacles[i+1:]:
                if obstacle.rect.colliderect(other_obstacle.rect):
                    if obstacle.rect.x <= other_obstacle.rect.x:
                        self.obstacles.remove(obstacle)
                    else:
                        self.obstacles.remove(other_obstacle)
                    break

    

#agregar el bird 
#Agregar los 2 cactus (probablemente utilizando random.choice donde importamos el cactus pequeño y el grande y simplemente lo colocamos dentro de un parentesis)
#SMALL_CACTUS, LARGE_CACTUS,...
