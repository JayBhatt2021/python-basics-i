def area(side: float) -> float:
    """Calculate the area of a square.

    :param side: The length of one side of the square.
    :return: The area of the square.
    """
    return side ** 2


def perimeter(side: float) -> float:
    """Calculate the perimeter of a square.

    :param side: The length of one side of the square.
    :return: The perimeter of the square.
    """
    return 4 * side


def main() -> None:
    """Get user input for square side length and display area and perimeter.

    :return: None
    """
    try:
        # Gets side length from the user
        side = float(input("Enter the side length of the square: "))

        print(f"\nArea: {area(side):.2f} square units")
        print(f"Perimeter: {perimeter(side):.2f} units")
    except ValueError:
        # Handles invalid input type
        print("The side length must be a float! Exiting program...")


if __name__ == "__main__":
    main()
