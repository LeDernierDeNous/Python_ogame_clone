from planets.planet import Planet
from src.entities.entity import Entity
class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.planets = []
        self.generate_player_first_planet()
        
    def generate_player_first_planet(self) -> None:
        planet = Planet(owner=self.name, name="Fist Planet")
        self.add_planet(planet)

    def add_planet(self, planet: Planet) -> None:
        self.planets.append(planet)