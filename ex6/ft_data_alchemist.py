import random

if __name__ == '__main__':
    print("=== Game Data Alchemist ===")
    player_list = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
                   "john", "kevin", "Liam"]
    print(f"\nInitial list of players {player_list}")
    full_cap_list = [name.capitalize() for name in player_list]
    print(f"New list with all names capitalized: {full_cap_list}")
    only_cap_list = [name for name in player_list if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_cap_list}")
    score_dict = {name: random.randint(1, 1000) for name in full_cap_list}
    print(f"Score dict: {score_dict}")
    result = 0
    for score in score_dict.values():
        result += score
    result = score / len(score_dict)
    print(f"Score average is {round(result, 2)}")
    print(score)
