# Week 13 - Step 0: does tkinter work on this PC?
# Software Programming (IGS1931)
#
# Run it: open this file in IDLE and press F5.
# You should see a small window that says "tkinter works!".
# Close the window to finish.

import tkinter
from tkinter import *

print("tkinter version:", tkinter.TkVersion)

root = Tk()
root.title("Check")
root.geometry("260x100")

Label(root, text="tkinter works!", font=("Arial", 16)).pack(pady=30)

root.mainloop()
