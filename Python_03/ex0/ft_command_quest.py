import sys


if __name__ == "__main__":
    argument: list[str] = sys.argv[1:]
    name_program: str = sys.argv[0]
    print("=== Command Quest ===")
    if len(argument) < 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        sys.exit
    elif len(argument) == 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        print(f"Argument 1: {sys.argv[1]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        i = 1
        sys.stdout.write("Program name: ")
        for letter in name_program:
            if letter == "_":
                sys.stdout.write("\\")
            sys.stdout.write(letter)
        print()
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        for arg in argument:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")
