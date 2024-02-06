def main() -> None:
    """Calculate meeting day based on the current day and days until the
    meeting.

    :return: None
    """
    try:
        # Defines the days of the week
        days_of_week = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday"
        ]

        # Gets the current day of the week from the user
        current_day_num = int(input("Enter the current day ([0, 6]): "))

        # Checks if the input is within the valid range [0, 6]
        if current_day_num < 0 or current_day_num > 6:
            print("Invalid input! Day must be within the range [0, 6].")
            exit(1)

        # Gets the number of days until the meeting
        days_until_meeting = int(
            input("Enter the number of days until the meeting: ")
        )

        # Checks if the input is valid (not negative)
        if days_until_meeting < 0:
            print(
                "Invalid input! Number of days until the meeting cannot be "
                "negative."
            )
            exit(1)

        # Calculates the meeting day
        meeting_day_num = (current_day_num + days_until_meeting) % 7
        meeting_day = days_of_week[meeting_day_num]

        # Prints the results
        print(f"\nToday is {days_of_week[current_day_num]}.")
        print(f"There are {days_until_meeting} days until the meeting.")
        print(f"The meeting day is on {meeting_day}.")
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("Invalid input! Please enter valid integers. Exiting program...")


if __name__ == "__main__":
    main()
