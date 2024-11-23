"""
Module that has bullet representation
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullet Representation"""

    def __init__(self, game_settings):
        """Instantiation of a new bullet"""
        super().__init__()
        self.window = game_settings.window
        self.settings = game_settings.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game_settings.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Updates the position of the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Creates rect object and draws it on the screen"""
        pygame.draw.rect(self.window, self.color, self.rect)
