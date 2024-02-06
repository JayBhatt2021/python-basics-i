def main() -> None:
    """Calculate the total value in dollars and cents based on the number of
    coins entered by the user.

    :return: None
    """
    try:
        # Gets the number of each type of coin from the user
        quarters = int(input("Enter the number of quarters: "))
        dimes = int(input("Enter the number of dimes: "))
        nickels = int(input("Enter the number of nickels: "))
        pennies = int(input("Enter the number of pennies: "))

        # Calculates the total value in cents
        total_cents = 25 * quarters + 10 * dimes + 5 * nickels + pennies

        # Converts the total cents to dollars and cents
        dollars = total_cents // 100
        cents = total_cents % 100

        # Displays the total value in dollars and cents
        print(f"\nYou have ${dollars}.{cents}.")
    except ValueError:
        print("The input must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
