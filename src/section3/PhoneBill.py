def main() -> None:
    """Calculate the phone bill based on the account number, service type, and
    usage.

    :return: None
    """
    try:
        account_number = int(input("Enter the account number: "))
        service_type = input("Enter the service type (Regular/Premium): ")

        if service_type == "Regular":
            total_minutes = int(input("Enter the total minutes: "))
            phone_bill = 15

            if total_minutes > 50:
                phone_bill += 0.5 * (total_minutes - 50)

            print(
                f"\nPhone Bill for Account #{account_number}: ${phone_bill:.2f}"
            )
        elif service_type == "Premium":
            daytime_minutes = int(input("Enter the daytime minutes: "))
            nighttime_minutes = int(input("Enter the nighttime minutes: "))
            phone_bill = 25

            if daytime_minutes > 50:
                phone_bill += 0.2 * (daytime_minutes - 50)

            if nighttime_minutes > 100:
                phone_bill += 0.1 * (nighttime_minutes - 100)

            print(
                f"\nPhone Bill for Account #{account_number}: ${phone_bill:.2f}"
            )
        else:
            print("Invalid service type selected!")

    except ValueError:
        print("Inputs must be valid! Exiting program...")


if __name__ == "__main__":
    main()
