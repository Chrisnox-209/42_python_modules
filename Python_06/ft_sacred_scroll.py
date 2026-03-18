import alchemy
from typing import Any


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    element_list: list = [
        "fire",
        "water",
        "earth",
        "air"
        ]

    print("Testing direct module access:")
    for element in element_list:
        fonction_name_direct: str = f"create_{element}"
        try:
            function_direct: Any = getattr(
                alchemy.elements,
                fonction_name_direct
                )
            print(f"alchemy.elements.create_{element}(): {function_direct()}")
        except AttributeError:
            print(f"{element}: AttributeError- not exposed")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    for element in element_list:
        fonction_name_package: str = f"create_{element}"
        try:
            function_package: Any = getattr(alchemy, fonction_name_package)
            print(f"alchemy.elements.create_{element}(): {function_package()}")
        except AttributeError:
            print(f"alchemy.create_{element}(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
