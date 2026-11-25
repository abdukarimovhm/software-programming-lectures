# Week 13 - Part 4: choices and tkinter variables
# Software Programming (IGS1931)
#
# Radiobutton (pick ONE), Checkbutton (tick or not), Spinbox (up/down arrows)
# and Scale (a slider). Make your choices, then press the button.

from tkinter import *
from tkinter import messagebox


def show():
    sizes = {1: "Small", 2: "Medium", 3: "Large"}
    text = "Size: " + sizes[x.get()] + "\n"
    text = text + "Music: " + str(music.get()) + "\n"
    text = text + "Age: " + sp.get() + "\n"           # a Spinbox gives a STRING
    text = text + "Volume: " + str(var.get())
    messagebox.showinfo("Your choices", text)


root = Tk()
root.title("Choices")
root.geometry("300x400")

# Radiobutton: all three share ONE variable, each has its own value
Label(root, text="Pick ONE size:").pack()
x = IntVar(value=1)
R1 = Radiobutton(root, text="Small", variable=x, value=1)
R1.pack()
R2 = Radiobutton(root, text="Medium", variable=x, value=2)
R2.pack()
R3 = Radiobutton(root, text="Large", variable=x, value=3)
R3.pack()

# Checkbutton: 1 when ticked, 0 when not
music = IntVar()
C1 = Checkbutton(root, text="Music", variable=music, onvalue=1, offvalue=0)
C1.pack(pady=5)

# Spinbox: wrap=True means after 30 it goes back to 0
Label(root, text="Age:").pack()
sp = Spinbox(root, from_=0, to=30, wrap=True, width=5)
sp.pack()

# Scale: a slider
var = IntVar()
scale = Scale(root, variable=var, from_=0, to=100, orient=HORIZONTAL, label="Volume")
scale.pack()

Button(root, text="Show my choices", command=show).pack(pady=10)

root.mainloop()
