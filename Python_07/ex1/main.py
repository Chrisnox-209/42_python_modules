from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
import random
import sys


if __name__ == "__main__":

    try:
        card_01 = CreatureCard("Fire Dragon",
                               5,
                               "Legendary",
                               7,
                               5
                               )
    except ValueError as error:
        print(error)
        sys.exit(1)

    try:
        card_02 = ArtifactCard("Mana Crystal",
                               3,
                               "Rare",
                               8,
                               "Permanent: +1 mana per turn"
                               )
    except ValueError as error:
        print(error)
        sys.exit(1)

    card_03 = SpellCard("Lightning Bolt",
                        2,
                        "Common",
                        "Deal 3 damage to target"
                        )
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck_obj = Deck()
    deck_obj.add_card(card_01)
    deck_obj.add_card(card_02)
    deck_obj.add_card(card_03)

    print(deck_obj.get_deck_stats())
    print("\nDrawing and playing cards:\n")

    nb_of_draws = 3
    game_state: dict = {}
    for i in range(3):
        if i > 1:
            deck_obj.shuffle()
        mana: int = random.randint(1, 10)
        card_drawd: Card = deck_obj.draw_card()
        print(f"Drew: {card_drawd.name} ({card_drawd.type})")
        if card_drawd.is_playable(mana):
            print(f"Play result: {card_drawd.play(game_state)}")
            deck_obj.remove_card(card_drawd.name)
        else:
            print(f"This card cannot be played: not enough mana ({mana})")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")
