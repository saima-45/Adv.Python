class Student:

    def __init__(self, name, no, marks):
        self.name = name
        self.no = no
        self.marks = marks

    def talk(self):
        print("Hello My Name is:", self.name)
        print("My Rollno is:", self.no)
        print("My Marks are:", self.marks)
        print("Address of self:", id(self))
        print()


print(Student.__doc__)

s1 = Student("Prachi", 101, 80)
s2 = Student("Priya", 102, 90)
s3 = Student("Saima", 103, 85)

s1.talk()
s2.talk()
s3.talk()

print("Address of s1:", id(s1))
print("Address of s2:", id(s2))
print("Address of s3:", id(s3))