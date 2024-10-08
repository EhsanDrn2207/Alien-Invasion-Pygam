class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0