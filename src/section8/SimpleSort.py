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
    """Sort a list using bubble sort algorithm.

    :param num_list: The list of integers to be sorted.
    :return: A tuple containing the sorted list and the number of swaps
             performed.
    """
    n = len(num_list)
    swaps = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swaps += 1

    return num_list, swaps


def insertion_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Sort a list using insertion sort algorithm.

    :param num_list: The list of integers to be sorted.
    :return: A tuple containing the sorted list and the number of swaps
             performed.
    """
    n = len(num_list)
    swaps = 0

    for i in range(1, n):
        temp = num_list[i]
        j = i - 1

        while j >= 0 and temp < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
            swaps += 1

        num_list[j + 1] = temp
        swaps += 1

    return num_list, swaps


def selection_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Sort a list using selection sort algorithm.

    :param num_list: The list of integers to be sorted.
    :return: A tuple containing the sorted list and the number of swaps
             performed.
    """
    n = len(num_list)
    swaps = 0

    for i in range(n - 1):
        pos_smallest = i
        for j in range(i + 1, n):
            if num_list[j] < num_list[pos_smallest]:
                pos_smallest = j

        num_list[i], num_list[pos_smallest] = (
            num_list[pos_smallest], num_list[i]
        )
        swaps += 1

    return num_list, swaps


def main() -> None:
    """Generate a list of integers, and perform bubble, insertion, and selection
    sorts.

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
