class Stock:
    """Represents a rectangle with given length and width."""

    def __init__(self, name: str, symbol: str) -> None:
        """Initialize the rectangle with length and width.

        :param length: The length of the rectangle (default is 1.0).
        :param width: The width of the rectangle (default is 1.0).
        :return: None
        """
        self.name = name
        self.symbol = symbol
        self.previous_closing_price = 0.0
        self.current_price = 0.0

    def __str__(self) -> str:
        """Return a string representation of the rectangle.

        :return: The string representation including length, width, perimeter,
                 and area.
        """
        change_percent = self.calculate_change_percent()
        return (
            f"{self.name} stock\nSymbol: {self.symbol}\nClosing price: "
            f"${self.previous_closing_price:.2f}\nCurrent price: $"
            f"{self.current_price:.2f}\nChange percent: {change_percent:.2f}%"
        )

    def calculate_change_percent(self) -> float:
        """Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        return (
                self.current_price - self.previous_closing_price) / self.current_price * 100


def main() -> None:
    """Construct and print rectangles with default and custom dimensions.

    :return: None
    """
    # Constructs and prints the Google stock
    google_stock = Stock("Google", "GOG")
    google_stock.previous_closing_price = 134.67
    google_stock.current_price = 131.98

    print(f"{google_stock}\n")

    # Constructs and prints the Microsoft stock
    microsoft_stock = Stock("Microsoft", "MSF")
    microsoft_stock.previous_closing_price = 156.52
    microsoft_stock.current_price = 161.22

    print(microsoft_stock)


if __name__ == "__main__":
    main()
