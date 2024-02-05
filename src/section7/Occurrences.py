from typing import List


def count(num_list: List[int]) -> None:
    """Print a sandclock pattern with the specified number of rows.

    :param rows: The number of rows for the upper-half of the sandclock.
    :return: None
    """
    num_frequency = {}

    for num in num_list:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    print("\nCount:")
    for num, frequency in num_frequency.items():
        if frequency == 1:
            print(f"{num} occurred 1 time.")
        else:
            print(f"{num} occurred {frequency} times.")


def main() -> None:
    """Print a sandclock pattern.

    :return: None
    """
    try:
        num_list = []

        for i in range(10):
            num = int(input(f"Enter Number #{i + 1}: "))
            num_list.append(num)

        count(num_list)
    except ValueError:
        print("The number of rows must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
