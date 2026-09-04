import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for args in range(1, len(sys.argv)):
        try:
            score: float = float(sys.argv[args])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: {sys.argv[args]}")
    if not scores:
        print(f"No scores provided. Usage python3 {sys.argv[0]} <score1>"
              " <score2> ...")
    else:
        total_players: int = len(scores)
        total_score: float = sum(scores)
        average_score: float = total_score / total_players
        high_score: float = max(scores)
        low_score: float = min(scores)
        score_range: float = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {round(total_score), 2}")
        print(f"Average score: {round(average_score, 2)}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
