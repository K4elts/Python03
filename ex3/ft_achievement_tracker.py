import random

achievements_set = {"Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"}


def gen_player_achievements(achievements_set: set[str]) -> set[str]:
    achievement_list = set(random.sample(
        list(achievements_set), random.randrange(1, len(achievements_set) + 1)
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
    print(f"Player Dylan: {dylan}\n")
    all_distinct = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}\n")
    common_achiev = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common_achiev}\n")
    only_alice = alice.difference(bob, charlie, dylan)
    print(f"Only Alice has: {only_alice}")
    only_bob = bob.difference(alice, charlie, dylan)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie.difference(alice, bob, dylan)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan.difference(alice, bob, charlie)
    print(f"Only Dylan has: {only_dylan}\n")
    missing_alice = set.difference(achievements_set, alice)
    print(f"Alice is missing: {missing_alice}")
    missing_bob = set.difference(achievements_set, bob)
    print(f"Bob is missing: {missing_bob}")
    missing_charlie = set.difference(achievements_set, charlie)
    print(f"Charlie is missing: {missing_charlie}")
    missing_dylan = set.difference(achievements_set, dylan)
    print(f"Dylan is missing: {missing_dylan}")
