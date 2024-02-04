import random


class Counter:
    """A simple counter for tracking occurrences."""

    def __init__(self) -> None:
        """Initialize the counter.

        :return: None
        """
        self.value = 0

    def increment(self) -> None:
        """Increment the counter.

        :return: None
        """
        self.value += 1


def main() -> None:
    """Simulate 100 coin flips and count the number of heads and tails.

    :return: None
    """
    heads_counter = Counter()

    for _ in range(100):
        if random.random() < 0.5:
            heads_counter.increment()

    print(f"Heads: {heads_counter.value}")
    print(f"Tails: {100 - heads_counter.value}")


if __name__ == "__main__":
    main()
