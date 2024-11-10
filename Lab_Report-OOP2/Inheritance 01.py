class Employee:
    def __init__(self, name, em_id):
        self.name = name
        self.em_id = em_id

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.em_id}")


class PermanentEmployee(Employee):
    def __init__(self, name, em_id, salary):
        super().__init__(name, em_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class ContractEmployee(Employee):
    def __init__(self, name, em_id, hourly_rate, hours_worked):
        super().__init__(name, em_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


perm_em = PermanentEmployee(name="Abdullah", em_id="1202", salary=200000)
print("Permanent Employee:")
perm_em.display()
print(f"Monthly salary: {perm_em.calculate_salary()}")
print()

cont_emp = ContractEmployee(
    name="Hira", em_id="1213", hourly_rate=100, hours_worked=150
)
print("Contract Employee:")
cont_emp.display()
print(f"Calculated Salary: {cont_emp.calculate_salary()}")
