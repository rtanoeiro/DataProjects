import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

# Variable to set frame rate
clock = pygame.time.Clock()

def run_game():
    # Initialize game and create screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(game_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        clock.tick(60) 
        gf.check_events(game_settings=game_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()
        bullets.update()
        gf.update_screen(game_settings=game_settings, screen=screen, ship=ship, bullets=bullets)

run_game()