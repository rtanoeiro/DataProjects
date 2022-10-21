import pygame
import os
from gameModules.environment import Environment
from gameModules.settings import GameSettings

gs = GameSettings()

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

        # Setting player surface and rectangle
        self.player_surface = pygame.image.load(self.current_path + "/art/graphics/Player/player_walk_1.png").convert_alpha()
        self.player_rect = self.player_surface.get_rect() # Rectangles

        # Saving initial values
        self.initial_x = self.environment.sky_rect.left + self.player_surface.get_width()
        self.initial_y = self.environment.sky_surface.get_height()

        # Setting initial position of player
        self.player_rect.centerx =  self.initial_x
        self.player_rect.bottom = self.initial_y

    def update(self):
        
        # This is going to imitate gravi ty
        self.yspeed += 1
        self.player_rect.y += self.yspeed

        if self.player_rect.bottom >= self.initial_y: # This will act like a floor
            self.player_rect.bottom = self.initial_y
            
    def blitme(self):
        
        self.screen.blit(self.player_surface, self.player_rect)
