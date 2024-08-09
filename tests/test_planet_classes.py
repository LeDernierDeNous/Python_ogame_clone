from collections import namedtuple
from io import StringIO
import unittest
from unittest.mock import MagicMock, patch

from src.resources.resource import Resource
from src.planets.planet import Planet
from src import *
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer

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

        # Verify the correct buildings are added
        self.assertIn(MetalMine.get_static_type(), self.planet.buildings)
        self.assertIn(CrystalField.get_static_type(), self.planet.buildings)
        self.assertNotIn(DeuteriumSynthesizer.get_static_type(), self.planet.buildings)

    def test_add_building_existing(self):
        planet = Planet(owner="Test Owner", name="Test Planet")
        metal_building = MetalMine()
        planet.add_building(metal_building)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            planet.add_building(metal_building)

        expected_output = "A Metalmine building already exists on this planet.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_calculate_base_production(self):
        tick = 3
        production_rates = self.planet.calculate_base_production(tick)

        # Verify production rates
        self.assertEqual(30, production_rates[0])
        self.assertEqual(15, production_rates[1])
        self.assertEqual(6, production_rates[2])

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
        self.planet.buildings[MetalMine.get_static_type()] = metal_mine
        self.planet.buildings[CrystalField.get_static_type()] = crystal_field
        self.planet.buildings[DeuteriumSynthesizer.get_static_type()] = deuterium_synthesizer

        production_rates = self.planet.calculate_building_production(tick)

        # Verify building-based production rates
        self.assertEqual(40, production_rates[0])
        self.assertEqual(30, production_rates[1])
        self.assertEqual(16, production_rates[2])

    def test_produce_resources(self):
        # Stub calculate_base_production and calculate_building_production
        self.planet.calculate_base_production = MagicMock(return_value=(10, 5, 2))
        self.planet.calculate_building_production = MagicMock(return_value=(20, 15, 8))

        self.planet.produce_resources(tick=3)

        # Verify that resources are updated correctly
        self.assertEqual(130, self.planet.resources.metal)
        self.assertEqual(70, self.planet.resources.crystal)
        self.assertEqual(30, self.planet.resources.deuterium)

    def test_str(self):
        # Stub __str__ method for Resource
        Resource.__str__ = MagicMock(return_value="ResourceString")

        # Verify that the __str__ method of Planet returns the expected string
        self.assertEqual("TestPlanet (Owner: TestOwner) - ResourceString", str(self.planet))

if __name__ == '__main__':
    unittest.main()
