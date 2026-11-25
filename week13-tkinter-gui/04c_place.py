# Week 13 - Part 3c: the same login form with place()
# Software Programming (IGS1931)
#
# place() puts a widget at exact x, y pixels (0, 0 is the top-left corner).

from tkinter import *
from tkinter import messagebox


def submit():
    messagebox.showinfo("Login", "Hello, " + e1.get())


win = Tk()
win.title("Login - place")
win.geometry("400x250")

Label(win, text="Username").place(x=30, y=50)
Label(win, text="Password").place(x=30, y=90)

# TRAP: e1 = Entry(win, width=20).place(x=100, y=50) makes e1 = None,
# because place() gives back None. Make the widget first, then place it:
e1 = Entry(win, width=20)
e1.place(x=100, y=50)
e2 = Entry(win, width=20, show="*")
e2.place(x=100, y=90)

Button(win, text="Submit", fg="red", command=submit).place(x=30, y=130)

win.mainloop()
