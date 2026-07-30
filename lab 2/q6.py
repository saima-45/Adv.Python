class Dog:

    legs = 4

    @classmethod
    def walk(cls, animal):
        print(animal, "walks with", cls.legs, "legs")


Dog.walk("Dog")
Dog.walk("Cat")
Dog.walk("Cow")