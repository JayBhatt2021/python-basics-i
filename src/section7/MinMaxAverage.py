from typing import List
import random


def create_random_grades() -> List[int]:
    """Find and return the set of distinct values in the given list.

    :param num_list: A list of integers.
    :return: A set containing distinct values.
    """
    return [random.randint(0, 100) for _ in range(16)]


def main() -> None:
    """Get user input for a list of numbers and display the set of distinct
    values.

    :return: None
    """
    grades = create_random_grades()

    # 4 by 4
    print("Grades:")
    for i, grade in enumerate(grades):
        print(f"{grade}\t", end="" if (i + 1) % 4 != 0 else "\n")

    print(f"\nHighest grade: {max(grades)}")
    print(f"Lowest grade: {min(grades)}")
    print(f"Class average: {sum(grades) / len(grades):.2f}")


if __name__ == "__main__":
    main()
