"""
Module representing Alien
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class which represents and alien"""

    def __init__(self, game_settings):
        """Instantation of alien"""
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
        """Updates position of alien and makes it move to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    def check_edges(self):
        window_rect = self.screen.get_rect()
        if self.rect.right >= window_rect.right or self.rect.left <= 0:
            return True
