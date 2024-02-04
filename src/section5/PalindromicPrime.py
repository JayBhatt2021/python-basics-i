import math


def is_palindrome(num: int) -> bool:
    """Check if a number is a palindrome.

    :param num: The number to check.
    :return: True if the number is a palindrome, False otherwise.
    """
    # Checks for negative number or numbers ending in zero (excluding zero)
    if num < 0 or (num != 0 and num % 10 == 0):
        return False

    original_num, reversed_num = num, 0
    # Reverses the number using integer division by 10
    while num > 0:
        last_digit = num % 10
        reversed_num = 10 * reversed_num + last_digit
        num //= 10

    return original_num == reversed_num


def is_prime(num: int) -> bool:
    """Check if a number is prime.

    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    # Numbers less than or equal to 1 are not prime.
    if num <= 1:
        return False

    # Checks for factors up to the square root of the number
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False

    return True


def main() -> None:
    """Display the first 50 palindromic prime numbers.

    :return: None
    """
    num = 2
    palindromic_primes = []

    # Finds and stores palindromic prime numbers
    while len(palindromic_primes) < 50:
        if is_palindrome(num) and is_prime(num):
            palindromic_primes.append(num)

        num += 1

    # Prints the palindromic prime numbers in a tabular format
    for i, prime in enumerate(palindromic_primes, start=1):
        print(f"{prime}\t", end="" if i % 10 else "\n")


if __name__ == "__main__":
    main()
