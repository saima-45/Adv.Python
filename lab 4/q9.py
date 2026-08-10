from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x520")
root.resizable(False, False)

expression = ""
equation = StringVar()


def press(value):
    global expression
    expression += str(value)
    equation.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def key_press(event):
    global expression

    if event.char in "0123456789+-*/.":
        press(event.char)

    elif event.keysym == "Return":
        equal()

    elif event.keysym == "BackSpace":
        expression = expression[:-1]
        equation.set(expression)

    elif event.keysym == "Escape":
        clear()


display = Entry(root,textvariable=equation,font=("Arial", 24),justify="right",bd=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=12)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root,text=text,font=("Arial", 16),width=5,height=2,command=equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root,text=text,font=("Arial", 16),width=5,height=2,command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

Button(root,text="Clear",font=("Arial", 16, "bold"),bg="orange",width=26,command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.bind("<Key>", key_press)
display.focus_set()

root.mainloop()