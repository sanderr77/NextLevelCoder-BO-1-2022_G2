import pygame
import random
from pygame.sprite import Sprite
from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import SCREEN_WIDTH, OOOMAGA
from dino_runner.utils.constants import GUN

class Gun(PowerUp):
    def __init__(self):
        super().__init__(GUN)
        self.projectiles = []
        self.last_shot_time = pygame.time.get_ticks()
        self.shot_cooldown = 500  

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > self.shot_cooldown:
            self.last_shot_time = now
            x = self.rect.x + self.rect.width
            y = self.rect.y + self.rect.height // 2
            