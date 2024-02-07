class Radio:
    """Represents a radio with station and volume controls."""

    def __init__(self) -> None:
        """Initialize the radio with default settings.

        :return: None
        """
        self.station = 1
        self.volume = 1
        self.is_on = False

    def __str__(self) -> str:
        """Return a string representation of the radio.

        :return: A string containing radio information.
        """
        status = "On" if self.is_on else "Off"
        return (
            f"Station Level: {self.station}\n"
            f"Volume Level: {self.volume}\n"
            f"Status: {status}"
        )

    def turn_on(self) -> None:
        """Turn on the radio.

        :return: None
        """
        self.is_on = True

    def turn_off(self) -> None:
        """Turn off the radio.

        :return: None
        """
        self.is_on = False

    def station_up(self, to_add: int) -> None:
        """Increase the station level.

        :param to_add: The value to add to the current station level.
        :return: None
        """
        if self.is_on:
            # Ensures station level does not exceed maximum (10)
            self.station = min(10, self.station + to_add)

    def station_down(self, to_subtract: int) -> None:
        """Decrease the station level.

        :param to_subtract: The value to subtract from the current station
                            level.
        :return: None
        """
        if self.is_on:
            # Ensures station level does not go below minimum (1)
            self.station = max(1, self.station - to_subtract)

    def volume_up(self, to_add: int) -> None:
        """Increase the volume level.

        :param to_add: The value to add to the current volume level.
        :return: None
        """
        if self.is_on:
            # Ensures volume level does not exceed maximum (10)
            self.volume = min(10, self.volume + to_add)

    def volume_down(self, to_subtract: int) -> None:
        """Decrease the volume level.

        :param to_subtract: The value to subtract from the current volume level.
        :return: None
        """
        if self.is_on:
            # Ensures volume level does not go below minimum (1)
            self.volume = max(1, self.volume - to_subtract)


def main() -> None:
    """Simulate radio operations.

    :return: None
    """
    # Creates the radio
    radio = Radio()
    print("Creating radio:")
    print(radio)

    # Turns the radio on
    radio.turn_on()
    print("\nTurning the radio on:")
    print(radio)

    # Increases volume level by 3
    radio.volume_up(3)
    print("\nIncreasing volume level by 3:")
    print(radio)

    # Increases station level by 5
    radio.station_up(5)
    print("\nIncreasing station level by 5:")
    print(radio)

    # Decreases volume level by 1
    radio.volume_down(1)
    print("\nDecreasing volume level by 1:")
    print(radio)

    # Increases station level by 3
    radio.station_up(3)
    print("\nIncreasing station level by 3:")
    print(radio)

    # Turns the radio off
    radio.turn_off()
    print("\nTurning the radio off:")
    print(radio)

    # Attempts to increase volume level by 2
    radio.volume_up(2)
    print("\nAttempting to increase volume level by 2 (Radio is off):")
    print(radio)

    # Attempts to decrease station level by 2
    radio.station_down(2)
    print("\nAttempting to decrease station level by 2 (Radio is off):")
    print(radio)


if __name__ == "__main__":
    main()
