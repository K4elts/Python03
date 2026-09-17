import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            c1, c2, c3 = coordinates.split(",")
            x = float(c1)
            y = float(c2)
            z = float(c3)
            return (x, y, z)
        except ValueError:
            print("Invalid syntax")


def get_second_coords() -> tuple[float, float, float]:
    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            c1, c2, c3 = coordinates.split(",")
            x = float(c1)
            y = float(c2)
            z = float(c3)
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    try:
        first_coords = get_player_pos()
        print(f"Got a first tuple: {first_coords}")
        print(f"It includes: X={first_coords[0]}, Y={first_coords[1]},"
              f" Z={first_coords[2]}")
        dist_to_center = math.sqrt(
                                    (0 - first_coords[0])**2 +
                                    (0 - first_coords[1])**2 +
                                    (0 - first_coords[2])**2)
        print(f"Distance to center: {round(dist_to_center, 4)}")
        print("\nGet a second set of coordinates")
        second_coords = get_second_coords()
        dist_between_coords = math.sqrt(
                                    (second_coords[0] - first_coords[0])**2 +
                                    (second_coords[1] - first_coords[1])**2 +
                                    (second_coords[2] - first_coords[2])**2)
        print("Distance between the 2 sets of coordinates:",
              f"{round(dist_between_coords, 4)}")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")
