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
        self.age_day: int = age_day

    def grow(self) -> None:
        """
        Increases the height of the plant by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increases the age of the plant by 1 day.
        """
        self.age_day += 1

    def get_info(self) -> str:
        """
        Prints the current state of the plant, including its name,
        height, and age.
        """
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")


if __name__ == "__main__":
    jardin: list = []
    day: int = 6
    my_plant1 = Plant("Rose", 25, 30)
    my_plant2 = Plant("Pavot", 22, 28)
    my_plant3 = Plant("Chanvre", 15, 17)
    my_plant4 = Plant("Chanvre", 15, 17)
    jardin.append(my_plant1)
    jardin.append(my_plant2)
    jardin.append(my_plant3)
    jardin.append(my_plant4)
    print("=== Day 1 ===")
    for my_plant in jardin:
        my_plant.get_info()
    for i in range(day):
        for my_plant in jardin:
            my_plant.grow()
            my_plant.age()
    print("=== Day 7 ===")
    for my_plant in jardin:
        my_plant.get_info()
