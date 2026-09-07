from tkinter import *
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="172.21.170.10",
    user="msc",
    password="msc",
    database="msc"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS msc")
cursor.execute("USE msc") 

cursor.execute("""
    CREATE TABLE student (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        course VARCHAR(100),
        semester INT
    )
""")

conn.commit()


def save_data():
    sid = entry_id.get()
    name = entry_name.get()
    course = entry_course.get()
    semester = entry_semester.get()

    if sid == "" or name == "" or course == "" or semester == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        sql = """
            INSERT INTO student (id, name, course, semester)
            VALUES (%s, %s, %s, %s)
        """

        values = (sid, name, course, semester)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Inserted in database successfully"
        )

        entry_id.delete(0, END)
        entry_name.delete(0, END)
        entry_course.delete(0, END)
        entry_semester.delete(0, END)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


root = Tk()
root.title("Student Registration Form")
root.geometry("350x300")

Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(root)
entry_id.grid(row=0, column=1)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
entry_name = Entry(root)
entry_name.grid(row=1, column=1)

Label(root, text="Course").grid(row=2, column=0, padx=10, pady=10)
entry_course = Entry(root)
entry_course.grid(row=2, column=1)

Label(root, text="Semester").grid(row=3, column=0, padx=10, pady=10)
entry_semester = Entry(root)
entry_semester.grid(row=3, column=1)

Button(
    root,
    text="Save",
    command=save_data
).grid(row=4, column=1, pady=20)

root.mainloop()

conn.close()