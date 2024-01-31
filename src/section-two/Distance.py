import math


def main() -> None:
    """Calculate the distance between two points in a 2D plane.

    :return: None
    """
    try:
        x1 = float(input("Enter X1: "))
        x2 = float(input("Enter X2: "))
        y1 = float(input("Enter Y1: "))
        y2 = float(input("Enter Y2: "))

        # Calculates the distance with the formula:
        # D = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print(f"\nDistance: {distance:.2f} units")
    except ValueError:
        print("Inputs must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
