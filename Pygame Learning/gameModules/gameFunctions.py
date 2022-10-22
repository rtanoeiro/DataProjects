import pygame
from gameModules.player import Player
from gameModules.enemies import Snail, Fly
from gameModules.environment import Environment
from gameModules.settings import GameSettings
import os

gs = GameSettings()
snail = Snail()
player = Player()
environment = Environment()

class GameFunctions():

    def __init__(self) -> None:
        self.game_state = True
        self.current_path = os.getcwd()

    def check_events(self):

        """This function will check for the events that happen on the keyboard or mouse"""
        # Watch for keyboard and mouse events.      
        for event in pygame.event.get():
                       
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)          

    def check_keydown_events(self, event):
        """This function will check for when a key is pressed"""
    
        if event.key == pygame.K_SPACE and player.player_rect.bottom==300:
            player.moving_up = True
    ## Recording when a key is pressed
        elif event.key == pygame.K_RIGHT:
            # Move the ship to the right
            player.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            player.moving_left = True

    def check_keyup_events(self, event):
    
    ## Recording when a key is pressed
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            player.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            player.moving_left = True

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        gs.clock.tick(60)
        player.update()
        snail.update()
        
        environment.blitme()
        player.blitme()
        snail.blitme()
        
        # Make the most recently draw screen visible
        pygame.display.flip()