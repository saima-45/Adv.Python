class Person:

    @staticmethod
    def isAdult(age):
        if age >= 18:
            print("Adult")
        else:
            print("Not Adult")


Person.isAdult(20)
Person.isAdult(15)