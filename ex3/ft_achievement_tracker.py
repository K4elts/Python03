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
    alice = gen_player_achievements(achievements_set)
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements(achievements_set)
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements(achievements_set)
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements(achievements_set)
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {achievements_set}\n")
    print()
    common_achiev = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common_achiev}")
    print()
    only_alice = set.difference(alice, set.union(bob, charlie, dylan))
    print(f"Only Alice has: {only_alice}")
    only_bob = set.difference(bob, set.union(alice, charlie, dylan))
    print(f"Only Bob has: {only_bob}")
    only_charlie = set.difference(charlie, set.union(alice, bob, dylan))
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = set.difference(dylan, set.union(alice, bob, charlie))
    print(f"Only Dylan has: {only_dylan}")
    print()
    missing_alice = set.difference(achievements_set, alice)
    print(f"Alice is missing: {missing_alice}")
    missing_bob = set.difference(achievements_set, bob)
    print(f"Bob is missing: {missing_bob}")
    missing_charlie = set.difference(achievements_set, charlie)
    print(f"Charlie is missing: {missing_charlie}")
    missing_dylan = set.difference(achievements_set, dylan)
    print(f"Dylan is missing: {missing_dylan}")
