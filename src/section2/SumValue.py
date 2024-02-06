def main() -> None:
    """Calculate the sum and average of three numbers entered by the user.

    :return: None
    """
    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        z = float(input("Enter z: "))

        # Calculates the sum of x, y, and z
        total = x + y + z

        # Displays the sum of x, y, and z
        print(f"\nSum of x, y, and z: {total:.2f}")

        # Calculates and displays the average of x, y, and z
        print(f"Average of x, y, and z: {total / 3:.2f}")
    except ValueError:
        print("The input must be a valid float! Exiting program...")
