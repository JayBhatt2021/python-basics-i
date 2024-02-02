import sys


def main() -> None:
    """Print the largest integer and its occurrences in a list.

    :return: None
    """
    try:
        # Gets a space-separated string of integers from the user
        int_str = input("Enter integers: ")

        # Converts the input string to a list of integers
        int_list = [int(num) for num in int_str.split()]

        # Initializes variables to track the largest integer and its occurrences
        largest = -sys.maxsize - 1
        int_frequency = {}

        # Iterates through the list of integers
        for num in int_list:
            # Updates the largest integer if the current number is greater
            if num > largest:
                largest = num

            # Updates the frequency count for each integer
            int_frequency[num] = int_frequency.get(num, 0) + 1

        # Prints the results
        print(f"\nLargest integer: {largest}")
        print(f"Occurrences: {int_frequency[largest]} times")

    except ValueError:
        # Handles the case where the input is not a valid list of integers
        print("The input can ONLY have integers and spaces! Exiting program...")


if __name__ == "__main__":
    main()
