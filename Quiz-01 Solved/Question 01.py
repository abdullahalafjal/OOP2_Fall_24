student_marks = [85, 55, 90, 73, 35, 88]


def category(marks):
    for i in marks:
        if i > 80:
            print("Excellent")
        elif 40 <= i <= 60:
            print("Needs Improvement")
        elif 61 <= i <= 80:
            print("Good")
        elif i < 40:
            print("Fail")


category(student_marks)
