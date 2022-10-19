import pygame
import os
from gameModules.settings import GameSettings

gs = GameSettings()
pygame.init()

class Environment():
    """This class represents the Display Surface"""

    def __init__(self):        
        # Creating font for score
        self.current_path = os.getcwd()
        self.screen = gs.screen
        self.test_font = pygame.font.Font(self.current_path + "/art/font/Pixeltype.ttf", 50)

        self.score = 0
        self.score_surface = self.test_font.render('Score: ', False, 'Red')
        self.score_rect = self.score_surface.get_rect()

        # Creating surfaces (Sky and ground) and setting colors (There could be many surfaces of this instance)
        self.sky_surface = pygame.image.load(self.current_path + "/art/graphics/sky.png").convert_alpha()
        self.sky_rect = self.sky_surface.get_rect()

        self.ground_surface = pygame.image.load(self.current_path + "/art/graphics/ground.png").convert_alpha()
        self.ground_rect = self.ground_surface.get_rect()

    def blitme(self):

        # Blit is used to put one surface into another surface
        self.screen.blit(self.sky_surface, (0,0))
        self.screen.blit(self.ground_surface, (0,  self.sky_rect.bottom))