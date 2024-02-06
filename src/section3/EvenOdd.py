def main() -> None:
    """Calculate and display even and odd numbers within a specified range.

    :return: None
    """
    # Specifies the range of numbers
    start = 50
    end = 100

    # Calculates and displays even numbers
    print(f"Even numbers in [{start}, {end}]:")
    print([num for num in range(start, end + 1) if num % 2 == 0])

    # Calculates and displays odd numbers
    print(f"\nOdd numbers in [{start}, {end}]:")
    print([num for num in range(start, end + 1) if num % 2 == 1])


if __name__ == "__main__":
    main()
