def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if plant_name == "":
        raise Exception("Error: Plant name cannot be empty!")
    elif water_level < 1:
        raise Exception(f"Error: Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise Exception(f"Error: Water level {water_level} is "
                        "too high (max 10)")
    elif sunlight_hours < 2:
        raise Exception(f"Error: Sunlight hours {sunlight_hours} is "
                        "too low (min 2)")
    elif sunlight_hours > 12:
        raise Exception(f"Error: Sunlight hours {sunlight_hours} is "
                        "too high (max 12)")
    else:
        return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 5))
    except Exception as error:
        print(error)
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 5))
    except Exception as error:
        print(error)
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 5))
    except Exception as error:
        print(error)
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except Exception as error:
        print(error)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
