import pygame

class GameSettings():
    """
    This class will contain all settings of the game, such as speed, size
    """
    def __init__(self):

        self.player_xspeed = 3
        self.player_yspeed = 0
        self.snail_xspeed = 6
        self.fly_xspeed = 5
        self.screen_width = 800
        self.screen_height = 400
        self.screen = pygame.display.set_mode((800, 400))
        self.clock = pygame.time.Clock()
        self.game_state = True