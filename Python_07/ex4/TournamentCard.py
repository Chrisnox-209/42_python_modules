from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        at_val: int,
        df_val: int,
        hp_val: int,
        rating: int = 1200
    ) -> None:
        super().__init__(name, cost, rarity)
        self.type: str = "Tournament"
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = rating

        if self.cost < 0:
            print(f"Warning: Negative cost for {name}. Setting to 0.")
            self.cost = 0

        self.attack_pwr: int
        if at_val < 0:
            print(f"Warning: Negative attack for {name}. Setting to 0.")
            self.attack_pwr = 0
        else:
            self.attack_pwr = at_val

        self.defense_pwr: int
        if df_val < 0:
            print(f"Warning: Negative defense for {name}. Setting to 0.")
            self.defense_pwr = 0
        else:
            self.defense_pwr = df_val

        self.health: int
        if hp_val <= 0:
            print(f"Warning: Invalid health for {name}. Setting to 1.")
            self.health = 1
        else:
            self.health = hp_val

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "status": "active in tournament",
            "mana_used": self.cost
        }

    def attack(self, target: Any) -> dict[str, Any]:
        target_name: str = (
            target if isinstance(target, str) else target.name
        )
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_pwr
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        safe_incoming: int = max(0, incoming_damage)
        actual_damage: int = max(0, safe_incoming - self.defense_pwr)

        self.health -= actual_damage
        is_alive: bool = self.health > 0

        return {
            "defender": self.name,
            "damage_taken": actual_damage,
            "remaining_health": self.health,
            "is_alive": is_alive
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_pwr,
            "defense": self.defense_pwr,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        if wins > 0:
            self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses > 0:
            self.losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }
