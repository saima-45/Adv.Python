class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eatanddrink(self):
        print("Eat biryani and drink Sprite")
        
        
class Employee(Person):
    
    def __init__(self, name, age, emp_no, emp_salary):
        super().__init__(name, age)
        self.emp_no = emp_no
        self.emp_salary = emp_salary
        
    def empinfo(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee Number:", self.emp_no)
        print("Employee Salary:", self.emp_salary)
        
p = Person("Arsh", 19)
print()
p.eatanddrink()


e = Employee("Arsh", 19, 2307, 100000)
e.empinfo()