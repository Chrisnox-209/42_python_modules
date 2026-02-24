class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
    
    def check_name(self):
        if self.name == "":
            raise Exception("Error adding plant: Plant name cannot be empty!")

    def get_info(self) -> str:
        return (f"name: {self.name}, height: {self.height}, age: {self.age}")


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} successfully")


def test_garden_management() -> None:
    print("test_garden_management()\n")
    
    print("Adding plants to garden...")
    my_garden = GardenManager()

    try:
        plant_01 = Plant("tomato", 30, 1) 
        my_garden.add_plant(plant_01)
    except Exception as error:
        print(error)

    try:
        plant_02 = Plant("", 20, 1)
        my_garden.add_plant(plant_02)
    except Exception as error:
        print(error)
        
        
    

if __name__ == "__main__":
    test_garden_management()


