import unittest
import time
from unittest.mock import Mock, patch
from src.resources.resourcetype import ResourceType
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer
from src.planets.planet import Planet

class TestPlanet(unittest.TestCase):

    def setUp(self):
        # Set up a basic planet instance
        self.planet = Planet(owner="John Doe", name="Earth")

    def test_initial_resources(self):
        # Check if the initial resources are set correctly
        resources = self.planet.get_resources()
        self.assertEqual(resources.metal, 100)
        self.assertEqual(resources.crystal, 50)
        self.assertEqual(resources.deuterium, 20)

    def test_calculate_base_production(self):
        # Test base production calculation
        metal, crystal, deuterium = self.planet.calculate_base_production(tick=1)
        self.assertEqual(metal, Planet.METAL_BASE_PRODUCTION_RATE)
        self.assertEqual(crystal, Planet.CRYSTAL_BASE_PRODUCTION_RATE)
        self.assertEqual(deuterium, Planet.DEUTERIUM_BASE_PRODUCTION_RATE)

    def test_add_and_upgrade_building(self):
        # Mock building and upgrade functionality
        metal_mine = MetalMine()
        metal_mine.get_type = Mock(return_value=MetalMine.get_static_type())
        metal_mine.calculate_upgrade_cost = Mock(return_value={
            ResourceType.METAL: 60,
            ResourceType.CRYSTAL: 15,
            ResourceType.DEUTERIUM: 0
        })
        metal_mine.get_level = Mock(return_value=1)
        metal_mine.upgrade = Mock()

        self.planet.upgrade_building(metal_mine)

        # Check if building is added
        self.assertIn(MetalMine.get_static_type(), self.planet.get_buildings())
        
        # Upgrade the building
        self.planet.upgrade_building(metal_mine)
        metal_mine.upgrade.assert_called_once()

    @patch('time.time', return_value=0)
    def test_produce_resources(self, mock_time):
        # Test resource production
        metal_mine = MetalMine()
        metal_mine.get_type = Mock(return_value=MetalMine.get_static_type())
        metal_mine.get_production = Mock(return_value=30)
        self.planet.buildings[MetalMine.get_static_type()] = metal_mine

        # Produce resources for one tick
        self.planet.produce_resources(tick=1)

        resources = self.planet.get_resources()
        self.assertEqual(resources.metal, 140)
        self.assertEqual(resources.crystal, 55)
        self.assertEqual(resources.deuterium, 22)

    def test_update_prodlists(self):
        planet = Planet(owner="Player1", name="Planet1")
        planet.buildings = {
            "metalmine": MetalMine(),
            "crystalfield": CrystalField(),
            "deuteriumsynthesizer": DeuteriumSynthesizer()
        }
        planet.building_prodlist = [["metalmine", time.time() - 10], ["crystalfield", time.time() - 5]]

        with patch("time.time", return_value=time.time() + 1):
            planet.update_prodlists()

        self.assertEqual(len(planet.building_prodlist), 0)
        self.assertEqual(planet.buildings["metalmine"].get_level(), 1)
        self.assertEqual(planet.buildings["crystalfield"].get_level(), 1)

    # def test_produce_units(self):
    #     # Mock a unit production
    #     unit = Unit()
    #     unit.get_type = Mock(return_value="fighter")
    #     unit.calculate_total_production_cost = Mock(return_value={
    #         ResourceType.METAL: 10,
    #         ResourceType.CRYSTAL: 5,
    #         ResourceType.DEUTERIUM: 0
    #     })

    #     self.planet.produce_units(unit, quantity=5)

    #     # Check if the resources are deducted correctly
    #     resources = self.planet.get_resources()
    #     self.assertEqual(resources.metal, 50)
    #     self.assertEqual(resources.crystal, 25)
    #     self.assertEqual(resources.deuterium, 20)

    #     # Check if unit is added to production list
    #     self.assertIn(["fighter", 5, 1], self.planet.unit_prodlist)

    def test_update_prodlists(self):
        planet = Planet(owner="Player1", name="Planet1")
        planet.buildings = {
            "metalmine": MetalMine(),
            "crystalfield": CrystalField(),
            "deuteriumsynthesizer": DeuteriumSynthesizer()
        }
        planet.building_prodlist = [["metalmine", time.time() - 10], ["crystalfield", time.time() - 5]]

        with patch("time.time", return_value=time.time() + 1):
            planet.update_prodlists()

        self.assertEqual(len(planet.building_prodlist), 0)
        self.assertEqual(planet.buildings["metalmine"].get_level(), 1)
        self.assertEqual(planet.buildings["crystalfield"].get_level(), 1)

    # def test_produce_units(self):
    #     # Mock a unit production
    #     unit = Unit()
    #     unit.get_type = Mock(return_value="fighter")
    #     unit.calculate_total_production_cost = Mock(return_value={
    #         ResourceType.METAL: 10,
    #         ResourceType.CRYSTAL: 5,
    #         ResourceType.DEUTERIUM: 0
    #     })

    #     self.planet.produce_units(unit, quantity=5)

    #     # Check if the resources are deducted correctly
    #     resources = self.planet.get_resources()
    #     self.assertEqual(resources.metal, 50)
    #     self.assertEqual(resources.crystal, 25)
    #     self.assertEqual(resources.deuterium, 20)

    #     # Check if unit is added to production list
    #     self.assertIn(["fighter", 5, 1], self.planet.unit_prodlist)

if __name__ == '__main__':
    unittest.main()
