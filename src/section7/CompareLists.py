def get_list_size() -> int:
    """Prompt the user for the class size.

    :return: The class size entered by the user.
    """
    while True:
        try:
            list_size = int(input("Enter the list size: "))
            if list_size > 0:
                return list_size
            else:
                print("List size must be a positive integer.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


def get_integers(list_size: int) -> list:
    """Prompt the user to enter scores for each student.

    :param class_size: The number of students in the class.
    :return: A list containing the scores entered by the user.
    """
    integers = []

    print(f"Enter the {list_size} integer(s):")
    for i in range(1, list_size + 1):
        while True:
            try:
                integer = int(input(f"Integer #{i}: "))
                integers.append(integer)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.\n")

    return integers


def compare_lists(int_list_one: list, int_list_two: list) -> None:
    """Display the results showing each student's score and grade.

    :param scores: A list containing the scores of all students.
    :return: None
    """
    print(f"\nThe lists are{' ' if int_list_one == int_list_two else ' not '}identical.")


def main() -> None:
    """Calculate statistics based on scores entered by the user.

    :return: None
    """
    try:
        list_size = get_list_size()

        print("\nList #1")
        int_list_one = get_integers(list_size)

        print("\nList #2")
        int_list_two = get_integers(list_size)

        compare_lists(int_list_one, int_list_two)
    except KeyboardInterrupt:
        print("\n\nExiting program...")
    except Exception as e:
        print(f'An error occurred: "{e}"')


if __name__ == "__main__":
    main()
