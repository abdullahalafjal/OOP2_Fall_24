class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        return f"Name: {self.first_name} {self.last_name}"

class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, \nAdmin, Joining Year: {self.joining_year}"

class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, \nTeacher, Joining Year: {self.joining_year}"


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Alumni(Student):
    def __init__(self, first_name, last_name, passing_year):
        super().__init__(first_name, last_name)
        self.passing_year = passing_year

    def display(self):
        return f"{super().display()}, \nAlumni, Passing Year: {self.passing_year}"

class CurrentStudent(Student):
    def __init__(self, first_name, last_name, current_semester):
        super().__init__(first_name, last_name)
        self.current_semester = current_semester

    def display(self):
        return f"{super().display()}, \nCurrent Student, Semester: {self.current_semester}"


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        return f"{super().display()}, \nEmployee ID: {self.employee_id}"

try:
    person1 = Person("Tarek", "Rahman")
    print(person1.display())

    admin1 = Admin("Asraf", "Khan", 2015)
    print(admin1.display())

    teacher1 = Teacher("Faiza", "Maam", 2018)
    print(teacher1.display())

    alumni2 = Alumni("Abdullah", "AL", 2020)
    print(alumni2.display())

    current_student1 = CurrentStudent("Abdullah Al", "Afjal", "5th")
    print(current_student1.display())

    employee1 = Employee("Abdullah", "Al",1730)
    print(employee1.display())
except Exception:
    print("Any Exception")