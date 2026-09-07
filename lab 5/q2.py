from tkinter import *
from tkinter import messagebox

def submit_feedback():
    name = entry_name.get()
    feedback = text_feedback.get("1.0", END).strip()

    if name == "" or feedback == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Feedback",
            "Thank you " + name + " for your feedback!"
        )

root = Tk()
root.title("Student Feedback Form")
root.geometry("400x350")

Label(root, text="Student Name").pack(pady=10)

entry_name = Entry(root, width=35)
entry_name.pack()

Label(root, text="Enter Your Feedback").pack(pady=10)

text_feedback = Text(root, width=40, height=8)
text_feedback.pack()

Button(
    root,
    text="Submit Feedback",
    command=submit_feedback,
    bg="green",
    fg="white"
).pack(pady=20)

root.mainloop()