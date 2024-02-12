import unittest
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer


class TestMineClasses(unittest.TestCase):

    def test_metal_mine(self):
        metal_mine = MetalMine()
        self.assertEqual(metal_mine.get_production(), 0)  # Add appropriate test value
        upgrade_cost = metal_mine.calculate_upgrade_cost()
        # Add appropriate assertions for upgrade cost

    def test_crystal_field(self):
        crystal_field = CrystalField()
        self.assertEqual(crystal_field.get_production(), 0)  # Add appropriate test value
        upgrade_cost = crystal_field.calculate_upgrade_cost()
        # Add appropriate assertions for upgrade cost

    def test_deuterium_synthesizer(self):
        deuterium_synthesizer = DeuteriumSynthesizer()
        self.assertEqual(deuterium_synthesizer.get_production(), 0)  # Add appropriate test value
        upgrade_cost = deuterium_synthesizer.calculate_upgrade_cost()
        # Add appropriate assertions for upgrade cost


if __name__ == '__main__':
    unittest.main()
