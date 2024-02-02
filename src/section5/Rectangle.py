def is_valid(length: float, width: float) -> bool:
    """Check if the given dimensions form a valid rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: True if the dimensions form a valid rectangle, False otherwise.
    """
    return length + width > 30


def area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    return length * width


def perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The perimeter of the rectangle.
    """
    return 2 * (length + width)


def main() -> None:
    """Get user input for rectangle dimensions and display area/perimeter.

    :return: None
    """
    try:
        # Gets dimensions from the user
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        if is_valid(length, width):
            # Displays calculated area and perimeter
            print(f"Area: {area(length, width)} units^2")
            print(f"Perimeter: {perimeter(length, width)} units")
        else:
            print("This is an invalid rectangle.")
    except ValueError:
        # Handles invalid input type
        print("The length/width must be a float! Exiting program...")


if __name__ == "__main__":
    main()
