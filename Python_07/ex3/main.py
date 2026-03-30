from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
import sys

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    deck_list: list = []
    enemy_list: list = []

    game_engine = GameEngine(deck_list, enemy_list)
    my_factory = FantasyCardFactory()
    my_strategy = AggressiveStrategy()
    print(f"Factory: {my_factory.get_factory_name()}")
    print(f"Strategy: {my_strategy.get_strategy_name()}")
    print(f"Available types:: {my_factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    game_engine.configure_engine(my_factory, my_strategy)

    try:
        enemy: dict = my_factory.create_ennemy_deck(5)
    except Exception as error:
        print(f"Deck ennemy creation error: {error}")
        sys.exit(1)

    for value in enemy.values():
        enemy_list.extend(value)

    try:
        my_deck: dict = game_engine.factory.create_themed_deck(5)
    except Exception as error:
        print(f"Deck themed creation error: {error}")
        sys.exit(1)

    for value in my_deck.values():
        deck_list.extend(value)

    game_engine.simulate_turn()

    print()
    print("\nTurn execution:")
    print(f"Strategy: { game_engine.strategy.get_strategy_name()}")
    game_engine.strategy.execute_turn(deck_list, enemy_list)

    print()
    print("\nGame Report:")
    print(game_engine.get_engine_status())
