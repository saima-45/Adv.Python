import numpy as np

marks = np.array([
    [78, 85, 92],
    [65, 72, 80],
    [88, 90, 85],
    [55, 68, 70],
    [92, 95, 89],
    [74, 81, 77],
    [69, 75, 82],
    [83, 87, 91],
    [60, 64, 71],
    [95, 93, 96]
])

print("Number of students:", marks.shape[0])
print()

print("Number of subjects:", marks.shape[1])
print()

print("Marks of 5th student:", marks[4])
print()

print("Marks of all students in Mathematics:", marks[:, 0])
print()

print("Average marks in each subject:", np.mean(marks, axis=0))
print()

print("Highest mark in each subject:", np.max(marks, axis=0))
print()

print("Lowest mark in each subject:", np.min(marks, axis=0))
print()

student_average = np.mean(marks, axis=1)
print("Average marks of each student:", student_average)
print()

highest_student = np.argmax(student_average) + 1
print("Student with the highest average:", highest_student)
print()
print("Highest average:", student_average[highest_student - 1])