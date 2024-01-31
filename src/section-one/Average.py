import sys


def main() -> None:
    """Find the minimum, maximum, and average of the user-inputted numbers.

    :return: None
    """
    minimum = sys.maxsize
    maximum = -sys.maxsize - 1
    total = 0
    count = 0

    while True:
        user_input = input('Enter a number (Type "quit" to quit.): ')
        if user_input.lower() == "quit":
            break

        try:
            num = int(user_input)

            if num < minimum:
                minimum = num

            if num > maximum:
                maximum = num

            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if count == 0:
        print("\nNo valid numbers entered.")
    else:
        print(f"\nMinimum Number: {minimum}")
        print(f"Maximum Number: {maximum}")
        print(f"Average of all numbers: {total / count}")


if __name__ == "__main__":
    main()
