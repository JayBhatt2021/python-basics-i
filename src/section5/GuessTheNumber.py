import random


def generate_secret_number() -> int:
    """Check if the given dimensions form a valid rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: True if the dimensions form a valid rectangle, False otherwise.
    """
    return random.randint(1, 20)


def check_guess(user_input: int, secret_number: int) -> str:
    """Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    if user_input < secret_number:
        return "too low"
    elif user_input == secret_number:
        return "correct"
    else:
        return "too high"


def main() -> None:
    """Get user input for rectangle dimensions and display area and perimeter.

    :return: None
    """
    try:
        #
        replay = True

        while replay:
            secret_number = generate_secret_number()
            print("\nGuess the secret number! It falls in [1, 20].")

            # Gets dimensions from the user
            while True:
                guess = int(input("Your guess: "))

                #
                result = check_guess(guess, secret_number)
                if result in ["too low", "too high"]:
                    print(f"\nYour guess is {result}! Try again!")
                else:
                    print("\nYou correctly entered the secret number!")
                    break

            #
            user_replay = input("Want to play again? (Enter 'yes' or 'no'): ")
            replay = user_replay.strip().lower() == "yes"

    except ValueError:
        # Handles invalid input type
        print("The input must be an integer! Exiting program...")


if __name__ == "__main__":
    main()
