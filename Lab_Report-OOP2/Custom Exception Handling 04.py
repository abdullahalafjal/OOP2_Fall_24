class InsufficientBalance(Exception):
    pass


class BankAccount:
    def __init__(self, balance, main_balance):
        self.balance = balance
        self.main_balance = main_balance

    def withdraw(self, amount):
        if self.balance - amount < self.main_balance:
            raise InsufficientBalance(f"Insufficient balance.")
        self.balance -= amount
        print(f"New Balance: {self.balance:.2f}")


def test_bank_account():
    account = BankAccount(balance=100000, main_balance=20000)

    print(f"Initial Balance: {account.balance:.2f}")
    print(f"Balance: {account.main_balance:.2f}")

    try:
        account.withdraw(4000)
        account.withdraw(50000)
        account.withdraw(70000)
    except InsufficientBalance as e:
        print(f"Error occurred: {e}")


test_bank_account()
