class Student:

    clg_name = "MSU"

    def __init__(self):
        Student.class_name = "BCA"

    def setFaculty(self):
        Student.faculty_name = "Mrs. Patel"


s = Student()

s.setFaculty()

Student.teacher_name = "Mrs. Hora"

print(Student.__dict__)

print("College Name:", Student.clg_name)
print("Class Name:", Student.class_name)
print("Faculty Name:", Student.faculty_name)
print("Teacher Name:", Student.teacher_name)

del Student.clg_name
del Student.class_name
del Student.faculty_name
del Student.teacher_name

print(Student.__dict__)