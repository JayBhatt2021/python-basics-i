def main() -> None:
    """Calculate and display miles per gallon based on user input.

    :return: None
    """
    try:
        miles = float(input("Enter the miles traveled: "))
        gallons = float(input("Enter the gallons used: "))

        if gallons == 0:
            print("Gallons must be greater than zero!")
        else:
            print(f"\nMiles per gallon: {miles / gallons:.2f}")
    except ValueError:
        print("Inputs must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
