def main() -> None:
    """Print a triangle pattern.

    :return: None
    """
    try:
        rows = int(input("Enter the number of rows for the triangle pattern: "))
        print()

        for i in range(rows):
            print(" " * i, end="")
            for j in range(1, rows + 1 - i):
                print(j, end="")
            print()

        print()
    except ValueError:
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
