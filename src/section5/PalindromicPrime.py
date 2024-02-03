import math


def is_palindrome(num: int) -> bool:
    """Print a series table.

    :param n: The number of terms in the series.
    :return: None
    """
    if num < 0 or num % 10 == 0:
        return False

    original_num = num
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = 10 * reversed_num + last_digit
        num /= 10

    return original_num == reversed_num


def is_prime(num: int) -> bool:
    """Print a series table.

    :param n: The number of terms in the series.
    :return: None
    """
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def main() -> None:
    """Display a series table.

    :return: None
    """
    num = 2
    palindromic_primes = []

    while len(palindromic_primes) < 51:
        if is_palindrome(num) and is_prime(num):
            palindromic_primes.append(num)

        num += 1

    for i in range(50):
        if i + 1 % 10 == 0:
            print(palindromic_primes[i])
        else:
            print(f"{palindromic_primes[i]} ", end="")


if __name__ == "__main__":
    main()
