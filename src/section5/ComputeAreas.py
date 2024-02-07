import math


def calculate_square_area(side: float) -> float:
    """Calculate the area of a square.

    :param side: The side length of the square.
    :return: The area of the square.
    """
    return side ** 2


def calculate_rectangle_area(width: float, length: float) -> float:
    """Calculate the area of a rectangle.

    :param width: The width of the rectangle.
    :param length: The length of the rectangle.
    :return: The area of the rectangle.
    """
    return width * length


def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    return math.pi * radius ** 2


def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle.

    :param base: The base length of the triangle.
    :param height: The height of the triangle.
    :return: The area of the triangle.
    """
    return 0.5 * base * height


def main() -> None:
    """Get user input for dimensions of various shapes and display their areas.

    :return: None
    """
    try:
        # Gets user input for square dimensions
        side = float(input("Enter the square side length: "))
        print(f"Square area: {calculate_square_area(side):.2f} square units")

        # Gets user input for rectangle dimensions
        width = float(input("\nEnter the rectangle width: "))
        length = float(input("Enter the rectangle length: "))
        print(
            f"Rectangle area: {calculate_rectangle_area(width, length):.2f} "
            f"square units"
        )

        # Gets user input for circle dimensions
        radius = float(input("\nEnter the circle radius length: "))
        print(f"Circle area: {calculate_circle_area(radius):.2f} square units")

        # Gets user input for triangle dimensions
        base = float(input("\nEnter the triangle base: "))
        height = float(input("Enter the triangle height: "))
        print(
            f"Triangle area: {calculate_triangle_area(base, height):.2f} square"
            f"units"
        )
    except ValueError:
        # Handles invalid input type
        print("The input must be a float! Exiting program...")


if __name__ == "__main__":
    main()
