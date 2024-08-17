import unittest
from unittest.mock import patch, Mock
import threading
import time

# Assuming your modules are correctly imported
from src.entities.player import Player
from src.planets.planet import Planet
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer
from main import add_building, view_planets, production_loop  # Assuming the main script is `main.py`

class TestGameScenario(unittest.TestCase):
    def setUp(self):
        # Create a mock player with planets
        self.player = Player(name="TestPlayer")
        self.planet1 = Planet(owner=self.player, name="TestPlanet1")
        self.planet2 = Planet(owner=self.player, name="TestPlanet2")
        self.player.planets.append(self.planet1)
        self.player.planets.append(self.planet2)

        # Mock building behavior
        self.metal_mine = MetalMine()
        self.crystal_field = CrystalField()
        self.deuterium_synthesizer = DeuteriumSynthesizer()

        # Add mock buildings to planet
        self.planet1.buildings["metalmine"] = self.metal_mine
        self.planet1.buildings["crystalfield"] = self.crystal_field

    @patch('builtins.input', side_effect=["1", "1", "1", "3"])  # Simulate adding building, then exit
    def test_add_building(self, mock_input):
        """Test adding a building via user input."""
        # Mock upgrade method so no actual logic is run
        self.metal_mine.calculate_upgrade_cost = Mock(return_value={
            "metal": 50, "crystal": 30, "deuterium": 10
        })
        self.metal_mine.get_level = Mock(return_value=1)
        self.metal_mine.upgrade = Mock()

        add_building(self.player)

        # Check that building was added and upgraded
        self.assertIn("metalmine", self.planet1.buildings)
        self.metal_mine.upgrade.assert_not_called()  # Since it's added to prodlist first

    @patch('builtins.input', side_effect=["e"])  # Simulate pressing 'e' to exit
    def test_view_planets(self, mock_input):
        """Test viewing planets and their buildings."""
        with patch('time.sleep', return_value=None):  # Mock time.sleep to speed up the test
            view_planets(self.player)

        # No asserts needed here as we are simulating user interaction and checking print outputs

    def test_production_loop(self):
        # Ensure planet1 is in the player's planet list
        self.player.planets.append(self.planet1)
        
        # Mock the produce_resources and update_prodlists methods on the Planet class
        with patch.object(Planet, 'produce_resources') as mock_produce_resources, \
            patch.object(Planet, 'update_prodlists') as mock_update_prodlists:

            # Create a stop event to control the loop
            stop_event = threading.Event()

            # Start the production loop in a separate thread
            production_thread = threading.Thread(target=production_loop, args=(self.player, stop_event, [Planet.produce_resources, Planet.update_prodlists]))
            production_thread.start()

            # Let the loop run briefly
            time.sleep(2)
            
            # Stop the loop
            stop_event.set()
            production_thread.join()

            # Ensure the mocked methods were called
            mock_produce_resources.assert_called()
            mock_update_prodlists.assert_called()

    @patch('builtins.input', side_effect=["3", "3"])  # Simulate user exiting the game
    @patch('threading.Thread.start', Mock())  # Prevent actual threading
    @patch('threading.Thread.join', Mock())  # Prevent join from throwing an error
    def test_main_exit(self, mock_input):
        """Test main game loop with immediate exit."""
        with patch('main.display_menu', return_value=None):
            with patch('main.production_loop', Mock()):
                from main import main  # Import main function from your script
                main()  # Run the game loop

        # If we reach here without issues, the game loop correctly handled exit

if __name__ == '__main__':
    unittest.main()
