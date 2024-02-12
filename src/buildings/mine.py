from resources.resourcetype import ResourceType
from src.buildings.building import Building
from abc import ABC, abstractmethod

class Mine(Building, ABC):
    def __init__(self, resource_type: ResourceType):
        super().__init__(name=f"{resource_type.capitalize()} Mine")
        self.resource_type = resource_type

    @abstractmethod
    def get_production(self) -> int:
        pass

class MetalMine(Mine):
    PRODUCTION_FACTOR = 30

    def __init__(self):
        super().__init__(resource_type=ResourceType.METAL)

    def get_production(self) -> int:
        return int(self.PRODUCTION_FACTOR * self.level * (1.1 ** self.level))
    
    def calculate_upgrade_cost(self) -> dict:
        # Calculate upgrade cost based on the formula
        metal_cost = int(60 * 1.5 ** (self.level - 1))
        crystal_cost = int(15 * 1.5 ** (self.level - 1))
        return {ResourceType.METAL: metal_cost, ResourceType.CRYSTAL: crystal_cost}


class CrystalField(Mine):
    PRODUCTION_FACTOR = 20

    def __init__(self):
        super().__init__(resource_type=ResourceType.CRYSTAL)

    def get_production(self) -> int:
        return int(self.PRODUCTION_FACTOR * self.level * (1.1 ** self.level))
    
    def calculate_upgrade_cost(self) -> dict:
        # Calculate upgrade cost based on the formula
        metal_cost = int(48 * 1.6 ** (self.level - 1))
        crystal_cost = int(24 * 1.6 ** (self.level - 1))
        return {ResourceType.METAL: metal_cost, ResourceType.CRYSTAL: crystal_cost}

class DeuteriumSynthesizer(Mine):
    PRODUCTION_FACTOR = 10

    def __init__(self):
        super().__init__(resource_type=ResourceType.DEUTERIUM)

    def get_production(self) -> int:
        return int(self.PRODUCTION_FACTOR * self.level * (1.1 ** self.level))

    def calculate_upgrade_cost(self) -> dict:
        # Calculate upgrade cost based on the formula
        metal_cost = int(225 * 1.5 ** (self.level - 1))
        crystal_cost = int(75 * 1.5 ** (self.level - 1))
        return {ResourceType.METAL: metal_cost, ResourceType.CRYSTAL: crystal_cost}
