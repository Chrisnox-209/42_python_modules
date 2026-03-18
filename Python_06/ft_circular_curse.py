from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    test_valid: str = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {test_valid}')
    test_invalid: str = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {test_invalid}')
    print()

    print("Testing spell recording with validation:")
    print('record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print('record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')
    print()

    print("Testing late import technique:")
    print('record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
