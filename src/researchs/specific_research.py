from src.researchs.research import Research

class EnergyTechnology(Research):
    def __init__(self):
        super().__init__(name="Energy Technology", metal_cost=100, crystal_cost=50, deuterium_cost=20)

    def apply_effect(self):
        # Logic for the effect of Energy Technology
        print("Energy Technology has been researched! Increased energy production.")

class LaserTechnology(Research):
    def __init__(self):
        super().__init__(name="Laser Technology", metal_cost=200, crystal_cost=150, deuterium_cost=50)

    def apply_effect(self):
        # Logic for the effect of Laser Technology
        print("Laser Technology has been researched! Increased attack power.")
