from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 Rarity_Enum: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, Rarity_Enum)

        if not isinstance(attack, int) or not isinstance(health, int):
            raise TypeError("Attack and health must be integers")

        if attack <= 0:
            raise ValueError("Attack must be positive")

        if health <= 0:
            raise ValueError("Health must be positive")

        self.attack = int(attack)
        self.health = int(health)
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        mana: int = game_state["mana"] - self.cost
        game_state.update({"mana": mana})
        return {"card_played": game_state["card_played"],
                "mana_used": game_state["cost"],
                "effect": game_state["effect"]}

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
            }

    def get_card_info(self) -> dict:
        dict_info: dict = (super().get_card_info())
        dict_info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health,
            })
        return dict_info
