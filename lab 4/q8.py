from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()
root.title("Pizza Slice Shop")
root.geometry("400x500")

Label(root, text="Order Your Pizza", font=("Arial", 18, "bold")).pack(pady=10)

size = StringVar()
size.set("Medium")

price = {
    "Small": 8,
    "Medium": 11,
    "Large": 14
}

frame1 = LabelFrame(root, text="Choose Size", padx=10, pady=10)
frame1.pack(fill="x", padx=20)

Radiobutton(frame1, text="Small ($8)", variable=size, value="Small").pack(anchor="w")
Radiobutton(frame1, text="Medium ($11)", variable=size, value="Medium").pack(anchor="w")
Radiobutton(frame1, text="Large ($14)", variable=size, value="Large").pack(anchor="w")

frame2 = LabelFrame(root, text="Add Toppings (+ $1 each)", padx=10, pady=10)
frame2.pack(fill="x", padx=20, pady=10)

pep = IntVar()
mush = IntVar()
onion = IntVar()
cheese = IntVar()
olive = IntVar()

Checkbutton(frame2, text="Pepperoni", variable=pep).pack(anchor="w")
Checkbutton(frame2, text="Mushrooms", variable=mush).pack(anchor="w")
Checkbutton(frame2, text="Onions", variable=onion).pack(anchor="w")
Checkbutton(frame2, text="Extra Cheese", variable=cheese).pack(anchor="w")
Checkbutton(frame2, text="Olives", variable=olive).pack(anchor="w")

def bill():
    total = price[size.get()]
    toppings= pep.get() + mush.get() + onion.get() + cheese.get() + olive.get()
    total += toppings * 1
    messagebox.showinfo("Total Bill", f"Your total bill is: ${total}")
    
Button(root, text="Place Order", font=("Arial", 14, "bold"),bg="lightblue", command=bill).pack(pady=20)

root.mainloop()