def main() -> None:
    """Simulate a countdown and display liftoff.

    :return: None
    """
    for i in range(3, -1, -1):
        print(f"{i}...")

    print("Liftoff!")
    print("Houston, we may or may not have a problem.")


if __name__ == "__main__":
    main()
