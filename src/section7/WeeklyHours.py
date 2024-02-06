from typing import List
import random


def generate_random_work_hours(size: int) -> List[int]:
    """Generate a list of random work hours.

    :param size: The number of work hours to generate.
    :return: A list containing random work hours.
    """
    return [random.randint(0, 10) for _ in range(size)]


def display_work_hours_table(work_hours: List[int]) -> None:
    """Display the work hours in a formatted table.

    :param work_hours: A list of work hours.
    :return: None
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    print("Employee Work Hours:")
    print("\t" + "\t".join(days))

    for i, day_hours in enumerate(work_hours, start=1):
        # Constructs the string representing the day's work hours along with the
        # employee number if it is the first day of the week
        day_hours_element = f"E{(i + 6) // 7}\t{day_hours}" if i % 7 == 1 \
            else day_hours

        # Prints the formatted string representing the day's work hours
        print(f"{day_hours_element}", end="\n" if i % 7 == 0 else "\t")


def calculate_weekly_hours(work_hours: List[int]) -> List[int]:
    """Calculate and return the weekly work hours for each employee.

    :param work_hours: A list of daily work hours.
    :return: A list containing the weekly work hours for each employee.
    """
    week_hours_list = []

    week_hours = 0
    for i, day_hours in enumerate(work_hours, start=1):
        week_hours += day_hours

        # Checks if it is the last day of the week
        if i % 7 == 0:
            # Adds the accumulated hours for the week to the list
            week_hours_list.append(week_hours)

            # Resets the weekly hours counter for the next week
            week_hours = 0

    return week_hours_list


def display_weekly_hours(weekly_hours: List[int]) -> None:
    """Display the weekly work hours for each employee.

    :param weekly_hours: A list of weekly work hours for each employee.
    :return: None
    """
    print("\nEmployee #\tWeekly Hours")
    print("-----------------------------")
    for i, week_hours in enumerate(weekly_hours, start=1):
        # Prints leading spaces
        print(" " * 5, end="")

        # Prints employee number
        print(i, end="")

        # Prints in-between spaces
        print(" " * 15, end="")

        # Prints weekly hours
        print(week_hours)


def main() -> None:
    """Generate and display random work hours, along with additional statistics.

    :return: None
    """
    # Generates random work hours
    work_hours = generate_random_work_hours(21)

    # Displays the work hours in a 3x7 table
    display_work_hours_table(work_hours)

    # Calculates and displays additional statistics
    weekly_hours = calculate_weekly_hours(work_hours)
    display_weekly_hours(weekly_hours)


if __name__ == "__main__":
    main()
