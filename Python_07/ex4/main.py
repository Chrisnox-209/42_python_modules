from typing import Any

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Rare", 8, 5, 15, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 6, 4, 10, 1150)

    print("Registering Tournament Cards...\n")

    id1: str = platform.register_card(dragon)
    print(f"{dragon.name} (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print()
    id2: str = platform.register_card(wizard)
    print(f"{wizard.name} (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(id1, id2)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard: Any = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
