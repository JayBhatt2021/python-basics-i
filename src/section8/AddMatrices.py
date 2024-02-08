from typing import List, Tuple


def construct_matrix(rows: int = 3, cols: int = 3, name: str = "Default") -> \
        List[List[int]]:
    """Generate a matrix of given dimensions and display it.

    :param rows: The number of rows in the matrix (default is 3).
    :param cols: The number of columns in the matrix (default is 3).
    :return: A list containing the elements of the matrix.
    """
    matrix = []

    # Inputs elements for the matrix
    print(f"\nEnter the elements for the {rows}x{cols} Matrix {name}:")
    for i in range(rows):
        matrix_row = []

        for j in range(cols):
            matrix_element = int(input(f"Element at [{i}][{j}]: "))
            matrix_row.append(matrix_element)

        matrix.append(matrix_row)

    return matrix


def display_matrix(matrix: List[List[int]], name: str = "Default") -> None:
    """Generate a matrix of given dimensions and display it.

    :param rows: The number of rows in the matrix (default is 3).
    :param cols: The number of columns in the matrix (default is 4).
    :return: A list containing the elements of the matrix.
    """
    print(f"\nMatrix {name}:")
    for row in matrix:
        print("\t".join(map(str, row)))


def add(matrix_one: List[List[int]], matrix_two: List[List[int]], ) -> List[
    List[int]]:
    """Locate the largest element in the matrix.

    :param matrix: The matrix to search for the largest element.
    :return: A tuple containing the row index, column index, and value of the
             largest element.
    """
    if len(matrix_one) != len(matrix_two) and len(matrix_one[0]) != len(
            matrix_two[0]):
        print("The matrices must have the same dimensions!")
        return

    added_matrices = []
    for i in range(len(matrix_one)):
        matrix_row = []
        for j in range(len(matrix_one[0])):
            matrix_row.append(0)

        added_matrices.append(matrix_row)

    for i in range(len(matrix_one)):
        for j in range(len(matrix_one[0])):
            added_matrices[i][j] = matrix_one[i][j] + matrix_two[i][j]

    return added_matrices


def main() -> None:
    """Generate and display a matrix, and locate the largest element.

    :return: None
    """
    try:
        matrix_a = construct_matrix(name="A")
        display_matrix(matrix_a, "A")

        matrix_b = construct_matrix(name="B")
        display_matrix(matrix_b, "B")

        added_matrices = add(matrix_a, matrix_b)
        display_matrix(added_matrices, "A + B")
    except ValueError:
        print("Invalid input! Please enter integers for matrix elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
