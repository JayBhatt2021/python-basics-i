from typing import List


def construct_matrix(matrix_name: str) -> List[int]:
    """Generate a list of random work hours.

    :param size: The number of work hours to generate.
    :return: A list containing random work hours.
    """
    matrix = []

    print(f"\nEnter the elements for the 3x3 Matrix {matrix_name}:")

    #
    for i in range(1, 10):
        matrix_element = int(input(f"Element #{i}: "))
        matrix.append(matrix_element)

    print()

    #
    for i, matrix_element in enumerate(matrix, start=1):
        print(matrix_element, end="\n" if i % 3 == 0 else "\t")

    return matrix


def is_equivalent(matrix_one, matrix_two) -> bool:
    """Generate a list of random work hours.

    :param size: The number of work hours to generate.
    :return: A list containing random work hours.
    """
    matrix_one.sort()
    matrix_two.sort()

    return matrix_one == matrix_two


def main() -> None:
    """Generate and display random work hours, along with additional statistics.

    :return: None
    """
    try:
        # Gets dimensions from the user
        matrix_a = construct_matrix("A")
        matrix_b = construct_matrix("B")

        print(
            f"\nThe matrices are{' ' if is_equivalent(matrix_a, matrix_b) else ' not '}equivalent!"
        )

    except ValueError:
        # Handles invalid input type
        print("The matrix value must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
