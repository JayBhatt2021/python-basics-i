import math


class QuadraticEquation:
    """"""

    def __init__(self, a: float, b, c) -> None:
        """Check if a number is a palindrome.

        :param num: The number to check.
        :return: True if the number is a palindrome, False otherwise.
        """
        self.a = a
        self.b = b
        self.discriminant = b ** 2 - 4 * a * c

    def calculate_first_root(self):
        """Check if a number is a palindrome.

        :param num: The number to check.
        :return: True if the number is a palindrome, False otherwise.
        """
        if self.discriminant < 0:
            return None

        return (-self.b + math.sqrt(self.discriminant)) / 2 * self.a

    def calculate_second_root(self):
        """Check if a number is a palindrome.

        :param num: The number to check.
        :return: True if the number is a palindrome, False otherwise.
        """
        if self.discriminant <= 0:
            return None

        return (-self.b - math.sqrt(self.discriminant)) / 2 * self.a


def main() -> None:
    """Calculate the relationship between two circles based on their centers
    and radii.

    :return: None
    """
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        quadratic_equation = QuadraticEquation(a, b, c)

        root_one = quadratic_equation.calculate_first_root()
        root_two = quadratic_equation.calculate_second_root()

        print(f"\nRoot #1: {root_one if root_one is not None else 'Undefined'}")
        print(f"Root #2: {root_two if root_two is not None else 'Undefined'}")
    except ValueError:
        print("Inputs must be floats! Exiting program...")


if __name__ == "__main__":
    main()
