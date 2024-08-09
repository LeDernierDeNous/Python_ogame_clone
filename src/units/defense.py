from abc import ABC, abstractmethod
from units.unit import Unit

class Defense(Unit, ABC):
    def __init__(self, planet):
        self.planet = planet

    def get_production_time(self) -> int:
        # To-do: Update with formula
        # (metal_cost + crystal_cost) / ((2500 *(1 + shipyard_level))* 2 ^ (nanite_level))
        return (self.get_cost().metal + self.get_cost().deuterium) / ((2500 *(1 + self.planet.shipyard_level))* 2 ^ (self.planet.nanite_level))