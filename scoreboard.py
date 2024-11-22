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
        self.screen.blit(self.score_image, self.score_rect)
