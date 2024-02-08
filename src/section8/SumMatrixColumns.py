from typing import List


def construct_matrix(rows: int = 3, cols: int = 4) -> List[List[int]]:
    """Generate a list representing a matrix of given dimensions.

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


def sum_columns(matrix: List[List[int]]) -> None:
    """Calculate and display the sum of each column in the matrix.

    :param matrix: The matrix for which to calculate column sums.
    :return: None
    """
    column_sums = [sum(column) for column in zip(*matrix)]

    print("\nMatrix Column Sums:")
    for j, column_total in enumerate(column_sums):
        print(f"The sum of column {j} is {column_total}.")


def main() -> None:
    """Generate and display a matrix, and calculate column sums.

    :return: None
    """
    try:
        matrix = construct_matrix()
        sum_columns(matrix)
    except ValueError:
        print("Invalid input! Please enter integers for matrix elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
