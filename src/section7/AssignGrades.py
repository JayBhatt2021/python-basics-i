def get_class_size() -> int:
    """Prompt the user for the class size.

    :return: The class size entered by the user.
    """
    while True:
        try:
            class_size = int(input("Enter the class size: "))
            if class_size > 0:
                return class_size
            else:
                print("Class size must be a positive integer.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


def get_scores(class_size: int) -> list:
    """Prompt the user to enter scores for each student.

    :param class_size: The number of students in the class.
    :return: A list containing the scores entered by the user.
    """
    scores = []

    print(f"\nEnter the scores for the {class_size} students:")
    for student_num in range(1, class_size + 1):
        while True:
            try:
                score = int(input(f"Score for Student #{student_num}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be within the range [0, 100].\n")
            except ValueError:
                print("Invalid input. Please enter a valid integer.\n")

    return scores


def display_results(scores: list) -> None:
    """Display the results showing each student's score and grade.

    :param scores: A list containing the scores of all students.
    :return: None
    """
    print("\nResults:")
    for student_num, score in enumerate(scores, start=1):
        grade = calculate_grade(score)
        print(
            f"Student #{student_num} received a score of {score} and a grade "
            f"of {grade}."
        )


def calculate_grade(score: int) -> str:
    """Calculate and return the grade based on the given score.

    :param score: The score of a student.
    :return: The grade corresponding to the given score.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    """Calculate statistics based on scores entered by the user.

    :return: None
    """
    try:
        class_size = get_class_size()
        scores = get_scores(class_size)
        display_results(scores)
    except KeyboardInterrupt:
        print("\n\nExiting program...")
    except Exception as e:
        print(f'An error occurred: "{e}"')


if __name__ == "__main__":
    main()
