import sys


def parsing(string: str, inventory: dict) -> dict:
    key: str = ""
    value: str = ""
    flag = False

    for letter in string:
        if letter == ":":
            if flag:
                raise ValueError("Error: Invalid format")
            flag = True
        elif not flag:
            key += letter
        else:
            value += letter
    error_value: int | None = check_error(value)
    if error_value is None:
        raise ValueError(f"Invalid value for {key}: {value}")
    if key in inventory:
        inventory[key] = inventory[key] + error_value
    else:
        inventory[key] = error_value
    return inventory


def check_error(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def items_search(inventory: dict) -> bool:
    for item in inventory:
        if item == "sword":
            return True
    return False


def items_demo(inventory: dict) -> None:
    sys.stdout.write("Dictionary keys: ")
    for i, item in enumerate(inventory):
        sys.stdout.write(item)
        if i != len(inventory) - 1:
            sys.stdout.write(", ")
        else:
            sys.stdout.write("\n")
    sys.stdout.write("Dictionary values: ")
    for j, value in enumerate(inventory):
        sys.stdout.write(f"{inventory[value]}")
        if j != len(inventory) - 1:
            sys.stdout.write(", ")
        else:
            sys.stdout.write("\n")
    sys.stdout.write(f"Sample lookup- 'sword' in inventory: "
                     f"{items_search(inventory)}\n")


def items_management(inventory: dict) -> None:
    restock: list = []
    sys.stdout.write("Restock needed: ")
    for item in inventory:
        if inventory[item] < 2:
            restock.append(item)
    for i, value in enumerate(restock):
        sys.stdout.write(value)
        if i != len(restock) - 1:
            sys.stdout.write(", ")
    sys.stdout.write("\n")


def items_categories(inventory: dict) -> None:
    Moderate: dict = {}
    Scarce: dict = {}
    for item in inventory:
        if inventory[item] > 3:
            Moderate[item] = inventory[item]
        else:
            Scarce[item] = inventory[item]
    print(f"Moderate: {Moderate}")
    print(f"Scarce: {Scarce}")


def items_analysis(inventory: dict) -> None:
    total: int = 0
    for value in inventory.values():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")


def items_statistics(inventory: dict) -> None:
    list_item: list = []
    list_item = list(inventory.items())
    total: int = 0
    pourcentage: float = 0
    for nb in inventory:
        total += inventory[nb]
    list_item = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for item in list_item:
        if pourcentage <= 0 and total <= 0:
            pourcentage = 0.00
        else:
            pourcentage = (item[1] / total) * 100
        print(f"{item[0]}: {item[1]} {'units' if item[1] > 1 else 'unit'} "
              f"({pourcentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {list_item[0][0]} ({list_item[0][1]} "
          f"{'units' if list_item[0][1] > 1 else 'unit'})")
    print(f"Most abundant: {list_item[len(list_item) - 1][0]} "
          f"({list_item[len(list_item) - 1][1]} "
          f"{'units' if list_item[len(list_item) - 1][1] > 1 else 'unit'})")


def build_inventory() -> dict | None:
    inventory: dict = {}
    argument: list = sys.argv[1:]
    if len(argument) < 1:
        print("Error: you must add at least one item !")
        sys.exit()
    else:
        try:
            for arg in argument:
                parsing(arg, inventory)
            return inventory
        except ValueError:
            print("Error: Invalid format")
            return None


if __name__ == "__main__":
    inventory: dict | None = build_inventory()
    if inventory is not None:
        print("=== Inventory System Analysis ===")
        items_analysis(inventory)
        print("\n=== Inventory System Analysis ===")
        items_statistics(inventory)
        print("\n=== Item Categories ===")
        items_categories(inventory)
        print("\n=== Management Suggestions ===")
        items_management(inventory)
        print("\n=== Dictionary Properties Demo ===")
        items_demo(inventory)
