class BankAccount:
    def __init__(self, Main_balance=0):
        # Private variable for account balance
        self.__balance = Main_balance

    # Public method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

   
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient balance. Withdrawal failed.")
        else:
            print("Withdrawal amount must be positive.")

    # Public method to check the account balance
    def check_balance(self):
        return self.__balance



account = BankAccount(100)

account.deposit(50) 

account.withdraw(200)  
print(f"Current Balance: ${account.check_balance():.2f}") 

account.withdraw(30) 
print(f"Current Balance: ${account.check_balance():.2f}")  