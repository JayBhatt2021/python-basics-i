def main() -> None:
    """Calculate the sum of even integers between 2 and n, inclusive.

    :return: None
    """
    try:
        # Gets the value of n from the user
        n = int(input("Enter the value of n (>= 2): "))

        # Checks if the input is valid
        if n < 2:
            print("The value of n must be greater than or equal to 2!")
            exit(1)

        # Calculates the sum of even integers between 2 and n
        even_sum = sum(num for num in range(2, n + 1, 2))
        print(f"\nThe sum of even integers between 2 and {n} is {even_sum}.")
    except ValueError:
        # Handles invalid inputs
        print("The value of n must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
