from typing import List, Set


def get_distinct_values(num_list: List[int]) -> Set[int]:
    """Find and return the index of the largest value in the given list.

    :param num_list: A list of integers.
    :return: The index of the largest value.
    """
    if not num_list:
        raise ValueError("The input list is empty!")

    return set(num_list)


def main() -> None:
    """Get user input for a list of numbers and display the index of the largest
    value.

    :return: None
    """
    try:
        num_list = []

        # Gets user input for a list of numbers
        for i in range(10):
            num = int(input(f"Enter Number #{i + 1}: "))
            num_list.append(num)

        # Displays the index of the largest value
        print(f"\nDistinct values: {get_distinct_values(num_list)}")
    except ValueError:
        print("Invalid input! Please enter an integer. Exiting program...")


if __name__ == "__main__":
    main()
