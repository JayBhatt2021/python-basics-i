def main() -> None:
    """Perform basic arithmetic operations on two numbers entered by the user.

    :return: None
    """
    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))

        # Performs addition, subtraction, multiplication, division, floor
        # division, and modulus operations on x and y
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
