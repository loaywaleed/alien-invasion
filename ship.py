import pygame


class Ship:
    def __init__(self, game_settings):
        self.window = game_settings.window
        self.screen_rect = game_settings.window.get_rect()

        # loading ship image
        self.image = pygame.image.load("imgs/falcon.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.window.blit(self.image, self.rect)
