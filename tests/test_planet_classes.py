from collections import namedtuple
import unittest
from unittest.mock import MagicMock
from src import *

class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.owner = "TestOwner"
        self.name = "TestPlanet"
        self.planet = Planet(owner=self.owner, name=self.name)

    def test_add_building(self):
        metal_mine = MetalMine()
        crystal_field = CrystalField()
        deuterium_synthesizer = DeuteriumSynthesizer()

        self.planet.add_building(metal_mine)
        self.planet.add_building(crystal_field)

        # Adding the same type of building should print a message
        with self.assertLogs() as log:
            self.planet.add_building(metal_mine)
            self.assertIn(f"A Metal building already exists on this planet.", log.output[0])

        # Verify the correct buildings are added
        self.assertIn(MetalMine.building_type, self.planet.buildings)
        self.assertIn(CrystalField.building_type, self.planet.buildings)
        self.assertNotIn(DeuteriumSynthesizer.building_type, self.planet.buildings)

    def test_calculate_base_production(self):
        tick = 3
        production_rates = self.planet.calculate_base_production(tick)

        # Verify production rates
        self.assertEqual(30, production_rates.metal)
        self.assertEqual(15, production_rates.crystal)
        self.assertEqual(6, production_rates.deuterium)

    def test_calculate_building_production(self):
        tick = 2

        # Create mock building instances
        metal_mine = MagicMock()
        metal_mine.get_production.return_value = 20

        crystal_field = MagicMock()
        crystal_field.get_production.return_value = 15

        deuterium_synthesizer = MagicMock()
        deuterium_synthesizer.get_production.return_value = 8

        # Add mock buildings to the planet
        self.planet.buildings[MetalMine.building_type] = metal_mine
        self.planet.buildings[CrystalField.building_type] = crystal_field
        self.planet.buildings[DeuteriumSynthesizer.building_type] = deuterium_synthesizer

        production_rates = self.planet.calculate_building_production(tick)

        # Verify building-based production rates
        self.assertEqual(40, production_rates.metal)
        self.assertEqual(30, production_rates.crystal)
        self.assertEqual(16, production_rates.deuterium)

    def test_produce_resources(self):
        # Stub calculate_base_production and calculate_building_production
        self.planet.calculate_base_production = MagicMock(return_value=namedtuple(metal=10, crystal=5, deuterium=2))
        self.planet.calculate_building_production = MagicMock(return_value=namedtuple(metal=20, crystal=15, deuterium=8))

        self.planet.produce_resources(tick=3)

        # Verify that resources are updated correctly
        self.assertEqual(96, self.planet.resources.metal)
        self.assertEqual(65, self.planet.resources.crystal)
        self.assertEqual(26, self.planet.resources.deuterium)

    def test_str(self):
        # Stub __str__ method for Resource
        Resource.__str__ = MagicMock(return_value="ResourceString")

        # Verify that the __str__ method of Planet returns the expected string
        self.assertEqual("TestPlanet (Owner: TestOwner) - ResourceString", str(self.planet))

if __name__ == '__main__':
    unittest.main()
