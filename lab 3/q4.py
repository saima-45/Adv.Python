class Human:

    class Head:

        def talk(self):
            print("Talking")
            
    class Brain:

        def think(self):
            print("Thinking")
            
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print("Name:", self.name)
        
h = Human("Priti")
h.display()

head = Human.Head()
brain = Human.Brain()

head.talk()
brain.think()
