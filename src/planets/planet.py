from src.buildings.mine import MetalMine,CrystalField,DeuteriumSynthesizer
from src.resources.resource import Resource
from src.buildings.building import Building

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

    def calculate_base_production(self, tick: int) -> tuple:
        # Calculate base resource production without building time
        metal_base_rate = int(self.METAL_BASE_PRODUCTION_RATE * tick)
        crystal_base_rate = int(self.CRYSTAL_BASE_PRODUCTION_RATE * tick)
        deuterium_base_rate = int(self.DEUTERIUM_BASE_PRODUCTION_RATE * tick)

        return metal_base_rate, crystal_base_rate, deuterium_base_rate

    def calculate_building_production(self, tick: int) -> tuple:
        # Initialize variables with default values
        metal_building_rate = 0
        crystal_building_rate = 0
        deuterium_building_rate = 0

        # Calculate resource production based on buildings and time
        for building_type in self.buildings:

            if building_type == MetalMine.get_static_type():
                metal_building_rate = int( self.buildings[building_type].get_production() * tick)
            elif building_type == CrystalField.get_static_type():
                crystal_building_rate = int( self.buildings[building_type].get_production() * tick)
            elif building_type == DeuteriumSynthesizer.get_static_type():
                deuterium_building_rate = int( self.buildings[building_type].get_production() * tick)

        return (
            metal_building_rate,
            crystal_building_rate,
            deuterium_building_rate
        )
    
    def produce_resources(self, tick: int = 1):
        # Calculate base production rates
        base_metal, base_crystal, base_deuterium = self.calculate_base_production(tick)

        # Calculate building-based production rates
        building_metal, building_crystal, building_deuterium = self.calculate_building_production(tick)

        # Add the produced resources to the planet
        self.resources.metal = self.resources.metal + (base_metal + building_metal)
        self.resources.crystal = self.resources.crystal + (base_crystal + building_crystal)
        self.resources.deuterium = self.resources.deuterium + (base_deuterium + building_deuterium)

    # Getters and setters
    def get_resources(self) -> Resource:
        return self.resources
    
    def get_owner(self) -> str:
        return self.owner
    
    def get_name(self) -> str:
        return self.name
    
    def get_buildings(self) -> dict:
        return self.buildings

    # Printable representation
    def __str__(self) -> str:
        return f"{self.name} (Owner: {self.owner}) - {str(self.resources)}"
