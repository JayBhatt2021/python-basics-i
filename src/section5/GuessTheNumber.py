import random


def generate_secret_number() -> int:
    """Generate a secret number between 1 and 20.

    :return: The randomly generated secret number.
    """
    return random.randint(1, 20)


def check_guess(user_input: int, secret_number: int) -> str:
    """Check the user's guess against the secret number.

    :param user_input: The user's guess.
    :param secret_number: The secret number to guess.
    :return: The result of the guess (too low, too high, or correct).
    """
    if user_input < secret_number:
        return "too low"
    elif user_input == secret_number:
        return "correct"
    else:
        return "too high"


def main() -> None:
    """Play a game to guess the secret number.

    :return: None
    """
    try:
        replay = True

        while replay:
            secret_number = generate_secret_number()
            print("\nGuess the secret number! It falls in [1, 20].")

            while True:
                try:
                    guess = int(input("Your guess: "))

                    result = check_guess(guess, secret_number)
                    if result in ["too low", "too high"]:
                        print(f"\nYour guess is {result}! Try again!")
                    else:
                        print("\nYou correctly guessed the secret number!")
                        break
                except ValueError:
                    print("\nInvalid input! Please enter an integer.")

            user_replay = input("Want to play again? (Enter 'yes' or 'no'): ")
            replay = user_replay.strip().lower() == "yes"
    except KeyboardInterrupt:
        print("\n\nGame ended by user.")


if __name__ == "__main__":
    main()
