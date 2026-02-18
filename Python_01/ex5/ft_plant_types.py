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

    def bloom(self) -> str:
        if self.age > 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming!")

    def get_info(self) -> str:
        return super().get_info() + f", {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade: int = self.trunk_diameter * 0.25
        print(f"{self.name} provides {shade} square meters of shade")
    
    def get_info(self) -> str:
        return super().get_info() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        info: str =  super().get_info() + f", {self.harvest_season} harvest\n"
        info += f"{self.name} is a rich in {self.nutritional_value}"
        return info
    

plants_data: list[tuple[str, int, int]] = [
    (Flower, "Rose", 25, 30, "red"),
    (Tree, "Oak", 500, 1825, 50),
    (Vegetable, "Tomato", 80, 90, "summer", "vitamin C"),
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
