def achievement_data() -> None:
    alice_set: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    bob_set: set = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie_set: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")
    print()
    achievement_analytics(alice_set, bob_set, charlie_set)


def achievement_analytics(alice_set, bob_set, charlie_set) -> None:
    print("=== Achievement Analytics ===")

    result: set = alice_set.union(bob_set.union(charlie_set))
    print(f"All unique achievements: {result}")
    print(f"Total unique achievements: {len(result)}")
    print()

    result = alice_set.intersection(bob_set.intersection(charlie_set))
    print(f"Common to all players: {result}")

    unique_1: set = alice_set - (bob_set | charlie_set)
    unique_2: set = bob_set - (alice_set | charlie_set)
    unique_3: set = charlie_set - (alice_set | bob_set)
    result = unique_1 | unique_2 | unique_3
    print(f"Rare achievements (1 player): {result}")
    print()

    result = alice_set.intersection(bob_set)
    print(f"Alice vs Bob common: {result}")

    result = alice_set.difference(bob_set)
    print(f"Alice unique: {result}")

    result = bob_set.difference(alice_set)
    print(f"Bob unique: {result}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    achievement_data()
