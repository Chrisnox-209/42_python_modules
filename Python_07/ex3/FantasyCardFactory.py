from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from enum import Enum
import random


class rarity_Enum(str, Enum):
    LEGENDARY = "Legendary"
    RARE = "Rare"
    COMMON = "Common"
    UNCOMMON = "Uncommon"


class Effect_Spell_Enum(str, Enum):
    DEAL_3_DAMAGE = "Deal 3 damage to target"
    HEAL_5_HEALTH = "Restore 5 health to target"
    DRAW_2_CARDS = "Draw 2 cards"
    SHIELD_4 = "Give 4 shield to target"


class Effect_Artifact_Enum(str, Enum):
    INCREASE_MANA = "Permanent: +1 mana per turn"
    INCREASE_HEALTH = "Permanent: +2 max health"
    INCREASE_ATTACK = "Permanent: +1 attack"
    DRAW_CARD_EACH_TURN = "Permanent: Draw 1 card each turn"


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.list_creatures: list[str] = ['dragon', 'goblin']
        self.list_spells: list[str] = ['fireball']
        self.list_artifacts: list[str] = ['mana_ring']
        self.name_factory = "FantasyCardFactory"

    def create_creature(self, name_or_power: str | int | None = None) -> Card:

        # ### Randomness Management
        name: str = random.choice(self.list_creatures)
        cost: int = random.randint(1, 10)
        rarity: str = random.choice(list(rarity_Enum))
        attack: int = random.randint(1, 20)
        health: int = random.randint(1, 30)

        if isinstance(name_or_power, str):
            if name_or_power in self.list_creatures:
                return CreatureCard(name_or_power, cost, rarity, attack,
                                    health)
            else:
                print(f"({name_or_power}): This creature is not in stock\n"
                      f"list of our creatures: {self.list_creatures}")
        elif isinstance(name_or_power, int):
            return CreatureCard(name, cost, rarity, name_or_power, health)
        elif name_or_power is None:
            return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:

        # ### Randomness Management
        name: str = random.choice(self.list_spells)
        cost: int = random.randint(1, 10)
        rarity: str = random.choice(list(rarity_Enum))
        effect_type: str = random.choice(list(Effect_Spell_Enum))

        if isinstance(name_or_power, str):
            if name_or_power in self.list_spells:
                return SpellCard(name_or_power, cost, rarity, effect_type)
            else:
                print(f"({name_or_power}): This spell is not in stock\n"
                      f"list of our spells: {self.list_spells}")
        elif isinstance(name_or_power, int):
            return SpellCard(name, name_or_power, rarity, effect_type)
        elif name_or_power is None:
            return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        # ### Randomness Management
        name: str = random.choice(self.list_spells)
        cost: int = random.randint(1, 10)
        rarity: str = random.choice(list(rarity_Enum))
        durability: int = random.randint(1, 25)
        effect_type: str = random.choice(list(Effect_Artifact_Enum))

        if isinstance(name_or_power, str):
            if name_or_power in self.list_spells:
                return ArtifactCard(name_or_power, cost, rarity, durability,
                                    effect_type)
            else:
                print(f"({name_or_power}): This artifact is not in stock\n"
                      f"list of our artifacts: {self.list_artifacts}")
        elif isinstance(name_or_power, int):
            return ArtifactCard(name, cost, rarity, name_or_power,
                                effect_type)
        elif name_or_power is None:
            return ArtifactCard(name, cost, rarity, durability, effect_type)

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        return {"creatures": self.list_creatures,
                "spells": self.list_spells,
                "artifacts": self.list_artifacts}

    def get_factory_name(self) -> str:
        return self.name_factory
