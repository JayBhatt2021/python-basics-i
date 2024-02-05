import datetime


class BankAccount:
    """A simple counter for tracking occurrences."""

    def __init__(self, account_id=None, balance=None) -> None:
        """Initialize the counter.

        :return: None
        """
        if account_id is None and balance is None:
            self.account_id = 0
            self.balance = 0.0
        elif account_id is None:
            self.account_id = 0
            self.balance = balance
        elif balance is None:
            self.account_id = account_id
            self.balance = 0.0
        else:
            self.account_id = account_id
            self.balance = balance

        self.annual_interest_rate = 0.0
        self.date_created = datetime.datetime.now()

    def __str__(self):
        """

        :return:
        """
        return (
            f"Account ID: {self.account_id}\nAccount Balance: "
            f"${self.balance:.2f}\nAnnual Interest Rate: "
            f"{self.annual_interest_rate:.2f}%\nDate Opened: "
            f"{self.date_created.strftime('%m/%d/%Y, %H:%M:%S')}"
        )

    def __repr__(self):
        """

        :return:
        """
        return f""

    def get_monthly_interest(self) -> float:
        """Increment the counter.

        :return: None
        """
        return self.balance * self.get_monthly_interest_rate() / 100

    def get_monthly_interest_rate(self) -> float:
        """Increment the counter.

        :return: None
        """
        return self.annual_interest_rate / 12

    def withdraw(self, amount) -> float:
        """Increment the counter.

        :return: None
        """
        if amount < 0:
            return 0.0

        if amount > self.balance:
            self.balance = 0
            return self.balance

        self.balance -= amount
        return amount

    def deposit(self, amount) -> float:
        """Increment the counter.

        :return: None
        """
        if amount < 0:
            return 0.0

        self.balance += amount
        return amount


def main() -> None:
    """Simulate 100 coin flips and count the number of heads and tails.

    :return: None
    """
    account = BankAccount(123456, 10000)
    account.annual_interest_rate = 2.5
    account.withdraw(3500)
    account.deposit(500)
    print(account)
    print(f"\nMonthly Interest: ${account.get_monthly_interest():.2f}")


if __name__ == "__main__":
    main()
