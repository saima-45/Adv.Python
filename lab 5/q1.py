from tkinter import *

def count_characters():
    text = text_box.get("1.0", END)
    count = len(text) - 1
    result_label.config(text="Number of characters: " + str(count))


root = Tk()
root.title("Character Counter")
root.geometry("400x300")

text_box = Text(root, height=10, width=40)
text_box.pack(pady=20)

count_button = Button(
    root,
    text="Count Characters",
    command=count_characters
)
count_button.pack(pady=10)


result_label = Label(
    root,
    text="Number of characters: 0",
    font=("Arial", 12)
)
result_label.pack(pady=10)

root.mainloop()