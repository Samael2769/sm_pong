##
## EPITECH PROJECT, 2021
## Untitled (Workspace)
## File description:
## settings
##

import pygame

class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1600, 900
        pygame.mouse.set_visible(False)
        self.bg_color = pygame.image.load("./assets/game_background.png")
        self.bg_color = pygame.transform.scale(self.bg_color, (1600, 900))
