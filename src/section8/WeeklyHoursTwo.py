from typing import List, Tuple
import random


def generate_random_work_hours() -> List[List[int]]:
    """Generate a list of random work hours.

    :param size: The number of work hours to generate.
    :return: A list containing random work hours.
    """
    return [[random.randint(0, 10) for _ in range(7)] for _ in range(3)]


def display_work_hours_table(work_hours: List[List[int]]) -> None:
    """Display the work hours in a formatted table.

    :param work_hours: A list of work hours.
    :return: None
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    print("Employee Work Hours:")
    print("\t" + "\t".join(days))

    for i, week_hours in enumerate(work_hours, start=1):
        for j, day_hours in enumerate(week_hours, start=1):
            # Constructs the string representing the day's work hours along with
            # the employee number if it is the first day of the week
            day_hours_element = f"E{i}\t{day_hours}" if j % 7 == 1 \
                else day_hours

            # Prints the formatted string representing the day's work hours
            print(f"{day_hours_element}", end="\n" if j % 7 == 0 else "\t")


def calculate_weekly_hours(work_hours: List[List[int]]) -> List[Tuple[int, int]]:
    """Calculate and return the weekly work hours for each employee.

    :param work_hours: A list of daily work hours.
    :return: A list containing the weekly work hours for each employee.
    """
    #
    weekly_hours = [(employee_num, sum(week_hours)) for employee_num, week_hours
                    in enumerate(work_hours, start=1)]

    #
    weekly_hours.sort(key=lambda x: x[1])

    return weekly_hours


def display_weekly_hours(weekly_hours: List[Tuple[int, int]]) -> None:
    """Display the weekly work hours for each employee.

    :param weekly_hours: A list of weekly work hours for each employee.
    :return: None
    """
    print("\nEmployee #\tWeekly Hours")
    print("-----------------------------")
    for employee_num, week_hours in weekly_hours:
        # Prints leading spaces
        print(" " * 5, end="")

        # Prints employee number
        print(employee_num, end="")

        # Prints in-between spaces
        print(" " * 15, end="")

        # Prints weekly hours
        print(week_hours)


def main() -> None:
    """Generate and display random work hours, along with additional statistics.

    :return: None
    """
    # Generates random work hours
    work_hours = generate_random_work_hours()

    # Displays the work hours in a 3x7 table
    display_work_hours_table(work_hours)

    # Calculates and displays additional statistics
    weekly_hours = calculate_weekly_hours(work_hours)
    display_weekly_hours(weekly_hours)


if __name__ == "__main__":
    main()
