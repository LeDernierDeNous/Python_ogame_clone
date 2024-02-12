from src.buildings.mine import MetalMine,CrystalField,DeuteriumSynthesizer
from src.resources.resource import Resource
from src.buildings.building import Building

from typing import NamedTuple

class ProductionRates(NamedTuple):
    metal: int
    crystal: int
    deuterium: int

class Planet:
    METAL_BASE_PRODUCTION_RATE = 10
    CRYSTAL_BASE_PRODUCTION_RATE = 5
    DEUTERIUM_BASE_PRODUCTION_RATE = 2

    starting_amount_resources = Resource(metal=100, crystal=50, deuterium=20)

    def __init__(self, owner: str, name: str):
        self.owner = owner
        self.name = name
        self.resources = self.starting_amount_resources
        self.buildings = {}

    def add_building(self, building: Building):
        # Check if a building of the same type already exists
        building_type = building.get_type()
        if building_type in self.buildings.keys():
            print(f"A {building_type.capitalize()} building already exists on this planet.")
        else:
            # Add the building to the planet
            self.buildings[building_type] = building

    def calculate_base_production(self, tick: int) -> ProductionRates:
        # Calculate base resource production without building time
        metal_production = self.METAL_BASE_PRODUCTION_RATE * tick
        crystal_production = self.CRYSTAL_BASE_PRODUCTION_RATE * tick
        deuterium_production = self.DEUTERIUM_BASE_PRODUCTION_RATE * tick

        return ProductionRates(
            metal=metal_production,
            crystal=crystal_production, 
            deuterium=deuterium_production
        )

    def calculate_building_production(self, tick: int) -> ProductionRates:
        # Calculate resource production based on buildings and time
        for building in self.buildings:
            if isinstance(building, MetalMine) :
                metal_building_rate = building.get_production()
            elif isinstance(building, CrystalField):
                crystal_building_rate = building.get_production()
            elif isinstance(building, DeuteriumSynthesizer):
                deuterium_building_rate = building.get_production()

        return ProductionRates(
            metal=int(metal_building_rate * tick),
            crystal=int(crystal_building_rate * tick),
            deuterium=int(deuterium_building_rate * tick)
        )
    
    def produce_resources(self, tick: int = 1):
        # Calculate base production rates
        base_metal, base_crystal, base_deuterium = self.calculate_base_production(tick)

        # Calculate building-based production rates
        building_metal, building_crystal, building_deuterium = self.calculate_building_production(tick)

        # Add the produced resources to the planet
        self.resources.metal += base_metal + building_metal
        self.resources.crystal += base_crystal + building_crystal
        self.resources.deuterium += base_deuterium + building_deuterium

    def __str__(self) -> str:
        return f"{self.name} (Owner: {self.owner}) - {str(self.resources)}"
