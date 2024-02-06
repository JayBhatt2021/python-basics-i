def main() -> None:
    """Calculate the sum and average of three numbers entered by the user.

    :return: None
    """
    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))

        # Displays the sum of x, y, and z
        print(f"\nx + y = {x + y:.2f}")
        print(f"x - y = {x - y:.2f}")
        print(f"x * y = {x * y:.2f}")
        print(f"x / y = {x / y:.2f}")
        print(f"x // y = {x // y:.2f}")
        print(f"x % y = {x % y:.2f}")
    except ValueError:
        print("The input must be a valid float! Exiting program...")


if __name__ == "__main__":
    main()
