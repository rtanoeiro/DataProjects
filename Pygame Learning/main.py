from player import Player
from enemies import Snail, Fly
from environment import Environment
import game_functions as gf
import pygame
from sys import exit

pygame.init()

# Initialize screen and dimensions (This is the main surface, a display surface, there can be only one of it)
screen = pygame.display.set_mode((800, 400))

# Set name of the window
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

## Setting classes of the game
environment = Environment(screen=screen)
player = Player(environment=environment, screen=screen, xspeed=3, yspeed=0) 
snail = Snail(environment=environment, speed=2, screen=screen)
fly = Fly(speed=5)

# Main loop to run game
while True:

    gf.check_events(player=player, snail=snail)
    gf.update_screen(player=player, environment=environment, enemies=snail)
    player.update()
    snail.update()

    clock.tick(60)