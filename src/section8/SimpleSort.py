from typing import List, Tuple
import random


def generate_random_list(size: int = 50, start: int = 0, end: int = 100) \
        -> List[int]:
    """Generate a list of random integers within a specified range.

    :param size: The size of the list (default is 50).
    :param start: The lower bound of the random range (default is 0).
    :param end: The upper bound of the random range (default is 100).
    :return: A list containing random integers.
    """
    return [random.randint(start, end) for _ in range(size)]


def bubble_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Perform linear search to find the target value in the list.

    :param num_list: The list of integers to search.
    :param target: The target value to search for.
    :return: The number of comparisons made during the search.
    """
    swaps = 0

    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swaps += 1

    return num_list, swaps


def insertion_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Perform linear search to find the target value in the list.

    :param num_list: The list of integers to search.
    :param target: The target value to search for.
    :return: The number of comparisons made during the search.
    """
    swaps = 0

    for position in range(1, len(num_list)):
        key = num_list[position]

        while position > 0 and key < num_list[position - 1]:
            num_list[position] = num_list[position - 1]
            position -= 1
            swaps += 1

        num_list[position] = key

    return num_list, swaps


def selection_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Perform linear search to find the target value in the list.

    :param num_list: The list of integers to search.
    :param target: The target value to search for.
    :return: The number of comparisons made during the search.
    """
    swaps = 0

    for i in range(len(num_list)):
        min_position = i

        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_position]:
                min_position = j

            if i != min_position and min_position < len(num_list):
                num_list[min_position], num_list[i] = num_list[i], num_list[
                    min_position]
                swaps += 1

    return num_list, swaps


def main() -> None:
    """Generate a list of integers, and perform linear and binary searches.

    :return: None
    """
    num_list = generate_random_list()
    print("\nList Values:", num_list)

    bubble_sorted_list, bubble_sort_swaps = bubble_sort(num_list[:])
    print(f"\nBubble Sorted Values: {bubble_sorted_list}")
    print(f"Bubble Sort Swaps: {bubble_sort_swaps}")

    insertion_sorted_list, insertion_sort_swaps = insertion_sort(num_list[:])
    print(f"\nInsertion Sorted Values: {insertion_sorted_list}")
    print(f"Insertion Sort Swaps: {insertion_sort_swaps}")

    selection_sorted_list, selection_sort_swaps = selection_sort(num_list[:])
    print(f"\nSelection Sorted Values: {selection_sorted_list}")
    print(f"Selection Sort Swaps: {selection_sort_swaps}")


if __name__ == "__main__":
    main()
