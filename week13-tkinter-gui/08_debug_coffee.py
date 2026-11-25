# Week 13 - Activity 2: debug the Coffee Shop app
# Software Programming (IGS1931)
#
# What the app SHOULD do:
#   - Pick ONE size: Small $3, Medium $4, Large $5
#   - Tick "Extra shot" to add $1 to every cup
#   - Choose how many cups (1 to 10)
#   - Press "Order" to see the total
#   Example: 2 cups, Medium, with an extra shot -> (4 + 1) * 2 = $10
#
# This file has 5 BUGS. Some crash the program, some only give wrong results.
# Work in pairs. Fix one bug, run again, repeat. Write "# FIXED" next to each fix.

from tkinter import *

prices = {1: 3, 2: 4, 3: 5}


def show_total():
    price = prices[size.get()]
    if extra.get == 1:
        price = price + 1
    qty = spin.get()
    total = price * qty
    total_label.config(text="Total: $" + str(total))


root = Tk()
root.title("Coffee Shop")
root.geometry("260x300")

Label(root, text="Size:", font=("Arial", 12, "bold")).pack()
size = IntVar(value=1)
Radiobutton(root, text="Small  $3", variable=size, value=1).pack()
Radiobutton(root, text="Medium $4", variable=size, value=1).pack()
Radiobutton(root, text="Large  $5", variable=size, value=1).pack()

extra = IntVar()
Checkbutton(root, text="Extra shot +$1", variable=extra).pack(pady=5)

Label(root, text="Cups:").pack()
spin = Spinbox(root, from_=1, to=10, width=5)
spin.pack()

total_label = Label(root, text="Total: $0", font=("Arial", 14))
total_label.grid(row=7, column=0)

Button(root, text="Order", command=show_total()).pack(pady=10)

root.mainloop()
