import math


class Circle:
    """Represents a rectangle with given length and width."""

    def __init__(self, radius: float = 1.0) -> None:
        """Initialize the rectangle with length and width.

        :param length: The length of the rectangle (default is 1.0).
        :param width: The width of the rectangle (default is 1.0).
        :return: None
        """
        self.radius = radius

    def __str__(self) -> str:
        """Return a string representation of the rectangle.

        :return: The string representation including length, width, perimeter,
                 and area.
        """
        circumference = self.calculate_circumference()
        area = self.calculate_area()
        return (
            f"Radius: {self.radius:.2f} unit(s)\nCircumference: "
            f"{circumference:.2f} unit(s)\nArea: {area:.2f} "
            f"square unit(s)"
        )

    def calculate_circumference(self) -> float:
        """Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        return 2 * math.pi * self.radius

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle.

        :return: The area of the rectangle.
        """
        return math.pi * self.radius ** 2


def main() -> None:
    """Construct and print rectangles with default and custom dimensions.

    :return: None
    """
    # Constructs and prints the default circle
    print("Default circle:")
    circle = Circle()
    print(circle)

    # Sets the radius to 10 and prints the modified circle
    print("\nModified default circle:")
    circle.radius = 10
    print(circle)


if __name__ == "__main__":
    main()
