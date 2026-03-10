from typing import Any


def list_comprehension(data: dict) -> None:
    list_name: list = []
    list_score: list = []
    list_active: list = []
    for name in data:
        list_score.append(data[name]["score"] * 2)
        if data[name]["score"] > 2000:
            list_name.append(name)
        if data[name]["active"]:
            list_active.append(name)
    print(f"High scorers (>2000): {list_name}")
    print(f"Scores doubled: {list_score}")
    print(f"Active players: {list_active}")


def dict_comprehension(data: dict) -> None:
    dict_scores: dict = {}
    dict_categories: dict = {}
    dict_achievements: dict = {}
    number_achievements: int = 0
    for name in data:
        dict_scores[name] = data[name]["score"]
        if data[name]["score"] < 2000:
            dict_categories["low"] = 1
        elif data[name]["score"] > 2200:
            dict_categories["high"] = 3
        else:
            dict_categories["medium"] = 2
        number_achievements = len(data[name]["achievements"])
        dict_achievements[name] = number_achievements

    """ dictionary sort """
    dict_sort: dict = {}
    while dict_categories:
        key_min: Any = None
        for key in dict_categories:
            if key_min is None or \
                    dict_categories[key] < dict_categories[key_min]:
                key_min = key
        dict_sort[key_min] = dict_categories[key_min]
        del dict_categories[key_min]

    print(f"Player scores: {dict_scores}")
    print(f"Score categories: {dict_sort}")
    print(f"Achievement counts: {dict_achievements}")


def set_comprehension(data) -> None:
    set_player: set = set()
    set_achievements: set = set()
    set_regions: set = set()

    for name in data:
        set_player.add(name)
        set_regions.add(data[name]["region"])
        for achievements in data[name]["achievements"]:
            set_achievements.add(achievements)
    print(f"Unique players: {sorted(set_player)}")
    print(f"Unique achievements: {set_achievements}")
    print(f"Active regions: {sorted(set_regions, reverse=True)}")


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
