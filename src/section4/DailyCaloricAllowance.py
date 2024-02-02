SENTINEL = "exit"
"""The sentinel value to exit the program."""


def get_user_input(prompt: str, prompt_type: type) -> type:
    """Get user input and validate the input type.

    :param prompt: The input prompt.
    :param prompt_type: The expected type for the prompt.
    :return: The user input of the specified prompt type.
    """
    while True:
        user_input = input(prompt)
        if user_input.lower() == SENTINEL:
            exit_program()

        try:
            return prompt_type(user_input.lower())
        except ValueError:
            print("Invalid input! Please enter a valid value.")


def exit_program() -> None:
    """Exit the program.

    :return: None
    """
    print("\nThank you for using this program!")
    exit()


def main() -> None:
    """Print the daily caloric allowance based on user inputs.

    :return: None
    """
    height_prompt = "\nEnter the height (in inches): "
    weight_prompt = "\nEnter the weight (in pounds): "
    age_prompt = "\nEnter the age (in years): "
    sex_prompt = '\nEnter the sex ("male" or "female"): '
    exercise_level_prompt = (
        "\nLevel of exercise:\n1) You don't exercise.\n2) You engage in light "
        "exercise one to three days a week.\n3) You exercise moderately three "
        "to five times a week.\n4) You exercise intensely six to seven days a "
        "week.\n5) You exercise intensely six to seven days a week and have a "
        "physically active job.\nEnter the level of exercise: "
    )

    prompts = {
        height_prompt: float,
        weight_prompt: float,
        age_prompt: int,
        sex_prompt: str,
        exercise_level_prompt: int,
    }

    print(
        "This program calculates the daily caloric allowance of an individual."
    )
    print(f'Type "{SENTINEL}" at any time to stop.')

    while True:
        user_inputs = {
            prompt: get_user_input(prompt, prompt_type)
            for prompt, prompt_type in prompts.items()
        }

        height, weight, age, sex, exercise_level = (
            user_inputs[height_prompt],
            user_inputs[weight_prompt],
            user_inputs[age_prompt],
            user_inputs[sex_prompt],
            user_inputs[exercise_level_prompt],
        )

        if sex not in ["male", "female"]:
            print("\nError: The inputted sex is invalid!")
            break

        if exercise_level not in range(1, 6):
            print("\nError: The inputted exercise level is invalid!")
            break

        # Calculates the basal metabolic rate based on sex
        basal_metabolic_rate = (
                655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
        ) if sex == "female" else (
                66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
        )

        # Calculates the daily caloric allowance based on exercise level
        exercise_factors = [1.2, 1.375, 1.55, 1.725, 1.9]
        daily_caloric_allowance = (
                exercise_factors[exercise_level - 1] * basal_metabolic_rate
        )

        # Prints the calculated daily caloric allowance
        print(
            f"\nDaily caloric allowance: {daily_caloric_allowance:.2f} calories"
        )
        print(
            f'This program will now repeat. Type "{SENTINEL}" at any time to '
            f'stop.'
        )


if __name__ == "__main__":
    main()
