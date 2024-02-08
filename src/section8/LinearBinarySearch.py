from typing import List


def construct_num_list(size: int = 10) -> List[int]:
    """Generate a list of integers of given size.

    :param size: The size of the list (default is 10).
    :return: A list containing the integers entered by the user.
    """
    num_list = []

    print(f"\nEnter the elements for the number list of size {size}:")
    for i in range(1, size + 1):
        num = int(input(f"Element #{i}: "))
        num_list.append(num)

    return num_list


def linear_search(num_list: List[int], target: int) -> int:
    """Perform linear search to find the target value in the list.

    :param num_list: The list of integers to search.
    :param target: The target value to search for.
    :return: The number of comparisons made during the search.
    """
    comparisons = 0

    for num in num_list:
        comparisons += 1

        if num == target:
            break

    return comparisons


def binary_search(num_list: List[int], target: int) -> int:
    """Perform binary search to find the target value in the sorted list.

    :param num_list: The sorted list of integers to search.
    :param target: The target value to search for.
    :return: The number of comparisons made during the search.
    """
    start = 0
    end = len(num_list) - 1
    comparisons = 0

    while start <= end:
        middle = (start + end) // 2
        comparisons += 1

        if num_list[middle] == target:
            break
        elif num_list[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return comparisons


def main() -> None:
    """Generate a list of integers, and perform linear and binary searches.

    :return: None
    """
    try:
        num_list = construct_num_list()
        target = int(input("\nEnter the target value: "))

        print("\nList Values:", num_list)
        print("Target Value:", target)

        linear_comparisons = linear_search(num_list, target)
        print(f"\nLinear Search Comparisons: {linear_comparisons}")

        num_list.sort()
        binary_comparisons = binary_search(num_list, target)
        print(f"Binary Search Comparisons: {binary_comparisons}")
    except ValueError:
        print("Invalid input! Please enter integers for list elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
