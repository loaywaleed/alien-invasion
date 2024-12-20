"""
Module representing Alien
"""

import pygame
from pygame.sprite import Sprite
from utils import resource_path


class Alien(Sprite):
    """Class which represents an alien"""

    def __init__(self, game_settings):
        """Instantiation of alien"""
        super().__init__()
        self.settings = game_settings.settings
        self.window = game_settings.window
        self.image = pygame.image.load(resource_path('imgs/alien.bmp'))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Updates position of the alien and makes it move to the right"""
        self.x += (self.settings.alien_speed * self.settings.aliens_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Checking screen edges"""
        window_rect = self.window.get_rect()
        if self.rect.right >= window_rect.right or self.rect.left <= 0:
            return True
