from src.buildings.mine import MetalMine, CrystalField, DeuteriumSynthesizer

def test_mine(mine_type: str):
    mine_class = {
        "metal": MetalMine,
        "crystal": CrystalField,
        "deuterium": DeuteriumSynthesizer
    }.get(mine_type.lower())

    if mine_class:
        mine = mine_class()
        production = mine.get_production()
        print(f"{mine_type.capitalize()} Mine production (Level {mine.level}): {production}")
        
        # Upgrade the mine
        mine.upgrade()
        production_after_upgrade = mine.get_production()
        print(f"{mine_type.capitalize()} Mine production after upgrade (Level {mine.level}): {production_after_upgrade}")
    else:
        print(f"Unsupported mine type: {mine_type}")

def test_type(mine_type: str):
    mine_class = {
        "metal": MetalMine,
        "crystal": CrystalField,
        "deuterium": DeuteriumSynthesizer
    }.get(mine_type.lower())

    if mine_class:
        mine = mine_class()
        type = mine.get_type()
        print(f"{mine_type.capitalize()} Mine type (Level {mine.level}): {type}")
    else:
        print(f"Unsupported mine type: {mine_type}")


# Test Metal Mine
test_mine("metal")

# Test Crystal Field
test_mine("crystal")

# Test Deuterium Synthesizer
test_mine("deuterium")

# Test type Metal Mine
test_type("metal")

# Test type Crystal Field
test_type("crystal")

# Test type Deuterium Synthesizer
test_type("deuterium")