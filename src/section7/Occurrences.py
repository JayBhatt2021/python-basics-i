from typing import List


def count(num_list: List[int]) -> None:
    """Print the count of occurrences for each number in the given list.

    :param num_list: A list of integers.
    :return: None
    """
    num_frequency = {}

    # Counts the occurrences of each number
    for num in num_list:
        num_frequency[num] = num_frequency.get(num, 0) + 1

    # Displays the count for each number
    print("\nCounts:")
    for num, frequency in num_frequency.items():
        occurrence_str = "time" if frequency == 1 else "times"
        print(f"{num} occurred {frequency} {occurrence_str}.")


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

        # Displays the count of occurrences
        count(num_list)
    except ValueError:
        print("Invalid input! Please enter an integer. Exiting program...")


if __name__ == "__main__":
    main()
