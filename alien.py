"""
Module representing Alien
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game_settings):
        super().__init__()
        self.settings = game_settings.settings
        self.window = game_settings.window
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Updates position of alien"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
