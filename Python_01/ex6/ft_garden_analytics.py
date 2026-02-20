class GardenManager:
    def __init__(self) -> None:
        self.gardens = {}

    def add_plant(self, garden_name: str, plant: Plant) -> None:
        if garden_name in self.gardens:
            self.gardens[garden_name] = self.gardens[garden_name] + [plant]
            print(f"Added {plant.name} to {self.owner_name}'s Garden")
        else:
            self.gardens[garden_name] = [plant]
            print(f"Added {plant.name} to {self.owner_name}'s Garden")

class Plant:
    def __init__(self, name_plant: str, height: int, age: int) -> None:
        self.name_plant = name_plant
        self.height = height
        self.age = age

    def grow(self) -> None:
        print(f"{self.name_plant} grew 1cm")
        self.height += 1

    def get_info(self) -> str:
        return f"- {self.name_plant}: {self.height}cm, {self.age} days."

class FloweringPlant(Plant):
    def __init__(self, name_plant: str, height: int, age: int, color: str) -> None:
        super().__init__(name_plant, height, age)
        self.color = color

    def get_info(self) -> str:
        return

class PrizeFlower(FloweringPlant):
    def __init__(self, name_plant: str, height: int, age: int, color: str,
                 prize: int) -> None:
        super().__init__(name_plant, height, age, color)
        self.prize = prize

    def get_info(self) -> str:
        return


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
