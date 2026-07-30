class Demo:

    def get_String(self):
        self.s = input("Enter String: ")

    def print_String(self):
        print(self.s.upper())


d = Demo()
d.get_String()
d.print_String()