class Department:
    a = 10
    
    def __init__(self):
        self.b = 20
        
    def m1(self):
        print("Department class method..")
        
class MSU:
    
    def __init__(self):
        self.department = Department()
        
    def m2(self):
        print("MSU has a Department")
        print("Static Variable =", self.department.a)
        print("Instance Variable =", self.department.b)
        self.department.m1()
        
m = MSU()
m.m2()