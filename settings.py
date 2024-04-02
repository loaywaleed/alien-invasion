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
        # Bullet settings.
        self.bullet_width = 3
        self.bullet_speed = 1
        self.bullet_height = 17
        self.bullet_color = (180, 0, 0)
        self.bullets_allowed = 4
        # Alien settings
        self.alien_speed = 1.0
