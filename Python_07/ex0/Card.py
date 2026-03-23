from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum

class type_Enum(str, Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        dict_info: Dict[str, str | int] = dict(
            name=self.name,
            cost=self.cost,
            rarity=self.rarity
            )
        return dict_info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False
