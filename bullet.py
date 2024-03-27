import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game_settings):
        super.__init__()

        self.screen = game_settings.screen
        self.settings = game_settings.settings
        self.color = game_settings.color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = game_settings.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.game_settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
