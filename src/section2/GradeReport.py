def main() -> None:
    """Analyze and print feedback based on the grade entered by the user.

    :return: None
    """
    try:
        # Gets the grade from the user
        grade = int(input("Enter the grade: "))

        # Provides feedback based on the grade
        if grade == 100:
            print("This grade is a perfect score. Well done!")
        elif 90 <= grade < 100:
            print("This grade is well above average. Excellent work!")
        elif 80 <= grade < 90:
            print("This grade is above average. Nice job!")
        elif 70 <= grade < 80:
            print("This grade is average.")
        elif 60 <= grade < 70:
            print("This grade is below average.")
        elif grade < 60:
            print("This grade is a failing grade.")
        else:
            print("Invalid grade value!")
    except ValueError:
        print("Grade must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
