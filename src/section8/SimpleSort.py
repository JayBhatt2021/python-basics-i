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

    # Iterates through the list
    for i in range(n - 1):
        # Iterates through the unsorted part of the list
        for j in range(n - 1 - i):
            # If the current element is greater than the next element
            if num_list[j] > num_list[j + 1]:
                # 1) Swap the elements
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

                # 2) Increment the swaps counter
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

    # Iterates through the list starting from the second element
    for i in range(1, n):
        # Stores the current element to be inserted
        key = num_list[i]

        # Sets the initial index to the element before the current one
        j = i - 1

        # Moves elements of num_list[0...i-1] that are greater than key to one
        # position ahead of their current position
        while j >= 0 and num_list[j] > key:
            # Shifts the element to the right
            num_list[j + 1] = num_list[j]

            # Moves to the previous index
            j -= 1

            # Increments the swaps counter
            swaps += 1

        # Inserts the stored key at its correct position
        num_list[j + 1] = key

    return num_list, swaps


def selection_sort(num_list: List[int]) -> Tuple[List[int], int]:
    """Sort a list using selection sort algorithm.

    :param num_list: The list of integers to be sorted.
    :return: A tuple containing the sorted list and the number of swaps
             performed.
    """
    n = len(num_list)
    swaps = 0

    # Iterates through the list
    for i in range(n - 1):
        # Assumes the current index has the smallest element
        min_idx = i

        # Iterates through the unsorted part of the list to find the smallest
        # element
        for j in range(i + 1, n):
            # Checks if the current element is smaller than the assumed minimum
            if num_list[j] < num_list[min_idx]:
                # Updates the index of the smallest element found so far
                min_idx = j

        # If the smallest element is not at its correct position, swap it with
        # the element at the current index
        if min_idx != i:
            # Swaps the elements
            num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

            # Increments the swaps counter
            swaps += 1

    return num_list, swaps


def main() -> None:
    """Generate a list of integers, and perform bubble, insertion, and selection
    sorts.

    :return: None
    """
    # Generates a list of random integers
    num_list = generate_random_list()
    print("\nList Values:", num_list)

    # Performs bubble sort and prints results
    bubble_sorted_list, bubble_sort_swaps = bubble_sort(num_list[:])
    print(f"\nBubble Sorted Values: {bubble_sorted_list}")
    print(f"Bubble Sort Swaps: {bubble_sort_swaps}")

    # Performs insertion sort and prints results
    insertion_sorted_list, insertion_sort_swaps = insertion_sort(num_list[:])
    print(f"\nInsertion Sorted Values: {insertion_sorted_list}")
    print(f"Insertion Sort Swaps: {insertion_sort_swaps}")

    # Performs selection sort and prints results
    selection_sorted_list, selection_sort_swaps = selection_sort(num_list[:])
    print(f"\nSelection Sorted Values: {selection_sorted_list}")
    print(f"Selection Sort Swaps: {selection_sort_swaps}")


if __name__ == "__main__":
    main()
