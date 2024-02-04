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
        self.discriminant = b ** 2 - 4 * a * c

    def calculate_roots(self) -> Tuple[Optional[float], Optional[float]]:
        """Calculate the roots of the quadratic equation.

        :return: A tuple containing the roots of the quadratic equation.
        """
        if self.discriminant < 0:
            return None, None
        elif self.discriminant == 0:
            root = -self.b / (2 * self.a)
            return root, None
        else:
            root1 = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(self.discriminant)) / (2 * self.a)
            return root1, root2


def main() -> None:
    """Calculate the roots of a quadratic equation.

    :return: None
    """
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        quadratic_equation = QuadraticEquation(a, b, c)

        root_one, root_two = quadratic_equation.calculate_roots()

        print(f"\nRoot #1: {root_one if root_one is not None else 'Undefined'}")
        print(f"Root #2: {root_two if root_two is not None else 'Undefined'}")
    except ValueError:
        print("Inputs must be floats! Exiting program...")


if __name__ == "__main__":
    main()
