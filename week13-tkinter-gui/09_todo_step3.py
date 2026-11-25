# Week 13 - Build-along: Mini To-Do, step 3 of 5
# Software Programming (IGS1931)
#
# Step 3: don't add empty tasks, and delete the task you click on.
# Fell behind? Open the next step file: each one is complete and runs.

from tkinter import *
from tkinter import messagebox                    # NEW in step 3


def add_task():
    task = E1.get().strip()                       # NEW in step 3: .strip() removes spaces
    if task == "":                                # NEW in step 3
        messagebox.showwarning("Add", "Type a task first.")     # NEW in step 3
        return                                    # NEW in step 3
    Lb1.insert(END, task)
    E1.delete(0, END)


def delete_task():                                # NEW in step 3
    selected = Lb1.curselection()                 # NEW in step 3: a tuple, e.g. (2,) or ()
    if len(selected) == 0:                        # NEW in step 3
        messagebox.showwarning("Delete", "Click a task first.")  # NEW in step 3
        return                                    # NEW in step 3
    Lb1.delete(selected[0])                       # NEW in step 3


root = Tk()
root.title("Mini To-Do")
root.geometry("320x400")

Label(root, text="My Tasks", font=("Arial", 18, "bold")).pack(pady=10)

top_row = Frame(root)
top_row.pack()
E1 = Entry(top_row, width=22)
E1.pack(side=LEFT, padx=5)
Button(top_row, text="Add", command=add_task).pack(side=LEFT)

Lb1 = Listbox(root, width=35, height=12)
Lb1.pack(pady=10)

Button(root, text="Delete selected", command=delete_task).pack()  # NEW in step 3

root.mainloop()
