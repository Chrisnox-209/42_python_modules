from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Type, List


def capabilities(name_class: Type) -> List[str]:
    list_method: list = []
    for method_name in dir(name_class):
        if (not method_name.startswith("__")
           and not method_name.startswith("_")):
            list_method.append(method_name)
    return list_method


if __name__ == "__main__":
    name: str = "Arcane Warrior"
    combat_type: str = "melee"
    rarity: str = "Legendary"
    attack_force: int = 12
    defense_force: int = 5
    spell_action: int = 5
    store_mana: int = 15
    health: int = 15
    cost: int = 5
    mana_enemy: int = 8
    game_state: dict = {}

    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {capabilities(Card)}")
    print(f"- Combatable: {capabilities(Combatable)}")
    print(f"- Magical: {capabilities(Magical)}")
    print("\nPlaying Arcane Warrior (Elite Card):\n")

    card_attack = EliteCard(name, cost, rarity, health, attack_force,
                            defense_force, spell_action, store_mana,
                            combat_type
                            )
    card_enemy = CreatureCard("Enemy", 4, "commun", 10, 7)
    card_enemy_01 = CreatureCard("Enemy1", 3, "commun", 4, 3)
    card_enemy_02 = CreatureCard("Enemy2", 5, "commun", 3, 4)

    print("Combat phase:")
    if card_attack.is_playable(card_attack.store_mana):
        game_state = card_attack.play(game_state)
        print(f"Attack result: {card_attack.attack(card_enemy)}")
    else:
        print("not enough mana to launch an attack "
              f"({card_attack.store_mana})")

    if card_attack.is_playable(card_attack.store_mana):
        game_state = card_attack.play(game_state)
        print(f"Defense result: {card_attack.defend(card_enemy.attack)}")
    else:
        print("not enough mana to launch an attack "
              f"({card_attack.store_mana})")
    print()

    print("Magic phase:")
    enemy_troops: list = [card_enemy_01, card_enemy_02]
    card_attack.store_mana = 15

    if card_attack.is_playable(card_attack.store_mana):
        game_state = card_attack.play(game_state)
        print('Spell cast: '
              f'{card_attack.cast_spell("Fireball", enemy_troops)}')
    else:
        print("not enough mana to launch an attack "
              f"({card_attack.store_mana})")

    if card_attack.is_playable(card_attack.store_mana):
        game_state = card_attack.play(game_state)
        print("Mana channel: "
              f"{card_attack.channel_mana(10)}")
    else:
        print("not enough mana to launch an attack "
              f"({card_attack.store_mana})")

    print("\nMultiple interface implementation successful!")
