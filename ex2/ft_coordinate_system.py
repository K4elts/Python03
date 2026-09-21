import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            coords = coordinates.split(",")
            if len(coords) != 3:
                print("Invalid syntax")
                continue
            x = float(coords[0])
            y = float(coords[1])
            z = float(coords[2])
            return x, y, z
        except ValueError:
            for c in coords:
                try:
                    float(c)
                except ValueError as e:
                    print(f"Error on parameter '{c}': {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    try:
        first_coords = get_player_pos()
        print(f"Got a first tuple: {first_coords}")
        print(f"It includes: X={first_coords[0]}, Y={first_coords[1]},",
              f"Z={first_coords[2]}")
        coord_one = (0 - first_coords[0])**2
        coord_two = (0 - first_coords[1])**2
        coord_three = (0 - first_coords[2])**2
        dist_to_center = math.sqrt(coord_one + coord_two + coord_three)
        print(f"Distance to center: {round(dist_to_center, 4)}")
        print("\nGet a second set of coordinates")
        second_coords = get_player_pos()
        coord_one = (second_coords[0] - first_coords[0])**2
        coord_two = (second_coords[1] - first_coords[1])**2
        coord_three = (second_coords[2] - first_coords[2])**2
        dist_between_coords = math.sqrt(coord_one + coord_two + coord_three)
        print("Distance between the 2 sets of coordinates:",
              f"{round(dist_between_coords, 4)}")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")
