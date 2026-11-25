# Week 13 - Warm-up: a tiny paint app
# Software Programming (IGS1931)
#
# Run it (IDLE: F5), pick a colour and drag the mouse on the white area.
# Don't worry about every line yet: by the end of today you can read all of it.

from tkinter import *


def paint(event):
    r = size.get()                      # brush size from the Scale
    x = event.x                         # where the mouse is now
    y = event.y
    C.create_oval(x - r, y - r, x + r, y + r, fill=colour.get(), outline=colour.get())
    status.config(text="Drawing at x=" + str(x) + ", y=" + str(y))


def clear():
    C.delete("all")
    status.config(text="Canvas cleared")


root = Tk()
root.title("Mini Paint")
root.resizable(False, False)

# Top bar: colours, brush size and a Clear button
bar = Frame(root, pady=5)
bar.pack(side=TOP, fill=X)

colour = StringVar(value="black")
for name in ["black", "red", "green", "blue", "orange"]:
    Radiobutton(bar, text=name, variable=colour, value=name,
                indicatoron=0, width=7, fg=name).pack(side=LEFT, padx=2)

size = IntVar(value=5)
Scale(bar, from_=1, to=20, orient=HORIZONTAL, variable=size,
      label="brush").pack(side=LEFT, padx=10)

Button(bar, text="Clear", command=clear).pack(side=RIGHT, padx=5)

# The drawing area
C = Canvas(root, width=600, height=400, bg="white")
C.pack()
C.bind("<B1-Motion>", paint)            # B1-Motion = move the mouse with the left button held down

status = Label(root, text="Hold the left mouse button and drag", anchor=W)
status.pack(fill=X)

root.mainloop()
