def main() -> None:
    """Print a triangle pattern.

    :return: None
    """
    try:
        # Gets the number of rows for the triangle pattern from the user
        rows = int(input("Enter the number of rows for the triangle pattern: "))
        print()

        # Iterates through each row to print the triangle pattern
        for i in range(rows):
            # Prints leading spaces for each row
            print(" " * i, end="")

            # Prints numbers in ascending order for each row
            for j in range(1, rows + 1 - i):
                print(j, end="")

            # Moves to the next line after completing each row
            print()

        print()
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
