import random


def generate_random_list(size: int = 5, start: int = 1, end: int = 100) -> list:
    """Generate a list of random integers within a specified range.

    :param size: The size of the list (default is 5).
    :param start: The lower bound of the random range (default is 1).
    :param end: The upper bound of the random range (default is 100).
    :return: A list containing random integers.
    """
    return [random.randint(start, end) for _ in range(size)]


def square_list(input_list: list) -> list:
    """Square each element of the input list.

    :param input_list: The list to be squared.
    :return: A list containing the squared elements.
    """
    return [element ** 2 for element in input_list]


def main() -> None:
    """Generate a random list, perform operations, and display results.

    :return: None
    """
    random_list = generate_random_list()
    print("Original List:", random_list)
    print("Max Value:", max(random_list))
    print("Min Value:", min(random_list))

    squared_list = square_list(random_list)
    print("Squared List:", squared_list)

    reversed_squared_list = list(reversed(squared_list))
    print("Reversed Squared List:", reversed_squared_list)


if __name__ == "__main__":
    main()
