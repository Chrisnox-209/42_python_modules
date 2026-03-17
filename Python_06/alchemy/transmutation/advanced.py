from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    gold: str = lead_to_gold()
    potion: str = healing_potion()
    return f"Philosopher’s stone created using {gold} and {potion}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
