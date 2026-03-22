
class Deck:
    def __init__(self, card: Card):
        self.card = []

    def add_card(self, card: Card) -> None:
        card.append(self.card)
        print(f"{self.name} la carte a ete ajoute")

    def remove_card(self, card_name: str) -> bool:
        for name in self.card:
            if self.card_name == name:
                self.card.remove(self.card_name)
                return True
        return False

def shuffle(self) -> None
def draw_card(self) -> Card
def get_deck_stats(self) -> dict


