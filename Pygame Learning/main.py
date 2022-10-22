import pygame
from gameModules.gameFunctions import GameFunctions

pygame.init()
gf = GameFunctions()

# Set name of the window
pygame.display.set_caption('Simple Platform Game')

# Main loop to run game
while True:

    if gf.game_state:
    ## Update check events and update screen to not receive arguments and to include player.update and snail.update        
        gf.check_events()
        gf.update_screen()
    else:
        gf.game_over() 