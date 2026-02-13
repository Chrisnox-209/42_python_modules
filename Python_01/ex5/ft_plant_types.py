class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        return f"{self.name} ({self.__class__.__name__}): {self.height}cm, " \
               f"{self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        if self.age > 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming!")

    def get_info(self) -> None:
        return super().get_info() + f", {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade: int = self.trunk_diameter * 0.25
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = nutritional_value


plants_data: list[tuple[str, int, int]] = [
    (Flower, "Rose", 25, 30, "red"),
    (Tree, "Oak", 667, 2563, 62),
    (Vegetable, "Tomato", 60, 90, "spring", "vitami C"),
]


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants: list = [plant[0](*plant[1:]) for plant in plants_data]
    for plant in plants:
        print()
        print(plant.get_info())
        if plant.__class__.__name__ == "Tree":
            plant.produce_shade()
        elif plant.__class__.__name__ == "Flower":
            plant.bloom()
