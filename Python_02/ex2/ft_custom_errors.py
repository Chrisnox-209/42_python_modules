class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def watering(self, liter: int) -> str:
        self.liter: int = liter
        if self.liter < 5:
            raise WaterError("Not enough water in the tank!")
        else:
            return f"{self.liter} added to the tank"

    def check_age(self) -> str:
        if self.age > 30:
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            return f"The {self.name} is in great shape"

    def get_info(self) -> str:
        return f"name: {self.name}: | size: {self.height}cm " \
               f"| age: {self.age} days"


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    my_plant = Plant("tomato", 25, 35)

    print("Testing PlantError...")
    try:
        print(my_plant.check_age())
    except PlantError as error:
        print("Caught PlantError:", error)
    print()
    print("Testing WaterError...")
    try:
        print(my_plant.watering(3))
    except WaterError as error:
        print("Caught WaterError:", error)
    print()
    print("Testing catching all garden errors...")
    try:
        print(my_plant.check_age())
    except GardenError as error:
        print("Caught a garden error:", error)
    try:
        print(my_plant.watering(3))
    except GardenError as error:
        print("Caught a garden error:", error)
    print()
    print("All custom error types work correctly!")
