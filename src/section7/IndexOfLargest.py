from typing import List


def find_index(num_list: List[int]) -> None:
    """Print the count of occurrences for each number in the given list.

    :param num_list: A list of integers.
    :return: None
    """
    largest_index, largest = 0, num_list[0]

    for i, num in enumerate(num_list, start=1):
        if num > largest:
            largest_index, largest = i, num

    return largest_index


def main() -> None:
    """Get user input for a list of numbers and display the count of
    occurrences.

    :return: None
    """
    try:
        num_list = []

        # Gets user input for a list of numbers
        for i in range(10):
            num = int(input(f"Enter Number #{i + 1}: "))
            num_list.append(num)

        # Gets user input for a list of numbers
        print(f"\nThe index of the largest value is {find_index(num_list)}.")
    except ValueError:
        print("Invalid input! Please enter an integer. Exiting program...")


if __name__ == "__main__":
    main()
