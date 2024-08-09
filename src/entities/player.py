from src.planets.planet import Planet
from src.entities.entity import Entity
class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.planets[Planet] = []
        self.generate_player_first_planet()
        self.active_fleet = []
        self.max_fleet = 2
        
    # Planet methods
    def generate_player_first_planet(self) -> None:
        planet = Planet(owner=self.name, name="Fist Planet")
        self.add_planet(planet)

    def add_planet(self, planet: Planet) -> None:
        self.planets.append(planet)

    def get_planets(self) -> list:
        return self.planets

    #  Fleet methods
    def get_active_fleet(self) -> list:
        return self.active_fleet
    
    def get_max_fleet(self) -> int:
        return self.max_fleet
    
    def get_available_fleet(self) -> bool:
        return len(self.active_fleet) < self.max_fleet
    
    def add_fleet(self, fleet) -> None:
        if self.get_available_fleet():
            self.active_fleet.append(fleet)
        else:
            print("Max fleet reached")
    
    def remove_fleet(self, fleet) -> None:
        self.active_fleet.remove(fleet)

    def merge_fleet(self, fleet1 : list, fleet2 : list) -> None:
        fleet1.add_to_fleet(fleet2)
        self.active_fleet.remove(fleet2)