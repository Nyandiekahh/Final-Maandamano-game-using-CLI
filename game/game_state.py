# Game state
class GameState:
    def __init__(self):
        self.player = None
        self.score = 0
        self.current_location = "CBD"
        self.resources = {
            "personnel": 100,
            "equipment": 100,
            "public_support": 50,
            "morale": 75
        }
        self.events = []
