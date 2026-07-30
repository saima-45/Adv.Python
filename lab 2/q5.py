class Bank:

    def __init__(self, name, bank, amount):
        self.name = name
        self.bank = bank
        self.amount = amount

    def deposit(self, amt):
        self.amount += amt

    def withdraw(self, amt):
        if amt <= self.amount:
            self.amount -= amt
        else:
            print("Insufficient Balance")

    def display(self):
        print("Customer:", self.name)
        print("Bank:", self.bank)
        print("Balance:", self.amount)


b = Bank("Saima", "Axis Bank", 5000)

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Display\n4.Exit")
    ch = int(input("Enter Choice: "))

    if ch == 1:
        amt = int(input("Enter Amount: "))
        b.deposit(amt)
    elif ch == 2:
        amt = int(input("Enter Amount: "))
        b.withdraw(amt)
    elif ch == 3:
        b.display()
    else:
        break