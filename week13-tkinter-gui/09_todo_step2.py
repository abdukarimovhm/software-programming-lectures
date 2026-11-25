# Week 13 - Build-along: Mini To-Do, step 2 of 5
# Software Programming (IGS1931)
#
# Step 2: type a task, press Add, and it goes into the Listbox.
# Fell behind? Open the next step file: each one is complete and runs.

from tkinter import *


def add_task():                                   # NEW in step 2
    task = E1.get()                               # NEW in step 2
    Lb1.insert(END, task)                         # NEW in step 2: END = at the bottom
    E1.delete(0, END)                             # NEW in step 2: empty the box


root = Tk()
root.title("Mini To-Do")
root.geometry("320x400")

Label(root, text="My Tasks", font=("Arial", 18, "bold")).pack(pady=10)

top_row = Frame(root)                             # NEW in step 2: a row for the box + button
top_row.pack()                                    # NEW in step 2
E1 = Entry(top_row, width=22)                     # NEW in step 2
E1.pack(side=LEFT, padx=5)                        # NEW in step 2
Button(top_row, text="Add", command=add_task).pack(side=LEFT)    # NEW in step 2

Lb1 = Listbox(root, width=35, height=12)          # NEW in step 2
Lb1.pack(pady=10)                                 # NEW in step 2

root.mainloop()
