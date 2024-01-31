def main() -> None:
    """Calculate sales tax and total price based on entered prices.

    :return: None
    """
    try:
        burger_price = float(input("Enter the burger price: "))
        fries_price = float(input("Enter the fries price: "))
        drink_price = float(input("Enter the drink price: "))
        tax_rate = 0.1

        # Calculate sales tax and total price
        sales_tax = tax_rate * (burger_price + fries_price + drink_price)
        total_price = burger_price + fries_price + drink_price + sales_tax

        # Display results with proper formatting
        print(f"Sales tax: ${sales_tax:.2f}")
        print(f"Total price: ${total_price:.2f}")

    except ValueError:
        print("Prices must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
