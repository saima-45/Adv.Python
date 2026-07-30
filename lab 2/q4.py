class InvoiceItem:

    def __init__(self, id, desc, qty, price):
        self.id = id
        self.desc = desc
        self.qty = qty
        self.price = price

    def getTotal(self):
        return self.qty * self.price


i = InvoiceItem(101, "Pen", 10, 20)
print("Total Invoice:", i.getTotal())