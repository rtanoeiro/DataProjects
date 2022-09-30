import pygame

class Environment():
    """This class represents the player"""

    def __init__(self, screen) -> None:        
        # Creating font for score
        self.screen = screen
        self.test_font = pygame.font.Font("Pygame Learning/font/Pixeltype.ttf", 50)

        self.score = 0
        self.score_surface = self.test_font.render('Score ', False, 'Red')
        self.score_rect = self.score_surface.get_rect()

        # Creating surfaces (Sky and ground) and setting colors (There could be many surfaces of this instance)
        self.sky_surface = pygame.image.load("Pygame Learning/graphics/sky.png").convert_alpha()
        self.sky_rect = self.sky_surface.get_rect()

        self.ground_surface = pygame.image.load("Pygame Learning/graphics/ground.png").convert_alpha()
        self.ground_rect = self.ground_surface.get_rect()

    def blitme(self):

        # Blit is used to put one surface into another surface
        self.screen.blit(self.sky_surface, (0,0))
        self.screen.blit(self.ground_surface, (0,  self.sky_rect.bottom))