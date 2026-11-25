# Week 13 - Build-along: Mini To-Do, step 4 of 5
# Software Programming (IGS1931)
#
# Step 4: save the tasks to tasks.txt, and load them when the app starts.
# Close the app, run it again: your tasks are still there.
# Fell behind? Open the next step file: each one is complete and runs.

import os                                         # NEW in step 4
from tkinter import *
from tkinter import messagebox

FILE = "tasks.txt"                                # NEW in step 4: next to this .py file (in IDLE)


def save_tasks():                                 # NEW in step 4
    with open(FILE, "w") as f:                    # NEW in step 4
        for task in Lb1.get(0, END):              # NEW in step 4: every task in the Listbox
            f.write(task + "\n")                  # NEW in step 4


def load_tasks():                                 # NEW in step 4
    if not os.path.exists(FILE):                  # NEW in step 4: first run, no file yet
        return                                    # NEW in step 4
    with open(FILE, "r") as f:                    # NEW in step 4
        for line in f:                            # NEW in step 4
            Lb1.insert(END, line.strip())         # NEW in step 4


def add_task():
    task = E1.get().strip()
    if task == "":
        messagebox.showwarning("Add", "Type a task first.")
        return
    Lb1.insert(END, task)
    E1.delete(0, END)
    save_tasks()                                  # NEW in step 4


def delete_task():
    selected = Lb1.curselection()
    if len(selected) == 0:
        messagebox.showwarning("Delete", "Click a task first.")
        return
    Lb1.delete(selected[0])
    save_tasks()                                  # NEW in step 4


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

load_tasks()                                      # NEW in step 4

root.mainloop()
