def main() -> None:
    """Calculate the sum of the digits in a given integer.

    :return: None
    """
    try:
        num = int(input("Enter a number: "))
        total = 0

        # Iterate through each digit in the number
        while num > 0:
            total += num % 10
            num //= 10

        print(f"Sum of digits: {total}")
    except ValueError:
        print("Input must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
