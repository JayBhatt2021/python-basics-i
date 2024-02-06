import random


def main() -> None:
    """Generate and display a list of random numbers within a specified range.

    :return: None
    """
    # Specifies the range of numbers and count
    start = 1
    end = 50
    count = 10

    # Generates and displays the list of random numbers
    print("Random numbers:", [random.randint(start, end) for _ in range(count)])


if __name__ == "__main__":
    main()
