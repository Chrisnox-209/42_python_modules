from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (lambda target, power:
            f"{spell1(target, power)}, {spell2(target, power)}")


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda power: base_spell(power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [s(target, power) for s in spells]

def main() -> None:
    print("Testing spell combiner...")

    def spell(target: str, power: int) -> str:
        return f"the spell hits {target} with a power of {power} HP"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"
    combined: Callable = spell_combiner(spell, heal)
    print(f"Combined spell result: {combined('Dragon', 42)}")

    print("\nTesting power amplifier...")

    def fireball(power: int) -> int:
        return power
    power: int = 10
    multiplier: int = 3
    mega_fireball: Callable = power_amplifier(fireball, multiplier)
    print(f"Original: {power}, Amplified: {mega_fireball(power)}")

    print("\nTesting conditional caster...")

    def condition(target: str, power: int) -> bool:
        if power > 10:
            return True
        else:
            return False
    conditional: Callable = conditional_caster(condition, spell)
    print(f"True condition: {conditional('Snake', 15)}")
    print(f"False condition: {conditional('Snake', 8)}")

    print("\nTesting spell sequence...")

    def iceball(target: str, power: int) -> str:
        return f"the iceball hits {target} with a power of {power} HP"

    list_spells: Callable = spell_sequence([spell, heal, iceball])

    spells: Any = list_spells("Dragon", 12)
    for sort in spells:
        print(f"- {sort}")


if __name__ == "__main__":
    main()
