from typing import List


def construct_matrix(rows: int = 3, cols: int = 3, name: str = "Default") -> \
        List[List[int]]:
    """Generate a matrix of given dimensions.

    :param rows: The number of rows in the matrix (default is 3).
    :param cols: The number of columns in the matrix (default is 3).
    :param name: The name of the matrix (default is "Default").
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
    """Display the matrix with its name.

    :param matrix: The matrix to be displayed.
    :param name: The name of the matrix (default is "Default").
    :return: None
    """
    print(f"\nMatrix {name}:")
    for row in matrix:
        print("\t".join(map(str, row)))


def add(matrix_one: List[List[int]], matrix_two: List[List[int]]) \
        -> List[List[int]]:
    """Add two matrices and return the result.

    :param matrix_one: The first matrix to be added.
    :param matrix_two: The second matrix to be added.
    :return: The sum of the two matrices.
    """
    if len(matrix_one) != len(matrix_two) or len(matrix_one[0]) != len(
            matrix_two[0]):
        print("\nThe matrices must have the same dimensions!")
        return []

    added_matrices = []
    for i in range(len(matrix_one)):
        matrix_row = []
        for j in range(len(matrix_one[0])):
            matrix_row.append(matrix_one[i][j] + matrix_two[i][j])

        added_matrices.append(matrix_row)

    return added_matrices


def main() -> None:
    """Generate and display matrices, and compute their sum.

    :return: None
    """
    try:
        matrix_a = construct_matrix(name="A")
        display_matrix(matrix_a, "A")

        matrix_b = construct_matrix(name="B")
        display_matrix(matrix_b, "B")

        added_matrices = add(matrix_a, matrix_b)
        if added_matrices:
            display_matrix(added_matrices, "A + B")
    except ValueError:
        print("Invalid input! Please enter integers for matrix elements.")
    except KeyboardInterrupt:
        print("\n\nExiting program...")


if __name__ == "__main__":
    main()
