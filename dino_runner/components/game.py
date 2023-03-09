import pygame
import pygame.mixer
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text_utils import TextUtils
from dino_runner.utils.constants import BG, COLORS, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, MUSIC
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_ups_manager import PowerUpManager
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.text_utils = TextUtils()
        self.game_running = True
        self.powerup_manager = PowerUpManager()
        self.max_score = 0
        self.attempts = 0


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        pygame.init()
        pygame.mixer.init()

        
        pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.play()

        while self.playing:
            self.events()
            self.update()
            self.draw()
            
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    def update(self):
        
                    
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLORS["white"])
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)


        self.screen.blit(self.text_utils.get_score(self.points), (10, 10))
        
        max_score_text, max_score_rect = self.text_utils.get_score(self.max_score)
        self.screen.blit(max_score_text, max_score_rect)
        attempts_text, attempts_rect = self.text_utils.get_attempts(self.attempts)
        self.screen.blit(attempts_text, attempts_rect)

        max_score_text, max_score_rect = self.text_utils.get_max_score(self.max_score)
        self.screen.blit(max_score_text, max_score_rect)

        attempts_text, attempts_rect = self.text_utils.get_attempts(self.attempts)
        self.screen.blit(attempts_text, attempts_rect)


        pygame.display.update()
        pygame.display.flip()
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        text, text_rect = self.text_utils.get_score(self.points)
        self.player.check_invincibility()
        self.screen.blit(text, text_rect)

    def show_menu(self, death_count = 0):
        self.game_running = True
        self.screen.fill(COLORS["white"])

        self.print_menu_elements(death_count)

        pygame.display.update()
        self.handle_key_events()

    def print_menu_elements(self, death_count=0):
        text, text_rext = self.text_utils.get_centered_message("Press any key to Start")
        self.screen.blit(text, text_rext)
        if death_count > 0:
            score, score_rect = self.text_utils.get_centered_message(
                "Your Score: " + str(self.points),
                height= SCREEN_HEIGHT//2 + 50)
            self.screen.blit(score, score_rect)
        self.screen.blit(RUNNING[0], (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 -140))

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()
    
    def update_max_score(self):
        if self.points > self.max_score:
            self.max_score = self.points

    def update_attempts(self):
        self.attempts += 1





   
    
