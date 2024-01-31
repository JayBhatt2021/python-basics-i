import math


def main() -> None:
    """Calculate the volume of a cylinder based on the entered dimensions.

    :return: None
    """
    try:
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))

        # Calculates the cylinder volume using the formula: V = πr^2h
        cylinder_volume = math.pi * radius ** 2 * height

        print(f"Cylinder volume: {cylinder_volume:.2f} units^3")
    except ValueError:
        print("Radius/height must be a valid float! Exiting program...")


if __name__ == "__main__":
    main()
