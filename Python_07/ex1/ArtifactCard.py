from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str) -> None:

        super().__init__(name, cost, rarity)

        if not isinstance(durability, int):
            raise TypeError("Durability must be integers")
        if durability <= 0:
            raise TypeError("Durability must be positive")

        self.durability: int = durability
        self.effect: str = effect
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect}

    def activate_ability(self) -> dict:
        return {
            "spell_name": self.name,
        }
