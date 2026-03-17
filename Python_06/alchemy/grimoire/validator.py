
def validate_ingredients(ingredients: str) -> str:
    list_ingredients: list = ["fire", "water", "earth", "air"]
    list_user: list[str] = ingredients.split(" ")
    if set(list_user) <= set(list_ingredients):
        return f"{list_user} - VALID"
    else:
        return f"{list_user} - INVALID"
