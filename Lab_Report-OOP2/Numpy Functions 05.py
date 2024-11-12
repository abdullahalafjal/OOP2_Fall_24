import numpy as np


def calculate_highest_average(scores):

    student_averages = np.mean(scores, axis=1)

    highest_average_index = np.argmax(student_averages)

    print(f"highest average score: {student_averages[highest_average_index]:.2f}")


scores = np.array([[85, 90, 80],[78, 88, 85],[92, 94, 89],[88, 76, 90],])

calculate_highest_average(scores)
