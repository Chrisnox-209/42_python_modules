class Plant:
    def __init__(self, name_plant: str, height: int, age: int) -> None:
        self.name_plant: str = name_plant
        self.height: int = height
        self.age: int = age
        self.initial_height: int = height

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


class Garden:
    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []

    def grow_all(self) -> None:
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name_plant} to {self.owner_name}'s garden")


class GardenManager:
    nb_garden: int = 0

    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def get_garden(self, owner_name: str) -> Garden:
        for garden in self.gardens:
            if owner_name == garden.owner_name:
                return garden

    def add_garden(self, garden: Garden) -> None:
        self.gardens += [garden]
        GardenManager.nb_garden += 1

    @classmethod
    def create_garden_network(cls, gardens) -> None:
        scores: list = []
        print("Garden scores - ", end="")
        for i, garden in enumerate(gardens):
            score = 0
            for plant in garden.plants:
                if type(plant) is PrizeFlower:
                    score += 174
                elif type(plant) is FloweringPlant:
                    score += 40
                elif type(plant) is Plant:
                    score += 4
            for score in scores:
                garden.owner_name, scores
            print(f"{garden.owner_name}: {score}", end="")
            if i < len(gardens) - 1:
                print(", ", end="")
        print()

    @classmethod
    def count_garden(cls) -> None:
        print(f"Total gardens managed: {GardenManager.nb_garden}")

    class GardenStats:
        def __init__(self, garden_analysis: "Garden") -> None:
            self.garden_analysis: Garden = garden_analysis

        @staticmethod
        def total_plant_growth(plants: list[Plant]) -> None:
            sum_grow: int = 0
            nb_plants: int = 0
            for plant in plants:
                sum_grow += (plant.height - plant.initial_height)
                nb_plants += 1
            total: float = sum_grow / nb_plants
            print(f"Plants added: {nb_plants}, Total growth: {total:.0f}cm")

        def get_plant_owner(self) -> None:
            for plant in self.garden_analysis.plants:
                if type(plant) is FloweringPlant:
                    print(f"- {plant.name_plant}: {plant.height}cm, {plant.color} flowers (blooming)")
                elif type(plant) is PrizeFlower:
                    print(f"- {plant.name_plant}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.prize}")
                elif type(plant) is Plant:
                    print(f"- {plant.name_plant}: {plant.height}cm")


        def count_type_plant(self) -> None:
            total_prizeflower: int = 0
            total_floweringplant: int = 0
            total_plant: int = 0
            for plant in self.garden_analysis.plants:
                if type(plant) is PrizeFlower:
                    total_prizeflower += 1
                elif type(plant) is FloweringPlant:
                    total_floweringplant += 1
                elif type(plant) is Plant:
                    total_plant += 1
            print(f"Plant types: {total_plant} regular, {total_floweringplant}"
                  f" flowering, {total_prizeflower} prize flowers")


list_gardens: list[Garden] = [Garden("Alice"), Garden("Bob")]
plants_alice: list[Plant] = [Plant("Oak Tree", 100, 32),
                             FloweringPlant("Rose", 25, 40, "red"),
                             PrizeFlower("Sunflower", 50, 23, "yellow", 10)
                             ]
plants_bob: list[Plant] = [FloweringPlant("Tulip", 25, 7, "purple"),
                           FloweringPlant("Daisy", 5, 3, "White"),
                           Plant("cactus", 60, 17),
                           Plant("Lily", 32, 24),
                           Plant("palm", 120, 82)
                           ]

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    instance = GardenManager()
    for list_garden in list_gardens:
        instance.add_garden(list_garden)
    for plant_alice in plants_alice:
        instance.get_garden("Alice").add_plant(plant_alice)
    print()
    for plant_bob in plants_bob:
        instance.get_garden("Bob").add_plant(plant_bob)

    for i in range(1):
        for garden in instance.gardens:
            garden.grow_all()

    print("\n=== Alice's Garden Report ===")
    
    stats_alice = GardenManager.GardenStats(instance.get_garden("Alice"))
    plants: list[Plant] = instance.get_garden("Alice").plants
    GardenManager.GardenStats.total_plant_growth(plants)
    stats_alice.count_type_plant()
    stats_alice.get_plant_owner()
    instance.count_garden()
    GardenManager.create_garden_network(instance.gardens)
