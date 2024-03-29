from typing import List, Tuple
import random

NUM_EMPLOYEES = 3
"""The number of employees."""

NUM_DAYS = 7
"""The number of working days."""

DAYS_OF_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
"""A list containing the days of the week."""


def generate_random_work_hours(
    num_employees: int = NUM_EMPLOYEES, num_days: int = NUM_DAYS
) -> List[List[int]]:
    """Generate a list of random work hours for each employee for each day of
    the week.

    :param num_employees: The number of employees.
    :param num_days: The number of days in a week.
    :return: A list containing random work hours for each employee for each day.
    """
    return [
        [random.randint(0, 10) for _ in range(num_days)] for _ in
        range(num_employees)
    ]


def display_work_hours_table(work_hours: List[List[int]]) -> None:
    """Display the work hours in a formatted table.

    :param work_hours: A list of work hours for each employee for each day.
    :return: None
    """
    print("Employee Work Hours:")
    print("\t" + "\t".join(DAYS_OF_WEEK))

    for emp_num, week_hours in enumerate(work_hours, start=1):
        formatted_hours = [
            # Constructs the string representing the day's work hours along with
            # the employee number if it is the first day of the week
            f"E{emp_num}\t{day_hours}" if i == 0 else str(day_hours)
            for i, day_hours in enumerate(week_hours)
        ]

        # Prints the formatted list representing the weekly work hours
        print("\t".join(formatted_hours))


def display_most_hours_worked(work_hours: List[List[int]]) -> None:
    """Display the day with the most worked hours for each employee.

    :param work_hours: A list of work hours for each employee for each day.
    :return: None
    """
    print()
    for emp_num, week_hours in enumerate(work_hours, start=1):
        _, max_day = max(
            # Pairs each day's work hours with the corresponding day of the week
            zip(week_hours, DAYS_OF_WEEK),

            # Selects the maximum value based on the first element of each pair
            # (daily work hours)
            key=lambda x: x[0]
        )

        print(f"Employee #{emp_num} worked the most hours on {max_day}.")


def calculate_weekly_hours(work_hours: List[List[int]]) \
        -> List[Tuple[int, int]]:
    """Calculate and return the weekly work hours for each employee.

    :param work_hours: A list of work hours for each employee for each day.
    :return: A list containing the weekly work hours for each employee.
    """
    # Calculates the weekly work hours for each employee
    weekly_hours = [
        (emp_num, sum(week_hours))
        for emp_num, week_hours in enumerate(work_hours, start=1)
    ]

    # Sorts the weekly_hours list based on the total hours worked in a week
    # (tup[1]) for each employee
    weekly_hours.sort(key=lambda tup: tup[1])

    return weekly_hours


def display_weekly_hours(weekly_hours: List[Tuple[int, int]]) -> None:
    """Display the weekly work hours for each employee.

    :param weekly_hours: A list of weekly work hours for each employee.
    :return: None
    """
    print("\nEmployee #\tWeekly Hours")
    print("-----------------------------")
    for emp_num, week_hours in weekly_hours:
        # Prints leading spaces
        print(" " * 5, end="")

        # Prints employee number
        print(emp_num, end="")

        # Prints in-between spaces
        print(" " * 15, end="")

        # Prints weekly hours
        print(week_hours)


def main() -> None:
    """Generate random work hours for employees, display them in a tabular
    format, and show additional statistics.

    :return: None
    """
    # Generates random work hours for employees
    work_hours = generate_random_work_hours()

    # Displays the work hours in a tabular format
    display_work_hours_table(work_hours)

    # Displays which day each employee worked the most hours
    display_most_hours_worked(work_hours)

    # Calculates and displays the total weekly work hours for each employee
    weekly_hours = calculate_weekly_hours(work_hours)
    display_weekly_hours(weekly_hours)


if __name__ == "__main__":
    main()
