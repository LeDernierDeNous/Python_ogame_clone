import unittest
import time
from unittest.mock import Mock, patch
from src.resources.resourcetype import ResourceType
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer
from src.planets.planet import Planet

class TestPlanet(unittest.TestCase):

    def setUp(self):
        """Set up a basic planet instance with default resources."""
        self.planet = Planet(owner="John Doe", name="Earth")

    def test_initial_resources(self):
        """Check if the initial resources are set correctly."""
        resources = self.planet.get_resources()
        self.assertEqual(resources.metal, 100)
        self.assertEqual(resources.crystal, 50)
        self.assertEqual(resources.deuterium, 20)

    def test_calculate_base_production(self):
        """Test base production calculation for a single tick."""
        metal, crystal, deuterium = self.planet.calculate_base_production(tick=1)
        self.assertEqual(metal, Planet.METAL_BASE_PRODUCTION_RATE)
        self.assertEqual(crystal, Planet.CRYSTAL_BASE_PRODUCTION_RATE)
        self.assertEqual(deuterium, Planet.DEUTERIUM_BASE_PRODUCTION_RATE)

    @patch('time.time', return_value=1000)
    def test_add_and_upgrade_building(self, mock_time):
        """Test adding and upgrading a building."""
        metal_mine = self._create_mock_metal_mine()

        # Attempt to upgrade the building
        self.planet.upgrade_building(metal_mine)

        # Check that the building is added to the production list
        self.assertIn(MetalMine.get_static_type(), self.planet.get_buildings())

        # Verify that resources were deducted after the upgrade
        self._assert_resources(metal=40, crystal=35, deuterium=20)

        # Ensure the building upgrade was added to the production list
        self.assertEqual(len(self.planet.building_prodlist), 1)

        # Simulate time passing and updating production lists
        mock_time.return_value += 10  # Fast forward 10 seconds
        self.planet.update_prodlists()

        # Verify that the upgrade method was called after the production was completed
        metal_mine.upgrade.assert_called_once()

        # Verify that the production list is now empty
        self.assertEqual(len(self.planet.building_prodlist), 0)

    @patch('time.time', return_value=0)
    def test_produce_resources(self, mock_time):
        """Test resource production for one tick."""
        metal_mine = self._create_mock_metal_mine(production=30)
        self.planet.buildings[MetalMine.get_static_type()] = metal_mine

        # Produce resources for one tick
        self.planet.produce_resources(tick=1)

        # Verify resource amounts after production
        self._assert_resources(metal=140, crystal=55, deuterium=22)

    def test_update_prodlists(self):
        """Test updating production lists."""
        planet = Planet(owner="Player1", name="Planet1")
        planet.buildings = {
            MetalMine.get_static_type(): MetalMine(),
            CrystalField.get_static_type(): CrystalField(),
            DeuteriumSynthesizer.get_static_type(): DeuteriumSynthesizer()
        }
        planet.building_prodlist = [
            [MetalMine.get_static_type(), time.time() - 10],
            [CrystalField.get_static_type(), time.time() - 5]
        ]

        # Mock time and simulate the passage of time
        with patch("time.time", return_value=time.time() + 1):
            planet.update_prodlists()

        # Ensure that the production list has been cleared
        self.assertEqual(len(planet.building_prodlist), 0)
        self.assertEqual(planet.buildings[MetalMine.get_static_type()].get_level(), 1)
        self.assertEqual(planet.buildings[CrystalField.get_static_type()].get_level(), 1)

    def _create_mock_metal_mine(self, production=0):
        """Helper method to create a mock MetalMine."""
        metal_mine = MetalMine()
        metal_mine.get_type = Mock(return_value=MetalMine.get_static_type())
        metal_mine.calculate_upgrade_cost = Mock(return_value={
            ResourceType.METAL: 60,
            ResourceType.CRYSTAL: 15,
            ResourceType.DEUTERIUM: 0
        })
        metal_mine.get_level = Mock(return_value=1)
        metal_mine.upgrade = Mock()
        metal_mine.get_production = Mock(return_value=production)
        return metal_mine

    def _assert_resources(self, metal, crystal, deuterium):
        """Helper method to assert resource amounts."""
        resources = self.planet.get_resources()
        self.assertEqual(resources.metal, metal)
        self.assertEqual(resources.crystal, crystal)
        self.assertEqual(resources.deuterium, deuterium)

if __name__ == '__main__':
    unittest.main()
