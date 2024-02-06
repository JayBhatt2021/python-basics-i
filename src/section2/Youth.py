def main() -> None:
    """Print a message based on the age entered by the user.

    :return: None
    """
    try:
        # Gets the age from the user
        age = int(input("Enter the age: "))
        print()

        # Checks if the age is less than 22
        if age < 22:
            print("Youth is a wonderful thing. Enjoy it.")

        # Prints the following message regardless of age
        print("Age is a state of mind.")
    except ValueError:
        print("Age must be a valid integer! Exiting program...")


if __name__ == "__main__":
    main()
