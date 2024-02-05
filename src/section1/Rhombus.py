def print_rhombus(rows: int) -> None:
    """Print a rhombus pattern.

    :param rows: The number of rows for the upper-half of the rhombus.
    :return: None
    """
    # Prints the upper half of the rhombus
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)

    # Prints the lower half of the rhombus
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)


def main() -> None:
    """Get user input for the number of rows and print a rhombus pattern.

    :return: None
    """
    try:
        # Gets the number of rows for the rhombus pattern from the user
        rows = int(input("Enter the number of rows for the rhombus: "))
        print()
        print_rhombus(rows)
        print()
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
