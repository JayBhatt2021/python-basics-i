from typing import Callable, List


def feet_to_meters(feet: float) -> float:
    """Convert feet to meters.

    :param feet: The length in feet.
    :return: The equivalent length in meters.
    """
    return 0.305 * feet


def meters_to_feet(meters: float) -> float:
    """Convert meters to feet.

    :param meters: The length in meters.
    :return: The equivalent length in feet.
    """
    return 3.279 * meters


def print_conversion_table(
        column_titles: List[str],
        conversion_function: Callable[[float], float]
) -> None:
    """Print a conversion table.

    :param column_titles: A list of column titles.
    :param conversion_function: The function for the conversion.
    :return: None
    """
    print(f"{column_titles[0]}\t{column_titles[1]}")

    for i in range(0, 21):
        print(f"{i:.1f}\t{conversion_function(i):.3f}")

    print()


def main() -> None:
    """Display conversion tables for feet to meters and meters to feet.

    :return: None
    """
    print_conversion_table(["Feet", "Meters"], feet_to_meters)
    print_conversion_table(["Meters", "Feet"], meters_to_feet)


if __name__ == "__main__":
    main()
