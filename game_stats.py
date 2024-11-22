"""
Game stats (numbers of ships left, etc) module
"""


class GameStats:
    """Responsible for tracking the game's stats"""

    def __init__(self, game_settings):
        """Initialization"""
        self.settings = game_settings.settings
        self.reset_stats()
        # Status settings
        self.game_active = False

    def reset_stats(self):
        """Resets game stats to initial values"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
