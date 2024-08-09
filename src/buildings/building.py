from abc import ABC, abstractmethod
class Building(ABC):
    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = level
        self.building_type = self._generate_building_type()

    def upgrade(self) -> None:
        # Default upgrade logic for all buildings
        self.level += 1

    @abstractmethod
    def calculate_upgrade_cost(self) -> dict:
        # Calculate upgrade cost
        raise NotImplementedError("Subclasses must implement calculate_upgrade_cost")

    def _generate_building_type(self):
        # Generate building type from class name
        return self.__class__.__name__.lower()

    def get_type(self):
        # Get building type
        return self.building_type
    
    @abstractmethod
    def get_static_type():
        # Get building type
        return __class__.__name__.lower()
    
    def get_name(self):
        # Get building  name
        return self.name
    
    def get_level(self):
        # Get building level
        return self.level

    def __str__(self) -> str:
        return f"{self.name} (Level {self.level})"
