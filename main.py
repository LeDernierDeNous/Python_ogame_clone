import time
import threading
from src.planets.planet import Planet
from src.entities.player import Player
from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer

def display_menu():
    print("\n--- Main Menu ---")
    print("1. Add Planet")
    print("2. Add Building")
    print("3. View Planets")
    print("4. Exit")

def add_planet(player):
    name = input("Enter the name of the planet: ")
    planet = Planet(owner=player.name, name=name)
    player.add_planet(planet)
    print(f"Planet '{name}' added to player '{player.name}'.")

def add_building(player):
    if not player.planets:
        print("No planets available. Add a planet first.")
        return

    print("Select a planet:")
    for index, planet in enumerate(player.planets):
        print(f"{index + 1}. {planet.name}")
    
    planet_index = int(input("Enter the number of the planet: ")) - 1
    if planet_index < 0 or planet_index >= len(player.planets):
        print("Invalid planet selection.")
        return
    
    planet = player.planets[planet_index]

    print("Select a building to add:")
    print("1. Metal Mine")
    print("2. Crystal Field")
    print("3. Deuterium Synthesizer")
    
    building_choice = int(input("Enter the number of the building: "))
    if building_choice == 1:
        building = MetalMine()
    elif building_choice == 2:
        building = CrystalField()
    elif building_choice == 3:
        building = DeuteriumSynthesizer()
    else:
        print("Invalid building selection.")
        return

    planet.add_building(building)
    print(f"{building.get_type().capitalize()} added to planet '{planet.name}'.")

def view_planets(player):
    while True:
        # Clear the screen (optional, depending on your environment)
        print("\033[H\033[J", end="")  # ANSI escape code to clear the screen (works in many terminals)

        print("\n--- View Planets ---")
        if not player.planets:
            print("No planets available.")
        else:
            for i, planet in enumerate(player.planets):
                print(f"{i + 1}. {planet}")

        print("\nOptions:")
        print("1. Refresh")
        print("2. Exit to Main Menu")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                pass  # Refresh logic is implicit in the loop
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        time.sleep(1)  # Short sleep to prevent rapid input processing

def resource_production_loop(player, stop_event):
    while not stop_event.is_set():
        for planet in player.planets:
            planet.produce_resources()
        time.sleep(1)  # Wait for 1 second before the next update

def main():
    player_name = input("Enter your player name: ")
    player = Player(name=player_name)

    stop_event = threading.Event()
    production_thread = threading.Thread(target=resource_production_loop, args=(player, stop_event))
    production_thread.start()

    try:
        while True:
            display_menu()
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                add_planet(player)
            elif choice == 2:
                add_building(player)
            elif choice == 3:
                view_planets(player)
            elif choice == 4:
                print("Exiting the game.")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        stop_event.set()
        production_thread.join()

if __name__ == "__main__":
    main()
