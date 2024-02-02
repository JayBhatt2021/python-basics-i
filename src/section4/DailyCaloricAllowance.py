def main() -> None:
    """Print a sandclock pattern.

    :return: None
    """
    sentinel = "exit"

    print(
        "This program calculates the daily caloric allowance of an individual.")
    print('Type "exit" at any time to stop.')
    while True:
        try:
            height = input("\nEnter the height (in inches): ")
            if height == sentinel:
                break
            height = float(height)

            weight = input("\nEnter the weight (in pounds): ")
            if weight == sentinel:
                break
            weight = float(weight)

            age = input("\nEnter the age (in years): ")
            if age == sentinel:
                break
            age = int(age)

            sex = input('\nEnter the sex ("Male" or "Female"): ').lower()
            if sex == sentinel:
                break
            if sex not in ["male", "female"]:
                print("Invalid sex!")
                break

            basal_metabolic_rate = 655 + (4.35 * weight) + (4.7 * height) - (
                    4.7 * age) if sex == "female" else 66 + (
                    6.23 * weight) + (12.7 * height) - (6.8 * age)

            print("\nLevel of exercise:")
            print("1) You don't exercise.")
            print("2) You engage in light exercise one to three days a week.")
            print("3) You exercise moderately three to five times a week.")
            print("4) You exercise intensely six to seven days a week.")
            print(
                "5) You exercise intensely six to seven days a week and have a physically active job.")

            exercise_level = input("\nEnter the level of exercise: ")
            if exercise_level == sentinel:
                break
            exercise_level = int(exercise_level)

            if exercise_level not in [1, 2, 3, 4, 5]:
                print("Invalid exercise level!")
                break

            if exercise_level == 1:
                daily_caloric_allowance = 1.2 * basal_metabolic_rate
            elif exercise_level == 2:
                daily_caloric_allowance = 1.375 * basal_metabolic_rate
            elif exercise_level == 3:
                daily_caloric_allowance = 1.55 * basal_metabolic_rate
            elif exercise_level == 4:
                daily_caloric_allowance = 1.725 * basal_metabolic_rate
            else:
                daily_caloric_allowance = 1.9 * basal_metabolic_rate

            print(
                f"\nDaily caloric allowance: {daily_caloric_allowance:.2f} calories")
            print(
                'This program will now repeat. Type "exit" at any time to stop.')
        except ValueError:
            print("The inputs must be valid! Exiting program...")
            break

    print("\nThank you for using this program!")


if __name__ == "__main__":
    main()
