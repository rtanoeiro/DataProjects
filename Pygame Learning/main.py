from sys import exit, modules
import pygame
import gameModules.gameFunctions as gf

pygame.init()

# Initialize screen and dimensions (This is the main surface, a display surface, there can be only one of it)

# Set name of the window
pygame.display.set_caption('Simple Platform Game')
clock = pygame.time.Clock()

# Main loop to run game
while True:

    ## Update check events and update screen to not receive arguments and to include player.update and snail.update        
    gf.check_events()
    gf.update_screen()

    clock.tick(60)