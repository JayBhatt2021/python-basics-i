import math


class Circle:
    """Represents a circle with a given radius."""

    def __init__(self, radius: float = 1.0) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        self.radius = radius

    def __str__(self) -> str:
        """Return a string representation of the circle.

        :return: A string containing circle information.
        """
        circumference = self.calculate_circumference()
        area = self.calculate_area()
        return (
            f"Radius: {self.radius:.2f} unit(s)\n"
            f"Circumference: {circumference:.2f} unit(s)\n"
            f"Area: {area:.2f} square unit(s)"
        )

    def calculate_circumference(self) -> float:
        """Calculate the circumference of the circle.

        :return: The circumference of the circle.
        """
        return 2 * math.pi * self.radius

    def calculate_area(self) -> float:
        """Calculate the area of the circle.

        :return: The area of the circle.
        """
        return math.pi * self.radius ** 2


def main() -> None:
    """Create and display information for a circle with the default and modified
    radius.

    :return: None
    """
    # Creates and prints the default circle
    print("Default circle:")
    default_circle = Circle()
    print(default_circle)

    # Modifies the radius and prints the modified circle
    print("\nModified default circle:")
    default_circle.radius = 10
    print(default_circle)


if __name__ == "__main__":
    main()
