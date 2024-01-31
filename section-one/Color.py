def main() -> None:
    """Determine the color based on the entered number.

    :return: None
    """
    try:
        num = int(input("Enter a number: "))
        color = "N/A"

        if 0 <= num < 10:
            color = "Red"
        elif 10 <= num < 20:
            color = "Green"
        elif 20 <= num < 30:
            color = "Blue"

        print(f"Corresponding color: {color}")
    except ValueError:
        print("Please enter a valid number. Exiting program...")


if __name__ == "__main__":
    main()
