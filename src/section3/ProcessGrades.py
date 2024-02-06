def main() -> None:
    """Calculate statistics based on grades entered by the user.

    :return: None
    """
    try:
        # Initializes an empty list to store grades
        grades = []

        # Gets grades from the user
        for i in range(1, 5):
            grade = int(input(f"Enter grade #{i}: "))

            # Checks if the grade is within the valid range [0, 100]
            if grade < 0 or grade > 100:
                print("Grade must be within the range [0, 100].")
                exit(1)

            # Appends the grade to the list
            grades.append(grade)

        # Calculates and displays statistics
        print(f"\nHighest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")
        print(f"Average grade: {sum(grades) / len(grades):.2f}")
    except ValueError:
        print("Grade must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
