import sys
import math
from typing import Any

def get_distance(gps: tuple[int, int, int]) -> float:
    gps_src: tuple = (0, 0, 0)
    calcul: float = (
        (gps[0] - gps_src[0])**2 +
        (gps[1] - gps_src[1])**2 +
        (gps[2] - gps_src[2])**2
    )
    distance: float = math.sqrt(calcul)
    return distance


def parse() -> tuple[int, int, int] | None:
    arguments: list[str] = sys.argv[1:]
    data: list = []
    gps: tuple = ()
    if len(arguments) == 1:
        for arg in arguments:
            data = data + (arg.split(","))
        try:
            for nb in data:
                gps = gps + (int(nb),)
            return gps
        except ValueError:
            print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
            print("Error parsing coordinates: invalid literal for int() "
                  "with base 10: 'abc'")
            print('''Error details- Type: ValueError, Args: ("invalid '''
                  '''literal for int() with base 10: 'abc'",)''')
            print()
        return None
    else:
        return None


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    gps_demo: tuple[int, int, int] = (10, 20, 5)
    distance: float = get_distance(gps_demo)
    print(f"Position created: {gps_demo}")
    print(f"Distance between(0, 0, 0) and {gps_demo}: {distance:.2f}")
    print()

    gps_user: tuple[int, int, int] | None = parse()
    if gps_user is not None:
        distance = get_distance(gps_user)
        print(f"Position created: {gps_user}")
        print(f"Distance between(0, 0, 0) and {gps_user}: {distance:.2f}")
        print()
    else:
        print("Invalid or incomplete coordinates.")

    x: int | Any = None
    y: int | Any = None
    z: int | Any = None
    x, y, z = gps_user
    print(f"Unpacking demonstration:\n Player at x={x}, y={y}, z={z}\n"
          "Coordinates: X=3, Y=4, Z=0")
