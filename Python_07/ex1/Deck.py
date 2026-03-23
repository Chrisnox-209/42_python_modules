from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self) -> None:
        self.list_card: list = []

    def add_card(self, card: Card) -> None:
        self.list_card.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.list_card:
            if card.name == card_name:
                self.list_card.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.list_card)

    def draw_card(self) -> Card:
        return self.list_card[0]

    def get_deck_stats(self) -> dict:
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: int = 0

        for monstre in self.list_card:
            if isinstance(monstre, CreatureCard):
                creatures += 1
            if isinstance(monstre, SpellCard):
                spells += 1
            if isinstance(monstre, ArtifactCard):
                artifacts += 1
            total_cost += monstre.cost
        size_dict: int = len(self.list_card)
        if size_dict > 0:
            avg_cost: float = total_cost / size_dict
        else:
            avg_cost = 0
        return {"total_cards": size_dict,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": round(avg_cost, 2)}
