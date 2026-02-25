class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """
        Return a formatted string containing basic information about the plant.

        Returns:
            str: A string describing the plant's name, type, height, and age.
        """
        return f"{self.name} ({self.__class__.__name__}): {self.height}cm, " \
               f"{self.age} days"


class Flower(Plant):
    """
    A class representing a flower, which is a type of Plant.

    Attributes:
        color (str): The color of the flower.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): The name of the flower.
            height (int): The height of the flower in centimeters.
            age (int): The age of the flower in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """
        Print a message indicating whether the flower is blooming.

        A flower blooms if its age is greater than 20 days.
        """
        if self.age > 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming!")

    def get_info(self) -> str:
        """
        Return a formatted string containing detailed information about
        the flower.

        Returns:
            str: A string describing the flower including its color.
        """
        return super().get_info() + f", {self.color} color"


class Tree(Plant):
    """
    A class representing a tree, which is a type of Plant.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk
        in centimeters.
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): The name of the tree.
            height (int): The height of the tree in centimeters.
            age (int): The age of the tree in days.
            trunk_diameter (int): The diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and print the amount of shade produced by the tree.

        The shade area is estimated as 25% of the trunk diameter.
        """
        shade: float = self.trunk_diameter * 0.25
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        """
        Return a formatted string containing detailed information about
        the tree.

        Returns:
            str: A string describing the tree including its trunk diameter.
        """
        return super().get_info() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """
    A class representing a vegetable, which is a type of Plant.

    Attributes:
        harvest_season (str): The season during which the vegetable
        is harvested.
        nutritional_value (str): The main nutritional benefit of the vegetable.
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            height (int): The height of the vegetable in centimeters.
            age (int): The age of the vegetable in days.
            harvest_season (str): The harvest season.
            nutritional_value (str): The main nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        """
        Return a formatted string containing detailed information
        about the vegetable.

        Returns:
            str: A string describing the vegetable including its harvest season
            and nutritional value.
        """
        info: str = super().get_info() + f", {self.harvest_season} harvest\n"
        info += f"{self.name} is a rich in {self.nutritional_value}"
        return info


plants_data: list[tuple[object, ...]] = [
    (Flower, "Rose", 25, 30, "red"),
    (Tree, "Oak", 500, 1825, 50),
    (Vegetable, "Tomato", 80, 90, "summer", "vitamin C"),
]


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants: list = [data[0](*data[1:]) for data in plants_data]
    for plant in plants:
        print()
        print(plant.get_info())
        if plant.__class__.__name__ == "Tree":
            plant.produce_shade()
        elif plant.__class__.__name__ == "Flower":
            plant.bloom()
