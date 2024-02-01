def main() -> None:
    """Compare the deals for small and large boxes based on weight and price.

    :return: None
    """
    try:
        small_box_weight = float(
            input("Enter the small box weight (in pounds): ")
        )
        small_box_price = float(
            input("Enter the small box price (in dollars): ")
        )
        large_box_weight = float(
            input("Enter the large box weight (in pounds): ")
        )
        large_box_price = float(
            input("Enter the large box price (in dollars): ")
        )

        small_box_ratio = small_box_price / small_box_weight
        large_box_ratio = large_box_price / large_box_weight

        if small_box_ratio < large_box_ratio:
            print("\nThe small box has the better deal!")
        elif small_box_ratio == large_box_ratio:
            print("\nBoth boxes have the same deal!")
        else:
            print("\nThe large box has the better deal!")

    except ValueError:
        print("Inputs must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
