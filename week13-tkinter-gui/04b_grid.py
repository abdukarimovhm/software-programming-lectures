# Week 13 - Part 3b: the same login form with grid()
# Software Programming (IGS1931)
#
# grid() is a table: every widget gets a row and a column.
# The labels line up in column 0 and the boxes in column 1.

from tkinter import *

win = Tk()
win.title("Login - grid")
win.geometry("300x200")

Label(win, text="Username").grid(row=0, column=0, padx=5, pady=5)
Entry(win, width=20).grid(row=0, column=1)
Label(win, text="Password").grid(row=1, column=0, padx=5, pady=5)
Entry(win, width=20, show="*").grid(row=1, column=1)
Button(win, text="Submit", fg="red").grid(row=2, column=1, pady=10)

# TRY: remove the # below and run. What happens? Why?
# Label(win, text="Welcome!").pack()

win.mainloop()
