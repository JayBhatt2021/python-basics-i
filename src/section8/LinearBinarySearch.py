from typing import List


def construct_num_list(size: int = 10) -> List[int]:
    """Generate a matrix of given dimensions.

    :param rows: The number of rows in the matrix (default is 3).
    :param cols: The number of columns in the matrix (default is 3).
    :param name: The name of the matrix (default is "Default").
    :return: A list containing the elements of the matrix.
    """
    num_list = []

    print(f"\nEnter the elements for the number list of size {size}:")
    for i in range(1, size + 1):
        num = int(input(f"Element #{i}: "))
        num_list.append(num)

    return num_list


def linear_search(num_list: List[int], target: int) -> None:
    """Add two matrices and return the result.

    :param matrix_one: The first matrix to be added.
    :param matrix_two: The second matrix to be added.
    :return: The sum of the two matrices.
    """
    comparisons = 0

    for num in num_list:
        comparisons += 1

        if num == target:
            break

    print(f"\nLinear Search Comparisons: {comparisons}")


def binary_search(num_list: List[int], target: int) -> None:
    """Add two matrices and return the result.

    :param matrix_one: The first matrix to be added.
    :param matrix_two: The second matrix to be added.
    :return: The sum of the two matrices.
    """
    start = 0
    end = len(num_list)
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

    print(f"Binary Search Comparisons: {comparisons}")


def main() -> None:
    """Generate and display matrices, and compute their sum.

    :return: None
    """
    try:
        num_list = construct_num_list()
        target = int(input("\nEnter the target value: "))

        print("\nList Values:", num_list)
        print("Target Value:", target)

        linear_search(num_list, target)

        num_list.sort()
        binary_search(num_list, target)
    except ValueError:
        print("Invalid input! Please enter integers for list elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
