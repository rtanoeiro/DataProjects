import pygame
from pathlib import Path


class Ship():
    """Characteristics of the ship"""

    def __init__(self, game_settings, screen) -> None:
        """Initialize the ship and start it's position"""
        
        self.current_path = str(Path.cwd())
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.current_path+'/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx =  self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - self.rect.bottom/2  ## Self.rect.bottom/2 will adjust the image up just a bit, so it's entirely in the screen

        #Store a decimal value of the ship's center, as speed factor can be decimal
        self.centerx = float(self.rect.centerx)
        self.centery =  float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flag"""
        # Update the center value of the ship
        # If the right coordinate of the ship is greater than the right of the screen, we do not update the position of it
        if self.moving_right and self.rect.right < self.game_settings.screen_width:           
            self.centerx += self.game_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.game_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.game_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.game_settings.screen_height:
            self.centery += self.game_settings.ship_speed_factor
        
        # After value of the centers are update, store the new position of the ship (x,y) on the coordinates for update on screen
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at it's current location"""

        self.screen.blit(self.image, self.rect)