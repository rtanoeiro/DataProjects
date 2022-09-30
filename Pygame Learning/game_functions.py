import pygame

def check_events(player, snail):
    """This function will check for the events that happen on the keyboard or mouse"""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player=player)

        if player.rect.colliderect(snail.rect):
            pygame.quit()
            exit()           

def check_keydown_events(event,player):
    """This function will check for when a key is pressed"""
       
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player.yspeed=-20

def update_screen(player, environment, enemies):
    """Update images on the screen and flip to the new screen."""

    environment.blitme()
    player.blitme() ## Redraws the ship, on it's new position\
    enemies.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()
