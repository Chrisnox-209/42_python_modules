def water_plants(plant_list) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant is None:
            raise Exception("Error: Cannot water None - invalid plant!")
        else:
            print(f"Watering {plant}")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
    except Exception as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    print()

    try:
        print("Testing with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
