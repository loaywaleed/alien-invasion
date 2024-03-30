#!/usr/bin/env python3
import pygame
import os
from ship import Ship
from bullet import Bullet


class GameSettings:
    """Managing game assets and behaviour"""
    FPS = 60

    def __init__(self):
        """Instantiation of the game assets and behaviour"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (0, 0, 0)
        self.ship = Ship(self)
        # Bullet Shape
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (180, 180, 180)

        # Storing bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(self.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.ship.rect.left > 0:
                self.ship.rect.centerx -= 10
        if keys[pygame.K_RIGHT]:
            if self.ship.rect.right < self.ship.screen_rect.right:
                self.ship.rect.centerx += 10
        if keys[pygame.K_SPACE]:
            self._fire_bullet()
        if keys[pygame.K_q]:
            os._exit(0)

    def _fire_bullet(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _update_screen(self):
        self.window.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    alien_invasion = GameSettings()
    alien_invasion.run_game()
