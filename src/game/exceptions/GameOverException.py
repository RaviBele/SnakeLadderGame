
class GameOverException(Exception):
    def __init__(self, message="No new players or Game is already over"):
        self.message = message
        super().__init__(self.message)