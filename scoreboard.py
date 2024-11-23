import pygame.font


class ScoreBoard:

    def __init__(self, game_settings) -> None:
        """Scoreboard initialization"""
        self.screen = game_settings.window
        self.screen_rect = self.screen.get_rect()
        self.settings = game_settings.settings
        self.stats = game_settings.stats

        # Font settings
        self.text_color = (255, 130, 130)
        self.font = pygame.font.SysFont(None, 60)

        # Preparation of the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Converting the score to a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Score display at the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displaying the score on the screen"""
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Converting the high score to a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def check_high_score(self):
        """Checking if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Converting the level to a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)

        # Level display below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
