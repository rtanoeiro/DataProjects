from sys import exit
from Players.player import Player
from Enemies.enemies import Snail, Fly
from DisplaySurface.environment import Environment
import game_functions as gf
import pygame

pygame.init()

# Initialize screen and dimensions (This is the main surface, a display surface, there can be only one of it)
screen = pygame.display.set_mode((800, 400))

# Set name of the window
pygame.display.set_caption('Simple Platform Game')
clock = pygame.time.Clock()

## Setting classes of the game
environment = Environment(screen=screen)
player = Player(screen=screen, xspeed=3, yspeed=0) 
snail = Snail(screen=screen, speed=2)
fly = Fly(speed=5)

# Main loop to run game
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
    gf.check_events(player=player, snail=snail)
    gf.update_screen(player=player, environment=environment, enemies=snail)
    player.update()
    snail.update()

    clock.tick(60)