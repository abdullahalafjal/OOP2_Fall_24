# (1)
class InvalidVoterException(Exception):

    def __init__(self, age):
        self.age = age
        # Call the constructor of the base Exception,from the InvalidVoterException class
        super().__init__(self.age)


try:
    age1 = int(input("Enter your age: "))
    if age1 < 18:
        raise InvalidVoterException()
    else:
        print("You are eligible to vote.")

except InvalidVoterException as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer Number.")


# (2)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        if not (10000 <= self.salary <= 50000):
            raise SalaryNotInRangeException()

    def displaySalary(self):
        print(f"Employee Name: {self.name}\n Salary: {self.salary}")


class SalaryNotInRangeException(Exception):

    def __init__(self, message="Salary must be between 10,000 and 50,000."):
        self.message = message
        super().__init__(self.message)


try:
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))

    emp1 = Employee(name, salary)
    emp1.displaySalary()
except SalaryNotInRangeException as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid number for salary.")


# (3a)
arr = [10, 5, 15, 20]

try:

    divisor = int(input("Enter a divisor: "))

    print("Division Results:")

    for i in range(len(arr)):
        print(f"{arr[i]} / {divisor} = {arr[i] / divisor}")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter a valid integer for the divisor.")
except NameError:
    print("A variable is not defined.")
except TypeError:
    print(" Type Error.")
except IndexError:
    print("Index out of range.")
except AttributeError:
    print("Invalid attribute access.")
except FileNotFoundError:
    print("File not found.")
else:
    print("Division completed successfully.")
finally:
    print("Program execution finished.")

# (3b)


class InsufficientError(Exception):

    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientError()
            else:
                self.balance -= amount
                print(f"Withdrawal successful.\n Current balance: {self.balance}")
        except InsufficientError as e:
            print(f"Error Type: {e}")


try:
    account = BankAccount(50000)

    withdrawal_amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(withdrawal_amount)

except ValueError:
    print("Please enter a valid numeric amount.")
