import pygame
from Players.player import Player
from Enemies.enemies import Snail, Fly

class GameFunctions():

    def __init__(self) -> None:
        self.player = Player()
        self.snail = Snail()

    def check_events(self):

        """This function will check for the events that happen on the keyboard or mouse"""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            if self.player.rect.colliderect(self.snail.rect):
                pygame.quit()
                exit()           

    def check_keydown_events(self, event: pygame.event):
        """This function will check for when a key is pressed"""
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.yspeed=-20

    def update_screen(player, environment, enemies):
        """Update images on the screen and flip to the new screen."""

        environment.blitme()
        player.blitme() ## Redraws the ship, on it's new position\
        enemies.blitme()

        # Make the most recently draw screen visible
        pygame.display.flip()
