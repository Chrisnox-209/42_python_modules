def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == 'packets':
        new_unit = "packets available"
    elif unit == 'grams':
        new_unit = "grams total"
    elif unit == "area":
        new_unit = "square meters"
    else:
        new_unit = "Unknown unit type"
    print(
        f"{seed_type.capitalize()} seeds"
        f"{' covers' if seed_type == 'lettuce' else ''} "
        f"{quantity} {new_unit}"
    )
