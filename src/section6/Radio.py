class Radio:
    """Represents a circle with a given radius."""

    def __init__(self) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        self.station = 1
        self.volume = 1
        self.is_on = False

    def __str__(self) -> str:
        """Return a string representation of the circle.

        :return: A string containing circle information.
        """
        return (
            f"Station Level: {self.station}\n"
            f"Volume Level: {self.volume}\n"
            f"Status: {self.is_on}"
        )

    def turn_on(self) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        self.is_on = True

    def turn_off(self) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        self.is_on = False

    def station_up(self, to_add: int) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        if self.is_on:
            if self.station + to_add < 10:
                self.station += to_add
            else:
                self.station = 10

    def station_down(self, to_subtract) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        if self.is_on:
            if self.station - to_subtract > 1:
                self.station -= to_subtract
            else:
                self.station = 1

    def volume_up(self, to_add: int) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        if self.is_on:
            if self.volume + to_add < 10:
                self.volume += to_add
            else:
                self.volume = 10

    def volume_down(self, to_subtract: int) -> None:
        """Initialize the circle with a radius.

        :param radius: The radius of the circle (default is 1.0).
        :return: None
        """
        if self.is_on:
            if self.volume - to_subtract > 1:
                self.volume -= to_subtract
            else:
                self.volume = 1


def main() -> None:
    """Create and display information for a circle with the default and modified
    radius.

    :return: None
    """
    # Creates and prints the radio
    radio = Radio()
    print(f"Creating radio:\n{radio}")

    # Turns the radio on
    radio.turn_on()
    print(f"Turning the radio on:\n{radio}")

    # Increases volume level by 3
    radio.volume_up(3)
    print(f"Increasing volume level by 3:\n{radio}")

    # Increases station level by 5
    radio.station_up(5)
    print(f"Increasing station level by 5:\n{radio}")

    # Decreases volume level by 1
    radio.volume_down(1)
    print(f"Decreasing volume level by 1:\n{radio}")

    # Increases station level by 3
    radio.station_up(3)
    print(f"Increasing station level by 3:\n{radio}")

    # Turns the radio off
    radio.turn_off()
    print(f"Turning the radio off:\n{radio}")

    # Attempts to increase volume level by 2
    radio.volume_up(2)
    print(f"Attempting to increase volume level by 2:\n{radio}")

    # Attempts to decrease station level by 2
    radio.station_down(2)
    print(f"Attempting to decrease station level by 2:\n{radio}")


if __name__ == "__main__":
    main()
