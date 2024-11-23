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
        self.high_score = 0
        self.load_high_score()

    def reset_stats(self):
        """Resets game stats to initial values"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Loading the high score from a file"""
        try:
            with open('high_score.txt', 'r') as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
            self.save_high_score()

    def save_high_score(self):
        """Saving the high score to a file"""
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))
