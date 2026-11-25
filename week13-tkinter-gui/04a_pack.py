# Week 13 - Part 3a: a login form with pack()
# Software Programming (IGS1931)
#
# pack() puts widgets one after another (from the TOP by default).
# Compare this window with 04b_grid.py and 04c_place.py.

from tkinter import *

win = Tk()
win.title("Login - pack")
win.geometry("300x200")

Label(win, text="Username").pack()
Entry(win, width=20).pack()
Label(win, text="Password").pack()
Entry(win, width=20, show="*").pack()            # show="*" hides the password
Button(win, text="Submit", fg="red").pack(pady=10)

win.mainloop()
