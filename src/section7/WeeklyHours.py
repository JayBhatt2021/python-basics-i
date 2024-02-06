from typing import List
import random


def generate_random_work_hours(size: int) -> List[int]:
    """Generate a list of random grades.

    :param size: The number of grades to generate.
    :return: A list containing random grades.
    """
    return [random.randint(0, 10) for _ in range(size)]


def display_work_hours_table(work_hours: List[int]) -> None:
    """Display the grades in a formatted table.

    :param grades: A list of grades.
    :param columns: The number of columns in the table.
    :return: None
    """
    days = ["\tMon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    print("Employees Data:")
    for i, day in enumerate(days, start=1):
        print(day, end="\n" if i == len(days) else "\t")

    for i, day_hours in enumerate(work_hours, start=1):
        day_hours_element = f"E{(i + 6) // 7}\t{day_hours}" if i % 7 == 1 else day_hours
        print(f"{day_hours_element}", end="\n" if i % 7 == 0 else "\t")


def add_hours(work_hours):
    """Display the grades in a formatted table.

     :param grades: A list of grades.
     :param columns: The number of columns in the table.
     :return: None
     """
    week_hours_list = []

    week_hours = 0
    for i, day_hours in enumerate(work_hours, start=1):
        week_hours += day_hours

        if i % 7 == 0:
            week_hours_list.append(week_hours)
            week_hours = 0

    print("\nEmployee #\tWeekly Hours")
    print("--------------------------------")
    for i, week_hours in enumerate(week_hours_list, start=1):
        print(f"   {i}\t\t   {week_hours}")


def main() -> None:
    """Generate and display random grades, along with additional statistics.

    :return: None
    """
    num_work_hours = 21
    work_hours = generate_random_work_hours(num_work_hours)

    # Displays the grades in a 3x7 table
    display_work_hours_table(work_hours)

    # Displays additional statistics
    add_hours(work_hours)


if __name__ == "__main__":
    main()
