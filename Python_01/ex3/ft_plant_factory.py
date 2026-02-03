class Plant:
    """
    Represents a plant with its growth characteristics.
    Attributes:
    name (str): The species or common name of the plant.
    height (int): The height of the plant in centimeters.
    age (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the plant.

        Returns:
            str: A formatted string showing the plant's details.
        """
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


plants_data: list[tuple[str, int, int]] = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]


def count_plants(plants) -> int:
    """
    Counts the number of items in a list of plant data.

    Args:
        plants (list): A list containing plant data (tuples or objects).

    Returns:
        int: The total count of plants in the list.
    """
    return len(plants)


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant(name, height, age)
        for (name, height, age) in plants_data
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(plant)
    print(f"\nTotal plants created: {count_plants(plants_data)}")
