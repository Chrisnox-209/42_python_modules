def check_temperature(temp_str) -> int | None:
    try:
        value = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if value < 0:
            print(f"Error: {value}°C is too cold for plants (min 0°C)")
            return None
        elif value > 40:
            print(f"Error: {value}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {value}°C is perfect for plants!")
            return value


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
