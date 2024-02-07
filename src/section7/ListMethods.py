import random


def generate_random_list() -> list:
    """Prompt the user to enter integers for each list.

    :return: A list containing the integers entered by the user.
    """
    return [random.randint(1, 100) for _ in range(5)]


def square_list(input_list: list) -> list:
    """Prompt the user to enter integers for each list.

    :return: A list containing the integers entered by the user.
    """
    return [element ** 2 for element in input_list]


def main() -> None:
    """Generate and display a list of random numbers within a specified range.

    :return: None
    """
    random_list = generate_random_list()

    print("Original List:", random_list)
    print("Max Value:", max(random_list))
    print("Min Value:", min(random_list))
    print("Squared List:", square_list(random_list))

    random_list.reverse()
    print("Reversed List:", random_list)


if __name__ == "__main__":
    main()
