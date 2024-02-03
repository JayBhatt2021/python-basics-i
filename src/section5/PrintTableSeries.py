def print_series_table(n: int) -> None:
    """Print a series table.

    :param n: The number of terms in the series.
    :return: None
    """
    print("\ni\tsum(i)")

    total = 0
    for i in range(1, n):
        total += i / (i + 1)
        print(f"{i}\t{total:.4f}")

    print()


def main() -> None:
    """Display a series table.

    :return: None
    """
    try:
        n = int(input("Enter the value for n: "))
        print_series_table(n)
    except ValueError:
        print("The value of n must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
