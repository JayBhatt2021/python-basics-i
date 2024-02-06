def main() -> None:
    """Perform basic arithmetic operations on two numbers entered by the user.

    :return: None
    """
    try:
        quarters = int(input("Enter the number of quarters: "))
        dimes = int(input("Enter the number of dimes: "))
        nickels = int(input("Enter the number of nickels: "))
        pennies = int(input("Enter the number of pennies: "))

        total_cents = 25 * quarters + 10 * dimes + 5 * nickels + pennies
        dollars = total_cents // 100
        cents = total_cents % 100

        print(f"\nYou have ${dollars}.{cents}.")
    except ValueError:
        print("The input must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
