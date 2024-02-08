from typing import List, Tuple


def construct_matrix(rows: int = 3, cols: int = 4) -> List[List[int]]:
    """Generate a matrix of given dimensions and display it.

    :param rows: The number of rows in the matrix (default is 3).
    :param cols: The number of columns in the matrix (default is 4).
    :return: A list containing the elements of the matrix.
    """
    matrix = []

    # Inputs elements for the matrix
    print(f"\nEnter the elements for the {rows}x{cols} Matrix:")
    for i in range(rows):
        matrix_row = []

        for j in range(cols):
            matrix_element = int(input(f"Element at [{i}][{j}]: "))
            matrix_row.append(matrix_element)

        matrix.append(matrix_row)

    # Displays the matrix
    print(f"\nThe {rows}x{cols} Matrix:")
    for row in matrix:
        print("\t".join(map(str, row)))

    return matrix


def locate_largest(matrix: List[List[int]]) -> Tuple[int, int, int]:
    """Locate the largest element in the matrix.

    :param matrix: The matrix to search for the largest element.
    :return: A tuple containing the row index, column index, and value of the
             largest element.
    """
    largest_i, largest_j, largest_element = 0, 0, matrix[0][0]

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > largest_element:
                largest_i, largest_j, largest_element = i, j, value

    return largest_i, largest_j, largest_element


def main() -> None:
    """Generate and display a matrix, and locate the largest element.

    :return: None
    """
    try:
        matrix = construct_matrix()

        largest_i, largest_j, largest_element = locate_largest(matrix)
        print(
            f"\nThe first largest value ({largest_element}) is located at row "
            f"{largest_i} and column {largest_j}."
        )
    except ValueError:
        print("Invalid input! Please enter integers for matrix elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
