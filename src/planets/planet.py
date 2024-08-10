import time  # Ensure the time module is imported
from src.resources.resourcetype import ResourceType
from src.buildings.mine import MetalMine,CrystalField,DeuteriumSynthesizer
from src.resources.resource import Resource
from src.buildings.building import Building
from src.units.unit import Unit

class Planet:
    METAL_BASE_PRODUCTION_RATE = 10
    CRYSTAL_BASE_PRODUCTION_RATE = 5
    DEUTERIUM_BASE_PRODUCTION_RATE = 2

    starting_amount_resources = Resource(metal=100, crystal=50, deuterium=20)

    universe_speed = 5

    def __init__(self, owner, name: str):
        self.owner = owner
        self.name = name
        self.resources = self.starting_amount_resources

        self.buildings = {}
        self.defenses = {}
        self.ships = {}

        self.research_prodlist = []
        self.unit_prodlist = []
        self.building_prodlist = []

    # Resources methods

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

    # Building methods

    def upgrade_building(self, building: Building) -> None:
        building_type = building.get_type()
        # Check if the player has enough resources to upgrade the building
        upgrade_cost = building.calculate_upgrade_cost()
        if self.resources.metal < upgrade_cost[ResourceType.METAL] or \
            self.resources.crystal < upgrade_cost[ResourceType.CRYSTAL] or \
            self.resources.deuterium < upgrade_cost[ResourceType.DEUTERIUM]:
            print("Insufficient resources to upgrade the building.")
            return
        else:
            # Deduct the resources from the player
            self.resources.metal -= upgrade_cost[ResourceType.METAL]
            self.resources.crystal -= upgrade_cost[ResourceType.CRYSTAL]
            self.resources.deuterium -= upgrade_cost[ResourceType.DEUTERIUM]
        if building_type not in self.buildings.keys():
            # First build the building
            print(f"Start building {building_type.capitalize()} on this planet.")
            self.buildings[building_type] = building
        else:
            # Upgrade the building
            print(f"Start Upgrading {building_type.capitalize()} from level {self.buildings[building_type].get_level()} to {self.buildings[building_type].get_level()+1} on this planet.")
            self.buildings[building_type].upgrade()
        self.add_building_to_prodlist(building, self.get_building_build_time(upgrade_cost))

    def add_building_to_prodlist(self, building: Building, duration) -> None:
        """Add a building to the production list with an end time.

        Args:
            building (Building): The building to add.
            duration (int): The duration in seconds until the building production is complete.
        """
        now = time.time()  # Current time in seconds since the epoch
        end_time = now + duration
        building_type = building.get_type()

        self.building_prodlist.append([building_type, end_time])

    def get_building_build_time(self, upgrade_cost) -> int:
        # Calculate the build time for the building (in hours)
        # metalcost = upgrade_cost[ResourceType.METAL]
        # crystalcost = upgrade_cost[ResourceType.CRYSTAL]
        # time_hours = (metalcost + crystalcost)/(2500*(1 + robotics_factory.get_level()) * self.get_universe_speed() * (2** nanite_factory.get_level()))    
        # return self.convert_hours_to_seconds(time_hours) 
        return 1

    # Units methods

    def produce_units(self, unit: Unit, quantity: int) -> None:
        # Produce units based on the production list
        # Check if the player has enough resources to produce the units
        unit_type = unit.get_type()
        production_cost = unit.calculate_total_production_cost(quantity)
        if self.resources.metal < production_cost[ResourceType.METAL] or \
            self.resources.crystal < production_cost[ResourceType.CRYSTAL] or \
            self.resources.deuterium < production_cost[ResourceType.DEUTERIUM]:
            print("Insufficient resources to produce the units.")
            return
        else:
            # Deduct the resources from the player
            self.resources.metal -= production_cost[ResourceType.METAL]
            self.resources.crystal -= production_cost[ResourceType.CRYSTAL]
            self.resources.deuterium -= production_cost[ResourceType.DEUTERIUM]

        print(f"Start producing {quantity} of {unit_type.capitalize()} on this planet.")
        self.ships[unit_type] = quantity
        self.add_unit_to_prodlist(unit, self.get_units_build_time(production_cost))

    def add_unit_to_prodlist(self, unit: Unit, quantity: int, duration) -> None:
        """
        Add a unit to the production list.

        Args:
            unit (Unit): The unit to be added.
            quantity (int): The quantity of the unit to be added.
            duration: The duration of the production.

        Returns:
            None
        """
        now = time.time()
        end_time = now + duration
        unit_type = unit.get_type()

        self.unit_prodlist.append([unit_type, quantity, end_time])

    def get_units_build_time(self, upgrade_cost) -> int:
        # Calculate the build time for the building (in hours)
        # metalcost = upgrade_cost[ResourceType.METAL]
        # crystalcost = upgrade_cost[ResourceType.CRYSTAL]
        # time_hours = (metalcost + crystalcost)/(2500*(1 + shipyard_level.get_level()) * self.get_universe_speed() * (2** nanite_factory.get_level()))    
        # return self.convert_hours_to_seconds(time_hours) 
        return 1
    
    # Research methods

    def get_research_build_time(self, upgrade_cost) -> int:
        # Calculate the build time for the building (in hours)
        # metalcost = upgrade_cost[ResourceType.METAL]
        # crystalcost = upgrade_cost[ResourceType.CRYSTAL]
        # time_hours = (metalcost + crystalcost)/(1000*(1 + research_level.get_level()) * self.get_universe_speed())  
        # return self.convert_hours_to_seconds(time_hours)  
        return 1 

    # Prodlists methods

    def update_prodlists(self):
        """
        Updates the production lists for buildings and units, and provides feedback when production finishes.
        """
        now = time.time()

        # Check which building productions are completed
        completed_buildings = [prod for prod in self.building_prodlist if prod[1] <= now]
        for building_type, _ in completed_buildings:
            building = self.buildings[building_type]
            print(f"Building production of '{building_type}' level {building.get_level()} completed on planet '{self.name}'.")


        # Update building production list to remove completed items
        self.building_prodlist = [prod for prod in self.building_prodlist if prod[1] > now]

        # Check which unit productions are completed
        completed_units = [prod for prod in self.unit_prodlist if prod[2] <= now]
        for unit_type, quantity, _ in completed_units:
            print(f"Production of {quantity} '{unit_type}' units completed on planet '{self.name}'.")

        # Update unit production list to remove completed items
        self.unit_prodlist = [prod for prod in self.unit_prodlist if prod[2] > now]


    # Getters and setters
    def get_resources(self) -> Resource:
        return self.resources
    
    def get_owner(self) -> str:
        return self.owner
    
    def get_name(self) -> str:
        return self.name
    
    def get_buildings(self) -> dict:
        return self.buildings

    def get_universe_speed(self) -> int:
        return self.universe_speed

    def convert_hours_to_seconds(self, hours: int) -> int:
        return hours * 60 * 60

    # Printable representation
    def __str__(self) -> str:
        return f"{self.name} (Owner: {self.owner}) - {str(self.resources)}"
