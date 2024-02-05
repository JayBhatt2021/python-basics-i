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


def simulate_coin_flips(num_flips: int) -> None:
    """Simulate coin flips and count the number of heads and tails.

    :param num_flips: The number of coin flips to simulate.
    :return: None
    """
    heads_counter = Counter()

    for _ in range(num_flips):
        if random.random() < 0.5:
            heads_counter.increment()

    print(f"Heads: {heads_counter.value}")
    print(f"Tails: {num_flips - heads_counter.value}")


def main() -> None:
    """Simulate 100 coin flips and count the number of heads and tails."""
    simulate_coin_flips(100)


if __name__ == "__main__":
    main()
