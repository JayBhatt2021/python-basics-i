def main() -> None:
    """Calculate and print gross earnings based on hours worked.

    :return: None
    """
    try:
        # Gets the number of hours worked from the user
        hours = int(input("Enter the hours: "))

        # Calculates gross earnings
        gross_earning = (hours - 40) * 15 + 400 if hours > 40 else hours * 10

        # Prints gross earnings
        print(f"\nGross earning: ${gross_earning:.2f}")
    except ValueError:
        print("The input must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
