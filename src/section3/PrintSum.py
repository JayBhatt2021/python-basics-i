def main() -> None:
    """Calculate the sum of integers between 1 and n, inclusive.

    :return: None
    """
    try:
        # Gets the value of n from the user
        n = int(input("Enter the value of n ([1, infinity)): "))

        # Checks if the input is valid
        if n < 1:
            print("The value of n must be greater than or equal to 1!")
            exit(1)

        # Calculates the sum of integers between 1 and n
        sum_of_integers = (n * (n + 1)) // 2
        print(f"\nThe sum of integers between 1 and {n} is {sum_of_integers}.")
    except ValueError:
        # Handles invalid inputs
        print("The value of n must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
