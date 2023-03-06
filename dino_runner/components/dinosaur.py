import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(Sprite):
    POS_X = 80
    POS_Y= 310
    POS_Y_DUCKING = 350
    JUMP_VEL = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_running = True
        self.dino_ducking = False 
        self.dino_jumping = False
        self.jump_vel = self.JUMP_VEL


    def update(self, user_input):
        if self.dino_running:
            self.run()
        elif self.dino_ducking:
            self.duck()
        elif self.dino_jumping:
            self.jump()
         
        if user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.dino_running = False 
            self.dino_ducking = True
            self.dino_jumping = False
        elif user_input[pygame.K_UP] and not self.dino_jumping:
            self.dino_running = False 
            self.dino_ducking = False
            self.dino_jumping = True
        elif not self.dino_jumping:
            self.dino_running = True
            self.dino_ducking = False
            self.dino_jumping = False
        else:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1


    def jump(self):
        self.image = JUMPING
        if self.dino_jumping:
            self.dino_rect.y -= self.jump_vel * 4 #salto
            self.jump_vel -= 0.8 #Salto, cuando llega a negativo, baja
        if self.jump_vel < -self.JUMP_VEL: # Cuando llega a JUMP_VEL en negativo, este se detiene
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL 

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index += 1
