from abc import ABC, abstractmethod
from units.unit import Unit

class Ship(Unit, ABC):
    def __init__(self):
        self.cargo_capacity: int
        self.base_speed: int
        self.fuel_consumption_base_cost: int

    def get_cargo_capacity(self) -> int:
        # To-do: Update with research of cargo technology
        return self.cargo_capacity

    def get_speed(self) -> int:
        # To-do: Update with research of differents motors technology
        return self.base_speed

    def get_fuel_consumption(self, distance: int) -> int:
        return 1 + round(((self.fuel_consumption_base_cost * distance)/35000)*((self.get_speed()/100)+1)**2)

    