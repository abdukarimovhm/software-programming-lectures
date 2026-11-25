# Week 13 - Activity 1: predict the window
# Software Programming (IGS1931)
#
# Work in pairs. For each snippet:
#   1. Read the code and DRAW the window on paper.
#   2. Then set SNIPPET to that letter and run the file to check.

SNIPPET = "A"          # change to "B", then "C"

from tkinter import *

top = Tk()
top.title("Snippet " + SNIPPET)

if SNIPPET == "A":
    # Question: where do Green and red end up?
    top.geometry("200x200")
    a = Button(top, text="yellow", bg="yellow")
    b = Button(top, text="Blue", bg="lightblue", pady=30)
    c = Button(top, text="Green", bg="lightgreen", pady=30)
    d = Button(top, text="red", bg="pink", pady=20)
    a.pack(side=LEFT)
    b.pack(side=RIGHT)
    c.pack(side=TOP)
    d.pack(side=BOTTOM)

elif SNIPPET == "B":
    # Question: rows 2, 3 and 4 are empty. Is there a gap above OK?
    Label(top, text="Position 1", width=20).grid(row=0, column=0)
    Label(top, text="Position 2", width=30).grid(row=0, column=1)
    Label(top, text="Position 3").grid(row=1, column=0)
    Label(top, text="Position 4").grid(row=1, column=1)
    Button(top, text="OK").grid(row=5, column=1)

elif SNIPPET == "C":
    # Question: how many labels can you see?
    top.geometry("250x200")
    Label(top, text="IGS1931", bg="pink").place(x=10, y=10)
    Label(top, text="x=60, y=40", bg="black", fg="white").place(x=60, y=40)
    Label(top, text="x=100, y=80", bg="pink").place(x=100, y=80)
    Label(top, text="Where am I?", bg="yellow").place(x=300, y=120)

top.mainloop()
