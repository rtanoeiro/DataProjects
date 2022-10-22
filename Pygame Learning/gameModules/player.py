import pygame
import os
from gameModules.environment import Environment
from gameModules.settings import GameSettings

gs = GameSettings()
pygame.font.init()

class Player():
    """This class represents the player"""

    def __init__(self) -> None:
        # Getting environment
        self.environment = Environment()
        self.current_path = os.getcwd()

        # Getting screen to place player on it
        self.screen = gs.screen
        self.screen_rect = self.screen.get_rect()
        # Setting speed of player
        self.xspeed = gs.player_xspeed
        self.yspeed = gs.player_yspeed

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

        # Setting player surface and rectangle
        self.player_surface = pygame.image.load(self.current_path + "/art/graphics/Player/player_walk_1.png").convert_alpha()
        self.player_rect = self.player_surface.get_rect() # Rectangles
        
        self.font = pygame.font.Font(self.current_path + "/art/font/Pixeltype.ttf", 50)

        # Setting player stand surface and rectangle
        self.player_stand_surface = pygame.image.load(self.current_path + "/art/graphics/Player/player_stand.png").convert_alpha()
        self.player_stand_rect = self.player_stand_surface.get_rect() # Rectangles
        self.player_stand_surface_scaled = pygame.transform.scale2x(self.player_stand_surface)

        # Saving initial values
        self.initial_x = self.environment.sky_rect.left + self.player_surface.get_width()
        self.initial_y = self.environment.sky_surface.get_height()

        # Setting initial position of player
        self.player_rect.centerx =  self.initial_x
        self.player_rect.bottom = self.initial_y

        self.score = 0
        self.high_score = 0
        self.score_text = "Score: " + str(self.score)
        self.score_surface = self.font.render(self.score_text, False, 'Red')
        self.score_rect = self.score_surface.get_rect()

        self.high_score_text = "Higher Score: " + str(self.high_score) 
        self.high_score_surface = self.font.render(self.high_score_text, False, 'Red')
        self.high_score_rect = self.high_score_surface.get_rect()

    def update(self):
        
        # This is going to imitate gravity
        self.yspeed += 1
        self.player_rect.centery += self.yspeed
        
        # This will act like a floor
        if self.player_rect.bottom >= self.initial_y:
            self.player_rect.bottom = self.initial_y

        if self.moving_right:
            self.player_rect.centerx += self.xspeed

        if self.moving_left:
            self.player_rect.centerx -= self.xspeed

    def blitme(self):
        
        self.screen.blit(self.player_surface, self.player_rect)
        self.screen.blit(self.score_surface, (550,5))
        self.screen.blit(self.high_score_surface, (100, 5))