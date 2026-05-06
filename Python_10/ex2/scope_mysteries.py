from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def call_counter() -> int:
        nonlocal count
        count += 1
        return count
    return call_counter


def spell_accumulator(initial_power: int) -> Callable:

    def add_power(amount):
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def build_enchantement(item_name: str):
        return (f"{enchantment_type} {item_name}")
    return build_enchantement


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        return vault.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = spell_accumulator(100)
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 30: {base(30)}")

    print("\nTesting memory vault...")
    use_spell_flaming = enchantment_factory("Flaming")
    use_spell_frozen = enchantment_factory("Frozen")
    print(use_spell_flaming("Sword"))
    print(use_spell_frozen("Shield"))

    print("\nTesting memory vault...")
    mem = memory_vault()
    mem['store']("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {mem['recall']('secret')}")
    print(f"Recall 'unknown': {mem['recall']('unknown')}")


if __name__ == "__main__":
    main()
