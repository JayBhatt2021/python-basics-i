def is_palindrome(number: int) -> bool:
    """Check if a given number is a palindrome.

    :param number: The number to check for palindrome.
    :return: True if the number is a palindrome, False otherwise.
    """
    if number < 0 or (number != 0 and number % 10 == 0):
        return False

    original_number, reversed_number = number, 0

    while original_number > 0:
        last_digit = original_number % 10
        reversed_number = 10 * reversed_number + last_digit
        original_number //= 10

    return number == reversed_number


def main() -> None:
    """Check if the given number is a palindrome.

    :return: None
    """
    try:
        num = int(input("Enter a number: "))

        if is_palindrome(num):
            print("\nPalindrome!")
        else:
            print("\nNot a palindrome!")
    except ValueError:
        print("The input must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
