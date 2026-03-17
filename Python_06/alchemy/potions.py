import alchemy.elements


def healing_potion() -> str:
    fire: str = alchemy.elements.create_fire()
    water: str = alchemy.elements.create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    earth: str = alchemy.elements.create_earth()
    fire: str = alchemy.elements.create_fire()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    air: str = alchemy.elements.create_air()
    water: str = alchemy.elements.create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    fire: str = alchemy.elements.create_fire()
    water: str = alchemy.elements.create_water()
    earth: str = alchemy.elements.create_earth()
    air: str = alchemy.elements.create_air()
    return (f"Wisdompotion brewed with all elements: {fire} "
            f"-  {water} - {earth} - {air}")
