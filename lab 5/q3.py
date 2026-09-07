from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Student Survey Form")
root.geometry("500x500")


Label(
    root,
    text="Question 1: How do you rate Python?",
    font=("Arial", 12, "bold")
).pack(pady=10)

python_rating = StringVar()
python_rating.set("Good")

Radiobutton(
    root,
    text="Excellent",
    variable=python_rating,
    value="Excellent"
).pack()

Radiobutton(
    root,
    text="Good",
    variable=python_rating,
    value="Good"
).pack()

Radiobutton(
    root,
    text="Average",
    variable=python_rating,
    value="Average"
).pack()

Radiobutton(
    root,
    text="Poor",
    variable=python_rating,
    value="Poor"
).pack()


Label(
    root,
    text="Question 2: Which topics do you like?",
    font=("Arial", 12, "bold")
).pack(pady=10)

python_var = IntVar()
tkinter_var = IntVar()
database_var = IntVar()

Checkbutton(
    root,
    text="Python",
    variable=python_var
).pack()

Checkbutton(
    root,
    text="Tkinter",
    variable=tkinter_var
).pack()

Checkbutton(
    root,
    text="Database",
    variable=database_var
).pack()


Label(
    root,
    text="Question 3: Which semester are you in?",
    font=("Arial", 12, "bold")
).pack(pady=10)

semester = ttk.Combobox(
    root,
    values=["1st Semester", "2nd Semester", "3rd Semester",
            "4th Semester", "5th Semester", "6th Semester"]
)

semester.pack()
semester.current(0)


def show_answers():

    rating = python_rating.get()

    topics = []

    if python_var.get() == 1:
        topics.append("Python")

    if tkinter_var.get() == 1:
        topics.append("Tkinter")

    if database_var.get() == 1:
        topics.append("Database")

    semester_answer = semester.get()

    if len(topics) == 0:
        topics.append("No topic selected")

    messagebox.showinfo(
        "Survey Answers",
        "Question 1:\nPython Rating: " + rating +
        "\n\nQuestion 2:\nTopics: " + ", ".join(topics) +
        "\n\nQuestion 3:\nSemester: " + semester_answer
    )


Button(
    root,
    text="Submit",
    command=show_answers,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=25)


root.mainloop()