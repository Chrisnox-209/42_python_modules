from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.list_card: list = []

    def add_card(self, card: Card) -> None:
        self.list_card.append(card)

    def remove_card(self, card_name: str) -> bool:
        for name in self.list_card:
            if card_name == name:
                self.list_card.remove(card_name)
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
            if monstre.type == "Creature":
                creatures += 1
            if monstre.type == "spell":
                spells += 1
            if monstre.type == "artifact":
                artifacts += 1
            total_cost += monstre.cost
        size_dict: int = len(self.list_card)
        avg_cost: float = total_cost / size_dict

        return {"total_cards": size_dict,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost:": round(avg_cost, 2)}
