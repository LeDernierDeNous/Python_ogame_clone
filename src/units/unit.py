from abc import ABC, abstractmethod
from src.resources.resource import Resource

class Unit(ABC):
    def __init__(self):
        self.structural_integrity: int
        self.shield_power: int
        self.weapon_power: int
        self.rapid_fire = {}
        self.cost = {}
        self.production_time = int
        self.engine_type = None
        self.buildings_requirements = {}
        self.technologies_requirements = {}

        self.unit_type = self._generate_unit_type()

    # combat system

    def recieve_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Damage must be a positive integer.")
        if self.structural_integrity <= 0:
            raise ValueError("Unit is already destroyed.")
        if damage >= self.structural_integrity:
            # Unit is destroyed
            self.structural_integrity = 0
        else:
            # Reduce the structural integrity by the damage
            self.structural_integrity -= damage

    def is_destroyed(self) -> bool:
        return self.structural_integrity <= 0

    # Getters

    @abstractmethod
    def calculate_production_cost(self) -> dict:
        # Calculate upgrade cost
        raise NotImplementedError("Subclasses must implement calculate_production_cost")

    def get_structural_integrity(self) -> int:
        # To-do: Update with the structural integrity is equal to metal cost and crystal cost
        return self.structural_integrity
    
    def get_shield_power(self) -> int:
        # To-do: Update with research of shield technology
        return self.shield_power

    def get_weapon_power(self) -> int:
        # To-do: Update with research of weapon technology
        return self.weapon_power
    
    def get_production_time(self) -> int:
        # To-do: Update with Building of Shipyard
        return self.production_time
    
    def get_cost(self) -> Resource:
        return self.cost
    
    def _generate_unit_type(self):
        # Generate building type from class name
        return self.__class__.__name__.lower()

    def get_type(self):
        # Get building type
        return self.unit_type