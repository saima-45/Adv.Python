class Employee:

    def __init__(self,name,dept,salary):
        self.emp_name = name
        self.emp_dept = dept
        self.emp_salary = salary

    def display(self):
        print("Name:", self.emp_name)
        print("Department:", self.emp_dept)
        print("Salary:", self.emp_salary)


class UpdateEmp:
    
    def updateinfo(self, emp):
        emp.emp_dept = "HR"
        emp.emp_salary = 50000
        
e = Employee("Saima", "IT", 40000)
e.display()

u = UpdateEmp()
u.updateinfo(e)

e.display()