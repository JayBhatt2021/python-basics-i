def calculate_taxes_due(annual_income: float) -> tuple:
    """Calculate taxes due based on different income brackets.

    :param annual_income: The annual income of the individual.
    :return: A tuple containing tax percent and taxes due.
    """
    if annual_income <= 50_000:
        tax_percent, taxes_due = 5, (0.05 * annual_income)
    elif 50_000 < annual_income <= 200_000:
        tax_percent, taxes_due = 10, (0.10 * (annual_income - 50_000) + 2_500)
    elif 200_000 < annual_income <= 400_000:
        tax_percent, taxes_due = 15, (0.15 * (annual_income - 200_000) + 17_500)
    elif 400_000 < annual_income <= 900_000:
        tax_percent, taxes_due = 25, (0.25 * (annual_income - 400_000) + 47_500)
    else:
        tax_percent, taxes_due = 35, (
                0.35 * (annual_income - 900_000) + 172_500
        )

    return tax_percent, taxes_due


def main() -> None:
    """Calculate the relationship between annual income, tax bracket, and taxes
    due.

    :return: None
    """
    try:
        # Gets the annual income from the user
        annual_income = float(input("Enter the annual income (in dollars): "))

        # Calculates tax based on income
        tax_percent, taxes_due = calculate_taxes_due(annual_income)

        # Prints the calculated tax information
        print(f"\nTax bracket: {tax_percent}%")
        print(f"Taxes due: ${taxes_due:.2f}")
    except ValueError:
        # Handles the case where the input is not a valid float
        print("The annual income must be a float! Exiting program...")


if __name__ == "__main__":
    main()
