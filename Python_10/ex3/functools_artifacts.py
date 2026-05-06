import functools
from functools import reduce, partial
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    elif operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell: partial = functools.partial(base_enchantment,
                                            power=50, element="Fire")
    ice_spell: partial = functools.partial(base_enchantment,
                                           power=50, element="Ice")
    lightning_spell: partial = functools.partial(base_enchantment,
                                                 power=50, element="Lightning")
    return {"Fire": fire_spell, "Ice": ice_spell, "Lightning": lightning_spell}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast


def main() -> None:
    print("Testing spell reducer...")
    power_spell: list[int] = [40, 20, 10, 30]
    print(f"Sum: {spell_reducer(power_spell, 'add')}")
    print(f"Product: {spell_reducer(power_spell, 'multiply')}")
    print(f"Max: {spell_reducer(power_spell, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return (f"power: {power}, element: {element}, target: {target}")
    spells: dict[str, Callable[..., Any]] = partial_enchanter(base_enchantment)
    print(spells["Fire"](target="Dragon"))
    print(spells["Ice"](target="Snake"))
    print(spells["Lightning"](target="Goblin"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    spellcaster: Callable[[Any], str] = spell_dispatcher()
    print(spellcaster(42))
    print(spellcaster("fireball"))
    print(spellcaster(["Feu", "Glace", "Foudre"]))
    print(spellcaster(42.5))


if __name__ == "__main__":
    main()
