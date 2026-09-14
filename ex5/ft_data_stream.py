import typing
import random


def gen_event() -> typing.Generator:
    player_list = ["alice",
                   "bob",
                   "charlie",
                   "dylan"
                   ]
    action_list = ["run",
                   "eat",
                   "sleep",
                   "grab",
                   "move",
                   "climb",
                   "swim",
                   "use",
                   "release"
                   ]
    while True:
        player = random.choice(player_list)
        action = random.choice(action_list)
        yield player, action


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(0, 1000 + 1):
        player, action = next(gen_event())
        print(f"Event {i}: Player {player} did action {action}")
    event_list = []
    for i in range(0, 10):
        player, event = next(gen_event())
        event_list.append((player, event))
    print(f"Built list of 10 events: {event_list}")
    for i in range(0, 10):
        event_choice = random.choice(event_list)
        print(f"Got event from list: {event_choice}")
        event_list.remove(event_choice)
        print(f"Remains in list: {event_list}")
