def main() -> None:
    """Construct a square pattern using a specified symbol.

    :return: None
    """
    try:
        # Gets the number of rows and the symbol from the user
        rows = int(input("Enter the number of rows for the symbol square: "))
        symbol = input("Enter the symbol to construct this square: ")

        # Checks if the symbol is a single character
        if len(symbol) != 1:
            print("The symbol must be a single character!")
            exit(1)

        # Constructs the square pattern
        print()
        for _ in range(rows):
            print(symbol * rows)
    except ValueError:
        # Handles invalid inputs
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
