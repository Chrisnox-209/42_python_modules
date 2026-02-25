def garden_operations() -> None:

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        dictionary: dict[str, str | int] = {
            "type": "plant",
            "name": "rose",
            "age": 28
        }
        print(dictionary["_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
        open("missing.txt")
        dictionary_2: dict[str, str | int] = {
            "type": "plant",
            "name": "rose",
            "age": 28
        }
        print(dictionary_2["_plant"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
