from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any
import sys


class GameEngine:
    def __init__(self) -> None:
        self.turns: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory: CardFactory = factory
        self.strategy: GameStrategy = strategy

    def simulate_turn(self) -> dict:
        hand_list: list = []
        battlefield_list: list = []
        try:
            my_deck_dict: dict = self.factory.create_themed_deck(3)
        except Exception as error:
            print(f"Deck themed creation error: {error}")
            sys.exit(1)
        for value in my_deck_dict.values():
            hand_list.extend(value)

        self.cards_created += len(hand_list)

        try:
            enemy: dict = self.factory.create_ennemy_deck(5)
        except Exception as error:
            print(f"Deck ennemy creation error: {error}")
            sys.exit(1)

        for value in enemy.values():
            battlefield_list.extend(value)

        sys.stdout.write("Hand: [")
        for i in range(len(hand_list)):
            card: Any = hand_list[i]
            sys.stdout.write(f"{card.name} ({card.cost})")
            if i != len(hand_list) - 1:
                sys.stdout.write(", ")
        sys.stdout.write("]")

        resultats_du_tour: dict = self.strategy.execute_turn(hand_list,
                                                             battlefield_list)
        tour_damage: Any = resultats_du_tour.get('damage_dealt', 0)
        self.total_damage += tour_damage
        self.turns += 1
        return resultats_du_tour

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": type(self.strategy).__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
