class Engine:
    a = 100
    
    def __init__(self):
        self.b = 200
        
    def m1(self):
        print("This is Engine class method...")
        
class Car:
    
    def __init__(self):
        self.engine = Engine()
        
    def m2(self):
        print("Static Variable a:", self.engine.a)
        print("Instance Variable b:", self.engine.b)
        self.engine.m1()
        
c = Car()
c.m2()