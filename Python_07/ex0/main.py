from ex0.CreatureCard import CreatureCard
import sys

if __name__ == "__main__":
    name: str = "Fire Dragon"
    cost: int = 5
    rarity: str = "Legendary"
    attack: int = 7
    health: int = 5
    mana: int = 6
    target: str = 'Goblin Warrior'
    game_state: dict = {}

    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    try:
        card_01 = CreatureCard(name, cost, rarity, attack, health)
        print("CreatureCard Info:")
        print(card_01.get_card_info())
    except ValueError as error:
        print(error)
        sys.exit(1)
    finally:
        print()

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {card_01.is_playable(mana)}")
    if card_01.is_playable(mana):
        print(f"Play result: {card_01.play(game_state)}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f'Attack result: {card_01.attack_target("Goblin Warrior")}')
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {card_01.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
