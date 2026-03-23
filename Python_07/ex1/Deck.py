from ex0.Card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.list_card = []

    def add_card(self, card: Card) -> None:
        self.list_card.append(card)
        print(f"{card.name} la carte a ete ajoute")

    def remove_card(self, card_name: str) -> bool:
        for name in self.card:
            if self.card_name == name:
                self.card.remove(self.card_name)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.card)

    # def draw_card(self) -> Card:

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
        size_dict = len(self.list_card)

        return {"total_cards": size_dict,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "total_cost": total_cost/size_dict }


