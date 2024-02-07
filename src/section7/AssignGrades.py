def main() -> None:
    """Calculate statistics based on grades entered by the user.

    :return: None
    """
    try:
        #
        class_size = int(input("Enter the class size: "))

        # Initializes an empty list to store scores
        scores = []

        #
        for student_num in range(0, class_size):
            scores.append(0)

        #
        print(f"\nEnter the scores for the {class_size} students:")
        student_num = 0
        while student_num < class_size:
            score = int(input(f"Score for Student #{student_num}: "))

            # Checks if the score is within the valid range [0, 100]
            if score < 0 or score > 100:
                print("Score must be within the range [0, 100].\n")
                continue

            # Appends the score to the list
            scores[student_num] = score

            #
            student_num += 1

        #
        print("\nResults:")
        for student_num, score in enumerate(scores):
            #
            grade = "F"
            if 90 <= score <= 100:
                grade = "A"
            elif 80 <= score <= 89:
                grade = "B"
            elif 70 <= score <= 79:
                grade = "C"
            elif 60 <= score <= 69:
                grade = "D"

            #
            print(
                f"Student #{student_num} received a score of {score} and a "
                f"grade of {grade}."
            )
    except ValueError:
        print("The input must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
