class Rectangle:
    """Represents a quadratic equation of the form ax^2 + bx + c = 0."""

    def __init__(self, length: float = 1.0, width: float = 1.0) -> None:
        """Initialize the quadratic equation with coefficients.

        :param a: Coefficient of the quadratic term (ax^2).
        :param b: Coefficient of the linear term (bx).
        :param c: Constant term in the quadratic equation.
        :return: None
        """
        self.length = length
        self.width = width

    def __str__(self) -> str:
        """

        :return:
        """
        return (
            f"Length: {self.length:.2f} units\nWidth: {self.width:.2f} units\n"
            f"Perimeter: {self.calculate_perimeter()} units\nArea: "
            f"{self.calculate_area()} square units"
        )

    def calculate_perimeter(self) -> float:
        """Calculate the roots of the quadratic equation.

        :return: A tuple containing the roots of the quadratic equation.
        """
        return 2 * (self.length + self.width)

    def calculate_area(self) -> float:
        """Calculate and return the discriminant of the quadratic equation.

        :return: The discriminant value.
        """
        return self.length * self.width


def main() -> None:
    """Calculate the roots of a quadratic equation.

    :return: None
    """
    # Constructs and prints the default rectangle
    print("Default rectangle:")
    default_rectangle = Rectangle()
    print(default_rectangle)

    # Constructs and prints an overloaded rectangle
    print("\nOverloaded rectangle:")
    overloaded_rectangle = Rectangle(5, 6)
    print(overloaded_rectangle)


if __name__ == "__main__":
    main()
