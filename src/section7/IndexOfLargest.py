from typing import List


def find_largest_index(num_list: List[int]) -> int:
    """Find and return the index of the largest value in the given list.

    :param num_list: A list of integers.
    :return: The index of the largest value.
    """
    if not num_list:
        raise ValueError("The input list is empty!")

    largest_index, largest_value = max(enumerate(num_list), key=lambda x: x[1])
    return largest_index


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
        print(
            f"\nThe index of the largest value is "
            f"{find_largest_index(num_list)}."
        )
    except ValueError:
        print("Invalid input! Please enter an integer. Exiting program...")


if __name__ == "__main__":
    main()
