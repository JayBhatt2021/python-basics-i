def main() -> None:
    """Determine the quadrant or axis where a point lies based on its
    coordinates.

    :return: None
    """
    try:
        # Gets the coordinates from the user
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))

        # Checks if the point lies on the origin or axis
        if x == 0 and y == 0:
            print("(0, 0) is on the origin.")
        elif x == 0:
            print(f"({x}, {y}) is on the y-axis.")
        elif y == 0:
            print(f"({x}, {y}) is on the x-axis.")

        # Determines the quadrant where the point lies
        if x > 0 and y > 0:
            print(f"({x}, {y}) is in the first quadrant.")
        elif x < 0 < y:
            print(f"({x}, {y}) is in the second quadrant.")
        elif x < 0 and y < 0:
            print(f"({x}, {y}) is in the third quadrant.")
        elif y < 0 < x:
            print(f"({x}, {y}) is in the fourth quadrant.")
    except ValueError:
        # Handles invalid inputs
        print("Invalid input! Coordinates must be integers. Exiting program...")


if __name__ == "__main__":
    main()
