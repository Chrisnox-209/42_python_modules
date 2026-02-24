class Plant:
    def __init__(self, name_plant: str, height: int, age: int) -> None:
        self.name_plant: str = name_plant
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        print(f"{self.name_plant} grew 1cm")
        self.height += 1

    def get_info(self) -> str:
        return f"- {self.name_plant}: {self.height}cm, {self.age} days."


class FloweringPlant(Plant):
    def __init__(self, name_plant: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name_plant, height, age)
        self.color: str = color

    def get_info(self) -> str:
        return super().get_info() + f", {self.color} color"


class PrizeFlower(FloweringPlant):
    def __init__(self, name_plant: str, height: int, age: int, color: str,
                 prize: int) -> None:
        super().__init__(name_plant, height, age, color)
        self.prize: int = prize

    def get_info(self) -> str:
        return super().get_info() + f", Prize points:{self.prize}"


class GardenManager:
    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list = []

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name_plant} to {self.owner_name}'s garden")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    gardener_1 = GardenManager("Alice")
    gardener_2 = GardenManager("Bob")
    plant_1 = Plant("Oak Tree", 100, 32)
    plant_2 = Plant("Rose", 25, 40)
    plant_3 = Plant("Sunflower", 50, 23)
    gardener_1.add_plant(plant_1)
    gardener_1.add_plant(plant_2)
    gardener_1.add_plant(plant_3)
    print("\nAlice is helping all plants grow...")
    plant_1.grow()
    plant_2.grow()
    plant_3.grow()
    print("\n=== Alice's Garden Report ===")
