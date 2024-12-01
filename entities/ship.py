"""
Module that has ship representation
"""
import pygame
from pygame.sprite import Sprite
from utils import resource_path


class Ship(Sprite):
    """Space ship representation"""

    def __init__(self, game_settings):
        """Instantiation of the ship"""
        super().__init__()
        self.window = game_settings.window
        self.screen_rect = game_settings.window.get_rect()
        # Loading ship image dynamically
        self.image = pygame.image.load(resource_path("imgs/falcon.bmp"))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Drawing the ship"""
        self.window.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)