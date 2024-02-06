def main() -> None:
    """Analyze and print feedback based on the grade entered by the user.

    :return: None
    """
    try:
        # Gets the grade from the user
        grade = int(input("Enter the grade: "))

        # Provides feedback based on the grade
        if grade == 100:
            print("\nThis grade is a perfect score. Well done!")
        elif 90 <= grade < 100:
            print("\nThis grade is well above average. Excellent work!")
        elif 80 <= grade < 90:
            print("\nThis grade is above average. Nice job!")
        elif 70 <= grade < 80:
            print("\nThis grade is average.")
        elif 60 <= grade < 70:
            print("\nThis grade is below average.")
        elif 0 <= grade < 60:
            print("\nThis grade is a failing grade.")
        else:
            print("\nInvalid grade value!")
    except ValueError:
        print("Grade must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
