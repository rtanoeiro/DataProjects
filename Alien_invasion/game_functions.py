from sys import exit
import pygame
from bullet import Bullet

def check_events(game_settings, screen, ship, bullets):
    """This function will check for the events that happen on the keyboard or mouse"""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """This function will check for when a key is pressed"""
       
    ## Recording when a key is pressed
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship up
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the ship down
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet) 
        
def check_keyup_events(event, ship):
    """This function will check for when a key is released"""
    # Recording when a key is released
    if event.key == pygame.K_RIGHT:
        # Stop moving the ship the  right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # Stop moving the ship the left
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # Stop moving the ship up
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        # Stop moving the ship down
        ship.moving_down = False

def update_screen(game_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen
    screen.fill(game_settings.bg_color)

    # Redraw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() ## Redraws the ship, on it's new position

    # Make the most recently draw screen visible
    pygame.display.flip()