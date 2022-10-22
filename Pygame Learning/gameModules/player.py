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

        # Saving initial values
        self.initial_x = self.environment.sky_rect.left + self.player_surface.get_width()
        self.initial_y = self.environment.sky_surface.get_height()

        # Setting initial position of player
        self.player_rect.centerx =  self.initial_x
        self.player_rect.bottom = self.initial_y

        self.score = 0
        self.score_font = pygame.font.Font(self.current_path + "/art/font/Pixeltype.ttf", 50)
        self.text = "Score: " + str(self.score)
        self.score_surface = self.score_font.render(self.text, False, 'Red')
        self.score_rect = self.score_surface.get_rect()

    def update(self):
        
        # This is going to imitate gravity
        self.yspeed += 1
        self.player_rect.y += self.yspeed

        if self.player_rect.bottom >= self.initial_y: # This will act like a floor
            self.player_rect.bottom = self.initial_y

        elif self.moving_right:
            self.player_rect.centerx += 1

        elif self.moving_left:
            self.player_rect.x -= 1
        
        elif self.moving_up and self.player_rect.bottom == Environment().sky_rect.top:
            self.player_rect.centery -= 20

    def blitme(self):
        
        self.screen.blit(self.player_surface, self.player_rect)
        self.screen.blit(self.score_surface, (self.screen.get_rect().midtop))