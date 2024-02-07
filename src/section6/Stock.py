class Stock:
    """Represents a stock with a name, symbol, and price information."""

    def __init__(self, name: str, symbol: str) -> None:
        """Initialize a stock with a name and symbol.

        :param name: The name of the stock.
        :param symbol: The symbol of the stock.
        """
        self.name = name
        self.symbol = symbol
        self.previous_closing_price = 0.0
        self.current_price = 0.0

    def __str__(self) -> str:
        """Return a string representation of the stock.

        :return: A string containing stock information.
        """
        change_percent = self.calculate_change_percent()
        return (
            f"{self.name} Stock\nSymbol: {self.symbol}\nClosing Price: "
            f"${self.previous_closing_price:.2f}\nCurrent Price: $"
            f"{self.current_price:.2f}\nChange Percent: {change_percent:.2f}%"
        )

    def calculate_change_percent(self) -> float:
        """Calculate the percentage change between previous and current prices.

        :return: The percentage change in price.
        """
        return ((self.current_price - self.previous_closing_price) /
                self.previous_closing_price * 100)


def main() -> None:
    """Create and display information for Google and Microsoft stocks.

    :return: None
    """
    # Google stock information
    google_stock = Stock("Google", "GOOG")
    google_stock.previous_closing_price = 134.67
    google_stock.current_price = 131.98
    print(f"{google_stock}\n")

    # Microsoft stock information
    microsoft_stock = Stock("Microsoft", "MSFT")
    microsoft_stock.previous_closing_price = 156.52
    microsoft_stock.current_price = 161.22
    print(microsoft_stock)


if __name__ == "__main__":
    main()
