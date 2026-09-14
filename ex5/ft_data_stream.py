import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
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


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        event_choice = random.choice(event_list)
        event_list.remove(event_choice)
        yield event_choice


def main() -> None:
    for i in range(0, 1000):
        player, action = next(gen_event())
        print(f"Event {i}: Player {player} did action {action}")
    event_list = []
    for i in range(0, 10):
        event = next(gen_event())
        event_list.append(event)
    print(f"Built list of 10 events: {event_list}")
    for event_choice in consume_event(event_list):
        print(f"Got event from list: {event_choice}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
