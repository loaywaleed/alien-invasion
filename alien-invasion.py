#!/usr/bin/env python3
"""
Alien Invasion using pygame, drive the millenium falcon to destroy the alien
fleet
"""
import pygame
import os
from time import sleep
from ship import Ship
from bullet import Bullet
from settings import Settings
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


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
        self.stats = GameStats(self)
        self.scoreboard = ScoreBoard(self)
        self.ship = Ship(self)
        self.settings = Settings()
        self.play_button = Button(self, "Play")

        # Storing bullets
        self.bullets = pygame.sprite.Group()
        # Storing aliens
        self.aliens = pygame.sprite.Group()
        self._create_aliens()

    def run_game(self):
        """Runs main event loop of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(self.FPS)

    def _check_events(self):
        """Protected method to constantly check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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
        """
        Protected method to fire bullets as long as they are withing the limit
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_screen(self):
        """Updates the screen"""
        self.window.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.window)
        self.scoreboard.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _update_bullets(self):
        """Method to manage and add/remove bullets when needed"""
        self.bullets.update()
        # Removing bullets after they disappear
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_collisions()

    def _check_collisions(self):
        """Checks if a bullet hits an alien"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.scoreboard.prep_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_aliens()
            self.settings.increase_speed()

    def _create_aliens(self):
        """Protected method to create several aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Space available in x direction for aliens
        width_available_horizontal = self.settings.screen_width - \
            (2 * alien_width)
        aliens_horizontal_space = width_available_horizontal // (
            2 * alien_width)
        ship_height = self.ship.rect.height
        # Space available in y direction for aliens
        height_available_vertical = self.settings.screen_height - \
            (3 * alien_height) - ship_height
        aliens_vertical_space = height_available_vertical // (2 * alien_height)
        for row_number in range(aliens_vertical_space):
            for alien_number in range(aliens_horizontal_space):
                self._create_one_alien(alien_number, row_number)

    def _create_one_alien(self, alien_number, row_number):
        """Protected method that creates one alien ship"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_aliens_edge(self):
        """Checks if an alien has reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_aliens_direction()
                break

    def _update_aliens(self):
        """Updates the position of aliens"""
        self._check_aliens_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Millenium Falcon has been hit!")
            self._ship_is_hit()

        self._check_aliens_reach_bottom()

    def _change_aliens_direction(self):
        """Changes direction of aliens movement"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.aliens_drop_speed
        self.settings.aliens_direction *= -1  # Switch directions

    def _ship_is_hit(self):
        """Responds to the millenium falcon's collisions with an alien ship"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Reset the screen
            self.aliens.empty()
            self.aliens.empty()
            # Recreate aliens and ship (centered)
            self._create_aliens()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_reach_bottom(self):
        """Checks if aliens have reached the bottom of the screen"""
        screen_rect = self.window.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_is_hit()  # Resets the screen
                break

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._create_aliens()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
# todo: start game method and press P to play


if __name__ == '__main__':
    alien_invasion = GameSettings()
    alien_invasion.run_game()
