import pygame
import os
from DisplaySurface.environment import Environment
from Functions.settings import GameSettings

gs = GameSettings()

class Player():
    """This class represents the player"""

    def __init__(self) -> None:
        ## Getting environment
        self.environment = Environment()
        self.current_path = os.getcwd()

        ## Getting screen to place player on it
        self.screen = gs.screen
        self.screen_rect = self.screen.get_rect()
        ## Setting speed of player
        self.xspeed = gs.player_xspeed
        self.yspeed = gs.player_yspeed

        ## Setting player surface and rectangle
        self.player_surface = pygame.image.load(self.current_path + "/graphics/Player/player_walk_1.png").convert_alpha()
        self.rect = self.player_surface.get_rect() # Rectangles

        # Saving initial values
        self.initial_x = self.environment.sky_rect.left + self.player_surface.get_width()
        self.initial_y = self.environment.sky_surface.get_height()

        ## Setting initial position of player
        self.rect.centerx =  self.initial_x
        self.rect.bottom = self.initial_y

    def update(self):
        
        # This is going to imitate gravity
        self.yspeed += 1
        self.rect.y += self.yspeed

        if self.rect.bottom >= self.initial_y: # moving the player up
            self.rect.bottom = self.initial_y
            
    def blitme(self):
        
        self.screen.blit(self.player_surface, self.rect)