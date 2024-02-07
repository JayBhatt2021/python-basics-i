from typing import Dict


def count_online_users(users_dict: Dict[str, str]) -> int:
    """Count the number of online users in the given dictionary.

    :param users_dict: A dictionary containing usernames as keys and their
                       corresponding online statuses as values.
    :return: The number of online users.
    """
    return sum(
        1 for status in users_dict.values() if status == "online"
    )


def main() -> None:
    """Count and print the number of online users from a predefined dictionary.

    :return: None
    """
    users_dict = {
        "Becky": "offline",
        "Jack": "online",
        "Jay": "online",
        "Kim": "offline",
        "Owen": "online",
        "Rick": "offline",
        "Tom": "online",
        "Zach": "online",
    }

    print(f"There are {count_online_users(users_dict)} users online.")


if __name__ == "__main__":
    main()
