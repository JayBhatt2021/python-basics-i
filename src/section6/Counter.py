import random


class Counter:
    """Represents a quadratic equation of the form ax^2 + bx + c = 0."""

    def __init__(self) -> None:
        """Initialize the quadratic equation with coefficients.

        :param a: Coefficient of the quadratic term (ax^2).
        :param b: Coefficient of the linear term (bx).
        :param c: Constant term in the quadratic equation.
        :return: None
        """
        self.value = 0

    def increment(self) -> None:
        """Initialize the quadratic equation with coefficients.

        :param a: Coefficient of the quadratic term (ax^2).
        :param b: Coefficient of the linear term (bx).
        :param c: Constant term in the quadratic equation.
        :return: None
        """
        self.value += 1


def main() -> None:
    """Calculate the roots of a quadratic equation.

    :return: None
    """
    heads_counter = Counter()

    for i in range(100):
        if 0 <= random.random() < 0.5:
            heads_counter.increment()

    print(f"Heads: {heads_counter.value}")
    print(f"Tails: {100 - heads_counter.value}")


if __name__ == "__main__":
    main()
