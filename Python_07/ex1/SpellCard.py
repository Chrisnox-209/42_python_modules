from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        mana: int = game_state["mana"] - self.cost
        game_state.update({"mana": mana})
        return {"card_played": game_state["card_played"],
                "mana_used": game_state["cost"],
                "effect": game_state["effect"]}

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell_name": self.name,
            "effect_type": self.effect_type,
            "targets_affected": targets
        }
