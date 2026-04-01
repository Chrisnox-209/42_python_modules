from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    deck_list: list = []
    enemy_list: list = []

    game_engine = GameEngine()
    my_factory = FantasyCardFactory()
    my_strategy = AggressiveStrategy()
    print(f"Factory: {my_factory.get_factory_name()}")
    print(f"Strategy: {my_strategy.get_strategy_name()}")
    print(f"Available types:: {my_factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    game_engine.configure_engine(my_factory, my_strategy)

    tour_report: dict = game_engine.simulate_turn()

    print()
    print("\nTurn execution:")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Actions: {tour_report}")

    print()
    print("\nGame Report:")
    print(game_engine.get_engine_status())

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
