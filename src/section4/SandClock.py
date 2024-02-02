def print_sandclock(rows: int) -> None:
    """Print a sandclock pattern with the specified number of rows.

    :param rows: The number of rows for the upper-half of the sandclock.
    :return: None
    """
    # Prints the upper half of the sandclock
    for i in range(rows):
        spaces = " " * i
        asterisks = "*" * (2 * (rows - i) - 1)
        print(spaces + asterisks + spaces)

    # Prints the lower half of the sandclock
    for i in range(rows - 2, -1, -1):
        spaces = " " * i
        asterisks = "*" * (2 * (rows - i) - 1)
        print(spaces + asterisks + spaces)


def main() -> None:
    """Print a sandclock pattern.

    :return: None
    """
    try:
        rows = int(input("Enter the number of rows for the sandclock: "))
        print()
        print_sandclock(rows)
        print()
    except ValueError:
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
