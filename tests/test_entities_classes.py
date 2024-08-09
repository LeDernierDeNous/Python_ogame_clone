import unittest
from src.entities.entity import Entity
from src.entities.npc import NPC
from src.entities.player import Player
from src.planets.planet import Planet  # Assuming Planet is defined somewhere

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity_name = "Test Entity"
        self.entity = Entity(name=self.entity_name)

    def test_initialization(self):
        # Verify that the entity is initialized with the correct name and no planets
        self.assertEqual(self.entity.name, self.entity_name)
        self.assertEqual(len(self.entity.planets), 0)

    def test_add_planet(self):
        # Mock a planet object (assuming a simple Planet class is defined elsewhere)
        mock_planet = Planet(owner=self.entity_name, name="Planet A")
        self.entity.add_planet(mock_planet)

        # Verify that the planet was added
        self.assertEqual(len(self.entity.planets), 1)
        self.assertIn(mock_planet, self.entity.planets)

    def test_str(self):
        # Verify that the string representation of the entity is as expected
        expected_str = f"{self.entity_name} - Planets: 0"
        self.assertEqual(str(self.entity), expected_str)


class TestNPC(unittest.TestCase):
    def setUp(self):
        self.npc_name = "Test NPC"
        self.npc = NPC(name=self.npc_name)

    def test_initialization(self):
        # Verify that the NPC is initialized with the correct name and no planets
        self.assertEqual(self.npc.name, self.npc_name)
        self.assertEqual(len(self.npc.planets), 0)

    def test_add_planet(self):
        # Mock a planet object
        mock_planet = Planet(owner=self.npc_name, name="Planet NPC")
        self.npc.add_planet(mock_planet)

        # Verify that the planet was added
        self.assertEqual(len(self.npc.planets), 1)
        self.assertIn(mock_planet, self.npc.planets)

    def test_str(self):
        # Verify that the string representation of the NPC is as expected
        expected_str = f"{self.npc_name} - Planets: 0"
        self.assertEqual(str(self.npc), expected_str)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_name = "Test Player"
        self.player = Player(name=self.player_name)

    def test_initialization(self):
        # Verify that the player is initialized with the correct name and no planets
        self.assertEqual(self.player.name, self.player_name)
        self.assertEqual(len(self.player.planets), 1)

    def test_add_planet(self):
        # Mock a planet object
        mock_planet = Planet(owner=self.player_name, name="Planet Player")
        self.player.add_planet(mock_planet)

        # Verify that the planet was added
        self.assertEqual(len(self.player.planets), 2)
        self.assertIn(mock_planet, self.player.planets)

    def test_str(self):
        # Verify that the string representation of the player is as expected
        expected_str = f"{self.player_name} - Planets: 1"
        self.assertEqual(str(self.player), expected_str)


if __name__ == '__main__':
    unittest.main()
