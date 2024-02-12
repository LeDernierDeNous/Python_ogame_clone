from src.entities.entity import Entity


class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        # Additional player-specific attributes and methods can be added here