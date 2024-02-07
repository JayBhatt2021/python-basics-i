class Rectangle:
    """Represents a rectangle with given length and width."""

    def __init__(self, length: float = 1.0, width: float = 1.0) -> None:
        """Initialize the rectangle with length and width.

        :param length: The length of the rectangle (default is 1.0).
        :param width: The width of the rectangle (default is 1.0).
        :return: None
        """
        self.length = length
        self.width = width

    def __str__(self) -> str:
        """Return a string representation of the rectangle.

        :return: The string representation including length, width, perimeter,
                 and area.
        """
        perimeter = self.calculate_perimeter()
        area = self.calculate_area()
        return (
            f"Length: {self.length:.2f} units\nWidth: {self.width:.2f} units\n"
            f"Perimeter: {perimeter:.2f} units\nArea: {area:.2f} square units"
        )

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.length * self.width


def main() -> None:
    """Construct and print rectangles with default and custom dimensions.

    :return: None
    """
    # Constructs and prints the default rectangle
    print("Default rectangle:")
    default_rectangle = Rectangle()
    print(default_rectangle)

    # Constructs and prints a custom rectangle
    print("\nCustom rectangle:")
    custom_rectangle = Rectangle(5, 6)
    print(custom_rectangle)


if __name__ == "__main__":
    main()
