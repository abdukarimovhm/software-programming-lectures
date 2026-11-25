# Week 13 - Build-along: Mini To-Do, step 5 of 5
# Software Programming (IGS1931)
#
# Step 5: a counter that always shows how many tasks are left.
# This small app already has 4 of the 5 final-project parts:
# a Tkinter GUI, functions, file operations and data management.

import os
from tkinter import *
from tkinter import messagebox

FILE = "tasks.txt"


def save_tasks():
    with open(FILE, "w") as f:
        for task in Lb1.get(0, END):
            f.write(task + "\n")


def load_tasks():
    if not os.path.exists(FILE):
        return
    with open(FILE, "r") as f:
        for line in f:
            Lb1.insert(END, line.strip())


def update_count():                               # NEW in step 5
    count.set(str(Lb1.size()) + " tasks left")    # NEW in step 5: the Label changes by itself


def add_task():
    task = E1.get().strip()
    if task == "":
        messagebox.showwarning("Add", "Type a task first.")
        return
    Lb1.insert(END, task)
    E1.delete(0, END)
    save_tasks()
    update_count()                                # NEW in step 5


def delete_task():
    selected = Lb1.curselection()
    if len(selected) == 0:
        messagebox.showwarning("Delete", "Click a task first.")
        return
    Lb1.delete(selected[0])
    save_tasks()
    update_count()                                # NEW in step 5


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

Button(root, text="Delete selected", command=delete_task).pack()

count = StringVar()                               # NEW in step 5
Label(root, textvariable=count, fg="gray").pack(pady=5)    # NEW in step 5

load_tasks()
update_count()                                    # NEW in step 5

root.mainloop()
