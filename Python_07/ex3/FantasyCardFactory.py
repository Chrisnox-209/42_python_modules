from ex3.CardFactory import CardFactory
from ex0.Card import Card


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.list_creatures = ['dragon', 'goblin']
        self.list_spells = ['fireball']
        self.list_artifacts = ['mana_ring']
        self.name_factory = "FantasyCardFactory"

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        return {"creatures": self.list_creatures,
                "spells": self.list_spells,
                "artifacts": self.list_artifacts}

    def get_factory_name(self) -> str:
        return self.name_factory
