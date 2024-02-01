def main() -> None:
    """Calculate the sales tax and total price based on the entered prices.

    :return: None
    """
    try:
        burger_price = float(input("Enter the burger price: "))
        fries_price = float(input("Enter the fries price: "))
        drink_price = float(input("Enter the drink price: "))

        # Calculates the sales tax and total price
        sales_tax = 0.1 * (burger_price + fries_price + drink_price)
        total_price = burger_price + fries_price + drink_price + sales_tax

        # Displays the results with proper formatting
        print(f"\nSales tax: ${sales_tax:.2f}")
        print(f"Total price: ${total_price:.2f}")
    except ValueError:
        print("Prices must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
