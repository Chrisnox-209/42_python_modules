def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if "INVALID" in validate_ingredients(ingredients):
        return ("Spell recorded: "
                f"{spell_name} {validate_ingredients(ingredients)}")
    else:
        return ("Spell rejected: "
                f"{spell_name} {validate_ingredients(ingredients)}")
