class GardenError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class WaterError(GardenError):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class HealthError(GardenError):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class Plant:
    def __init__(self, name: str, height: int, age: int, water: int,
                 sun: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.water: int = water
        self.sun: int = sun

    def get_info(self) -> str:
        return (f"name: {self.name} | height: {self.height} | "
                f"age: {self.age} | water: {self.water} | sun: {self.sun}")


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.__tank: int = 0

    def add_plant(self, plant: Plant) -> None:
        if plant.name == "":
            raise Exception("Plant name cannot be empty!")
        else:
            self.plants += [plant]
            print(f"Added {plant.name} successfully")

    def watering(self, liter: int) -> None:
        print("Opening watering system")
        for plant in self.plants:
            plant.water += liter
            if plant.water < 5:
                raise WaterError("Not enough water in the tank!")
            else:
                print(f"Watering {plant.name} - success")

    def check_health(self) -> None:
        for plant in self.plants:
            if plant.water > 10:
                raise HealthError(f"Water level {plant.water} is too high "
                                  "(max 10)", plant.name)
            elif plant.sun > 10:
                raise HealthError(f" Sun level {plant.sun} is too high "
                                  "(max 10)", plant.name)
            else:
                print(f"{plant.name}: healthy (water: {plant.water}, "
                      f"sun: {plant.sun})")

    def check_tank(self) -> None:
        if self.__tank == 0:
            raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    my_garden = GardenManager()
    list_plants: list[Plant] = [
            Plant("tomato", 30, 1, 1, 6),
            Plant("lettuce", 12, 5, 8, 10),
            Plant("", 0, 0, 0, 0)
    ]
    print("Adding plants to garden...")
    try:
        for plant in list_plants:
            my_garden.add_plant(plant)
    except Exception as error:
        print("Error adding plant:", error)

    print()
    print("Watering plants...")
    try:
        my_garden.watering(6)
    except WaterError as error:
        print("Caught WaterError:", error)
    finally:
        print("Closing watering system (cleanup)")

    print()
    print("Checking plant health...")
    try:
        my_garden.check_health()
    except HealthError as error:
        print(f"Error checking {error.args[1]}: {error.args[0]}")

    print()
    print("Testing error recovery...")
    try:
        my_garden.check_tank()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
