class InsufficientBalance(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientBalance("Insufficient balance.")
        self.balance -= amount
        print(f"New Balance: {self.balance}")


try:
    b = BankAccount(50000)
    print(f"Balance: {b.balance}")
    b.withdraw(5000)
except InsufficientBalance as e:
    print(f"Error occurred: {e}")
