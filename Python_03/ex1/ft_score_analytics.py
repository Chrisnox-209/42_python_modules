import sys


def check_digit(arguments: list) -> bool:
    for arg in arguments:
        try:
            arg = int(arg)
        except ValueError:
            print(f"oops, I typed ’{arg}’ instead of ’1000’")
            return False
    return True


def statistics(scores: list) -> None:
    i: int = 0
    min: int = scores[0]
    max: int = 0
    total: int = 0
    for nb in scores:
        if nb < min:
            min = nb
        if nb > max:
            max = nb
        total += nb
        i += 1
    print(f"Total players: {i}")
    print(f"Total score: {total}")
    print(f"Average score: {total/i}")
    print(f"High score: {max}")
    print(f"Low score: {min}")
    print(f"Score range: {max - min}")
    return


def leaderboard() -> None:
    scores: list = []
    arguments: list[str] = sys.argv[1:]
    if len(arguments) < 1:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        sys.exit()
        return
    else:
        if check_digit(arguments):
            for arg in arguments:
                scores.append(int(arg))
            print(f"Scores processed: {scores}")
            statistics(scores)
        return


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    leaderboard()
