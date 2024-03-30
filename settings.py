"""
Module that includes game settings
"""


class Settings:
    """Game's setting representation"""

    def __init__(self):
        """Instantiation of games setting"""
        # Screen settings.
        self.screen = (1200, 800)
        self.bg_color = (0, 0, 0)
        # Bullet settings.
        self.bullet_width = 3
        self.bullet_speed = 1
        self.bullet_height = 17
        self.bullet_color = (180, 0, 0)
