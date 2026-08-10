class Book:
    def __init__(self, pages):
        self.pages = pages
        
book1 = Book(120)
book2 = Book(250)
book3 = Book(180)
book4 = Book(300)

total_pages = book1.pages + book2.pages + book3.pages + book4.pages

print("Book 1 Pages =", book1.pages)
print("Book 2 Pages =", book2.pages)
print("Book 3 Pages =", book3.pages)
print("Book 4 Pages =", book4.pages)
print("Total Pages =", total_pages)
