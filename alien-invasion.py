#!/usr/bin/env python3
import pygame
import os
from ship import Ship
from bullet import Bullet
from settings import Settings


class GameSettings:
    """Managing game assets and behaviour"""
    FPS = 60

    def __init__(self):
        """Instantiation of the game assets and behaviour"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.window = pygame.display.set_mode(self.screen)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Bullet Shape
        self.settings = Settings()

        # Storing bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.bullets.update()
            # Removing bullets after they disappear
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_screen()
            self.clock.tick(self.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.ship.rect.left > 0:
                self.ship.rect.centerx -= 10
        if keys[pygame.K_RIGHT]:
            if self.ship.rect.right < self.ship.screen_rect.right:
                self.ship.rect.centerx += 10
        if keys[pygame.K_q]:
            os._exit(0)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_screen(self):
        self.window.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    alien_invasion = GameSettings()
    alien_invasion.run_game()
