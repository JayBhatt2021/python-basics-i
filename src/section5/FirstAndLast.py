from typing import List, Tuple


def get_first_and_last_integers(num_list: List[int]) -> Tuple[int, int]:
    """Return the first and last integers from a list.

    :param num_list: The list of integers.
    :return: A tuple containing the first and last integers.
    """
    if not num_list:
        raise ValueError("The list of integers must not be empty.")

    return num_list[0], num_list[-1]


def main() -> None:
    """Get user input for a list of integers and display the first and last
    integers.

    :return: None
    """
    try:
        num_list = []

        # Gets integers from the user
        print("Keep entering integers. Enter '0' to stop entering integers.")
        while True:
            num = int(input("Enter an integer: "))

            # Breaks loop if input is 0
            if not num:
                break

            num_list.append(num)

        # Checks if the list is empty
        if not num_list:
            print("The list of integers must not be empty!")
            exit(1)

        # Gets the first and last integers from the list
        first, last = get_first_and_last_integers(num_list)
        print(f"\nThe first integer entered is {first}.")
        print(f"The last integer entered is {last}.")
    except ValueError:
        # Handles invalid input type
        print("The input must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
