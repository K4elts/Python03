import random

achievements_set = {"Crafting Genius", "Stategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"}


def gen_player_achievements(achievements_set: set[str]) -> set[str]:
    achievement_list = set(random.sample(
                                    list(achievements_set),
                                    random.randrange(1, len(achievements_set))
                                    ))
    return achievement_list


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_1 = gen_player_achievements(achievements_set)
    print(f"Player Alice: {player_1}")
    player_2 = gen_player_achievements(achievements_set)
    print(f"Player Bob: {player_2}")
    player_3 = gen_player_achievements(achievements_set)
    print(f"Player Charlie: {player_3}")
    player_4 = gen_player_achievements(achievements_set)
    print(f"Player Dylan: {player_4}")
    print()
    print(f"All distinct achievements: {achievements_set}\n")
    print()
    common_achiev = set.intersection(player_1, player_2, player_3, player_4)
    print(f"Common achievements: {common_achiev}")
    print()
    difference_1 = set.difference(player_1, player_2, player_3, player_4)
    print(f"Only Alice has: {difference_1}")
    difference_2 = set.difference(player_2, player_1, player_3, player_4)
    print(f"Only Bob has: {difference_2}")
    difference_3 = set.difference(player_3, player_1, player_2, player_4)
    print(f"Only Charlie has: {difference_3}")
    difference_4 = set.difference(player_4, player_1, player_2, player_3)
    print(f"Only Dylan has: {difference_4}")
    print()
    missing_1 = set.difference(achievements_set, player_1)
    print(f"Alice is missing: {missing_1}")
    missing_2 = set.difference(achievements_set, player_2)
    print(f"Bob is missing: {missing_2}")
    missing_3 = set.difference(achievements_set, player_3)
    print(f"Charlie is missing: {missing_3}")
    missing_4 = set.difference(achievements_set, player_4)
    print(f"Dylan is missing: {missing_4}")
