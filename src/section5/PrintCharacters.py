def print_characters(starting_character: str, ending_character: str) -> None:
    """Print a series of characters between the starting and ending characters.

    :param starting_character: The starting character of the series.
    :param ending_character: The ending character of the series.
    :return: None
    """
    count = 0
    print("\nOutput:")

    # Iterates through characters from starting to ending character
    for i in range(ord(starting_character), ord(ending_character) + 1):
        count += 1
        print(chr(i), end="\n" if count % 5 == 0 else "\t")
    print()


def main() -> None:
    """Get user input for starting and ending characters and display the series
    table.

    :return: None
    """
    # Gets input for starting and ending characters
    start = input("Enter the starting character: ")
    end = input("Enter the ending character: ")

    # Checks input validity
    if len(start) != 1 or len(end) != 1:
        print("The length of the character must be one!")
        return

    if start > end:
        print(
            "The ending character must come after or be the same as the "
            "starting character!"
        )
        return

    # Prints the series table
    print_characters(start, end)


if __name__ == "__main__":
    main()
