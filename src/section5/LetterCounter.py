def count_letters(input_str: str) -> None:
    """Count the number of uppercase and lowercase characters in a string.

    :param input_str: The input string to count characters from.
    :return: None
    """
    uppercase_characters = sum(1 for char in input_str if char.isupper())
    lowercase_characters = sum(1 for char in input_str if char.islower())

    print(f"\nNumber of uppercase characters: {uppercase_characters}")
    print(f"Number of lowercase characters: {lowercase_characters}")


def main() -> None:
    """Prompt the user to enter a string and count its uppercase and lowercase
    characters.

    :return: None
    """
    input_str = input("Enter a string: ")
    count_letters(input_str)


if __name__ == "__main__":
    main()
