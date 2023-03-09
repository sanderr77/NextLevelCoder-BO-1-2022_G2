import pygame
import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, OBSTACLES, BULLET_IMG, BULLET_SOUND


class Projectile(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, game_speed):
        self.rect.x += game_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)



