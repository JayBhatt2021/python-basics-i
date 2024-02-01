def main() -> None:
    """Calculate the driving cost based on the distance, fuel efficiency, and
    fuel cost.

    :return: None
    """
    try:
        distance = float(input("Enter the distance travelled (miles): "))
        fuel_efficiency = float(
            input("Enter the car fuel efficiency (miles/gallon): ")
        )
        fuel_cost = float(input("Enter the fuel cost (dollars/gallon): "))

        # Calculates the total driving cost
        driving_cost = (distance / fuel_efficiency) * fuel_cost

        print(f"\nDriving cost: ${driving_cost:.2f}")
    except ValueError:
        print("Inputs must be valid floats! Exiting program...")


if __name__ == "__main__":
    main()
