class Employee:

    def __init__(self):
        self.emp_no = 101
        print("Constructor Called")

    def setName(self):
        self.emp_name = "Saima"

    def deleteName(self):
        del self.emp_name


e = Employee()

e.setName()

e.emp_salary = 50000

print(e.__dict__)

print("Employee No:", e.emp_no)
print("Employee Name:", e.emp_name)
print("Employee Salary:", e.emp_salary)

e.deleteName()

del e.emp_salary

print(e.__dict__)


class Demo:

    def __init__(self):
        print("First Constructor")

    def __init__(self, x):
        print("Second Constructor:", x)

    def __init__(self, x, y):
        print("Third Constructor:", x, y)


d = Demo(10, 20)