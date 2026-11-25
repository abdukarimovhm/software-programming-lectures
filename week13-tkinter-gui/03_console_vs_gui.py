# Week 13 - Part 2: the same program, console vs window
# Software Programming (IGS1931)
#
# Version 1 asks one question in the Shell. Version 2 is a window:
# Label (text), Entry (a box to type in) and Button (runs a function).


from tkinter import *


# ---------- Version 1: console ----------
def tip_console():
    bill = float(input("Bill amount: "))
    print("Tip (15%):", round(bill * 0.15, 2))


# tip_console()        # TRY 1: remove the # and run. Then put the # back.


# ---------- Version 2: window ----------
def calculate():
    bill = float(E1.get())             # .get() gives a STRING, so we use float(...)
    tip = round(bill * 0.15, 2)
    lbl.config(text="Tip (15%): " + str(tip))


window = Tk()
window.title("Tip Calculator")
window.geometry("300x150")

L1 = Label(window, text="Bill amount:")
L1.pack()

E1 = Entry(window, bd=5)
E1.pack()

btn = Button(window, text="Calculate", fg="blue", command=calculate)     # no () after calculate
# btn = Button(window, text="Calculate", fg="blue", command=calculate())  # TRY 2: use this line instead
btn.pack()

lbl = Label(window, text="Tip (15%): ?", font=("Arial", 14))
lbl.pack()

window.mainloop()
