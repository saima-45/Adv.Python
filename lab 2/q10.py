class MathOperation:

    @staticmethod
    def sum(a, b):
        print("Sum:", a + b)

    @staticmethod
    def product(a, b):
        print("Product:", a * b)

    @staticmethod
    def average(a, b):
        print("Average:", (a + b) / 2)


MathOperation.sum(10, 20)
MathOperation.product(10, 20)
MathOperation.average(10, 20)