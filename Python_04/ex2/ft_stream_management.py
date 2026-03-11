import sys


def standard_error() -> bool:
    sys.stderr.write("[ALERT] System diagnostic: Communication "
                     "channels verified\n")
    return True


def standard_output(id: str, status: str) -> bool:
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
    if standard_error():
        sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
    return True


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    id: str = input("Input Stream active. Enter archivist ID: ")
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status: str = sys.stdin.readline().rstrip()
    print()
    if standard_output(id, status):
        print("\nThree-channel communication test successful.")
