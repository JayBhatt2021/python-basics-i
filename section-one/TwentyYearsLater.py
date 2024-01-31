def main() -> None:
    """Calculate the age in 20 years.

    :return: None
    """
    try:
        age = int(input("Enter your current age: "))
        print(f"Your age in 20 years: {age + 20}")
    except ValueError:
        print("Please enter a valid age as a number. Exiting program...")


if __name__ == "__main__":
    main()
