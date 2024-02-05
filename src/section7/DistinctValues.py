from typing import List, Set


def get_distinct_values(num_list: List[int]) -> Set[int]:
    """Find and return the set of distinct values in the given list.

    :param num_list: A list of integers.
    :return: A set containing distinct values.
    """
    return set(num_list)


def main() -> None:
    """Get user input for a list of numbers and display the set of distinct
    values.

    :return: None
    """
    try:
        # Gets user input for a list of numbers
        num_list = [int(input(f"Enter Number #{i + 1}: ")) for i in range(10)]

        # Displays the set of distinct values
        distinct_values = get_distinct_values(num_list)
        print(f"\nDistinct values: {distinct_values}")
    except ValueError:
        print("Invalid input! Please enter an integer. Exiting program...")


if __name__ == "__main__":
    main()
