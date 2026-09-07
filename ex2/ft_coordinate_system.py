import math


def get_player_pos():
    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            x, y, z = coordinates.split(",")
            x = float(x)
            y = float(y)
            z = float(z)
            return (x, y, z)
        except ValueError:
            print("Invalid syntax")


def get_second_coords():
    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            x, y, z = coordinates.split(",")
            x = float(x)
            y = float(y)
            z = float(z)
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    first_coords = get_player_pos()
    print(f"Got a first tuple: {first_coords}")
    print(f"It includes: X={first_coords[0]}, Y={first_coords[1]},"
          f" Z={first_coords[2]}")
    dist_to_center = math.sqrt(
                                   (0 - first_coords[0])**2 +
                                   (0 - first_coords[1])**2 +
                                   (0 - first_coords[2])**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print("Get a second set of coordinates")
    second_coords = get_second_coords()
    dist_between_coords = math.sqrt(
                                   (second_coords[0] - first_coords[0])**2 +
                                   (second_coords[1] - first_coords[1])**2 +
                                   (second_coords[2] - first_coords[2])**2)
    print("Distance between the 2 sets of coordinates:",
          f"{round(dist_between_coords, 4)}")
