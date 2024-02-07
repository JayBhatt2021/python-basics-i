def main() -> None:
    """Print a star triangle based on the number of rows specified by the user.

    :return: None
    """
    try:
        # Gets the number of rows for the star triangle from the user
        rows = int(input("Enter the number of rows for the star triangle: "))
        print()

        # Iterates over each row to print the star triangle
        for i in range(rows):
            # Prints leading spaces for each row
            print(" " * (rows - 1 - i), end="")

            # Prints stars for each row
            print("*" * (2 * i + 1))

        print()
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
