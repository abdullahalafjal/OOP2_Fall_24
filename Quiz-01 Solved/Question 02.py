def calculate_average(grades):
    return sum(grades) / len(grades)


def find_top_student(students):
    top_student = 0
    highest_average = 0

    for student in students:
        name, student_id, grades = student
        average_grade = calculate_average(grades)

        if average_grade > highest_average:
            highest_average = average_grade
            top_student = (name, student_id)
            # top_student = (name, student_id, grades)

    return top_student


# Dictionary used
students = [
    ("Alice", "ID001", [85, 90, 78]),
    ("Bob", "ID002", [88, 92, 95]),
    ("Charlie", "ID003", [70, 75, 80]),
]

top_student = find_top_student(students)
print(
    f"Top Student: {top_student[0]} ({top_student[1]})with the highest average grade."
)
# print(f"Top Student: {top_student[0]} ({top_student[1]}){top_student[2]}with the highest average grade.")
