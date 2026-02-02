class Plant:
    """
    Represents a plant with a name, height, and age.
    Attributes:
    name (str): Plant name.
    height (int): Plant height (e.g., in centimeters).
    age (int): Plant age (e.g., in years).
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant instance with the given name, height,
        and age.
        Args:
            name (str): Name of the plant.
            height (int): Initial height of the plant in centimeters.
            age (int): Initial age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def display_class(name: str, height: int, age: int) -> None:
    """
    Creates a Plant object with the specified parameters and
    prints its information.
    Args:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.

    Prints:
        The plant's name, height, and age in a formatted string.
    """
    my_plant = Plant(name, height, age)
    print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    display_class("Rose", 25, 30)
    display_class("Sunflower", 80, 45)
    display_class("Cactus", 15, 120)
