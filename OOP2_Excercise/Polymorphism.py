class Department:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(f"Department Name: {self.name}")

class Teacher(Department):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def displayName(self):
        print(f"Teacher Department Name: {self.name}")

    def scheduleClass(self):
        pass

    def gradeStudent(self):
        pass

    def profile(self):
        print(f"Teacher's Profile: \nSubject: {self.subject}\nDepartment Of: {self.name}")

class Author:
    def __init__(self, name):
        self.name = name

    def writeArticle(self):
        pass

    def publishBlog(self):
        pass

    def profile(self):
        print(f"Author's Profile Name: {self.name}")

class TeacherAuthor(Teacher, Author):
    def __init__(self, name, subject):
        Teacher.__init__(self, name, subject) 
        Author.__init__(self, name)           

    def profile(self):
        print(f"Teacher Author Profile Name: {self.name}\nSubject: {self.subject}")

t1 = TeacherAuthor("Abdullah", "CSE")
t2=Teacher("GED","CSE")
t2.profile()
t1.displayName()  
t1.profile()      
