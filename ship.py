"""
Module that has ship representation
"""
import pygame


class Ship:
    """Space ship representation"""

    def __init__(self, game_settings):
        """Instantiation of the ship"""
        self.window = game_settings.window
        self.screen_rect = game_settings.window.get_rect()
        # loading ship image
        self.image = pygame.image.load("imgs/falcon.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Drawing the ship"""
        self.window.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)