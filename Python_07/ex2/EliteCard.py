from ex0.Card import type_Enum
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 health: int,
                 attack_force: int,
                 defense_force: int,
                 spell_action: int,
                 store_mana: int,
                 combat_type: str
                 ) -> None:
        super().__init__(name, cost, rarity)
        if health <= 0:
            raise ValueError("Health has to be positive")
        if attack_force < 0:
            raise ValueError("attack_force has to be positive")
        if defense_force < 0:
            raise ValueError("defense_force cannot be negative")
        self.health: int = health
        self.attack_force: int = attack_force
        self.defense_force: int = defense_force
        self.spell_action: int = spell_action
        self.store_mana: int = store_mana
        self.combat_type: str = combat_type
        self.type: type_Enum = type_Enum.ELITE

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "combat_type": self.combat_type}

    def attack(self, target) -> dict:
        damage_attack: int = random.randint(1, self.attack_force)
        self.store_mana = (self.store_mana - damage_attack)
        return {"attacker": self.name, "target": target.name,
                "damage": damage_attack, "combat_type": self.combat_type}

    def defend(self, incoming_damage: int) -> dict:
        life: bool = True
        damage: int = random.randint(1, max(1, incoming_damage))
        damage_blocked: int = random.randint(1, max(1, self.defense_force))
        damage_defend: int = damage - damage_blocked
        self.store_mana = (self.store_mana - damage_blocked)

        if damage_defend < 0:
            damage_defend = 0
        if damage_defend >= self.health:
            life = False
        self.health = (self.health - damage_defend)

        return {"defender": self.name, "damage_taken": damage_defend,
                "damage_blocked": damage_blocked, "still_alive": life}

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "health": self.health,
                "mana": self.store_mana}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        targets_name: list = []
        total_health: int = 0
        for enemy in targets:
            targets_name.append(enemy.name)
            total_health += enemy.health
        average: Any | float = ((total_health + self.store_mana)
                                / (len(targets_name)))
        mana_used: int = random.randint(1, max(1, int(average)))
        self.store_mana = self.store_mana - mana_used

        return {"caster": self.name, "spell": spell_name,
                "targets": targets_name, "mana_used": mana_used}

    def channel_mana(self, amount: int) -> dict:
        amount = random.randint(1, max(1, amount))
        self.store_mana += amount
        return {"channeled": amount,
                "total_mana": self.store_mana}

    def get_magic_stats(self) -> dict:
        return {"name": self.name, "health": self.health,
                "mana": self.store_mana, "spell": self.spell_action}
