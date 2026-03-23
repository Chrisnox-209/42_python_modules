from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
import sys


if __name__ == "__main__":
	print("=== card creation ===\n")
	print(" -----------------------------------------------------"
	      "------------------------------------------\n"
	      "|     name     |     type     |     cost     |     rarity     "
		  "|     attack     |     health     |\n"
		  " -----------------------------------------------------"
	      "------------------------------------------")
	try:
		card_01 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
		print(f"|  {card_01.name} |   {card_01.type}   |       {card_01.cost}      |   {card_01.Rarity_Enum}    |       {card_01.attack}        |       {card_01.health}        |")
	except ValueError as error:
		print(error)
		sys.exit(1)
	finally:
		print()

	deck_obj = Deck()
	deck_obj.add_card(card_01)

	print(deck_obj.get_deck_stats())
