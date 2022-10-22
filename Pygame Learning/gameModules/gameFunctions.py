import pygame
from gameModules.player import Player
from gameModules.enemies import Snail, Fly
from gameModules.environment import Environment
from gameModules.settings import GameSettings
import os

gs = GameSettings()
snail = Snail()
player = Player()
environment = Environment()

class GameFunctions():

    def __init__(self) -> None:
        self.game_state = True
        self.current_path = os.getcwd()
        self.test_font150 = pygame.font.Font(self.current_path + "/art/font/Pixeltype.ttf", 150)
        self.test_font75 = pygame.font.Font(self.current_path + "/art/font/Pixeltype.ttf", 75)

        self.game_over_text_surface = self.test_font150.render('Game Over!', False, 'White')
        self.game_over_text_rect = self.game_over_text_surface.get_rect()

        self.continue_surface = self.test_font75.render('Press Enter to Continue Playing!', False, 'White')
        self.continue_surface_rect = self.continue_surface.get_rect()

        self.game_over_screen_surface = gs.screen
        self.game_over_screen_rect = gs.screen.get_rect()


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
        
        if snail.snail_rect.colliderect(player.player_rect):
            gs.game_state=False
            print("Game Over!")
            self.game_over()

        # Moving snail back to right of the screen and updating player score
        if snail.snail_rect.right < 0:
            snail.snail_rect.x = snail.initial_position
            player.score += 1
            print("Current Score: ", player.score)
            player.text = "Score: " + str(player.score)
            player.score_surface = player.score_font.render(player.text, False, 'Red')
            player.score_rect = player.score_surface.get_rect()
            
    # def check_keydown_events(self, event):
    #     """This function will check for when a key is pressed"""
    # 
    #     if event.key == pygame.K_SPACE and player.player_rect.bottom==300:
    #         player.moving_up = True
    # ## Recording when a key is pressed
    #     elif event.key == pygame.K_RIGHT:
    #         # Move the ship to the right
    #         player.moving_right = True
    #     elif event.key == pygame.K_LEFT:
    #         # Move the ship to the left
    #         player.moving_left = True
# 
    #         if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 exit()
    #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #             self.game_state = True
    #             snail.snail_rect.right = -1
    #             print(event)
    #             #sleep(2)
# 
    #     gs.clock.tick(60)
    #     pygame.display.update()

    def game_over(self):
        
        gs.clock.tick(60)
        # Update Player Score
        player.score = 0
        print("Game Over Score: ", player.score)
        player.text = "Score: " + str(player.score)
        player.score_surface = player.score_font.render(player.text, False, 'Red')
        player.score_rect = player.score_surface.get_rect()

        self.game_over_screen_surface.fill('Black')
        gs.screen.blit(self.game_over_screen_surface, (0,0))
        gs.screen.blit(self.game_over_text_surface, (150,150))
        gs.screen.blit(self.continue_surface, (50,250))

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game_state = True
                snail.snail_rect.right = gs.screen.get_width() + 50

        pygame.display.update()

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        
        gs.clock.tick(60)
        player.update()
        snail.update()
        
        environment.blitme()
        player.blitme() # Redraws the ship, on it's new position
        snail.blitme()
        
        # Make the most recently draw screen visible
        pygame.display.flip()