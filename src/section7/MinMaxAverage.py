from typing import List
import random


def generate_random_grades(size: int) -> List[int]:
    """Generate a list of random grades.

    :param size: The number of grades to generate.
    :return: A list containing random grades.
    """
    return [random.randint(0, 100) for _ in range(size)]


def display_grades_table(grades: List[int], columns: int) -> None:
    """Display the grades in a formatted table.

    :param grades: A list of grades.
    :param columns: The number of columns in the table.
    :return: None
    """
    print("Grades:")
    for i, grade in enumerate(grades, start=1):
        print(f"{grade}", end="\n" if i % columns == 0 else "\t")


def main() -> None:
    """Generate and display random grades, along with additional statistics.

    :return: None
    """
    num_grades = 16
    grades = generate_random_grades(num_grades)

    # Displays the grades in a 4x4 table
    display_grades_table(grades, columns=4)

    # Displays additional statistics
    print(f"\nHighest grade: {max(grades)}")
    print(f"Lowest grade: {min(grades)}")
    print(f"Class average: {sum(grades) / len(grades):.2f}")


if __name__ == "__main__":
    main()
