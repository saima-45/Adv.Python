class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(self.name, self.roll, self.marks)

    def grade(self):
        if self.marks >= 75:
            print("Grade A")
        elif self.marks >= 60:
            print("Grade B")
        elif self.marks >= 40:
            print("Grade C")
        else:
            print("Fail")


s = Student("Saima", 101, 80)
s.display()
s.grade()