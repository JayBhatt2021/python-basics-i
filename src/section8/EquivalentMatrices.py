from typing import List


def construct_matrix(matrix_name: str) -> List[int]:
    """Generate a list representing a 3x3 matrix.

    :param matrix_name: The name of the matrix.
    :return: A list containing the elements of the matrix.
    """
    matrix = []

    # Inputs elements for the matrix
    print(f"\nEnter the elements for the 3x3 Matrix {matrix_name}:")
    for i in range(1, 10):
        matrix_element = int(input(f"Element #{i}: "))
        matrix.append(matrix_element)

    # Displays the matrix
    print()
    for i, matrix_element in enumerate(matrix, start=1):
        print(matrix_element, end="\n" if i % 3 == 0 else "\t")

    return matrix


def is_equivalent(matrix_one: List[int], matrix_two: List[int]) -> bool:
    """Check if two matrices are equivalent.

    :param matrix_one: The first matrix.
    :param matrix_two: The second matrix.
    :return: True if the matrices are equivalent, False otherwise.
    """
    matrix_one.sort()
    matrix_two.sort()

    return matrix_one == matrix_two


def main() -> None:
    """Generate and display two matrices, and check if they are equivalent.

    :return: None
    """
    try:
        # Gets input matrices from the user
        matrix_a = construct_matrix("A")
        matrix_b = construct_matrix("B")

        # Checks if the matrices are equivalent
        print(
            f"\nThe matrices are"
            f"{' ' if is_equivalent(matrix_a, matrix_b) else ' not '}"
            f"equivalent!"
        )

    except ValueError:
        # Handles invalid input type
        print("The matrix value must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
