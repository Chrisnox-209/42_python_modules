from typing import Generator, Tuple, Any
import sys
import random
import time


def numbers_prime(nb: int) -> bool:
    i: int = 2
    if nb <= 1:
        return False
    if nb == 2:
        return True
    while i < nb:
        if nb % i == 0:
            return False
        i += 1
    return True


def get_number_prime(nb: int) -> Generator[int, Any, None]:
    i: int = 1
    prime: int = 2
    while i <= nb:
        if numbers_prime(prime):
            yield prime
            i += 1
        prime += 1


def game_stream(nb_game: int) -> Generator[
    Tuple[str, int, str, str],
    None,
    None
]:
    name_player: list[str] = ["alice", "bob", "charlie"]
    action: list[str] = ["killed monster", "found treasure", "leveled up"]
    print(f"Processing {nb_game} game events...\n")
    for i in range(1, nb_game + 1):
        lvl: int = random.randint(1, 21)
        nb_player: int = random.randint(0, 2)
        nb_action: int = random.randint(0, 2)
        string_event: str = (f"Event {i}: Player {name_player[nb_player]} "
                             f"(level {lvl}) {action[nb_action]}")
        yield string_event, lvl, action[nb_action], name_player[nb_player]


def stream_data(
    list_level: list,
    dict_event: dict,
    level: int,
    event: str
) -> None:
    list_level.append(level)
    if event in dict_event:
        dict_event[event] += 1
    else:
        dict_event[event] = 1


def stream_analytics(list_level: list, dict_event: dict, nb_game: int) -> None:
    count_lvl: int = 0
    for lvl in list_level:
        if lvl >= 10:
            count_lvl += 1
    print(f"Total events processed: {nb_game}")
    print(f"High-level players (10+): {count_lvl}")
    print(f"Treasure events: {dict_event.get('found treasure', 0)}")
    print(f"Level-up events: {dict_event.get('leveled up', 0)}")


def get_number_fibonacci(nb: int) -> Generator[int, Any, None]:
    f_nb: list[int] = [0, 1]

    for i in range(nb):
        if i < 2:
            yield i
        else:
            fnb: int = f_nb[0] + f_nb[1]
            f_nb[0] = f_nb[1]
            f_nb[1] = fnb
            yield fnb


if __name__ == "__main__":
    list_level: list[int] = []
    dict_event: dict[str, int] = {}
    print("=== Game Data Stream Processor ===\n")
    start_time: float = time.time()
    nb_game = 1000
    generator: Generator[Tuple[str, int, str, str], None, None] = game_stream(
        nb_game)
    for i in range(nb_game):
        string_event: str
        lvl: int
        action: str
        player: str
        string_event, lvl, action, player = next(generator)
        stream_data(list_level, dict_event, lvl, action)
        print(string_event)
    end_time: float = time.time()
    print("\n=== Stream Analytics ===")
    stream_analytics(list_level, dict_event, nb_game)
    processing_time: float = end_time - start_time
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fibonacci_digit_number: int = 10
    generator_fibonacci: Generator[int, Any, None] = get_number_fibonacci(
        fibonacci_digit_number)
    sys.stdout.write(f"Fibonacci sequence (first {fibonacci_digit_number}): ")
    for i in range(fibonacci_digit_number):
        prime: int = next(generator_fibonacci)
        sys.stdout.write(str(prime))
        if i != fibonacci_digit_number - 1:
            sys.stdout.write(", ")
    sys.stdout.write("\n")

    prime_digit_number: int = 5
    generator_prime: Generator[int, Any, None] = get_number_prime(
        prime_digit_number)
    sys.stdout.write(f"Prime numbers (first {prime_digit_number}): ")
    for i in range(prime_digit_number):
        prime = next(generator_prime)
        sys.stdout.write(str(prime))
        if i != prime_digit_number - 1:
            sys.stdout.write(", ")
    sys.stdout.write("\n")
