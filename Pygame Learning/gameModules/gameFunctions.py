import pygame
from gameModules.player import Player
from gameModules.enemies import Snail, Fly
from gameModules.environment import Environment
from gameModules.settings import GameSettings

gs = GameSettings()
snail = Snail()
player = Player()
environment = Environment()

class GameFunctions():

    def __init__(self) -> None:
        self.game_state = True

    def check_events(self):

        """This function will check for the events that happen on the keyboard or mouse"""
        # Watch for keyboard and mouse events.
        if snail.snail_rect.colliderect(player.player_rect):
                self.game_state=False
                print("Game Over!")
                self.game_over()
        
        for event in pygame.event.get():
                       
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.player_rect.bottom==300:
                    player.yspeed=-20


    def game_over(self):
        
        return gs.screen.fill('Yellow')
        #text = "Game Over"
        #environment.score_surface = environment.test_font.render(text, False, 'Red')
        #environment.test_font.render(text, False, 'Black')
        #environment.blitme()

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""

        environment.blitme()
        player.blitme() # Redraws the ship, on it's new position
        snail.blitme()

        player.update()
        snail.update()

        gs.clock.tick(60)
        # Make the most recently draw screen visible
        pygame.display.flip()
