class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __mul__(self, other):
        return self.salary * other.days
    
class WorkingDays:

    def __init__(self, days):
        self.days = days
        
e = Employee("Priti", 1000)
w = WorkingDays(26)

print("Monthly Salary:", e * w)