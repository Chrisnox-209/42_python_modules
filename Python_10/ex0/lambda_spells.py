import sys
from typing import Any


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(m["power"] for m in mages) / len(mages),
            2,
        ),
    }


if __name__ == "__main__":

    # ### data
    pourit: dict[str, Any] = {'name': "Lantern of Souls",
                              'power': 12, 'type': "B"}
    fluberg: dict[str, Any] = {'name': "Frost Shard", 'power': 40, 'type': "C"}
    emaj: dict[str, Any] = {'name': "Fire Staff", 'power': 92, 'type': "A"}
    heingstar: dict[str, Any] = {'name': "Ring of Secrets",
                                 'power': 33, 'type': "D"}
    qubrik: dict[str, Any] = {'name': "Crystal Orb", 'power': 85, 'type': "E"}

    magnus: dict[str, Any] = {'name': "Magnus Firethorn",
                              'power': 12, 'element': "water"}
    seraphin: dict[str, Any] = {'name': "Seraphin Lowell",
                                'power': 40, 'element': "fire"}
    thalor: dict[str, Any] = {'name': "Thalor Brightspell",
                              'power': 22, 'element': "earth"}
    kaelion: dict[str, Any] = {'name': "Kaelion Duskwind",
                               'power': 33, 'element': "air"}
    arkanor: dict[str, Any] = {'name': "Arkanor Virel",
                               'power': 85, 'element': "water"}

    artifacts: list[dict[str, Any]] = [pourit, fluberg, emaj,
                                       heingstar, qubrik]
    mages: list[dict[str, Any]] = [magnus, seraphin, thalor, kaelion, arkanor]
    spells: list[str] = ["fireball", "heal", "shield"]
    # ### data

    print("Testing artifact sorter...")
    sorted_artifacts: list[dict] = artifact_sorter(artifacts)
    for i, artifact in enumerate(sorted_artifacts):
        sys.stdout.write(f"{artifact['name']} ({artifact['power']} power) ")
        if len(sorted_artifacts) - 1 != i:
            sys.stdout.write("comes before ")
    sys.stdout.write("\n")

    print("\nTesting power filter...")
    power = 33
    mages_filter: list[dict] = power_filter(mages, power)
    for mage in mages_filter:
        sys.stdout.write(f"- {mage['name']}: {mage['power']} power\n")

    print("\nTesting spell transformer...")
    spells_transformer: list[str] = spell_transformer(spells)
    for spell in spells_transformer:
        sys.stdout.write(f"{spell} ")
    sys.stdout.write("\n")

    print("\nTesting mage stats...")
    stats: dict = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Average Power: {stats['avg_power']}")
