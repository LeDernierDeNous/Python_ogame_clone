class Resource:
    def __init__(self, metal:int=0, crystal:int=0, deuterium:int=0):
        self.metal = metal
        self.crystal = crystal
        self.deuterium = deuterium

    def __str__(self):
        return f"Metal: {self.metal}, Crystal: {self.crystal}, Deuterium: {self.deuterium}"
