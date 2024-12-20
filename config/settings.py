"""
Module that includes game settings
"""


class Settings:
    """Game's setting representation"""

    def __init__(self):
        """Instantiation of games setting"""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = (self.screen_width, self.screen_height)
        self.bg_color = (0, 0, 0)
        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (180, 0, 0)
        self.bullets_allowed = 4
        # Alien settings
        self.aliens_drop_speed = 10
        # Ship settings
        self.ship_limit = 3
        self.speed_factor = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.aliens_direction = 1  # 1 right, -1 left
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_factor
        self.bullet_speed *= self.speed_factor
        self.alien_speed *= self.speed_factor
        self.alien_points = int(self.alien_points * self.score_scale)
