from ex3.GameStrategy import GameStrategy
from ex0.Card import type_Enum


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self.name_strategy = "AggressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        my_hand_final: list = []
        my_creature: list = []
        my_spell: list = []
        my_artifact: list = []

        for card in hand:
            if card.type == type_Enum.CREATURE:
                my_creature.append(card)
            elif card.type == type_Enum.SPELL:
                my_spell.append(card)
            elif card.type == type_Enum.ARTIFACT:
                my_artifact.append(card)

        my_creature = sorted(my_creature,
                             key=lambda card: (card.attack),
                             reverse=True)
        my_spell = sorted(my_spell,
                          key=lambda card: (card.cost))
        my_artifact = sorted(my_artifact,
                             key=lambda card: (card.durability),
                             reverse=True)

        my_hand_final = my_creature + my_spell + my_artifact
        list_targets: list = self.prioritize_targets(battlefield)

        return {"Cards": "plop"}

    def get_strategy_name(self) -> str:
        return self.name_strategy

    def prioritize_targets(self, available_targets: list) -> list:
        list_targets: list = []
        for card in available_targets:
            if card.type == type_Enum.CREATURE:
                list_targets.append(card)
        list_targets: list = sorted(list_targets,
                                    key=lambda card: (card.health),
                                    reverse=True)
        return list_targets
