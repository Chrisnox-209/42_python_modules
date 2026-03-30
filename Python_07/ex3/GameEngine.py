from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
import random
import sys


class GameEngine:
    def __init__(self, hand_list: list, battlefield_list: list) -> None:
        self.hand_list: list = hand_list
        self.battlefield_list: list = battlefield_list
        self.turns: int = 0
        self.total_damage: int = random.randint(1, 50)
        self.cards_created: int = len(self.hand_list)

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory: CardFactory = factory
        self.strategy: GameStrategy = strategy

    def simulate_turn(self) -> dict:
        sys.stdout.write("hand: [")
        for i, card in enumerate(self.hand_list):
            sys.stdout.write(f"{card.name} ({card.cost})")
            if i != len(self.hand_list) - 1:
                sys.stdout.write(", ")
        sys.stdout.write("]\n")
        return {"Cards": self.hand_list}

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": type(self.strategy).__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
