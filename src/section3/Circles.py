import math


def main() -> None:
    """Calculate the relationship between two circles based on their centers
    and radii.

    :return: None
    """
    try:
        x1 = float(input("Enter the x-value of the center of Circle 1: "))
        y1 = float(input("Enter the y-value of the center of Circle 1: "))
        radius_1 = float(input("Enter the radius of Circle 1: "))
        x2 = float(input("Enter the x-value of the center of Circle 2: "))
        y2 = float(input("Enter the y-value of the center of Circle 2: "))
        radius_2 = float(input("Enter the radius of Circle 2: "))

        # Calculates the distance between the centers of Circles 1 and 2
        center_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if center_distance < abs(radius_2 - radius_1):
            print("\nCircle 2 is completely inside Circle 1.")
        elif center_distance > radius_1 + radius_2:
            print("\nCircle 2 is completely outside Circle 1.")
        else:
            print("\nCircle 2 is overlapping Circle 1.")
    except ValueError:
        print("Inputs must be floats! Exiting program...")


if __name__ == "__main__":
    main()
