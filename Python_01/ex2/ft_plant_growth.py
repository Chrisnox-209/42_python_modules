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
        Initializes a new Plant instance.
        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def display_one_day(name: str, height: int, age: int) -> None:
    """
    Creates a Plant object with the given parameters and prints its
    current state.
    Args:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.

    Prints:
        The plant's name, height, and age.
    """
    my_plant = Plant(name, height, age)
    print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")


def display_seven_day(name: str, height: int, age: int) -> None:
    """
    Creates a Plant object with the given parameters, simulates 7 days of
    growth, and prints the updated state.
    Growth assumptions:
        - Height increases by 6 cm over 7 days.
        - Age increases by 6 days.
    Args:
        name (str): Name of the plant.
        height (int): Initial height of the plant in centimeters.
        age (int): Initial age of the plant in days.
    Prints:
        The plant's name, height, and age after 7 days.
    """
    my_plant = Plant(name, height, age)
    my_plant.height = height + 6
    my_plant.age = age + 6
    print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")


if __name__ == "__main__":
    display_one_day("Rose", 25, 30)
    display_seven_day("Rose", 25, 30)
