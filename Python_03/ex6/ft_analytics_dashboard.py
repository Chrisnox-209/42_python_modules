from typing import Any


def list_comprehension(data: dict) -> None:
    list_name: list = [data[name]["score"] * 2 for name in data]
    list_score: list = [name for name in data if data[name]["score"] > 2000]
    list_active: list = [name for name in data if data[name]["active"]]
    print(f"High scorers (>2000): {list_score}")
    print(f"Scores doubled: {list_name}")
    print(f"Active players: {list_active}")


def dict_comprehension(data: dict) -> None:
    dict_scores: dict = {name: data[name]["score"] for name in data}
    dict_categories: dict = {}
    dict_achievements: dict = {name: len(data[name]["achievements"])
                               for name in data}
    for name in data:
        if data[name]["score"] < 2000:
            dict_categories["low"] = 1
        elif data[name]["score"] > 2200:
            dict_categories["high"] = 3
        else:
            dict_categories["medium"] = 2

    """ dictionary sort """
    dict_sort: dict = {}
    while dict_categories:
        key_min: Any = None
        for key in dict_categories:
            if key_min is None or \
                    dict_categories[key] > dict_categories[key_min]:
                key_min = key
        dict_sort[key_min] = dict_categories[key_min]
        del dict_categories[key_min]

    print(f"Player scores: {dict_scores}")
    print(f"Score categories: {dict_sort}")
    print(f"Achievement counts: {dict_achievements}")


def set_comprehension(data: dict) -> None:
    set_player: set = {name for name in data}
    set_regions: set = {v["region"] for v in data.values()}
    set_achievements: set = {
        achievement
        for v in data.values()
        for achievement in v["achievements"]
    }
    print(f"Unique players: {sorted(set_player)}")
    print(f"Unique achievements: {set_achievements}")
    print(f"Active regions: {sorted(set_regions, reverse=True)}")


def combined_comprehension(data: dict) -> None:
    achivements_unique: set = set()
    total_players: int = sum([1 for _ in data])
    total_score: float = 0
    max_point: int = 0
    list_performer: list = []
    for name in data:
        total_score += data[name]["score"]
        if data[name]["score"] > max_point:
            list_performer = [name, data[name]["score"],
                              len(data[name]["achievements"])]
            max_point = data[name]["score"]
        for achivements in data[name]["achievements"]:
            achivements_unique.add(achivements)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(achivements_unique)}")
    print(f"Average score: {total_score / total_players:.1f}")
    if not list_performer:
        print("No valid scores to calculate")
    else:
        point: str = ('point' if list_performer[1] <= 1 else 'points')
        achievement: str = ('achievement'
                            if list_performer[2] <= 1
                            else 'achievements'
                            )
        print(
            f"Top performer: {list_performer[0]} "
            f"({list_performer[1]} {point}, {list_performer[2]} {achievement})"
        )


if __name__ == "__main__":
    data: dict[str, dict[str, Any]] = {
        "alice": {
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ['level_10',
                             'double_kill',
                             'treasure_hunter',
                             'elite_warrior',
                             'boss_slayer']
        },
        "bob": {
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ['boss_slayer',
                             'elite_warrior',
                             'level_10']
        },
        "charlie": {
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": ['first_kill',
                             'level_10',
                             'double_kill',
                             'treasure_hunter',
                             'elite_warrior',
                             'boss_slayer',
                             'quest_master']
        },
        "diana": {
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ['first_kill']
        }
    }

    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    list_comprehension(data)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(data)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(data)
    print("\n=== Combined Analysis ===")
    combined_comprehension(data)
