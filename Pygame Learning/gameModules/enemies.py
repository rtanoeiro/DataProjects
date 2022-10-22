import pygame
import os
from gameModules.environment import Environment
from gameModules.settings import GameSettings

gs = GameSettings()

class Snail():
    """This class represents the snail in the screen"""

    def __init__(self) -> None:
        ## Getting environment
        self.environment = Environment()
        self.current_path = os.getcwd()

        ## Getting screen to place player on it
        self.screen = gs.screen
        self.screen_rect = self.screen.get_rect()

        ## Setting speed of player
        self.speed = gs.snail_xspeed

        ## Setting snail surface and rectangle
        self.snail_surface = pygame.image.load(self.current_path + "/art/graphics/snail/snail1.png").convert_alpha() # Surface
        self.snail_rect = self.snail_surface.get_rect() # Rectangle

        ## Setting initial position of snail
        self.snail_rect.centerx =  self.environment.sky_rect.right
        self.snail_rect.centery = self.environment.sky_rect.bottom - self.snail_surface.get_height()/2 ## Self.rect.bottom/2 will adjust the image up just a bit, so it's entirely in the screen

        self.initial_position = self.snail_rect.centerx

    def update(self):
        
        self.snail_rect.x -= self.speed

    def blitme(self):
        
        # Blit is used to put one surface into another surface
        self.screen.blit(self.snail_surface,self.snail_rect)

class Fly():
    """This class represents the fly in the screen"""

    def __init__(self, speed) -> None:
        self.speed = speed
        self.current_path = os.getcwd()
        self.surface = pygame.image.load(self.current_path + "/art/graphics/Fly/fly1.png").convert_alpha() # Surface
        self.rect = self.surface.get_rect() # Rectangle