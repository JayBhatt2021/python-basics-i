def main() -> None:
    """Calculate the sum of even numbers up to a stopping point.

    :return: None
    """
    try:
        end = int(input("Enter the stopping point: "))
        print(f"Sum of the even numbers: {sum(range(0, end + 1, 2))}")
    except ValueError:
        print("Stopping point must be a valid number! Exiting program...")


if __name__ == "__main__":
    main()
