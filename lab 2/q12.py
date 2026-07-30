class Example:

    x = 100

    def __init__(self):
        self.y = 200

    def instanceMethod(self):
        z = 300
        print(Example.x)
        print(self.y)
        print(z)

    @classmethod
    def classMethod(cls):
        print(cls.x)

    @staticmethod
    def staticMethod():
        print(Example.x)


e = Example()
e.instanceMethod()
Example.classMethod()
Example.staticMethod()