import unittest
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer
from src.resources.resourcetype import ResourceType

class TestMineBuildings(unittest.TestCase):

    def test_metal_mine_initialization(self):
        metal_mine = MetalMine()
        self.assertEqual(metal_mine.get_name(), "Metal Mine")
        self.assertEqual(metal_mine.get_type(), "metalmine")
        self.assertEqual(metal_mine.resource_type, ResourceType.METAL)

    def test_crystal_field_initialization(self):
        crystal_field = CrystalField()
        self.assertEqual(crystal_field.get_name(), "Crystal Mine")
        self.assertEqual(crystal_field.get_type(), "crystalfield")
        self.assertEqual(crystal_field.resource_type, ResourceType.CRYSTAL)

    def test_deuterium_synthesizer_initialization(self):
        deuterium_synthesizer = DeuteriumSynthesizer()
        self.assertEqual(deuterium_synthesizer.get_name(), "Deuterium Mine")
        self.assertEqual(deuterium_synthesizer.get_type(), "deuteriumsynthesizer")
        self.assertEqual(deuterium_synthesizer.resource_type, ResourceType.DEUTERIUM)

    def test_metal_mine_production(self):
        metal_mine = MetalMine()
        metal_mine.level = 5
        expected_production = int(30 * 5 * (1.1 ** 5))
        self.assertEqual(metal_mine.get_production(), expected_production)

    def test_upgrade_costs(self):
        metal_mine = MetalMine()
        metal_mine.level = 1
        costs = metal_mine.calculate_upgrade_cost()
        self.assertEqual(costs[ResourceType.METAL], 60)
        self.assertEqual(costs[ResourceType.CRYSTAL], 15)

    def test_static_types(self):
        self.assertEqual(MetalMine.get_static_type(), "metalmine")
        self.assertEqual(CrystalField.get_static_type(), "crystalfield")
        self.assertEqual(DeuteriumSynthesizer.get_static_type(), "deuteriumsynthesizer")

if __name__ == "__main__":
    unittest.main()