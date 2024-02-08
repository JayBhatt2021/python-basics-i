from typing import List


def construct_matrix() -> List[List[int]]:
    """Generate a list representing a 3x3 matrix.

    :return: A list containing the elements of the matrix.
    """
    matrix = []

    # Inputs elements for the matrix
    print(f"\nEnter the elements for the 3x4 Matrix:")
    element_counter = 1
    for i in range(3):
        matrix_row = []

        for j in range(4):
            matrix_element = int(input(f"Element #{element_counter}: "))
            matrix_row.append(matrix_element)
            element_counter += 1

        matrix.append(matrix_row)

    # Displays the matrix
    print(f"\nThe 3x4 Matrix:")
    for i in range(3):
        for j in range(4):
            print(matrix[i][j], end="\n" if j == 3 else "\t")

    return matrix


def sum_columns(matrix: List[List[int]]) -> None:
    """Check if two matrices are equivalent.

    :param matrix_one: The first matrix.
    :param matrix_two: The second matrix.
    :return: True if the matrices are equivalent, False otherwise.
    """
    column_sums = []

    #
    for j in range(4):
        column_total = 0

        for i in range(3):
            column_total += matrix[i][j]

        column_sums.append(column_total)

    #
    print("\nMatrix Column Sums:")
    for j, column_total in enumerate(column_sums):
        print(f"The sum of column {j} is {column_total}.")


def main() -> None:
    """Generate and display two matrices, and check if they are equivalent.

    :return: None
    """
    try:
        # Gets the input matrix from the user
        matrix = construct_matrix()

        #
        sum_columns(matrix)
    except ValueError:
        # Handles invalid input type
        print("The matrix value must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
