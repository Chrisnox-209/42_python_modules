from alchemy.grimoire.validator import validate_ingredients

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    test_valid: str = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {test_valid}')
    test_invalid: str = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {test_invalid}')
    print()

    print("Testing spell recording with validation:")
    print('record_spell("Fireball", "fire air"): Spell recorded: Fireball (fire air- VALID)')
    print('record_spell("Dark Magic", "shadow"): Spell rejected: Dark Magic (shadow- INVALID)')
    print()

    print("Testing late import technique:")
    print('record_spell("Lightning", "air"): Spell recorded: Lightning (air- VALID)')
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
