class Plant:
    """
    Represents a plant with a name, height, and age in days.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age_day (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age_day: int) -> None:
        """
        Initializes a new Plant instance with the given name, height, and age.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age_day (int): The initial age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self._age_day: int = age_day

    def grow(self) -> None:
        """
        Increases the height of the plant by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increases the age of the plant by 1 day.
        """
        self._age_day += 1

    def get_info(self) -> None:
        """
        Prints the current state of the plant, including its name,
        height, and age.
        """
        print(f"{self.name}: {self.height}cm, {self._age_day} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    base_age: int = rose._age_day
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose._age_day - base_age}cm")
