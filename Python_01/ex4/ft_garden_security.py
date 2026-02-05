class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        print(f"Plant created: {name}")
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, new_height) -> None:
        if -1 < new_height:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print("Invalid operation attempted: height"
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, set_age) -> None:
        if -1 < set_age:
            self.__age = set_age
            print(f"age updated: {set_age}cm [OK]")
        else:
            print("Invalid operation attempted: age"
                  f"{set_age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self) -> str:
        print(f"Current plant: {self.name} ({self.__height}cm, {self.__age} "
              "days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    my_plant: SecurePlant = SecurePlant("Rose", 25, 30)
    print()
    my_plant.set_height(-5)
    print()
    my_plant.get_info()
