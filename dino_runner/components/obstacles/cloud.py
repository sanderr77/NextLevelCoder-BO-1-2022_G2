import pygame
import random
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH)
        self.rect.y = random.randint(0, 150)

    def update(self, game_speed):
        self.rect.x -= game_speed // 2
        if self.rect.x <= -self.rect.width:
            self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH)
            self.rect.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, self.rect)