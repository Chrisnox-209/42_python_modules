class Plant:
    """
    Represents a basic plant with a name, height, and age.
    Tracks its initial height to measure growth over time.
    """
    def __init__(self, name_plant: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        :param name_plant: Name of the plant.
        :param height: Current height of the plant in centimeters.
        :param age: Age of the plant in days.
        """
        self.name_plant: str = name_plant
        self.height: int = height
        self.age: int = age
        self.initial_height: int = height

    def grow(self) -> None:
        """
        Increase the plant's height by 1 cm and print a growth message.
        """
        print(f"{self.name_plant} grew 1cm")
        self.height += 1

    def get_info(self) -> str:
        """
        Return a formatted string containing plant information.

        :return: String with plant name, height, and age.
        """
        return f"- {self.name_plant}: {self.height}cm, {self.age} days."


class FloweringPlant(Plant):
    """
    Represents a flowering plant, extending the basic Plant class
    by adding a flower color attribute.
    """
    def __init__(self, name_plant: str, height: int,
                 age: int, color: str) -> None:
        """
        Initialize a FloweringPlant instance.

        :param name_plant: Name of the plant.
        :param height: Current height in centimeters.
        :param age: Age in days.
        :param color: Color of the flowers.
        """
        super().__init__(name_plant, height, age)
        self.color: str = color

    def get_info(self) -> str:
        """
        Return formatted information including flower color.

        :return: String with plant details and flower color.
        """
        return super().get_info() + f", {self.color} color"


class PrizeFlower(FloweringPlant):
    """
    Represents a special flowering plant that earns prize points.
    Extends FloweringPlant by adding a prize score.
    """
    def __init__(self, name_plant: str, height: int, age: int, color: str,
                 prize: int) -> None:
        """
        Initialize a PrizeFlower instance.

        :param name_plant: Name of the plant.
        :param height: Current height in centimeters.
        :param age: Age in days.
        :param color: Flower color.
        :param prize: Prize points awarded to this plant.
        """
        super().__init__(name_plant, height, age, color)
        self.prize: int = prize

    def get_info(self) -> str:
        """
        Return formatted information including prize points.

        :return: String with plant details, flower color, and prize points.
        """
        return super().get_info() + f", Prize points:{self.prize}"


class Garden:
    """
    Represents a garden owned by a specific person.
    A garden can contain multiple plants.
    """
    def __init__(self, owner_name: str) -> None:
        """
        Initialize a Garden instance.

        :param owner_name: Name of the garden owner.
        """
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []

    def grow_all(self) -> None:
        """
        Trigger growth for all plants in the garden.
        """
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        :param plant: A Plant (or subclass) instance to add.
        """
        self.plants += [plant]
        print(f"Added {plant.name_plant} to {self.owner_name}'s garden")


class GardenManager:
    """
    Manages multiple gardens and provides global statistics
    and network-related operations.
    """
    nb_garden: int = 0

    def __init__(self) -> None:
        """
        Initialize a GardenManager instance.
        """
        self.gardens: list[Garden] = []

    def get_garden(self, owner_name: str) -> Garden:
        """
        Retrieve a garden by its owner's name.

        :param owner_name: Name of the garden owner.
        :return: The corresponding Garden instance.
        """
        for garden in self.gardens:
            if owner_name == garden.owner_name:
                return garden

    def add_garden(self, garden: Garden) -> None:
        """
        Add a garden to the manager and increment the garden counter.

        :param garden: Garden instance to add.
        """
        self.gardens += [garden]
        GardenManager.nb_garden += 1

    @classmethod
    def create_garden_network(cls, gardens) -> None:
        """
        Calculate and display a score for each garden based on plant types.

        Scoring rules:
        - PrizeFlower: 174 points
        - FloweringPlant: 40 points
        - Plant: 4 points

        :param gardens: List of Garden instances.
        """
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
        """
        Print the total number of gardens managed.
        """
        print(f"Total gardens managed: {GardenManager.nb_garden}")

    class GardenStats:
        """
        Provides statistical analysis tools for a specific garden.
        """

        def __init__(self, garden_analysis: "Garden") -> None:
            """
            Initialize GardenStats with a garden to analyze.

            :param garden_analysis: Garden instance to analyze.
            """
            self.garden_analysis: Garden = garden_analysis

        @staticmethod
        def total_plant_growth(plants: list[Plant]) -> None:
            """
            Calculate and print the average growth of plants.

            :param plants: List of Plant instances.
            """
            sum_grow: int = 0
            nb_plants: int = 0
            for plant in plants:
                sum_grow += (plant.height - plant.initial_height)
                nb_plants += 1
            total: float = sum_grow / nb_plants
            print(f"Plants added: {nb_plants}, Total growth: {total:.0f}cm")

        def get_plant_owner(self) -> None:
            """
            Display detailed information about each plant
            in the analyzed garden.
            """
            for plant in self.garden_analysis.plants:
                if type(plant) is FloweringPlant:
                    print(f"- {plant.name_plant}: {plant.height}cm, "
                          f"{plant.color} flowers (blooming)")
                elif type(plant) is PrizeFlower:
                    print(f"- {plant.name_plant}: {plant.height}cm, "
                          f"{plant.color} flowers (blooming), "
                          f"Prize points: {plant.prize}")
                elif type(plant) is Plant:
                    print(f"- {plant.name_plant}: {plant.height}cm")

        def count_type_plant(self) -> None:
            """
            Count and display the number of each plant type
            in the analyzed garden.
            """
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

        @classmethod
        def test_height(cls, gardens) -> None:
            """
            Verify that all plants in all gardens have a
            height greater than 5 cm.

            :param gardens: List of Garden instances.
            """
            test_validation: int = 0
            nb_plant: int = 0
            for garden in gardens:
                for plant in garden.plants:
                    if plant.height > 5:
                        test_validation += 1
                    nb_plant += 1
            if nb_plant == test_validation:
                print("Height validation test: True")
            else:
                print("Height validation test: false")


"""
List of gardens managed in the system (one for Alice and one for Bob).
"""
list_gardens: list[Garden] = [Garden("Alice"), Garden("Bob")]
"""
List of plants to be added to Alice's garden, including regular,
flowering, and prize flowers.
"""
plants_alice: list[Plant] = [Plant("Oak Tree", 100, 32),
                             FloweringPlant("Rose", 25, 40, "red"),
                             PrizeFlower("Sunflower", 50, 23, "yellow", 10)
                             ]
"""
List of plants to be added to Bob's garden, including
regular and flowering plants.
"""
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
    print("Plants in garden:")
    stats_alice = GardenManager.GardenStats(instance.get_garden("Alice"))
    plants: list[Plant] = instance.get_garden("Alice").plants
    stats_alice.get_plant_owner()
    print()
    GardenManager.GardenStats.total_plant_growth(plants)
    stats_alice.count_type_plant()
    print()
    GardenManager.GardenStats.test_height(instance.gardens)
    GardenManager.create_garden_network(instance.gardens)
    instance.count_garden()
