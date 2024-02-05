import datetime


class BankAccount:
    """Represents a simple bank account."""

    def __init__(self, account_id=0, balance=0.0) -> None:
        """Initialize the bank account.

        :param account_id: The account ID.
        :param balance: The initial account balance.
        :return: None
        """
        self.account_id = account_id
        self.balance = balance
        self.annual_interest_rate = 0.0
        self.date_created = datetime.datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the bank account.

        :return: A formatted string containing account information.
        """
        return (
            f"Account ID: {self.account_id}\nAccount Balance: "
            f"${self.balance:.2f}\nAnnual Interest Rate: "
            f"{self.annual_interest_rate:.2f}%\nDate Opened: "
            f"{self.date_created.strftime('%m/%d/%Y, %H:%M:%S')}"
        )

    def get_monthly_interest(self) -> float:
        """Calculate the monthly interest.

        :return: The calculated monthly interest.
        """
        return self.balance * self.get_monthly_interest_rate() / 100

    def get_monthly_interest_rate(self) -> float:
        """Get the monthly interest rate.

        :return: The monthly interest rate.
        """
        return self.annual_interest_rate / 12

    def withdraw(self, amount) -> float:
        """Withdraw money from the account.

        :param amount: The amount to be withdrawn.
        :return: The withdrawn amount.
        """
        if amount < 0:
            return 0.0

        if amount > self.balance:
            amount = self.balance
            self.balance = 0
        else:
            self.balance -= amount

        return amount

    def deposit(self, amount) -> float:
        """Deposit money into the account.

        :param amount: The amount to be deposited.
        :return: The deposited amount.
        """
        if amount < 0:
            return 0.0

        self.balance += amount
        return amount


def main() -> None:
    """Simulate bank account operations and display account information.

    :return: None
    """
    account = BankAccount(account_id=123456, balance=10000)
    account.annual_interest_rate = 2.5

    withdrawn_amount = account.withdraw(3500)
    deposited_amount = account.deposit(500)

    print(account)
    print(f"\nWithdrawn Amount: ${withdrawn_amount:.2f}")
    print(f"Deposited Amount: ${deposited_amount:.2f}")
    print(f"Monthly Interest: ${account.get_monthly_interest():.2f}")


if __name__ == "__main__":
    main()
