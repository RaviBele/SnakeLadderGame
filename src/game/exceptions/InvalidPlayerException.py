class InvalidPlayerException(Exception):
    def __init__(self, message="This player is invalid or already won the game"):
        self.message = message
        super().__init__(self.message)