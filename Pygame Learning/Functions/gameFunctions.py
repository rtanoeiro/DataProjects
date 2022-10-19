import pygame
from Players.player import Player
from Enemies.enemies import Snail, Fly
from DisplaySurface.environment import Environment
from Functions.settings import GameSettings

gs = GameSettings()
snail = Snail()
player = Player()
environment = Environment()

def check_events():

    """This function will check for the events that happen on the keyboard or mouse"""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.yspeed=-20

        if player.rect.colliderect(snail):
            pygame.quit()
            exit()

def update_screen():
    """Update images on the screen and flip to the new screen."""

    environment.blitme()
    player.blitme() ## Redraws the ship, on it's new position\
    snail.blitme()

    player.update()
    snail.update()
    # Make the most recently draw screen visible
    pygame.display.flip()
