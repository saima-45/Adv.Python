class Car:
    
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        
    def getinfo(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)
        print("Car Color:", self.color)
        
class Employee:
    
    def __init__(self, emp_name, emp_no, car):
        self.emp_name = emp_name
        self.emp_no = emp_no
        self.car = car
        
    def empinfo(self):
        print("Employee Name:", self.emp_name)
        print("Employee Number:", self.emp_no)
        print("Car Details:")
        self.car.getinfo()
        
c = Car("Fortuner", "Legender", "Black")
e = Employee("Arsh Vahora", 2307, c)
e.empinfo()