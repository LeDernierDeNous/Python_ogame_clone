class Entity:
    def __init__(self, name):
        self.name = name
        self.planets = []

    def add_planet(self, planet):
        # Logic for adding a planet to the entity
        self.planets.append(planet)

    def __str__(self):
        return f"{self.name} - Planets: {len(self.planets)}"
