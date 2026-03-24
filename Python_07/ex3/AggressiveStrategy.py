from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self.name_strategy = "AggressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return self.name_strategy

    def prioritize_targets(self, available_targets: list) -> list:
        pass
