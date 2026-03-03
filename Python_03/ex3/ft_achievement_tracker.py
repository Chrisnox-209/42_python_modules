def achievement_tracker() -> None:
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


def achievement_analytics(alice_set, bob_set, charlie_set):
    result = alice_set.union(bob_set.union(charlie_set))
    print(result)


if __name__ == "__main__":
    alice_set: set = {
        "plop",
        "plip",
        "plap",
        "plep"
    }
    bob_set: set = {
        "plop",
        "plip",
        "plap",
        "plup"
    }

    charlie_set: set = {
        "plop",
        "plip",
        "pfff",
        "plyp"
    }  
    print("=== Achievement Tracker System ===")
    print()
    # achievement_tracker()
    achievement_analytics(alice_set, bob_set, charlie_set)
    print()
