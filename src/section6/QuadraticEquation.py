import math
from typing import Optional, Tuple


class QuadraticEquation:
    """Represents a quadratic equation of the form ax^2 + bx + c = 0."""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Initialize the quadratic equation with coefficients.

        :param a: Coefficient of the quadratic term (ax^2).
        :param b: Coefficient of the linear term (bx).
        :param c: Constant term in the quadratic equation.
        :return: None
        """
        self.a = a
        self.b = b
        self.c = c

    def calculate_roots(self) -> Tuple[Optional[float], Optional[float]]:
        """Calculate the roots of the quadratic equation.

        :return: A tuple containing the roots of the quadratic equation.
        """
        discriminant = self.calculate_discriminant()

        if discriminant < 0:
            # No real roots if the discriminant is negative
            return None, None
        elif discriminant == 0:
            # One real root if the discriminant is zero
            root = -self.b / (2 * self.a)
            return root, None
        else:
            # Two real roots if the discriminant is positive
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2

    def calculate_discriminant(self) -> float:
        """Calculate and return the discriminant of the quadratic equation.

        :return: The discriminant value.
        """
        return self.b ** 2 - 4 * self.a * self.c


def main() -> None:
    """Calculate the roots of a quadratic equation.

    :return: None
    """
    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the constant term c: "))
        quadratic_equation = QuadraticEquation(a, b, c)

        root_one, root_two = quadratic_equation.calculate_roots()

        print(f"\nRoot #1: {root_one if root_one is not None else 'Undefined'}")
        print(f"Root #2: {root_two if root_two is not None else 'Undefined'}")
    except ValueError:
        print("Coefficients must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
